# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlay


class StaticRoutesMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def static_routes(self: AvdStructuredConfigUnderlay) -> None:
        """
        Returns structured config for static_routes.

        Consist of
        - static_routes configured under node type l3 interfaces
        """
        for l3_interface in self.shared_utils.l3_interfaces:
            if not l3_interface.static_routes:
                continue

            if not l3_interface.peer_ip:
                msg = f"Cannot set a static_route route for interface {l3_interface.name} because 'peer_ip' is missing."
                raise AristaAvdInvalidInputsError(msg)
            for l3_interface_static_route in l3_interface.static_routes:
                static_route = EosCliConfigGen.StaticRoutesItem(destination_address_prefix=l3_interface_static_route.prefix, gateway=l3_interface.peer_ip)
                self.structured_config.static_routes.append(static_route)
