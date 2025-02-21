# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from pyavd._anta.logs import LogMessage

if TYPE_CHECKING:
    from anta.models import AntaTest

    from pyavd._anta.logs import TestLoggerAdapter
    from pyavd._anta.models import DeviceTestContext


class AntaTestInputFactory(ABC):
    """Base class for AntaTest.Input factories."""

    def __init__(self, device_context: DeviceTestContext, logger: TestLoggerAdapter) -> None:
        self.device = device_context
        self.structured_config = device_context.structured_config
        self.structured_configs = device_context.structured_configs
        self.logger = logger

    @abstractmethod
    def create(self) -> AntaTest.Input | None:
        """Create the AntaTest.Input model for the AntaTest."""

    def is_peer_available(self, peer: str, caller: str) -> bool:
        """Check if a peer is part of the fabric and is deployed."""
        if peer not in self.structured_configs or not self.structured_configs[peer].is_deployed:
            self.logger.debug(LogMessage.PEER_UNAVAILABLE, caller=caller, peer=peer)
            return False
        return True

    def get_interface_ip(self, peer: str, peer_interface: str, caller: str) -> str | None:
        """Get the IP address of a peer interface."""
        if not self.is_peer_available(peer, caller=caller):
            return None
        for intf in self.structured_configs[peer].ethernet_interfaces:
            if intf.name == peer_interface:
                return intf.ip_address
        self.logger.debug(LogMessage.PEER_INTERFACE_NO_IP, caller=caller, peer=peer, peer_interface=peer_interface)
        return None
