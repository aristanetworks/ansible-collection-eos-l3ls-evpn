# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from anta.tests.routing.generic import VerifyRoutingTableEntry

from pyavd._anta.logs import LogMessage

from ._base_classes import AntaTestInputFactory


class VerifyRoutingTableEntryInputFactory(AntaTestInputFactory):
    """Input factory class for the VerifyRoutingTableEntry test.

    Requirements:
      - Device is VTEP (not WAN router)
      - Peers exist and are deployed
      - Peers within boundary scope if configured

    Notes:
      - Validates routes for all peer Loopback0 and VTEP IPs
      - Deduplicates routes (e.g., MLAG VTEP IPs)
    """

    def create(self) -> VerifyRoutingTableEntry.Input | None:
        """Create Input for the VerifyRoutingTableEntry test."""
        # Skip the test if the device is not a VTEP or is a WAN VTEP
        if not self.device.is_vtep or self.device.is_wan_router:
            self.logger.debug(LogMessage.DEVICE_NOT_VTEP)
            return None

        # Using a set to avoid duplicate tests for the same IP address (e.g. MLAG VTEPs)
        routes = set()

        # Here we use the special IPs mapping (Loopback0 IP + VXLAN source interface IP) to get all routes to check
        for peer, ips in self.fabric_data.get_ip_index("special_ips").items():
            caller = ", ".join([str(ip) for ip in ips])
            if not self.is_peer_available(peer, caller=caller) or not self.is_peer_in_boundary(peer, caller=caller):
                continue

            routes.update(ips)

        return VerifyRoutingTableEntry.Input(routes=sorted(routes), collect="all") if routes else None
