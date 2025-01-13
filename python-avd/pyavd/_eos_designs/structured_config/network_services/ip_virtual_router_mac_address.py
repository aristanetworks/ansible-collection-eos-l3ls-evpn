# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class IpVirtualRouterMacAddressMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def ip_virtual_router_mac_address(self: AvdStructuredConfigNetworkServices) -> str | None:
        """Return structured config for ip_virtual_router_mac_address."""
        if (
            self.shared_utils.network_services_l2
            and self.shared_utils.network_services_l3
            and self.shared_utils.node_config.virtual_router_mac_address is not None
        ):
            return str(self.shared_utils.node_config.virtual_router_mac_address).lower()

        return None
