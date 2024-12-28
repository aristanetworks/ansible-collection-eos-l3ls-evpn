# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from pyavd._anta.logs import LogMessage

if TYPE_CHECKING:
    from anta.models import AntaTest

    from pyavd._anta.logs import TestLoggerAdapter
    from pyavd._anta.models import ExtendedDeviceData


class AntaTestInputFactory(ABC):
    """Base class for AntaTest.Input factories."""

    def __init__(self, device_data: ExtendedDeviceData, logger: TestLoggerAdapter) -> None:
        self.device = device_data
        self.logger = logger

        # Shortcut attributes
        self.structured_config = device_data.structured_config
        self.fabric_data = device_data.fabric_data
        self.scope = device_data.fabric_data.scope

    @abstractmethod
    def create(self) -> AntaTest.Input | None:
        """Create the AntaTest.Input model for the AntaTest."""

    def is_peer_in_boundary(self, peer: str, caller: str) -> bool:
        """Check if the peer is in the same boundary as the device."""
        if self.scope.boundary == "unlimited":
            return True

        if peer not in self.fabric_data.get_devices_by_attribute("boundary_location", self.device.boundary_location):
            self.logger.info(LogMessage.PEER_OUTSIDE_BOUNDARY, caller=caller, peer=peer, boundary=self.scope.boundary)
            return False

        return True

    def is_peer_available(self, peer: str, caller: str) -> bool:
        """Check if a peer is deployed by looking at his `is_deployed` key."""
        if peer not in self.fabric_data.devices or not self.fabric_data.devices[peer].is_deployed:
            self.logger.info(LogMessage.PEER_UNAVAILABLE, caller=caller, peer=peer)
            return False
        return True
