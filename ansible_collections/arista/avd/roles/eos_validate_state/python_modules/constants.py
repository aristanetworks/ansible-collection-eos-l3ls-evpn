# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import Any

from .tests import (
    AvdTestAPIHttpsSSL,
    AvdTestAvtPath,
    AvdTestAvtRole,
    AvdTestBGP,
    AvdTestDpsReachability,
    AvdTestHardware,
    AvdTestInbandReachability,
    AvdTestInterfacesState,
    AvdTestIPSecurity,
    AvdTestLLDPTopology,
    AvdTestLoopback0Reachability,
    AvdTestMLAG,
    AvdTestNTP,
    AvdTestP2PIPReachability,
    AvdTestReloadCause,
    AvdTestRoutingTable,
    AvdTestStun,
)

ACRONYM_CATEGORIES: set[str] = {"aaa", "mlag", "snmp", "bgp", "ospf", "vxlan", "stp", "igmp", "ip", "lldp", "ntp", "bfd", "ptp", "lanz", "stun", "vlan"}
"""
A set of network protocol or feature acronyms that should be represented in uppercase in the eos_validate_state report.
"""

AVD_TEST_CLASSES: dict[str, dict[Any, Any]] = {
    AvdTestHardware: {},
    AvdTestNTP: {},
    AvdTestInterfacesState: {},
    AvdTestLLDPTopology: {},
    AvdTestMLAG: {},
    AvdTestP2PIPReachability: {},
    AvdTestBGP: {},
    AvdTestReloadCause: {},
    AvdTestRoutingTable: {},
    AvdTestInbandReachability: {},
    AvdTestLoopback0Reachability: {},
    AvdTestAPIHttpsSSL: {},
    AvdTestIPSecurity: {},
    AvdTestStun: {},
    AvdTestDpsReachability: {},
    AvdTestAvtPath: {},
    AvdTestAvtRole: {},
}
"""
A dict of all AVD eos_validate_state test classes.

These classes each contains a `test_definition` attribute generated from the AVD structured_config.
"""
