# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from pyavd._utils import get

if TYPE_CHECKING:
    from anta.tests.hardware import VerifyEnvironmentCooling, VerifyEnvironmentPower, VerifyTransceiversManufacturers

    from pyavd._anta.utils import ConfigManager, TestLoggerAdapter


class VerifyEnvironmentPowerInputFactory:
    """Input factory class for the VerifyEnvironmentPower test."""

    @classmethod
    def create(cls, test: type[VerifyEnvironmentPower], manager: ConfigManager, logger: TestLoggerAdapter) -> VerifyEnvironmentPower.Input:
        """Create Input for the VerifyEnvironmentPower test."""
        _ = logger

        pwr_supply_states = get(manager.structured_config, "accepted_pwr_supply_states", ["ok"])

        return test.Input(states=pwr_supply_states)


class VerifyEnvironmentCoolingInputFactory:
    """Input factory class for the VerifyEnvironmentCooling test."""

    @classmethod
    def create(cls, test: type[VerifyEnvironmentCooling], manager: ConfigManager, logger: TestLoggerAdapter) -> VerifyEnvironmentCooling.Input:
        """Create Input for the VerifyEnvironmentCooling test."""
        _ = logger

        fan_states = get(manager.structured_config, "accepted_fan_states", ["ok"])

        return test.Input(states=fan_states)


class VerifyTransceiversManufacturersInputFactory:
    """Input factory class for the VerifyTransceiversManufacturers test."""

    @classmethod
    def create(cls, test: type[VerifyTransceiversManufacturers], manager: ConfigManager, logger: TestLoggerAdapter) -> VerifyTransceiversManufacturers.Input:
        """Create Input for the VerifyTransceiversManufacturers test."""
        _ = logger

        xcvr_manufacturers = get(manager.structured_config, "accepted_xcvr_manufacturers", ["Arista Networks", "Arastra, Inc."])
        xcvr_manufacturers.append("Not Present")

        return test.Input(manufacturers=xcvr_manufacturers)
