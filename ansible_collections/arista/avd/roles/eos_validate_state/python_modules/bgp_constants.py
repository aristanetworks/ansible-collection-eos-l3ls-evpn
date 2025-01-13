# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

BGP_ADDRESS_FAMILIES = [
    {"afi": "evpn", "safi": None, "description": "EVPN", "avd_key": "address_family_evpn"},
    {"afi": "path-selection", "safi": None, "description": "Path-Selection", "avd_key": "address_family_path_selection"},
    {"afi": "link-state", "safi": None, "description": "Link-State", "avd_key": "address_family_link_state"},
    {"afi": "ipv4", "safi": "unicast", "description": "IPv4 Unicast", "avd_key": "address_family_ipv4"},
    {"afi": "ipv6", "safi": "unicast", "description": "IPv6 Unicast", "avd_key": "address_family_ipv6"},
    {"afi": "ipv4", "safi": "sr-te", "description": "IPv4 SR-TE", "avd_key": "address_family_ipv4_sr_te"},
    {"afi": "ipv6", "safi": "sr-te", "description": "IPv6 SR-TE", "avd_key": "address_family_ipv6_sr_te"},
]
"""
List of dictionaries that map the BGP address family identifier (AFI) and the subsequent address family identifier (SAFI) for validation,
description as formatted input messages in the report and avd_key to access address families in structured config.
"""
