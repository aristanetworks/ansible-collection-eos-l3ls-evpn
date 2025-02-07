# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd.j2filters import natural_sort

if TYPE_CHECKING:
    from . import AvdStructuredConfigOverlayProtocol


class RouteMapsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def route_maps(self: AvdStructuredConfigOverlayProtocol) -> None:
        """Set the structured config for route_maps."""
        if self.shared_utils.overlay_cvx:
            return

        if self.shared_utils.overlay_routing_protocol == "ebgp":
            if self.inputs.evpn_prevent_readvertise_to_server:
                remote_asns = natural_sort({rs_dict.get("bgp_as") for rs_dict in self._evpn_route_servers.values()})
                for remote_asn in remote_asns:
                    route_maps_item = self.structured_config.RouteMapsItem(name=f"RM-EVPN-FILTER-AS{remote_asn}")
                    sequence_numbers_item = route_maps_item.SequenceNumbersItem(sequence=10, type="deny")
                    sequence_numbers_item.match.append(f"as {remote_asn}")
                    route_maps_item.sequence_numbers.append(sequence_numbers_item)
                    sequence_numbers_item = route_maps_item.SequenceNumbersItem(sequence=20, type="permit")
                    route_maps_item.sequence_numbers.append(sequence_numbers_item)
                    self.structured_config.route_maps.append(route_maps_item)

        elif self.shared_utils.overlay_routing_protocol == "ibgp" and self.shared_utils.overlay_vtep and self.shared_utils.evpn_role != "server":
            # Route-map IN and OUT for SOO
            route_maps_item = self.structured_config.RouteMapsItem(name="RM-EVPN-SOO-IN")
            sequence_numbers_item = route_maps_item.SequenceNumbersItem(sequence=10, type="deny")
            sequence_numbers_item.match.append("extcommunity ECL-EVPN-SOO")
            route_maps_item.sequence_numbers.append(sequence_numbers_item)
            sequence_numbers_item = route_maps_item.SequenceNumbersItem(sequence=20, type="permit")
            route_maps_item.sequence_numbers.append(sequence_numbers_item)
            self.structured_config.route_maps.append(route_maps_item)
            route_maps_item = self.structured_config.RouteMapsItem(name="RM-EVPN-SOO-OUT")
            sequence_numbers_item = route_maps_item.SequenceNumbersItem(sequence=10, type="permit")
            sequence_numbers_item.set.append(f"extcommunity soo {self.shared_utils.evpn_soo} additive")
            route_maps_item.sequence_numbers.append(sequence_numbers_item)
            self.structured_config.route_maps.append(route_maps_item)

            if self.shared_utils.wan_ha:
                route_maps_item = self.structured_config.RouteMapsItem(name="RM-WAN-HA-PEER-IN")
                sequence_numbers_item = route_maps_item.SequenceNumbersItem(
                    sequence=10, type="permit", description="Set tag 50 on routes received from HA peer over EVPN"
                )
                sequence_numbers_item.set.append("tag 50")
                route_maps_item.sequence_numbers.append(sequence_numbers_item)
                self.structured_config.route_maps.append(route_maps_item)
                route_maps_item = self.structured_config.RouteMapsItem(name="RM-WAN-HA-PEER-OUT")
                sequence_numbers_item = route_maps_item.SequenceNumbersItem(
                    sequence=10, type="permit", description="Make EVPN routes learned from WAN less preferred on HA peer"
                )
                sequence_numbers_item.match.append("route-type internal")
                sequence_numbers_item.set.append("local-preference 50")
                route_maps_item.sequence_numbers.append(sequence_numbers_item)
                sequence_numbers_item = route_maps_item.SequenceNumbersItem(
                    sequence=20, type="permit", description="Make locally injected routes less preferred on HA peer"
                )
                sequence_numbers_item.set.append("local-preference 75")
                route_maps_item.sequence_numbers.append(sequence_numbers_item)
                self.structured_config.route_maps.append(route_maps_item)
