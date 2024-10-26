# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections import defaultdict
from functools import cached_property
from typing import TYPE_CHECKING, Literal

from pyavd._utils import get

if TYPE_CHECKING:
    from . import SharedUtils


class FlowTrackingMixin:
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def flow_tracking_type(self: SharedUtils) -> str:
        default_flow_tracker_type = get(self.node_type_key_data, "default_flow_tracker_type", "sampled")
        return get(self.switch_data_combined, "flow_tracker_type", default=default_flow_tracker_type)

    @cached_property
    def default_flow_tracker_name(self: SharedUtils) -> str:
        return "FLOW-TRACKER"

    @cached_property
    def fabric_flow_tracking(self: SharedUtils) -> defaultdict:
        """Return fabric level flow tracking settings for all data models."""
        configured_values = get(self.hostvars, "fabric_flow_tracking", default={})

        # By default, flow tracker is `hardware` type named `FLOW-TRACKER`
        output_settings = defaultdict(
            lambda: {
                "enabled": None,
                "name": self.default_flow_tracker_name,
            },
        )

        # By default, flow tracking is enabled only on DPS interfaces
        output_settings["dps_interfaces"]["enabled"] = True

        for data_model, settings in configured_values.items():
            tracker_enabled = settings.get("enabled")
            tracker_name = settings.get("name")

            if tracker_enabled is not None:
                output_settings[data_model]["enabled"] = tracker_enabled

            if tracker_name:
                output_settings[data_model]["name"] = tracker_name
        return output_settings

    def get_flow_tracker(
        self: SharedUtils,
        link_settings: dict | None,
        data_model: Literal[
            "uplinks",
            "downlinks",
            "endpoints",
            "l3_edge",
            "core_interfaces",
            "mlag_interfaces",
            "l3_interfaces",
            "dps_interfaces",
            "direct_wan_ha_links",
        ],
    ) -> dict:
        """Return flow_tracking settings for a link, falling back to the fabric flow_tracking_settings if not defined."""
        link_tracker_enabled, link_tracker_name = None, None
        if link_settings is not None:
            link_tracker_enabled = get(link_settings, "flow_tracking.enabled")
            link_tracker_name = get(link_settings, "flow_tracking.name")

        fabric_flow = self.fabric_flow_tracking[data_model]

        tracking_enabled = link_tracker_enabled if link_tracker_enabled is not None else fabric_flow["enabled"]
        if not tracking_enabled:
            return None

        tracker_name = link_tracker_name or fabric_flow["name"]

        return {self.flow_tracking_type: tracker_name}
