# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError
from pyavd._utils import get
from pyavd.j2filters import range_expand

if TYPE_CHECKING:
    from . import SharedUtils


class RoutingMixin:
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def underlay_routing_protocol(self: SharedUtils) -> str:
        default_underlay_routing_protocol = get(self.node_type_key_data, "default_underlay_routing_protocol", default="ebgp")
        return str(get(self.hostvars, "underlay_routing_protocol", default=default_underlay_routing_protocol)).lower()

    @cached_property
    def overlay_routing_protocol(self: SharedUtils) -> str:
        default_overlay_routing_protocol = get(self.node_type_key_data, "default_overlay_routing_protocol", default="ebgp")
        return str(get(self.hostvars, "overlay_routing_protocol", default=default_overlay_routing_protocol)).lower()

    @cached_property
    def overlay_address_families(self: SharedUtils) -> list:
        if self.overlay_routing_protocol in ["ebgp", "ibgp"]:
            default_overlay_address_families = get(self.node_type_key_data, "default_overlay_address_families", ["evpn"])
            return get(self.switch_data_combined, "overlay_address_families", default=default_overlay_address_families)
        return []

    @cached_property
    def bgp(self: SharedUtils) -> bool:
        """Boolean telling if BGP Routing should be configured."""
        if not self.underlay_router:
            return False

        return (
            self.uplink_type in ["p2p", "p2p-vrfs", "lan"]
            and (
                self.underlay_routing_protocol == "ebgp"
                or (
                    self.overlay_routing_protocol in ["ebgp", "ibgp"]
                    and (self.evpn_role in ["client", "server"] or self.mpls_overlay_role in ["client", "server"])
                )
                or self.bgp_in_network_services
            )
        ) or bool(self.l3_interfaces_bgp_neighbors)

    @cached_property
    def router_id(self: SharedUtils) -> str | None:
        """Render IP address for router_id."""
        if self.underlay_router:
            return self.ip_addressing.router_id()
        return None

    @cached_property
    def ipv6_router_id(self: SharedUtils) -> str | None:
        """Render IPv6 address for router_id."""
        if self.underlay_router and self.underlay_ipv6:
            return self.ip_addressing.ipv6_router_id()
        return None

    @cached_property
    def isis_instance_name(self: SharedUtils) -> str | None:
        if self.underlay_router and self.underlay_routing_protocol in ["isis", "isis-ldp", "isis-sr", "isis-sr-ldp"]:
            default_isis_instance_name = "CORE" if self.mpls_lsr else "EVPN_UNDERLAY"
            return get(self.hostvars, "underlay_isis_instance_name", default=default_isis_instance_name)
        return None

    @cached_property
    def bgp_as(self: SharedUtils) -> str | None:
        """
        Get global bgp_as or fabric_topology bgp_as.

        At least one of global bgp_as or fabric_topology bgp_as must be defined.

        AS ranges in fabric_topology bgp_as will be expanded to a list and:
         - For standalone or A/A MH devices, the node id will be used to index into the list to find the ASN.
         - For MLAG devices, the node id of the first node in the node group will be used to index into the ASN list.
         - If a bare ASN is used, that ASN will be used for all relevant devices (depending on whether defined
           at the defaults, node_group or node level).
         - Lower level definitions override higher level definitions as is standard with AVD.
        """
        if self.bgp:
            if get(self.hostvars, "bgp_as") is not None:
                return str(get(self.hostvars, "bgp_as"))

            bgp_as_range_expanded = range_expand(str(get(self.switch_data_combined, "bgp_as", required=True)))
            try:
                if len(bgp_as_range_expanded) == 1:
                    return bgp_as_range_expanded[0]
                if self.mlag:
                    return bgp_as_range_expanded[self.mlag_switch_ids["primary"] - 1]

                if self.id is None:
                    msg = f"'id' is not set on '{self.hostname}' and is required when expanding 'bgp_as'"
                    raise AristaAvdInvalidInputsError(msg)
                return bgp_as_range_expanded[self.id - 1]
            except IndexError as exc:
                msg = f"Unable to allocate BGP AS: bgp_as range is too small ({len(bgp_as_range_expanded)}) for the id of the device"
                raise AristaAvdError(msg) from exc
        return None

    @cached_property
    def always_configure_ip_routing(self: SharedUtils) -> bool:
        return get(self.switch_data_combined, "always_configure_ip_routing")
