# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigOverlay


class RouterTrafficEngineering(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def router_traffic_engineering(self: AvdStructuredConfigOverlay) -> dict | None:
        """Return structured config for router traffic-engineering."""
        if not self.shared_utils.is_cv_pathfinder_router:
            return None

        return {"enabled": True}
