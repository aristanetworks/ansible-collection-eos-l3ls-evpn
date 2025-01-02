# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from .mixins import DeviceUtilsMixin, ValidationMixin

if TYPE_CHECKING:
    from collections.abc import Mapping

    from .config_manager import ConfigManager

LOGGER = logging.getLogger(__name__)


class AvdTestBase(DeviceUtilsMixin, ValidationMixin):
    """Base class for all AVD eos_validate_state tests."""

    def __init__(self, config_manager: ConfigManager) -> None:
        """Initialize the AvdTestBase class.

        Args:
        ----
            config_manager (ConfigManager): The ConfigManager instance for the device.
        """
        self.config_manager = config_manager

    @property
    def device_name(self) -> str:
        """Return the device name from the ConfigManager instance."""
        return self.config_manager.device_name

    @property
    def hostvars(self) -> Mapping:
        """Return the hostvars from the ConfigManager instance."""
        return self.config_manager.hostvars

    @property
    def structured_config(self) -> Mapping:
        """Return the structured_config from the ConfigManager instance."""
        return self.config_manager.structured_config

    @property
    def loopback0_mapping(self) -> list[tuple[str, str]]:
        """Return the loopback0_mapping from the ConfigManager instance."""
        return self.config_manager.loopback0_mapping

    @property
    def vtep_mapping(self) -> list[tuple[str, str]]:
        """Return the vtep_mapping from the ConfigManager instance."""
        return self.config_manager.vtep_mapping

    @property
    def dps_mapping(self) -> list[tuple[str, str]]:
        """Return the dps_mapping from the ConfigManager instance."""
        return self.config_manager.dps_mapping

    def render(self) -> dict:
        """Return the test_definition of the class.

        This method attempts to retrieve the value of the `test_definition` attribute.
        If `test_definition` is not set or returns a falsy value (e.g., None),
        an empty dictionary will be returned instead.

        Returns:
        -------
            dict: The test definition if available and valid; otherwise, an empty dictionary.
        """
        return getattr(self, "test_definition", None) or {}
