# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import append_if_not_duplicate, default, unique
from pyavd.j2filters import natural_sort, range_expand

from .utils import UtilsMixin

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

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

        if self.shared_utils.overlay_her and not self.inputs.overlay_her_flood_list_per_vni and (common := self._overlay_her_flood_lists.get("common")):
            vxlan["flood_vteps"] = natural_sort(unique(common))

        if self.shared_utils.overlay_cvx:
            vxlan["controller_client"] = {"enabled": True}

        vlans: list[dict] = []
        vrfs: list[dict] = []
        # vnis is a list of dicts only used for duplication checks across multiple types of objects all having "vni" as a key.
        vnis: list[dict] = []

        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                self._get_vxlan_interface_config_for_vrf(vrf, tenant, vrfs, vlans, vnis)

            if not self.shared_utils.network_services_l2:
                continue

            for l2vlan in tenant.l2vlans:
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
                vrf_data = {"name": vrf.name, "vni": vrf.wan_vni}
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

    def _get_vxlan_interface_config_for_vrf(
        self: AvdStructuredConfigNetworkServices,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
        vrfs: list[dict],
        vlans: list[dict],
        vnis: list[dict],
    ) -> None:
        """In place updates of the vlans, vnis and vrfs list."""
        if self.shared_utils.network_services_l2:
            for svi in vrf.svis:
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

        if self.shared_utils.network_services_l3 and (self.shared_utils.overlay_evpn_vxlan or self.shared_utils.is_wan_router):
            vrf_name = vrf.name

            # Only configure VNI for VRF if the VRF is EVPN enabled
            if "evpn" not in vrf.address_families:
                return

            if self.shared_utils.is_wan_router:
                # Every VRF with EVPN on a WAN router must have a wan_vni defined.
                if vrf_name not in self._filtered_wan_vrfs:
                    msg = (
                        f"The VRF '{vrf_name}' does not have a `wan_vni` defined under 'wan_virtual_topologies'. "
                        "If this VRF was not intended to be extended over the WAN, but still required to be configured on the WAN router, "
                        "set 'address_families: []' under the VRF definition. If this VRF was not intended to be configured on the WAN router, "
                        "use the VRF filter 'deny_vrfs' under the node settings."
                    )
                    raise AristaAvdInvalidInputsError(msg)
                vni = self._filtered_wan_vrfs[vrf_name].wan_vni
            else:
                vni = default(vrf.vrf_vni, vrf.vrf_id)

            if vni is None:
                # Silently ignore if we cannot set a VNI
                # This is legacy behavior so we will leave stricter enforcement to the schema
                return

            # NOTE: this can never be None here, it would be caught previously in the code
            vrf_id: int = default(vrf.vrf_id, vrf.vrf_vni)

            vrf_data = {"name": vrf_name, "vni": vni}

            if getattr(vrf, "_evpn_l3_multicast_enabled", False):
                if vrf_multicast_group := getattr(vrf, "_evpn_l3_multicast_group_ip", None):
                    vrf_data["multicast_group"] = vrf_multicast_group
                else:
                    if not tenant.evpn_l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool:
                        msg = f"'evpn_l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool' for Tenant: {tenant.name} is required."
                        raise AristaAvdInvalidInputsError(msg)

                    vrf_data["multicast_group"] = self.shared_utils.ip_addressing.evpn_underlay_l3_multicast_group(
                        tenant.evpn_l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool,
                        vni,
                        vrf_id,
                        tenant.evpn_l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool_offset,
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

    def _get_vxlan_interface_config_for_vlan(
        self: AvdStructuredConfigNetworkServices,
        vlan: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem
        | EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlansItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
    ) -> dict:
        """
        vxlan_interface logic for one vlan.

        Can be used for both svis and l2vlans
        """
        if not vlan.vxlan:
            return {}

        vxlan_interface_vlan = {"id": vlan.id}
        if vlan.vni_override:
            vxlan_interface_vlan["vni"] = vlan.vni_override
        else:
            if tenant.mac_vrf_vni_base is None:
                msg = f"'mac_vrf_vni_base' for Tenant: {tenant.name} is required."
                raise AristaAvdInvalidInputsError(msg)
            vxlan_interface_vlan["vni"] = tenant.mac_vrf_vni_base + vlan.id

        vlan_evpn_l2_multicast_enabled = bool(default(vlan.evpn_l2_multicast.enabled, tenant.evpn_l2_multicast.enabled)) and self.shared_utils.evpn_multicast
        if vlan_evpn_l2_multicast_enabled is True:
            if not tenant.evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool:
                msg = f"'evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool' for Tenant: {tenant.name} is required."
                raise AristaAvdInvalidInputsError(msg)

            vxlan_interface_vlan["multicast_group"] = self.shared_utils.ip_addressing.evpn_underlay_l2_multicast_group(
                tenant.evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool,
                vlan.id,
                tenant.evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool_offset,
            )

        if self.shared_utils.overlay_her and self.inputs.overlay_her_flood_list_per_vni and (vlan_id_entry := self._overlay_her_flood_lists.get(vlan.id)):
            vxlan_interface_vlan["flood_vteps"] = natural_sort(unique(vlan_id_entry))

        return vxlan_interface_vlan

    @cached_property
    def _overlay_her_flood_lists(self: AvdStructuredConfigNetworkServices) -> dict[str | int, list]:
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
        overlay_her_flood_list_scope = self.inputs.overlay_her_flood_list_scope

        if overlay_her_flood_list_scope == "dc" and self.inputs.dc_name is None:
            msg = "'dc_name' is required with 'overlay_her_flood_list_scope: dc'"
            raise AristaAvdInvalidInputsError(msg)

        for peer in self.shared_utils.all_fabric_devices:
            if peer == self.shared_utils.hostname:
                continue

            peer_facts = self.shared_utils.get_peer_facts(peer, required=True)

            if overlay_her_flood_list_scope == "dc" and peer_facts.get("dc_name") != self.inputs.dc_name:
                continue

            if (vtep_ip := peer_facts.get("vtep_ip")) is None:
                continue

            if not self.inputs.overlay_her_flood_list_per_vni:
                # Use common flood list
                overlay_her_flood_lists.setdefault("common", []).append(vtep_ip)
                continue

            # Use flood lists per vlan
            peer_vlans = peer_facts.get("vlans", [])
            peer_vlans_list = range_expand(peer_vlans)
            for vlan in peer_vlans_list:
                overlay_her_flood_lists.setdefault(int(vlan), []).append(vtep_ip)

        return overlay_her_flood_lists

    @cached_property
    def _multi_vtep(self: AvdStructuredConfigNetworkServices) -> bool:
        return self.shared_utils.mlag is True and self.shared_utils.evpn_multicast is True
