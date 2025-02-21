# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
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

        if self.shared_utils.overlay_routing_protocol == "ebgp" and self.inputs.evpn_prevent_readvertise_to_server:
            remote_asns = natural_sort({rs_dict.get("bgp_as") for rs_dict in self._evpn_route_servers.values()})
            for remote_asn in remote_asns:
                route_maps_item = EosCliConfigGen.RouteMapsItem(name=f"RM-EVPN-FILTER-AS{remote_asn}")
                route_maps_item.sequence_numbers.append_new(
                    sequence=10, type="deny", match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match([f"as {remote_asn}"])
                )
                route_maps_item.sequence_numbers.append_new(sequence=20, type="permit")
                self.structured_config.route_maps.append(route_maps_item)

        if (
            self.shared_utils.overlay_routing_protocol == "ibgp" and self.shared_utils.overlay_vtep and self.shared_utils.evpn_role != "server"
        ) or self.shared_utils.is_wan_client:
            # Route-map IN and OUT for SOO

            route_maps_item = EosCliConfigGen.RouteMapsItem(name="RM-EVPN-SOO-IN")
            route_maps_item.sequence_numbers.append_new(
                sequence=10, type="deny", match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["extcommunity ECL-EVPN-SOO"])
            )
            route_maps_item.sequence_numbers.append_new(sequence=20, type="permit")
            self.structured_config.route_maps.append(route_maps_item)

            route_maps_item = EosCliConfigGen.RouteMapsItem(name="RM-EVPN-SOO-OUT")
            route_maps_item.sequence_numbers.append_new(
                sequence=10,
                type="permit",
                set=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Set([f"extcommunity soo {self.shared_utils.evpn_soo} additive"]),
            )
            self.structured_config.route_maps.append(route_maps_item)

            if self.shared_utils.wan_ha:
                route_maps_item = EosCliConfigGen.RouteMapsItem(name="RM-WAN-HA-PEER-IN")
                route_maps_item.sequence_numbers.append_new(
                    sequence=10,
                    type="permit",
                    description="Set tag 50 on routes received from HA peer over EVPN",
                    set=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Set(["tag 50"]),
                )
                self.structured_config.route_maps.append(route_maps_item)
                route_maps_item = EosCliConfigGen.RouteMapsItem(name="RM-WAN-HA-PEER-OUT")
                route_maps_item.sequence_numbers.append_new(
                    sequence=10,
                    type="permit",
                    match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["route-type internal"]),
                    set=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Set(["local-preference 50"]),
                    description="Make EVPN routes learned from WAN less preferred on HA peer",
                )
                route_maps_item.sequence_numbers.append_new(
                    sequence=20,
                    type="permit",
                    description="Make locally injected routes less preferred on HA peer",
                    set=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Set(["local-preference 75"]),
                )
                self.structured_config.route_maps.append(route_maps_item)
