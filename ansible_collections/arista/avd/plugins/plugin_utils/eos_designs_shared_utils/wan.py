# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.errors import AristaAvdError
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, get_item

if TYPE_CHECKING:
    from .shared_utils import SharedUtils


class WanMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def wan_mode(self: SharedUtils) -> str:
        return get(self.hostvars, "wan_mode", default="cv-pathfinder")

    @cached_property
    def wan_role(self: SharedUtils) -> str | None:
        if self.underlay_router is False or self.wan_mode is None:
            return None

        default_wan_role = get(self.node_type_key_data, "default_wan_role", default=None)
        wan_role = get(self.switch_data_combined, "wan_role", default=default_wan_role)
        if wan_role is not None and self.overlay_routing_protocol != "ibgp":
            raise AristaAvdError("Only 'ibgp' is supported as 'overlay_routing_protocol' for WAN nodes.")
        if wan_role == "server" and self.evpn_role != "server":
            raise AristaAvdError("'wan_role' server requires 'evpn_role' server.")
        if wan_role == "client" and self.evpn_role != "client":
            raise AristaAvdError("'wan_role' client requires 'evpn_role' client.")
        return wan_role

    @cached_property
    def cv_pathfinder_role(self: SharedUtils) -> str | None:
        if self.underlay_router is False or self.wan_mode != "cv-pathfinder":
            return None

        default_cv_pathfinder_role = get(self.node_type_key_data, "default_cv_pathfinder_role", default=None)
        cv_pathfinder_role = get(self.switch_data_combined, "cv_pathfinder_role", default=default_cv_pathfinder_role)
        if cv_pathfinder_role == "pathfinder" and self.wan_role != "server":
            raise AristaAvdError("'wan_role' must be 'server' when 'cv_pathfinder_role' is set to 'pathfinder'")
        if cv_pathfinder_role in ["transit", "edge"] and self.wan_role != "client":
            raise AristaAvdError("'wan_role' must be 'client' when 'cv_pathfinder_role' is set to 'transit' or 'edge'")
        return cv_pathfinder_role

    @cached_property
    def wan_interfaces(self: SharedUtils) -> list:
        """
        As a first approach, only interfaces under l3edge.l3_interfaces can be considered
        as WAN interfaces.
        This may need to be made wider.
        This also may require a different format for the dictionaries inside the list.
        """
        if self.wan_role is None:
            return []

        wan_interfaces = []
        for interface in self.l3_interfaces:
            if get(interface, "wan_carrier") is not None:
                wan_interfaces.append(interface)

        return wan_interfaces

    @cached_property
    def wan_local_carriers(self: SharedUtils) -> list:
        """
        List of carriers present on this router based on the wan_interfaces with the associated WAN interfaces
            interfaces:
              - name: ...
                ip: ...
        """
        if not self.wan_role:
            return []

        local_carriers_dict = {}
        global_carriers = get(self.hostvars, "wan_carriers", required=True)
        for interface in self.wan_interfaces:
            interface_carrier = interface["wan_carrier"]
            if interface_carrier not in local_carriers_dict:
                local_carriers_dict[interface_carrier] = get_item(
                    global_carriers,
                    "name",
                    interface["wan_carrier"],
                    required=True,
                    custom_error_msg=f"WAN carrier {interface['wan_carrier']} is not in the available carriers defined in `wan_carriers`",
                ).copy()
                local_carriers_dict[interface_carrier]["interfaces"] = []

            local_carriers_dict[interface_carrier]["interfaces"].append(
                {
                    "name": get(interface, "name", required=True),
                    "ip_address": get(interface, "ip", required=True),
                    "connected_to_pathfinder": get(interface, "connected_to_pathfinder", default=True),
                }
            )

        return list(local_carriers_dict.values())

    @cached_property
    def wan_local_path_groups(self: SharedUtils) -> list:
        """
        List of path_groups present on this router based on the local carriers.
        Also add for each path_groups the local interfaces in a data structure
            interfaces:
              - name: ...
                ip: ...
        """
        if self.wan_role is None:
            return []

        local_path_groups_dict = {}
        global_path_groups = get(self.hostvars, "wan_path_groups", required=True)
        for carrier in self.wan_local_carriers:
            path_group_name = get(carrier, "path_group", required=True)
            if path_group_name not in local_path_groups_dict:
                local_path_groups_dict[path_group_name] = get_item(
                    global_path_groups,
                    "name",
                    path_group_name,
                    required=True,
                    custom_error_msg=(
                        f"WAN path_group {path_group_name} defined for a WAN carrier is not in the available path_groups defined in `wan_path_groups`"
                    ),
                ).copy()
                local_path_groups_dict[path_group_name]["interfaces"] = []

            local_path_groups_dict[path_group_name]["interfaces"].extend(carrier["interfaces"])

        return list(local_path_groups_dict.values())
