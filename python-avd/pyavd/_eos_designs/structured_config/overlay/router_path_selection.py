# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdError
from pyavd._utils import get, get_ip_from_ip_prefix, strip_empties_from_dict

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigOverlay


class RouterPathSelectionMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def router_path_selection(self: AvdStructuredConfigOverlay) -> dict | None:
        """Return structured config for router path-selection (DPS)."""
        if not self.shared_utils.is_wan_router:
            return None

        router_path_selection = {
            "tcp_mss_ceiling": {"ipv4_segment_size": self.shared_utils.node_config.dps_mss_ipv4},
            "path_groups": self._get_path_groups(),
        }

        if self.shared_utils.is_wan_server:
            router_path_selection["peer_dynamic_source"] = "stun"

        return strip_empties_from_dict(router_path_selection)

    @cached_property
    def _dp_ipsec_profile_name(self: AvdStructuredConfigOverlay) -> str:
        """Returns the IPsec profile name to use for Data-Plane.

        If no data-plane config is present for IPsec, default to the control-plane profile-name.
        """
        if self.inputs.wan_ipsec_profiles.data_plane:
            return self.inputs.wan_ipsec_profiles.data_plane.profile_name
        return self.inputs.wan_ipsec_profiles.control_plane.profile_name

    def _get_path_groups(self: AvdStructuredConfigOverlay) -> list:
        """Generate the required path-groups locally."""
        path_groups = []

        # Configure all path-groups on Pathfinders and AutoVPN RRs. Otherwise only configure the local path-groups
        path_groups_to_configure = self.inputs.wan_path_groups if self.shared_utils.is_wan_server else self.shared_utils.wan_local_path_groups

        for path_group in path_groups_to_configure:
            pg_name = path_group.name
            is_local_pg = pg_name in self.shared_utils.wan_local_path_group_names
            disable_dynamic_peer_ipsec = is_local_pg and not path_group.ipsec.dynamic_peers

            path_group_data = {
                "name": pg_name,
                "id": self._get_path_group_id(pg_name, path_group.id),
                "local_interfaces": self._get_local_interfaces_for_path_group(pg_name),
                "dynamic_peers": self._get_dynamic_peers(disable_dynamic_peer_ipsec),
                "static_peers": self._get_static_peers_for_path_group(pg_name),
            }

            if is_local_pg:
                # On pathfinder IPsec profile is not required for non local path_groups
                if path_group.ipsec.static_peers:
                    path_group_data["ipsec_profile"] = self.inputs.wan_ipsec_profiles.control_plane.profile_name

                # KeepAlive config is not required for non local path_groups
                if interval := path_group.dps_keepalive.interval:
                    if interval == "auto":
                        path_group_data["keepalive"] = {"auto": True}
                    else:
                        if not (interval.isdigit() and 50 <= int(interval) <= 60000):
                            msg = (
                                f"Invalid value '{interval}' for dps_keepalive.interval - "
                                f"should be either 'auto', or an integer[50-60000] for wan_path_groups[{pg_name}]"
                            )
                            raise AristaAvdError(msg)
                        path_group_data["keepalive"] = {
                            "interval": int(interval),
                            "failure_threshold": path_group.dps_keepalive.failure_threshold,
                        }

            path_groups.append(path_group_data)

        if self.shared_utils.wan_ha or self.shared_utils.is_cv_pathfinder_server:
            path_groups.append(self._generate_ha_path_group())

        return path_groups

    def _generate_ha_path_group(self: AvdStructuredConfigOverlay) -> dict:
        """Called only when self.shared_utils.wan_ha is True or on Pathfinders."""
        ha_path_group = {
            "name": self.inputs.wan_ha.lan_ha_path_group_name,
            "id": self._get_path_group_id(self.inputs.wan_ha.lan_ha_path_group_name),
            "flow_assignment": "lan",
        }
        if self.shared_utils.is_cv_pathfinder_server:
            return ha_path_group

        if self.shared_utils.use_port_channel_for_direct_ha is True:
            local_interfaces = [{"name": f"Port-Channel{self.shared_utils.wan_ha_port_channel_id}"}]
        else:
            local_interfaces = [{"name": interface} for interface in self.shared_utils.wan_ha_interfaces]

        # not a pathfinder device
        ha_path_group.update(
            {
                # This should be the LAN interface over which a DPS tunnel is built
                "local_interfaces": local_interfaces,
                "static_peers": [
                    {
                        "router_ip": self._wan_ha_peer_vtep_ip(),
                        "name": self.shared_utils.wan_ha_peer,
                        "ipv4_addresses": [get_ip_from_ip_prefix(ip_address) for ip_address in self.shared_utils.wan_ha_peer_ip_addresses],
                    },
                ],
            },
        )
        if self.shared_utils.wan_ha_ipsec:
            ha_path_group["ipsec_profile"] = self._dp_ipsec_profile_name

        return ha_path_group

    def _wan_ha_interfaces(self: AvdStructuredConfigOverlay) -> list:
        """Return list of interfaces for HA."""
        return [uplink for uplink in self.shared_utils.get_switch_fact("uplinks") if get(uplink, "vrf") is None]

    def _wan_ha_peer_vtep_ip(self: AvdStructuredConfigOverlay) -> str:
        peer_facts = self.shared_utils.get_peer_facts(self.shared_utils.wan_ha_peer, required=True)
        return get(peer_facts, "vtep_ip", required=True)

    def _get_path_group_id(self: AvdStructuredConfigOverlay, path_group_name: str, config_id: int | None = None) -> int:
        """
        Get path group id.

        TODO: - implement algorithm to auto assign IDs - cf internal documentation
        TODO: - also implement algorithm for cross connects on public path_groups.
        """
        if path_group_name == self.inputs.wan_ha.lan_ha_path_group_name:
            return 65535
        if config_id is not None:
            return config_id
        return 500

    def _get_local_interfaces_for_path_group(self: AvdStructuredConfigOverlay, path_group_name: str) -> list:
        """
        Generate the router_path_selection.local_interfaces list.

        For AUTOVPN clients, configure the stun server profiles as appropriate
        """
        local_interfaces = []
        if path_group_name not in self.shared_utils.wan_local_path_groups:
            return local_interfaces

        for interface in self.shared_utils.wan_local_path_groups[path_group_name]._interfaces:
            local_interface = {"name": get(interface, "name", required=True)}

            if self.shared_utils.is_wan_client and self.shared_utils.should_connect_to_wan_rs([path_group_name]):
                stun_server_profiles = self._stun_server_profiles.get(path_group_name, [])
                if stun_server_profiles:
                    local_interface["stun"] = {"server_profiles": [profile["name"] for profile in stun_server_profiles]}

            local_interfaces.append(local_interface)

        return local_interfaces

    def _get_dynamic_peers(self: AvdStructuredConfigOverlay, disable_ipsec: bool) -> dict | None:
        """TODO: support ip_local ?"""
        if not self.shared_utils.is_wan_client:
            return None

        dynamic_peers = {"enabled": True}
        if disable_ipsec:
            dynamic_peers["ipsec"] = False
        return dynamic_peers

    def _get_static_peers_for_path_group(self: AvdStructuredConfigOverlay, path_group_name: str) -> list | None:
        """Retrieves the static peers to configure for a given path-group based on the connected nodes."""
        if not self.shared_utils.is_wan_router:
            return None

        static_peers = []
        for wan_route_server in self.shared_utils.filtered_wan_route_servers:
            if path_group_name not in wan_route_server.path_groups:
                continue

            ipv4_addresses = [
                get_ip_from_ip_prefix(interface.public_ip) for interface in wan_route_server.path_groups[path_group_name].interfaces if interface.public_ip
            ]

            static_peers.append(
                {
                    "router_ip": wan_route_server.vtep_ip,
                    "name": wan_route_server.hostname,
                    "ipv4_addresses": ipv4_addresses,
                },
            )

        return static_peers
