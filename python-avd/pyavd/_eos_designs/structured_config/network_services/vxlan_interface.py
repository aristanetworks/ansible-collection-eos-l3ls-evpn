# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, NoReturn

from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError
from pyavd._utils import append_if_not_duplicate, default, get, get_item, unique
from pyavd.j2filters import natural_sort, range_expand

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class VxlanInterfaceMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def vxlan_interface(self: AvdStructuredConfigNetworkServices) -> dict | None:
        """
        Returns structured config for vxlan_interface.

        Only used for VTEPs and for WAN

        This function also detects duplicate VNIs and raise an error in case of duplicates between
        all Network Services deployed on this device.
        """
        if not (self.shared_utils.overlay_vtep or self.shared_utils.is_wan_router):
            return None

        vxlan = {
            "udp_port": 4789,
        }

        if self._multi_vtep:
            vxlan["source_interface"] = "Loopback0"
            vxlan["mlag_source_interface"] = self.shared_utils.vtep_loopback
        else:
            vxlan["source_interface"] = self.shared_utils.vtep_loopback

        if self.shared_utils.mlag_l3 and self.shared_utils.network_services_l3 and self.shared_utils.overlay_evpn:
            vxlan["virtual_router_encapsulation_mac_address"] = "mlag-system-id"

        if self.shared_utils.overlay_her and self._overlay_her_flood_list_per_vni is False and (common := self._overlay_her_flood_lists.get("common")):
            vxlan["flood_vteps"] = natural_sort(unique(common))

        if self.shared_utils.overlay_cvx:
            vxlan["controller_client"] = {"enabled": True}

        vlans = []
        vrfs = []
        # vnis is a list of dicts only used for duplication checks across multiple types of objects all having "vni" as a key.
        vnis = []

        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant["vrfs"]:
                self._get_vxlan_interface_config_for_vrf(vrf, tenant, vrfs, vlans, vnis)

            if not self.shared_utils.network_services_l2:
                continue

            for l2vlan in tenant["l2vlans"]:
                if vlan := self._get_vxlan_interface_config_for_vlan(l2vlan, tenant):
                    # Duplicate check is not done on the actual list of vlans, but instead on our local "vnis" list.
                    # This is necessary to find duplicate VNIs across multiple object types.
                    append_if_not_duplicate(
                        list_of_dicts=vnis,
                        primary_key="vni",
                        new_dict=vlan,
                        context="VXLAN VNIs for L2VLANs",
                        context_keys=["id", "name", "vni"],
                    )
                    # Here we append to the actual list of VRFs, so duplication check is on the VLAN ID here.
                    append_if_not_duplicate(
                        list_of_dicts=vlans,
                        primary_key="id",
                        new_dict=vlan,
                        context="VXLAN VNIs for L2VLANs",
                        context_keys=["id", "vni"],
                    )

        if self.shared_utils.is_wan_server:
            # loop through wan_vrfs and add VRF VNI if not present
            for vrf in self._filtered_wan_vrfs:
                # Duplicate check is not done on the actual list of vlans, but instead on our local "vnis" list.
                # This is necessary to find duplicate VNIs across multiple object types.
                vrf_data = {"name": vrf["name"], "vni": vrf["wan_vni"]}
                append_if_not_duplicate(
                    list_of_dicts=vnis,
                    primary_key="vni",
                    new_dict=vrf_data,
                    context="VXLAN VNIs for VRFs",
                    context_keys=["id", "name", "vni"],
                )
                # Here we append to the actual list of VRFs, so duplication check is on the VRF here.
                append_if_not_duplicate(
                    list_of_dicts=vrfs,
                    primary_key="name",
                    new_dict=vrf_data,
                    context="VXLAN VNIs for VRFs",
                    context_keys=["name", "vni"],
                )

        if vlans:
            vxlan["vlans"] = vlans

        if vrfs:
            vxlan["vrfs"] = vrfs

        return {
            "vxlan1": {
                "description": f"{self.shared_utils.hostname}_VTEP",
                "vxlan": vxlan,
            },
        }

    def _get_vxlan_interface_config_for_vrf(self: AvdStructuredConfigNetworkServices, vrf: dict, tenant: dict, vrfs: list, vlans: list, vnis: list) -> None:
        """In place updates of the vlans, vnis and vrfs list."""
        if self.shared_utils.network_services_l2:
            for svi in vrf["svis"]:
                if vlan := self._get_vxlan_interface_config_for_vlan(svi, tenant):
                    # Duplicate check is not done on the actual list of vlans, but instead on our local "vnis" list.
                    # This is necessary to find duplicate VNIs across multiple object types.
                    append_if_not_duplicate(
                        list_of_dicts=vnis,
                        primary_key="vni",
                        new_dict=vlan,
                        context="VXLAN VNIs for SVIs",
                        context_keys=["id", "name", "vni"],
                    )
                    # Here we append to the actual list of VRFs, so duplication check is on the VLAN ID here.
                    append_if_not_duplicate(
                        list_of_dicts=vlans,
                        primary_key="id",
                        new_dict=vlan,
                        context="VXLAN VNIs for SVIs",
                        context_keys=["id", "vni"],
                    )

        if self.shared_utils.network_services_l3 and self.shared_utils.overlay_evpn_vxlan:
            vrf_name = vrf["name"]

            # Only configure VNI for VRF if the VRF is EVPN enabled
            if "evpn" not in vrf.get("address_families", ["evpn"]):
                return

            if self.shared_utils.is_wan_router:
                # Every VRF with EVPN on a WAN router must have a wan_vni defined.
                error_message = (
                    f"The VRF '{vrf_name}' does not have a `wan_vni` defined under 'wan_virtual_topologies'. "
                    "If this VRF was not intended to be extended over the WAN, but still required to be configured on the WAN router, "
                    "set 'address_families: []' under the VRF definition. If this VRF was not intended to be configured on the WAN router, "
                    "use the VRF filter 'deny_vrfs' under the node settings."
                )
                wan_vrf = get_item(self._filtered_wan_vrfs, "name", vrf_name, required=True, custom_error_msg=error_message)
                vni = get(wan_vrf, "wan_vni", required=True, custom_error_msg=error_message)
            else:
                vni = default(
                    vrf.get("vrf_vni"),
                    vrf.get("vrf_id"),
                )

            # NOTE: this can never be None here, it would be caught previously in the code
            vrf_id = default(
                vrf.get("vrf_id"),
                vrf.get("vrf_vni"),
            )
            if vni is not None:
                # Silently ignore if we cannot set a VNI
                # This is legacy behavior so we will leave stricter enforcement to the schema
                vrf_data = {"name": vrf_name, "vni": vni}

                if get(vrf, "_evpn_l3_multicast_enabled"):
                    if vrf_multicast_group := get(vrf, "_evpn_l3_multicast_group_ip"):
                        vrf_data["multicast_group"] = vrf_multicast_group
                    else:
                        underlay_l3_multicast_group_ipv4_pool = get(
                            tenant,
                            "evpn_l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool",
                            required=True,
                            custom_error_msg=f"'evpn_l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool' for Tenant: {tenant['name']} is required.",
                        )
                        underlay_l3_mcast_group_ipv4_pool_offset = get(tenant, "evpn_l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool_offset", default=0)
                        vrf_data["multicast_group"] = self.shared_utils.ip_addressing.evpn_underlay_l3_multicast_group(
                            underlay_l3_multicast_group_ipv4_pool,
                            vni,
                            vrf_id,
                            underlay_l3_mcast_group_ipv4_pool_offset,
                        )

                # Duplicate check is not done on the actual list of vlans, but instead on our local "vnis" list.
                # This is necessary to find duplicate VNIs across multiple object types.
                append_if_not_duplicate(
                    list_of_dicts=vnis,
                    primary_key="vni",
                    new_dict=vrf_data,
                    context="VXLAN VNIs for VRFs",
                    context_keys=["id", "name", "vni"],
                )
                # Here we append to the actual list of VRFs, so duplication check is on the VRF here.
                append_if_not_duplicate(
                    list_of_dicts=vrfs,
                    primary_key="name",
                    new_dict=vrf_data,
                    context="VXLAN VNIs for VRFs",
                    context_keys=["name", "vni"],
                )

    def _get_vxlan_interface_config_for_vlan(self: AvdStructuredConfigNetworkServices, vlan: dict, tenant: dict) -> dict:
        """
        vxlan_interface logic for one vlan.

        Can be used for both svis and l2vlans
        """
        if vlan.get("vxlan") is False:
            return {}

        vlan_id = int(vlan["id"])
        vxlan_interface_vlan = {"id": vlan_id}
        if (vni_override := vlan.get("vni_override")) is not None:
            vxlan_interface_vlan["vni"] = int(vni_override)
        else:
            mac_vrf_vni_base = int(
                get(tenant, "mac_vrf_vni_base", required=True, custom_error_msg=f"'mac_vrf_vni_base' for Tenant: {tenant['name']} is required.")
            )
            vxlan_interface_vlan["vni"] = mac_vrf_vni_base + vlan_id

        vlan_evpn_l2_multicast_enabled = (
            default(get(vlan, "evpn_l2_multicast.enabled"), get(tenant, "evpn_l2_multicast.enabled")) and self.shared_utils.evpn_multicast is True
        )
        if vlan_evpn_l2_multicast_enabled is True:
            underlay_l2_multicast_group_ipv4_pool = get(
                tenant,
                "evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool",
                required=True,
                custom_error_msg=f"'evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool' for Tenant: {tenant['name']} is required.",
            )
            underlay_l2_multicast_group_ipv4_pool_offset = get(tenant, "evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool_offset", default=0)
            vxlan_interface_vlan["multicast_group"] = self.shared_utils.ip_addressing.evpn_underlay_l2_multicast_group(
                underlay_l2_multicast_group_ipv4_pool,
                vlan_id,
                underlay_l2_multicast_group_ipv4_pool_offset,
            )

        if self.shared_utils.overlay_her and self._overlay_her_flood_list_per_vni and (vlan_id_entry := self._overlay_her_flood_lists.get(vlan_id)):
            vxlan_interface_vlan["flood_vteps"] = natural_sort(unique(vlan_id_entry))

        return vxlan_interface_vlan

    @cached_property
    def _overlay_her_flood_list_per_vni(self: AvdStructuredConfigNetworkServices) -> bool:
        return get(self._hostvars, "overlay_her_flood_list_per_vni") is True

    @cached_property
    def _overlay_her_flood_lists(self: AvdStructuredConfigNetworkServices) -> dict[list]:
        """
        Returns a dict with HER Flood Lists.

        Only used when overlay_route_protocol == 'HER'

        If "overlay_her_flood_list_per_vni" is True:
        - return {<vlan>: [<peer_vtep>, <peer_vtep>, ...], ...}
        Else
        - return {common: [<peer_vtep>, <peer_vtep> ...]}

        Uses "overlay_her_flood_list_scope" to find the peer switches
        If overlay_her_flood_list_scope == "dc"
          - dc_name *must* be set.
          - Otherwise an error will be raised
        """
        overlay_her_flood_lists = {}
        overlay_her_flood_list_scope = get(self._hostvars, "overlay_her_flood_list_scope")

        if overlay_her_flood_list_scope == "dc" and self.shared_utils.dc_name is None:
            msg = "'dc_name' is required with 'overlay_her_flood_list_scope: dc'"
            raise AristaAvdInvalidInputsError(msg)

        for peer in self.shared_utils.all_fabric_devices:
            if peer == self.shared_utils.hostname:
                continue

            peer_facts = self.shared_utils.get_peer_facts(peer, required=True)

            if overlay_her_flood_list_scope == "dc" and peer_facts.get("dc_name") != self.shared_utils.dc_name:
                continue

            if (vtep_ip := peer_facts.get("vtep_ip")) is None:
                continue

            if not self._overlay_her_flood_list_per_vni:
                # Use common flood list
                overlay_her_flood_lists.setdefault("common", []).append(vtep_ip)
                continue

            # Use flood lists per vlan
            peer_vlans = peer_facts.get("vlans", [])
            peer_vlans_list = range_expand(peer_vlans)
            for vlan in peer_vlans_list:
                overlay_her_flood_lists.setdefault(int(vlan), []).append(vtep_ip)

        return overlay_her_flood_lists

    def _raise_duplicate_vni_error(self: AvdStructuredConfigNetworkServices, vni: int, context: str, tenant: str, duplicate_vni_tenant: str) -> NoReturn:
        msg = f"Duplicate VXLAN VNI '{vni}' found in Tenant(s) '{tenant}' during configuration of {context}."
        if duplicate_vni_tenant != tenant:
            msg = f"{msg} Other VNI is in Tenant(s) '{duplicate_vni_tenant}'."

        raise AristaAvdError(msg)

    @cached_property
    def _multi_vtep(self: AvdStructuredConfigNetworkServices) -> bool:
        return self.shared_utils.mlag is True and self.shared_utils.evpn_multicast is True
