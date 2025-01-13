# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd.api.interface_descriptions import InterfaceDescriptionData

if TYPE_CHECKING:
    from . import SharedUtils


class L3InterfacesMixin:
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    def sanitize_interface_name(self: SharedUtils, interface_name: str) -> str:
        """
        Interface name is used as value for certain fields, but `/` are not allowed in the value.

        So we transform `/` to `_`
        Ethernet1/1.1 is transformed into Ethernet1_1.1
        """
        return interface_name.replace("/", "_")

    def apply_l3_interfaces_profile(
        self: SharedUtils, l3_interface: EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3InterfacesItem
    ) -> EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3InterfacesItem:
        """Apply a profile to an l3_interface."""
        if not l3_interface.profile:
            # Nothing to do
            return l3_interface

        if l3_interface.profile not in self.inputs.l3_interface_profiles:
            msg = f"Profile '{l3_interface.profile}' applied under l3_interface '{l3_interface.name}' does not exist in `l3_interface_profiles`."
            raise AristaAvdInvalidInputsError(msg)

        profile_as_interface = self.inputs.l3_interface_profiles[l3_interface.profile]._cast_as(
            EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3InterfacesItem
        )
        return l3_interface._deepinherited(profile_as_interface)

    @cached_property
    def l3_interfaces(self: SharedUtils) -> EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3Interfaces:
        """Returns the list of l3_interfaces, where any referenced profiles are applied."""
        return EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3Interfaces(
            [self.apply_l3_interfaces_profile(l3_interface) for l3_interface in self.node_config.l3_interfaces]
        )

    @cached_property
    def l3_interfaces_bgp_neighbors(self: SharedUtils) -> list:
        neighbors = []
        for interface in self.l3_interfaces:
            if not (interface.peer_ip and interface.bgp):
                continue

            peer_as = interface.bgp.peer_as
            if peer_as is None:
                msg = f"'l3_interfaces[{interface.name}].bgp.peer_as' needs to be set to enable BGP."
                raise AristaAvdInvalidInputsError(msg)

            is_intf_wan = bool(interface.wan_carrier)

            if not interface.bgp.ipv4_prefix_list_in and is_intf_wan:
                msg = f"BGP is enabled but 'bgp.ipv4_prefix_list_in' is not configured for l3_interfaces[{interface.name}]"
                raise AristaAvdInvalidInputsError(msg)

            description = interface.description
            if not description:
                description = self.interface_descriptions.underlay_ethernet_interface(
                    InterfaceDescriptionData(
                        shared_utils=self,
                        interface=interface.name,
                        peer=interface.peer,
                        peer_interface=interface.peer_interface,
                        wan_carrier=interface.wan_carrier,
                        wan_circuit_id=interface.wan_circuit_id,
                    ),
                )

            neighbor = {
                "ip_address": interface.peer_ip,
                "remote_as": peer_as,
                "description": description,
            }

            neighbor["ipv4_prefix_list_in"] = interface.bgp.ipv4_prefix_list_in
            neighbor["ipv4_prefix_list_out"] = interface.bgp.ipv4_prefix_list_out
            if is_intf_wan:
                neighbor["set_no_advertise"] = True

            # The inbound route-map is only used if there is a prefix list or no-advertise
            if neighbor["ipv4_prefix_list_in"] or neighbor.get("set_no_advertise") is True:
                neighbor["route_map_in"] = f"RM-BGP-{neighbor['ip_address']}-IN"
            neighbor["route_map_out"] = f"RM-BGP-{neighbor['ip_address']}-OUT"

            neighbors.append(neighbor)

        return neighbors
