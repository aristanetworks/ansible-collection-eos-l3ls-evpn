# Copyright (c) 2023-2025 Arista Networks, Inc.
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
      - Peers exist, are deployed and are not WAN routers
      - Peers within boundary scope if configured

    Notes:
      - Validates routes for all peer (excluding WAN routers) Loopback0 and VTEP IPs
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

        # TODO: In eos_validate_state, WAN routers Loopback0 IPs are included in the mapping
        # so their IPs are checked here. Not the case for their DPS IPs. This could be a bug
        # in eos_validate_state, depending if we should/would like to check WAN routers
        # Loopback0 IPs from a VTEP or not. In this new plugin, we need to decide if we want
        # to include WAN routers Loopback0 IPs or not. Right now, we are not. Since we now have
        # the scope boundary, we could include them when it is set to "unlimited" and setting
        # the scope to "fabric" would exclude them.
        for peer, ips in self.fabric_data.get_ip_index("special_ips", is_wan_router=False).items():
            caller = ", ".join([str(ip) for ip in ips])
            if not self.is_peer_available(peer, caller=caller) or not self.is_peer_in_boundary(peer, caller=caller):
                continue

            routes.update(ips)

        return VerifyRoutingTableEntry.Input(routes=sorted(routes), collect="all") if routes else None
