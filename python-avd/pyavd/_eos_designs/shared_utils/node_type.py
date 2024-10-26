# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from re import search
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import get

if TYPE_CHECKING:
    from . import SharedUtils


class NodeTypeMixin:
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def type(self: SharedUtils) -> str:
        """Type fact set based on type variable."""
        if (node_type := get(self.hostvars, "type")) is not None:
            return node_type
        if self.default_node_type:
            return self.default_node_type

        msg = f"'type' for host {self.hostname}"
        raise AristaAvdInvalidInputsError(msg)

    @cached_property
    def default_node_type(self: SharedUtils) -> str | None:
        """default_node_type set based on hostname, returning first node type matching a regex in default_node_types."""
        default_node_types = get(self.hostvars, "default_node_types", default=[])

        for default_node_type in default_node_types:
            for hostname_regex in default_node_type["match_hostnames"]:
                if search(f"^{hostname_regex}$", self.hostname):
                    return default_node_type["node_type"]

        return None

    @cached_property
    def cvp_tag_topology_hint_type(self: SharedUtils) -> str:
        """topology_tag_type set based on node_type_keys.<node_type_key>.cvp_tags.topology_hint_type."""
        return get(self.node_type_key_data, "cvp_tags.topology_hint_type", default="endpoint")

    @cached_property
    def connected_endpoints(self: SharedUtils) -> bool:
        """
        Should we configure connected endpoints?

        connected_endpoints set based on
        node_type_keys.<node_type_key>.connected_endpoints.
        """
        return get(self.node_type_key_data, "connected_endpoints", default=False)

    @cached_property
    def underlay_router(self: SharedUtils) -> bool:
        """
        Is this an underlay router?

        underlay_router set based on
        node_type_keys.<node_type_key>.underlay_router.
        """
        return get(self.node_type_key_data, "underlay_router", default=True)

    @cached_property
    def uplink_type(self: SharedUtils) -> str:
        """
        Uplink type.

        uplink_type set based on <node_type_key>.nodes.[].uplink_type and node_type_keys.<node_type_key>.uplink_type.
        """
        default_uplink_type = get(self.node_type_key_data, "uplink_type", default="p2p")
        return get(self.switch_data_combined, "uplink_type", default=default_uplink_type)

    @cached_property
    def network_services_l1(self: SharedUtils) -> bool:
        """
        Should we configure L1 network services?

        network_services_l1 set based on node_type_keys.<node_type_key>.network_services.l1.
        """
        return get(self.node_type_key_data, "network_services.l1", default=False)

    @cached_property
    def network_services_l2(self: SharedUtils) -> bool:
        """
        Should we configure L2 network services?

        network_services_l2 set based on node_type_keys.<node_type_key>.network_services.l2.
        """
        return get(self.node_type_key_data, "network_services.l2", default=False)

    @cached_property
    def network_services_l3(self: SharedUtils) -> bool:
        """
        Should we configure L3 network services?

        network_services_l3 set based on node_type_keys.<node_type_key>.network_services.l3
        and <node_type_key>.<defaults | node_groups.<> | nodes.<> >.evpn_services_l2_only.
        """
        # network_services_l3 override based on evpn_services_l2_only
        if self.vtep is True and get(self.switch_data_combined, "evpn_services_l2_only") is True:
            return False
        return get(self.node_type_key_data, "network_services.l3", default=False)

    @cached_property
    def network_services_l2_as_subint(self: SharedUtils) -> bool:
        """
        Should we deploy SVIs as subinterfaces?

        network_services_l2_as_subint set based on
        node_type_keys.<node_type_key>.network_services.l3 for uplink_type "lan" or "lan-port-channel".
        """
        return self.network_services_l3 and self.uplink_type in ["lan", "lan-port-channel"]

    @cached_property
    def any_network_services(self: SharedUtils) -> bool:
        """Returns True if either L1, L2 or L3 network_services are enabled."""
        return self.network_services_l1 is True or self.network_services_l2 is True or self.network_services_l3 is True

    @cached_property
    def mpls_lsr(self: SharedUtils) -> bool:
        """
        Is this an MPLS LSR?

        mpls_lsr set based on
        node_type_keys.<node_type_key>.mpls_lsr.
        """
        return get(self.node_type_key_data, "mpls_lsr", default=False)

    @cached_property
    def vtep(self: SharedUtils) -> bool:
        """
        Is this a VTEP?

        vtep set based on
        <node_type_key>.nodes.[].vtep and
        node_type_keys.<node_type_key>.vtep.
        """
        default_vtep = get(self.node_type_key_data, "vtep")
        return get(self.switch_data_combined, "vtep", default=default_vtep) is True
