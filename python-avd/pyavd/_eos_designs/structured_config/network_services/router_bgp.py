# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ipaddress
from itertools import groupby as itertools_groupby
from typing import TYPE_CHECKING, Protocol, cast

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.schema import EosDesigns
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import AvdStringFormatter, default, get_item, strip_empties_from_dict
from pyavd.j2filters import list_compress

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class RouterBgpMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    need_mlag_peer_group: bool = False
    """Flag set during configuration of BGP VRFs if they have MLAG enabled. Used later to decide if we need to configure the MLAG peer group or not."""

    @structured_config_contributor
    def router_bgp(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Set the structured config for router_bgp.

        The main function calls some individual functions which updates structured configuration directly.

        Changing legacy behavior is to only render this on vtep or mpls_ler
        by instead skipping vlans/bundles if not vtep or mpls_ler
        TODO: Fix so this also works for L2LS with VRFs
        """
        if not self.shared_utils.bgp:
            return

        tenant_svis_l2vlans_dict = self._router_bgp_sorted_vlans_and_svis_lists()

        # These functions update structured config directly.
        self._router_bgp_peer_groups()
        self._router_bgp_vrfs()

        self._router_bgp_vlans(tenant_svis_l2vlans_dict)
        self._router_bgp_vlan_aware_bundles(tenant_svis_l2vlans_dict)
        self._router_bgp_redistribute_routes()
        self._router_bgp_vpws()

        # Configure MLAG iBGP peer-group if needed. The function updates structured config directly.
        # Catches cases where underlay is not BGP but we still need MLAG iBGP peering.
        if not self.shared_utils.underlay_bgp and self.need_mlag_peer_group:
            self.structured_config.router_bgp._deepmerge(self.shared_utils.get_router_bgp_with_mlag_peer_group(self.custom_structured_configs))

    def _router_bgp_peer_groups(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Set partial structured config for router_bgp.peer_groups.

        Covers two areas:
        - bgp_peer_groups defined under the vrf including ipv4/ipv6 address_families.
        - adding route-map to the underlay peer-group in case of services in vrf default
        """
        if not self.shared_utils.network_services_l3:
            return

        peer_groups: list[
            EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.BgpPeerGroupsItem
            | EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.BgpPeerGroupsItem
        ] = []
        peer_peergroups = set()
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                # bgp_peers is already filtered in filtered_tenants to only contain entries with our hostname
                if not (vrf.bgp_peers or vrf.bgp_peer_groups):
                    continue

                vrf_peer_peergroups = {peer.peer_group for peer in vrf.bgp_peers if peer.peer_group}
                peer_groups.extend(
                    [
                        peer_group
                        for peer_group in vrf.bgp_peer_groups
                        if self.shared_utils.hostname in peer_group.nodes or peer_group.name in vrf_peer_peergroups
                    ],
                )
                peer_peergroups.update(vrf_peer_peergroups)

            peer_groups.extend(
                [peer_group for peer_group in tenant.bgp_peer_groups if self.shared_utils.hostname in peer_group.nodes or peer_group.name in peer_peergroups],
            )

        for peer_group in peer_groups:
            self.structured_config.router_bgp.peer_groups.append(peer_group._cast_as(EosCliConfigGen.RouterBgp.PeerGroupsItem, ignore_extra_keys=True))
            if peer_group.address_family_ipv4:
                af_peer_group = peer_group.address_family_ipv4._cast_as(EosCliConfigGen.RouterBgp.AddressFamilyIpv4.PeerGroupsItem, ignore_extra_keys=True)
                af_peer_group.name = peer_group.name
                self.structured_config.router_bgp.address_family_ipv4.peer_groups.append(af_peer_group)
            if peer_group.address_family_ipv6:
                af_peer_group = peer_group.address_family_ipv6._cast_as(EosCliConfigGen.RouterBgp.AddressFamilyIpv6.PeerGroupsItem, ignore_extra_keys=True)
                af_peer_group.name = peer_group.name
                self.structured_config.router_bgp.address_family_ipv6.peer_groups.append(af_peer_group)

        # router bgp default vrf configuration for evpn
        if self._vrf_default_evpn and (self._vrf_default_ipv4_subnets or self._vrf_default_ipv4_static_routes["static_routes"]):
            self.structured_config.router_bgp.peer_groups.append_new(
                name=self.inputs.bgp_peer_groups.ipv4_underlay_peers.name,
                type="ipv4",
                route_map_out="RM-BGP-UNDERLAY-PEERS-OUT",
            )

    def _router_bgp_vrfs(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Set partial structured config for router_bgp.

        Covers these areas:
        - vrfs for all VRFs.
        - neighbors and address_family_ipv4/6 for VRF default.
        """
        if not self.shared_utils.network_services_l3:
            return

        # For VRF default the bgp_vrf variable will be set to the global router_bgp for some settings.
        bgp_vrf: EosCliConfigGen.RouterBgp.VrfsItem | EosCliConfigGen.RouterBgp

        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                if not self.shared_utils.bgp_enabled_for_vrf(vrf):
                    continue

                bgp_vrf = EosCliConfigGen.RouterBgp.VrfsItem()
                if vrf.bgp.raw_eos_cli:
                    bgp_vrf.eos_cli = vrf.bgp.raw_eos_cli

                if vrf.bgp.structured_config:
                    self.custom_structured_configs.nested.router_bgp.vrfs.obtain(vrf.name)._deepmerge(
                        vrf.bgp.structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
                    )

                vrf_address_families = {af for af in vrf.address_families if af in self.shared_utils.overlay_address_families}
                if self.shared_utils.is_wan_vrf(vrf):
                    # If the VRF is a WAN VRF, EVPN RTs are needed.
                    vrf_address_families.add("evpn")

                if vrf_address_families:
                    # The called function in-place updates the bgp_vrf dict.
                    self._update_router_bgp_vrf_evpn_or_mpls_cfg(bgp_vrf, vrf, vrf_address_families)

                if vrf.name != "default":
                    bgp_vrf.router_id = self.get_vrf_router_id(vrf, tenant, vrf.bgp.router_id)

                    if vrf.redistribute_connected:
                        bgp_vrf.redistribute.connected.enabled = True
                    # Redistribution of static routes for VRF default are handled elsewhere
                    # since there is a choice between redistributing to underlay or overlay.
                    if vrf.redistribute_static or (vrf.static_routes and vrf.redistribute_static is None):
                        bgp_vrf.redistribute.static.enabled = True

                    if self.shared_utils.inband_mgmt_vrf == vrf.name and self.shared_utils.inband_management_parent_vlans:
                        bgp_vrf.redistribute.attached_host.enabled = True

                else:
                    # VRF default

                    # RD/RT and/or eos_cli/struct_cfg which should go under the vrf default context.
                    # Any peers added later will be put directly under router_bgp
                    if bgp_vrf:
                        bgp_vrf.name = vrf.name
                        self.structured_config.router_bgp.vrfs.append(bgp_vrf)

                    # Resetting bgp_vrf so we only add global keys if there are any neighbors for VRF default
                    bgp_vrf = self.structured_config.router_bgp

                    if self.shared_utils.underlay_routing_protocol == "none":
                        # We need to add redistribute connected for the default VRF when underlay_routing_protocol is "none"
                        bgp_vrf.redistribute.connected.enabled = True

                # MLAG IBGP Peering VLANs per VRF
                # Will only be configured for VRF default if underlay_routing_protocol == "none".
                if (vlan_id := self._mlag_ibgp_peering_vlan_vrf(vrf, tenant)) is not None:
                    self._update_router_bgp_vrf_mlag_neighbor_cfg(bgp_vrf, vrf, tenant, vlan_id)
                    self.need_mlag_peer_group = True

                for bgp_peer in vrf.bgp_peers:
                    peer_ip = bgp_peer.ip_address
                    address_family = bgp_vrf.address_family_ipv6 if ipaddress.ip_address(peer_ip).version == 6 else bgp_vrf.address_family_ipv4
                    address_family.neighbors.append_new(
                        ip_address=peer_ip,
                        activate=True,
                        prefix_list_in=bgp_peer.prefix_list_in,
                        prefix_list_out=bgp_peer.prefix_list_out,
                    )

                    # Below we recast directly to eos_cli_config_gen. Losing incompatible keys, but relaying everything else.
                    bgp_peer_config = bgp_peer._cast_as(bgp_vrf.NeighborsItem, ignore_extra_keys=True)

                    if bgp_peer.set_ipv4_next_hop or bgp_peer.set_ipv6_next_hop:
                        route_map = f"RM-{vrf.name}-{peer_ip}-SET-NEXT-HOP-OUT"
                        bgp_peer_config.route_map_out = route_map
                        if bgp_peer_config.default_originate and not bgp_peer_config.default_originate.route_map:
                            bgp_peer_config.default_originate.route_map = route_map

                    # TODO: Figure out how to fix type checking. It looses track of the bgp_peer_config even though it was derived from bgp_vrf.NeighborsItem.
                    bgp_vrf.neighbors.append(bgp_peer_config)

                if vrf.ospf.enabled and vrf.redistribute_ospf and (not vrf.ospf.nodes or self.shared_utils.hostname in vrf.ospf.nodes):
                    bgp_vrf.redistribute.ospf.enabled = True

                if bgp_vrf.neighbors and self.inputs.bgp_update_wait_install and self.shared_utils.platform_settings.feature_support.bgp_update_wait_install:
                    bgp_vrf.updates.wait_install = True

                # Skip adding the VRF if we have no config.
                if not bgp_vrf:
                    continue

                if vrf.name == "default":
                    # VRF default is added directly under router_bgp
                    bgp_vrf = cast(EosCliConfigGen.RouterBgp, bgp_vrf)
                    self.structured_config.router_bgp._deepmerge(bgp_vrf)
                else:
                    bgp_vrf = cast(EosCliConfigGen.RouterBgp.VrfsItem, bgp_vrf)
                    bgp_vrf.name = vrf.name
                    self.structured_config.router_bgp.vrfs.append(bgp_vrf)

    def _update_router_bgp_vrf_evpn_or_mpls_cfg(
        self: AvdStructuredConfigNetworkServicesProtocol,
        bgp_vrf: EosCliConfigGen.RouterBgp.VrfsItem,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
        vrf_address_families: set[str],
    ) -> None:
        """In-place update EVPN/MPLS part of structured config for *one* VRF under router_bgp.vrfs."""
        bgp_vrf.rd = self.get_vrf_rd(vrf)
        vrf_rt = self.get_vrf_rt(vrf)
        route_targets = {"import": [], "export": []}

        for af in sorted(vrf_address_families):
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

        if vrf.name == "default" and self._vrf_default_evpn and self._route_maps_vrf_default:
            # Special handling of vrf default with evpn.

            if (target := get_item(route_targets["export"], "address_family", "evpn")) is None:
                route_targets["export"].append({"address_family": "evpn", "route_targets": ["route-map RM-EVPN-EXPORT-VRF-DEFAULT"]})
            else:
                target.setdefault("route_targets", []).append("route-map RM-EVPN-EXPORT-VRF-DEFAULT")

        bgp_vrf.route_targets = EosCliConfigGen.RouterBgp.VrfsItem.RouteTargets._from_dict(route_targets)

        # VRF default
        if vrf.name == "default":
            return

        # Not VRF default
        bgp_vrf.evpn_multicast = getattr(vrf._internal_data, "evpn_l3_multicast_enabled", None)
        if evpn_multicast_transit_mode := getattr(vrf._internal_data, "evpn_l3_multicast_evpn_peg_transit", False):
            bgp_vrf.evpn_multicast_address_family.ipv4.transit = evpn_multicast_transit_mode

    def _update_router_bgp_vrf_mlag_neighbor_cfg(
        self: AvdStructuredConfigNetworkServicesProtocol,
        bgp_vrf: EosCliConfigGen.RouterBgp.VrfsItem | EosCliConfigGen.RouterBgp,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
        vlan_id: int,
    ) -> None:
        """In-place update MLAG neighbor part of structured config for *one* VRF under router_bgp.vrfs."""
        if self._exclude_mlag_ibgp_peering_from_redistribute(vrf, tenant):
            bgp_vrf.redistribute.connected._update(enabled=True, route_map="RM-CONN-2-BGP-VRFS")

        interface_name = f"Vlan{vlan_id}"

        if self.inputs.underlay_rfc5549 and self.inputs.overlay_mlag_rfc5549:
            bgp_vrf.neighbor_interfaces.append_new(
                name=interface_name,
                peer_group=self.shared_utils.mlag_vrfs_peer_group_name,
                remote_as=self.shared_utils.bgp_as,
                description=AvdStringFormatter().format(
                    self.inputs.mlag_bgp_peer_description,
                    mlag_peer=self.shared_utils.mlag_peer,
                    interface=interface_name,
                    peer_interface=interface_name,
                ),
            )
        else:
            if not vrf.mlag_ibgp_peering_ipv4_pool:
                ip_address = self.shared_utils.mlag_peer_ibgp_ip
            elif self.shared_utils.mlag_role == "primary":
                ip_address = self.shared_utils.ip_addressing.mlag_ibgp_peering_ip_secondary(vrf.mlag_ibgp_peering_ipv4_pool)
            else:
                ip_address = self.shared_utils.ip_addressing.mlag_ibgp_peering_ip_primary(vrf.mlag_ibgp_peering_ipv4_pool)

            bgp_vrf.neighbors.append_new(
                ip_address=ip_address,
                peer_group=self.shared_utils.mlag_vrfs_peer_group_name,
                description=AvdStringFormatter().format(
                    self.inputs.mlag_bgp_peer_description,
                    **strip_empties_from_dict(
                        {"mlag_peer": self.shared_utils.mlag_peer, "interface": interface_name, "peer_interface": interface_name, "vrf": vrf.name}
                    ),
                ),
            )
            # In case of only underlay_rfc5549 but not overlay_mlag_rfc5549, we need to remove the ipv6 next-hop per neighbor/vrf
            # This is only needed when we use the same MLAG peer-group for both underlay and overlay.
            if self.inputs.underlay_rfc5549 and not self.shared_utils.use_separate_peer_group_for_mlag_vrfs:
                af_neighbor = bgp_vrf.address_family_ipv4.neighbors.obtain(ip_address)
                af_neighbor.next_hop.address_family_ipv6.enabled = False

    def _router_bgp_sorted_vlans_and_svis_lists(self: AvdStructuredConfigNetworkServicesProtocol) -> dict:
        tenant_svis_l2vlans_dict = {}
        for tenant in self.shared_utils.filtered_tenants:
            tenant_svis_l2vlans_dict[tenant.name] = {}

            # For L2VLANs
            l2vlans_bundle_dict = {}
            l2vlans_non_bundle_list = {}
            sorted_vlan_list = sorted(tenant.l2vlans, key=self._get_vlan_aware_bundle_name_tuple_for_l2vlans)
            bundle_groups = itertools_groupby(sorted_vlan_list, self._get_vlan_aware_bundle_name_tuple_for_l2vlans)
            for vlan_aware_bundle_name_tuple, l2vlans in bundle_groups:
                bundle_name, is_evpn_vlan_bundle = vlan_aware_bundle_name_tuple
                l2vlans_list = list(l2vlans)

                if is_evpn_vlan_bundle:
                    l2vlans_bundle_dict[bundle_name] = l2vlans_list
                else:
                    l2vlans_non_bundle_list[bundle_name] = l2vlans_list

            # For SVIs
            vrf_svis_bundle_dict = {}
            vrf_svis_non_bundle_dict = {}
            for vrf in tenant.vrfs:
                vrf_svis_non_bundle_dict[vrf.name] = []
                vrf_svis_bundle_dict[vrf.name] = {}
                sorted_svi_list = sorted(vrf.svis, key=self._get_vlan_aware_bundle_name_tuple_for_svis)
                bundle_groups_svis = itertools_groupby(sorted_svi_list, self._get_vlan_aware_bundle_name_tuple_for_svis)
                for vlan_aware_bundle_name_tuple, svis in bundle_groups_svis:
                    bundle_name, is_evpn_vlan_bundle = vlan_aware_bundle_name_tuple
                    svis_list = list(svis)

                    if is_evpn_vlan_bundle:
                        vrf_svis_bundle_dict[vrf.name][bundle_name] = svis_list
                    else:
                        vrf_svis_non_bundle_dict[vrf.name] = svis_list

            tenant_svis_l2vlans_dict[tenant.name].update(
                {
                    "svi_bundle": vrf_svis_bundle_dict,
                    "svi_non_bundle": vrf_svis_non_bundle_dict,
                    "l2vlan_bundle": l2vlans_bundle_dict,
                    "l2vlan_non_bundle": l2vlans_non_bundle_list,
                }
            )

        return tenant_svis_l2vlans_dict

    def _router_bgp_vlans(self: AvdStructuredConfigNetworkServicesProtocol, tenant_svis_l2vlans_dict: dict) -> None:
        """Return structured config for router_bgp.vlans."""
        if not (
            self.shared_utils.network_services_l2
            and "evpn" in self.shared_utils.overlay_address_families
            and not self.inputs.evpn_vlan_aware_bundles
            and (self.shared_utils.overlay_vtep or self.shared_utils.overlay_ler)
            and (self.shared_utils.overlay_evpn)
        ):
            return

        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                for svi in tenant_svis_l2vlans_dict[tenant.name]["svi_non_bundle"][vrf.name]:
                    if (vlan := self._router_bgp_vlans_vlan(svi, tenant, vrf)) is not None:
                        self.structured_config.router_bgp.vlans.append(vlan, ignore_fields=("tenant",))

            # L2 Vlans per Tenant
            for l2vlans in tenant_svis_l2vlans_dict[tenant.name]["l2vlan_non_bundle"].values():
                for l2vlan in l2vlans:
                    if (
                        vlan := self._router_bgp_vlans_vlan(
                            l2vlan, tenant, vrf=EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem()
                        )
                    ) is not None:
                        self.structured_config.router_bgp.vlans.append(vlan, ignore_fields=("tenant",))

    def _router_bgp_vlans_vlan(
        self: AvdStructuredConfigNetworkServicesProtocol,
        vlan: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem
        | EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlansItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
    ) -> EosCliConfigGen.RouterBgp.VlansItem | None:
        """Return structured config for one given vlan under router_bgp.vlans."""
        if not vlan.vxlan:
            return None

        vlan_rd = self.get_vlan_rd(vlan, tenant)
        vlan_rt = self.get_vlan_rt(vlan, tenant)

        bgp_vlan = EosCliConfigGen.RouterBgp.VlansItem(
            id=vlan.id,
            tenant=tenant.name,
            rd=vlan_rd,
        )
        bgp_vlan.route_targets.both.append(vlan_rt)
        bgp_vlan.redistribute_routes.append("learned")

        if vlan.bgp.raw_eos_cli:
            bgp_vlan.eos_cli = vlan.bgp.raw_eos_cli

        if vlan.bgp.structured_config:
            self.custom_structured_configs.nested.router_bgp.vlans.obtain(vlan.id)._deepmerge(
                vlan.bgp.structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
            )

        if self.shared_utils.node_config.evpn_gateway.evpn_l2.enabled and default(
            vlan.evpn_l2_multi_domain, vrf.evpn_l2_multi_domain, tenant.evpn_l2_multi_domain
        ):
            bgp_vlan.rd_evpn_domain._update(domain="remote", rd=vlan_rd)
            bgp_vlan.route_targets.import_export_evpn_domains.append_new(domain="remote", route_target=vlan_rt)

        vlan_evpn_l2_multicast_enabled = default(vlan.evpn_l2_multicast.enabled, tenant.evpn_l2_multicast.enabled) and self.shared_utils.evpn_multicast is True
        # if vlan_evpn_l2_multicast_enabled we redistribute igmp if:
        #   - This is an L2 vlan
        #   - L3 multicast is disabled or not configured
        #   - evpn_l2_multicast.always_redistribute_igmp is set on the vlan or tenant.
        if vlan_evpn_l2_multicast_enabled and (
            isinstance(vlan, EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlansItem)
            or not getattr(vrf._internal_data, "evpn_l3_multicast_enabled", False)
            or bool(default(vlan.evpn_l2_multicast.always_redistribute_igmp, tenant.evpn_l2_multicast.always_redistribute_igmp))
        ):
            bgp_vlan.redistribute_routes.append("igmp")

        return bgp_vlan

    def _get_vlan_aware_bundle_name_tuple_for_l2vlans(
        self: AvdStructuredConfigNetworkServicesProtocol, vlan: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlansItem
    ) -> tuple[str, bool] | None:
        """Return a tuple with string with the vlan-aware-bundle name for one VLAN and a boolean saying if this is a evpn_vlan_bundle."""
        if vlan.evpn_vlan_bundle:
            return (vlan.evpn_vlan_bundle, True)
        return (vlan.name, False)

    def _get_vlan_aware_bundle_name_tuple_for_svis(
        self: AvdStructuredConfigNetworkServicesProtocol, vlan: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem
    ) -> tuple[str, bool] | None:
        """
        Return a tuple with string with the vlan-aware-bundle name for one VLAN and a boolean saying if this is a evpn_vlan_bundle.

        If no bundle is configured, it will return an empty string as name, since the calling function will then get all svis without bundle
        grouped under "".
        """
        if vlan.evpn_vlan_bundle:
            return (vlan.evpn_vlan_bundle, True)
        return ("", False)

    def _get_evpn_vlan_bundle(
        self: AvdStructuredConfigNetworkServicesProtocol,
        vlan: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem
        | EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlansItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
        bundle_name: str,
    ) -> EosDesigns.EvpnVlanBundlesItem:
        """Return an evpn_vlan_bundle dict if it exists, else raise an exception."""
        if bundle_name not in self.inputs.evpn_vlan_bundles:
            msg = (
                "The 'evpn_vlan_bundle' of the svis/l2vlans must be defined in the common 'evpn_vlan_bundles' setting. First occurrence seen for svi/l2vlan"
                f" {vlan.id} in Tenant '{tenant.name}' and evpn_vlan_bundle '{vlan.evpn_vlan_bundle}'."
            )
            raise AristaAvdInvalidInputsError(msg)
        return self.inputs.evpn_vlan_bundles[bundle_name]

    def _get_svi_l2vlan_bundle(
        self: AvdStructuredConfigNetworkServicesProtocol,
        evpn_vlan_bundle: EosDesigns.EvpnVlanBundlesItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
        vlans: list,
    ) -> EosCliConfigGen.RouterBgp.VlanAwareBundlesItem | None:
        """Return an bundle config for a svi or l2vlan."""
        bundle = self._router_bgp_vlan_aware_bundle(
            name=evpn_vlan_bundle.name,
            vlans=vlans,
            rd=self.get_vlan_aware_bundle_rd(id=evpn_vlan_bundle.id, tenant=tenant, is_vrf=False, rd_override=evpn_vlan_bundle.rd_override),
            rt=self.get_vlan_aware_bundle_rt(
                id=evpn_vlan_bundle.id,
                vni=evpn_vlan_bundle.id,
                tenant=tenant,
                is_vrf=False,
                rt_override=evpn_vlan_bundle.rt_override,
            ),
            evpn_l2_multi_domain=default(evpn_vlan_bundle.evpn_l2_multi_domain, tenant.evpn_l2_multi_domain),
            tenant=tenant,
        )

        if bundle is not None:
            if (eos_cli := evpn_vlan_bundle.bgp.raw_eos_cli) is not None:
                bundle.eos_cli = eos_cli
            return bundle

        return None

    def _router_bgp_vlan_aware_bundles(self: AvdStructuredConfigNetworkServicesProtocol, tenant_svis_l2vlans_dict: dict) -> None:
        """Set structured config for router_bgp.vlan_aware_bundles."""
        if not self.shared_utils.network_services_l2 or not self.shared_utils.overlay_evpn:
            return

        for tenant in self.shared_utils.filtered_tenants:
            l2vlan_svi_vlan_aware_bundles = {}
            for vrf in tenant.vrfs:
                for bundle_name, svis in tenant_svis_l2vlans_dict[tenant.name]["svi_bundle"][vrf.name].items():
                    # SVIs which have an evpn_vlan_bundle defined
                    if bundle_name in l2vlan_svi_vlan_aware_bundles:
                        l2vlan_svi_vlan_aware_bundles[bundle_name]["l2vlan_svis"].extend(svis)
                    else:
                        # check if the referred name exists in the global evpn_vlan_bundles
                        evpn_vlan_bundle = self._get_evpn_vlan_bundle(svis[0], tenant, bundle_name)
                        l2vlan_svi_vlan_aware_bundles[bundle_name] = {"evpn_vlan_bundle": evpn_vlan_bundle, "l2vlan_svis": svis}

                if self.inputs.evpn_vlan_aware_bundles:
                    svis = tenant_svis_l2vlans_dict[tenant.name]["svi_non_bundle"][vrf.name]
                    # SVIs which don't have an evpn_vlan_bundle defined are included in the VRF vlan-aware-bundle
                    if (bundle := self._router_bgp_vlan_aware_bundles_vrf(vrf, tenant, svis)) is not None:
                        self.structured_config.router_bgp.vlan_aware_bundles.append(bundle)

            # L2 Vlans per Tenant
            # If multiple L2 Vlans share the same evpn_vlan_bundle name, they will be part of the same vlan-aware-bundle else they use the vlan name as bundle
            for bundle_name, l2vlans in tenant_svis_l2vlans_dict[tenant.name]["l2vlan_bundle"].items():
                if bundle_name in l2vlan_svi_vlan_aware_bundles:
                    l2vlan_svi_vlan_aware_bundles[bundle_name]["l2vlan_svis"].extend(l2vlans)
                else:
                    # check if the referred name exists in the global evpn_vlan_bundles
                    evpn_vlan_bundle = self._get_evpn_vlan_bundle(l2vlans[0], tenant, bundle_name)
                    l2vlan_svi_vlan_aware_bundles[bundle_name] = {"evpn_vlan_bundle": evpn_vlan_bundle, "l2vlan_svis": l2vlans}

            if self.inputs.evpn_vlan_aware_bundles:
                for bundle_name, l2vlans in tenant_svis_l2vlans_dict[tenant.name]["l2vlan_non_bundle"].items():
                    # Without "evpn_vlan_bundle" we fall back to per-vlan behavior
                    if (
                        bgp_vlan := self._router_bgp_vlans_vlan(
                            l2vlans[0], tenant, vrf=EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem()
                        )
                    ) is None:
                        # Skip bundle since no vlans were enabled for vxlan.
                        continue

                    # We are reusing the regular bgp vlan function so need to cast as bundle removing the incompatible keys. (Historic behavior)
                    bundle = bgp_vlan._cast_as(EosCliConfigGen.RouterBgp.VlanAwareBundlesItem, ignore_extra_keys=True)
                    bundle.name = bundle_name
                    bundle.vlan = list_compress([l2vlan.id for l2vlan in l2vlans])
                    self.structured_config.router_bgp.vlan_aware_bundles.append(bundle)

            # L2VLANs and SVIs which have an evpn_vlan_bundle defined
            for bundle_dict in l2vlan_svi_vlan_aware_bundles.values():
                evpn_vlan_bundle: EosDesigns.EvpnVlanBundlesItem = bundle_dict["evpn_vlan_bundle"]
                l2vlans_svis = bundle_dict["l2vlan_svis"]

                if (bundle := self._get_svi_l2vlan_bundle(evpn_vlan_bundle, tenant, l2vlans_svis)) is None:
                    # Skip bundle since no vlans were enabled for vxlan.
                    continue

                self.structured_config.router_bgp.vlan_aware_bundles.append(bundle)

    def _router_bgp_vlan_aware_bundles_vrf(
        self: AvdStructuredConfigNetworkServicesProtocol,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
        svis: list[EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem],
    ) -> EosCliConfigGen.RouterBgp.VlanAwareBundlesItem | None:
        """Return structured config for one vrf under router_bgp.vlan_aware_bundles."""
        return self._router_bgp_vlan_aware_bundle(
            name=vrf.name,
            vlans=svis,
            rd=self.get_vlan_aware_bundle_rd(id=self.shared_utils.get_vrf_id(vrf), tenant=tenant, is_vrf=True),
            rt=self.get_vlan_aware_bundle_rt(id=self.shared_utils.get_vrf_id(vrf), vni=self.shared_utils.get_vrf_vni(vrf), tenant=tenant, is_vrf=True),
            evpn_l2_multi_domain=default(vrf.evpn_l2_multi_domain, tenant.evpn_l2_multi_domain),
            tenant=tenant,
        )

    def _router_bgp_vlan_aware_bundle(
        self: AvdStructuredConfigNetworkServicesProtocol,
        name: str,
        vlans: list[EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem]
        | list[EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlansItem],
        rd: str,
        rt: str,
        evpn_l2_multi_domain: bool,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
    ) -> EosCliConfigGen.RouterBgp.VlanAwareBundlesItem | None:
        """
        Set structured config for one vlan-aware-bundle.

        Used for VRFs and bundles defined under "evpn_vlan_bundles" referred by l2vlans and SVIs.
        """
        vlans = [vlan for vlan in vlans if vlan.vxlan is not False]
        if not vlans:
            return None

        bundle = EosCliConfigGen.RouterBgp.VlanAwareBundlesItem(
            name=name,
            rd=rd,
            route_targets=EosCliConfigGen.RouterBgp.VlanAwareBundlesItem.RouteTargets(
                both=EosCliConfigGen.RouterBgp.VlanAwareBundlesItem.RouteTargets.Both([rt])
            ),
            redistribute_routes=EosCliConfigGen.RouterBgp.VlanAwareBundlesItem.RedistributeRoutes(["learned"]),
            vlan=list_compress([vlan.id for vlan in vlans]),
        )
        if self.shared_utils.node_config.evpn_gateway.evpn_l2.enabled and evpn_l2_multi_domain:
            bundle.rd_evpn_domain._update(domain="remote", rd=rd)
            bundle.route_targets.import_export_evpn_domains.append_new(domain="remote", route_target=rt)

        if any(default(vlan.evpn_l2_multicast.enabled, tenant.evpn_l2_multicast.enabled) for vlan in vlans):
            bundle.redistribute_routes.append("igmp")

        return bundle

    def _router_bgp_redistribute_routes(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Set structured config for router_bgp.redistribute.

        Add redistribute static to default if either "redistribute_in_overlay" is set or
        "redistribute_in_underlay" and underlay protocol is BGP.
        """
        if not (
            self._vrf_default_ipv4_static_routes["redistribute_in_overlay"]
            or (self._vrf_default_ipv4_static_routes["redistribute_in_underlay"] and self.shared_utils.underlay_bgp)
        ):
            return

        if self.shared_utils.wan_role:
            # For WAN routers we only wish to redistribute static routes defined under the tenants to BGP.
            if self._vrf_default_ipv4_static_routes["redistribute_in_overlay"]:
                self.structured_config.router_bgp.redistribute.static._update(enabled=True, route_map="RM-STATIC-2-BGP")
            return

        self.structured_config.router_bgp.redistribute.static.enabled = True

    def _router_bgp_vpws(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """Set structured config for router_bgp.vpws."""
        if not (self.shared_utils.network_services_l1 and self.shared_utils.overlay_ler and self.shared_utils.overlay_evpn_mpls):
            return

        for tenant in self.shared_utils.filtered_tenants:
            if not tenant.point_to_point_services or tenant.pseudowire_rt_base is None:
                continue

            pseudowires = EosCliConfigGen.RouterBgp.VpwsItem.Pseudowires()
            for point_to_point_service in tenant.point_to_point_services._natural_sorted():
                endpoints = point_to_point_service.endpoints
                for local_index, endpoint in enumerate(endpoints):
                    if self.shared_utils.hostname not in endpoint.nodes or not endpoint.interfaces:
                        continue

                    # Endpoints can only have two entries with index 0 and 1.
                    # So the remote must be the other index.
                    remote_endpoint = endpoints[(local_index + 1) % 2]

                    if point_to_point_service.subinterfaces:
                        for subif in point_to_point_service.subinterfaces:
                            pseudowires.append_new(
                                name=f"{point_to_point_service.name}_{subif.number}",
                                id_local=endpoint.id + subif.number,
                                id_remote=remote_endpoint.id + subif.number,
                            )
                    else:
                        pseudowires.append_new(
                            name=point_to_point_service.name,
                            id_local=endpoint.id,
                            id_remote=remote_endpoint.id,
                        )

            if pseudowires:
                rd = f"{self.shared_utils.overlay_rd_type_admin_subfield}:{tenant.pseudowire_rt_base}"
                rt = f"{self._rt_admin_subfield or tenant.pseudowire_rt_base}:{tenant.pseudowire_rt_base}"
                self.structured_config.router_bgp.vpws.append_new(
                    name=tenant.name,
                    rd=rd,
                    route_targets=EosCliConfigGen.RouterBgp.VpwsItem.RouteTargets(import_export=rt),
                    pseudowires=pseudowires,
                )
