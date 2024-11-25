# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from ipaddress import IPv4Address, IPv6Address
from typing import Literal

from pydantic import BaseModel


class BgpAddressFamily(BaseModel):
    """BgpAddressFamily model used to define a BGP address family to filter."""

    afi: Literal["evpn", "path-selection", "link-state", "ipv4", "ipv6"]
    safi: Literal["unicast", "sr-te"] | None = None
    peers: list[IPv4Address | IPv6Address]
