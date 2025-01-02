# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils.avdtestbase import AvdTestBase
from ansible_collections.arista.avd.plugins.plugin_utils.utils import get


class AvdTestHardware(AvdTestBase):
    """AvdTestHardware class for hardware tests."""

    anta_module = "anta.tests.hardware"

    @staticmethod
    def format_list(list_to_format: list) -> str:
        """Return a formatted string of a list of string."""
        return ", ".join(f"'{s}'" for s in list_to_format)

    @cached_property
    def test_definition(self) -> dict:
        """
        Generates the proper ANTA test definition for all hardware tests.

        Returns:
            test_definition (dict): ANTA test definition.
        """
        pwr_supply_states = get(self.structured_config, "accepted_pwr_supply_states", ["ok"])
        fan_states = get(self.structured_config, "accepted_fan_states", ["ok"])
        xcvr_manufacturers = get(self.structured_config, "accepted_xcvr_manufacturers", ["Arista Networks", "Arastra, Inc."])
        xcvr_manufacturers.append("Not Present")

        anta_tests = [
            {
                "VerifyEnvironmentPower": {
                    "states": pwr_supply_states,
                    "result_overwrite": {"custom_field": f"Accepted States: {self.format_list(pwr_supply_states)}"},
                },
            },
            {
                "VerifyEnvironmentCooling": {
                    "states": fan_states,
                    "result_overwrite": {"custom_field": f"Accepted States: {self.format_list(fan_states)}"},
                },
            },
            {"VerifyTemperature": None},
            {
                "VerifyTransceiversManufacturers": {
                    "manufacturers": xcvr_manufacturers,
                    "result_overwrite": {"custom_field": f"Accepted Manufacturers: {self.format_list(xcvr_manufacturers)}"},
                },
            },
        ]

        return {self.anta_module: anta_tests}
