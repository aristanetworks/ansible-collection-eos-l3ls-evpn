# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

# TODO: Add support for other address families
DEFAULT_VRF_ADDRESS_FAMILIES = {
    "address_family_evpn": "l2VpnEvpn",
    "address_family_path_selection": "dps",
    "address_family_link_state": "linkState",
    "address_family_ipv4": "ipv4Unicast",
    "address_family_ipv6": "ipv6Unicast",
    "address_family_ipv4_sr_te": "ipv4SrTe",
    "address_family_ipv6_sr_te": "ipv6SrTe",
}
"""Supported BGP address families for the default VRF."""

# TODO: Add support for other VRF address families
VRF_ADDRESS_FAMILIES = {
    "address_family_ipv4": "ipv4Unicast",
    "address_family_ipv6": "ipv6Unicast",
}
"""Supported BGP address families for non-default VRFs."""
