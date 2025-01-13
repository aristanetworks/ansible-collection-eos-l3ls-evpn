# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigUnderlay


class AgentsMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def agents(self: AvdStructuredConfigUnderlay) -> list | None:
        """Return structured config for agents."""
        if not self.shared_utils.is_wan_router:
            return None

        return [
            {"name": "KernelFib", "environment_variables": [{"name": "KERNELFIB_PROGRAM_ALL_ECMP", "value": "1"}]},
        ]
