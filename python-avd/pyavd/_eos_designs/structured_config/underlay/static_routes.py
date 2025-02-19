# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from itertools import chain
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlayProtocol


class StaticRoutesMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def static_routes(self: AvdStructuredConfigUnderlayProtocol) -> None:
        """
        Set the structured config for static_routes.

        Consist of
        - static_routes configured under node type l3_interfaces and l3_port_channels
        """
        for l3_generic_interface in chain(self.shared_utils.l3_interfaces, self.shared_utils.node_config.l3_port_channels):
            if not l3_generic_interface.static_routes:
                continue

            if not l3_generic_interface.peer_ip:
                # TODO: add better context to error message once source is available
                # to hint whether interface is L3 interface vs L3 Port-Channel
                msg = f"Cannot set a static_route route for interface {l3_generic_interface.name} because 'peer_ip' is missing."
                raise AristaAvdInvalidInputsError(msg)

            for l3_generic_interface_static_route in l3_generic_interface.static_routes:
                static_route = EosCliConfigGen.StaticRoutesItem(
                    destination_address_prefix=l3_generic_interface_static_route.prefix, gateway=l3_generic_interface.peer_ip
                )
                self.structured_config.static_routes.append_unique(static_route)
