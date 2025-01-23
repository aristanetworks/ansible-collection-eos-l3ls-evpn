# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from itertools import groupby as itertools_groupby

from pyavd._eos_designs.schema import EosDesigns
from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import AvdStringFormatter, append_if_not_duplicate, default, merge, strip_empties_from_dict
from pyavd.j2filters import list_compress

from .utils import UtilsMixin


class RouterBgpMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def router_bgp(self) -> dict | None:
        """
        Return the structured config for router_bgp.

        Changing legacy behavior is to only render this on vtep or mpls_ler
        by instead skipping vlans/bundles if not vtep or mpls_ler
        TODO: Fix so this also works for L2LS with VRFs
        """
        if not self.shared_utils.bgp:
            return None

        tenant_svis_l2vlans_dict = self._router_bgp_sorted_vlans_and_svis_lists()

        router_bgp = {}
        merge(
            router_bgp,
            self._router_bgp_peer_groups(),
            self._router_bgp_vrfs,
            # stripping empties here to avoid overwriting keys with None values.
            strip_empties_from_dict(
                {
                    "vlans": self._router_bgp_vlans(tenant_svis_l2vlans_dict),
                    "vlan_aware_bundles": self._router_bgp_vlan_aware_bundles(tenant_svis_l2vlans_dict),
                    "redistribute": self._router_bgp_redistribute_routes,
                    "vpws": self._router_bgp_vpws,
                }
            ),
        )
        # Configure MLAG iBGP peer-group if needed
        if self._configure_bgp_mlag_peer_group:
            merge(router_bgp, self._router_bgp_mlag_peer_group())

        # Strip None values from vlan before returning
        return {key: value for key, value in router_bgp.items() if value is not None}

    def _router_bgp_peer_groups(self) -> dict:
        """
        Return the structured config for router_bgp.peer_groups.

        Covers two areas:
        - bgp_peer_groups defined under the vrf including ipv4/ipv6 address_families.
        - adding route-map to the underlay peer-group in case of services in vrf default
        """
        if not self.shared_utils.network_services_l3:
            return {}

        peer_groups: list[EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.BgpPeerGroupsItem] = []
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

        router_bgp = {"peer_groups": []}
        for peer_group in peer_groups:
            peer_group_dict = peer_group._as_dict()
            peer_group_dict.pop("nodes", None)
            for af in ["address_family_ipv4", "address_family_ipv6"]:
                if not (af_peer_group := peer_group_dict.pop(af, None)):
                    continue
                af_peer_groups = router_bgp.setdefault(af, {"peer_groups": []})["peer_groups"]
                append_if_not_duplicate(
                    primary_key="name",
                    list_of_dicts=af_peer_groups,
                    new_dict={"name": peer_group_dict["name"], **af_peer_group},
                    context=f"BGP Peer Groups for '{af}' defined under network services",
                    context_keys=["name"],
                )
            append_if_not_duplicate(
                list_of_dicts=router_bgp["peer_groups"],
                primary_key="name",
                new_dict=peer_group_dict,
                context="BGP Peer Groups defined under network services",
                context_keys=["name"],
            )

        # router bgp default vrf configuration for evpn
        if self._vrf_default_evpn and (self._vrf_default_ipv4_subnets or self._vrf_default_ipv4_static_routes["static_routes"]):
            router_bgp["peer_groups"].append(
                {
                    "name": self.inputs.bgp_peer_groups.ipv4_underlay_peers.name,
                    "type": "ipv4",
                    "route_map_out": "RM-BGP-UNDERLAY-PEERS-OUT",
                },
            )

        return strip_empties_from_dict(router_bgp)

    def _router_bgp_sorted_vlans_and_svis_lists(self) -> dict:
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

    def _router_bgp_vlans(self, tenant_svis_l2vlans_dict: dict) -> list | None:
        """Return structured config for router_bgp.vlans."""
        if not (
            self.shared_utils.network_services_l2
            and "evpn" in self.shared_utils.overlay_address_families
            and not self.inputs.evpn_vlan_aware_bundles
            and (self.shared_utils.overlay_vtep or self.shared_utils.overlay_ler)
            and (self.shared_utils.overlay_evpn)
        ):
            return None

        vlans = []
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                for svi in tenant_svis_l2vlans_dict[tenant.name]["svi_non_bundle"][vrf.name]:
                    if (vlan := self._router_bgp_vlans_vlan(svi, tenant, vrf)) is not None:
                        append_if_not_duplicate(
                            list_of_dicts=vlans,
                            primary_key="id",
                            new_dict=vlan,
                            context="BGP VLANs defined under network services",
                            context_keys=["id", "tenant"],
                            ignore_keys={"tenant"},
                        )

            # L2 Vlans per Tenant
            for l2vlans in tenant_svis_l2vlans_dict[tenant.name]["l2vlan_non_bundle"].values():
                for l2vlan in l2vlans:
                    if (
                        vlan := self._router_bgp_vlans_vlan(
                            l2vlan, tenant, vrf=EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem()
                        )
                    ) is not None:
                        append_if_not_duplicate(
                            list_of_dicts=vlans,
                            primary_key="id",
                            new_dict=vlan,
                            context="BGP VLANs defined under network services",
                            context_keys=["id", "tenant"],
                            ignore_keys={"tenant"},
                        )
        return vlans or None

    def _router_bgp_vlans_vlan(
        self,
        vlan: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem
        | EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlansItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
    ) -> dict | None:
        """Return structured config for one given vlan under router_bgp.vlans."""
        if not vlan.vxlan:
            return None

        vlan_rd = self.get_vlan_rd(vlan, tenant)
        vlan_rt = self.get_vlan_rt(vlan, tenant)

        bgp_vlan = {
            "id": vlan.id,
            "tenant": tenant.name,
            "rd": vlan_rd,
            "route_targets": {"both": [vlan_rt]},
            "redistribute_routes": ["learned"],
            "eos_cli": vlan.bgp.raw_eos_cli,
        }

        if vlan.bgp.structured_config:
            self.custom_structured_configs.nested.router_bgp.vlans.obtain(vlan.id)._deepmerge(
                vlan.bgp.structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
            )

        if self.shared_utils.node_config.evpn_gateway.evpn_l2.enabled and default(
            vlan.evpn_l2_multi_domain, vrf.evpn_l2_multi_domain, tenant.evpn_l2_multi_domain
        ):
            bgp_vlan["rd_evpn_domain"] = {"domain": "remote", "rd": vlan_rd}
            bgp_vlan["route_targets"]["import_export_evpn_domains"] = [{"domain": "remote", "route_target": vlan_rt}]

        vlan_evpn_l2_multicast_enabled = default(vlan.evpn_l2_multicast.enabled, tenant.evpn_l2_multicast.enabled) and self.shared_utils.evpn_multicast is True
        if vlan_evpn_l2_multicast_enabled:
            if isinstance(vlan, EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlansItem):
                # l2vlans will always redistribute IGMP
                bgp_vlan["redistribute_routes"].append("igmp")
            elif not getattr(vrf, "_evpn_l3_multicast_enabled", False) or bool(
                default(vlan.evpn_l2_multicast.always_redistribute_igmp, tenant.evpn_l2_multicast.always_redistribute_igmp)
            ):
                bgp_vlan["redistribute_routes"].append("igmp")

        # Strip None values from vlan before returning
        return {key: value for key, value in bgp_vlan.items() if value is not None}

    def _get_vlan_aware_bundle_name_tuple_for_l2vlans(
        self, vlan: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlansItem
    ) -> tuple[str, bool] | None:
        """Return a tuple with string with the vlan-aware-bundle name for one VLAN and a boolean saying if this is a evpn_vlan_bundle."""
        if vlan.evpn_vlan_bundle:
            return (vlan.evpn_vlan_bundle, True)
        return (vlan.name, False)

    def _get_vlan_aware_bundle_name_tuple_for_svis(
        self, vlan: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem
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
        self,
        vlan: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem
        | EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlansItem,
        bundle_name: str,
    ) -> EosDesigns.EvpnVlanBundlesItem:
        """Return an evpn_vlan_bundle dict if it exists, else raise an exception."""
        if bundle_name not in self.inputs.evpn_vlan_bundles:
            msg = (
                "The 'evpn_vlan_bundle' of the svis/l2vlans must be defined in the common 'evpn_vlan_bundles' setting. First occurrence seen for svi/l2vlan"
                f" {vlan.id} in Tenant '{vlan._tenant}' and evpn_vlan_bundle '{vlan.evpn_vlan_bundle}'."
            )
            raise AristaAvdInvalidInputsError(msg)
        return self.inputs.evpn_vlan_bundles[bundle_name]

    def _get_svi_l2vlan_bundle(
        self,
        evpn_vlan_bundle: EosDesigns.EvpnVlanBundlesItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
        vlans: list,
    ) -> dict | None:
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
                bundle["eos_cli"] = eos_cli
            return bundle

        return None

    def _router_bgp_vlan_aware_bundles(self, tenant_svis_l2vlans_dict: dict) -> list | None:
        """Return structured config for router_bgp.vlan_aware_bundles."""
        if not self.shared_utils.network_services_l2 or not self.shared_utils.overlay_evpn:
            return None

        bundles = []
        for tenant in self.shared_utils.filtered_tenants:
            l2vlan_svi_vlan_aware_bundles = {}
            for vrf in tenant.vrfs:
                for bundle_name, svis in tenant_svis_l2vlans_dict[tenant.name]["svi_bundle"][vrf.name].items():
                    # SVIs which have an evpn_vlan_bundle defined
                    if bundle_name in l2vlan_svi_vlan_aware_bundles:
                        l2vlan_svi_vlan_aware_bundles[bundle_name]["l2vlan_svis"].extend(svis)
                    else:
                        # check if the referred name exists in the global evpn_vlan_bundles
                        evpn_vlan_bundle = self._get_evpn_vlan_bundle(svis[0], bundle_name)
                        l2vlan_svi_vlan_aware_bundles[bundle_name] = {"evpn_vlan_bundle": evpn_vlan_bundle, "l2vlan_svis": svis}

                if self.inputs.evpn_vlan_aware_bundles:
                    svis = tenant_svis_l2vlans_dict[tenant.name]["svi_non_bundle"][vrf.name]
                    # SVIs which don't have an evpn_vlan_bundle defined are included in the VRF vlan-aware-bundle
                    if (bundle := self._router_bgp_vlan_aware_bundles_vrf(vrf, tenant, svis)) is not None:
                        append_if_not_duplicate(
                            list_of_dicts=bundles,
                            primary_key="name",
                            new_dict=bundle,
                            context="BGP VLAN-Aware Bundles defined under network services",
                            context_keys=["name"],
                        )

            # L2 Vlans per Tenant
            # If multiple L2 Vlans share the same evpn_vlan_bundle name, they will be part of the same vlan-aware-bundle else they use the vlan name as bundle
            for bundle_name, l2vlans in tenant_svis_l2vlans_dict[tenant.name]["l2vlan_bundle"].items():
                if bundle_name in l2vlan_svi_vlan_aware_bundles:
                    l2vlan_svi_vlan_aware_bundles[bundle_name]["l2vlan_svis"].extend(l2vlans)
                else:
                    # check if the referred name exists in the global evpn_vlan_bundles
                    evpn_vlan_bundle = self._get_evpn_vlan_bundle(l2vlans[0], bundle_name)
                    l2vlan_svi_vlan_aware_bundles[bundle_name] = {"evpn_vlan_bundle": evpn_vlan_bundle, "l2vlan_svis": l2vlans}

            if self.inputs.evpn_vlan_aware_bundles:
                for bundle_name, l2vlans in tenant_svis_l2vlans_dict[tenant.name]["l2vlan_non_bundle"].items():
                    # Without "evpn_vlan_bundle" we fall back to per-vlan behavior
                    if (
                        bundle := self._router_bgp_vlans_vlan(
                            l2vlans[0], tenant, vrf=EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem()
                        )
                    ) is None:
                        # Skip bundle since no vlans were enabled for vxlan.
                        continue

                    # We are reusing the regular bgp vlan function so need to add vlan info and remove the vlan id.
                    bundle.pop("id")
                    bundle["vlan"] = list_compress([l2vlan.id for l2vlan in l2vlans])
                    bundle = {"name": bundle_name, **bundle}
                    append_if_not_duplicate(
                        list_of_dicts=bundles,
                        primary_key="name",
                        new_dict=bundle,
                        context=(
                            "BGP VLAN-Aware Bundles defined under network services. A common reason is that an 'l2vlan' name overlaps with an"
                            " 'evpn_vlan_bundle' name"
                        ),
                        context_keys=["name"],
                    )

            # L2VLANs and SVIs which have an evpn_vlan_bundle defined
            for bundle_dict in l2vlan_svi_vlan_aware_bundles.values():
                evpn_vlan_bundle: EosDesigns.EvpnVlanBundlesItem = bundle_dict["evpn_vlan_bundle"]
                l2vlans_svis = bundle_dict["l2vlan_svis"]

                if (bundle := self._get_svi_l2vlan_bundle(evpn_vlan_bundle, tenant, l2vlans_svis)) is None:
                    # Skip bundle since no vlans were enabled for vxlan.
                    continue

                append_if_not_duplicate(
                    list_of_dicts=bundles,
                    primary_key="name",
                    new_dict=bundle,
                    context=(
                        "BGP VLAN-Aware Bundles defined under network services. A common reason is that an 'l2vlan' or 'svi' name overlaps with an"
                        " 'evpn_vlan_bundle' name"
                    ),
                    context_keys=["name"],
                )

        return bundles or None

    def _router_bgp_vlan_aware_bundles_vrf(
        self,
        vrf: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
        svis: list[EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem],
    ) -> dict | None:
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
        self,
        name: str,
        vlans: list[EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.VrfsItem.SvisItem]
        | list[EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem.L2vlansItem],
        rd: str,
        rt: str,
        evpn_l2_multi_domain: bool,
        tenant: EosDesigns._DynamicKeys.DynamicNetworkServicesItem.NetworkServicesItem,
    ) -> dict | None:
        """
        Return structured config for one vlan-aware-bundle.

        Used for VRFs and bundles defined under "evpn_vlan_bundles" referred by l2vlans and SVIs.
        """
        vlans = [vlan for vlan in vlans if vlan.vxlan is not False]
        if not vlans:
            return None

        bundle = {
            "name": name,
            "rd": rd,
            "route_targets": {
                "both": [rt],
            },
            "redistribute_routes": ["learned"],
            "vlan": list_compress([vlan.id for vlan in vlans]),
        }
        if self.shared_utils.node_config.evpn_gateway.evpn_l2.enabled and evpn_l2_multi_domain:
            bundle["rd_evpn_domain"] = {"domain": "remote", "rd": rd}
            bundle["route_targets"]["import_export_evpn_domains"] = [{"domain": "remote", "route_target": rt}]

        if any(default(vlan.evpn_l2_multicast.enabled, tenant.evpn_l2_multicast.enabled) for vlan in vlans):
            bundle["redistribute_routes"].append("igmp")

        return bundle

    @cached_property
    def _router_bgp_redistribute_routes(self) -> dict | None:
        """
        Return structured config for router_bgp.redistribute.

        Add redistribute static to default if either "redistribute_in_overlay" is set or
        "redistribute_in_underlay" and underlay protocol is BGP.
        """
        if not (
            self._vrf_default_ipv4_static_routes["redistribute_in_overlay"]
            or (self._vrf_default_ipv4_static_routes["redistribute_in_underlay"] and self.shared_utils.underlay_bgp)
        ):
            return None

        if self.shared_utils.wan_role:
            # For WAN routers we only wish to redistribute static routes defined under the tenants to BGP.
            if self._vrf_default_ipv4_static_routes["redistribute_in_overlay"]:
                return {"static": {"enabled": True, "route_map": "RM-STATIC-2-BGP"}}
            return None

        return {"static": {"enabled": True}}

    @cached_property
    def _router_bgp_vpws(self) -> list[dict] | None:
        """Return structured config for router_bgp.vpws."""
        if not (self.shared_utils.network_services_l1 and self.shared_utils.overlay_ler and self.shared_utils.overlay_evpn_mpls):
            return None

        vpws = []
        for tenant in self.shared_utils.filtered_tenants:
            if not tenant.point_to_point_services or tenant.pseudowire_rt_base is None:
                continue

            pseudowires = []
            for point_to_point_service in tenant.point_to_point_services._natural_sorted():
                endpoints = point_to_point_service.endpoints
                for local_index, endpoint in enumerate(endpoints):
                    if self.shared_utils.hostname not in endpoint.nodes or not endpoint.interfaces:
                        continue

                    # Endpoints can only have two entries with index 0 and 1.
                    # So the remote must be the other index.
                    remote_endpoint = endpoints[(local_index + 1) % 2]

                    if point_to_point_service.subinterfaces:
                        pseudowires.extend(
                            {
                                "name": f"{point_to_point_service.name}_{subif.number}",
                                "id_local": endpoint.id + subif.number,
                                "id_remote": remote_endpoint.id + subif.number,
                            }
                            for subif in point_to_point_service.subinterfaces
                        )

                    else:
                        pseudowires.append(
                            {
                                "name": point_to_point_service.name,
                                "id_local": endpoint.id,
                                "id_remote": remote_endpoint.id,
                            },
                        )

            if pseudowires:
                rd = f"{self.shared_utils.overlay_rd_type_admin_subfield}:{tenant.pseudowire_rt_base}"
                rt = f"{self._rt_admin_subfield or tenant.pseudowire_rt_base}:{tenant.pseudowire_rt_base}"
                vpws.append(
                    {
                        "name": tenant.name,
                        "rd": rd,
                        "route_targets": {"import_export": rt},
                        "pseudowires": pseudowires,
                    },
                )

        if vpws:
            return vpws

        return None

    def _router_bgp_mlag_peer_group(self) -> dict:
        """
        Return a partial router_bgp structured_config covering the MLAG peer_group and associated address_family activations.

        TODO: Partially duplicated from mlag. Should be moved to a common class
        """
        peer_group_name = self.inputs.bgp_peer_groups.mlag_ipv4_underlay_peer.name
        router_bgp = {}
        peer_group = {
            "name": peer_group_name,
            "type": "ipv4",
            "remote_as": self.shared_utils.bgp_as,
            "next_hop_self": True,
            "description": AvdStringFormatter().format(self.inputs.mlag_bgp_peer_group_description, mlag_peer=self.shared_utils.mlag_peer),
            "password": self.inputs.bgp_peer_groups.mlag_ipv4_underlay_peer.password,
            "maximum_routes": 12000,
            "send_community": "all",
        }

        if self.inputs.bgp_peer_groups.mlag_ipv4_underlay_peer.structured_config:
            self.custom_structured_configs.nested.router_bgp.peer_groups.obtain(peer_group_name)._deepmerge(
                self.inputs.bgp_peer_groups.mlag_ipv4_underlay_peer.structured_config, list_merge=self.custom_structured_configs.list_merge_strategy
            )

        if self.shared_utils.node_config.mlag_ibgp_origin_incomplete:
            peer_group["route_map_in"] = "RM-MLAG-PEER-IN"

        router_bgp["peer_groups"] = [peer_group]

        if self.shared_utils.underlay_ipv6:
            router_bgp["address_family_ipv6"] = {
                "peer_groups": [
                    {
                        "name": peer_group_name,
                        "activate": True,
                    },
                ],
            }

        address_family_ipv4_peer_group = {"name": peer_group_name, "activate": True}
        if self.inputs.underlay_rfc5549:
            address_family_ipv4_peer_group["next_hop"] = {"address_family_ipv6": {"enabled": True, "originate": True}}

        router_bgp["address_family_ipv4"] = {"peer_groups": [address_family_ipv4_peer_group]}
        return strip_empties_from_dict(router_bgp)
