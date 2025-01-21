# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils.avdtestbase import AvdTestBase
from ansible_collections.arista.avd.plugins.plugin_utils.utils import default, get

from ..bgp_constants import BGP_ADDRESS_FAMILIES  # noqa: TID252 will be fixed when moving to pyavd

LOGGER = logging.getLogger(__name__)


class AvdTestRoutingTable(AvdTestBase):
    """AvdTestRoutingTable class for routing table entry verification tests."""

    anta_module = "anta.tests.routing.generic"

    @cached_property
    def test_definition(self) -> dict | None:
        """
        Generates the proper ANTA test definition for all routing table entry verification tests.

        Returns:
            test_definition (dict): ANTA test definition.
        """
        anta_tests = []

        def add_test(mapping: list) -> None:
            """
            Add a test with the proper parameters to the anta_tests list.

            Avoids duplicate tests for the same IP address (e.g. MLAG VTEPs).
            """
            processed_ips = set()

            for peer, ip in mapping:
                if not self.is_peer_available(peer):
                    continue

                if ip not in processed_ips:
                    anta_tests.append(
                        {
                            "VerifyRoutingTableEntry": {
                                "routes": [ip],
                                "result_overwrite": {"custom_field": f"Route: {ip} - Peer: {peer}"},
                            },
                        },
                    )
                    processed_ips.add(ip)

        # Skip the test if the host is not a VTEP (no VXLAN interface)
        if get(self.structured_config, "vxlan_interface") is None:
            LOGGER.info("Host is not a VTEP since it doesn't have a VXLAN interface. %s is skipped.", self.__class__.__name__)
            return None
        # TODO: Remove the support of Vxlan1 in AVD 6.0.0 version
        vtep_interface = default(
            get(self.structured_config, "vxlan_interface.vxlan1.vxlan.source_interface"),
            get(self.structured_config, "vxlan_interface.Vxlan1.vxlan.source_interface"),
        )

        # TODO: For now, we exclude WAN VTEPs from testing
        if "Dps" in vtep_interface:
            LOGGER.info("Host is a VTEP with a DPS source interface for VXLAN. For now, WAN VTEPs are excluded. %s is skipped.", self.__class__.__name__)
            return None

        add_test(mapping=self.loopback0_mapping)

        if vtep_interface is not None:
            add_test(mapping=self.vtep_mapping)

        return {self.anta_module: anta_tests} if anta_tests else None


class AvdTestBGP(AvdTestBase):
    """AvdTestBGP class for BGP tests.

    Supports IPv4, IPv6, Path-Selection, Link-State and EVPN address families.
    """

    anta_module = "anta.tests.routing"
    anta_tests = {}  # noqa: RUF012

    def add_test(self, afi: str, bgp_neighbor_ip: str, bgp_peer: str, description: str, safi: str | None = None) -> dict:
        """Add a BGP test definition with the proper input parameters."""
        custom_field = f"BGP {description} Peer: {f'{bgp_peer} (IP: {bgp_neighbor_ip})' if bgp_peer is not None else bgp_neighbor_ip}"

        address_family = {"afi": afi, "peers": [bgp_neighbor_ip]}
        if safi:
            address_family["safi"] = safi

        self.anta_tests.setdefault(f"{self.anta_module}.bgp", []).append(
            {
                "VerifyBGPSpecificPeers": {
                    "address_families": [address_family],
                    "result_overwrite": {"custom_field": custom_field},
                },
            },
        )

    def create_tests(
        self,
        afi: str,
        description: str,
        avd_key: str,
        safi: str | None = None,
    ) -> None:
        """Create BGP tests for the given AFI and SAFI."""
        bgp_neighbors = get(self.structured_config, "router_bgp.neighbors", [])

        # Retrieve peer groups and direct neighbors.
        peer_groups = get(self.structured_config, f"router_bgp.{avd_key}.peer_groups", [])
        direct_neighbors = get(self.structured_config, f"router_bgp.{avd_key}.neighbors", [])

        # Only explicitly activated neighbors and peer groups are tested.
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
            # Check peer availability if the 'peer' key exists. Otherwise, still include the test for potential BGP external peers.
            if peer is not None and not self.is_peer_available(peer):
                continue
            self.add_test(afi=afi, safi=safi, bgp_neighbor_ip=str(ip), bgp_peer=peer, description=description)

    @cached_property
    def test_definition(self) -> dict | None:
        """Generates the proper ANTA test definition for all BGP tests.

        Returns:
        -------
            test_definition (dict): ANTA test definition.

        """
        # Check if BGP configuration is present with multi-agent model
        if self.structured_config.get("router_bgp") is None:
            LOGGER.info("No router bgp configuration found. %s is skipped.", self.__class__.__name__)
            return None

        if not self.validate_data(service_routing_protocols_model="multi-agent", logging_level="WARNING"):
            return None

        self.anta_tests.setdefault(f"{self.anta_module}.generic", []).append(
            {
                "VerifyRoutingProtocolModel": {
                    "model": "multi-agent",
                    "result_overwrite": {"custom_field": "Routing protocol model: multi-agent"},
                },
            },
        )
        # Create tests for IPv4, IPv6, Path-Selection, Link-State and EVPN address families
        for family in BGP_ADDRESS_FAMILIES:
            self.create_tests(**family)

        return self.anta_tests if self.anta_tests.get(f"{self.anta_module}.bgp") else None
