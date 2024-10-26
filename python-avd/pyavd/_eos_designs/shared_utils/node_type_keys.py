# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import get, get_item, replace_or_append_item

if TYPE_CHECKING:
    from . import SharedUtils

MPLS_DEFAULT_NODE_TYPE_KEYS = [
    {
        "key": "p",
        "type": "p",
        "mpls_lsr": True,
        "default_mpls_overlay_role": "none",
        "default_overlay_routing_protocol": "ibgp",
        "default_underlay_routing_protocol": "isis-sr",
    },
    {
        "key": "pe",
        "type": "pe",
        "mpls_lsr": True,
        "connected_endpoints": True,
        "default_mpls_overlay_role": "client",
        "default_evpn_role": "client",
        "network_services": {
            "l1": True,
            "l2": True,
            "l3": True,
        },
        "default_overlay_routing_protocol": "ibgp",
        "default_underlay_routing_protocol": "isis-sr",
        "default_overlay_address_families": ["vpn-ipv4"],
        "default_evpn_encapsulation": "mpls",
    },
    {
        "key": "rr",
        "type": "rr",
        "mpls_lsr": True,
        "default_mpls_overlay_role": "server",
        "default_evpn_role": "server",
        "default_overlay_routing_protocol": "ibgp",
        "default_underlay_routing_protocol": "isis-sr",
        "default_overlay_address_families": ["vpn-ipv4"],
        "default_evpn_encapsulation": "mpls",
    },
]
L2LS_DEFAULT_NODE_TYPE_KEYS = [
    {
        "key": "l3spine",
        "type": "l3spine",
        "connected_endpoints": True,
        "mlag_support": True,
        "network_services": {
            "l2": True,
            "l3": True,
        },
        "default_overlay_routing_protocol": "none",
        "default_underlay_routing_protocol": "none",
    },
    {
        "key": "spine",
        "type": "spine",
        "connected_endpoints": True,
        "mlag_support": True,
        "network_services": {
            "l2": True,
        },
        "underlay_router": False,
        "uplink_type": "port-channel",
    },
    {
        "key": "leaf",
        "type": "leaf",
        "connected_endpoints": True,
        "mlag_support": True,
        "network_services": {
            "l2": True,
        },
        "underlay_router": False,
        "uplink_type": "port-channel",
    },
]

# NOTE: There is a static list of default node_type_keys in the fabric documentation templates which must be updated as well

DEFAULT_NODE_TYPE_KEYS = {
    "l3ls-evpn": [
        {
            "key": "spine",
            "type": "spine",
            "default_evpn_role": "server",
            "default_ptp_priority1": 20,
            "cv_tags_topology_type": "spine",
        },
        {
            "key": "l3leaf",
            "type": "l3leaf",
            "connected_endpoints": True,
            "default_evpn_role": "client",
            "mlag_support": True,
            "network_services": {
                "l2": True,
                "l3": True,
            },
            "vtep": True,
            "default_ptp_priority1": 30,
            "cv_tags_topology_type": "leaf",
        },
        {
            "key": "l2leaf",
            "type": "l2leaf",
            "connected_endpoints": True,
            "mlag_support": True,
            "network_services": {
                "l2": True,
            },
            "underlay_router": False,
            "uplink_type": "port-channel",
            "cv_tags_topology_type": "leaf",
        },
        # Avoiding duplicate code
        get_item(L2LS_DEFAULT_NODE_TYPE_KEYS, "key", "l3spine", required=True),
        {
            "key": "l2spine",
            "type": "l2spine",
            "connected_endpoints": True,
            "mlag_support": True,
            "network_services": {
                "l2": True,
            },
            "underlay_router": False,
            "uplink_type": "port-channel",
        },
        {
            "key": "super_spine",
            "type": "super-spine",
            "cv_tags_topology_type": "core",
        },
        {
            "key": "overlay_controller",
            "type": "overlay-controller",
            "default_evpn_role": "server",
            "cv_tags_topology_type": "spine",
        },
        {
            "key": "wan_router",
            "type": "wan_router",
            "default_evpn_role": "client",
            "default_wan_role": "client",
            "default_underlay_routing_protocol": "none",
            "default_overlay_routing_protocol": "ibgp",
            "default_flow_tracker_type": "hardware",
            "vtep": True,
            "network_services": {
                "l3": True,
            },
        },
        {
            "key": "wan_rr",
            "type": "wan_rr",
            "default_evpn_role": "server",
            "default_wan_role": "server",
            "default_underlay_routing_protocol": "none",
            "default_overlay_routing_protocol": "ibgp",
            "default_flow_tracker_type": "hardware",
            "vtep": True,
            "network_services": {
                "l3": True,
            },
        },
        # Avoiding duplicate code
        *MPLS_DEFAULT_NODE_TYPE_KEYS,
    ],
    "mpls": MPLS_DEFAULT_NODE_TYPE_KEYS,
    "l2ls": L2LS_DEFAULT_NODE_TYPE_KEYS,
}


class NodeTypeKeysMixin:
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def node_type_keys(self: SharedUtils) -> list:
        """NOTE: This method is called _before_ any schema validation, since we need to resolve node_type_keys dynamically."""
        design_type = get(self.hostvars, "design.type", default="l3ls-evpn")
        default_node_type_keys_for_our_design = get(DEFAULT_NODE_TYPE_KEYS, design_type)

        # Using list() to force a copy of node_type_keys so we don't modify the default when we apply custom_node_type_keys
        node_type_keys = list(get(self.hostvars, "node_type_keys", default=default_node_type_keys_for_our_design))
        custom_node_type_keys = get(self.hostvars, "custom_node_type_keys", default=[])

        for node_type_key in custom_node_type_keys:
            replace_or_append_item(node_type_keys, "key", node_type_key)

        return node_type_keys

    @cached_property
    def node_type_key_data(self: SharedUtils) -> dict:
        """node_type_key_data containing settings for this node_type."""
        for node_type_key in self.node_type_keys:
            if node_type_key["type"] == self.type:
                return node_type_key

        # Not found
        msg = f"node_type_keys.[type=={self.type}]"
        raise AristaAvdInvalidInputsError(msg)
