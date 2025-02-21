# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from anta.tests.hardware import VerifyEnvironmentCooling, VerifyEnvironmentPower, VerifyTransceiversManufacturers

from pyavd._utils import get_v2
from pyavd.j2filters import natural_sort

from ._base_classes import AntaTestInputFactory


class VerifyEnvironmentPowerInputFactory(AntaTestInputFactory):
    """Input factory class for the VerifyEnvironmentPower test.

    This factory generates test inputs for verifying the power supply states.

    The test verifies that the power supply states are 'ok'.

    Other states will be configurable in the future.
    """

    def create(self) -> VerifyEnvironmentPower.Input:
        """Create Input for the VerifyEnvironmentPower test."""
        # TODO: `accepted_pwr_supply_states` is not yet implemented in the AVD EosCliConfigGen schema.
        states = get_v2(self.structured_config, "accepted_pwr_supply_states", default=["ok"])

        return VerifyEnvironmentPower.Input(states=natural_sort(states))


class VerifyEnvironmentCoolingInputFactory(AntaTestInputFactory):
    """Input factory class for the VerifyEnvironmentCooling test.

    This factory generates test inputs for verifying the fan states.

    The test verifies that the fan states are 'ok'.

    Other states will be configurable in the future.
    """

    def create(self) -> VerifyEnvironmentCooling.Input:
        """Create Input for the VerifyEnvironmentCooling test."""
        # TODO: `accepted_fan_states` is not yet implemented in the AVD EosCliConfigGen schema.
        states = get_v2(self.structured_config, "accepted_fan_states", default=["ok"])

        return VerifyEnvironmentCooling.Input(states=natural_sort(states))


class VerifyTransceiversManufacturersInputFactory(AntaTestInputFactory):
    """Input factory class for the VerifyTransceiversManufacturers test.

    This factory generates test inputs for verifying the transceiver manufacturers.

    The test verifites that the transceiver manufacturers are 'Arista Networks' and 'Arastra, Inc.'.

    Other manufacturers will be configurable in the future.

    'Not Present' state is always included.
    """

    def create(self) -> VerifyTransceiversManufacturers.Input:
        """Create Input for the VerifyTransceiversManufacturers test."""
        # TODO: `accepted_xcvr_manufacturers` is not yet implemented in the AVD EosCliConfigGen schema.
        manufacturers = get_v2(self.structured_config, "accepted_xcvr_manufacturers", default=["Arista Networks", "Arastra, Inc."])
        manufacturers.append("Not Present")

        return VerifyTransceiversManufacturers.Input(manufacturers=natural_sort(manufacturers))
