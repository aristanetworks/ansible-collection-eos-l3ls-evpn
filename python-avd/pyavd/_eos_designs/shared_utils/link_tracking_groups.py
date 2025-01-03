# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import default, strip_empties_from_list

if TYPE_CHECKING:
    from . import SharedUtils


class LinkTrackingGroupsMixin:
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def link_tracking_groups(self: SharedUtils) -> list | None:
        if self.node_config.link_tracking.enabled:
            link_tracking_groups = []
            default_recovery_delay = default(self.platform_settings.reload_delay.mlag, 300)
            if len(self.node_config.link_tracking.groups) > 0:
                for lt_group in self.node_config.link_tracking.groups:
                    lt_group_dict = lt_group._as_dict(include_default_values=True)
                    lt_group_dict["recovery_delay"] = default(lt_group.recovery_delay, default_recovery_delay)
                    link_tracking_groups.append(lt_group_dict)
            else:
                link_tracking_groups.append({"name": "LT_GROUP1", "recovery_delay": default_recovery_delay})

            return strip_empties_from_list(link_tracking_groups)

        return None
