# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Models used to build the fabric data for the ANTA tests."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ipaddress import IPv4Address


@dataclass(frozen=True)
class Link:
    """Represents a link between two devices."""

    local_device: str
    local_interface: str
    local_ip: IPv4Address | None
    peer_device: str
    peer_interface: str
    peer_ip: IPv4Address | None
    routed: bool
    validate_lldp: bool


@dataclass(frozen=True)
class Device:
    """Represents a device in the fabric."""

    hostname: str
    is_deployed: bool
    dc_name: str
    pod: str
    rack: str
    loopback0_ip: IPv4Address | None
    vtep_ip: IPv4Address | None
    inband_mgmt_ip: IPv4Address | None
    inband_mgmt_vrf: str
    is_vtep: bool
    is_wan_router: bool
