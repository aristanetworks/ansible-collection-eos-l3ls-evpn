# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import get

if TYPE_CHECKING:
    from . import SharedUtils


class DescriptionsMixin:
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def default_network_ports_description(self: SharedUtils) -> str:
        default_value = self.schema.get_default_value(["default_network_ports_description"])
        return get(self.hostvars, "default_network_ports_description", default=default_value)

    @cached_property
    def default_network_ports_port_channel_description(self: SharedUtils) -> str:
        default_value = self.schema.get_default_value(["default_network_ports_port_channel_description"])
        return get(self.hostvars, "default_network_ports_port_channel_description", default=default_value)

    @cached_property
    def default_connected_endpoints_description(self: SharedUtils) -> str:
        default_value = self.schema.get_default_value(["default_connected_endpoints_description"])
        return get(self.hostvars, "default_connected_endpoints_description", default=default_value)

    @cached_property
    def default_connected_endpoints_port_channel_description(self: SharedUtils) -> str:
        default_value = self.schema.get_default_value(["default_connected_endpoints_port_channel_description"])
        return get(self.hostvars, "default_connected_endpoints_port_channel_description", default=default_value)

    @cached_property
    def mlag_member_description(self: SharedUtils) -> str:
        default_value = self.schema.get_default_value(["mlag_member_description"])
        return get(self.hostvars, "mlag_member_description", default=default_value)

    @cached_property
    def mlag_port_channel_description(self: SharedUtils) -> str:
        default_value = self.schema.get_default_value(["mlag_port_channel_description"])
        return get(self.hostvars, "mlag_port_channel_description", default=default_value)

    @cached_property
    def mlag_peer_svi_description(self: SharedUtils) -> str:
        default_value = self.schema.get_default_value(["mlag_peer_svi_description"])
        return get(self.hostvars, "mlag_peer_svi_description", default=default_value)

    @cached_property
    def mlag_peer_l3_svi_description(self: SharedUtils) -> str:
        default_value = self.schema.get_default_value(["mlag_peer_l3_svi_description"])
        return get(self.hostvars, "mlag_peer_l3_svi_description", default=default_value)

    @cached_property
    def mlag_peer_vlan_name(self: SharedUtils) -> str:
        default_value = self.schema.get_default_value(["mlag_peer_vlan_name"])
        return get(self.hostvars, "mlag_peer_vlan_name", default=default_value)

    @cached_property
    def mlag_peer_l3_vlan_name(self: SharedUtils) -> str:
        default_value = self.schema.get_default_value(["mlag_peer_l3_vlan_name"])
        return get(self.hostvars, "mlag_peer_l3_vlan_name", default=default_value)

    @cached_property
    def mlag_peer_l3_vrf_svi_description(self: SharedUtils) -> str:
        default_value = self.schema.get_default_value(["mlag_peer_l3_vrf_svi_description"])
        return get(self.hostvars, "mlag_peer_l3_vrf_svi_description", default=default_value)

    @cached_property
    def mlag_peer_l3_vrf_vlan_name(self: SharedUtils) -> str:
        default_value = self.schema.get_default_value(["mlag_peer_l3_vrf_vlan_name"])
        return get(self.hostvars, "mlag_peer_l3_vrf_vlan_name", default=default_value)

    @cached_property
    def mlag_bgp_peer_group_description(self: SharedUtils) -> str:
        default_value = self.schema.get_default_value(["mlag_bgp_peer_group_description"])
        return get(self.hostvars, "mlag_bgp_peer_group_description", default=default_value)

    @cached_property
    def mlag_bgp_peer_description(self: SharedUtils) -> str:
        default_value = self.schema.get_default_value(["mlag_bgp_peer_description"])
        return get(self.hostvars, "mlag_bgp_peer_description", default=default_value)

    @cached_property
    def overlay_bgp_peer_description(self: SharedUtils) -> str:
        default_value = self.schema.get_default_value(["overlay_bgp_peer_description"])
        return get(self.hostvars, "overlay_bgp_peer_description", default=default_value)

    @cached_property
    def default_underlay_p2p_ethernet_description(self: SharedUtils) -> str:
        default_value = self.schema.get_default_value(["default_underlay_p2p_ethernet_description"])
        return get(self.hostvars, "default_underlay_p2p_ethernet_description", default=default_value)

    @cached_property
    def default_underlay_p2p_port_channel_description(self: SharedUtils) -> str:
        default_value = self.schema.get_default_value(["default_underlay_p2p_port_channel_description"])
        return get(self.hostvars, "default_underlay_p2p_port_channel_description", default=default_value)

    @cached_property
    def underlay_l2_ethernet_description(self: SharedUtils) -> str:
        default_value = self.schema.get_default_value(["underlay_l2_ethernet_description"])
        return get(self.hostvars, "underlay_l2_ethernet_description", default=default_value)

    @cached_property
    def underlay_l2_port_channel_description(self: SharedUtils) -> str:
        default_value = self.schema.get_default_value(["underlay_l2_port_channel_description"])
        return get(self.hostvars, "underlay_l2_port_channel_description", default=default_value)

    @cached_property
    def default_vrf_diag_loopback_description(self: SharedUtils) -> str:
        default_value = self.schema.get_default_value(["default_vrf_diag_loopback_description"])
        return get(self.hostvars, "default_vrf_diag_loopback_description", default=default_value)
