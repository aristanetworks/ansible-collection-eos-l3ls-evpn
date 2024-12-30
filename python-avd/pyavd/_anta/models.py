# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Data models used by PyAVD for ANTA."""

from __future__ import annotations

from dataclasses import dataclass
from functools import cached_property
from ipaddress import IPv4Address, IPv6Address, ip_interface
from logging import getLogger
from typing import TYPE_CHECKING, Any, Literal

from pydantic import BaseModel

if TYPE_CHECKING:
    from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
    from pyavd.api.fabric_data import FabricData

LOGGER = getLogger(__name__)


# TODO: Check if we need Pydantic model for this class
class FabricScope(BaseModel):
    """Defines scope and permissions for fabric boundary test input generation."""

    boundary: Literal["unlimited", "fabric", "dc", "pod", "rack"] = "unlimited"
    allow_bgp_external: bool = False
    allow_bgp_vrfs: bool = False


@dataclass(frozen=True)
class BoundaryLocation:
    """Represents device location within fabric hierarchy (fabric->dc->pod->rack)."""

    fabric: str | None = None
    dc: str | None = None
    pod: str | None = None
    rack: str | None = None


@dataclass(frozen=True)
class BgpNeighbor:
    """Represents a BGP neighbor configuration."""

    ip_address: IPv4Address
    vrf: str
    peer_group: str | None
    peer: str | None = None


@dataclass(frozen=True)
class DeviceData:
    """Stores device metadata and network attributes for test input generation."""

    hostname: str
    dns_domain: str | None
    is_deployed: bool
    # TODO: Check if the individual location fields are needed
    fabric_name: str | None
    dc_name: str | None
    pod_name: str | None
    rack: str | None
    boundary_location: BoundaryLocation
    is_vtep: bool
    is_wan_router: bool
    loopback0_ip: IPv4Address | None
    vtep_ip: IPv4Address | None
    # TODO: `interface_to_ip` might be a better name
    ip_by_interface: dict[str, IPv4Address]


@dataclass
class ExtendedDeviceData:
    """Extends DeviceData with structured config and fabric-wide data access."""

    hostname: str
    fabric_data: FabricData
    structured_config: EosCliConfigGen

    def __post_init__(self) -> None:
        self._base: DeviceData = self.fabric_data.devices[self.hostname]

        # Shortcut attributes for easier access and type hinting in the input factories
        self.device = self._base
        self.is_vtep = self._base.is_vtep
        self.is_wan_router = self._base.is_wan_router
        self.loopback0_ip = self._base.loopback0_ip
        self.vtep_ip = self._base.vtep_ip
        self.boundary_location = self._base.boundary_location

    # Forward all other attribute access to the base DeviceData object
    def __getattr__(self, name: str) -> Any:
        return getattr(self._base, name)

    @cached_property
    def bgp_neighbors(self) -> list[BgpNeighbor]:
        """Generate a list of BGP neighbors for the device."""
        neighbors = []
        for neighbor in self.structured_config.router_bgp.neighbors:
            identifier = f"{neighbor.ip_address}" if neighbor.peer is None else f"{neighbor.peer} ({neighbor.ip_address})"

            # Skip neighbors or their peer groups that are shutdown
            if neighbor.shutdown is True:
                LOGGER.debug("<%s>: skipped BGP peer %s - shutdown", self.hostname, identifier)
                continue
            if (
                neighbor.peer_group
                and neighbor.peer_group in self.structured_config.router_bgp.peer_groups
                and self.structured_config.router_bgp.peer_groups[neighbor.peer_group].shutdown is True
            ):
                LOGGER.debug("<%s>: skipped BGP peer %s - peer group %s shutdown", self.hostname, identifier, neighbor.peer_group)
                continue

            # If peer field is set, validate it exists in FabricData, is deployed, and is in the boundary
            if neighbor.peer:
                if neighbor.peer not in self.fabric_data.devices or not self.fabric_data.devices[neighbor.peer].is_deployed:
                    LOGGER.debug("<%s>: skipped BGP peer %s - peer not found or not deployed", self.hostname, identifier)
                    continue
                if (
                    self.fabric_data.scope.boundary != "unlimited"
                    and self.fabric_data.scope.allow_bgp_external is False
                    and neighbor.peer not in self.fabric_data.get_devices_by_attribute("boundary_location", self.device.boundary_location)
                ):
                    LOGGER.debug("<%s>: skipped BGP peer %s - peer outside %s boundary", self.hostname, identifier, self.fabric_data.scope.boundary)
                    continue

            # TODO: IPv6 neighbors are not supported in ANTA yet
            ip_address = ip_interface(neighbor.ip_address).ip
            if isinstance(ip_address, IPv6Address):
                LOGGER.debug("<%s>: skipped BGP peer %s - IPv6 not supported", self.hostname, identifier)
                continue

            neighbors.append(BgpNeighbor(ip_address=ip_address, vrf="default", peer_group=neighbor.peer_group, peer=neighbor.peer))

        if not self.fabric_data.scope.allow_bgp_vrfs:
            LOGGER.debug("<%s>: skipped BGP VRF peers - VRF processing disabled", self.hostname)
            return neighbors

        for vrf in self.structured_config.router_bgp.vrfs:
            for neighbor in vrf.neighbors:
                identifier = f"{neighbor.ip_address} (VRF {vrf.name})"

                # Skip neighbors or their peer groups that are shutdown
                if neighbor.shutdown is True:
                    LOGGER.debug("<%s>: skipped BGP peer %s - shutdown", self.hostname, identifier)
                    continue
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
