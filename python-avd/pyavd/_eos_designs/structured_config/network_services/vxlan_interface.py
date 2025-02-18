# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field
from functools import cached_property
from typing import TYPE_CHECKING, Literal, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.schema import EosDesigns
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import default, unique
from pyavd.j2filters import natural_sort, range_expand

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


@dataclass(frozen=True, order=True)
class VniContext:
    vni: int
    """The VNI."""
    source_type: Literal["L2VLAN", "VRF", "SVI"] = field(compare=False)
    """The source type of the VNI."""
    name: str
    """The VRF name or the VLAN ID as a string."""
    tenant: str = field(compare=False)
    """The tenant name."""
    real_type: Literal["VLAN", "VRF"] = field(init=False)

    def __post_init__(self) -> None:
        """
        Setting real_type to VLAN or VRF based on the source type.

        The field is used in comparison to detect duplicates.
        """
        real_type = "VLAN" if self.source_type in ["L2VLAN", "SVI"] else "VRF"
        object.__setattr__(self, "real_type", real_type)

    def __repr__(self) -> str:
        return f"{self.source_type} {self.name} in tenant {self.tenant}"


class VxlanInterfaceMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def _multi_vtep(self: AvdStructuredConfigNetworkServicesProtocol) -> bool:
        return self.shared_utils.mlag is True and self.shared_utils.evpn_multicast is True

    @structured_config_contributor
    def vxlan_interface(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Set structured config for vxlan_interface.

        Only used for VTEPs and for WAN

        This function also detects duplicate VNIs and raise an error in case of duplicates between
        all Network Services deployed on this device.
        """
        if not (self.shared_utils.overlay_vtep or self.shared_utils.is_wan_router):
            return

        self.structured_config.vxlan_interface.vxlan1.description = f"{self.shared_utils.hostname}_VTEP"

        vxlan = self.structured_config.vxlan_interface.vxlan1.vxlan
        vxlan.udp_port = 4789

        if self._multi_vtep:
            vxlan.source_interface = "Loopback0"
            vxlan.mlag_source_interface = self.shared_utils.vtep_loopback
        else:
            vxlan.source_interface = self.shared_utils.vtep_loopback

        if self.shared_utils.mlag_l3 and self.shared_utils.network_services_l3 and self.shared_utils.overlay_evpn:
            vxlan.virtual_router_encapsulation_mac_address = "mlag-system-id"

        if self.shared_utils.overlay_her and not self.inputs.overlay_her_flood_list_per_vni and (common := self._overlay_her_flood_lists.get("common")):
            vxlan.flood_vteps.extend(natural_sort(unique(common)))

        if self.shared_utils.overlay_cvx:
            vxlan.controller_client.enabled = True

        # Keep track of the VNIs added to check for duplicates
        # The entries are {<vni>: (<type>, <name>, <tenant>)}
        vnis: dict[int, set[VniContext]] = defaultdict(set)
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                self._set_vxlan_interface_config_for_vrf(vrf, tenant, vnis)

            if not self.shared_utils.network_services_l2:
                continue

            for l2vlan in tenant.l2vlans:
                if l2vlan.vxlan:
                    self._set_vxlan_interface_config_for_vlan(l2vlan, tenant, vnis)

        if self.shared_utils.is_wan_server:
            # loop through wan_vrfs and add VRF VNI if not present
            for wan_vrf in self._filtered_wan_vrfs:
                vrf = vxlan.vrfs.append_new(name=wan_vrf.name, vni=wan_vrf.wan_vni)
                vnis[wan_vrf.wan_vni].add(VniContext(vni=wan_vrf.wan_vni, name=wan_vrf.name, tenant="", source_type="VRF"))

        self._check_for_duplicates(vnis)

    def _set_vxlan_interface_config_for_vrf(
        self: AvdStructuredConfigNetworkServicesProtocol,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
        vnis: dict[int, set[VniContext]],
    ) -> None:
        """
        Set one Vxlan1 VRF in structured_config and its associated SVI VLANs.

        the VRF is set only if the device has L3 services
        the SVI VLANs are set only if the device has L2 services
        """
        if self.shared_utils.network_services_l2:
            for svi in vrf.svis:
                if svi.vxlan:
                    self._set_vxlan_interface_config_for_vlan(svi, tenant, vnis)

        if self.shared_utils.network_services_l3 and self.shared_utils.overlay_evpn_vxlan:
            # Only configure VNI for VRF if the VRF is EVPN enabled
            if "evpn" not in vrf.address_families:
                return

            if self.shared_utils.is_wan_router:
                # Every VRF with EVPN on a WAN router must have a wan_vni defined.
                if vrf.name not in self._filtered_wan_vrfs:
                    msg = (
                        f"The VRF '{vrf.name}' does not have a `wan_vni` defined under 'wan_virtual_topologies'. "
                        "If this VRF was not intended to be extended over the WAN, but still required to be configured on the WAN router, "
                        "set 'address_families: []' under the VRF definition. If this VRF was not intended to be configured on the WAN router, "
                        "use the VRF filter 'deny_vrfs' under the node settings."
                    )
                    raise AristaAvdInvalidInputsError(msg)
                vni = self._filtered_wan_vrfs[vrf.name].wan_vni
            else:
                vni = default(vrf.vrf_vni, vrf.vrf_id)

            if vni is None:
                # Silently ignore if we cannot set a VNI
                # This is legacy behavior so we will leave stricter enforcement to the schema
                return

            # NOTE: this can never be None here, it would be caught previously in the code
            vrf_id: int = default(vrf.vrf_id, vrf.vrf_vni)

            vxlan_vrf = EosCliConfigGen.VxlanInterface.Vxlan1.Vxlan.VrfsItem(name=vrf.name, vni=vni)

            if getattr(vrf._internal_data, "evpn_l3_multicast_enabled", False):
                if vrf_multicast_group := getattr(vrf._internal_data, "evpn_l3_multicast_group_ip", None):
                    vxlan_vrf.multicast_group = vrf_multicast_group
                else:
                    if not tenant.evpn_l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool:
                        msg = f"'evpn_l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool' for Tenant: {tenant.name} is required."
                        raise AristaAvdInvalidInputsError(msg)

                    vxlan_vrf.multicast_group = self.shared_utils.ip_addressing.evpn_underlay_l3_multicast_group(
                        tenant.evpn_l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool,
                        vni,
                        vrf_id,
                        tenant.evpn_l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool_offset,
                    )

            self.structured_config.vxlan_interface.vxlan1.vxlan.vrfs.append(vxlan_vrf)
            vnis[vxlan_vrf.vni].add(VniContext(vni=vxlan_vrf.vni, name=vxlan_vrf.name, tenant=tenant.name, source_type="VRF"))

    def _set_vxlan_interface_config_for_vlan(
        self: AvdStructuredConfigNetworkServicesProtocol,
        vlan: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem
        | EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlansItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
        vnis: dict[int, set[VniContext]],
    ) -> None:
        """
        Set one Vxlan1 vlan in structured_config.

        Can be used for both svis and l2vlans
        """
        vxlan_vlan = EosCliConfigGen.VxlanInterface.Vxlan1.Vxlan.VlansItem(id=vlan.id)

        if vlan.vni_override:
            vxlan_vlan.vni = vlan.vni_override
        else:
            if tenant.mac_vrf_vni_base is None:
                msg = f"'mac_vrf_vni_base' for Tenant: {tenant.name} is required."
                raise AristaAvdInvalidInputsError(msg)
            vxlan_vlan.vni = tenant.mac_vrf_vni_base + vlan.id

        vlan_evpn_l2_multicast_enabled = bool(default(vlan.evpn_l2_multicast.enabled, tenant.evpn_l2_multicast.enabled)) and self.shared_utils.evpn_multicast
        if vlan_evpn_l2_multicast_enabled is True:
            if not tenant.evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool:
                msg = f"'evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool' for Tenant: {tenant.name} is required."
                raise AristaAvdInvalidInputsError(msg)

            vxlan_vlan.multicast_group = self.shared_utils.ip_addressing.evpn_underlay_l2_multicast_group(
                tenant.evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool,
                vlan.id,
                tenant.evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool_offset,
            )

        if self.shared_utils.overlay_her and self.inputs.overlay_her_flood_list_per_vni and (vlan_id_entry := self._overlay_her_flood_lists.get(vlan.id)):
            vxlan_vlan.flood_vteps.extend(natural_sort(unique(vlan_id_entry)))

        self.structured_config.vxlan_interface.vxlan1.vxlan.vlans.append(vxlan_vlan)
        vlan_type = "L2VLAN" if isinstance(vlan, EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlansItem) else "SVI"
        vnis[vxlan_vlan.vni].add(VniContext(vni=vxlan_vlan.vni, name=str(vxlan_vlan.id), tenant=tenant.name, source_type=vlan_type))

    @cached_property
    def _overlay_her_flood_lists(self: AvdStructuredConfigNetworkServicesProtocol) -> dict[str | int, list]:
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

    def _check_for_duplicates(
        self: AvdStructuredConfigNetworkServicesProtocol,
        vnis: dict[int, set[VniContext]],
    ) -> None:
        """Pass through the vnis dictionary and raise an exception for any duplicate found."""
        for vni, items in vnis.items():
            if len(items) > 1:
                msg = (
                    f"Found duplicate objects with conflicting data while generating configuration for VXLAN VNI {vni}. "
                    f"The following items are conflicting: {', '.join(f'{item}' for item in sorted(items))}."
                )
                raise AristaAvdInvalidInputsError(msg)
