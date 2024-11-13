# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdError
from pyavd._utils import default, get, get_ip_from_ip_prefix, get_item, strip_empties_from_dict
from pyavd.api.interface_descriptions import InterfaceDescriptionData
from pyavd.j2filters import natural_sort, range_expand

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigUnderlay


class UtilsMixin:
    """
    Mixin Class with internal functions.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def _avd_peers(self: AvdStructuredConfigUnderlay) -> list:
        """
        Returns a list of peers.

        This cannot be loaded in shared_utils since it will not be calculated until EosDesignsFacts has been rendered
        and shared_utils are shared between EosDesignsFacts and AvdStructuredConfig classes like this one.
        """
        return natural_sort(get(self._hostvars, f"avd_topology_peers..{self.shared_utils.hostname}", separator="..", default=[]))

    @cached_property
    def _underlay_filter_peer_as_route_maps_asns(self: AvdStructuredConfigUnderlay) -> list:
        """Filtered ASNs."""
        if not self.inputs.underlay_filter_peer_as:
            return []

        # using set comprehension with `{}` to remove duplicates and then run natural_sort to convert to list.
        return natural_sort({link["peer_bgp_as"] for link in self._underlay_links if link["type"] == "underlay_p2p"})

    @cached_property
    def _underlay_links(self: AvdStructuredConfigUnderlay) -> list:
        """Returns the list of underlay links for this device."""
        underlay_links = []
        underlay_links.extend(self._uplinks)
        if self.inputs.fabric_sflow.uplinks is not None:
            for uplink in underlay_links:
                uplink.update({"sflow": {"enable": self.inputs.fabric_sflow.uplinks}})

        uplinks_flow_tracker = self.shared_utils.get_flow_tracker(self.inputs.fabric_flow_tracking.uplinks)
        if uplinks_flow_tracker is not None:
            for uplink in underlay_links:
                uplink["flow_tracker"] = uplinks_flow_tracker

        downlinks_flow_tracker = self.shared_utils.get_flow_tracker(self.inputs.fabric_flow_tracking.downlinks)

        for peer in self._avd_peers:
            peer_facts = self.shared_utils.get_peer_facts(peer, required=True)
            for uplink in peer_facts["uplinks"]:
                if uplink["peer"] == self.shared_utils.hostname:
                    link = {
                        "interface": uplink["peer_interface"],
                        "peer": peer,
                        "peer_interface": uplink["interface"],
                        "peer_type": get(peer_facts, "type"),
                        "peer_is_deployed": peer_facts["is_deployed"],
                        "peer_bgp_as": get(peer_facts, "bgp_as"),
                        "type": get(uplink, "type", required=True),
                        "speed": get(uplink, "peer_speed", default=get(uplink, "speed")),
                        "ip_address": get(uplink, "peer_ip_address"),
                        "peer_ip_address": get(uplink, "ip_address"),
                        "prefix_length": get(uplink, "prefix_length"),
                        "channel_group_id": get(uplink, "peer_channel_group_id"),
                        "peer_channel_group_id": get(uplink, "channel_group_id"),
                        "peer_node_group": get(uplink, "node_group"),
                        "vlans": get(uplink, "vlans"),
                        "native_vlan": get(uplink, "native_vlan"),
                        "trunk_groups": get(uplink, "peer_trunk_groups"),
                        "bfd": get(uplink, "bfd"),
                        "ptp": get(uplink, "ptp"),
                        "mac_security": get(uplink, "mac_security"),
                        "short_esi": get(uplink, "peer_short_esi"),
                        "mlag": get(uplink, "peer_mlag"),
                        "underlay_multicast": get(uplink, "underlay_multicast"),
                        "ipv6_enable": get(uplink, "ipv6_enable"),
                        "sflow": {"enable": self.inputs.fabric_sflow.downlinks},
                        "flow_tracker": downlinks_flow_tracker,
                        "spanning_tree_portfast": get(uplink, "peer_spanning_tree_portfast"),
                        "structured_config": get(uplink, "structured_config"),
                    }
                    if get(peer_facts, "inband_ztp"):
                        # l2 inband ztp
                        link["inband_ztp_vlan"] = get(peer_facts, "inband_ztp_vlan")
                        link["inband_ztp_lacp_fallback_delay"] = get(peer_facts, "inband_ztp_lacp_fallback_delay")
                        # l3 inband ztp
                        link["dhcp_server"] = True

                    if (subinterfaces := get(uplink, "subinterfaces")) is not None:
                        link["subinterfaces"] = [
                            {
                                **subinterface,
                                "interface": subinterface["peer_interface"],
                                "peer_interface": subinterface["interface"],
                                "ip_address": subinterface.get("peer_ip_address"),
                                "peer_ip_address": subinterface.get("ip_address"),
                            }
                            for subinterface in subinterfaces
                        ]
                    underlay_links.append(strip_empties_from_dict(link))

        return natural_sort(underlay_links, "interface")

    @cached_property
    def _underlay_vlan_trunk_groups(self: AvdStructuredConfigUnderlay) -> list:
        """Returns a list of trunk groups to configure on the underlay link."""
        if self.inputs.enable_trunk_groups is not True:
            return []

        trunk_groups = []

        for peer in self._avd_peers:
            peer_facts = self.shared_utils.get_peer_facts(peer, required=True)
            for uplink in peer_facts["uplinks"]:
                if uplink["peer"] == self.shared_utils.hostname:
                    if (peer_trunk_groups := get(uplink, "peer_trunk_groups")) is None:
                        continue

                    trunk_groups.append(
                        {
                            "vlan_list": uplink["vlans"],
                            "trunk_groups": peer_trunk_groups,
                        },
                    )

        if trunk_groups:
            return trunk_groups

        return []

    @cached_property
    def _uplinks(self: AvdStructuredConfigUnderlay) -> list:
        return get(self._hostvars, "switch.uplinks")

    def _get_l3_interface_cfg(
        self: AvdStructuredConfigUnderlay, l3_interface: EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3InterfacesItem
    ) -> dict | None:
        """Returns structured_configuration for one L3 interface."""
        interface_description = l3_interface.description
        if not interface_description:
            interface_description = self.shared_utils.interface_descriptions.underlay_ethernet_interface(
                InterfaceDescriptionData(
                    shared_utils=self.shared_utils,
                    interface=l3_interface.name,
                    peer=l3_interface.peer,
                    peer_interface=l3_interface.peer_interface,
                    wan_carrier=l3_interface.wan_carrier,
                    wan_circuit_id=l3_interface.wan_circuit_id,
                ),
            )

        # TODO: catch if ip_address is not valid or not dhcp
        interface = {
            "name": l3_interface.name,
            "peer_type": "l3_interface",
            "peer": l3_interface.peer,
            "peer_interface": l3_interface.peer_interface,
            "ip_address": l3_interface.ip_address,
            "shutdown": not l3_interface.enabled,
            "switchport": {"enabled": False if "." not in l3_interface.name else None},
            "description": interface_description,
            "speed": l3_interface.speed,
            "service_profile": l3_interface.qos_profile,
            "access_group_in": get(self._l3_interface_acls, f"{l3_interface.name}..ipv4_acl_in..name", separator=".."),
            "access_group_out": get(self._l3_interface_acls, f"{l3_interface.name}..ipv4_acl_out..name", separator=".."),
            "eos_cli": l3_interface.raw_eos_cli,
            "struct_cfg": l3_interface.structured_config._as_dict(),
            "flow_tracker": self.shared_utils.get_flow_tracker(l3_interface.flow_tracking),
        }

        if self.inputs.fabric_sflow.l3_interfaces is not None:
            interface["sflow"] = {"enable": self.inputs.fabric_sflow.l3_interfaces}

        if "." in l3_interface.name:
            interface["encapsulation_dot1q"] = {"vlan": default(l3_interface.encapsulation_dot1q_vlan, int(l3_interface.name.split(".", maxsplit=1)[-1]))}

        if l3_interface.ip_address == "dhcp" and l3_interface.dhcp_accept_default_route:
            interface["dhcp_client_accept_default_route"] = True

        if (
            self.shared_utils.is_wan_router
            and (wan_carrier_name := l3_interface.wan_carrier) is not None
            and interface["access_group_in"] is None
            and (wan_carrier_name not in self.inputs.wan_carriers or not self.inputs.wan_carriers[wan_carrier_name].trusted)
        ):
            msg = (
                "'ipv4_acl_in' must be set on WAN interfaces where 'wan_carrier' is set, unless the carrier is configured as 'trusted' "
                f"under 'wan_carriers'. 'ipv4_acl_in' is missing on interface '{l3_interface.name}'."
            )
            raise AristaAvdError(msg)

        return strip_empties_from_dict(interface)

    def _get_l3_uplink_with_l2_as_subint(self: AvdStructuredConfigUnderlay, link: dict) -> tuple[dict, list[dict]]:
        """Return a tuple with main uplink interface, list of subinterfaces representing each SVI."""
        vlans = [int(vlan) for vlan in range_expand(link["vlans"])]

        # Main interface
        # Routed interface with no config unless there is an SVI matching the native-vlan, then it will contain the config for that SVI

        interfaces = []
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                for svi in vrf.svis:
                    # Skip any vlans not part of the link
                    if svi.id not in vlans:
                        continue

                    interfaces.append(self._get_l2_as_subint(link, svi, vrf))

        # If we have the main interface covered, we can just exclude it from the list and return as main interface.
        # Otherwise we return an almost empty dict as the main interface since it was already covered by the calling function.
        main_interface = get_item(interfaces, "name", link["interface"], default={"switchport": {"enabled": False}, "mtu": self.shared_utils.p2p_uplinks_mtu})
        main_interface.pop("description", None)

        if (mtu := main_interface.get("mtu", 1500)) != self.shared_utils.p2p_uplinks_mtu:
            msg = (
                f"MTU '{self.shared_utils.p2p_uplinks_mtu}' set for 'p2p_uplinks_mtu' conflicts with MTU '{mtu}' "
                f"set on SVI for uplink_native_vlan '{link['native_vlan']}'."
                "Either adjust the MTU on the SVI or p2p_uplinks_mtu or change/remove the uplink_native_vlan setting."
            )
            raise AristaAvdError(msg)
        return main_interface, [interface for interface in interfaces if interface["name"] != link["interface"]]

    def _get_l2_as_subint(
        self: AvdStructuredConfigUnderlay,
        link: dict,
        svi: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
    ) -> dict:
        """
        Return structured config for one subinterface representing the given SVI.

        Only supports static IPs or VRRP.
        """
        is_native = svi.id == link.get("native_vlan")
        interface_name = link["interface"] if is_native else f"{link['interface']}.{svi.id}"
        subinterface = {
            "name": interface_name,
            "peer": link["peer"],
            "peer_interface": f"{link['peer_interface']} VLAN {svi.id}",
            "peer_type": link["peer_type"],
            "description": default(svi.description, svi.name),
            "shutdown": not default(svi.enabled, False),  # noqa: FBT003
            "switchport": {"enabled": False if is_native else None},
            "encapsulation_dot1q": {"vlan": None if is_native else svi.id},
            "vrf": vrf.name if vrf.name != "default" else None,
            "ip_address": svi.ip_address,
            "ipv6_address": svi.ipv6_address,
            "ipv6_enable": svi.ipv6_enable,
            "mtu": svi.mtu if self.shared_utils.platform_settings.feature_support.per_interface_mtu else None,
            "eos_cli": svi.raw_eos_cli,
            "struct_cfg": svi.structured_config._as_dict() or None,
            "flow_tracker": link.get("flow_tracker"),
        }
        if (mtu := subinterface["mtu"]) is not None and subinterface["mtu"] > self.shared_utils.p2p_uplinks_mtu:
            msg = (
                f"MTU '{self.shared_utils.p2p_uplinks_mtu}' set for 'p2p_uplinks_mtu' must be larger or equal to MTU '{mtu}' "
                f"set on the SVI '{svi.id}'."
                "Either adjust the MTU on the SVI or p2p_uplinks_mtu."
            )
            raise AristaAvdError(msg)

        # Only set VRRPv4 if ip_address is set
        if subinterface["ip_address"] is not None:
            # TODO: in separate PR adding VRRP support for SVIs
            pass

        # Only set VRRPv6 if ipv6_address is set
        if subinterface["ipv6_address"] is not None:
            # TODO: in separate PR adding VRRP support for SVIs
            pass

        # Adding IP helpers and OSPF via a common function also used for SVIs on L3 switches.
        self.shared_utils.get_additional_svi_config(subinterface, svi, vrf)

        return strip_empties_from_dict(subinterface)

    @cached_property
    def _l3_interface_acls(self: AvdStructuredConfigUnderlay) -> dict[str, dict[str, dict]]:
        """
        Return dict of l3 interface ACLs.

        <interface_name>: {
            "ipv4_acl_in": <generated_ipv4_acl>,
            "ipv4_acl_out": <generated_ipv4_acl>,
        }

        Only contains interfaces with ACLs and only the ACLs that are set,
        so use `get(self._l3_interface_acls, f"{interface_name}.ipv4_acl_in")` to get the value.
        """
        l3_interface_acls = {}
        for l3_interface in self.shared_utils.l3_interfaces:
            ipv4_acl_in = l3_interface.ipv4_acl_in
            ipv4_acl_out = l3_interface.ipv4_acl_out
            if ipv4_acl_in is None and ipv4_acl_out is None:
                continue

            interface_ip = l3_interface.dhcp_ip if (ip_address := l3_interface.ip_address) == "dhcp" else ip_address
            if interface_ip is not None and "/" in interface_ip:
                interface_ip = get_ip_from_ip_prefix(interface_ip)

            if ipv4_acl_in is not None:
                l3_interface_acls.setdefault(l3_interface.name, {})["ipv4_acl_in"] = self.shared_utils.get_ipv4_acl(
                    name=ipv4_acl_in,
                    interface_name=l3_interface.name,
                    interface_ip=interface_ip,
                    peer_ip=l3_interface.peer_ip,
                )._as_dict()
            if ipv4_acl_out is not None:
                l3_interface_acls.setdefault(l3_interface.name, {})["ipv4_acl_out"] = self.shared_utils.get_ipv4_acl(
                    name=ipv4_acl_out,
                    interface_name=l3_interface.name,
                    interface_ip=interface_ip,
                    peer_ip=l3_interface.peer_ip,
                )._as_dict()

        return l3_interface_acls
