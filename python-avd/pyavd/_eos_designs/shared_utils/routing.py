# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError, AristaAvdMissingVariableError
from pyavd.j2filters import range_expand

from .utils import UtilsMixin


class RoutingMixin(UtilsMixin):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def underlay_routing_protocol(self) -> str:
        default_underlay_routing_protocol = self.shared_utils.node_type_key_data.default_underlay_routing_protocol
        return (self.inputs.underlay_routing_protocol or default_underlay_routing_protocol).lower()

    @cached_property
    def overlay_routing_protocol(self) -> str:
        default_overlay_routing_protocol = self.shared_utils.node_type_key_data.default_overlay_routing_protocol
        return (self.inputs.overlay_routing_protocol or default_overlay_routing_protocol).lower()

    @cached_property
    def overlay_address_families(self) -> list[str]:
        if self.overlay_routing_protocol in ["ebgp", "ibgp"]:
            default_overlay_address_families = self.shared_utils.node_type_key_data.default_overlay_address_families
            return self.shared_utils.node_config.overlay_address_families._as_list() or default_overlay_address_families._as_list()
        return []

    @cached_property
    def bgp(self) -> bool:
        """Boolean telling if BGP Routing should be configured."""
        if not self.shared_utils.underlay_router:
            return False

        return (
            self.shared_utils.uplink_type in ["p2p", "p2p-vrfs", "lan"]
            and (
                self.underlay_routing_protocol == "ebgp"
                or (
                    self.overlay_routing_protocol in ["ebgp", "ibgp"]
                    and (self.shared_utils.evpn_role in ["client", "server"] or self.shared_utils.mpls_overlay_role in ["client", "server"])
                )
                or self.shared_utils.bgp_in_network_services
            )
        ) or bool(self.shared_utils.l3_interfaces_bgp_neighbors)

    @cached_property
    def router_id(self) -> str | None:
        """Render IP address for router_id."""
        if self.shared_utils.underlay_router:
            return self.shared_utils.ip_addressing.router_id()
        return None

    @cached_property
    def ipv6_router_id(self) -> str | None:
        """Render IPv6 address for router_id."""
        if self.shared_utils.underlay_router and self.shared_utils.underlay_ipv6:
            return self.shared_utils.ip_addressing.ipv6_router_id()
        return None

    @cached_property
    def isis_instance_name(self) -> str | None:
        if self.shared_utils.underlay_router and self.underlay_routing_protocol in ["isis", "isis-ldp", "isis-sr", "isis-sr-ldp"]:
            default_isis_instance_name = "CORE" if self.shared_utils.mpls_lsr else "EVPN_UNDERLAY"
            return self.inputs.underlay_isis_instance_name or default_isis_instance_name
        return None

    @cached_property
    def bgp_as(self) -> str | None:
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
        if not self.bgp:
            return None

        if self.inputs.bgp_as:
            return self.inputs.bgp_as

        if self.shared_utils.node_config.bgp_as is None:
            msg = "bgp_as"
            raise AristaAvdMissingVariableError(msg)

        bgp_as_range_expanded = range_expand(self.shared_utils.node_config.bgp_as)
        try:
            if len(bgp_as_range_expanded) == 1:
                return bgp_as_range_expanded[0]
            if self.shared_utils.mlag_switch_ids:
                return bgp_as_range_expanded[self.shared_utils.mlag_switch_ids["primary"] - 1]

            if self.shared_utils.id is None:
                msg = f"'id' is not set on '{self.shared_utils.hostname}' and is required when expanding 'bgp_as'"
                raise AristaAvdInvalidInputsError(msg)
            return bgp_as_range_expanded[self.shared_utils.id - 1]
        except IndexError as exc:
            msg = f"Unable to allocate BGP AS: bgp_as range is too small ({len(bgp_as_range_expanded)}) for the id of the device"
            raise AristaAvdError(msg) from exc
