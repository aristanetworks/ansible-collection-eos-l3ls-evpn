# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import ipaddress
from functools import cached_property
from itertools import groupby as itertools_groupby
from re import fullmatch as re_fullmatch
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import AvdStringFormatter, append_if_not_duplicate, default, get, get_item, merge, strip_empties_from_dict
from pyavd.j2filters import list_compress, natural_sort

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class RouterBgpMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def router_bgp(self: AvdStructuredConfigNetworkServices) -> dict | None:
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

    def _router_bgp_peer_groups(self: AvdStructuredConfigNetworkServices) -> dict:
        """
        Return the structured config for router_bgp.peer_groups.

        Covers two areas:
        - bgp_peer_groups defined under the vrf including ipv4/ipv6 address_families.
        - adding route-map to the underlay peer-group in case of services in vrf default
        """
        if not self.shared_utils.network_services_l3:
            return {}

        peer_groups = []
        peer_peergroups = set()
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant["vrfs"]:
                # bgp_peers is already filtered in filtered_tenants to only contain entries with our hostname
                if not (vrf["bgp_peers"] or vrf.get("bgp_peer_groups")):
                    continue

                vrf_peer_peergroups = {peer["peer_group"] for peer in vrf["bgp_peers"] if "peer_group" in peer}
                peer_groups.extend(
                    [
                        peer_group
                        for peer_group in vrf.get("bgp_peer_groups", [])
                        if (self.shared_utils.hostname in peer_group.get("nodes", []) or peer_group["name"] in vrf_peer_peergroups)
                    ],
                )
                peer_peergroups.update(vrf_peer_peergroups)

            peer_groups.extend(
                [
                    peer_group
                    for peer_group in tenant.get("bgp_peer_groups", [])
                    if (self.shared_utils.hostname in peer_group.get("nodes", []) or peer_group["name"] in peer_peergroups)
                ],
            )

        router_bgp = {"peer_groups": []}
        if peer_groups:
            for peer_group in peer_groups:
                peer_group.pop("nodes", None)
                for af in ["address_family_ipv4", "address_family_ipv6"]:
                    if not (af_peer_group := peer_group.pop(af, None)):
                        continue
                    af_peer_groups = router_bgp.setdefault(af, {"peer_groups": []})["peer_groups"]
                    append_if_not_duplicate(
                        primary_key="name",
                        list_of_dicts=af_peer_groups,
                        new_dict={"name": peer_group["name"], **af_peer_group},
                        context=f"BGP Peer Groups for '{af}' defined under network services",
                        context_keys=["name"],
                    )
                append_if_not_duplicate(
                    list_of_dicts=router_bgp["peer_groups"],
                    primary_key="name",
                    new_dict=peer_group,
                    context="BGP Peer Groups defined under network services",
                    context_keys=["name"],
                )

        # router bgp default vrf configuration for evpn
        if self._vrf_default_evpn and (self._vrf_default_ipv4_subnets or self._vrf_default_ipv4_static_routes["static_routes"]):
            router_bgp["peer_groups"].append(
                {
                    "name": self.shared_utils.bgp_peer_groups["ipv4_underlay_peers"]["name"],
                    "type": "ipv4",
                    "route_map_out": "RM-BGP-UNDERLAY-PEERS-OUT",
                },
            )

        return strip_empties_from_dict(router_bgp)

    @cached_property
    def _router_bgp_vrfs(self: AvdStructuredConfigNetworkServices) -> dict:
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
            for vrf in tenant["vrfs"]:
                if not self.shared_utils.bgp_enabled_for_vrf(vrf):
                    continue

                vrf_name = vrf["name"]
                bgp_vrf = strip_empties_from_dict(
                    {
                        "eos_cli": get(vrf, "bgp.raw_eos_cli"),
                        "struct_cfg": get(vrf, "bgp.structured_config"),
                    }
                )

                if vrf_address_families := [af for af in vrf.get("address_families", ["evpn"]) if af in self.shared_utils.overlay_address_families]:
                    # The called function in-place updates the bgp_vrf dict.
                    self._update_router_bgp_vrf_evpn_or_mpls_cfg(bgp_vrf, vrf, vrf_address_families)

                bgp_vrf_redistribute_connected = get(vrf, "redistribute_connected", default=True)
                if vrf_name != "default":
                    # Non-default VRF
                    bgp_vrf["router_id"] = self.shared_utils.router_id
                    if bgp_vrf_redistribute_connected is True:
                        bgp_vrf["redistribute"] = {"connected": {"enabled": True}}
                    # Redistribution of static routes for VRF default are handled elsewhere
                    # since there is a choice between redistributing to underlay or overlay.
                    if (bgp_vrf_redistribute_static := vrf.get("redistribute_static")) is True or (
                        vrf["static_routes"] and bgp_vrf_redistribute_static is not False
                    ):
                        bgp_vrf["redistribute"].update({"static": {"enabled": True}})

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

                for bgp_peer in vrf["bgp_peers"]:
                    # Below we pop various keys that are not supported by the eos_cli_config_gen schema.
                    # The rest of the keys are relayed directly to eos_cli_config_gen.
                    # 'ip_address' is popped even though it is supported. It will be added again later
                    # to ensure it comes first in the generated dict.
                    peer_ip = bgp_peer.pop("ip_address")
                    address_family = f"address_family_ipv{ipaddress.ip_address(peer_ip).version}"
                    neighbor = strip_empties_from_dict(
                        {
                            "ip_address": peer_ip,
                            "activate": True,
                            "prefix_list_in": bgp_peer.pop("prefix_list_in", None),
                            "prefix_list_out": bgp_peer.pop("prefix_list_out", None),
                        },
                    )

                    append_if_not_duplicate(
                        list_of_dicts=bgp_vrf.setdefault(address_family, {}).setdefault("neighbors", []),
                        primary_key="ip_address",
                        new_dict=neighbor,
                        context="BGP peer defined under VRFs",
                        context_keys=["ip_address"],
                    )

                    if bgp_peer.get("set_ipv4_next_hop") is not None or bgp_peer.get("set_ipv6_next_hop") is not None:
                        route_map = f"RM-{vrf_name}-{peer_ip}-SET-NEXT-HOP-OUT"
                        bgp_peer["route_map_out"] = route_map
                        if bgp_peer.get("default_originate") is not None:
                            bgp_peer["default_originate"]["route_map"] = bgp_peer["default_originate"].get("route_map", route_map)

                        bgp_peer.pop("set_ipv4_next_hop", None)
                        bgp_peer.pop("set_ipv6_next_hop", None)

                    bgp_peer.pop("nodes", None)

                    append_if_not_duplicate(
                        list_of_dicts=bgp_vrf.setdefault("neighbors", []),
                        primary_key="ip_address",
                        new_dict={"ip_address": peer_ip, **bgp_peer},
                        context="BGP peer defined under VRFs",
                        context_keys=["ip_address"],
                    )

                if (
                    get(vrf, "ospf.enabled") is True
                    and vrf.get("redistribute_ospf") is not False
                    and self.shared_utils.hostname in get(vrf, "ospf.nodes", default=[self.shared_utils.hostname])
                ):
                    bgp_vrf.setdefault("redistribute", {}).update({"ospf": {"enabled": True}})

                if bgp_vrf.get("neighbors"):
                    platform_bgp_update_wait_install = get(self.shared_utils.platform_settings, "feature_support.bgp_update_wait_install", default=True) is True
                    if get(self._hostvars, "bgp_update_wait_install", default=True) is True and platform_bgp_update_wait_install:
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

    def _update_router_bgp_vrf_evpn_or_mpls_cfg(self: AvdStructuredConfigNetworkServices, bgp_vrf: dict, vrf: dict, vrf_address_families: list) -> None:
        """In-place update EVPN/MPLS part of structured config for *one* VRF under router_bgp.vrfs."""
        vrf_name = vrf["name"]
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

        for rt in vrf["additional_route_targets"]:
            if (target := get_item(route_targets[rt["type"]], "address_family", rt["address_family"])) is None:
                route_targets[rt["type"]].append({"address_family": rt["address_family"], "route_targets": [rt["route_target"]]})
            else:
                target["route_targets"].append(rt["route_target"])

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
        bgp_vrf["evpn_multicast"] = get(vrf, "_evpn_l3_multicast_enabled")
        if (evpn_multicast_transit_mode := get(vrf, "_evpn_l3_multicast_evpn_peg_transit")) is True:
            bgp_vrf["evpn_multicast_address_family"] = {"ipv4": {"transit": evpn_multicast_transit_mode}}

    def _update_router_bgp_vrf_mlag_neighbor_cfg(self: AvdStructuredConfigNetworkServices, bgp_vrf: dict, vrf: dict, tenant: dict, vlan_id: int) -> None:
        """In-place update MLAG neighbor part of structured config for *one* VRF under router_bgp.vrfs."""
        if self._exclude_mlag_ibgp_peering_from_redistribute(vrf, tenant):
            bgp_vrf["redistribute"]["connected"] = {"enabled": True, "route_map": "RM-CONN-2-BGP-VRFS"}

        interface_name = f"Vlan{vlan_id}"
        if self.shared_utils.underlay_rfc5549 and self.shared_utils.overlay_mlag_rfc5549:
            bgp_vrf.setdefault("neighbor_interfaces", []).append(
                {
                    "name": interface_name,
                    "peer_group": self.shared_utils.bgp_peer_groups["mlag_ipv4_underlay_peer"]["name"],
                    "remote_as": self.shared_utils.bgp_as,
                    "description": AvdStringFormatter().format(
                        self.shared_utils.mlag_bgp_peer_description,
                        mlag_peer=self.shared_utils.mlag_peer,
                        interface=interface_name,
                        peer_interface=interface_name,
                    ),
                },
            )
        else:
            if (mlag_ibgp_peering_ipv4_pool := vrf.get("mlag_ibgp_peering_ipv4_pool")) is None:
                ip_address = self.shared_utils.mlag_peer_ibgp_ip
            elif self.shared_utils.mlag_role == "primary":
                ip_address = self.shared_utils.ip_addressing.mlag_ibgp_peering_ip_secondary(mlag_ibgp_peering_ipv4_pool)
            else:
                ip_address = self.shared_utils.ip_addressing.mlag_ibgp_peering_ip_primary(mlag_ibgp_peering_ipv4_pool)

            bgp_vrf.setdefault("neighbors", []).append(
                {
                    "ip_address": ip_address,
                    "peer_group": self.shared_utils.bgp_peer_groups["mlag_ipv4_underlay_peer"]["name"],
                    "description": AvdStringFormatter().format(
                        self.shared_utils.mlag_bgp_peer_description,
                        **strip_empties_from_dict(
                            {"mlag_peer": self.shared_utils.mlag_peer, "interface": interface_name, "peer_interface": interface_name, "vrf": vrf["name"]}
                        ),
                    ),
                },
            )
            if self.shared_utils.underlay_rfc5549:
                bgp_vrf.setdefault("address_family_ipv4", {}).setdefault("neighbors", []).append(
                    {
                        "ip_address": ip_address,
                        "next_hop": {
                            "address_family_ipv6": {"enabled": False},
                        },
                    },
                )

    def _router_bgp_sorted_vlans_and_svis_lists(self: AvdStructuredConfigNetworkServices) -> dict:
        tenant_svis_l2vlans_dict = {}
        for tenant in self.shared_utils.filtered_tenants:
            tenant_svis_l2vlans_dict[tenant["name"]] = {}

            # For L2VLANs
            l2vlans_bundle_dict = {}
            l2vlans_non_bundle_list = {}
            sorted_vlan_list = sorted(tenant["l2vlans"], key=self._get_vlan_aware_bundle_name_tuple_for_l2vlans)
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
            for vrf in tenant["vrfs"]:
                vrf_svis_non_bundle_dict[vrf["name"]] = []
                vrf_svis_bundle_dict[vrf["name"]] = {}
                sorted_svi_list = sorted(vrf["svis"], key=self._get_vlan_aware_bundle_name_tuple_for_svis)
                bundle_groups_svis = itertools_groupby(sorted_svi_list, self._get_vlan_aware_bundle_name_tuple_for_svis)
                for vlan_aware_bundle_name_tuple, svis in bundle_groups_svis:
                    bundle_name, is_evpn_vlan_bundle = vlan_aware_bundle_name_tuple
                    svis_list = list(svis)

                    if is_evpn_vlan_bundle:
                        vrf_svis_bundle_dict[vrf["name"]][bundle_name] = svis_list
                    else:
                        vrf_svis_non_bundle_dict[vrf["name"]] = svis_list

            tenant_svis_l2vlans_dict[tenant["name"]]["svi_bundle"] = vrf_svis_bundle_dict
            tenant_svis_l2vlans_dict[tenant["name"]]["svi_non_bundle"] = vrf_svis_non_bundle_dict
            tenant_svis_l2vlans_dict[tenant["name"]]["l2vlan_bundle"] = l2vlans_bundle_dict
            tenant_svis_l2vlans_dict[tenant["name"]]["l2vlan_non_bundle"] = l2vlans_non_bundle_list

        return tenant_svis_l2vlans_dict

    def _router_bgp_vlans(self: AvdStructuredConfigNetworkServices, tenant_svis_l2vlans_dict: dict) -> list | None:
        """Return structured config for router_bgp.vlans."""
        if not (
            self.shared_utils.network_services_l2
            and "evpn" in self.shared_utils.overlay_address_families
            and not self._evpn_vlan_aware_bundles
            and (self.shared_utils.overlay_vtep or self.shared_utils.overlay_ler)
            and (self.shared_utils.overlay_evpn)
        ):
            return None

        vlans = []
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant["vrfs"]:
                for svi in tenant_svis_l2vlans_dict[tenant["name"]]["svi_non_bundle"][vrf["name"]]:
                    if (vlan := self._router_bgp_vlans_vlan(svi, tenant, vrf)) is not None:
                        vlan_id = int(svi["id"])
                        vlan = {"id": vlan_id, **vlan}
                        append_if_not_duplicate(
                            list_of_dicts=vlans,
                            primary_key="id",
                            new_dict=vlan,
                            context="BGP VLANs defined under network services",
                            context_keys=["id", "tenant"],
                            ignore_keys={"tenant"},
                        )

            # L2 Vlans per Tenant
            for l2vlans in tenant_svis_l2vlans_dict[tenant["name"]]["l2vlan_non_bundle"].values():
                for l2vlan in l2vlans:
                    if (vlan := self._router_bgp_vlans_vlan(l2vlan, tenant, vrf={})) is not None:
                        vlan_id = int(l2vlan["id"])
                        vlan = {"id": vlan_id, **vlan}
                        append_if_not_duplicate(
                            list_of_dicts=vlans,
                            primary_key="id",
                            new_dict=vlan,
                            context="BGP VLANs defined under network services",
                            context_keys=["id", "tenant"],
                            ignore_keys={"tenant"},
                        )
        return vlans or None

    def _router_bgp_vlans_vlan(self: AvdStructuredConfigNetworkServices, vlan: dict, tenant: dict, vrf: dict) -> dict | None:
        """Return structured config for one given vlan under router_bgp.vlans."""
        if vlan.get("vxlan") is False:
            return None

        vlan_rd = self.get_vlan_rd(vlan, tenant)
        vlan_rt = self.get_vlan_rt(vlan, tenant)

        bgp_vlan = {
            "tenant": vlan["tenant"],
            "rd": vlan_rd,
            "route_targets": {"both": [vlan_rt]},
            "redistribute_routes": ["learned"],
            "eos_cli": get(vlan, "bgp.raw_eos_cli"),
            "struct_cfg": get(vlan, "bgp.structured_config"),
        }
        if (
            self.shared_utils.evpn_gateway_vxlan_l2
            and default(vlan.get("evpn_l2_multi_domain"), vrf.get("evpn_l2_multi_domain"), tenant.get("evpn_l2_multi_domain"), True) is True  # noqa: FBT003
        ):
            bgp_vlan["rd_evpn_domain"] = {"domain": "remote", "rd": vlan_rd}
            bgp_vlan["route_targets"]["import_export_evpn_domains"] = [{"domain": "remote", "route_target": vlan_rt}]

        vlan_evpn_l2_multicast_enabled = (
            default(get(vlan, "evpn_l2_multicast.enabled"), get(tenant, "evpn_l2_multicast.enabled")) and self.shared_utils.evpn_multicast is True
        )
        if vlan_evpn_l2_multicast_enabled is True:
            always_redistribute_igmp = default(
                get(vlan, "evpn_l2_multicast.always_redistribute_igmp"),
                get(tenant, "evpn_l2_multicast.always_redistribute_igmp"),
                False,  # noqa: FBT003
            )
            # For l2vlans vrf is an empty dict so this will always configure redistribute igmp
            if not get(vrf, "_evpn_l3_multicast_enabled") or always_redistribute_igmp:
                bgp_vlan["redistribute_routes"].append("igmp")

        # Strip None values from vlan before returning
        return {key: value for key, value in bgp_vlan.items() if value is not None}

    @cached_property
    def _evpn_vlan_bundles(self: AvdStructuredConfigNetworkServices) -> list:
        return get(self._hostvars, "evpn_vlan_bundles", default=[])

    @cached_property
    def _evpn_vlan_aware_bundles(self: AvdStructuredConfigNetworkServices) -> bool:
        return get(self._hostvars, "evpn_vlan_aware_bundles", default=False)

    def _get_vlan_aware_bundle_name_tuple_for_l2vlans(self: AvdStructuredConfigNetworkServices, vlan: dict) -> tuple[str, bool] | None:
        """Return a tuple with string with the vlan-aware-bundle name for one VLAN and a boolean saying if this is a evpn_vlan_bundle."""
        if vlan.get("evpn_vlan_bundle") is not None:
            return (str(vlan.get("evpn_vlan_bundle")), True)
        return (str(vlan.get("name")), False)

    def _get_vlan_aware_bundle_name_tuple_for_svis(self: AvdStructuredConfigNetworkServices, vlan: dict) -> tuple[str, bool] | None:
        """
        Return a tuple with string with the vlan-aware-bundle name for one VLAN and a boolean saying if this is a evpn_vlan_bundle.

        If no bundle is configured, it will return an empty string as name, since the calling function will then get all svis without bundle
        grouped under "".
        """
        if vlan.get("evpn_vlan_bundle") is not None:
            return (str(vlan.get("evpn_vlan_bundle")), True)
        return ("", False)

    def _get_evpn_vlan_bundle(self: AvdStructuredConfigNetworkServices, vlan: dict, bundle_name: str) -> dict:
        """Return an evpn_vlan_bundle dict if it exists, else raise an exception."""
        if (evpn_vlan_bundle := get_item(self._evpn_vlan_bundles, "name", bundle_name)) is None:
            msg = (
                "The 'evpn_vlan_bundle' of the svis/l2vlans must be defined in the common 'evpn_vlan_bundles' setting. First occurrence seen for svi/l2vlan"
                f" {vlan['id']} in Tenant '{vlan['tenant']}' and evpn_vlan_bundle '{vlan['evpn_vlan_bundle']}'."
            )
            raise AristaAvdInvalidInputsError(msg)
        return evpn_vlan_bundle

    def _get_svi_l2vlan_bundle(self: AvdStructuredConfigNetworkServices, evpn_vlan_bundle: dict, tenant: dict, vlans: list) -> dict | None:
        """Return an bundle config for a svi or l2vlan."""
        bundle = self._router_bgp_vlan_aware_bundle(
            name=evpn_vlan_bundle["name"],
            vlans=vlans,
            rd=self.get_vlan_aware_bundle_rd(id=evpn_vlan_bundle["id"], tenant=tenant, is_vrf=False, rd_override=evpn_vlan_bundle.get("rd_override")),
            rt=self.get_vlan_aware_bundle_rt(
                id=evpn_vlan_bundle["id"],
                vni=evpn_vlan_bundle["id"],
                tenant=tenant,
                is_vrf=False,
                rt_override=evpn_vlan_bundle.get("rt_override"),
            ),
            evpn_l2_multi_domain=default(evpn_vlan_bundle.get("evpn_l2_multi_domain"), tenant.get("evpn_l2_multi_domain", True)) is True,
            tenant=tenant,
        )

        if bundle is not None:
            if (eos_cli := get(evpn_vlan_bundle, "bgp.raw_eos_cli")) is not None:
                bundle["eos_cli"] = eos_cli
            return bundle

        return None

    def _router_bgp_vlan_aware_bundles(self: AvdStructuredConfigNetworkServices, tenant_svis_l2vlans_dict: dict) -> list | None:
        """Return structured config for router_bgp.vlan_aware_bundles."""
        if not self.shared_utils.network_services_l2 or not self.shared_utils.overlay_evpn:
            return None

        bundles = []
        for tenant in self.shared_utils.filtered_tenants:
            l2vlan_svi_vlan_aware_bundles = {}
            for vrf in tenant["vrfs"]:
                for bundle_name, svis in tenant_svis_l2vlans_dict[tenant["name"]]["svi_bundle"][vrf["name"]].items():
                    # SVIs which have an evpn_vlan_bundle defined
                    if bundle_name in l2vlan_svi_vlan_aware_bundles:
                        l2vlan_svi_vlan_aware_bundles[bundle_name]["l2vlan_svis"].extend(svis)
                    else:
                        # check if the referred name exists in the global evpn_vlan_bundles
                        evpn_vlan_bundle = self._get_evpn_vlan_bundle(svis[0], bundle_name)
                        l2vlan_svi_vlan_aware_bundles[bundle_name] = {"evpn_vlan_bundle": evpn_vlan_bundle, "l2vlan_svis": svis}

                if self._evpn_vlan_aware_bundles:
                    svis = tenant_svis_l2vlans_dict[tenant["name"]]["svi_non_bundle"][vrf["name"]]
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
            for bundle_name, l2vlans in tenant_svis_l2vlans_dict[tenant["name"]]["l2vlan_bundle"].items():
                if bundle_name in l2vlan_svi_vlan_aware_bundles:
                    l2vlan_svi_vlan_aware_bundles[bundle_name]["l2vlan_svis"].extend(l2vlans)
                else:
                    # check if the referred name exists in the global evpn_vlan_bundles
                    evpn_vlan_bundle = self._get_evpn_vlan_bundle(l2vlans[0], bundle_name)
                    l2vlan_svi_vlan_aware_bundles[bundle_name] = {"evpn_vlan_bundle": evpn_vlan_bundle, "l2vlan_svis": l2vlans}

            if self._evpn_vlan_aware_bundles:
                for bundle_name, l2vlans in tenant_svis_l2vlans_dict[tenant["name"]]["l2vlan_non_bundle"].items():
                    # Without "evpn_vlan_bundle" we fall back to per-vlan behavior
                    if (bundle := self._router_bgp_vlans_vlan(l2vlans[0], tenant, vrf={})) is None:
                        # Skip bundle since no vlans were enabled for vxlan.
                        continue

                    # We are reusing the regular bgp vlan function so need to add vlan info
                    bundle["vlan"] = list_compress([int(l2vlan["id"]) for l2vlan in l2vlans])
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
                evpn_vlan_bundle = bundle_dict["evpn_vlan_bundle"]
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

    def _router_bgp_vlan_aware_bundles_vrf(self: AvdStructuredConfigNetworkServices, vrf: dict, tenant: dict, vlans: list[dict]) -> dict | None:
        """Return structured config for one vrf under router_bgp.vlan_aware_bundles."""
        return self._router_bgp_vlan_aware_bundle(
            name=vrf["name"],
            vlans=vlans,
            rd=self.get_vlan_aware_bundle_rd(id=self.shared_utils.get_vrf_id(vrf), tenant=tenant, is_vrf=True),
            rt=self.get_vlan_aware_bundle_rt(id=self.shared_utils.get_vrf_id(vrf), vni=self.shared_utils.get_vrf_vni(vrf), tenant=tenant, is_vrf=True),
            evpn_l2_multi_domain=default(vrf.get("evpn_l2_multi_domain"), tenant.get("evpn_l2_multi_domain", True)) is True,
            tenant=tenant,
        )

    def _router_bgp_vlan_aware_bundle(
        self: AvdStructuredConfigNetworkServices, name: str, vlans: list, rd: str, rt: str, evpn_l2_multi_domain: bool, tenant: dict
    ) -> dict | None:
        """
        Return structured config for one vlan-aware-bundle.

        Used for VRFs and bundles defined under "evpn_vlan_bundles" referred by l2vlans and SVIs.
        """
        vlans = [vlan for vlan in vlans if vlan.get("vxlan") is not False]
        if not vlans:
            return None

        bundle = {
            "name": name,
            "rd": rd,
            "route_targets": {
                "both": [rt],
            },
            "redistribute_routes": ["learned"],
            "vlan": list_compress([int(vlan["id"]) for vlan in vlans]),
        }
        if self.shared_utils.evpn_gateway_vxlan_l2 and evpn_l2_multi_domain:
            bundle["rd_evpn_domain"] = {"domain": "remote", "rd": rd}
            bundle["route_targets"]["import_export_evpn_domains"] = [{"domain": "remote", "route_target": rt}]

        if any(get(vlan, "evpn_l2_multicast.enabled", get(tenant, "evpn_l2_multicast.enabled")) is True for vlan in vlans):
            bundle["redistribute_routes"].append("igmp")

        return bundle

    @cached_property
    def _rt_admin_subfield(self: AvdStructuredConfigNetworkServices) -> str | None:
        """
        Return a string with the route-target admin subfield unless set to "vrf_id" or "vrf_vni" or "id".

        Returns None if not set, since the calling functions will use
        per-vlan numbers by default.
        """
        admin_subfield = self.shared_utils.overlay_rt_type["admin_subfield"]
        if admin_subfield is None:
            return None

        if admin_subfield == "bgp_as":
            return self.shared_utils.bgp_as

        if re_fullmatch(r"\d+", str(admin_subfield)):
            return admin_subfield

        return None

    def get_vlan_mac_vrf_id(self: AvdStructuredConfigNetworkServices, vlan: dict, tenant: dict) -> int:
        mac_vrf_id_base = default(tenant.get("mac_vrf_id_base"), tenant.get("mac_vrf_vni_base"))
        if mac_vrf_id_base is None:
            msg = (
                "'rt_override' or 'vni_override' or 'mac_vrf_id_base' or 'mac_vrf_vni_base' must be set. "
                f"Unable to set EVPN RD/RT for vlan {vlan['id']} in Tenant '{vlan['tenant']}'"
            )
            raise AristaAvdInvalidInputsError(msg)
        return mac_vrf_id_base + int(vlan["id"])

    def get_vlan_mac_vrf_vni(self: AvdStructuredConfigNetworkServices, vlan: dict, tenant: dict) -> int:
        mac_vrf_vni_base = default(tenant.get("mac_vrf_vni_base"), tenant.get("mac_vrf_id_base"))
        if mac_vrf_vni_base is None:
            msg = (
                "'rt_override' or 'vni_override' or 'mac_vrf_id_base' or 'mac_vrf_vni_base' must be set. "
                f"Unable to set EVPN RD/RT for vlan {vlan['id']} in Tenant '{vlan['tenant']}'"
            )
            raise AristaAvdInvalidInputsError(msg)
        return mac_vrf_vni_base + int(vlan["id"])

    def get_vlan_rd(self: AvdStructuredConfigNetworkServices, vlan: dict, tenant: dict) -> str:
        """Return a string with the route-destinguisher for one VLAN."""
        rd_override = default(vlan.get("rd_override"), vlan.get("rt_override"), vlan.get("vni_override"))

        if ":" in str(rd_override):
            return rd_override

        if rd_override is not None:
            assigned_number_subfield = rd_override
        elif self.shared_utils.overlay_rd_type["vlan_assigned_number_subfield"] == "mac_vrf_vni":
            assigned_number_subfield = self.get_vlan_mac_vrf_vni(vlan, tenant)
        elif self.shared_utils.overlay_rd_type["vlan_assigned_number_subfield"] == "vlan_id":
            assigned_number_subfield = vlan["id"]
        else:
            assigned_number_subfield = self.get_vlan_mac_vrf_id(vlan, tenant)

        return f"{self.shared_utils.overlay_rd_type_admin_subfield}:{assigned_number_subfield}"

    def get_vlan_rt(self: AvdStructuredConfigNetworkServices, vlan: dict, tenant: dict) -> str:
        """Return a string with the route-target for one VLAN."""
        rt_override = default(vlan.get("rt_override"), vlan.get("vni_override"))

        if ":" in str(rt_override):
            return rt_override

        if self._rt_admin_subfield is not None:
            admin_subfield = self._rt_admin_subfield
        elif rt_override is not None:
            admin_subfield = rt_override
        elif self.shared_utils.overlay_rt_type["admin_subfield"] == "vrf_vni":
            admin_subfield = self.get_vlan_mac_vrf_vni(vlan, tenant)
        elif self.shared_utils.overlay_rt_type["admin_subfield"] == "id":
            admin_subfield = vlan["id"]
        else:
            admin_subfield = self.get_vlan_mac_vrf_id(vlan, tenant)

        if rt_override is not None:
            assigned_number_subfield = rt_override
        elif self.shared_utils.overlay_rt_type["vlan_assigned_number_subfield"] == "mac_vrf_vni":
            assigned_number_subfield = self.get_vlan_mac_vrf_vni(vlan, tenant)
        elif self.shared_utils.overlay_rt_type["vlan_assigned_number_subfield"] == "vlan_id":
            assigned_number_subfield = vlan["id"]
        else:
            assigned_number_subfield = self.get_vlan_mac_vrf_id(vlan, tenant)

        return f"{admin_subfield}:{assigned_number_subfield}"

    @cached_property
    def _vrf_rt_admin_subfield(self: AvdStructuredConfigNetworkServices) -> str | None:
        """
        Return a string with the VRF route-target admin subfield unless set to "vrf_id" or "vrf_vni" or "id".

        Returns None if not set, since the calling functions will use
        per-vrf numbers by default.
        """
        admin_subfield = self.shared_utils.overlay_rt_type["vrf_admin_subfield"]
        if admin_subfield is None:
            return None

        if admin_subfield == "bgp_as":
            return self.shared_utils.bgp_as

        if re_fullmatch(r"\d+", str(admin_subfield)):
            return admin_subfield

        return None

    def get_vrf_rd(self: AvdStructuredConfigNetworkServices, vrf: dict) -> str:
        """Return a string with the route-destinguisher for one VRF."""
        rd_override = default(vrf.get("rd_override"))

        if ":" in str(rd_override):
            return rd_override

        if rd_override is not None:
            return f"{self.shared_utils.overlay_rd_type_vrf_admin_subfield}:{rd_override}"

        return f"{self.shared_utils.overlay_rd_type_vrf_admin_subfield}:{self.shared_utils.get_vrf_id(vrf)}"

    def get_vrf_rt(self: AvdStructuredConfigNetworkServices, vrf: dict) -> str:
        """Return a string with the route-target for one VRF."""
        rt_override = default(vrf.get("rt_override"))

        if ":" in str(rt_override):
            return rt_override

        if self._vrf_rt_admin_subfield is not None:
            admin_subfield = self._vrf_rt_admin_subfield
        elif self.shared_utils.overlay_rt_type["vrf_admin_subfield"] == "vrf_vni":
            admin_subfield = self.shared_utils.get_vrf_vni(vrf)
        else:
            # Both for 'id' and 'vrf_id' options.
            admin_subfield = self.shared_utils.get_vrf_id(vrf)

        if rt_override is not None:
            return f"{admin_subfield}:{rt_override}"

        return f"{admin_subfield}:{self.shared_utils.get_vrf_id(vrf)}"

    def get_vlan_aware_bundle_rd(
        self: AvdStructuredConfigNetworkServices,
        id: int,  # noqa: A002
        tenant: dict,
        is_vrf: bool,
        rd_override: str | None = None,
    ) -> str:
        """Return a string with the route-destinguisher for one VLAN Aware Bundle."""
        admin_subfield = self.shared_utils.overlay_rd_type_vrf_admin_subfield if is_vrf else self.shared_utils.overlay_rd_type_admin_subfield

        if rd_override is not None:
            if ":" in str(rd_override):
                return rd_override

            return f"{admin_subfield}:{rd_override}"

        bundle_number = id + int(get(tenant, "vlan_aware_bundle_number_base", default=0))
        return f"{admin_subfield}:{bundle_number}"

    def get_vlan_aware_bundle_rt(
        self: AvdStructuredConfigNetworkServices,
        id: int,  # noqa: A002
        vni: int,
        tenant: dict,
        is_vrf: bool,
        rt_override: str | None = None,
    ) -> str:
        """Return a string with the route-target for one VLAN Aware Bundle."""
        if rt_override is not None and ":" in str(rt_override):
            return rt_override

        bundle_number = id + int(get(tenant, "vlan_aware_bundle_number_base", default=0))

        if is_vrf and self._vrf_rt_admin_subfield is not None:
            admin_subfield = self._vrf_rt_admin_subfield
        elif is_vrf and self.shared_utils.overlay_rt_type["vrf_admin_subfield"] == "vrf_vni":
            admin_subfield = vni
        else:
            # Both for 'id' and 'vrf_id' options.
            admin_subfield = bundle_number

        if rt_override is not None:
            return f"{admin_subfield}:{rt_override}"

        return f"{admin_subfield}:{bundle_number}"

    @cached_property
    def _router_bgp_redistribute_routes(self: AvdStructuredConfigNetworkServices) -> dict | None:
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
    def _router_bgp_vpws(self: AvdStructuredConfigNetworkServices) -> list[dict] | None:
        """Return structured config for router_bgp.vpws."""
        if not (self.shared_utils.network_services_l1 and self.shared_utils.overlay_ler and self.shared_utils.overlay_evpn_mpls):
            return None

        vpws = []
        for tenant in self.shared_utils.filtered_tenants:
            if "point_to_point_services" not in tenant:
                continue

            if get(tenant, "pseudowire_rt_base") is None:
                continue

            pseudowires = []
            for point_to_point_service in natural_sort(tenant["point_to_point_services"], "name"):
                if subifs := point_to_point_service.get("subinterfaces", []):
                    subifs = [subif for subif in subifs if subif.get("number") is not None]

                endpoints = point_to_point_service.get("endpoints", [])
                for local_index, endpoint in enumerate(endpoints):
                    if not (self.shared_utils.hostname in endpoint.get("nodes", []) and endpoint.get("interfaces") is not None):
                        continue

                    # Endpoints can only have two entries with index 0 and 1.
                    # So the remote must be the other index.
                    remote_endpoint = endpoints[(local_index + 1) % 2]

                    if subifs:
                        for subif in subifs:
                            subif_number = int(subif["number"])
                            pseudowires.append(
                                {
                                    "name": f"{point_to_point_service['name']}_{subif_number}",
                                    "id_local": int(endpoint["id"]) + subif_number,
                                    "id_remote": int(remote_endpoint["id"]) + subif_number,
                                },
                            )

                    else:
                        pseudowires.append(
                            {
                                "name": f"{point_to_point_service['name']}",
                                "id_local": int(endpoint["id"]),
                                "id_remote": int(remote_endpoint["id"]),
                            },
                        )

            if pseudowires:
                rt_base = get(tenant, "pseudowire_rt_base", required=True, custom_error_msg=f"'pseudowire_rt_base' under Tenant '{tenant['name']} is required.")
                rd = f"{self.shared_utils.overlay_rd_type_admin_subfield}:{rt_base}"
                rt = f"{self._rt_admin_subfield or rt_base}:{rt_base}"
                vpws.append(
                    {
                        "name": tenant["name"],
                        "rd": rd,
                        "route_targets": {"import_export": rt},
                        "pseudowires": pseudowires,
                    },
                )

        if vpws:
            return vpws

        return None

    def _router_bgp_mlag_peer_group(self: AvdStructuredConfigNetworkServices) -> dict:
        """
        Return a partial router_bgp structured_config covering the MLAG peer_group and associated address_family activations.

        TODO: Partially duplicated from mlag. Should be moved to a common class
        """
        peer_group_name = self.shared_utils.bgp_peer_groups["mlag_ipv4_underlay_peer"]["name"]
        router_bgp = {}
        peer_group = {
            "name": peer_group_name,
            "type": "ipv4",
            "remote_as": self.shared_utils.bgp_as,
            "next_hop_self": True,
            "description": AvdStringFormatter().format(self.shared_utils.mlag_bgp_peer_group_description, mlag_peer=self.shared_utils.mlag_peer),
            "password": self.shared_utils.bgp_peer_groups["mlag_ipv4_underlay_peer"]["password"],
            "maximum_routes": 12000,
            "send_community": "all",
            "struct_cfg": self.shared_utils.bgp_peer_groups["mlag_ipv4_underlay_peer"]["structured_config"],
        }

        if self.shared_utils.mlag_ibgp_origin_incomplete is True:
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
        if self.shared_utils.underlay_rfc5549:
            address_family_ipv4_peer_group["next_hop"] = {"address_family_ipv6": {"enabled": True, "originate": True}}

        router_bgp["address_family_ipv4"] = {"peer_groups": [address_family_ipv4_peer_group]}
        return strip_empties_from_dict(router_bgp)
