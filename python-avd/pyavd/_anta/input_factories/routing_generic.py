# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from pyavd._anta.utils import LogMessage

if TYPE_CHECKING:
    from anta.tests.routing.generic import VerifyRoutingTableEntry

    from pyavd._anta.utils import ConfigManager, TestLoggerAdapter


class VerifyRoutingTableEntryInputFactory:
    """Input factory class for the VerifyRoutingTableEntry test."""

    @classmethod
    def create(cls, test: type[VerifyRoutingTableEntry], manager: ConfigManager, logger: TestLoggerAdapter) -> VerifyRoutingTableEntry.Input | None:
        """Create Input for the VerifyRoutingTableEntry test."""
        # Skip the test if the device is not a VTEP
        if not manager.is_vtep():
            logger.info(LogMessage.NOT_VTEP)
            return None

        # TODO: For now, we exclude WAN VTEPs from testing
        if manager.is_wan_vtep():
            logger.info(LogMessage.WAN_VTEP)
            return None

        # Using a set to avoid duplicate tests for the same IP address (e.g. MLAG VTEPs)
        processed_ips = set()

        # Here we use the combined_mapping (Loopback0 IP + VXLAN source interface IP) to get all routes to check
        for peer, ips in manager.fabric_data.combined_mapping.items():
            if not manager.is_peer_available(peer):
                logger.info(LogMessage.UNAVAILABLE_PEER, entity=str(ips), peer=peer)
                continue

            processed_ips.update(ips)

        return test.Input(routes=list(processed_ips)) if processed_ips else None
