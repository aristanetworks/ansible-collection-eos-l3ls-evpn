# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import EosDesignsFacts


class WanMixin:
    """
    Mixin Class providing a subset of EosDesignsFacts.

    Class should only be used as Mixin to the EosDesignsFacts class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def wan_path_groups(self: EosDesignsFacts) -> list | None:
        """
        Return the list of WAN path_groups directly connected to this router.

        Each with a list of dictionaries containing the (interface, ip_address) in the path_group.

        TODO: Also add the path_groups importing any of our connected path groups.
              Need to find out if we need to resolve recursive imports.
        """
        if not self.shared_utils.is_wan_router:
            return None

        return self.shared_utils.wan_local_path_groups
