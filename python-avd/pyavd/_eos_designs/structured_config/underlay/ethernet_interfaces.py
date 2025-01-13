# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._errors import AristaAvdError, AristaAvdMissingVariableError
from pyavd._utils import append_if_not_duplicate, get, strip_null_from_data
from pyavd.api.interface_descriptions import InterfaceDescriptionData
from pyavd.j2filters import encrypt, natural_sort

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlay


class EthernetInterfacesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def ethernet_interfaces(self: AvdStructuredConfigUnderlay) -> list | None:
        """Return structured config for ethernet_interfaces."""
        ethernet_interfaces = []

        for link in self._underlay_links:
            # common values
            description = self.shared_utils.interface_descriptions.underlay_ethernet_interface(
                InterfaceDescriptionData(
                    shared_utils=self.shared_utils,
                    interface=link["interface"],
                    link_type=link["type"],
                    peer=link["peer"],
                    peer_interface=link["peer_interface"],
                ),
            )
            ethernet_interface = {
                "name": link["interface"],
                "peer": link["peer"],
                "peer_interface": link["peer_interface"],
                "peer_type": link["peer_type"],
                "description": description,
                "speed": link.get("speed"),
                "shutdown": self.inputs.shutdown_interfaces_towards_undeployed_peers and not link["peer_is_deployed"],
            }

            # L3 interface
            # Used for p2p uplinks as well as main interface for p2p-vrfs.
            if link["type"] == "underlay_p2p":
                ethernet_interface.update(
                    {
                        "mtu": self.shared_utils.p2p_uplinks_mtu,
                        "service_profile": self.inputs.p2p_uplinks_qos_profile,
                        "mac_security": link.get("mac_security"),
                        "switchport": {"enabled": False},
                        "ipv6_enable": link.get("ipv6_enable"),
                        "link_tracking_groups": link.get("link_tracking_groups"),
                        "sflow": link.get("sflow"),
                        "flow_tracker": link.get("flow_tracker"),
                    },
                )

                # PTP
                if get(link, "ptp.enable") is True:
                    ptp_config = {}

                    # Apply PTP profile config if using the new ptp config style
                    if self.shared_utils.ptp_enabled:
                        ptp_config.update(self.shared_utils.ptp_profile._as_dict(include_default_values=True))

                    ptp_config["enable"] = True
                    ptp_config.pop("profile", None)
                    ethernet_interface["ptp"] = ptp_config

                # MPLS
                if self.shared_utils.underlay_mpls is True:
                    mpls_dict = {"ip": True}
                    if self.shared_utils.underlay_ldp is True:
                        mpls_dict["ldp"] = {
                            "interface": True,
                            "igp_sync": True,
                        }

                    ethernet_interface["mpls"] = mpls_dict

                # IP address
                if link.get("ip_address") is not None:
                    if "unnumbered" in link["ip_address"].lower():
                        ethernet_interface["ip_address"] = link["ip_address"]
                    else:
                        ethernet_interface["ip_address"] = f"{link['ip_address']}/{link['prefix_length']}"

                if self.shared_utils.underlay_ospf is True:
                    ethernet_interface["ospf_network_point_to_point"] = True
                    ethernet_interface["ospf_area"] = self.inputs.underlay_ospf_area
                    ospf_authentication = self.inputs.underlay_ospf_authentication.enabled
                    ospf_message_digest_keys = self.inputs.underlay_ospf_authentication.message_digest_keys
                    if ospf_authentication and ospf_message_digest_keys:
                        ospf_keys = [
                            {
                                "id": ospf_key.id,
                                "hash_algorithm": ospf_key.hash_algorithm,
                                "key": encrypt(
                                    ospf_key.key,
                                    passwd_type="ospf_message_digest",  # NOSONAR # noqa: S106
                                    key=ethernet_interface["name"],
                                    hash_algorithm=ospf_key.hash_algorithm,
                                    key_id=ospf_key.id,
                                ),
                            }
                            for ospf_key in ospf_message_digest_keys
                        ]

                        if len(ospf_keys) > 0:
                            ethernet_interface["ospf_authentication"] = "message-digest"
                            ethernet_interface["ospf_message_digest_keys"] = ospf_keys
                        else:
                            msg = "'underlay_ospf_authentication.enabled' is True but no message-digest keys with both key and ID are defined."
                            raise AristaAvdError(msg)

                if self.shared_utils.underlay_isis is True:
                    ethernet_interface.update(
                        {
                            "isis_enable": self.shared_utils.isis_instance_name,
                            "isis_bfd": self.inputs.underlay_isis_bfd or None,
                            "isis_metric": self.inputs.isis_default_metric,
                            "isis_network_point_to_point": True,
                            "isis_circuit_type": self.inputs.isis_default_circuit_type,
                        },
                    )
                    if self.inputs.underlay_isis_authentication_mode:
                        ethernet_interface.setdefault("isis_authentication", {}).setdefault("both", {})["mode"] = self.inputs.underlay_isis_authentication_mode

                    if self.inputs.underlay_isis_authentication_key is not None:
                        ethernet_interface.setdefault("isis_authentication", {}).setdefault("both", {}).update(
                            {
                                "key": self.inputs.underlay_isis_authentication_key,
                                "key_type": "7",
                            }
                        )

                if link.get("underlay_multicast") is True:
                    ethernet_interface["pim"] = {"ipv4": {"sparse_mode": True}}

                # DHCP server settings (primarily used for ZTP)
                if link.get("ip_address") is not None and "unnumbered" not in link["ip_address"].lower() and link.get("dhcp_server"):
                    ethernet_interface["dhcp_server_ipv4"] = True

                # Structured Config
                if structured_config := link.get("structured_config"):
                    self.custom_structured_configs.nested.ethernet_interfaces.obtain(link["interface"])._deepmerge(
                        EosCliConfigGen.EthernetInterfacesItem._from_dict(structured_config), list_merge=self.custom_structured_configs.list_merge_strategy
                    )

            # L2 interface
            elif link["type"] == "underlay_l2":
                if self.shared_utils.network_services_l2_as_subint:
                    # Render L3 subinterfaces for each SVI.
                    # The peer will just render a regular trunk.
                    main_interface, ethernet_subinterfaces = self._get_l3_uplink_with_l2_as_subint(link)
                    ethernet_interface.update(main_interface)

                elif (channel_group_id := link.get("channel_group_id")) is not None:
                    # Render port-channel member
                    ethernet_interface.update(
                        {
                            "channel_group": {
                                "id": int(channel_group_id),
                                "mode": "active",
                            },
                        },
                    )
                    if get(link, "inband_ztp_vlan"):
                        ethernet_interface.update({"switchport": {"enabled": True, "mode": "access", "access_vlan": link["inband_ztp_vlan"]}})
                else:
                    # Render trunk interface
                    ethernet_interface.update(
                        {
                            "switchport": {
                                "enabled": True,
                                "mode": "trunk",
                                "trunk": {
                                    "allowed_vlan": link["vlans"],
                                    "native_vlan": link.get("native_vlan"),
                                },
                            },
                            "service_profile": self.inputs.p2p_uplinks_qos_profile,
                            "link_tracking_groups": link.get("link_tracking_groups"),
                            "spanning_tree_portfast": link.get("spanning_tree_portfast"),
                            "flow_tracker": link.get("flow_tracker"),
                        },
                    )

            # Remove None values
            ethernet_interface = strip_null_from_data(ethernet_interface, strip_values_tuple=(None, "", {}))

            append_if_not_duplicate(
                list_of_dicts=ethernet_interfaces,
                primary_key="name",
                new_dict=ethernet_interface,
                context="Ethernet Interfaces defined for underlay",
                context_keys=["name", "peer", "peer_interface"],
            )

            # Adding subinterfaces for each VRF after the main interface.
            if link["type"] == "underlay_p2p" and "subinterfaces" in link:
                for subinterface in get(link, "subinterfaces", default=[]):
                    description = self.shared_utils.interface_descriptions.underlay_ethernet_interface(
                        InterfaceDescriptionData(
                            shared_utils=self.shared_utils,
                            interface=subinterface["interface"],
                            link_type=link["type"],
                            peer=link["peer"],
                            peer_interface=subinterface["peer_interface"],
                            vrf=subinterface["vrf"],
                        ),
                    )
                    ethernet_subinterface = {
                        "name": subinterface["interface"],
                        "peer": link["peer"],
                        "peer_interface": subinterface["peer_interface"],
                        "peer_type": link["peer_type"],
                        "vrf": subinterface["vrf"],
                        # TODO: - for now reusing the encapsulation as it is hardcoded to the VRF ID which is used as
                        # subinterface name
                        "description": description,
                        "shutdown": self.inputs.shutdown_interfaces_towards_undeployed_peers and not link["peer_is_deployed"],
                        "encapsulation_dot1q": {"vlan": subinterface["encapsulation_dot1q_vlan"]},
                        "ipv6_enable": subinterface.get("ipv6_enable"),
                        "sflow": link.get("sflow"),
                        "flow_tracker": link.get("flow_tracker"),
                        "mtu": self.shared_utils.p2p_uplinks_mtu,
                    }
                    if subinterface.get("ip_address") is not None:
                        ethernet_subinterface.update({"ip_address": f"{subinterface['ip_address']}/{subinterface['prefix_length']}"})

                    ethernet_subinterface = {key: value for key, value in ethernet_subinterface.items() if value is not None}
                    append_if_not_duplicate(
                        list_of_dicts=ethernet_interfaces,
                        primary_key="name",
                        new_dict=ethernet_subinterface,
                        context="Ethernet sub-interfaces defined for underlay",
                        context_keys=["name", "peer", "peer_interface"],
                    )

            # Adding subinterfaces for each SVI after the main interface.
            if link["type"] == "underlay_l2" and self.shared_utils.network_services_l2_as_subint:
                for ethernet_subinterface in ethernet_subinterfaces:  # pylint: disable=used-before-assignment # False positive since condition is the same as above.
                    append_if_not_duplicate(
                        list_of_dicts=ethernet_interfaces,
                        primary_key="name",
                        new_dict=ethernet_subinterface,
                        context="Ethernet sub-interfaces defined for underlay",
                        context_keys=["name", "peer", "peer_interface"],
                    )

        # Support l3_interface as sub interfaces
        subif_parent_interface_names = set()
        for l3_interface in self.shared_utils.l3_interfaces:
            if "." in l3_interface.name:
                # This is a subinterface so we need to ensure that the parent is created
                parent_interface_name, _ = l3_interface.name.split(".", maxsplit=1)
                subif_parent_interface_names.add(parent_interface_name)

            ethernet_interface = self._get_l3_interface_cfg(l3_interface)

            append_if_not_duplicate(
                list_of_dicts=ethernet_interfaces,
                primary_key="name",
                new_dict=ethernet_interface,
                context=f"L3 Interfaces defined under {self.shared_utils.node_type_key_data.key} l3_interfaces",
                context_keys=["name", "peer", "peer_interface"],
            )

        subif_parent_interface_names = subif_parent_interface_names.difference(eth_int["name"] for eth_int in ethernet_interfaces)
        if subif_parent_interface_names:
            for interface_name in natural_sort(subif_parent_interface_names):
                parent_interface = {
                    "name": interface_name,
                    "switchport": {"enabled": False},
                    "peer_type": "l3_interface",
                    "shutdown": False,
                }

                append_if_not_duplicate(
                    list_of_dicts=ethernet_interfaces,
                    primary_key="name",
                    new_dict=parent_interface,
                    context=f"L3 Interfaces defined under {self.shared_utils.node_type_key_data.key} l3_interfaces",
                    context_keys=["name", "peer", "peer_interface"],
                )

        # WAN HA interface(s) for direct connection
        for wan_ha_interface in self._get_direct_ha_ethernet_interfaces():
            append_if_not_duplicate(
                list_of_dicts=ethernet_interfaces,
                primary_key="name",
                new_dict=wan_ha_interface,
                context=f"L3 Interfaces defined under {self.shared_utils.node_type_key_data.key} wan_ha.ha_interfaces",
                context_keys=["name", "peer", "peer_interface"],
            )

        if ethernet_interfaces:
            return ethernet_interfaces

        return None

    def _get_direct_ha_ethernet_interfaces(self: AvdStructuredConfigUnderlay) -> list:
        """
        Return a list of ethernet interfaces to be configured for WAN direct HA.

        Caters for the scenarii where either a port-channel is used or a single l3_interface.
        """
        if self.shared_utils.use_uplinks_for_wan_ha:
            return []

        direct_wan_ha_interfaces = []

        direct_wan_ha_links_flow_tracker = self.shared_utils.get_flow_tracker(self.shared_utils.node_config.wan_ha.flow_tracking)

        if not self.shared_utils.node_config.wan_ha.ha_interfaces:
            msg = "wan_ha.ha_interfaces"
            raise AristaAvdMissingVariableError(msg)

        for index, interface in enumerate(self.shared_utils.node_config.wan_ha.ha_interfaces):
            description = self.shared_utils.interface_descriptions.wan_ha_ethernet_interface(
                InterfaceDescriptionData(
                    shared_utils=self.shared_utils,
                    interface=interface,
                    peer=self.shared_utils.wan_ha_peer,
                    peer_interface=interface,
                ),
            )
            if self.shared_utils.use_port_channel_for_direct_ha:
                direct_wan_ha_interfaces.append(
                    {
                        "name": interface,
                        "peer_type": "wan_ha_peer",
                        "peer_interface": interface,
                        "peer": self.shared_utils.wan_ha_peer,
                        "description": description,
                        "shutdown": False,
                        "channel_group": {
                            "id": self.shared_utils.wan_ha_port_channel_id,
                            "mode": "active",
                        },
                        # TODO: do we need speed?
                        "mtu": self.shared_utils.node_config.wan_ha.mtu,
                    }
                )
            else:
                # Using direct l3 interface
                direct_wan_ha_interfaces.append(
                    {
                        "name": interface,
                        "switchport": {"enabled": False},
                        "peer_type": "l3_interface",
                        "peer": self.shared_utils.wan_ha_peer,
                        "shutdown": False,
                        "description": description,
                        "ip_address": self.shared_utils.wan_ha_ip_addresses[index],
                        "flow_tracker": direct_wan_ha_links_flow_tracker,
                        "mtu": self.shared_utils.node_config.wan_ha.mtu,
                    }
                )

        return direct_wan_ha_interfaces
