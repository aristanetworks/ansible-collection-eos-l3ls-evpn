# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Test index for PyAVD ANTA tests."""

from __future__ import annotations

from pyavd._anta.input_factories import *
from pyavd._anta.lib.tests import *
from pyavd.api.anta import TestSpec

from .constants import StructuredConfigKey

PYAVD_TEST_INDEX: list[TestSpec] = [
    TestSpec(
        test_class=VerifyAPIHttpsSSL,
        conditional_keys=[StructuredConfigKey.HTTPS_SSL_PROFILE],
        input_dict={"profile": StructuredConfigKey.HTTPS_SSL_PROFILE},
    ),
    TestSpec(
        test_class=VerifyAVTRole,
        conditional_keys=[StructuredConfigKey.AVT_ROLE],
        input_factory=VerifyAVTRoleInputFactory,
    ),
    TestSpec(
        test_class=VerifyBGPPeerMPCaps,
        conditional_keys=[StructuredConfigKey.ROUTER_BGP],
        input_factory=VerifyBGPPeerMPCapsInputFactory,
    ),
    TestSpec(
        test_class=VerifyBGPPeerSession,
        conditional_keys=[StructuredConfigKey.ROUTER_BGP],
        input_factory=VerifyBGPPeerSessionInputFactory,
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
        test_class=VerifyNTP,
    ),
    TestSpec(
        test_class=VerifyReachability,
        input_factory=VerifyReachabilityInputFactory,
    ),
    TestSpec(
        test_class=VerifyReloadCause,
    ),
    TestSpec(
        test_class=VerifyRoutingProtocolModel,
        conditional_keys=[StructuredConfigKey.SERVICE_ROUTING_PROTOCOLS_MODEL],
        input_dict={"model": StructuredConfigKey.SERVICE_ROUTING_PROTOCOLS_MODEL},
    ),
    TestSpec(
        test_class=VerifySpecificIPSecConn,
        conditional_keys=[StructuredConfigKey.ROUTER_PATH_SELECTION_GROUPS],
        input_factory=VerifySpecificIPSecConnInputFactory,
    ),
    TestSpec(
        test_class=VerifyStunClientTranslation,
        conditional_keys=[StructuredConfigKey.ROUTER_PATH_SELECTION_GROUPS],
        input_factory=VerifyStunClientTranslationInputFactory,
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

PYAVD_TEST_INDEX.sort(key=lambda x: x.test_class.name)
"""Sort the test index by the test class name."""

PYAVD_TEST_NAMES: list[str] = [test.test_class.name for test in PYAVD_TEST_INDEX]
"""List of all available ANTA test names that PyAVD will run by default."""
