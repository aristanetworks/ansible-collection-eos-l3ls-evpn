# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from itertools import chain
from typing import TYPE_CHECKING, Protocol

from pyavd._errors import AristaAvdInvalidInputsError

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlayProtocol


class StaticRoutesMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def static_routes(self: AvdStructuredConfigUnderlayProtocol) -> list[dict] | None:
        """
        Returns structured config for static_routes.

        Consist of
        - static_routes configured under node type l3_interfaces and l3_port_channels
        """
        static_routes = []
        for l3_generic_interface in chain(self.shared_utils.l3_interfaces, self.shared_utils.node_config.l3_port_channels):
            if not l3_generic_interface.static_routes:
                continue

            if not l3_generic_interface.peer_ip:
                # TODO: add better context to error message once source is available
                # to hint whether interface is L3 interface vs L3 Port-Channel
                msg = f"Cannot set a static_route route for interface {l3_generic_interface.name} because 'peer_ip' is missing."
                raise AristaAvdInvalidInputsError(msg)

            static_routes.extend(
                {"destination_address_prefix": l3_generic_interface_static_route.prefix, "gateway": l3_generic_interface.peer_ip}
                for l3_generic_interface_static_route in l3_generic_interface.static_routes
            )

        if static_routes:
            return static_routes

        return None
