# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

INTERFACE_MODELS = [
    "ethernet_interfaces",
    "port_channel_interfaces",
    "vlan_interfaces",
    "loopback_interfaces",
    "dps_interfaces",
]
"""List of interface models from the structured configurations that are used for testing."""

BGP_MAPPINGS = [
    {"afi": "evpn", "safi": None, "description": "EVPN", "avd_key": "address_family_evpn"},
    {"afi": "path-selection", "safi": None, "description": "Path-Selection", "avd_key": "address_family_path_selection"},
    {"afi": "link-state", "safi": None, "description": "Link-State", "avd_key": "address_family_link_state"},
    {"afi": "ipv4", "safi": "unicast", "description": "IPv4 Unicast", "avd_key": "address_family_ipv4"},
    {"afi": "ipv6", "safi": "unicast", "description": "IPv6 Unicast", "avd_key": "address_family_ipv6"},
    {"afi": "ipv4", "safi": "sr-te", "description": "IPv4 SR-TE", "avd_key": "address_family_ipv4_sr_te"},
    {"afi": "ipv6", "safi": "sr-te", "description": "IPv6 SR-TE", "avd_key": "address_family_ipv6_sr_te"},
]
"""
List of dictionaries that maps the BGP Address Family Identifier (AFI) and the Subsequent Address Family Identifier (SAFI) for validation.
Each dictionary includes a description formatted for input messages in the report and an avd_key to access the address families in the structured configuration.
"""
