# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from pyavd._utils import get

from ._base_classes import AntaTestInputFactory

if TYPE_CHECKING:
    from anta.tests.hardware import VerifyEnvironmentCooling, VerifyEnvironmentPower, VerifyTransceiversManufacturers


class VerifyEnvironmentPowerInputFactory(AntaTestInputFactory):
    """Input factory class for the VerifyEnvironmentPower test.

    This factory creates test inputs for power supply status verification.

    It collects accepted power supply states:
      - Default accepted state is `ok`
      - Additional states can be defined in `accepted_pwr_supply_states`

    TODO: `accepted_pwr_supply_states` is not yet implemented in the AVD structured config schema.
    """

    def create(self) -> VerifyEnvironmentPower.Input:
        """Create Input for the VerifyEnvironmentPower test."""
        pwr_supply_states = get(self.manager.structured_config, "accepted_pwr_supply_states", ["ok"])

        return self.test.Input(states=pwr_supply_states)


class VerifyEnvironmentCoolingInputFactory(AntaTestInputFactory):
    """Input factory class for the VerifyEnvironmentCooling test.

    This factory creates test inputs for cooling system status verification.

    It collects accepted fan states:
      - Default accepted state is `ok`
      - Additional states can be defined in `accepted_fan_states`

    TODO: `accepted_fan_states` is not yet implemented in the AVD structured config schema.
    """

    def create(self) -> VerifyEnvironmentCooling.Input:
        """Create Input for the VerifyEnvironmentCooling test."""
        fan_states = get(self.manager.structured_config, "accepted_fan_states", ["ok"])

        return self.test.Input(states=fan_states)


class VerifyTransceiversManufacturersInputFactory(AntaTestInputFactory):
    """Input factory class for the VerifyTransceiversManufacturers test.

    This factory creates test inputs for transceiver manufacturer verification.

    It collects accepted manufacturer names:
      - Default accepted manufacturers are `Arista Networks` and `Arastra, Inc.`
      - Additional manufacturers can be defined in `accepted_xcvr_manufacturers`
      - `Not Present` state is always included

    TODO: `accepted_xcvr_manufacturers` is not yet implemented in the AVD structured config schema.
    """

    def create(self) -> VerifyTransceiversManufacturers.Input:
        """Create Input for the VerifyTransceiversManufacturers test."""
        xcvr_manufacturers = get(self.manager.structured_config, "accepted_xcvr_manufacturers", ["Arista Networks", "Arastra, Inc."])
        xcvr_manufacturers.append("Not Present")

        return self.test.Input(manufacturers=xcvr_manufacturers)
