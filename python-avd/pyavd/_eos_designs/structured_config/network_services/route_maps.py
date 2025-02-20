# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class RouteMapsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def route_maps(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Set structured config for route_maps.

        Contains two parts.
        - Route-maps for tenant bgp peers set_ipv4_next_hop parameter
        - Route-maps for EVPN services in VRF "default" (using _route_maps_default_vrf)
        - Route-map for tenant redistribute connected if any VRF is not redistributing MLAG peer subnet
        """
        if not self.shared_utils.network_services_l3:
            return

        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                # BGP Peers are already filtered in filtered_tenants
                #  so we only have entries with our hostname in them.
                for bgp_peer in vrf.bgp_peers:
                    ipv4_next_hop = bgp_peer.set_ipv4_next_hop
                    ipv6_next_hop = bgp_peer.set_ipv6_next_hop
                    if ipv4_next_hop is None and ipv6_next_hop is None:
                        continue

                    route_map_name = f"RM-{vrf.name}-{bgp_peer.ip_address}-SET-NEXT-HOP-OUT"
                    set_action = f"ip next-hop {ipv4_next_hop}" if ipv4_next_hop is not None else f"ipv6 next-hop {ipv6_next_hop}"

                    route_maps_item = EosCliConfigGen.RouteMapsItem(name=route_map_name)
                    route_maps_item.sequence_numbers.append_new(
                        sequence=10, type="permit", set=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Set([set_action])
                    )

                    self.structured_config.route_maps.append(route_maps_item)
        self._route_maps_vrf_default()

        # Note we check the 'flag need_mlag_peer_group' here which is being set by router_bgp logic. So this must run after.
        # TODO: Move this logic to a single place instead.
        if self.need_mlag_peer_group and self.shared_utils.node_config.mlag_ibgp_origin_incomplete:
            self._bgp_mlag_peer_group_route_map()

        if self._mlag_ibgp_peering_subnets_without_redistribution:
            self._connected_to_bgp_vrfs_route_map()

    def _route_maps_vrf_default(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Route-maps for EVPN services in VRF "default".

        Called from main route_maps function

        Also checked under router_bgp_vrfs to figure out if a route-map should be set on EVPN export.
        """
        if not self._vrf_default_evpn:
            return

        if not any([self._vrf_default_ipv4_subnets, self._vrf_default_ipv4_static_routes["static_routes"], self.shared_utils.is_wan_router]):
            return

        self._evpn_export_vrf_default_route_map()
        self._bgp_underlay_peers_route_map()
        self._redistribute_connected_to_bgp_route_map()
        self._redistribute_static_to_bgp_route_map()

    def _route_maps_vrf_default_check(self: AvdStructuredConfigNetworkServicesProtocol) -> bool | None:
        if not self._vrf_default_evpn:
            return None

        if any((self._vrf_default_ipv4_subnets, self._vrf_default_ipv4_static_routes["static_routes"], self.shared_utils.is_wan_router)):
            return True

        if not self.inputs.underlay_filter_redistribute_connected:
            return None

        if self.shared_utils.wan_role and self._vrf_default_ipv4_static_routes["redistribute_in_overlay"]:
            return True
        return None

    def _bgp_mlag_peer_group_route_map(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Return dict with one route-map.

        Origin Incomplete for MLAG iBGP learned routes.

        TODO: Partially duplicated from mlag. Should be moved to a common class
        """
        route_maps_item = EosCliConfigGen.RouteMapsItem(name="RM-MLAG-PEER-IN")
        route_maps_item.sequence_numbers.append_new(
            sequence=10,
            type="permit",
            set=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Set(["origin incomplete"]),
            description="Make routes learned over MLAG Peer-link less preferred on spines to ensure optimal routing",
        )
        self.structured_config.route_maps.append(route_maps_item)

    def _connected_to_bgp_vrfs_route_map(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Return dict with one route-map.

        Filter MLAG peer subnets for redistribute connected for overlay VRFs.
        """
        route_maps_item = EosCliConfigGen.RouteMapsItem(name="RM-CONN-2-BGP-VRFS")
        route_maps_item.sequence_numbers.append_new(
            sequence=10,
            type="deny",
            match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ip address prefix-list PL-MLAG-PEER-VRFS"]),
        )
        route_maps_item.sequence_numbers.append_new(
            sequence=20,
            type="permit",
        )
        self.structured_config.route_maps.append(route_maps_item)

    def _evpn_export_vrf_default_route_map(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Match the following prefixes to be exported in EVPN for VRF default.

        * SVI subnets in VRF default
        * Static routes subnets in VRF default.

        * for WAN routers, all the routes matching the SOO (which includes the two above)
        """
        sequence_numbers = EosCliConfigGen.RouteMapsItem.SequenceNumbers()
        if self.shared_utils.is_wan_router:
            sequence_numbers.append_new(
                sequence=10,
                type="permit",
                match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["extcommunity ECL-EVPN-SOO"]),
            )
        else:
            # TODO: refactor existing behavior to SoO?
            if self._vrf_default_ipv4_subnets:
                sequence_numbers.append_new(
                    sequence=10,
                    type="permit",
                    match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ip address prefix-list PL-SVI-VRF-DEFAULT"]),
                )

            if self._vrf_default_ipv4_static_routes["static_routes"]:
                sequence_numbers.append_new(
                    sequence=20,
                    type="permit",
                    match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ip address prefix-list PL-STATIC-VRF-DEFAULT"]),
                )
        if not sequence_numbers:
            return
        self.structured_config.route_maps.append_new(name="RM-EVPN-EXPORT-VRF-DEFAULT", sequence_numbers=sequence_numbers)

    def _bgp_underlay_peers_route_map(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        For non WAN routers filter EVPN routes away from underlay.

        For WAN routers the underlay towards LAN side also permits the tenant routes for VRF default,
        so routes should not be filtered.
        """
        if self.shared_utils.is_wan_router:
            return

        sequence_numbers = EosCliConfigGen.RouteMapsItem.SequenceNumbers()

        if self._vrf_default_ipv4_subnets:
            sequence_numbers.append_new(
                sequence=10,
                type="deny",
                match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ip address prefix-list PL-SVI-VRF-DEFAULT"]),
            )

        if self._vrf_default_ipv4_static_routes["static_routes"]:
            sequence_numbers.append_new(
                sequence=15,
                type="deny",
                match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ip address prefix-list PL-STATIC-VRF-DEFAULT"]),
            )

        if not sequence_numbers:
            return

        sequence_numbers.append_new(
            sequence=20,
            type="permit",
        )
        self.structured_config.route_maps.append_new(name="RM-BGP-UNDERLAY-PEERS-OUT", sequence_numbers=sequence_numbers)

    def _redistribute_connected_to_bgp_route_map(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Append network services relevant entries to the route-map used to redistribute connected subnets in BGP.

        sequence 10 is set in underlay and sequence 20 in inband management, so avoid setting those here
        """
        if not self.inputs.underlay_filter_redistribute_connected:
            return

        sequence_numbers = EosCliConfigGen.RouteMapsItem.SequenceNumbers()

        if self._vrf_default_ipv4_subnets:
            # Add subnets to redistribution in default VRF
            sequence_30 = EosCliConfigGen.RouteMapsItem.SequenceNumbersItem(
                sequence=30, type="permit", match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ip address prefix-list PL-SVI-VRF-DEFAULT"])
            )
            if self.shared_utils.wan_role:
                sequence_30.set = EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Set([f"extcommunity soo {self.shared_utils.evpn_soo} additive"])

            sequence_numbers.append(sequence_30)

        if not sequence_numbers:
            return
        self.structured_config.route_maps.append_new(name="RM-CONN-2-BGP", sequence_numbers=sequence_numbers)

    def _redistribute_static_to_bgp_route_map(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """Append network services relevant entries to the route-map used to redistribute static routes to BGP."""
        if not (self.shared_utils.wan_role and self._vrf_default_ipv4_static_routes["redistribute_in_overlay"]):
            return

        sequence_numbers = EosCliConfigGen.RouteMapsItem.SequenceNumbers()
        sequence_numbers.append_new(
            sequence=10,
            type="permit",
            match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ip address prefix-list PL-STATIC-VRF-DEFAULT"]),
            set=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Set([f"extcommunity soo {self.shared_utils.evpn_soo} additive"]),
        )
        self.structured_config.route_maps.append_new(name="RM-STATIC-2-BGP", sequence_numbers=sequence_numbers)
