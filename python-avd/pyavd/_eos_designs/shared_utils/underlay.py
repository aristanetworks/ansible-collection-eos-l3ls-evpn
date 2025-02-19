# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen

if TYPE_CHECKING:
    from . import SharedUtilsProtocol


class UnderlayMixin(Protocol):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def underlay_bgp(self: SharedUtilsProtocol) -> bool:
        return self.bgp and self.underlay_routing_protocol == "ebgp" and self.underlay_router and self.uplink_type in ["p2p", "p2p-vrfs"]

    @cached_property
    def underlay_mpls(self: SharedUtilsProtocol) -> bool:
        return (
            self.underlay_routing_protocol in ["isis-sr", "isis-ldp", "isis-sr-ldp", "ospf-ldp"]
            and self.mpls_lsr
            and self.underlay_router
            and self.uplink_type in ["p2p", "p2p-vrfs"]
        )

    @cached_property
    def underlay_ldp(self: SharedUtilsProtocol) -> bool:
        return self.underlay_routing_protocol in ["isis-ldp", "isis-sr-ldp", "ospf-ldp"] and self.underlay_mpls

    @cached_property
    def underlay_sr(self: SharedUtilsProtocol) -> bool:
        return self.underlay_routing_protocol in ["isis-sr", "isis-sr-ldp"] and self.underlay_mpls

    @cached_property
    def underlay_ospf(self: SharedUtilsProtocol) -> bool:
        return self.underlay_routing_protocol in ["ospf", "ospf-ldp"] and self.underlay_router and self.uplink_type in ["p2p", "p2p-vrfs"]

    @cached_property
    def underlay_isis(self: SharedUtilsProtocol) -> bool:
        return (
            self.underlay_routing_protocol in ["isis", "isis-sr", "isis-ldp", "isis-sr-ldp"]
            and self.underlay_router
            and self.uplink_type in ["p2p", "p2p-vrfs"]
        )

    @cached_property
    def underlay_ipv6(self: SharedUtilsProtocol) -> bool:
        return self.inputs.underlay_ipv6 and self.underlay_router

    @cached_property
    def underlay_multicast(self: SharedUtilsProtocol) -> bool:
        return self.inputs.underlay_multicast and self.underlay_router

    @cached_property
    def underlay_multicast_rp_interfaces(self: SharedUtilsProtocol) -> list[EosCliConfigGen.LoopbackInterfacesItem] | None:
        if not self.underlay_multicast or not self.inputs.underlay_multicast_rps:
            return None

        underlay_multicast_rp_interfaces = []
        for rp_entry in self.inputs.underlay_multicast_rps:
            if self.hostname not in rp_entry.nodes:
                continue

            underlay_multicast_rp_interfaces.append(
                EosCliConfigGen.LoopbackInterfacesItem(
                    name=f"Loopback{rp_entry.nodes[self.hostname].loopback_number}",
                    description=rp_entry.nodes[self.hostname].description,
                    ip_address=f"{rp_entry.rp}/32",
                )
            )

        if underlay_multicast_rp_interfaces:
            return underlay_multicast_rp_interfaces

        return None
