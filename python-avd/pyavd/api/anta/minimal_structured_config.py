# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from dataclasses import dataclass

from pyavd._utils import get


@dataclass(frozen=True)
class MinimalEthernetInterface:
    """A minimal version of an Ethernet interface containing only the required data."""

    name: str
    ip_address: str


@dataclass(frozen=True)
class MinimalStructuredConfig:
    """A minimal version of a device structured configuration containing only the required data."""

    hostname: str
    is_deployed: bool
    dns_domain: str | None
    ethernet_interfaces: list[MinimalEthernetInterface]


def get_minimal_structured_configs(structured_configs: dict[str, dict]) -> dict[str, MinimalStructuredConfig]:
    """Get a minimal version of structured configurations for all devices, loaded in dataclasses."""
    minimal_structured_configs: dict[str, MinimalStructuredConfig] = {}

    for device, structured_config in structured_configs.items():
        # Parse the Ethernet interfaces
        minimal_ethernet_interfaces = [
            MinimalEthernetInterface(name=intf["name"], ip_address=intf_ip)
            for intf in get(structured_config, "ethernet_interfaces", default=[])
            if (intf_ip := get(intf, "ip_address")) and intf_ip != "dhcp" and get(intf, "switchport.enabled") is False
        ]

        # Create the minimal structured configuration
        minimal_structured_configs[device] = MinimalStructuredConfig(
            hostname=structured_config["hostname"],
            is_deployed=get(structured_config, "is_deployed", default=False),
            dns_domain=get(structured_config, "dns_domain"),
            ethernet_interfaces=minimal_ethernet_interfaces,
        )
    return minimal_structured_configs
