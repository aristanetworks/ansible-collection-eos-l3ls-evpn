# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ipaddress
from functools import cached_property
from re import fullmatch as re_fullmatch
from typing import TYPE_CHECKING

from pyavd._eos_designs.structured_config.structured_config_generator import StructuredConfigGenerator
from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError
from pyavd._utils import append_if_not_duplicate, default, get, get_ip_from_ip_prefix, get_item
from pyavd._utils.format_string import AvdStringFormatter
from pyavd._utils.strip_empties import strip_empties_from_dict, strip_empties_from_list
from pyavd.j2filters import natural_sort

from .utils_wan import UtilsWanMixin

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns


class UtilsMixin(UtilsWanMixin, StructuredConfigGenerator):
    """
    Mixin Class with internal functions.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def _local_endpoint_trunk_groups(self) -> set:
        return set(get(self._hostvars, "switch.local_endpoint_trunk_groups", default=[]))

    @cached_property
    def _vrf_default_evpn(self) -> bool:
        """Return boolean telling if VRF "default" is running EVPN or not."""
        if not (self.shared_utils.network_services_l3 and self.shared_utils.overlay_vtep and self.shared_utils.overlay_evpn):
            return False

        for tenant in self.shared_utils.filtered_tenants:
            if "default" not in tenant.vrfs:
                continue

            if "evpn" in tenant.vrfs["default"].address_families:
                if self.inputs.underlay_filter_peer_as:
                    msg = "'underlay_filter_peer_as' cannot be used while there are EVPN services in the default VRF."
                    raise AristaAvdError(msg)
                return True

        return False

    @cached_property
    def _vrf_default_ipv4_subnets(self) -> list[str]:
        """Return list of ipv4 subnets in VRF "default"."""
        subnets = []
        for tenant in self.shared_utils.filtered_tenants:
            if "default" not in tenant.vrfs:
                continue

            for svi in tenant.vrfs["default"].svis:
                ip_address = default(svi.ip_address, svi.ip_address_virtual)
                if ip_address is None:
                    continue

                subnet = str(ipaddress.ip_network(ip_address, strict=False))
                if subnet not in subnets:
                    subnets.append(subnet)

        return subnets

    @cached_property
    def _vrf_default_ipv4_static_routes(self) -> dict:
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
            if "default" not in tenant.vrfs:
                continue

            if not (static_routes := tenant.vrfs["default"].static_routes):
                continue

            for static_route in static_routes:
                vrf_default_ipv4_static_routes.add(static_route.destination_address_prefix)

            vrf_default_redistribute_static = default(tenant.vrfs["default"].redistribute_static, vrf_default_redistribute_static)

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

    def _mlag_ibgp_peering_enabled(
        self,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
    ) -> bool:
        """
        Returns True if mlag ibgp_peering is enabled.

        For VRF default we return False unless there is no underlay routing protocol.

        False otherwise.
        """
        if not self.shared_utils.mlag_l3 or not self.shared_utils.network_services_l3:
            return False

        mlag_ibgp_peering = default(vrf.enable_mlag_ibgp_peering_vrfs, tenant.enable_mlag_ibgp_peering_vrfs)
        return bool((vrf.name != "default" or self.shared_utils.underlay_routing_protocol == "none") and mlag_ibgp_peering)

    def _mlag_ibgp_peering_vlan_vrf(
        self,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
    ) -> int | None:
        """
        MLAG IBGP Peering VLANs per VRF.

        Performs all relevant checks if MLAG IBGP Peering is enabled
        Returns None if peering is not enabled
        """
        if not self._mlag_ibgp_peering_enabled(vrf, tenant):
            return None

        if (mlag_ibgp_peering_vlan := vrf.mlag_ibgp_peering_vlan) is not None:
            vlan_id = mlag_ibgp_peering_vlan
        else:
            base_vlan = self.inputs.mlag_ibgp_peering_vrfs.base_vlan
            vrf_id = default(vrf.vrf_id, vrf.vrf_vni)
            if vrf_id is None:
                msg = f"Unable to assign MLAG VRF Peering VLAN for vrf {vrf.name}.Set either 'mlag_ibgp_peering_vlan' or 'vrf_id' or 'vrf_vni' on the VRF"
                raise AristaAvdInvalidInputsError(msg)
            vlan_id = base_vlan + vrf_id - 1

        return vlan_id

    def _exclude_mlag_ibgp_peering_from_redistribute(
        self,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
    ) -> bool:
        """
        Returns True if redistribute_connected is True and MLAG IBGP Peering subnet should be _excluded_ from redistribution for the given vrf/tenant.

        Does _not_ include checks if the peering is enabled at all, so that should be checked first.
        """
        if vrf.redistribute_connected:
            return default(vrf.redistribute_mlag_ibgp_peering_vrfs, tenant.redistribute_mlag_ibgp_peering_vrfs) is False

        return False

    @cached_property
    def _configure_bgp_mlag_peer_group(self) -> bool:
        """
        Flag set during creating of BGP VRFs if an MLAG peering is needed.

        Decides if MLAG BGP peer-group should be configured.
        Catches cases where underlay is not BGP but we still need MLAG iBGP peering.
        """
        if self.shared_utils.underlay_bgp:
            return False

        # Checking neighbors directly under BGP to cover VRF default case.
        for neighbor_settings in get(self._router_bgp_vrfs, "neighbors", default=[]):
            if neighbor_settings.get("peer_group") == self.inputs.bgp_peer_groups.mlag_ipv4_underlay_peer.name:
                return True

        for bgp_vrf in get(self._router_bgp_vrfs, "vrfs", default=[]):
            if "neighbors" not in bgp_vrf:
                continue
            for neighbor_settings in bgp_vrf["neighbors"]:
                if neighbor_settings.get("peer_group") == self.inputs.bgp_peer_groups.mlag_ipv4_underlay_peer.name:
                    return True

        return False

    @cached_property
    def _rt_admin_subfield(self) -> str | None:
        """
        Return a string with the route-target admin subfield unless set to "vrf_id" or "vrf_vni" or "id".

        Returns None if not set, since the calling functions will use
        per-vlan numbers by default.
        """
        admin_subfield = self.inputs.overlay_rt_type.admin_subfield
        if admin_subfield is None:
            return None

        if admin_subfield == "bgp_as":
            return self.shared_utils.bgp_as

        if re_fullmatch(r"\d+", str(admin_subfield)):
            return admin_subfield

        return None

    def get_vlan_mac_vrf_id(
        self,
        vlan: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem
        | EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlansItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
    ) -> int:
        mac_vrf_id_base = default(tenant.mac_vrf_id_base, tenant.mac_vrf_vni_base)
        if mac_vrf_id_base is None:
            msg = (
                "'rt_override' or 'vni_override' or 'mac_vrf_id_base' or 'mac_vrf_vni_base' must be set. "
                f"Unable to set EVPN RD/RT for vlan {vlan.id} in Tenant '{vlan._tenant}'"
            )
            raise AristaAvdInvalidInputsError(msg)
        return mac_vrf_id_base + vlan.id

    def get_vlan_mac_vrf_vni(
        self,
        vlan: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem
        | EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlansItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
    ) -> int:
        mac_vrf_vni_base = default(tenant.mac_vrf_vni_base, tenant.mac_vrf_id_base)
        if mac_vrf_vni_base is None:
            msg = (
                "'rt_override' or 'vni_override' or 'mac_vrf_id_base' or 'mac_vrf_vni_base' must be set. "
                f"Unable to set EVPN RD/RT for vlan {vlan.id} in Tenant '{vlan._tenant}'"
            )
            raise AristaAvdInvalidInputsError(msg)
        return mac_vrf_vni_base + vlan.id

    def get_vlan_rd(
        self,
        vlan: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem
        | EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlansItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
    ) -> str:
        """Return a string with the route-destinguisher for one VLAN."""
        rd_override = default(vlan.rd_override, vlan.rt_override, vlan.vni_override)

        if isinstance(rd_override, str) and ":" in rd_override:
            return rd_override

        if rd_override is not None:
            assigned_number_subfield = rd_override
        elif self.inputs.overlay_rd_type.vlan_assigned_number_subfield == "mac_vrf_vni":
            assigned_number_subfield = self.get_vlan_mac_vrf_vni(vlan, tenant)
        elif self.inputs.overlay_rd_type.vlan_assigned_number_subfield == "vlan_id":
            assigned_number_subfield = vlan.id
        else:
            assigned_number_subfield = self.get_vlan_mac_vrf_id(vlan, tenant)

        return f"{self.shared_utils.overlay_rd_type_admin_subfield}:{assigned_number_subfield}"

    def get_vlan_rt(
        self,
        vlan: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem
        | EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlansItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
    ) -> str:
        """Return a string with the route-target for one VLAN."""
        rt_override = default(vlan.rt_override, vlan.vni_override)

        if isinstance(rt_override, str) and ":" in rt_override:
            return rt_override

        if self._rt_admin_subfield is not None:
            admin_subfield = self._rt_admin_subfield
        elif rt_override is not None:
            admin_subfield = rt_override
        elif self.inputs.overlay_rt_type.admin_subfield == "vrf_vni":
            admin_subfield = self.get_vlan_mac_vrf_vni(vlan, tenant)
        elif self.inputs.overlay_rt_type.admin_subfield == "id":
            admin_subfield = vlan.id
        else:
            admin_subfield = self.get_vlan_mac_vrf_id(vlan, tenant)

        if rt_override is not None:
            assigned_number_subfield = rt_override
        elif self.inputs.overlay_rt_type.vlan_assigned_number_subfield == "mac_vrf_vni":
            assigned_number_subfield = self.get_vlan_mac_vrf_vni(vlan, tenant)
        elif self.inputs.overlay_rt_type.vlan_assigned_number_subfield == "vlan_id":
            assigned_number_subfield = vlan.id
        else:
            assigned_number_subfield = self.get_vlan_mac_vrf_id(vlan, tenant)

        return f"{admin_subfield}:{assigned_number_subfield}"

    @cached_property
    def _vrf_rt_admin_subfield(self) -> str | None:
        """
        Return a string with the VRF route-target admin subfield unless set to "vrf_id" or "vrf_vni" or "id".

        Returns None if not set, since the calling functions will use
        per-vrf numbers by default.
        """
        admin_subfield: str = default(self.inputs.overlay_rt_type.vrf_admin_subfield, self.inputs.overlay_rt_type.admin_subfield)
        if admin_subfield == "bgp_as":
            return self.shared_utils.bgp_as

        if re_fullmatch(r"\d+", admin_subfield):
            return admin_subfield

        return None

    def get_vrf_rd(self, vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem) -> str:
        """Return a string with the route-destinguisher for one VRF."""
        rd_override = vrf.rd_override

        if rd_override is not None:
            if ":" in rd_override:
                return rd_override

            return f"{self.shared_utils.overlay_rd_type_vrf_admin_subfield}:{rd_override}"

        return f"{self.shared_utils.overlay_rd_type_vrf_admin_subfield}:{self.shared_utils.get_vrf_id(vrf)}"

    def get_vrf_rt(self, vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem) -> str:
        """Return a string with the route-target for one VRF."""
        rt_override = vrf.rt_override

        if rt_override is not None and ":" in rt_override:
            return rt_override

        if self._vrf_rt_admin_subfield is not None:
            admin_subfield = self._vrf_rt_admin_subfield
        elif default(self.inputs.overlay_rt_type.vrf_admin_subfield, self.inputs.overlay_rt_type.admin_subfield) == "vrf_vni":
            admin_subfield = self.shared_utils.get_vrf_vni(vrf)
        else:
            # Both for 'id' and 'vrf_id' options.
            admin_subfield = self.shared_utils.get_vrf_id(vrf)

        if rt_override is not None:
            return f"{admin_subfield}:{rt_override}"

        return f"{admin_subfield}:{self.shared_utils.get_vrf_id(vrf)}"

    def get_vlan_aware_bundle_rd(
        self,
        id: int,  # noqa: A002
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
        is_vrf: bool,
        rd_override: str | None = None,
    ) -> str:
        """Return a string with the route-destinguisher for one VLAN Aware Bundle."""
        admin_subfield = self.shared_utils.overlay_rd_type_vrf_admin_subfield if is_vrf else self.shared_utils.overlay_rd_type_admin_subfield

        if rd_override is not None:
            if ":" in str(rd_override):
                return rd_override

            return f"{admin_subfield}:{rd_override}"

        bundle_number = id + tenant.vlan_aware_bundle_number_base
        return f"{admin_subfield}:{bundle_number}"

    def get_vlan_aware_bundle_rt(
        self,
        id: int,  # noqa: A002
        vni: int,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
        is_vrf: bool,
        rt_override: str | None = None,
    ) -> str:
        """Return a string with the route-target for one VLAN Aware Bundle."""
        if rt_override is not None and ":" in str(rt_override):
            return rt_override

        bundle_number = id + tenant.vlan_aware_bundle_number_base

        if is_vrf and self._vrf_rt_admin_subfield is not None:
            admin_subfield = self._vrf_rt_admin_subfield
        elif is_vrf and default(self.inputs.overlay_rt_type.vrf_admin_subfield, self.inputs.overlay_rt_type.admin_subfield) == "vrf_vni":
            admin_subfield = vni
        else:
            # Both for 'id' and 'vrf_id' options.
            admin_subfield = bundle_number

        if rt_override is not None:
            return f"{admin_subfield}:{rt_override}"

        return f"{admin_subfield}:{bundle_number}"

    def get_vrf_router_id(
        self,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
        router_id: str,
        tenant_name: str,
    ) -> str | None:
        """
        Determine the router ID for a given VRF based on its configuration.

        Args:
            vrf: The VRF object containing OSPF/BGP and vtep_diagnostic details.
            router_id: The router ID type specified for the VRF (e.g., "vtep_diagnostic", "main_router_id", "none", or an IPv4 address).
            tenant_name: The name of the tenant to which the VRF belongs.

        Returns:
            The resolved router ID as a string, or None if the router ID is not applicable.

        Raises:
            AristaAvdInvalidInputsError: If required configuration for "vtep_diagnostic" router ID is missing.
        """
        # Handle "vtep_diagnostic" router ID case
        if router_id == "diagnostic_loopback":
            # Validate required configuration
            if (interface_data := self._get_vtep_diagnostic_loopback_for_vrf(vrf)) is None:
                msg = (
                    f"Invalid configuration on VRF '{vrf.name}' in Tenant '{tenant_name}'. "
                    "'vtep_diagnostic.loopback' along with either 'vtep_diagnostic.loopback_ip_pools' or 'vtep_diagnostic.loopback_ip_range' must be defined "
                    "when 'router_id' is set to 'diagnostic_loopback' on the VRF."
                )
                raise AristaAvdInvalidInputsError(msg)
            # Resolve router ID from loopback interface
            return get_ip_from_ip_prefix(interface_data["ip_address"])
        if router_id == "main_router_id":
            return self.shared_utils.router_id if not self.inputs.use_router_general_for_router_id else None
        # Handle "none" router ID
        if router_id == "none":
            return None

        # Default to the specified router ID
        return router_id

    def _get_vtep_diagnostic_loopback_for_vrf(self, vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem) -> dict | None:
        if (loopback := vrf.vtep_diagnostic.loopback) is None:
            return None

        pod_name = self.inputs.pod_name
        loopback_ip_pools = vrf.vtep_diagnostic.loopback_ip_pools
        if not (loopback_ipv4_pool := vrf.vtep_diagnostic.loopback_ip_range) and pod_name and loopback_ip_pools and pod_name in loopback_ip_pools:
            loopback_ipv4_pool = loopback_ip_pools[pod_name].ipv4_pool

        if not (loopback_ipv6_pool := vrf.vtep_diagnostic.loopback_ipv6_range) and pod_name and loopback_ip_pools and pod_name in loopback_ip_pools:
            loopback_ipv6_pool = loopback_ip_pools[pod_name].ipv6_pool

        if not loopback_ipv4_pool and not loopback_ipv6_pool:
            return None

        interface_name = f"Loopback{loopback}"
        description_template = default(vrf.vtep_diagnostic.loopback_description, self.inputs.default_vrf_diag_loopback_description)
        return strip_empties_from_dict(
            {
                "name": interface_name,
                "description": AvdStringFormatter().format(description_template, interface=interface_name, vrf=vrf.name, tenant=vrf._tenant),
                "shutdown": False,
                "vrf": vrf.name,
                "ip_address": f"{self.shared_utils.ip_addressing.vrf_loopback_ip(loopback_ipv4_pool)}/32" if loopback_ipv4_pool else None,
                "ipv6_address": f"{self.shared_utils.ip_addressing.vrf_loopback_ipv6(loopback_ipv6_pool)}/128" if loopback_ipv6_pool else None,
            }
        )

    @cached_property
    def _route_maps_vrf_default(self) -> list | None:
        """
        Route-maps for EVPN services in VRF "default".

        Called from main route_maps function

        Also checked under router_bgp_vrfs to figure out if a route-map should be set on EVPN export.
        """
        if not self._vrf_default_evpn:
            return None

        if not any([self._vrf_default_ipv4_subnets, self._vrf_default_ipv4_static_routes["static_routes"], self.shared_utils.is_wan_router]):
            return None

        route_maps = strip_empties_from_list(
            [
                self._evpn_export_vrf_default_route_map(),
                self._bgp_underlay_peers_route_map(),
                self._redistribute_connected_to_bgp_route_map(),
                self._redistribute_static_to_bgp_route_map(),
            ],
        )

        return route_maps or None

    def _bgp_mlag_peer_group_route_map(self) -> dict:
        """
        Return dict with one route-map.

        Origin Incomplete for MLAG iBGP learned routes.

        TODO: Partially duplicated from mlag. Should be moved to a common class
        """
        return {
            "name": "RM-MLAG-PEER-IN",
            "sequence_numbers": [
                {
                    "sequence": 10,
                    "type": "permit",
                    "set": ["origin incomplete"],
                    "description": "Make routes learned over MLAG Peer-link less preferred on spines to ensure optimal routing",
                },
            ],
        }

    def _connected_to_bgp_vrfs_route_map(self) -> dict:
        """
        Return dict with one route-map.

        Filter MLAG peer subnets for redistribute connected for overlay VRFs.
        """
        return {
            "name": "RM-CONN-2-BGP-VRFS",
            "sequence_numbers": [
                {
                    "sequence": 10,
                    "type": "deny",
                    "match": ["ip address prefix-list PL-MLAG-PEER-VRFS"],
                },
                {
                    "sequence": 20,
                    "type": "permit",
                },
            ],
        }

    def _evpn_export_vrf_default_route_map(self) -> dict | None:
        """
        Match the following prefixes to be exported in EVPN for VRF default.

        * SVI subnets in VRF default
        * Static routes subnets in VRF default.

        * for WAN routers, all the routes matching the SOO (which includes the two above)
        """
        sequence_numbers = []
        if self.shared_utils.is_wan_router:
            sequence_numbers.append(
                {
                    "sequence": 10,
                    "type": "permit",
                    "match": ["extcommunity ECL-EVPN-SOO"],
                },
            )
        else:
            # TODO: refactor existing behavior to SoO?
            if self._vrf_default_ipv4_subnets:
                sequence_numbers.append(
                    {
                        "sequence": 10,
                        "type": "permit",
                        "match": ["ip address prefix-list PL-SVI-VRF-DEFAULT"],
                    },
                )

            if self._vrf_default_ipv4_static_routes["static_routes"]:
                sequence_numbers.append(
                    {
                        "sequence": 20,
                        "type": "permit",
                        "match": ["ip address prefix-list PL-STATIC-VRF-DEFAULT"],
                    },
                )

        if not sequence_numbers:
            return None

        return {"name": "RM-EVPN-EXPORT-VRF-DEFAULT", "sequence_numbers": sequence_numbers}

    def _bgp_underlay_peers_route_map(self) -> dict | None:
        """
        For non WAN routers filter EVPN routes away from underlay.

        For WAN routers the underlay towards LAN side also permits the tenant routes for VRF default,
        so routes should not be filtered.
        """
        sequence_numbers = []

        if self.shared_utils.is_wan_router:
            return None

        if self._vrf_default_ipv4_subnets:
            sequence_numbers.append(
                {
                    "sequence": 10,
                    "type": "deny",
                    "match": ["ip address prefix-list PL-SVI-VRF-DEFAULT"],
                },
            )

        if self._vrf_default_ipv4_static_routes["static_routes"]:
            sequence_numbers.append(
                {
                    "sequence": 15,
                    "type": "deny",
                    "match": ["ip address prefix-list PL-STATIC-VRF-DEFAULT"],
                },
            )

        if not sequence_numbers:
            return None

        sequence_numbers.append(
            {
                "sequence": 20,
                "type": "permit",
            },
        )

        return {"name": "RM-BGP-UNDERLAY-PEERS-OUT", "sequence_numbers": sequence_numbers}

    def _redistribute_connected_to_bgp_route_map(self) -> dict | None:
        """
        Append network services relevant entries to the route-map used to redistribute connected subnets in BGP.

        sequence 10 is set in underlay and sequence 20 in inband management, so avoid setting those here
        """
        if not self.inputs.underlay_filter_redistribute_connected:
            return None

        sequence_numbers = []

        if self._vrf_default_ipv4_subnets:
            # Add subnets to redistribution in default VRF
            sequence_30 = {
                "sequence": 30,
                "type": "permit",
                "match": ["ip address prefix-list PL-SVI-VRF-DEFAULT"],
            }
            if self.shared_utils.wan_role:
                sequence_30["set"] = [f"extcommunity soo {self.shared_utils.evpn_soo} additive"]

            sequence_numbers.append(sequence_30)

        if not sequence_numbers:
            return None

        return {"name": "RM-CONN-2-BGP", "sequence_numbers": sequence_numbers}

    def _redistribute_static_to_bgp_route_map(self) -> dict | None:
        """Append network services relevant entries to the route-map used to redistribute static routes to BGP."""
        if not (self.shared_utils.wan_role and self._vrf_default_ipv4_static_routes["redistribute_in_overlay"]):
            return None

        return {
            "name": "RM-STATIC-2-BGP",
            "sequence_numbers": [
                {
                    "sequence": 10,
                    "type": "permit",
                    "match": ["ip address prefix-list PL-STATIC-VRF-DEFAULT"],
                    "set": [f"extcommunity soo {self.shared_utils.evpn_soo} additive"],
                },
            ],
        }

    @cached_property
    def _router_bgp_vrfs(self) -> dict:
        """
        Return partial structured config for router_bgp.

        Covers these areas:
        - vrfs for all VRFs.
        - neighbors and address_family_ipv4/6 for VRF default.
        """
        if not self.shared_utils.network_services_l3:
            return {}

        router_bgp = {"vrfs": []}

        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                if not self.shared_utils.bgp_enabled_for_vrf(vrf):
                    continue

                vrf_name = vrf.name
                bgp_vrf = strip_empties_from_dict(
                    {
                        "eos_cli": vrf.bgp.raw_eos_cli,
                    }
                )

                if vrf.bgp.structured_config:
                    self.custom_structured_configs.nested.router_bgp.vrfs.obtain(vrf_name)._deepmerge(
                        vrf.bgp.structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
                    )

                if vrf_address_families := [af for af in vrf.address_families if af in self.shared_utils.overlay_address_families]:
                    # The called function in-place updates the bgp_vrf dict.
                    self._update_router_bgp_vrf_evpn_or_mpls_cfg(bgp_vrf, vrf, vrf_address_families)

                if vrf_name != "default":
                    bgp_vrf["router_id"] = self.get_vrf_router_id(vrf, vrf.bgp.router_id, tenant.name)

                    if vrf.redistribute_connected:
                        bgp_vrf["redistribute"] = {"connected": {"enabled": True}}
                    # Redistribution of static routes for VRF default are handled elsewhere
                    # since there is a choice between redistributing to underlay or overlay.
                    if vrf.redistribute_static or (vrf.static_routes and vrf.redistribute_static is None):
                        bgp_vrf["redistribute"].update({"static": {"enabled": True}})

                    if self.shared_utils.inband_mgmt_vrf == vrf_name and self.shared_utils.inband_management_parent_vlans:
                        bgp_vrf["redistribute"].update({"attached_host": {"enabled": True}})

                else:
                    # VRF default
                    if bgp_vrf:
                        # RD/RT and/or eos_cli/struct_cfg which should go under the vrf default context.
                        # Any peers added later will be put directly under router_bgp
                        append_if_not_duplicate(
                            list_of_dicts=router_bgp["vrfs"],
                            primary_key="name",
                            new_dict={"name": vrf_name, **bgp_vrf},
                            context="BGP VRFs defined under network services",
                            context_keys=["name"],
                        )
                        # Resetting bgp_vrf so we only add global keys if there are any neighbors for VRF default
                        bgp_vrf = {}

                    if self.shared_utils.underlay_routing_protocol == "none":
                        # We need to add redistribute connected for the default VRF when underlay_routing_protocol is "none"
                        bgp_vrf["redistribute"] = {"connected": {"enabled": True}}

                # MLAG IBGP Peering VLANs per VRF
                # Will only be configured for VRF default if underlay_routing_protocol == "none".
                if (vlan_id := self._mlag_ibgp_peering_vlan_vrf(vrf, tenant)) is not None:
                    self._update_router_bgp_vrf_mlag_neighbor_cfg(bgp_vrf, vrf, tenant, vlan_id)

                for bgp_peer in vrf.bgp_peers:
                    # Below we pop various keys that are not supported by the eos_cli_config_gen schema.
                    # The rest of the keys are relayed directly to eos_cli_config_gen.
                    # 'ip_address' is popped even though it is supported. It will be added again later
                    # to ensure it comes first in the generated dict.
                    bgp_peer_dict = bgp_peer._as_dict()
                    peer_ip = bgp_peer_dict.pop("ip_address")
                    address_family = f"address_family_ipv{ipaddress.ip_address(peer_ip).version}"
                    neighbor = strip_empties_from_dict(
                        {
                            "ip_address": peer_ip,
                            "activate": True,
                            "prefix_list_in": bgp_peer_dict.pop("prefix_list_in", None),
                            "prefix_list_out": bgp_peer_dict.pop("prefix_list_out", None),
                        },
                    )

                    append_if_not_duplicate(
                        list_of_dicts=bgp_vrf.setdefault(address_family, {}).setdefault("neighbors", []),
                        primary_key="ip_address",
                        new_dict=neighbor,
                        context="BGP peer defined under VRFs",
                        context_keys=["ip_address"],
                    )

                    if bgp_peer.set_ipv4_next_hop or bgp_peer.set_ipv6_next_hop:
                        route_map = f"RM-{vrf_name}-{peer_ip}-SET-NEXT-HOP-OUT"
                        bgp_peer_dict["route_map_out"] = route_map
                        if bgp_peer_dict.get("default_originate") is not None:
                            bgp_peer_dict["default_originate"].setdefault("route_map", route_map)

                        bgp_peer_dict.pop("set_ipv4_next_hop", None)
                        bgp_peer_dict.pop("set_ipv6_next_hop", None)

                    bgp_peer_dict.pop("nodes", None)

                    append_if_not_duplicate(
                        list_of_dicts=bgp_vrf.setdefault("neighbors", []),
                        primary_key="ip_address",
                        new_dict={"ip_address": peer_ip, **bgp_peer_dict},
                        context="BGP peer defined under VRFs",
                        context_keys=["ip_address"],
                    )

                if vrf.ospf.enabled and vrf.redistribute_ospf and (not vrf.ospf.nodes or self.shared_utils.hostname in vrf.ospf.nodes):
                    bgp_vrf.setdefault("redistribute", {}).update({"ospf": {"enabled": True}})

                if (
                    bgp_vrf.get("neighbors")
                    and self.inputs.bgp_update_wait_install
                    and self.shared_utils.platform_settings.feature_support.bgp_update_wait_install
                ):
                    bgp_vrf.setdefault("updates", {})["wait_install"] = True

                bgp_vrf = strip_empties_from_dict(bgp_vrf)

                # Skip adding the VRF if we have no config.
                if not bgp_vrf:
                    continue

                if vrf_name == "default":
                    # VRF default is added directly under router_bgp
                    router_bgp.update(bgp_vrf)
                else:
                    append_if_not_duplicate(
                        list_of_dicts=router_bgp["vrfs"],
                        primary_key="name",
                        new_dict={"name": vrf_name, **bgp_vrf},
                        context="BGP VRFs defined under network services",
                        context_keys=["name"],
                    )
        return strip_empties_from_dict(router_bgp)

    def _update_router_bgp_vrf_evpn_or_mpls_cfg(
        self,
        bgp_vrf: dict,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
        vrf_address_families: list[str],
    ) -> None:
        """In-place update EVPN/MPLS part of structured config for *one* VRF under router_bgp.vrfs."""
        vrf_name = vrf.name
        bgp_vrf["rd"] = self.get_vrf_rd(vrf)
        vrf_rt = self.get_vrf_rt(vrf)
        route_targets = {"import": [], "export": []}

        for af in vrf_address_families:
            if (target := get_item(route_targets["import"], "address_family", af)) is None:
                route_targets["import"].append({"address_family": af, "route_targets": [vrf_rt]})
            else:
                target["route_targets"].append(vrf_rt)

            if (target := get_item(route_targets["export"], "address_family", af)) is None:
                route_targets["export"].append({"address_family": af, "route_targets": [vrf_rt]})
            else:
                target["route_targets"].append(vrf_rt)

        for rt in vrf.additional_route_targets:
            if rt.type is None:
                continue
            if (target := get_item(route_targets[rt.type], "address_family", rt.address_family)) is None:
                route_targets[rt.type].append({"address_family": rt.address_family, "route_targets": [rt.route_target]})
            else:
                target["route_targets"].append(rt.route_target)

        if vrf_name == "default" and self._vrf_default_evpn and self._route_maps_vrf_default:
            # Special handling of vrf default with evpn.

            if (target := get_item(route_targets["export"], "address_family", "evpn")) is None:
                route_targets["export"].append({"address_family": "evpn", "route_targets": ["route-map RM-EVPN-EXPORT-VRF-DEFAULT"]})
            else:
                target.setdefault("route_targets", []).append("route-map RM-EVPN-EXPORT-VRF-DEFAULT")

        bgp_vrf["route_targets"] = route_targets

        # VRF default
        if vrf_name == "default":
            return

        # Not VRF default
        bgp_vrf["evpn_multicast"] = getattr(vrf, "_evpn_l3_multicast_enabled", None)
        if evpn_multicast_transit_mode := getattr(vrf, "_evpn_l3_multicast_evpn_peg_transit", False):
            bgp_vrf["evpn_multicast_address_family"] = {"ipv4": {"transit": evpn_multicast_transit_mode}}

    def _update_router_bgp_vrf_mlag_neighbor_cfg(
        self,
        bgp_vrf: dict,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
        vlan_id: int,
    ) -> None:
        """In-place update MLAG neighbor part of structured config for *one* VRF under router_bgp.vrfs."""
        if self._exclude_mlag_ibgp_peering_from_redistribute(vrf, tenant):
            bgp_vrf["redistribute"]["connected"] = {"enabled": True, "route_map": "RM-CONN-2-BGP-VRFS"}

        interface_name = f"Vlan{vlan_id}"
        if self.inputs.underlay_rfc5549 and self.inputs.overlay_mlag_rfc5549:
            bgp_vrf.setdefault("neighbor_interfaces", []).append(
                {
                    "name": interface_name,
                    "peer_group": self.inputs.bgp_peer_groups.mlag_ipv4_underlay_peer.name,
                    "remote_as": self.shared_utils.bgp_as,
                    "description": AvdStringFormatter().format(
                        self.inputs.mlag_bgp_peer_description,
                        mlag_peer=self.shared_utils.mlag_peer,
                        interface=interface_name,
                        peer_interface=interface_name,
                    ),
                },
            )
        else:
            if not vrf.mlag_ibgp_peering_ipv4_pool:
                ip_address = self.shared_utils.mlag_peer_ibgp_ip
            elif self.shared_utils.mlag_role == "primary":
                ip_address = self.shared_utils.ip_addressing.mlag_ibgp_peering_ip_secondary(vrf.mlag_ibgp_peering_ipv4_pool)
            else:
                ip_address = self.shared_utils.ip_addressing.mlag_ibgp_peering_ip_primary(vrf.mlag_ibgp_peering_ipv4_pool)

            bgp_vrf.setdefault("neighbors", []).append(
                {
                    "ip_address": ip_address,
                    "peer_group": self.inputs.bgp_peer_groups.mlag_ipv4_underlay_peer.name,
                    "description": AvdStringFormatter().format(
                        self.inputs.mlag_bgp_peer_description,
                        **strip_empties_from_dict(
                            {"mlag_peer": self.shared_utils.mlag_peer, "interface": interface_name, "peer_interface": interface_name, "vrf": vrf.name}
                        ),
                    ),
                },
            )
            if self.inputs.underlay_rfc5549:
                bgp_vrf.setdefault("address_family_ipv4", {}).setdefault("neighbors", []).append(
                    {
                        "ip_address": ip_address,
                        "next_hop": {
                            "address_family_ipv6": {"enabled": False},
                        },
                    },
                )

    def _get_vlan_ip_config_for_mlag_peering(self, vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem) -> dict:
        """
        Build IP config for MLAG peering SVI for the given VRF.

        Called from _get_vlan_interface_config_for_mlag_peering and prefix_lists.
        """
        if self.inputs.underlay_rfc5549 and self.inputs.overlay_mlag_rfc5549:
            return {"ipv6_enable": True}

        if vrf.mlag_ibgp_peering_ipv4_pool:
            if self.shared_utils.mlag_role == "primary":
                return {
                    "ip_address": (
                        f"{self.shared_utils.ip_addressing.mlag_ibgp_peering_ip_primary(vrf.mlag_ibgp_peering_ipv4_pool)}/"
                        f"{self.inputs.fabric_ip_addressing.mlag.ipv4_prefix_length}"
                    )
                }

            return {
                "ip_address": (
                    f"{self.shared_utils.ip_addressing.mlag_ibgp_peering_ip_secondary(vrf.mlag_ibgp_peering_ipv4_pool)}/"
                    f"{self.inputs.fabric_ip_addressing.mlag.ipv4_prefix_length}"
                )
            }

        return {"ip_address": f"{self.shared_utils.mlag_ibgp_ip}/{self.inputs.fabric_ip_addressing.mlag.ipv4_prefix_length}"}

    @cached_property
    def _mlag_ibgp_peering_subnets_without_redistribution(self) -> list:
        """Return sorted list of MLAG peerings for VRFs where MLAG iBGP peering should not be redistributed."""
        mlag_prefixes = set()
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                if self._mlag_ibgp_peering_vlan_vrf(vrf, tenant) is None:
                    continue

                if not self._exclude_mlag_ibgp_peering_from_redistribute(vrf, tenant):
                    # By default the BGP peering is redistributed, so we only need the prefix-list for the false case.
                    continue

                if (mlag_ip_address := self._get_vlan_ip_config_for_mlag_peering(vrf).get("ip_address")) is None:
                    # No MLAG prefix for this VRF (could be RFC5549)
                    continue

                # Convert mlag_ip_address to network prefix string and add to set.
                mlag_prefixes.add(str(ipaddress.IPv4Network(mlag_ip_address, strict=False)))

        return natural_sort(mlag_prefixes)
