# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.eos_validate_state_utils.avdtestbase import AvdTestBase

LOGGER = logging.getLogger(__name__)


class AvdTestMLAG(AvdTestBase):
    """AvdTestMLAG class for MLAG tests."""

    anta_module = "anta.tests.mlag"

    @cached_property
    def test_definition(self) -> dict:
        """
        Generates the proper ANTA test definition for all MLAG tests.

        Returns:
            test_definition (dict): ANTA test definition.
        """
        if self.structured_config.get("mlag_configuration") is None:
            LOGGER.info("No mlag configuration found. %s is skipped.", self.__class__.__name__)
            return None

        anta_tests = [
            {"VerifyMlagStatus": None},
        ]

        return {self.anta_module: anta_tests}
