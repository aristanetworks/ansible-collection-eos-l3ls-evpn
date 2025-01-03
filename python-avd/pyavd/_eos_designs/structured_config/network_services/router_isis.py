# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class RouterIsisMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def router_isis(self: AvdStructuredConfigNetworkServices) -> dict | None:
        """
        return structured config for router_isis.

        Used for non-EVPN where underlay_routing_protocol is ISIS,
        static routes in VRF "default" should be redistributed into ISIS
        unless specifically disabled under the vrf.
        """
        if (
            self.shared_utils.network_services_l3
            and self._vrf_default_ipv4_static_routes["redistribute_in_underlay"]
            and self.shared_utils.underlay_routing_protocol in ["isis", "isis-ldp", "isis-sr", "isis-sr-ldp"]
        ):
            return {"redistribute_routes": [{"source_protocol": "static"}]}

        return None
