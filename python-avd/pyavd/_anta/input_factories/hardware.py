# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from anta.tests.hardware import VerifyEnvironmentCooling, VerifyEnvironmentPower, VerifyTransceiversManufacturers

from pyavd._utils import get_v2

from ._base_classes import AntaTestInputFactory


class VerifyEnvironmentPowerInputFactory(AntaTestInputFactory):
    """Input factory class for the VerifyEnvironmentPower test.

    Required config:
      - accepted_pwr_supply_states (default: ["ok"])
    """

    def create(self) -> VerifyEnvironmentPower.Input:
        """Create Input for the VerifyEnvironmentPower test."""
        # TODO: `accepted_pwr_supply_states` is not yet implemented in the AVD EosCliConfigGen schema.
        states = get_v2(self.structured_config, "accepted_pwr_supply_states", default=["ok"])

        return VerifyEnvironmentPower.Input(states=states)


class VerifyEnvironmentCoolingInputFactory(AntaTestInputFactory):
    """Input factory class for the VerifyEnvironmentCooling test.

    Required config:
      - accepted_fan_states (default: ["ok"])
    """

    def create(self) -> VerifyEnvironmentCooling.Input:
        """Create Input for the VerifyEnvironmentCooling test."""
        # TODO: `accepted_fan_states` is not yet implemented in the AVD EosCliConfigGen schema.
        states = get_v2(self.structured_config, "accepted_fan_states", default=["ok"])

        return VerifyEnvironmentCooling.Input(states=states)


class VerifyTransceiversManufacturersInputFactory(AntaTestInputFactory):
    """Input factory class for the VerifyTransceiversManufacturers test.

    Required config:
      - accepted_xcvr_manufacturers (default: ["Arista Networks", "Arastra, Inc."])

    Notes:
      - "Not Present" state is always included
    """

    def create(self) -> VerifyTransceiversManufacturers.Input:
        """Create Input for the VerifyTransceiversManufacturers test."""
        # TODO: `accepted_xcvr_manufacturers` is not yet implemented in the AVD EosCliConfigGen schema.
        manufacturers = get_v2(self.structured_config, "accepted_xcvr_manufacturers", default=["Arista Networks", "Arastra, Inc."])
        manufacturers.append("Not Present")

        return VerifyTransceiversManufacturers.Input(manufacturers=manufacturers)
