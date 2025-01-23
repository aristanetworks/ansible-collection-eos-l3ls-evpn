# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from ipaddress import ip_address
from re import fullmatch

from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError
from pyavd._utils import default

from .utils import UtilsMixin


class OverlayMixin(UtilsMixin):
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def vtep_loopback(self) -> str:
        """The default is Loopback1 except for WAN devices where the default is Dps1."""
        default_vtep_loopback = "Dps1" if self.shared_utils.is_wan_router else "Loopback1"
        return default(self.shared_utils.node_config.vtep_loopback, default_vtep_loopback)

    @cached_property
    def evpn_role(self) -> str | None:
        if self.shared_utils.underlay_router:
            default_evpn_role = self.shared_utils.node_type_key_data.default_evpn_role
            return default(self.shared_utils.node_config.evpn_role, default_evpn_role)
        return None

    @cached_property
    def mpls_overlay_role(self) -> str | None:
        if self.shared_utils.underlay_router:
            default_mpls_overlay_role = self.shared_utils.node_type_key_data.default_mpls_overlay_role
            return default(self.shared_utils.node_config.mpls_overlay_role, default_mpls_overlay_role)
        return None

    @cached_property
    def overlay_rd_type_admin_subfield(self) -> str:
        admin_subfield = self.inputs.overlay_rd_type.admin_subfield
        admin_subfield_offset = self.inputs.overlay_rd_type.admin_subfield_offset
        return self.get_rd_admin_subfield_value(admin_subfield, admin_subfield_offset)

    @cached_property
    def overlay_rd_type_vrf_admin_subfield(self) -> str:
        vrf_admin_subfield: str = default(self.inputs.overlay_rd_type.vrf_admin_subfield, self.inputs.overlay_rd_type.admin_subfield)
        vrf_admin_subfield_offset: int = default(self.inputs.overlay_rd_type.vrf_admin_subfield_offset, self.inputs.overlay_rd_type.admin_subfield_offset)
        return self.get_rd_admin_subfield_value(vrf_admin_subfield, vrf_admin_subfield_offset)

    def get_rd_admin_subfield_value(self, admin_subfield: str, admin_subfield_offset: int) -> str:
        if admin_subfield in ["router_id", "overlay_loopback_ip"]:
            return self.shared_utils.router_id

        if admin_subfield == "vtep_loopback":
            return self.shared_utils.vtep_ip

        if admin_subfield == "bgp_as":
            return self.shared_utils.bgp_as

        if admin_subfield == "switch_id":
            if self.shared_utils.id is None:
                msg = f"'id' is not set on '{self.shared_utils.hostname}' and 'overlay_rd_type_admin_subfield' is set to 'switch_id'"
                raise AristaAvdInvalidInputsError(msg)
            return self.shared_utils.id + admin_subfield_offset

        if fullmatch(r"\d+", str(admin_subfield)):
            return str(int(admin_subfield) + admin_subfield_offset)

        try:
            ip_address(admin_subfield)
        except ValueError:
            return self.shared_utils.router_id

        return admin_subfield

    @cached_property
    def overlay_routing_protocol_address_family(self) -> str:
        overlay_routing_protocol_address_family = self.inputs.overlay_routing_protocol_address_family
        if overlay_routing_protocol_address_family == "ipv6" and not (self.shared_utils.underlay_ipv6 is True and self.inputs.underlay_rfc5549):
            msg = "'overlay_routing_protocol_address_family: ipv6' is only supported in combination with 'underlay_ipv6: True' and 'underlay_rfc5549: True'"
            raise AristaAvdError(msg)
        return overlay_routing_protocol_address_family

    @cached_property
    def evpn_encapsulation(self) -> str:
        """EVPN encapsulation based on fabric_evpn_encapsulation and node default_evpn_encapsulation."""
        return default(self.inputs.fabric_evpn_encapsulation, self.shared_utils.node_type_key_data.default_evpn_encapsulation)

    @cached_property
    def evpn_soo(self) -> str:
        """
        Site-Of-Origin used as BGP extended community.

        - For regular VTEPs this is <vtep_ip>:1
        - For WAN routers this is <router_id_of_primary_HA_router>:<site_id or 0>
        - Otherwise this is <router_id>:1.

        TODO: Reconsider if suffix should just be :1 for all WAN routers.
        """
        if self.shared_utils.is_wan_router:
            # for Pathfinder, no HA, no Site ID
            if not self.shared_utils.is_cv_pathfinder_client:
                return f"{self.shared_utils.router_id}:0"

            if self.shared_utils.wan_site is None:
                # Should never happen but just in case.
                msg = "Could not find 'cv_pathfinder_site' so it is not possible to generate evpn_soo."
                raise AristaAvdInvalidInputsError(msg)

            if not self.shared_utils.wan_ha:
                return f"{self.shared_utils.router_id}:{self.shared_utils.wan_site.id}"
            if self.shared_utils.is_first_ha_peer:
                return f"{self.shared_utils.router_id}:{self.shared_utils.wan_site.id}"

            peer_fact = self.get_peer_facts_dict(self.shared_utils.wan_ha_peer)
            return f"{peer_fact['router_id']}:{self.shared_utils.wan_site.id}"

        if self.overlay_vtep:
            return f"{self.shared_utils.vtep_ip}:1"

        return f"{self.shared_utils.router_id}:1"

    @cached_property
    def overlay_evpn(self) -> bool:
        # Set overlay_evpn to enable EVPN on the node
        return (
            self.shared_utils.bgp
            and (self.evpn_role in ["client", "server"] or self.mpls_overlay_role in ["client", "server"])
            and self.shared_utils.overlay_routing_protocol in ["ebgp", "ibgp"]
            and "evpn" in self.shared_utils.overlay_address_families
        )

    @cached_property
    def overlay_mpls(self) -> bool:
        """Set overlay_mpls to enable MPLS as the primary overlay."""
        return any([self.overlay_evpn_mpls, self.overlay_vpn_ipv4, self.overlay_vpn_ipv6]) and not self.overlay_evpn_vxlan

    @cached_property
    def overlay_ipvpn_gateway(self) -> bool:
        # Set overlay_ipvpn_gateway to trigger ipvpn interworking configuration.
        return self.overlay_evpn and self.shared_utils.node_config.ipvpn_gateway.enabled

    @cached_property
    def overlay_ler(self) -> bool:
        return (
            self.shared_utils.underlay_mpls
            and (self.mpls_overlay_role in ["client", "server"] or self.evpn_role in ["client", "server"])
            and (self.shared_utils.any_network_services)
        )

    @cached_property
    def overlay_vtep(self) -> bool:
        # Set overlay_vtep to enable VXLAN VTEP
        return (
            self.shared_utils.overlay_routing_protocol in ["ebgp", "ibgp", "her", "cvx"]
            and (self.shared_utils.network_services_l2 or self.shared_utils.network_services_l3)
            and self.shared_utils.underlay_router
            and self.shared_utils.uplink_type in ["p2p", "p2p-vrfs", "lan"]
            and self.shared_utils.vtep
        )

    @cached_property
    def overlay_vpn_ipv4(self) -> bool:
        # Set overlay_vpn_ipv4 enable IP-VPN configuration on the node.
        if self.shared_utils.bgp is not True:
            return False

        return (self.shared_utils.overlay_routing_protocol == "ibgp" and "vpn-ipv4" in self.shared_utils.overlay_address_families) or (
            "vpn-ipv4" in self.shared_utils.node_config.ipvpn_gateway.address_families and self.overlay_ipvpn_gateway
        )

    @cached_property
    def overlay_vpn_ipv6(self) -> bool:
        # Set overlay_vpn_ipv4 to enable IP-VPN configuration on the node.
        if self.shared_utils.bgp is not True:
            return False

        return (self.shared_utils.overlay_routing_protocol == "ibgp" and "vpn-ipv6" in self.shared_utils.overlay_address_families) or (
            "vpn-ipv6" in self.shared_utils.node_config.ipvpn_gateway.address_families and self.overlay_ipvpn_gateway
        )

    @cached_property
    def overlay_peering_address(self) -> str | None:
        if not self.shared_utils.underlay_router:
            return None

        if self.overlay_routing_protocol_address_family == "ipv6":
            return self.shared_utils.ipv6_router_id

        return self.shared_utils.router_id

    @cached_property
    def overlay_cvx(self) -> bool:
        return self.shared_utils.overlay_routing_protocol == "cvx"

    @cached_property
    def overlay_her(self) -> bool:
        return self.shared_utils.overlay_routing_protocol == "her"

    @cached_property
    def overlay_dpath(self) -> bool:
        # Set dpath based on ipvpn_gateway parameters
        return self.overlay_ipvpn_gateway and self.shared_utils.node_config.ipvpn_gateway.enable_d_path

    @cached_property
    def overlay_evpn_vxlan(self) -> bool:
        return self.overlay_evpn and self.evpn_encapsulation == "vxlan"

    @cached_property
    def overlay_evpn_mpls(self) -> bool:
        return self.overlay_evpn and self.evpn_encapsulation == "mpls"
