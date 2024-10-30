# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ipaddress
from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError
from pyavd._utils import default, get, get_item
from pyavd.j2filters import natural_sort

from .utils_wan import UtilsWanMixin
from .utils_zscaler import UtilsZscalerMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class UtilsMixin(UtilsWanMixin, UtilsZscalerMixin):
    """
    Mixin Class with internal functions.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def _trunk_groups_mlag_name(self: AvdStructuredConfigNetworkServices) -> str:
        return get(self.shared_utils.trunk_groups, "mlag.name", required=True)

    @cached_property
    def _trunk_groups_mlag_l3_name(self: AvdStructuredConfigNetworkServices) -> str:
        return get(self.shared_utils.trunk_groups, "mlag_l3.name", required=True)

    @cached_property
    def _trunk_groups_uplink_name(self: AvdStructuredConfigNetworkServices) -> str:
        return get(self.shared_utils.trunk_groups, "uplink.name", required=True)

    @cached_property
    def _local_endpoint_trunk_groups(self: AvdStructuredConfigNetworkServices) -> set:
        return set(get(self._hostvars, "switch.local_endpoint_trunk_groups", default=[]))

    @cached_property
    def _vrf_default_evpn(self: AvdStructuredConfigNetworkServices) -> bool:
        """Return boolean telling if VRF "default" is running EVPN or not."""
        if not (self.shared_utils.network_services_l3 and self.shared_utils.overlay_vtep and self.shared_utils.overlay_evpn):
            return False

        for tenant in self.shared_utils.filtered_tenants:
            if (vrf_default := get_item(tenant["vrfs"], "name", "default")) is None:
                continue

            if "evpn" in vrf_default.get("address_families", ["evpn"]):
                if self.shared_utils.underlay_filter_peer_as:
                    msg = "'underlay_filter_peer_as' cannot be used while there are EVPN services in the default VRF."
                    raise AristaAvdError(msg)
                return True

        return False

    @cached_property
    def _vrf_default_ipv4_subnets(self: AvdStructuredConfigNetworkServices) -> list[str]:
        """Return list of ipv4 subnets in VRF "default"."""
        subnets = []
        for tenant in self.shared_utils.filtered_tenants:
            if (vrf_default := get_item(tenant["vrfs"], "name", "default")) is None:
                continue

            for svi in vrf_default["svis"]:
                ip_address = default(svi.get("ip_address"), svi.get("ip_address_virtual"))
                if ip_address is None:
                    continue

                subnet = str(ipaddress.ip_network(ip_address, strict=False))
                if subnet not in subnets:
                    subnets.append(subnet)

        return subnets

    @cached_property
    def _vrf_default_ipv4_static_routes(self: AvdStructuredConfigNetworkServices) -> dict:
        """
        Finds static routes defined under VRF "default" and find out if they should be redistributed in underlay and/or overlay.

        Returns:
        -------
        dict
            static_routes: []
                List of ipv4 static routes in VRF "default"
            redistribute_in_underlay: bool
                Whether to redistribute static into the underlay protocol.
                True when there are any static routes this device is not an EVPN VTEP.
                Can be overridden with "vrf.redistribute_static: False".
            redistribute_in_overlay: bool
                Whether to redistribute static into overlay protocol for vrf default.
                True there are any static routes and this device is an EVPN VTEP.
                Can be overridden with "vrf.redistribute_static: False".
        """
        vrf_default_ipv4_static_routes = set()
        vrf_default_redistribute_static = True
        for tenant in self.shared_utils.filtered_tenants:
            if (vrf_default := get_item(tenant["vrfs"], "name", "default")) is None:
                continue

            if (static_routes := vrf_default.get("static_routes")) is None:
                continue

            for static_route in static_routes:
                vrf_default_ipv4_static_routes.add(static_route["destination_address_prefix"])

            vrf_default_redistribute_static = vrf_default.get("redistribute_static", vrf_default_redistribute_static)

        if self.shared_utils.overlay_evpn and self.shared_utils.overlay_vtep:
            # This is an EVPN VTEP
            redistribute_in_underlay = False
            redistribute_in_overlay = vrf_default_redistribute_static and vrf_default_ipv4_static_routes
        else:
            # This is a not an EVPN VTEP
            redistribute_in_underlay = vrf_default_redistribute_static and vrf_default_ipv4_static_routes
            redistribute_in_overlay = False

        return {
            "static_routes": natural_sort(vrf_default_ipv4_static_routes),
            "redistribute_in_underlay": redistribute_in_underlay,
            "redistribute_in_overlay": redistribute_in_overlay,
        }

    def _mlag_ibgp_peering_enabled(self: AvdStructuredConfigNetworkServices, vrf: dict, tenant: dict) -> bool:
        """
        Returns True if mlag ibgp_peering is enabled.

        For VRF default we return False unless there is no underlay routing protocol.

        False otherwise.
        """
        if not self.shared_utils.mlag_l3 or not self.shared_utils.network_services_l3:
            return False

        mlag_ibgp_peering: bool = default(vrf.get("enable_mlag_ibgp_peering_vrfs"), tenant.get("enable_mlag_ibgp_peering_vrfs"), True)  # noqa: FBT003
        return (vrf["name"] != "default" or self.shared_utils.underlay_routing_protocol == "none") and mlag_ibgp_peering

    def _mlag_ibgp_peering_vlan_vrf(self: AvdStructuredConfigNetworkServices, vrf: dict, tenant: dict) -> int | None:
        """
        MLAG IBGP Peering VLANs per VRF.

        Performs all relevant checks if MLAG IBGP Peering is enabled
        Returns None if peering is not enabled
        """
        if not self._mlag_ibgp_peering_enabled(vrf, tenant):
            return None

        if (mlag_ibgp_peering_vlan := get(vrf, "mlag_ibgp_peering_vlan")) is not None:
            vlan_id = mlag_ibgp_peering_vlan
        else:
            base_vlan = self.shared_utils.mlag_ibgp_peering_vrfs_base_vlan
            vrf_id = vrf.get("vrf_id", vrf.get("vrf_vni"))
            if vrf_id is None:
                msg = f"Unable to assign MLAG VRF Peering VLAN for vrf {vrf['name']}.Set either 'mlag_ibgp_peering_vlan' or 'vrf_id' or 'vrf_vni' on the VRF"
                raise AristaAvdInvalidInputsError(msg)
            vlan_id = base_vlan + int(vrf_id) - 1

        return vlan_id

    def _exclude_mlag_ibgp_peering_from_redistribute(self: AvdStructuredConfigNetworkServices, vrf: dict, tenant: dict) -> bool | None:
        """
        Returns True if redistribute_connected is True and MLAG IBGP Peering subnet should be _excluded_ from redistribution for the given vrf/tenant.

        Does _not_ include checks if the peering is enabled at all, so that should be checked first.
        """
        if get(vrf, "redistribute_connected", True) is True:
            return default(vrf.get("redistribute_mlag_ibgp_peering_vrfs"), tenant.get("redistribute_mlag_ibgp_peering_vrfs"), False) is False  # noqa: FBT003

        return None

    @cached_property
    def _configure_bgp_mlag_peer_group(self: AvdStructuredConfigNetworkServices) -> bool:
        """
        Flag set during creating of BGP VRFs if an MLAG peering is needed.

        Decides if MLAG BGP peer-group should be configured.
        Catches cases where underlay is not BGP but we still need MLAG iBGP peering.
        """
        if self.shared_utils.underlay_bgp:
            return False

        # Checking neighbors directly under BGP to cover VRF default case.
        for neighbor_settings in get(self._router_bgp_vrfs, "neighbors", default=[]):
            if neighbor_settings.get("peer_group") == self.shared_utils.bgp_peer_groups["mlag_ipv4_underlay_peer"]["name"]:
                return True

        for bgp_vrf in get(self._router_bgp_vrfs, "vrfs", default=[]):
            if "neighbors" not in bgp_vrf:
                continue
            for neighbor_settings in bgp_vrf["neighbors"]:
                if neighbor_settings.get("peer_group") == self.shared_utils.bgp_peer_groups["mlag_ipv4_underlay_peer"]["name"]:
                    return True

        return False
