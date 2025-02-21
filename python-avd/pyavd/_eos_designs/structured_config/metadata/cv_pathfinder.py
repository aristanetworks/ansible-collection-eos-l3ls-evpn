# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._errors import AristaAvdError, AristaAvdInvalidInputsError
from pyavd._utils import default

if TYPE_CHECKING:
    from . import AvdStructuredConfigMetadataProtocol


class CvPathfinderMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    def _cv_pathfinder(self: AvdStructuredConfigMetadataProtocol) -> None:
        """
        Generate metadata for CV Pathfinder feature.

        Only relevant for cv_pathfinder routers.

        Metadata for "applications" and "internet_exit_policies" is generated in the network services module,
        since all the required data was readily available in there.
        """
        region_name = self.shared_utils.wan_region.name if self.shared_utils.wan_region is not None else None
        site_name = self.shared_utils.wan_site.name if self.shared_utils.wan_site is not None else None
        # Pathfinder
        if self.shared_utils.is_cv_pathfinder_server:
            self.structured_config.metadata.cv_pathfinder._update(
                role=self.shared_utils.cv_pathfinder_role,
                ssl_profile=self.shared_utils.wan_stun_dtls_profile_name,
                vtep_ip=self.shared_utils.vtep_ip,
                region=region_name,
                site=site_name,
                address=self.shared_utils.wan_site.location if self.shared_utils.wan_site is not None else None,
            )
            self._metadata_interfaces()
            self._metadata_pathgroups()
            self._metadata_regions()
            if self.structured_config.router_adaptive_virtual_topology.vrfs and self.structured_config.router_path_selection.load_balance_policies:
                self._metadata_vrfs()
        else:
            self.structured_config.metadata.cv_pathfinder._update(
                role=self.shared_utils.cv_pathfinder_role,
                ssl_profile=self.shared_utils.wan_stun_dtls_profile_name,
                vtep_ip=self.shared_utils.vtep_ip,
                region=region_name,
                zone=self.shared_utils.wan_zone["name"] if region_name else None,
                site=site_name,
            )
            self._metadata_interfaces()
            self._metadata_pathfinder_vtep_ips()

    def _metadata_interfaces(self: AvdStructuredConfigMetadataProtocol) -> None:
        for carrier in self.shared_utils.wan_local_carriers:
            for interface in carrier["interfaces"]:
                self.structured_config.metadata.cv_pathfinder.interfaces.append_new(
                    name=interface["name"],
                    carrier=carrier["name"],
                    circuit_id=interface.get("wan_circuit_id"),
                    pathgroup=carrier["path_group"],
                    public_ip=str(interface["public_ip"]) if self.shared_utils.is_cv_pathfinder_server else None,
                )

    def _metadata_pathgroups(self: AvdStructuredConfigMetadataProtocol) -> None:
        for pathgroup in self.inputs.wan_path_groups:
            path_group = EosCliConfigGen.Metadata.CvPathfinder.PathgroupsItem(name=pathgroup.name)
            for carrier in self.inputs.wan_carriers:
                if carrier.path_group == pathgroup.name:
                    path_group.carriers.append_new(name=carrier.name)
                if carrier.path_group in [imported_pathgroup.remote for imported_pathgroup in pathgroup.import_path_groups]:
                    path_group.imported_carriers.append_new(name=carrier.name)
            self.structured_config.metadata.cv_pathfinder.pathgroups.append(path_group)

    def _metadata_regions(self: AvdStructuredConfigMetadataProtocol) -> None:
        if not self.inputs.cv_pathfinder_regions:
            msg = "'cv_pathfinder_regions' key must be set when 'wan_mode' is 'cv-pathfinder'."
            raise AristaAvdInvalidInputsError(msg)
        regions = self.inputs.cv_pathfinder_regions
        for region in regions:
            region_item = EosCliConfigGen.Metadata.CvPathfinder.RegionsItem(name=region.name, id=region.id)
            region_item.zones.append_new(name=f"{region.name}-ZONE", id=1)
            for site in region.sites:
                site_item = region_item.zones[0].SitesItem(name=site.name, id=site.id)
                site_item.location.address = site.location
                region_item.zones[0].sites.append(site_item)
            self.structured_config.metadata.cv_pathfinder.regions.append(region_item)

    def _metadata_pathfinder_vtep_ips(self: AvdStructuredConfigMetadataProtocol) -> None:
        for wan_route_server in self.shared_utils.filtered_wan_route_servers:
            self.structured_config.metadata.cv_pathfinder.pathfinders.append_new(vtep_ip=wan_route_server.vtep_ip)

    def _metadata_vrfs(self: AvdStructuredConfigMetadataProtocol) -> None:
        """Extracting metadata for VRFs by parsing the generated structured config and flatten it a bit (like hiding load-balance policies)."""
        avt_vrfs = self.structured_config.router_adaptive_virtual_topology.vrfs
        load_balance_policies = self.structured_config.router_path_selection.load_balance_policies

        avt_policies = self.structured_config.router_adaptive_virtual_topology.policies

        if self.shared_utils.is_wan_server:
            # On pathfinders, verify that the Load Balance policies have at least one priority one except for the HA path-group
            for lb_policy in load_balance_policies:
                if not any(
                    default(path_group.priority, 1) == 1 for path_group in lb_policy.path_groups if path_group.name != self.inputs.wan_ha.lan_ha_path_group_name
                ):
                    msg = (
                        "At least one path-group must be configured with preference '1' or 'preferred' for "
                        f"load-balance policy {lb_policy.name}' to use CloudVision integration. "
                        "If this is an auto-generated policy, ensure that at least one default_preference "
                        "for a non excluded path-group is set to 'preferred' (or unset as this is the default)."
                    )
                    raise AristaAvdError(msg)

        for vrf in avt_vrfs:
            if not vrf.policy:
                continue

            avt_policy = avt_policies[vrf.policy]
            metadata_vrf = EosCliConfigGen.Metadata.CvPathfinder.VrfsItem(name=vrf.name, vni=self._get_vni_for_vrf_name(vrf.name))
            for profile in vrf.profiles:
                if not profile.name:
                    continue
                lb_policy = load_balance_policies[self.shared_utils.generate_lb_policy_name(profile.name)]
                avt = EosCliConfigGen.Metadata.CvPathfinder.VrfsItem.AvtsItem(id=profile.id, name=profile.name)
                for match in avt_policy.matches:
                    if match.avt_profile == profile.name and match.application_profile and match.application_profile != "default":
                        avt.application_profiles.append(match.application_profile)

                avt.constraints._update(
                    jitter=lb_policy.jitter,
                    latency=lb_policy.latency,
                    hop_count="lowest" if lb_policy.lowest_hop_count else None,
                )
                if lb_policy.loss_rate:
                    avt.constraints.lossrate = str(float(lb_policy.loss_rate))
                for pathgroup in lb_policy.path_groups:
                    avt.pathgroups.append_new(name=pathgroup.name, preference="alternate" if default(pathgroup.priority, 1) > 1 else "preferred")
                metadata_vrf.avts.append(avt)

            self.structured_config.metadata.cv_pathfinder.vrfs.append(metadata_vrf)

    def _get_vni_for_vrf_name(self: AvdStructuredConfigMetadataProtocol, vrf_name: str) -> int:
        if vrf_name not in self.inputs.wan_virtual_topologies.vrfs or (wan_vni := self.inputs.wan_virtual_topologies.vrfs[vrf_name].wan_vni) is None:
            if vrf_name == "default":
                return 1

            msg = f"Unable to find the WAN VNI for VRF {vrf_name} during generation of cv_pathfinder metadata."
            raise AristaAvdError(msg)

        return wan_vni
