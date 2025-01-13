# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Literal

from pyavd._eos_designs.schema import EosDesigns
from pyavd._utils import default

if TYPE_CHECKING:
    from . import SharedUtils

    FlowTracking = (
        EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem.FlowTracking
        | EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.L3InterfacesItem.FlowTracking
        | EosDesigns.CoreInterfaces.P2pLinksItem.FlowTracking
        | EosDesigns.L3Edge.P2pLinksItem.FlowTracking
        | EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.WanHa.FlowTracking
        | EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3InterfacesItem.FlowTracking
        | EosDesigns.FabricFlowTracking.MlagInterfaces
        | EosDesigns.FabricFlowTracking.DpsInterfaces
        | EosDesigns.FabricFlowTracking.Uplinks
        | EosDesigns.FabricFlowTracking.Downlinks
    )


class FlowTrackingMixin:
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def flow_tracking_type(self: SharedUtils) -> Literal["sampled", "hardware"]:
        default_flow_tracker_type = self.node_type_key_data.default_flow_tracker_type
        return self.node_config.flow_tracker_type or default_flow_tracker_type

    def get_flow_tracker(self: SharedUtils, flow_tracking: FlowTracking) -> dict[str, str] | None:
        """Return flow_tracking settings for a link, falling back to the fabric flow_tracking_settings if not defined."""
        match flow_tracking:
            case EosDesigns._DynamicKeys.DynamicConnectedEndpointsItem.ConnectedEndpointsItem.AdaptersItem.FlowTracking():
                enabled: bool = default(flow_tracking.enabled, self.inputs.fabric_flow_tracking.endpoints.enabled)
                name: str = default(flow_tracking.name, self.inputs.fabric_flow_tracking.endpoints.name)
            case EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.L3InterfacesItem.FlowTracking():
                enabled: bool = default(flow_tracking.enabled, self.inputs.fabric_flow_tracking.l3_interfaces.enabled)
                name: str = default(flow_tracking.name, self.inputs.fabric_flow_tracking.l3_interfaces.name)
            case EosDesigns.CoreInterfaces.P2pLinksItem.FlowTracking():
                enabled: bool = default(flow_tracking.enabled, self.inputs.fabric_flow_tracking.core_interfaces.enabled)
                name: str = default(flow_tracking.name, self.inputs.fabric_flow_tracking.core_interfaces.name)
            case EosDesigns.L3Edge.P2pLinksItem.FlowTracking():
                enabled: bool = default(flow_tracking.enabled, self.inputs.fabric_flow_tracking.l3_edge.enabled)
                name: str = default(flow_tracking.name, self.inputs.fabric_flow_tracking.l3_edge.name)
            case EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.WanHa.FlowTracking():
                enabled: bool = default(flow_tracking.enabled, self.inputs.fabric_flow_tracking.direct_wan_ha_links.enabled)
                name: str = default(flow_tracking.name, self.inputs.fabric_flow_tracking.direct_wan_ha_links.name)
            case EosDesigns._DynamicKeys.DynamicNodeTypesItem.NodeTypes.NodesItem.L3InterfacesItem.FlowTracking():
                enabled: bool = default(flow_tracking.enabled, self.inputs.fabric_flow_tracking.l3_interfaces.enabled)
                name: str = default(flow_tracking.name, self.inputs.fabric_flow_tracking.l3_interfaces.name)
            case (
                EosDesigns.FabricFlowTracking.MlagInterfaces()
                | EosDesigns.FabricFlowTracking.DpsInterfaces()
                | EosDesigns.FabricFlowTracking.Uplinks()
                | EosDesigns.FabricFlowTracking.Downlinks()
            ):
                enabled: bool = flow_tracking.enabled
                name: str = flow_tracking.name

        if not enabled:
            return None

        return {self.flow_tracking_type: name}
