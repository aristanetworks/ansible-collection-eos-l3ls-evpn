# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import strip_empties_from_dict

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigBase


class RouterGeneralMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def router_general(self: AvdStructuredConfigBase) -> dict | None:
        if self.inputs.use_router_general_for_router_id:
            return strip_empties_from_dict(
                {
                    "router_id": {
                        "ipv4": self.shared_utils.router_id,
                        "ipv6": self.shared_utils.ipv6_router_id,
                    }
                }
            )

        return None
