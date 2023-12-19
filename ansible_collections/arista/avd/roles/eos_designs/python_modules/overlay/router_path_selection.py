# Copyright (c) 2023 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.strip_empties import strip_empties_from_dict
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get

from .utils import UtilsMixin


class RouterPathSelectionMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def router_path_selection(self) -> dict | None:
        """
        Return structured config for router path-selection (DPS)
        """

        if not self.shared_utils.wan_role:
            return None

        path_groups = self._get_path_groups()

        router_path_selection = {
            "path_groups": path_groups,
            "load_balance_policies": self._get_load_balance_policies(path_groups),
            "policies": self._get_policies(),
            "vrfs": self._get_vrfs(),
        }

        if self.shared_utils.wan_role == "server":
            router_path_selection["peer_dynamic_source"] = "stun"

        return strip_empties_from_dict(router_path_selection)

    def _get_path_groups(self) -> list:
        """
        Generate the required path-groups locally
        """
        path_groups = []

        # TODO - need to have default value in one place only -> maybe facts / shared_utils ?
        ipsec_profile_name = get(self._hostvars, "wan_ipsec_profiles.control_plane.profile_name", default="CP-PROFILE")

        for path_group in self.shared_utils.wan_local_path_groups:
            pg_name = path_group.get("name")

            path_group_data = {
                "name": pg_name,
                "id": self._get_path_group_id(pg_name),
                "local_interfaces": self._get_local_interfaces(pg_name),
                "dynamic_peers": self._get_dynamic_peers(),
                "static_peers": self._get_static_peers(pg_name),
            }

            if path_group.get("ipsec", True):
                path_group_data["ipsec_profile"] = ipsec_profile_name

            path_groups.append(path_group_data)

        if self.shared_utils.cv_pathfinder_role:
            pass
            # implement LAN_HA here

        return path_groups

    def _get_load_balance_policies(self, path_groups: dict) -> dict | None:
        """ """
        # TODO for now a default load balance policy with all path-groups.
        load_balance_policies = []
        load_balance_policies.append({"name": "LBPOLICY", "path_groups": [{"name": pg.get("name")} for pg in path_groups]})
        return load_balance_policies

    def _get_policies(self) -> list | None:
        """
        Only configure a default DPS policy for the default VRF if wan_mode is autovpn
        for cv-pathfinder, the VRFs are confgured under adaptive_virtual_topology.
        """
        policies = []
        if self.shared_utils.wan_mode == "autovpn":
            # TODO DPS policies - for now adding one default one - MAYBE NEED TO REMOVED
            policies = [{"name": "dps-policy-default", "default_match": {"load_balance": "LBPOLICY"}}]
            return policies
        return None

    def _get_vrfs(self) -> list | None:
        """
        Only configure a default VRF if wan_mode is autovpn
        for cv-pathfinder, the VRFs are confgured under adaptive_virtual_topology.
        """
        vrfs = []
        if self.shared_utils.wan_mode == "autovpn":
            # TODO - Adding default VRF here - check if it makes sense later
            vrfs = [{"name": "default", "path_selection_policy": "dps-policy-default"}]
            return vrfs
        return None

    def _get_path_group_id(self, path_group_name: str) -> int:
        """
        TODO - implement algorithm to auto assign IDs - cf internal documenation
        TODO - also implement algorithm for cross connects on public path_groups
        """
        if path_group_name == "LAN_HA":
            return 65535
        return 500

    def _get_local_interfaces(self, path_group_name: str) -> list | None:
        """
        Generate the router_path_selection.local_interfaces list

        For AUTOVPN clients, configure the stun server profiles as appropriate
        """
        local_interfaces = []
        for wan_interface in self.shared_utils.wan_interfaces:
            # Skipping interface not in the target path_group
            if wan_interface.get("wan_path_group") != path_group_name:
                continue

            local_interface = {"name": get(wan_interface, "interface", required=True)}

            if self.shared_utils.wan_role == "client":
                stun_server_profiles = []
                for wrr, data in self._wan_route_servers.items():
                    for index, path_group in enumerate(get(data, "wan_path_groups", required=True)):
                        if path_group.get("name") != path_group_name:
                            continue
                        if not self._should_connect_to_wan_rr([path_group["name"]]):
                            continue
                        stun_server_profiles.append(self._stun_server_profile_name(wrr, path_group_name, index))

                if stun_server_profiles:
                    local_interface["stun"] = {"server_profiles": stun_server_profiles}

            local_interfaces.append(local_interface)

        return local_interfaces

    def _get_dynamic_peers(self) -> dict | None:
        """ """
        if self.shared_utils.wan_role != "client":
            return None
        return {"enabled": True}

    def _get_static_peers(self, path_group_name: str) -> list | None:
        """
        TODO
        """
        if self.shared_utils.wan_role != "client":
            return None
        static_peers = []
        for wan_route_server, data in self._wan_route_servers.items():
            for path_group in get(data, "wan_path_groups", required=True):
                if path_group["name"] != path_group_name:
                    continue
                if not self._should_connect_to_wan_rr([path_group["name"]]):
                    continue

                for interface_dict in path_group.get("interfaces", []):
                    ipv4_addresses = []
                    if (ip_address := interface_dict.get("ip_address")) is not None:
                        # TODO - removing mask using split but maybe a helper is clearer
                        ipv4_addresses.append(ip_address.split("/")[0])
                    static_peers.append(
                        {
                            "router_ip": get(data, "router_id", required=True),
                            "name": wan_route_server,
                            "ipv4_addresses": ipv4_addresses,
                        }
                    )

        return static_peers
