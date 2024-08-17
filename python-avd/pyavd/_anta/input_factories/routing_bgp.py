# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections import defaultdict
from typing import TYPE_CHECKING

from pyavd._anta.utils import LogMessage
from pyavd._utils import get

from .constants import BGP_MAPPINGS

if TYPE_CHECKING:
    from anta.tests.routing.bgp import VerifyBGPSpecificPeers

    from pyavd._anta.utils import ConfigManager, TestLoggerAdapter


class VerifyBGPSpecificPeersInputFactory:
    """Input factory class for the VerifyBGPSpecificPeers test."""

    @classmethod
    def create(cls, test: type[VerifyBGPSpecificPeers], manager: ConfigManager, logger: TestLoggerAdapter) -> VerifyBGPSpecificPeers.Input | None:
        """Create Input for the VerifyBGPSpecificPeers test."""
        address_families = defaultdict(lambda: {"peers": []})

        for bgp_mapping in BGP_MAPPINGS:
            bgp_neighbors = get(manager.structured_config, "router_bgp.neighbors", [])

            # Retrieve peer groups and direct neighbors
            peer_groups = get(manager.structured_config, f"router_bgp.{bgp_mapping['avd_key']}.peer_groups", [])
            direct_neighbors = get(manager.structured_config, f"router_bgp.{bgp_mapping['avd_key']}.neighbors", [])

            # Only explicitly activated neighbors and peer groups are tested
            filtered_peer_groups = [peer_group["name"] for peer_group in peer_groups if peer_group.get("activate")]
            filtered_neighbors = [neighbor["ip_address"] for neighbor in direct_neighbors if neighbor.get("activate")]

            # Combine neighbors from peer groups and direct neighbors
            all_neighbors = [
                (neighbor["ip_address"], neighbor.get("peer"))
                for neighbor in bgp_neighbors
                if neighbor.get("peer_group") in filtered_peer_groups or neighbor["ip_address"] in filtered_neighbors
            ]

            # Add tests for all neighbors
            for ip, peer in all_neighbors:
                # Check peer availability if the 'peer' key exists. Otherwise, still include the test for potential BGP external peers
                if peer is not None and not manager.is_peer_available(peer):
                    logger.info(LogMessage.UNAVAILABLE_PEER, entity=f"{ip} ({bgp_mapping['description']})", peer=peer)
                    continue

                # Add the peer IP address to the corresponding address family
                key = (bgp_mapping["afi"], bgp_mapping["safi"])
                address_families[key]["afi"] = bgp_mapping["afi"]
                if bgp_mapping["safi"]:
                    address_families[key]["safi"] = bgp_mapping["safi"]
                address_families[key]["peers"].append(ip)

        inputs = [test.Input.BgpAfi(**bgp_afi) for bgp_afi in address_families.values()]

        return test.Input(address_families=inputs) if inputs else None
