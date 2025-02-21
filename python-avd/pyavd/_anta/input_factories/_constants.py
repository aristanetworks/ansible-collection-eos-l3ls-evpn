# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

DEFAULT_VRF_ADDRESS_FAMILIES = {
    "address_family_evpn": "l2VpnEvpn",
    "address_family_flow_spec_ipv4": "ipv4FlowSpec",
    "address_family_flow_spec_ipv6": "ipv6FlowSpec",
    "address_family_ipv4": "ipv4Unicast",
    "address_family_ipv4_labeled_unicast": "ipv4MplsLabels",
    "address_family_ipv4_multicast": "ipv4Multicast",
    "address_family_ipv4_sr_te": "ipv4SrTe",
    "address_family_ipv6": "ipv6Unicast",
    "address_family_ipv6_multicast": "ipv6Multicast",
    "address_family_ipv6_sr_te": "ipv6SrTe",
    "address_family_link_state": "linkState",
    "address_family_path_selection": "dps",
    "address_family_rtc": "rtMembership",
    "address_family_vpn_ipv4": "ipv4MplsVpn",
    "address_family_vpn_ipv6": "ipv6MplsVpn",
}
"""Supported BGP address families for the default VRF in AVD."""

VRF_ADDRESS_FAMILIES = {
    "address_family_flow_spec_ipv4": "ipv4FlowSpec",
    "address_family_flow_spec_ipv6": "ipv6FlowSpec",
    "address_family_ipv4": "ipv4Unicast",
    "address_family_ipv4_multicast": "ipv4Multicast",
    "address_family_ipv6": "ipv6Unicast",
    "address_family_ipv6_multicast": "ipv6Multicast",
}
"""Supported BGP address families for non-default VRFs in AVD."""
