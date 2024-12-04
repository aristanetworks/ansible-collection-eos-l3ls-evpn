# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from pyavd._anta.utils import LogMessage
from pyavd._utils import get

from ._base_classes import AntaTestInputFactory
from ._constants import BGP_MAPPINGS

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
                if peer is not None and not self.manager.is_peer_available(peer):
                    self.logger.debug(LogMessage.UNAVAILABLE_PEER, entity=f"{ip} ({bgp_mapping['description']})", peer=peer)
                    continue
                peers.append(ip)

            if peers:
                address_families.append(self.test.Input.BgpAfi(afi=bgp_mapping["afi"], safi=bgp_mapping["safi"], peers=peers))

        return self.test.Input(address_families=address_families) if address_families else None
