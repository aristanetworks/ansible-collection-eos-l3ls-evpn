# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigOverlayProtocol


class RouterTrafficEngineering(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def router_traffic_engineering(self: AvdStructuredConfigOverlayProtocol) -> None:
        """Set the structured config for router traffic-engineering."""
        if not self.shared_utils.is_cv_pathfinder_router:
            return

        self.structured_config.router_traffic_engineering.enabled = True
