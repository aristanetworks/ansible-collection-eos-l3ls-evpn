# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdError
from pyavd._utils import get, strip_empties_from_dict
from pyavd.j2filters import natural_sort

if TYPE_CHECKING:
    from . import AvdStructuredConfigOverlay


class UtilsMixin:
    """
    Mixin Class with internal functions.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def _avd_overlay_peers(self: AvdStructuredConfigOverlay) -> list:
        """
        Returns a list of overlay peers for the device.

        This cannot be loaded in shared_utils since it will not be calculated until EosDesignsFacts has been rendered
        and shared_utils are shared between EosDesignsFacts and AvdStructuredConfig classes like this one.
        """
        return get(self._hostvars, f"avd_overlay_peers..{self.shared_utils.hostname}", separator="..", default=[])

    @cached_property
    def _evpn_gateway_remote_peers(self: AvdStructuredConfigOverlay) -> dict:
        if not self.shared_utils.overlay_evpn:
            return {}

        evpn_gateway_remote_peers = {}

        for remote_peer in self.shared_utils.node_config.evpn_gateway.remote_peers._natural_sorted():
            remote_peer_name = remote_peer.hostname

            # These remote gateways can be outside of the inventory or in the inventory
            gw_info = strip_empties_from_dict(
                {
                    "bgp_as": remote_peer.bgp_as,
                    "ip_address": remote_peer.ip_address,
                    # Not adding the "overlay_peering_interface" since we do not know it for this device. Only used for description.
                }
            )

            peer_facts = self.shared_utils.get_peer_facts(remote_peer_name, required=False)
            if peer_facts is None:
                # No matching host found in the inventory for this remote gateway
                evpn_gateway_remote_peers[remote_peer_name] = gw_info
            else:
                # Found a matching name for this remote gateway in the inventory
                self._append_peer(evpn_gateway_remote_peers, remote_peer_name, peer_facts)
                # Apply potential override if present in the input variables
                evpn_gateway_remote_peers[remote_peer_name].update(strip_empties_from_dict(gw_info))

            if any(key not in evpn_gateway_remote_peers[remote_peer_name] for key in ["bgp_as", "ip_address"]):
                msg = f"The EVPN Gateway remote peer '{remote_peer_name}' is missing either a `bpg_as` or an `ip_address`."
                raise AristaAvdError(msg)

        return evpn_gateway_remote_peers

    @cached_property
    def _evpn_route_clients(self: AvdStructuredConfigOverlay) -> dict:
        if not self.shared_utils.overlay_evpn:
            return {}

        if self.shared_utils.evpn_role != "server":
            return {}

        evpn_route_clients = {}

        for avd_peer in self._avd_overlay_peers:
            peer_facts = self.shared_utils.get_peer_facts(avd_peer, required=True)
            if (
                self.shared_utils.hostname in peer_facts.get("evpn_route_servers", [])
                and peer_facts.get("evpn_role") in ["server", "client"]
                and avd_peer not in self._evpn_route_servers
            ):
                self._append_peer(evpn_route_clients, avd_peer, peer_facts)

        return evpn_route_clients

    @cached_property
    def _evpn_route_servers(self: AvdStructuredConfigOverlay) -> dict:
        if not self.shared_utils.overlay_evpn:
            return {}

        evpn_route_servers = {}

        for route_server in natural_sort(get(self._hostvars, "switch.evpn_route_servers", default=[])):
            peer_facts = self.shared_utils.get_peer_facts(route_server, required=True)
            if peer_facts.get("evpn_role") != "server":
                continue

            self._append_peer(evpn_route_servers, route_server, peer_facts)

        return evpn_route_servers

    # The next four should probably be moved to facts
    @cached_property
    def _is_mpls_client(self: AvdStructuredConfigOverlay) -> bool:
        return self.shared_utils.mpls_overlay_role == "client" or (self.shared_utils.evpn_role == "client" and self.shared_utils.overlay_evpn_mpls)

    @cached_property
    def _is_mpls_server(self: AvdStructuredConfigOverlay) -> bool:
        return self.shared_utils.mpls_overlay_role == "server" or (self.shared_utils.evpn_role == "server" and self.shared_utils.overlay_evpn_mpls)

    def _is_peer_mpls_client(self: AvdStructuredConfigOverlay, peer_facts: dict) -> bool:
        return peer_facts.get("mpls_overlay_role") == "client" or (peer_facts.get("evpn_role") == "client" and get(peer_facts, "overlay.evpn_mpls") is True)

    def _is_peer_mpls_server(self: AvdStructuredConfigOverlay, peer_facts: dict) -> bool:
        return peer_facts.get("mpls_overlay_role") == "server" or (peer_facts.get("evpn_role") == "server" and get(peer_facts, "overlay.evpn_mpls") is True)

    @cached_property
    def _ipvpn_gateway_remote_peers(self: AvdStructuredConfigOverlay) -> dict:
        if self.shared_utils.overlay_ipvpn_gateway is not True:
            return {}

        ipvpn_gateway_remote_peers = {}

        for remote_peer in self.shared_utils.node_config.ipvpn_gateway.remote_peers._natural_sorted():
            # These remote gw are outside of the inventory

            bgp_as = remote_peer.bgp_as

            ipvpn_gateway_remote_peers[remote_peer.hostname] = {
                "bgp_as": str(bgp_as) if bgp_as is not None else None,
                "ip_address": remote_peer.ip_address,
                # Not adding the "overlay_peering_interface" since we do not know it for this device. Only used for description.
            }

        return ipvpn_gateway_remote_peers

    @cached_property
    def _mpls_route_clients(self: AvdStructuredConfigOverlay) -> dict:
        if self._is_mpls_server is not True:
            return {}

        mpls_route_clients = {}

        for avd_peer in self._avd_overlay_peers:
            peer_facts = self.shared_utils.get_peer_facts(avd_peer, required=True)
            if self._is_peer_mpls_client(peer_facts) is not True:
                continue

            if self.shared_utils.hostname in peer_facts.get("mpls_route_reflectors", []) and avd_peer not in self._mpls_route_reflectors:
                self._append_peer(mpls_route_clients, avd_peer, peer_facts)

        return mpls_route_clients

    @cached_property
    def _mpls_mesh_pe(self: AvdStructuredConfigOverlay) -> dict:
        if not self.shared_utils.overlay_mpls or not self.inputs.bgp_mesh_pes:
            return {}

        mpls_mesh_pe = {}
        for fabric_switch in self.shared_utils.all_fabric_devices:
            if self._mpls_route_reflectors is not None and fabric_switch in self._mpls_route_reflectors:
                continue
            if fabric_switch == self.shared_utils.hostname:
                continue

            peer_facts = self.shared_utils.get_peer_facts(fabric_switch, required=True)
            if self._is_peer_mpls_client(peer_facts) is not True:
                continue

            self._append_peer(mpls_mesh_pe, fabric_switch, peer_facts)

        return mpls_mesh_pe

    @cached_property
    def _mpls_route_reflectors(self: AvdStructuredConfigOverlay) -> dict:
        if self._is_mpls_client is not True:
            return {}

        mpls_route_reflectors = {}

        for route_reflector in natural_sort(get(self._hostvars, "switch.mpls_route_reflectors", default=[])):
            if route_reflector == self.shared_utils.hostname:
                continue

            peer_facts = self.shared_utils.get_peer_facts(route_reflector, required=True)
            if self._is_peer_mpls_server(peer_facts) is not True:
                continue

            self._append_peer(mpls_route_reflectors, route_reflector, peer_facts)

        return mpls_route_reflectors

    @cached_property
    def _mpls_rr_peers(self: AvdStructuredConfigOverlay) -> dict:
        if self._is_mpls_server is not True:
            return {}

        mpls_rr_peers = {}

        for route_reflector in natural_sort(get(self._hostvars, "switch.mpls_route_reflectors", default=[])):
            if route_reflector == self.shared_utils.hostname:
                continue

            peer_facts = self.shared_utils.get_peer_facts(route_reflector, required=True)
            if self._is_peer_mpls_server(peer_facts) is not True:
                continue

            self._append_peer(mpls_rr_peers, route_reflector, peer_facts)

        for avd_peer in self._avd_overlay_peers:
            peer_facts = self.shared_utils.get_peer_facts(avd_peer, required=True)
            if self._is_peer_mpls_server(peer_facts) is not True:
                continue

            if self.shared_utils.hostname in peer_facts.get("mpls_route_reflectors", []) and avd_peer not in get(
                self._hostvars,
                "switch.mpls_route_reflectors",
                default=[],
            ):
                self._append_peer(mpls_rr_peers, avd_peer, peer_facts)

        return mpls_rr_peers

    def _append_peer(self: AvdStructuredConfigOverlay, peers_dict: dict, peer_name: str, peer_facts: dict) -> None:
        """
        Retrieve bgp_as and "overlay.peering_address" from peer_facts and append a new peer to peers_dict.

        {
            peer_name: {
                "bgp_as": bgp_as,
                "ip_address": overlay.peering_address,
                "overlay_peering_interface": "Loopback0"
            }
        }.
        """
        bgp_as = peer_facts.get("bgp_as")
        peers_dict[peer_name] = {
            "bgp_as": str(bgp_as) if bgp_as is not None else None,
            "ip_address": get(
                peer_facts,
                "overlay.peering_address",
                required=True,
                custom_error_msg=f"switch.overlay.peering_address for {peer_name} is required.",
            ),
            "overlay_peering_interface": "Loopback0",
        }

    @cached_property
    def _is_wan_server_with_peers(self: AvdStructuredConfigOverlay) -> bool:
        return self.shared_utils.is_wan_server and len(self.shared_utils.filtered_wan_route_servers) > 0

    def _stun_server_profile_name(self: AvdStructuredConfigOverlay, wan_route_server_name: str, path_group_name: str, interface_name: str) -> str:
        """
        Return a string to use as the name of the stun server_profile.

        `/` are not allowed, `.` are allowed so
        Ethernet1/1.1 is transformed into Ethernet1_1.1
        """
        sanitized_interface_name = self.shared_utils.sanitize_interface_name(interface_name)
        return f"{path_group_name}-{wan_route_server_name}-{sanitized_interface_name}"

    @cached_property
    def _stun_server_profiles(self: AvdStructuredConfigOverlay) -> dict:
        """Return a dictionary of _stun_server_profiles with ip_address per local path_group."""
        stun_server_profiles = {}
        for wan_route_server in self.shared_utils.filtered_wan_route_servers:
            for path_group in wan_route_server.path_groups:
                stun_server_profiles.setdefault(path_group.name, []).extend(
                    {
                        "name": self._stun_server_profile_name(wan_route_server.hostname, path_group.name, interface.name),
                        "ip_address": interface.public_ip,
                        "ssl_profile": self.shared_utils.wan_stun_dtls_profile_name,
                    }
                    for interface in path_group.interfaces
                )
        return stun_server_profiles

    def _wan_ha_peer_vtep_ip(self: AvdStructuredConfigOverlay) -> str:
        peer_facts = self.shared_utils.get_peer_facts(self.shared_utils.wan_ha_peer, required=True)
        return get(peer_facts, "vtep_ip", required=True)
