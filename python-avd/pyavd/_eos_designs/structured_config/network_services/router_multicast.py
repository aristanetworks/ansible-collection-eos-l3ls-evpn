# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class RouterMulticastMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def router_multicast(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Set the structured config for router_multicast.

        Used to enable multicast routing on the VRF.
        """
        if not self.shared_utils.network_services_l3:
            return

        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                if getattr(vrf._internal_data, "evpn_l3_multicast_enabled", False):
                    self.structured_config.router_multicast.vrfs.append_new(name=vrf.name, ipv4=EosCliConfigGen.RouterMulticast.VrfsItem.Ipv4(routing=True))
