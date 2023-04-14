from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.filter.list_compress import list_compress
from ansible_collections.arista.avd.plugins.plugin_utils.avdfacts import AvdFacts
from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_empties_from_dict
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get


class AvdStructuredConfig(AvdFacts):
    def render(self):
        """
        Wrap class render function with a check for mlag is True
        """
        if self.shared_utils.mlag is True:
            return super().render()
        return {}

    @cached_property
    def _trunk_groups_mlag_name(self):
        return get(self.shared_utils.trunk_groups, "mlag.name", required=True)

    @cached_property
    def _trunk_groups_mlag_l3_name(self):
        return get(self.shared_utils.trunk_groups, "mlag_l3.name", required=True)

    @cached_property
    def _p2p_uplinks_mtu(self):
        return get(self._hostvars, "p2p_uplinks_mtu", required=True)

    @cached_property
    def _underlay_rfc5549(self):
        return get(self._hostvars, "underlay_rfc5549")

    @cached_property
    def _bgp_as(self):
        return get(self._hostvars, "switch.bgp_as", required=True)

    @cached_property
    def spanning_tree(self):
        if self.shared_utils.mlag_peer_l3_vlan is not None:
            vlans = [self.shared_utils.mlag_peer_vlan, self.shared_utils.mlag_peer_l3_vlan]
            return {"no_spanning_tree_vlan": list_compress(vlans)}

        return {"no_spanning_tree_vlan": self.shared_utils.mlag_peer_vlan}

    @cached_property
    def vlans(self):
        vlans = {}
        if self.shared_utils.mlag_peer_l3_vlan is not None:
            vlans[self.shared_utils.mlag_peer_l3_vlan] = {
                "tenant": "system",
                "name": "LEAF_PEER_L3",
                "trunk_groups": [self._trunk_groups_mlag_l3_name],
            }

        vlans[self.shared_utils.mlag_peer_vlan] = {
            "tenant": "system",
            "name": "MLAG_PEER",
            "trunk_groups": [self._trunk_groups_mlag_name],
        }
        return vlans

    @cached_property
    def vlan_interfaces(self) -> list | None:
        """
        Return list with VLAN Interfaces used for MLAG

        May return both the main MLAG VLAN as well as a dedicated L3 VLAN
        Can also combine L3 configuration on the main MLAG VLAN
        """

        # Create Main MLAG VLAN Interface
        main_vlan_interface_name = f"Vlan{self.shared_utils.mlag_peer_vlan}"
        main_vlan_interface = {
            "name": main_vlan_interface_name,
            "description": "MLAG_PEER",
            "shutdown": False,
            "ip_address": f"{self.shared_utils.mlag_ip}/31",
            "no_autostate": True,
            "struct_cfg": self.shared_utils.mlag_peer_vlan_structured_config,
            "mtu": self._p2p_uplinks_mtu,
        }
        if not self.shared_utils.mlag_l3:
            return [strip_empties_from_dict(main_vlan_interface)]

        # Create L3 data which will go on either a dedicated l3 vlan or the main mlag vlan
        l3_cfg = {
            "struct_cfg": get(self.shared_utils.switch_data_combined, "mlag_peer_l3_vlan_structured_config"),
        }
        if self.shared_utils.underlay_routing_protocol == "ospf":
            l3_cfg.update(
                {
                    "ospf_network_point_to_point": True,
                    "ospf_area": get(self._hostvars, "underlay_ospf_area", required=True),
                }
            )

        elif self.shared_utils.underlay_routing_protocol == "isis":
            l3_cfg.update(
                {
                    "isis_enable": self.shared_utils.isis_instance_name,
                    "isis_metric": 50,
                    "isis_network_point_to_point": True,
                }
            )

        if self.shared_utils.underlay_multicast:
            l3_cfg["pim"] = {"ipv4": {"sparse_mode": True}}

        if self._underlay_rfc5549 is True:
            l3_cfg["ipv6_enable"] = True

        # Add L3 config if the main interface is also used for L3 peering
        if self.shared_utils.mlag_peer_l3_vlan is None:
            main_vlan_interface.update(l3_cfg)
            # Applying structured config again in the case it is set on both l3vlan and main vlan
            if self.shared_utils.mlag_peer_vlan_structured_config is not None:
                main_vlan_interface["struct_cfg"] = self.shared_utils.mlag_peer_vlan_structured_config

            return [strip_empties_from_dict(main_vlan_interface)]

        # Next create l3 interface if not using the main vlan
        l3_vlan_interface_name = f"Vlan{self.shared_utils.mlag_peer_l3_vlan}"
        l3_vlan_interface = {
            "name": l3_vlan_interface_name,
            "description": "MLAG_PEER_L3_PEERING",
            "shutdown": False,
            "mtu": self._p2p_uplinks_mtu,
        }
        if self._underlay_rfc5549 is not True:
            l3_vlan_interface["ip_address"] = f"{self.shared_utils.mlag_l3_ip}/31"

        l3_vlan_interface.update(l3_cfg)

        return [
            strip_empties_from_dict(l3_vlan_interface),
            strip_empties_from_dict(main_vlan_interface),
        ]

    @cached_property
    def port_channel_interfaces(self):
        """
        Return dict with one Port Channel Interface used for MLAG Peer Link
        """

        port_channel_interface_name = f"Port-Channel{self.shared_utils.mlag_port_channel_id}"
        port_channel_interface = {
            "name": port_channel_interface_name,
            "description": self.shared_utils.interface_descriptions.mlag_port_channel_interfaces(),
            "type": "switched",
            "shutdown": False,
            "vlans": get(self.shared_utils.switch_data_combined, "mlag_peer_link_allowed_vlans", default="2-4094"),
            "mode": "trunk",
            "service_profile": get(self._hostvars, "p2p_uplinks_qos_profile"),
            "trunk_groups": [self._trunk_groups_mlag_name],
            "struct_cfg": get(self.shared_utils.switch_data_combined, "mlag_port_channel_structured_config"),
        }

        if self.shared_utils.mlag_l3 is True and self._trunk_groups_mlag_l3_name != self._trunk_groups_mlag_name:
            # Add LEAF_PEER_L3 even if we reuse the MLAG trunk group for underlay peering
            # since this trunk group is also used for overlay iBGP peerings
            # except in the case where the same trunk group name is defined.
            port_channel_interface["trunk_groups"].append(self._trunk_groups_mlag_l3_name)
            # Retain legacy order
            port_channel_interface["trunk_groups"].reverse()

        return [strip_empties_from_dict(port_channel_interface)]

    @cached_property
    def ethernet_interfaces(self):
        """
        Return dict with Ethernet Interfaces used for MLAG Peer Link
        """

        if not (mlag_interfaces := self.shared_utils.mlag_interfaces):
            return None

        ethernet_interfaces = {}
        for mlag_interface in mlag_interfaces:
            ethernet_interface = {
                "peer": self.shared_utils.mlag_peer,
                "peer_interface": mlag_interface,
                "peer_type": "mlag_peer",
                "description": self.shared_utils.interface_descriptions.mlag_ethernet_interfaces(mlag_interface),
                "type": "switched",
                "shutdown": False,
                "channel_group": {
                    "id": self.shared_utils.mlag_port_channel_id,
                    "mode": "active",
                },
                "speed": self.shared_utils.mlag_interfaces_speed,
            }

            ethernet_interfaces[mlag_interface] = ethernet_interface

        return strip_empties_from_dict(ethernet_interfaces)

    @cached_property
    def mlag_configuration(self):
        """
        Return Structured Config for MLAG Configuration
        """

        mlag_configuration = {
            "domain_id": self.shared_utils.group,
            "local_interface": f"Vlan{self.shared_utils.mlag_peer_vlan}",
            "peer_address": self.shared_utils.mlag_peer_ip,
            "peer_link": f"Port-Channel{self.shared_utils.mlag_port_channel_id}",
            "reload_delay_mlag": get(self.shared_utils.platform_settings, "reload_delay.mlag"),
            "reload_delay_non_mlag": get(self.shared_utils.platform_settings, "reload_delay.non_mlag"),
        }
        if (
            get(self.shared_utils.switch_data_combined, "mlag_dual_primary_detection", default=False) is True
            and self.shared_utils.mlag_peer_mgmt_ip is not None
            and (mgmt_interface_vrf := get(self._hostvars, "mgmt_interface_vrf")) is not None
        ):
            mlag_configuration.update(
                {
                    "peer_address_heartbeat": {
                        "peer_ip": self.shared_utils.mlag_peer_mgmt_ip,
                        "vrf": mgmt_interface_vrf,
                    },
                    "dual_primary_detection_delay": 5,
                }
            )

        return strip_empties_from_dict(mlag_configuration)

    @cached_property
    def route_maps(self):
        """
        Return dict with one route-map
        Origin Incomplete for MLAG iBGP learned routes

        TODO: Partially duplicated in network_services. Should be moved to a common class
        """

        if not (self.shared_utils.mlag_l3 is True and self.shared_utils.mlag_ibgp_origin_incomplete is True and self.shared_utils.underlay_bgp):
            return None

        return [
            {
                "name": "RM-MLAG-PEER-IN",
                "sequence_numbers": [
                    {
                        "sequence": 10,
                        "type": "permit",
                        "set": ["origin incomplete"],
                        "description": "Make routes learned over MLAG Peer-link less preferred on spines to ensure optimal routing",
                    }
                ],
            }
        ]

    @cached_property
    def router_bgp(self):
        """
        Return structured config for router bgp

        Peer group and underlay MLAG iBGP peering is created only for BGP underlay.
        """

        if not (self.shared_utils.mlag_l3 is True and self.shared_utils.underlay_bgp):
            return None

        # MLAG Peer group
        peer_group_name = self.shared_utils.bgp_peer_groups["mlag_ipv4_underlay_peer"]["name"]
        router_bgp = self._router_bgp_mlag_peer_group()

        # Underlay MLAG peering
        if not self.shared_utils.underlay_bgp:
            return strip_empties_from_dict(router_bgp)

        if self._underlay_rfc5549 is True:
            vlan = default(self.shared_utils.mlag_peer_l3_vlan, self.shared_utils.mlag_peer_vlan)
            neighbor_interface_name = f"Vlan{vlan}"
            router_bgp["neighbor_interfaces"] = [
                {
                    "name": neighbor_interface_name,
                    "peer_group": peer_group_name,
                    "remote_as": self._bgp_as,
                    "description": self.shared_utils.mlag_peer,
                }
            ]

        else:
            neighbor_ip = default(self.shared_utils.mlag_peer_l3_ip, self.shared_utils.mlag_peer_ip)
            router_bgp["neighbors"] = [
                {
                    "ip_address": neighbor_ip,
                    "peer_group": peer_group_name,
                    "description": self.shared_utils.mlag_peer,
                }
            ]

        return strip_empties_from_dict(router_bgp)

    def _router_bgp_mlag_peer_group(self) -> dict:
        """
        Return a partial router_bgp structured_config covering the MLAG peer_group
        and associated address_family activations

        TODO: Duplicated in network_services. Should be moved to a common class
        """
        peer_group_name = self.shared_utils.bgp_peer_groups["mlag_ipv4_underlay_peer"]["name"]
        router_bgp = {}
        peer_group = {
            "name": peer_group_name,
            "type": "ipv4",
            "remote_as": self._bgp_as,
            "next_hop_self": True,
            "description": self.shared_utils.mlag_peer,
            "password": self.shared_utils.bgp_peer_groups["mlag_ipv4_underlay_peer"]["password"],
            "maximum_routes": 12000,
            "send_community": "all",
            "struct_cfg": self.shared_utils.bgp_peer_groups["mlag_ipv4_underlay_peer"]["structured_config"],
        }
        if self.shared_utils.mlag_ibgp_origin_incomplete is True:
            peer_group["route_map_in"] = "RM-MLAG-PEER-IN"

        router_bgp["peer_groups"] = [peer_group]

        if self.shared_utils.underlay_ipv6:
            router_bgp["address_family_ipv6"] = {
                "peer_groups": [
                    {
                        "name": peer_group_name,
                        "activate": True,
                    }
                ]
            }

        address_family_ipv4_peer_group = {"name": peer_group_name, "activate": True}
        if self._underlay_rfc5549 is True:
            address_family_ipv4_peer_group["next_hop"] = {"address_family_ipv6_originate": True}

        router_bgp["address_family_ipv4"] = {"peer_groups": [address_family_ipv4_peer_group]}

        return router_bgp
