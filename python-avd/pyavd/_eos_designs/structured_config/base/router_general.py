# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigBaseProtocol


class RouterGeneralMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def router_general(self: AvdStructuredConfigBaseProtocol) -> None:
        if self.inputs.use_router_general_for_router_id:
            self.structured_config.router_general.router_id.ipv4 = self.shared_utils.router_id
            self.structured_config.router_general.router_id.ipv6 = self.shared_utils.ipv6_router_id
