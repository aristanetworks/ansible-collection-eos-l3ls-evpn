# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from .utils import UtilsMixin


class UnderlayMixin(UtilsMixin):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def underlay_bgp(self) -> bool:
        return (
            self.shared_utils.bgp
            and self.shared_utils.underlay_routing_protocol == "ebgp"
            and self.shared_utils.underlay_router
            and self.shared_utils.uplink_type in ["p2p", "p2p-vrfs"]
        )

    @cached_property
    def underlay_mpls(self) -> bool:
        return (
            self.shared_utils.underlay_routing_protocol in ["isis-sr", "isis-ldp", "isis-sr-ldp", "ospf-ldp"]
            and self.shared_utils.mpls_lsr
            and self.shared_utils.underlay_router
            and self.shared_utils.uplink_type in ["p2p", "p2p-vrfs"]
        )

    @cached_property
    def underlay_ldp(self) -> bool:
        return self.shared_utils.underlay_routing_protocol in ["isis-ldp", "isis-sr-ldp", "ospf-ldp"] and self.underlay_mpls

    @cached_property
    def underlay_sr(self) -> bool:
        return self.shared_utils.underlay_routing_protocol in ["isis-sr", "isis-sr-ldp"] and self.underlay_mpls

    @cached_property
    def underlay_ospf(self) -> bool:
        return (
            self.shared_utils.underlay_routing_protocol in ["ospf", "ospf-ldp"]
            and self.shared_utils.underlay_router
            and self.shared_utils.uplink_type in ["p2p", "p2p-vrfs"]
        )

    @cached_property
    def underlay_isis(self) -> bool:
        return (
            self.shared_utils.underlay_routing_protocol in ["isis", "isis-sr", "isis-ldp", "isis-sr-ldp"]
            and self.shared_utils.underlay_router
            and self.shared_utils.uplink_type in ["p2p", "p2p-vrfs"]
        )

    @cached_property
    def underlay_ipv6(self) -> bool:
        return self.inputs.underlay_ipv6 and self.shared_utils.underlay_router

    @cached_property
    def underlay_multicast(self) -> bool:
        return self.inputs.underlay_multicast and self.shared_utils.underlay_router

    @cached_property
    def underlay_multicast_rp_interfaces(self) -> list[dict] | None:
        if not self.underlay_multicast or not self.inputs.underlay_multicast_rps:
            return None

        underlay_multicast_rp_interfaces = []
        for rp_entry in self.inputs.underlay_multicast_rps:
            if self.shared_utils.hostname not in rp_entry.nodes:
                continue

            underlay_multicast_rp_interfaces.append(
                {
                    "name": f"Loopback{rp_entry.nodes[self.shared_utils.hostname].loopback_number}",
                    "description": rp_entry.nodes[self.shared_utils.hostname].description,
                    "ip_address": f"{rp_entry.rp}/32",
                },
            )

        if underlay_multicast_rp_interfaces:
            return underlay_multicast_rp_interfaces

        return None
