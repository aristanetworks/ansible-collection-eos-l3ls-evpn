# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._utils import get

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlayProtocol


class RouteMapsMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def route_maps(self: AvdStructuredConfigUnderlayProtocol) -> None:
        """
        Set structured config for route_maps.

        Contains two parts.
        - Route map for connected routes redistribution in BGP
        - Route map to filter peer AS in underlay
        """
        if not self.shared_utils.underlay_bgp and not self.shared_utils.is_wan_router:
            return

        if self.shared_utils.overlay_routing_protocol != "none" and self.inputs.underlay_filter_redistribute_connected:
            # RM-CONN-2-BGP
            sequence_numbers = EosCliConfigGen.RouteMapsItem.SequenceNumbers()
            sequence_10 = EosCliConfigGen.RouteMapsItem.SequenceNumbersItem(
                sequence=10, type="permit", match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY"])
            )
            if self.shared_utils.wan_role:
                sequence_10.set = EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Set([f"extcommunity soo {self.shared_utils.evpn_soo} additive"])

            sequence_numbers.append(sequence_10)
            # SEQ 20 is set by inband management if applicable, so avoid setting that here

            if self.shared_utils.underlay_ipv6 is True:
                sequence_numbers.append_new(
                    sequence=30,
                    type="permit",
                    match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ipv6 address prefix-list PL-LOOPBACKS-EVPN-OVERLAY-V6"]),
                )

            if self.shared_utils.underlay_multicast_rp_interfaces is not None:
                sequence_numbers.append_new(
                    sequence=40,
                    type="permit",
                    match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ip address prefix-list PL-LOOPBACKS-PIM-RP"]),
                )

            if self.shared_utils.wan_ha and self.shared_utils.use_uplinks_for_wan_ha:
                sequence_numbers.append_new(
                    sequence=50,
                    type="permit",
                    match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ip address prefix-list PL-WAN-HA-PREFIXES"]),
                )

            add_p2p_links = False
            for peer in self._avd_peers:
                peer_facts = self.shared_utils.get_peer_facts(peer, required=True)
                for uplink in peer_facts["uplinks"]:
                    if (
                        uplink["peer"] == self.shared_utils.hostname
                        and uplink["type"] == "underlay_p2p"
                        and uplink.get("ip_address")
                        and "unnumbered" not in uplink["ip_address"]
                        and get(peer_facts, "inband_ztp")
                    ):
                        add_p2p_links = True
                        break
                if add_p2p_links:
                    break
            if add_p2p_links:
                sequence_numbers.append_new(
                    sequence=70,
                    type="permit",
                    match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ip address prefix-list PL-P2P-LINKS"]),
                )

            self.structured_config.route_maps.append_new(name="RM-CONN-2-BGP", sequence_numbers=sequence_numbers)

        # RM-BGP-AS{{ asn }}-OUT
        for asn in self._underlay_filter_peer_as_route_maps_asns:
            route_map_name = f"RM-BGP-AS{asn}-OUT"
            sequence_numbers = EosCliConfigGen.RouteMapsItem.SequenceNumbers()
            sequence_numbers.append_new(sequence=10, type="deny", match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match([f"as {asn}"]))
            sequence_numbers.append_new(sequence=20, type="permit")
            self.structured_config.route_maps.append_new(name=route_map_name, sequence_numbers=sequence_numbers)

        # Route-map IN and OUT for SOO, rendered for WAN routers
        if self.shared_utils.underlay_routing_protocol == "ebgp" and self.shared_utils.wan_role == "client":
            # RM-BGP-UNDERLAY-PEERS-IN
            sequence_numbers = EosCliConfigGen.RouteMapsItem.SequenceNumbers()
            sequence_numbers.append_new(
                sequence=40,
                type="permit",
                set=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Set([f"extcommunity soo {self.shared_utils.evpn_soo} additive"]),
                description="Mark prefixes originated from the LAN",
            )
            if self.shared_utils.wan_ha and self.shared_utils.use_uplinks_for_wan_ha:
                sequence_numbers.append_new(
                    sequence=10,
                    type="permit",
                    match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["ip address prefix-list PL-WAN-HA-PEER-PREFIXES"]),
                    description="Allow WAN HA peer interface prefixes",
                )
                sequence_numbers.append_new(
                    sequence=20,
                    type="deny",
                    match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["as-path ASPATH-WAN"]),
                    description="Deny other routes from the HA peer",
                )

            self.structured_config.route_maps.append_new(name="RM-BGP-UNDERLAY-PEERS-IN", sequence_numbers=sequence_numbers)

            # RM-BGP-UNDERLAY-PEERS-OUT
            if self.shared_utils.wan_ha:
                sequence_numbers = EosCliConfigGen.RouteMapsItem.SequenceNumbers()
                sequence_numbers.append_new(
                    sequence=10,
                    type="permit",
                    match=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Match(["tag 50", "route-type internal"]),
                    description="Make routes learned from WAN HA peer less preferred on LAN routers",
                    set=EosCliConfigGen.RouteMapsItem.SequenceNumbersItem.Set(["metric 50"]),
                )
                sequence_numbers.append_new(sequence=20, type="permit")

                self.structured_config.route_maps.append_new(name="RM-BGP-UNDERLAY-PEERS-OUT", sequence_numbers=sequence_numbers)
