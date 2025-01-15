# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError
from pyavd._utils import default, unique
from pyavd.j2filters import natural_sort, range_expand

if TYPE_CHECKING:
    from . import SharedUtils


class FilteredTenantsMixin:
    """
    Mixin Class providing a subset of SharedUtils.

    Class should only be used as Mixin to the SharedUtils class.
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def filtered_tenants(self: SharedUtils) -> EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServices:
        """
        Return sorted tenants list from all network_services_keys and filtered based on filter_tenants.

        Keys of Tenant data model will be converted to lists.
        All sub data models like vrfs and l2vlans are also converted and filtered.
        """
        if not self.any_network_services:
            return EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServices()

        filtered_tenants = EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServices()
        filter_tenants = self.node_config.filter.tenants
        for network_services_key in self.inputs._dynamic_keys.network_services:
            for original_tenant in network_services_key.value:
                if original_tenant.name not in filter_tenants and "all" not in filter_tenants:
                    continue
                tenant = original_tenant._deepcopy()
                tenant.l2vlans = self.filtered_l2vlans(tenant)
                tenant.vrfs = self.filtered_vrfs(tenant)
                filtered_tenants.append(tenant)

        no_vrf_default = all("default" not in tenant.vrfs for tenant in filtered_tenants)
        if self.is_wan_router and no_vrf_default:
            filtered_tenants.append(
                EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem(
                    name="WAN_DEFAULT",
                    vrfs=EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.Vrfs(
                        [
                            EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem(
                                name="default",
                                vrf_id=1,
                            )
                        ]
                    ),
                )
            )
        elif self.is_wan_router:
            # It is enough to check only the first occurrence of default VRF as some other piece of code
            # checks that if the VRF is in multiple tenants, the configuration is consistent.
            for tenant in filtered_tenants:
                if "default" not in tenant.vrfs:
                    continue
                if "evpn" not in tenant.vrfs["default"].address_families:
                    msg = "WAN configuration requires EVPN to be enabled for VRF 'default'. Got 'address_families: {vrf_default['address_families']}."
                    raise AristaAvdError(msg)
                if self.inputs.underlay_filter_peer_as:
                    msg = "WAN configuration is not compatible with 'underlay_filter_peer_as'"
                    raise AristaAvdError
                break

        return filtered_tenants._natural_sorted()

    def filtered_l2vlans(
        self: SharedUtils, tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem
    ) -> EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlans:
        """
        Return sorted and filtered l2vlan list from given tenant.

        Filtering based on l2vlan tags.
        """
        if not self.network_services_l2 or not tenant.l2vlans:
            EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlans()

        filtered_l2vlans = tenant.l2vlans._filtered(
            lambda l2vlan: self.is_accepted_vlan(l2vlan) and bool("all" in self.filter_tags or set(l2vlan.tags).intersection(self.filter_tags))
        )
        # Set tenant on all l2vlans TODO: avoid this.
        for l2vlan in filtered_l2vlans:
            l2vlan._tenant = tenant.name

        if tenant.evpn_vlan_bundle:
            for l2vlan in filtered_l2vlans:
                l2vlan.evpn_vlan_bundle = l2vlan.evpn_vlan_bundle or tenant.evpn_vlan_bundle

        return filtered_l2vlans._natural_sorted(sort_key="id")

    def is_accepted_vlan(
        self: SharedUtils,
        vlan: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlansItem
        | EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem,
    ) -> bool:
        """
        Check if vlan is in accepted_vlans list.

        If filter.only_vlans_in_use is True also check if vlan id or trunk group is assigned to connected endpoint.
        """
        if vlan.id not in self.accepted_vlans:
            return False

        if not self.node_config.filter.only_vlans_in_use:
            # No further filtering
            return True

        if vlan.id in self.endpoint_vlans:
            return True

        # Picking this up from facts so this would fail if accessed when shared_utils is run before facts
        # TODO: see if this can be optimized
        endpoint_trunk_groups = set(self.get_switch_fact("endpoint_trunk_groups", required=False) or [])
        return bool(self.inputs.enable_trunk_groups and vlan.trunk_groups and endpoint_trunk_groups.intersection(vlan.trunk_groups))

    @cached_property
    def accepted_vlans(self: SharedUtils) -> list[int]:
        """
        The 'vlans' switch fact is a string representing a vlan range (ex. "1-200").

        For l2 switches return intersection of vlans from this switch and vlans from uplink switches.
        For anything else return the expanded vlans from this switch.
        """
        switch_vlans = self.get_switch_fact("vlans", required=False)
        if not switch_vlans:
            return []
        switch_vlans_list = range_expand(switch_vlans)
        accepted_vlans = [int(vlan) for vlan in switch_vlans_list]
        if self.uplink_type != "port-channel":
            return accepted_vlans

        uplink_switches = unique(self.uplink_switches)
        uplink_switches = [uplink_switch for uplink_switch in uplink_switches if uplink_switch in self.all_fabric_devices]
        for uplink_switch in uplink_switches:
            uplink_switch_facts = self.get_peer_facts(uplink_switch, required=True)
            uplink_switch_vlans = uplink_switch_facts.get("vlans", [])
            uplink_switch_vlans_list = range_expand(uplink_switch_vlans)
            uplink_switch_vlans_list = [int(vlan) for vlan in uplink_switch_vlans_list]
            accepted_vlans = [vlan for vlan in accepted_vlans if vlan in uplink_switch_vlans_list]

        return accepted_vlans

    def is_accepted_vrf(self: SharedUtils, vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem) -> bool:
        """
        Returns True if.

        - filter.allow_vrfs == ["all"] OR VRF is included in filter.allow_vrfs.

        AND

        - filter.not_vrfs == [] OR VRF is NOT in filter.deny_vrfs
        """
        return ("all" in self.node_config.filter.allow_vrfs or vrf.name in self.node_config.filter.allow_vrfs) and (
            not self.node_config.filter.deny_vrfs or vrf.name not in self.node_config.filter.deny_vrfs
        )

    def is_forced_vrf(self: SharedUtils, vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem, tenant_name: str) -> bool:
        """
        Returns True if the given VRF name should be configured even without any loopbacks or SVIs etc.

        There can be various causes for this:
        - The VRF is part of a tenant set under 'always_include_vrfs_in_tenants'
        - 'always_include_vrfs_in_tenants' is set to ['all']
        - This device is using 'p2p-vrfs' as uplink type and the VRF present on the uplink switch.
        """
        if "all" in self.node_config.filter.always_include_vrfs_in_tenants or tenant_name in self.node_config.filter.always_include_vrfs_in_tenants:
            return True

        return vrf.name in (self.get_switch_fact("uplink_switch_vrfs", required=False) or [])

    def filtered_vrfs(
        self: SharedUtils, tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem
    ) -> EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.Vrfs:
        """
        Return sorted and filtered vrf list from given tenant.

        Filtering based on svi tags, l3interfaces, loopbacks or self.is_forced_vrf() check.
        Keys of VRF data model will be converted to lists.
        """
        filtered_vrfs = EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.Vrfs()

        for vrf in tenant.vrfs._natural_sorted():
            if not self.is_accepted_vrf(vrf):
                continue

            # Copying original_vrf
            vrf._tenant = tenant.name

            vrf.bgp_peers = vrf.bgp_peers._filtered(lambda bgp_peer: self.hostname in bgp_peer.nodes)._natural_sorted(sort_key="ip_address")
            vrf.static_routes = vrf.static_routes._filtered(lambda route: not route.nodes or self.hostname in route.nodes)
            vrf.ipv6_static_routes = vrf.ipv6_static_routes._filtered(lambda route: not route.nodes or self.hostname in route.nodes)
            vrf.svis = self.filtered_svis(vrf)
            vrf.l3_interfaces = vrf.l3_interfaces._filtered(
                lambda l3_interface: bool(self.hostname in l3_interface.nodes and l3_interface.ip_addresses and l3_interface.interfaces)
            )
            vrf.loopbacks = vrf.loopbacks._filtered(lambda loopback: loopback.node == self.hostname)

            if self.vtep is True:
                evpn_l3_multicast_enabled = default(vrf.evpn_l3_multicast.enabled, tenant.evpn_l3_multicast.enabled)
                # TODO: Consider if all this should be moved out of filtered_vrfs.
                if self.evpn_multicast:
                    vrf._evpn_l3_multicast_enabled = evpn_l3_multicast_enabled
                    vrf._evpn_l3_multicast_group_ip = vrf.evpn_l3_multicast.evpn_underlay_l3_multicast_group

                    rps = []
                    for rp_entry in vrf.pim_rp_addresses or tenant.pim_rp_addresses:
                        if not rp_entry.nodes or self.hostname in rp_entry.nodes:
                            if not rp_entry.rps:
                                # TODO: Evaluate if schema should just have required for this key.
                                msg = f"'pim_rp_addresses.rps' under VRF '{vrf.name}' in Tenant '{tenant.name}' is required."
                                raise AristaAvdInvalidInputsError(msg)
                            for rp_ip in rp_entry.rps:
                                rp_address = {"address": rp_ip}
                                if rp_entry.groups:
                                    if rp_entry.access_list_name:
                                        rp_address["access_lists"] = [rp_entry.access_list_name]
                                    else:
                                        rp_address["groups"] = rp_entry.groups._as_list()

                                rps.append(rp_address)

                    if rps:
                        vrf._pim_rp_addresses = rps

                        for evpn_peg in vrf.evpn_l3_multicast.evpn_peg or tenant.evpn_l3_multicast.evpn_peg:
                            if not evpn_peg.nodes or self.hostname in evpn_peg.nodes:
                                vrf._evpn_l3_multicast_evpn_peg_transit = evpn_peg.transit
                                break

            vrf.additional_route_targets = vrf.additional_route_targets._filtered(
                lambda rt: bool((not rt.nodes or self.hostname in rt.nodes) and rt.address_family and rt.route_target and rt.type in ["import", "export"])
            )

            if vrf.svis or vrf.l3_interfaces or vrf.loopbacks or self.is_forced_vrf(vrf, tenant.name):
                filtered_vrfs.append(vrf)

            if tenant_evpn_vlan_bundle := tenant.evpn_vlan_bundle:
                for svi in vrf.svis:
                    svi.evpn_vlan_bundle = svi.evpn_vlan_bundle or tenant_evpn_vlan_bundle

        return filtered_vrfs

    def get_merged_svi_config(
        self: SharedUtils, svi: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem
    ) -> EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem:
        """
        Return structured config for one svi after inheritance.

        Handle inheritance of node config as svi_profiles in two levels:

        First variables will be merged
        svi > svi_profile > svi_parent_profile --> svi_cfg
        &
        svi.nodes.<hostname> > svi_profile.nodes.<hostname> > svi_parent_profile.nodes.<hostname> --> svi_node_cfg

        Then svi is updated with the result of merging svi_node_cfg over svi_cfg
        svi_node_cfg > svi_cfg --> svi
        """
        if svi.profile:
            if svi.profile not in self.inputs.svi_profiles:
                msg = f"Profile '{svi.profile}' applied under SVI '{svi.name}' does not exist in `svi_profiles`."
                raise AristaAvdInvalidInputsError(msg)
            svi_profile = self.inputs.svi_profiles[svi.profile]._deepcopy()

            if svi_profile.parent_profile:
                if svi_profile.parent_profile not in self.inputs.svi_profiles:
                    msg = f"Profile '{svi_profile.parent_profile}' applied under SVI Profile '{svi_profile.profile}' does not exist in `svi_profiles`."
                    raise AristaAvdInvalidInputsError(msg)

                # Inherit from the parent profile
                svi_profile._deepinherit(self.inputs.svi_profiles[svi_profile.parent_profile])

            # Inherit from the profile
            merged_svi = svi._deepinherited(
                svi_profile._cast_as(EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem, ignore_extra_keys=True)
            )
        else:
            merged_svi = svi

        # Merge node specific SVI over the general SVI data.
        if self.hostname in merged_svi.nodes:
            node_specific_svi = merged_svi.nodes[self.hostname]._cast_as(
                EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem, ignore_extra_keys=True
            )
            merged_svi._deepmerge(node_specific_svi, list_merge="replace")

        return merged_svi

    def filtered_svis(
        self: SharedUtils, vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem
    ) -> EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.Svis:
        """
        Return sorted and filtered svi list from given tenant vrf.

        Filtering based on accepted vlans since eos_designs_facts already
        filtered that on tags and trunk_groups.
        """
        if not (self.network_services_l2 or self.network_services_l2_as_subint):
            return EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.Svis()

        svis = vrf.svis._filtered(self.is_accepted_vlan)

        # Handle svi_profile inheritance
        svis = EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.Svis([self.get_merged_svi_config(svi) for svi in svis])

        # Perform filtering on tags after merge of profiles, to support tags being set inside profiles.
        svis = svis._filtered(lambda svi: "all" in self.filter_tags or bool(set(svi.tags).intersection(self.filter_tags)))

        # Set tenant key on all SVIs
        for svi in svis:
            svi._tenant = vrf._tenant

        return svis._natural_sorted(sort_key="id")

    @cached_property
    def endpoint_vlans(self: SharedUtils) -> list:
        endpoint_vlans = self.get_switch_fact("endpoint_vlans", required=False)
        if not endpoint_vlans:
            return []
        return [int(vlan_id) for vlan_id in range_expand(endpoint_vlans)]

    @staticmethod
    def get_vrf_id(vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem, required: bool = True) -> int | None:
        vrf_id = default(vrf.vrf_id, vrf.vrf_vni)
        if vrf_id is None and required:
            msg = f"'vrf_id' or 'vrf_vni' for VRF '{vrf.name}' must be set."
            raise AristaAvdInvalidInputsError(msg)
        return vrf_id

    @staticmethod
    def get_vrf_vni(vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem) -> int:
        vrf_vni = default(vrf.vrf_vni, vrf.vrf_id)
        if vrf_vni is None:
            msg = f"'vrf_vni' or 'vrf_id' for VRF '{vrf.name}' must be set."
            raise AristaAvdInvalidInputsError(msg)
        return vrf_vni

    @cached_property
    def vrfs(self: SharedUtils) -> list[str]:
        """
        Return the list of vrfs to be defined on this switch.

        Ex. ["default", "prod"]
        """
        if not self.network_services_l3:
            return []

        return natural_sort({vrf.name for tenant in self.filtered_tenants for vrf in tenant.vrfs})

    @staticmethod
    def get_additional_svi_config(
        svi_config: dict,
        svi: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
    ) -> None:
        """
        Adding IP helpers and OSPF for SVIs via a common function.

        Used for SVIs and for subinterfaces when uplink_type: lan.

        The given svi_config is updated in-place.
        """
        svi_ip_helpers = svi.ip_helpers or vrf.ip_helpers
        if svi_ip_helpers:
            svi_config["ip_helpers"] = [
                {"ip_helper": svi_ip_helper.ip_helper, "source_interface": svi_ip_helper.source_interface, "vrf": svi_ip_helper.source_vrf}
                for svi_ip_helper in svi_ip_helpers
            ]

        if svi.ospf.enabled and vrf.ospf.enabled:
            svi_config.update(
                {
                    "ospf_area": svi.ospf.area,
                    "ospf_network_point_to_point": svi.ospf.point_to_point,
                    "ospf_cost": svi.ospf.cost,
                },
            )
            ospf_authentication = svi.ospf.authentication
            if ospf_authentication == "simple" and (ospf_simple_auth_key := svi.ospf.simple_auth_key) is not None:
                svi_config.update({"ospf_authentication": ospf_authentication, "ospf_authentication_key": ospf_simple_auth_key})
            elif ospf_authentication == "message-digest" and (ospf_message_digest_keys := svi.ospf.message_digest_keys) is not None:
                ospf_keys = []
                for ospf_key in ospf_message_digest_keys:
                    if not (ospf_key.id and ospf_key.key):
                        continue

                    ospf_keys.append({"id": ospf_key.id, "hash_algorithm": ospf_key.hash_algorithm, "key": ospf_key.key})
                if ospf_keys:
                    svi_config.update({"ospf_authentication": ospf_authentication, "ospf_message_digest_keys": ospf_keys})

    @cached_property
    def bgp_in_network_services(self: SharedUtils) -> bool:
        """
        True if BGP is needed or forcefully enabled for any VRF under network services.

        Used to enable router_bgp even if there is no overlay or underlay routing protocol.
        """
        if not self.network_services_l3:
            return False

        return any(self.bgp_enabled_for_vrf(vrf) for tenant in self.filtered_tenants for vrf in tenant.vrfs)

    def bgp_enabled_for_vrf(self: SharedUtils, vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem) -> bool:
        """
        True if the given VRF should be included under Router BGP.

        - If bgp.enabled is set to True, we will always configure the VRF.
        - If bgp.enabled is set to False, we will never configure the VRF.

        Otherwise we will autodetect:
        - If the VRF is part of an overlay we will configure BGP for it.
        - If the VRF is on a WAN router, we will configure BGP for it.
        - If any BGP peers are configured we will configure BGP for it.
        - If uplink type is p2p_vrfs and the vrf is included in uplink VRFs.
        """
        if vrf.bgp.enabled is not None:
            return vrf.bgp.enabled

        vrf_address_families = [af for af in vrf.address_families if af in self.overlay_address_families]
        return any(
            [
                (self.is_wan_router and self.vrf_has_wan_vni(vrf.name)),
                vrf_address_families,
                vrf.bgp_peers,
                (self.uplink_type == "p2p-vrfs" and vrf.name in (self.get_switch_fact("uplink_switch_vrfs", required=False) or [])),
            ]
        )
