# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from ipaddress import ip_address
from re import fullmatch
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError
from pyavd._utils import default

if TYPE_CHECKING:
    from . import SharedUtils


class OverlayMixin:
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def vtep_loopback(self: SharedUtils) -> str:
        """The default is Loopback1 except for WAN devices where the default is Dps1."""
        default_vtep_loopback = "Dps1" if self.is_wan_router else "Loopback1"
        return default(self.node_config.vtep_loopback, default_vtep_loopback)

    @cached_property
    def evpn_role(self: SharedUtils) -> str | None:
        if self.underlay_router:
            default_evpn_role = self.node_type_key_data.default_evpn_role
            if self.is_wan_router and self.inputs.wan_use_evpn_node_settings_for_lan:
                default_evpn_role = None
            return default(self.node_config.evpn_role, default_evpn_role)
        return None

    @cached_property
    def mpls_overlay_role(self: SharedUtils) -> str | None:
        if self.underlay_router:
            default_mpls_overlay_role = self.node_type_key_data.default_mpls_overlay_role
            return default(self.node_config.mpls_overlay_role, default_mpls_overlay_role)
        return None

    @cached_property
    def overlay_rd_type_admin_subfield(self: SharedUtils) -> str:
        admin_subfield = self.inputs.overlay_rd_type.admin_subfield
        admin_subfield_offset = self.inputs.overlay_rd_type.admin_subfield_offset
        return self.get_rd_admin_subfield_value(admin_subfield, admin_subfield_offset)

    @cached_property
    def overlay_rd_type_vrf_admin_subfield(self: SharedUtils) -> str:
        vrf_admin_subfield: str = default(self.inputs.overlay_rd_type.vrf_admin_subfield, self.inputs.overlay_rd_type.admin_subfield)
        vrf_admin_subfield_offset: int = default(self.inputs.overlay_rd_type.vrf_admin_subfield_offset, self.inputs.overlay_rd_type.admin_subfield_offset)
        return self.get_rd_admin_subfield_value(vrf_admin_subfield, vrf_admin_subfield_offset)

    def get_rd_admin_subfield_value(self: SharedUtils, admin_subfield: str, admin_subfield_offset: int) -> str:
        if admin_subfield in ["router_id", "overlay_loopback_ip"]:
            return self.router_id

        if admin_subfield == "vtep_loopback":
            return self.vtep_ip

        if admin_subfield == "bgp_as":
            return self.bgp_as

        if admin_subfield == "switch_id":
            if self.id is None:
                msg = f"'id' is not set on '{self.hostname}' and 'overlay_rd_type_admin_subfield' is set to 'switch_id'"
                raise AristaAvdInvalidInputsError(msg)
            return self.id + admin_subfield_offset

        if fullmatch(r"\d+", str(admin_subfield)):
            return str(int(admin_subfield) + admin_subfield_offset)

        try:
            ip_address(admin_subfield)
        except ValueError:
            return self.router_id

        return admin_subfield

    @cached_property
    def overlay_routing_protocol_address_family(self: SharedUtils) -> str:
        overlay_routing_protocol_address_family = self.inputs.overlay_routing_protocol_address_family
        if overlay_routing_protocol_address_family == "ipv6" and not (self.underlay_ipv6 is True and self.inputs.underlay_rfc5549):
            msg = "'overlay_routing_protocol_address_family: ipv6' is only supported in combination with 'underlay_ipv6: True' and 'underlay_rfc5549: True'"
            raise AristaAvdError(msg)
        return overlay_routing_protocol_address_family

    @cached_property
    def evpn_encapsulation(self: SharedUtils) -> str:
        """EVPN encapsulation based on fabric_evpn_encapsulation and node default_evpn_encapsulation."""
        return default(self.inputs.fabric_evpn_encapsulation, self.node_type_key_data.default_evpn_encapsulation)

    @cached_property
    def evpn_soo(self: SharedUtils) -> str:
        """
        Site-Of-Origin used as BGP extended community.

        - For regular VTEPs this is <vtep_ip>:1
        - For WAN routers this is <router_id_of_primary_HA_router>:<site_id or 0>
        - Otherwise this is <router_id>:1.

        TODO: Reconsider if suffix should just be :1 for all WAN routers.
        """
        if self.is_wan_router:
            # for Pathfinder, no HA, no Site ID
            if not self.is_cv_pathfinder_client:
                return f"{self.router_id}:0"

            if self.wan_site is None:
                # Should never happen but just in case.
                msg = "Could not find 'cv_pathfinder_site' so it is not possible to generate evpn_soo."
                raise AristaAvdInvalidInputsError(msg)

            if not self.wan_ha:
                return f"{self.router_id}:{self.wan_site.id}"
            if self.is_first_ha_peer:
                return f"{self.router_id}:{self.wan_site.id}"

            peer_fact = self.get_peer_facts(self.wan_ha_peer, required=True)
            return f"{peer_fact['router_id']}:{self.wan_site.id}"

        if self.overlay_vtep:
            return f"{self.vtep_ip}:1"

        return f"{self.router_id}:1"

    @cached_property
    def overlay_evpn(self: SharedUtils) -> bool:
        # Set overlay_evpn to enable EVPN on the node
        return (
            self.bgp
            and (self.evpn_role in ["client", "server"] or self.mpls_overlay_role in ["client", "server"])
            and self.overlay_routing_protocol in ["ebgp", "ibgp"]
            and "evpn" in self.overlay_address_families
        )

    @cached_property
    def overlay_mpls(self: SharedUtils) -> bool:
        """Set overlay_mpls to enable MPLS as the primary overlay."""
        return any([self.overlay_evpn_mpls, self.overlay_vpn_ipv4, self.overlay_vpn_ipv6]) and not self.overlay_evpn_vxlan

    @cached_property
    def overlay_ipvpn_gateway(self: SharedUtils) -> bool:
        # Set overlay_ipvpn_gateway to trigger ipvpn interworking configuration.
        return self.overlay_evpn and self.node_config.ipvpn_gateway.enabled

    @cached_property
    def overlay_ler(self: SharedUtils) -> bool:
        return self.underlay_mpls and (self.mpls_overlay_role in ["client", "server"] or self.evpn_role in ["client", "server"]) and (self.any_network_services)

    @cached_property
    def overlay_vtep(self: SharedUtils) -> bool:
        # Set overlay_vtep to enable VXLAN VTEP
        return (
            self.overlay_routing_protocol in ["ebgp", "ibgp", "her", "cvx"]
            and (self.network_services_l2 or self.network_services_l3)
            and self.underlay_router
            and self.uplink_type in ["p2p", "p2p-vrfs", "lan"]
            and self.vtep
        )

    @cached_property
    def overlay_vpn_ipv4(self: SharedUtils) -> bool:
        # Set overlay_vpn_ipv4 enable IP-VPN configuration on the node.
        if self.bgp is not True:
            return False

        return (self.overlay_routing_protocol == "ibgp" and "vpn-ipv4" in self.overlay_address_families) or (
            "vpn-ipv4" in self.node_config.ipvpn_gateway.address_families and self.overlay_ipvpn_gateway
        )

    @cached_property
    def overlay_vpn_ipv6(self: SharedUtils) -> bool:
        # Set overlay_vpn_ipv4 to enable IP-VPN configuration on the node.
        if self.bgp is not True:
            return False

        return (self.overlay_routing_protocol == "ibgp" and "vpn-ipv6" in self.overlay_address_families) or (
            "vpn-ipv6" in self.node_config.ipvpn_gateway.address_families and self.overlay_ipvpn_gateway
        )

    @cached_property
    def overlay_peering_address(self: SharedUtils) -> str | None:
        if not self.underlay_router:
            return None

        if self.overlay_routing_protocol_address_family == "ipv6":
            return self.ipv6_router_id

        return self.router_id

    @cached_property
    def overlay_cvx(self: SharedUtils) -> bool:
        return self.overlay_routing_protocol == "cvx"

    @cached_property
    def overlay_her(self: SharedUtils) -> bool:
        return self.overlay_routing_protocol == "her"

    @cached_property
    def overlay_dpath(self: SharedUtils) -> bool:
        # Set dpath based on ipvpn_gateway parameters
        return self.overlay_ipvpn_gateway and self.node_config.ipvpn_gateway.enable_d_path

    @cached_property
    def overlay_evpn_vxlan(self: SharedUtils) -> bool:
        return self.overlay_evpn and self.evpn_encapsulation == "vxlan"

    @cached_property
    def overlay_evpn_mpls(self: SharedUtils) -> bool:
        return self.overlay_evpn and self.evpn_encapsulation == "mpls"
