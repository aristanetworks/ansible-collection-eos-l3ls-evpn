# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class Ipv6StaticRoutesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def ipv6_static_routes(self: AvdStructuredConfigNetworkServices) -> list[dict] | None:
        """
        Returns structured config for ipv6_static_routes.

        Consist of
        - ipv6 static_routes defined under the vrfs
        - static routes added automatically for VARPv6 with prefixes
        """
        if not self.shared_utils.network_services_l3:
            return None

        ipv6_static_routes = []
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                for static_route in vrf.ipv6_static_routes:
                    ipv6_static_route = static_route._as_dict()
                    ipv6_static_route["vrf"] = vrf.name
                    ipv6_static_route.pop("nodes", None)

                    # Ignore duplicate items in case of duplicate VRF definitions across multiple tenants.
                    if static_route not in ipv6_static_routes:
                        ipv6_static_routes.append(ipv6_static_route)

        if ipv6_static_routes:
            return ipv6_static_routes

        return None
