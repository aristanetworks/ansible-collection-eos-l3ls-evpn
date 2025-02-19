# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from re import search
from typing import TYPE_CHECKING, Literal, Protocol

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import default

if TYPE_CHECKING:
    from . import SharedUtilsProtocol


class NodeTypeMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def type(self: SharedUtilsProtocol) -> str:
        """Type fact set based on type variable."""
        if (node_type := self.inputs.type) is not None:
            return node_type
        if self.default_node_type:
            return self.default_node_type

        msg = f"'type' for host {self.hostname}"
        raise AristaAvdInvalidInputsError(msg)

    @cached_property
    def default_node_type(self: SharedUtilsProtocol) -> str | None:
        """default_node_type set based on hostname, returning first node type matching a regex in default_node_types."""
        for default_node_type in self.inputs.default_node_types:
            for hostname_regex in default_node_type.match_hostnames:
                if search(f"^{hostname_regex}$", self.hostname):
                    return default_node_type.node_type

        return None

    @cached_property
    def connected_endpoints(self: SharedUtilsProtocol) -> bool:
        """
        Should we configure connected endpoints?

        connected_endpoints set based on
        node_type_keys.<node_type_key>.connected_endpoints.
        """
        return self.node_type_key_data.connected_endpoints

    @cached_property
    def underlay_router(self: SharedUtilsProtocol) -> bool:
        """
        Is this an underlay router?

        underlay_router set based on
        node_type_keys.<node_type_key>.underlay_router.
        """
        return self.node_type_key_data.underlay_router

    @cached_property
    def uplink_type(self: SharedUtilsProtocol) -> Literal["p2p", "port-channel", "p2p-vrfs", "lan"]:
        """
        Uplink type.

        uplink_type set based on <node_type_key>.nodes.[].uplink_type and node_type_keys.<node_type_key>.uplink_type.
        """
        return default(self.node_config.uplink_type, self.node_type_key_data.uplink_type)

    @cached_property
    def network_services_l1(self: SharedUtilsProtocol) -> bool:
        """
        Should we configure L1 network services?

        network_services_l1 set based on node_type_keys.<node_type_key>.network_services.l1.
        """
        return self.node_type_key_data.network_services.l1

    @cached_property
    def network_services_l2(self: SharedUtilsProtocol) -> bool:
        """
        Should we configure L2 network services?

        network_services_l2 set based on node_type_keys.<node_type_key>.network_services.l2.
        """
        return self.node_type_key_data.network_services.l2

    @cached_property
    def network_services_l3(self: SharedUtilsProtocol) -> bool:
        """
        Should we configure L3 network services?

        network_services_l3 set based on node_type_keys.<node_type_key>.network_services.l3
        and <node_type_key>.<defaults | node_groups.<> | nodes.<> >.evpn_services_l2_only.
        """
        # network_services_l3 override based on evpn_services_l2_only
        if self.vtep and self.node_config.evpn_services_l2_only:
            return False
        return self.node_type_key_data.network_services.l3

    @cached_property
    def network_services_l2_as_subint(self: SharedUtilsProtocol) -> bool:
        """
        Should we deploy SVIs as subinterfaces?

        network_services_l2_as_subint set based on
        node_type_keys.<node_type_key>.network_services.l3 for uplink_type "lan" or "lan-port-channel".
        """
        return self.network_services_l3 and self.uplink_type in ["lan", "lan-port-channel"]

    @cached_property
    def any_network_services(self: SharedUtilsProtocol) -> bool:
        """Returns True if either L1, L2 or L3 network_services are enabled."""
        return self.network_services_l1 or self.network_services_l2 or self.network_services_l3

    @cached_property
    def mpls_lsr(self: SharedUtilsProtocol) -> bool:
        """
        Is this an MPLS LSR?

        mpls_lsr set based on
        node_type_keys.<node_type_key>.mpls_lsr.
        """
        return self.node_type_key_data.mpls_lsr

    @cached_property
    def vtep(self: SharedUtilsProtocol) -> bool:
        """
        Is this a VTEP?

        vtep set based on
        <node_type_key>.nodes.[].vtep and
        node_type_keys.<node_type_key>.vtep.
        """
        if self.is_wan_router and not self.inputs.wan_use_evpn_node_settings_for_lan:
            # For WAN routers without the knob, vtep should be ignored.
            return False
        return default(self.node_config.vtep, self.node_type_key_data.vtep)
