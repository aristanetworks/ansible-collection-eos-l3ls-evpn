# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import Field

from pyavd._anta.utils import LogMessage
from pyavd._utils import get

from ._base_classes import AntaTestInputFactory, AntaTestInputFactoryFilter
from ._constants import BGP_MAPPINGS
from ._filter_models import BgpAddressFamily

if TYPE_CHECKING:
    from anta.tests.routing.bgp import VerifyBGPSpecificPeers


class VerifyBGPSpecificPeersInputFactory(AntaTestInputFactory):
    """Input factory class for the VerifyBGPSpecificPeers test.

    This factory creates test inputs for BGP address families peer verification.

    It collects BGP peers that should be established for:
      - These configured address families: EVPN, IPv4/IPv6 Unicast, Path-Selection, Link-State, SR-TE
      - Both peer group and direct neighbor configurations

    The factory ensures:
      - Only explicitly activated peers and peer groups are tested
      - Only peers that are available (`is_deployed: true`) are included
      - External BGP peers (not configured by AVD) without 'peer' key are still honored and included
      - Peer collection is skipped for address families with no peers

    TODO: Add support for BGP VRFs
    """

    class Filter(AntaTestInputFactoryFilter):
        """Filter model for the VerifyBGPSpecificPeers test.

        This filter allows excluding peers and specific address families from the test.
        """

        exclude_peers: list[str] = Field(default_factory=list, description="List of peers to exclude from the test.", examples=["DC1-LEAF1A", "DC1-LEAF1B"])
        exclude_address_families: list[BgpAddressFamily] = Field(
            default_factory=list,
            description="List of BGP address families to exclude from the test.",
            examples=[{"afi": "ipv4", "safi": "unicast", "peers": ["10.0.0.1", "10.0.0.2"]}],
        )

    def _create_address_family(self, afi: str, safi: str | None, peers: list[str]) -> VerifyBGPSpecificPeers.Input.BgpAfi | None:
        """Create an address family input for the VerifyBGPSpecificPeers test, considering `input_filter`."""
        # If no address family filters are defined, return the input as is
        if not (exclude_address_families := getattr(self.input_filter, "exclude_address_families", [])):
            return self.test.Input.BgpAfi(afi=afi, safi=safi, peers=peers)

        # Find all matching filters based on the AFI and SAFI
        matching_filters = [f for f in exclude_address_families if (f.afi, f.safi) == (afi, safi)]

        # If we found matching filters, remove all filter peers from actual peers
        if matching_filters:
            filter_peers_set = set().union(*(set(f.peers) for f in matching_filters))
            peers = [peer for peer in peers if peer not in filter_peers_set]

        return self.test.Input.BgpAfi(afi=afi, safi=safi, peers=peers) if peers else None

    def create(self) -> VerifyBGPSpecificPeers.Input | None:
        """Create Input for the VerifyBGPSpecificPeers test."""
        address_families = []
        bgp_neighbors = get(self.manager.structured_config, "router_bgp.neighbors", [])

        for bgp_mapping in BGP_MAPPINGS:
            # Retrieve peer groups and direct neighbors
            peer_groups = get(self.manager.structured_config, f"router_bgp.{bgp_mapping['avd_key']}.peer_groups", [])
            direct_neighbors = get(self.manager.structured_config, f"router_bgp.{bgp_mapping['avd_key']}.neighbors", [])

            # Only explicitly activated neighbors and peer groups are tested
            filtered_peer_groups = [peer_group["name"] for peer_group in peer_groups if peer_group.get("activate")]
            filtered_neighbors = [neighbor["ip_address"] for neighbor in direct_neighbors if neighbor.get("activate")]

            # Combine neighbors from peer groups and direct neighbors
            all_neighbors = [
                (neighbor["ip_address"], neighbor.get("peer"))
                for neighbor in bgp_neighbors
                if neighbor.get("peer_group") in filtered_peer_groups or neighbor["ip_address"] in filtered_neighbors
            ]

            # Gather all available peers for the address family
            peers = []
            for ip, peer in all_neighbors:
                # Check peer availability if the 'peer' key exists. Otherwise, still include the test for potential BGP external peers
                if peer is not None:
                    if not self.manager.is_peer_available(peer):
                        self.logger.debug(LogMessage.UNAVAILABLE_PEER, entity=f"{ip} ({bgp_mapping['description']})", peer=peer)
                        continue
                    if self.is_peer_filtered(peer):
                        self.logger.debug(LogMessage.FILTERED_PEER, entity=f"{ip} ({bgp_mapping['description']})", peer=peer)
                        continue

                peers.append(ip)

            if peers:
                filtered_address_family = self._create_address_family(bgp_mapping["afi"], bgp_mapping["safi"], peers)
                if filtered_address_family:
                    address_families.append(filtered_address_family)

        return self.test.Input(address_families=address_families) if address_families else None
