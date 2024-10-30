# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import get, get_item, merge
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

    def apply_l3_interfaces_profile(self: SharedUtils, l3_interface: dict) -> dict:
        """Apply a profile to an l3_interface."""
        if "profile" not in l3_interface:
            # Nothing to do
            return l3_interface

        msg = f"Profile '{l3_interface['profile']}' applied under l3_interface '{l3_interface['name']}' does not exist in `l3_interface_profiles`."
        profile = get_item(self.l3_interface_profiles, "profile", l3_interface["profile"], required=True, custom_error_msg=msg)
        merged_dict: dict = merge(profile, l3_interface, list_merge="replace", destructive_merge=False)
        merged_dict.pop("profile", None)
        return merged_dict

    @cached_property
    def l3_interface_profiles(self: SharedUtils) -> list:
        return get(self.hostvars, "l3_interface_profiles", default=[])

    @cached_property
    def l3_interfaces(self: SharedUtils) -> list:
        """Returns the list of l3_interfaces, where any referenced profiles are applied."""
        if not (l3_interfaces := get(self.switch_data_combined, "l3_interfaces")):
            return []

        # Apply l3_interfaces._profile if set.
        if self.l3_interface_profiles:
            l3_interfaces = [self.apply_l3_interfaces_profile(l3_interface) for l3_interface in l3_interfaces]

        return l3_interfaces

    @cached_property
    def l3_interfaces_bgp_neighbors(self: SharedUtils) -> list:
        neighbors = []
        for interface in self.l3_interfaces:
            peer_ip = get(interface, "peer_ip")
            bgp = get(interface, "bgp")
            if not (peer_ip and bgp):
                continue

            peer_as = get(bgp, "peer_as")
            if peer_as is None:
                msg = f"'l3_interfaces[{interface['name']}].bgp.peer_as' needs to be set to enable BGP."
                raise AristaAvdInvalidInputsError(msg)

            is_intf_wan = get(interface, "wan_carrier") is not None

            prefix_list_in = get(bgp, "ipv4_prefix_list_in")
            if prefix_list_in is None and is_intf_wan:
                msg = f"BGP is enabled but 'bgp.ipv4_prefix_list_in' is not configured for l3_interfaces[{interface['name']}]"
                raise AristaAvdInvalidInputsError(msg)

            description = interface.get("description")
            if not description:
                description = self.interface_descriptions.underlay_ethernet_interface(
                    InterfaceDescriptionData(
                        shared_utils=self,
                        interface=interface["name"],
                        peer=interface.get("peer"),
                        peer_interface=interface.get("peer_interface"),
                        wan_carrier=interface.get("wan_carrier"),
                        wan_circuit_id=interface.get("wan_circuit_id"),
                    ),
                )

            neighbor = {
                "ip_address": peer_ip,
                "remote_as": peer_as,
                "description": description,
            }

            neighbor["ipv4_prefix_list_in"] = prefix_list_in
            neighbor["ipv4_prefix_list_out"] = get(bgp, "ipv4_prefix_list_out")
            if is_intf_wan:
                neighbor["set_no_advertise"] = True

            # The inbound route-map is only used if there is a prefix list or no-advertise
            if neighbor["ipv4_prefix_list_in"] or neighbor.get("set_no_advertise") is True:
                neighbor["route_map_in"] = f"RM-BGP-{neighbor['ip_address']}-IN"
            neighbor["route_map_out"] = f"RM-BGP-{neighbor['ip_address']}-OUT"

            neighbors.append(neighbor)

        return neighbors
