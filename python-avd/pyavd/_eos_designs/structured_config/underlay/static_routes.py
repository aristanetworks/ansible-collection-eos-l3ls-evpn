# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdInvalidInputsError

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlay


class StaticRoutesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def static_routes(self: AvdStructuredConfigUnderlay) -> list[dict] | None:
        """
        Returns structured config for static_routes.

        Consist of
        - static_routes configured under node type l3 interfaces
        """
        static_routes = []

        for l3_interface in self.shared_utils.l3_interfaces:
            if not l3_interface.static_routes:
                continue

            if not l3_interface.peer_ip:
                msg = f"Cannot set a static_route route for interface {l3_interface.name} because 'peer_ip' is missing."
                raise AristaAvdInvalidInputsError(msg)

            static_routes.extend(
                {"destination_address_prefix": l3_interface_static_route.prefix, "gateway": l3_interface.peer_ip}
                for l3_interface_static_route in l3_interface.static_routes
            )

        if static_routes:
            return static_routes

        return None
