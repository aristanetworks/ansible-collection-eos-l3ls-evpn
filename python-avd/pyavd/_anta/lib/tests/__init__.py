# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Centralized package to import all the tests of the ANTA framework."""

from anta.tests.connectivity import VerifyLLDPNeighbors, VerifyReachability
from anta.tests.hardware import (
    VerifyEnvironmentCooling,
    VerifyEnvironmentPower,
    VerifyEnvironmentSystemCooling,
    VerifyTemperature,
    VerifyTransceiversManufacturers,
    VerifyTransceiversTemperature,
)
from anta.tests.interfaces import VerifyInterfacesStatus
from anta.tests.mlag import VerifyMlagStatus
from anta.tests.routing.bgp import VerifyBGPSpecificPeers
from anta.tests.routing.generic import VerifyRoutingTableEntry
from anta.tests.security import VerifyAPIHttpsSSL

__all__ = [
    "VerifyLLDPNeighbors",
    "VerifyReachability",
    "VerifyEnvironmentCooling",
    "VerifyEnvironmentPower",
    "VerifyEnvironmentSystemCooling",
    "VerifyTemperature",
    "VerifyTransceiversManufacturers",
    "VerifyTransceiversTemperature",
    "VerifyInterfacesStatus",
    "VerifyMlagStatus",
    "VerifyBGPSpecificPeers",
    "VerifyRoutingTableEntry",
    "VerifyAPIHttpsSSL",
]
