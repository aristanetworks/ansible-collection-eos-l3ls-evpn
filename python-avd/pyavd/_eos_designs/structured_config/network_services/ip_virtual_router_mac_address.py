# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class IpVirtualRouterMacAddressMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def ip_virtual_router_mac_address(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """Set the structured config for ip_virtual_router_mac_address."""
        if (
            self.shared_utils.network_services_l2
            and self.shared_utils.network_services_l3
            and self.shared_utils.node_config.virtual_router_mac_address is not None
        ):
            self.structured_config.ip_virtual_router_mac_address = str(self.shared_utils.node_config.virtual_router_mac_address).lower()
