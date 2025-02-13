# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from . import EosDesignsFactsProtocol


class OverlayMixin(Protocol):
    """
    Mixin Class used to generate some of the EosDesignsFacts.

    Class should only be used as Mixin to the EosDesignsFacts class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def evpn_role(self: EosDesignsFactsProtocol) -> str | None:
        """Exposed in avd_switch_facts."""
        return self.shared_utils.evpn_role

    @cached_property
    def mpls_overlay_role(self: EosDesignsFactsProtocol) -> str | None:
        """Exposed in avd_switch_facts."""
        return self.shared_utils.mpls_overlay_role

    @cached_property
    def evpn_route_servers(self: EosDesignsFactsProtocol) -> list:
        """
        Exposed in avd_switch_facts.

        For evpn clients the default value for EVPN Route Servers is the content of the uplink_switches variable set elsewhere.
        For all other evpn roles there is no default.
        """
        if self.shared_utils.underlay_router is True:
            if self.evpn_role == "client":
                return self.shared_utils.node_config.evpn_route_servers._as_list() or self.shared_utils.uplink_switches
            return self.shared_utils.node_config.evpn_route_servers._as_list()
        return []

    @cached_property
    def mpls_route_reflectors(self: EosDesignsFactsProtocol) -> list | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.underlay_router is True and (
            self.mpls_overlay_role in ["client", "server"] or (self.evpn_role in ["client", "server"] and self.overlay["evpn_mpls"])
        ):
            return self.shared_utils.node_config.mpls_route_reflectors._as_list()
        return None

    @cached_property
    def overlay(self: EosDesignsFactsProtocol) -> dict | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.underlay_router is True:
            return {
                "peering_address": self.shared_utils.overlay_peering_address,
                "evpn_mpls": self.shared_utils.overlay_evpn_mpls,
            }
        return None

    @cached_property
    def vtep_ip(self: EosDesignsFactsProtocol) -> str | None:
        """Exposed in avd_switch_facts."""
        if self.shared_utils.vtep:
            return self.shared_utils.vtep_ip
        return None
