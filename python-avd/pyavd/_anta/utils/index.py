# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from pyavd._anta.input_factories import *
from pyavd._anta.lib.tests import *
from pyavd.api.anta_test_spec import TestSpec

from .constants import StructuredConfigKey

PYAVD_TEST_INDEX: list[TestSpec] = [
    TestSpec(
        test_class=VerifyAPIHttpsSSL,
        conditional_keys=[StructuredConfigKey.HTTPS_SSL_PROFILE],
        input_dict={"profile": StructuredConfigKey.HTTPS_SSL_PROFILE},
    ),
    TestSpec(
        test_class=VerifyBGPSpecificPeers,
        conditional_keys=[StructuredConfigKey.ROUTER_BGP],
        input_factory=VerifyBGPSpecificPeersInputFactory,
    ),
    TestSpec(
        test_class=VerifyEnvironmentCooling,
        input_factory=VerifyEnvironmentCoolingInputFactory,
    ),
    TestSpec(
        test_class=VerifyEnvironmentPower,
        input_factory=VerifyEnvironmentPowerInputFactory,
    ),
    TestSpec(
        test_class=VerifyEnvironmentSystemCooling,
    ),
    TestSpec(
        test_class=VerifyInterfacesStatus,
        input_factory=VerifyInterfacesStatusInputFactory,
    ),
    TestSpec(
        test_class=VerifyLLDPNeighbors,
        conditional_keys=[StructuredConfigKey.ETHERNET_INTERFACES],
        input_factory=VerifyLLDPNeighborsInputFactory,
    ),
    TestSpec(
        test_class=VerifyMlagStatus,
        conditional_keys=[StructuredConfigKey.MLAG_CONFIGURATION],
    ),
    TestSpec(
        test_class=VerifyReachability,
        input_factory=VerifyReachabilityInputFactory,
    ),
    TestSpec(
        test_class=VerifyRoutingTableEntry,
        input_factory=VerifyRoutingTableEntryInputFactory,
    ),
    TestSpec(
        test_class=VerifyTemperature,
    ),
    TestSpec(
        test_class=VerifyTransceiversManufacturers,
        input_factory=VerifyTransceiversManufacturersInputFactory,
    ),
    TestSpec(
        test_class=VerifyTransceiversTemperature,
    ),
]
"""List of all ANTA tests with their specifications that PyAVD will run by default."""
