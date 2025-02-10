# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class DpsInterfacesMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def dps_interfaces(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Returns structured config for dps_interfaces.

        Only used for WAN devices
        """
        if not self.shared_utils.is_wan_router:
            return

        dps1 = EosCliConfigGen.DpsInterfacesItem(name="Dps1", description="DPS Interface", mtu=9194)

        if self.shared_utils.vtep_loopback.lower().startswith("dps"):
            dps1.ip_address = f"{self.shared_utils.vtep_ip}/32"

        # TODO: do IPv6 when needed - for now no easy way in AVD to detect if this is needed
        # When needed - need a default value if different than IPv4

        dps1.flow_tracker = self.shared_utils.new_get_flow_tracker(
            self.inputs.fabric_flow_tracking.dps_interfaces, output_type=EosCliConfigGen.DpsInterfacesItem.FlowTracker
        )

        self.structured_config.dps_interfaces.append(dps1)
