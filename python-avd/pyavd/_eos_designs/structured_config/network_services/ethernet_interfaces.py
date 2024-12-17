# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdError
from pyavd._utils import append_if_not_duplicate, get
from pyavd.j2filters import natural_sort

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class EthernetInterfacesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def ethernet_interfaces(self: AvdStructuredConfigNetworkServices) -> list | None:
        """
        Return structured config for ethernet_interfaces.

        Only used with L3 or L1 network services
        """
        if not (self.shared_utils.network_services_l3 or self.shared_utils.network_services_l1):
            return None

        ethernet_interfaces = []
        subif_parent_interface_names = set()

        if self.shared_utils.network_services_l3:
            for tenant in self.shared_utils.filtered_tenants:
                for vrf in tenant.vrfs:
                    # The l3_interfaces has already been filtered in filtered_tenants
                    # to only contain entries with our hostname
                    for l3_interface in vrf.l3_interfaces:
                        nodes_length = len(l3_interface.nodes)
                        if (
                            len(l3_interface.interfaces) != nodes_length
                            or len(l3_interface.ip_addresses) != nodes_length
                            or (l3_interface.descriptions and len(l3_interface.descriptions) != nodes_length)
                        ):
                            msg = (
                                "Length of lists 'interfaces', 'nodes', 'ip_addresses' and 'descriptions' (if used) must match for l3_interfaces for"
                                f" {vrf.name} in {tenant.name}"
                            )
                            raise AristaAvdError(msg)

                        for node_index, node_name in enumerate(l3_interface.nodes):
                            if node_name != self.shared_utils.hostname:
                                continue

                            interface_name = l3_interface.interfaces[node_index]
                            # if 'descriptions' is set, it is preferred
                            interface_description = l3_interface.descriptions[node_index] if l3_interface.descriptions else l3_interface.description
                            interface = {
                                "name": interface_name,
                                "peer_type": "l3_interface",
                                "ip_address": l3_interface.ip_addresses[node_index],
                                "mtu": l3_interface.mtu if self.shared_utils.platform_settings.feature_support.per_interface_mtu else None,
                                "shutdown": not l3_interface.enabled,
                                "description": interface_description,
                                "eos_cli": l3_interface.raw_eos_cli,
                                "struct_cfg": l3_interface.structured_config._as_dict() or None,
                                "flow_tracker": self.shared_utils.get_flow_tracker(l3_interface.flow_tracking),
                            }

                            if self.inputs.fabric_sflow.l3_interfaces is not None:
                                interface["sflow"] = {"enable": self.inputs.fabric_sflow.l3_interfaces}

                            if self._l3_interface_acls is not None:
                                interface.update(
                                    {
                                        "access_group_in": get(self._l3_interface_acls, f"{interface_name}..ipv4_acl_in..name", separator=".."),
                                        "access_group_out": get(self._l3_interface_acls, f"{interface_name}..ipv4_acl_out..name", separator=".."),
                                    },
                                )

                            if "." in interface_name:
                                # This is a subinterface so we need to ensure that the parent is created
                                parent_interface_name, subif_id = interface_name.split(".", maxsplit=1)
                                subif_parent_interface_names.add(parent_interface_name)

                                encapsulation_dot1q_vlans = l3_interface.encapsulation_dot1q_vlan
                                if len(encapsulation_dot1q_vlans) > node_index:
                                    interface["encapsulation_dot1q"] = {"vlan": encapsulation_dot1q_vlans[node_index]}
                                else:
                                    interface["encapsulation_dot1q"] = {"vlan": int(subif_id)}
                            else:
                                interface.update({"switchport": {"enabled": False}})

                            if vrf.name != "default":
                                interface["vrf"] = vrf.name

                            if l3_interface.ospf.enabled and vrf.ospf.enabled:
                                interface["ospf_area"] = l3_interface.ospf.area
                                interface["ospf_network_point_to_point"] = l3_interface.ospf.point_to_point
                                interface["ospf_cost"] = l3_interface.ospf.cost
                                ospf_authentication = l3_interface.ospf.authentication
                                if ospf_authentication == "simple" and (ospf_simple_auth_key := l3_interface.ospf.simple_auth_key) is not None:
                                    interface["ospf_authentication"] = ospf_authentication
                                    interface["ospf_authentication_key"] = ospf_simple_auth_key
                                elif (
                                    ospf_authentication == "message-digest" and (ospf_message_digest_keys := l3_interface.ospf.message_digest_keys) is not None
                                ):
                                    ospf_keys = []
                                    for ospf_key in ospf_message_digest_keys:
                                        if not (ospf_key.id and ospf_key.key):
                                            continue

                                        ospf_keys.append(
                                            {
                                                "id": ospf_key.id,
                                                "hash_algorithm": ospf_key.hash_algorithm,
                                                "key": ospf_key.key,
                                            },
                                        )

                                    if ospf_keys:
                                        interface["ospf_authentication"] = ospf_authentication
                                        interface["ospf_message_digest_keys"] = ospf_keys

                            if l3_interface.pim.enabled:
                                if not getattr(vrf, "_evpn_l3_multicast_enabled", False):
                                    # Possibly the key was not set because `evpn_multicast` is not set to `true`.
                                    if not self.shared_utils.evpn_multicast:
                                        msg = (
                                            f"'pim: enabled' set on l3_interface '{interface_name}' on '{self.shared_utils.hostname}' requires "
                                            "'evpn_multicast: true' at the fabric level"
                                        )
                                    else:
                                        msg = (
                                            f"'pim: enabled' set on l3_interface '{interface_name}' on '{self.shared_utils.hostname}' requires "
                                            f"'evpn_l3_multicast.enabled: true' under VRF '{vrf.name}' or Tenant '{tenant.name}'"
                                        )
                                    raise AristaAvdError(msg)

                                if not getattr(vrf, "_pim_rp_addresses", None):
                                    msg = (
                                        f"'pim: enabled' set on l3_interface '{interface_name}' on '{self.shared_utils.hostname}' requires at least one RP"
                                        f" defined in pim_rp_addresses under VRF '{vrf.name}' or Tenant '{tenant.name}'"
                                    )
                                    raise AristaAvdError(msg)

                                interface["pim"] = {"ipv4": {"sparse_mode": True}}

                            # Strip None values from vlan before adding to list
                            interface = {key: value for key, value in interface.items() if value is not None}

                            append_if_not_duplicate(
                                list_of_dicts=ethernet_interfaces,
                                primary_key="name",
                                new_dict=interface,
                                context="Ethernet Interfaces defined under l3_interfaces",
                                context_keys=["name", "vrf"],
                            )

        if self.shared_utils.network_services_l1:
            for tenant in self.shared_utils.filtered_tenants:
                if not tenant.point_to_point_services:
                    continue

                for point_to_point_service in tenant.point_to_point_services._natural_sorted():
                    for endpoint in point_to_point_service.endpoints:
                        if self.shared_utils.hostname not in endpoint.nodes:
                            continue

                        for node_index, interface_name in enumerate(endpoint.interfaces):
                            if endpoint.nodes[node_index] != self.shared_utils.hostname:
                                continue

                            if (port_channel_mode := endpoint.port_channel.mode) in ["active", "on"]:
                                first_interface_index = endpoint.nodes.index(self.shared_utils.hostname)
                                first_interface_name = endpoint.interfaces[first_interface_index]
                                channel_group_id = int("".join(re.findall(r"\d", first_interface_name)))
                                ethernet_interface = {
                                    "name": interface_name,
                                    "peer_type": "point_to_point_service",
                                    "shutdown": False,
                                    "channel_group": {
                                        "id": channel_group_id,
                                        "mode": port_channel_mode,
                                    },
                                }

                                append_if_not_duplicate(
                                    list_of_dicts=ethernet_interfaces,
                                    primary_key="name",
                                    new_dict=ethernet_interface,
                                    context="Ethernet Interfaces defined under point_to_point_services",
                                    context_keys=["name"],
                                    ignore_same_dict=False,
                                )

                                continue

                            if point_to_point_service.subinterfaces:
                                # This is a subinterface so we need to ensure that the parent is created
                                subif_parent_interface_names.add(interface_name)
                                for subif in point_to_point_service.subinterfaces:
                                    subif_name = f"{interface_name}.{subif.number}"
                                    ethernet_interface = {
                                        "name": subif_name,
                                        "peer_type": "point_to_point_service",
                                        "encapsulation_vlan": {
                                            "client": {
                                                "encapsulation": "dot1q",
                                                "vlan": subif.number,
                                            },
                                            "network": {
                                                "encapsulation": "client",
                                            },
                                        },
                                        "shutdown": False,
                                    }

                                    append_if_not_duplicate(
                                        list_of_dicts=ethernet_interfaces,
                                        primary_key="name",
                                        new_dict=ethernet_interface,
                                        context="Ethernet Interfaces defined under point_to_point_services",
                                        context_keys=["name"],
                                        ignore_same_dict=False,
                                    )

                            else:
                                interface = {
                                    "name": interface_name,
                                    "switchport": {"enabled": False},
                                    "peer_type": "point_to_point_service",
                                    "shutdown": False,
                                }
                                if point_to_point_service.lldp_disable:
                                    interface["lldp"] = {
                                        "transmit": False,
                                        "receive": False,
                                    }

                                append_if_not_duplicate(
                                    list_of_dicts=ethernet_interfaces,
                                    primary_key="name",
                                    new_dict=interface,
                                    context="Ethernet Interfaces defined under point_to_point_services",
                                    context_keys=["name"],
                                    ignore_same_dict=False,
                                )

        subif_parent_interface_names = subif_parent_interface_names.difference(eth_int["name"] for eth_int in ethernet_interfaces)
        if subif_parent_interface_names:
            ethernet_interfaces.extend(
                {
                    "name": interface_name,
                    "switchport": {"enabled": False},
                    "peer_type": "l3_interface",
                    "shutdown": False,
                }
                for interface_name in natural_sort(subif_parent_interface_names)
            )

        ethernet_interfaces.extend(
            {
                "name": connection["source_interface"],
                "ip_nat": {
                    "service_profile": self.get_internet_exit_nat_profile_name(internet_exit_policy.type),
                },
            }
            for internet_exit_policy, connections in self._filtered_internet_exit_policies_and_connections
            for connection in connections
            if connection["type"] == "ethernet"
        )

        if ethernet_interfaces:
            return ethernet_interfaces

        return None
