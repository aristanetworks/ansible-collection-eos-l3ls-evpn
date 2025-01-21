# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd.j2filters import natural_sort

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigOverlay


class RouteMapsMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def route_maps(self: AvdStructuredConfigOverlay) -> list | None:
        """Return structured config for route_maps."""
        if self.shared_utils.overlay_cvx:
            return None

        route_maps = []

        if self.shared_utils.overlay_routing_protocol == "ebgp":
            if self.inputs.evpn_prevent_readvertise_to_server:
                remote_asns = natural_sort({rs_dict.get("bgp_as") for rs_dict in self._evpn_route_servers.values()})
                for remote_asn in remote_asns:
                    route_map_name = f"RM-EVPN-FILTER-AS{remote_asn}"
                    route_maps.append(
                        {
                            "name": route_map_name,
                            "sequence_numbers": [
                                {
                                    "sequence": 10,
                                    "type": "deny",
                                    "match": [f"as {remote_asn}"],
                                },
                                {
                                    "sequence": 20,
                                    "type": "permit",
                                },
                            ],
                        },
                    )

        elif self.shared_utils.overlay_routing_protocol == "ibgp" and self.shared_utils.overlay_vtep and self.shared_utils.evpn_role != "server":
            # Route-map IN and OUT for SOO
            route_maps.append(
                {
                    "name": "RM-EVPN-SOO-IN",
                    "sequence_numbers": [
                        {
                            "sequence": 10,
                            "type": "deny",
                            "match": ["extcommunity ECL-EVPN-SOO"],
                        },
                        {
                            "sequence": 20,
                            "type": "permit",
                        },
                    ],
                },
            )

            route_maps.append(
                {
                    "name": "RM-EVPN-SOO-OUT",
                    "sequence_numbers": [
                        {
                            "sequence": 10,
                            "type": "permit",
                            "set": [f"extcommunity soo {self.shared_utils.evpn_soo} additive"],
                        },
                    ],
                },
            )

            if self.shared_utils.wan_ha:
                route_maps.append(
                    {
                        "name": "RM-WAN-HA-PEER-IN",
                        "sequence_numbers": [
                            {
                                "sequence": 10,
                                "type": "permit",
                                "description": "Set tag 50 on routes received from HA peer over EVPN",
                                "set": ["tag 50"],
                            },
                        ],
                    },
                )
                route_maps.append(
                    {
                        "name": "RM-WAN-HA-PEER-OUT",
                        "sequence_numbers": [
                            {
                                "sequence": 10,
                                "type": "permit",
                                "description": "Make EVPN routes learned from WAN less preferred on HA peer",
                                "match": ["route-type internal"],
                                "set": ["local-preference 50"],
                            },
                            {
                                "sequence": 20,
                                "type": "permit",
                                "description": "Make locally injected routes less preferred on HA peer",
                                "set": ["local-preference 75"],
                            },
                        ],
                    },
                )

        if route_maps:
            return route_maps

        return None
