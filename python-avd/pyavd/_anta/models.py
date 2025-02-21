# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Data models used by PyAVD for ANTA."""

from __future__ import annotations

from dataclasses import dataclass
from functools import cached_property
from ipaddress import IPv4Address, IPv6Address, ip_interface
from logging import getLogger
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
    from pyavd.api.anta import MinimalStructuredConfig, TestGenerationSettings

LOGGER = getLogger(__name__)


@dataclass(frozen=True)
class BgpNeighbor:
    """Represents a BGP neighbor configuration."""

    ip_address: IPv4Address
    vrf: str
    peer_group: str | None
    peer: str | None = None


@dataclass
class DeviceTestContext:
    """Stores device test context data for ANTA test generation."""

    hostname: str
    structured_config: EosCliConfigGen
    structured_configs: dict[str, MinimalStructuredConfig]
    test_generation_settings: TestGenerationSettings

    @cached_property
    def is_vtep(self) -> bool:
        """Check if the device is a VTEP."""
        return bool(self.structured_config.vxlan_interface.vxlan1.vxlan.source_interface)

    @cached_property
    def is_wan_router(self) -> bool:
        """Check if the device is a WAN router."""
        return self.is_vtep and "Dps" in self.structured_config.vxlan_interface.vxlan1.vxlan.source_interface

    @cached_property
    def bgp_neighbors(self) -> list[BgpNeighbor]:
        """Generate a list of BGP neighbors for the device."""
        neighbors = []
        for neighbor in self.structured_config.router_bgp.neighbors:
            identifier = f"{neighbor.ip_address}" if neighbor.peer is None else f"{neighbor.peer} ({neighbor.ip_address})"

            # Skip neighbors that are shutdown
            if neighbor.shutdown is True:
                LOGGER.debug("<%s>: skipped BGP peer %s - shutdown", self.hostname, identifier)
                continue

            # Skip neighbors in shutdown peer groups
            if (
                neighbor.peer_group
                and neighbor.peer_group in self.structured_config.router_bgp.peer_groups
                and self.structured_config.router_bgp.peer_groups[neighbor.peer_group].shutdown is True
            ):
                LOGGER.debug("<%s>: skipped BGP peer %s - peer group %s shutdown", self.hostname, identifier, neighbor.peer_group)
                continue

            # When peer field is set, check if the peer device is in the fabric and deployed
            if neighbor.peer and (neighbor.peer not in self.structured_configs or not self.structured_configs[neighbor.peer].is_deployed):
                LOGGER.debug("<%s>: skipped BGP peer %s - peer not in fabric or not deployed", self.hostname, identifier)
                continue

            # TODO: IPv6 neighbors are not supported in ANTA yet
            ip_address = ip_interface(neighbor.ip_address).ip
            if isinstance(ip_address, IPv6Address):
                LOGGER.debug("<%s>: skipped BGP peer %s - IPv6 not supported", self.hostname, identifier)
                continue

            neighbors.append(BgpNeighbor(ip_address=ip_address, vrf="default", peer_group=neighbor.peer_group, peer=neighbor.peer))

        if not self.test_generation_settings.allow_bgp_vrfs:
            LOGGER.debug("<%s>: skipped BGP VRF peers - VRF processing disabled", self.hostname)
            return neighbors

        for vrf in self.structured_config.router_bgp.vrfs:
            for neighbor in vrf.neighbors:
                identifier = f"{neighbor.ip_address} (VRF {vrf.name})"

                # Skip neighbors that are shutdown
                if neighbor.shutdown is True:
                    LOGGER.debug("<%s>: skipped BGP peer %s - shutdown", self.hostname, identifier)
                    continue

                # Skip neighbors in shutdown peer groups
                if (
                    neighbor.peer_group
                    and neighbor.peer_group in self.structured_config.router_bgp.peer_groups
                    and self.structured_config.router_bgp.peer_groups[neighbor.peer_group].shutdown is True
                ):
                    LOGGER.debug("<%s>: skipped BGP peer %s - peer group %s shutdown", self.hostname, identifier, neighbor.peer_group)
                    continue

                # TODO: IPv6 neighbors are not supported in ANTA yet
                ip_address = ip_interface(neighbor.ip_address).ip
                if isinstance(ip_address, IPv6Address):
                    LOGGER.debug("<%s>: skipped BGP peer %s - IPv6 not supported", self.hostname, identifier)
                    continue

                neighbors.append(BgpNeighbor(ip_address=ip_address, vrf=vrf.name, peer_group=neighbor.peer_group))

        return neighbors
