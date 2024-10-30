# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdError
from pyavd._utils import get, get_all, get_item, strip_empties_from_list

if TYPE_CHECKING:
    from . import AvdStructuredConfigMetadata


class CvPathfinderMixin:
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    def _cv_pathfinder(self: AvdStructuredConfigMetadata) -> dict | None:
        """
        Generate metadata for CV Pathfinder feature.

        Only relevant for cv_pathfinder routers.

        Metadata for "applications" and "internet_exit_policies" is generated in the network services module,
        since all the required data was readily available in there.
        """
        if not self.shared_utils.is_cv_pathfinder_router:
            return None

        # Pathfinder
        if self.shared_utils.is_cv_pathfinder_server:
            return {
                "role": self.shared_utils.cv_pathfinder_role,
                "ssl_profile": self.shared_utils.wan_stun_dtls_profile_name,
                "vtep_ip": self.shared_utils.vtep_ip,
                "region": get(self.shared_utils.wan_region or {}, "name"),
                "site": get(self.shared_utils.wan_site or {}, "name"),
                "address": get(self.shared_utils.wan_site or {}, "location"),
                "interfaces": self._metadata_interfaces(),
                "pathgroups": self._metadata_pathgroups(),
                "regions": self._metadata_regions(),
                "vrfs": self._metadata_vrfs(),
            }

        # Edge or transit
        return {
            "role": self.shared_utils.cv_pathfinder_role,
            "ssl_profile": self.shared_utils.wan_stun_dtls_profile_name,
            "vtep_ip": self.shared_utils.vtep_ip,
            "region": self.shared_utils.wan_region["name"],
            "zone": self.shared_utils.wan_zone["name"],
            "site": self.shared_utils.wan_site["name"],
            "interfaces": self._metadata_interfaces(),
            "pathfinders": self._metadata_pathfinder_vtep_ips(),
        }

    def _metadata_interfaces(self: AvdStructuredConfigMetadata) -> list:
        return [
            {
                "name": interface["name"],
                "carrier": carrier["name"],
                "circuit_id": interface.get("wan_circuit_id"),
                "pathgroup": carrier["path_group"],
                "public_ip": str(interface["public_ip"]) if self.shared_utils.is_cv_pathfinder_server else None,
            }
            for carrier in self.shared_utils.wan_local_carriers
            for interface in carrier["interfaces"]
        ]

    def _metadata_pathgroups(self: AvdStructuredConfigMetadata) -> list:
        return [
            {
                "name": pathgroup["name"],
                "carriers": [
                    {
                        "name": carrier["name"],
                    }
                    for carrier in self.shared_utils.wan_carriers
                    if carrier["path_group"] == pathgroup["name"]
                ],
                "imported_carriers": [
                    {
                        "name": carrier["name"],
                    }
                    for carrier in self.shared_utils.wan_carriers
                    if carrier["path_group"] in [imported_pathgroup["remote"] for imported_pathgroup in pathgroup.get("import_path_groups", [])]
                ],
            }
            for pathgroup in self.shared_utils.wan_path_groups
        ]

    def _metadata_regions(self: AvdStructuredConfigMetadata) -> list:
        regions = get(
            self._hostvars,
            "cv_pathfinder_regions",
            required=True,
            custom_error_msg="'cv_pathfinder_regions' key must be set when 'wan_mode' is 'cv-pathfinder'.",
        )
        return [
            {
                "name": region["name"],
                "id": region["id"],
                "zones": [
                    {
                        # TODO: Once we give configurable zones this should be updated
                        "name": f"{region['name']}-ZONE",
                        "id": 1,
                        "sites": [
                            {
                                "name": site["name"],
                                "id": site["id"],
                                "location": (
                                    {
                                        "address": site.get("location"),
                                    }
                                    if site.get("location")
                                    else None
                                ),
                            }
                            for site in region["sites"]
                        ],
                    },
                ],
            }
            for region in regions
        ]

    def _metadata_pathfinder_vtep_ips(self: AvdStructuredConfigMetadata) -> list:
        return [
            {
                "vtep_ip": wan_route_server["vtep_ip"],
            }
            for wan_route_server in self.shared_utils.filtered_wan_route_servers.values()
        ]

    def _metadata_vrfs(self: AvdStructuredConfigMetadata) -> list:
        """Extracting metadata for VRFs by parsing the generated structured config and flatten it a bit (like hiding load-balance policies)."""
        if (avt_vrfs := get(self._hostvars, "router_adaptive_virtual_topology.vrfs")) is None:
            return []

        if (load_balance_policies := get(self._hostvars, "router_path_selection.load_balance_policies")) is None:
            return []

        avt_policies = get(self._hostvars, "router_adaptive_virtual_topology.policies", required=True)

        if self.shared_utils.is_wan_server:
            # On pathfinders, verify that the Load Balance policies have at least one priority one except for the HA path-group
            for lb_policy in load_balance_policies:
                if not any(
                    path_group.get("priority", 1) == 1
                    for path_group in lb_policy["path_groups"]
                    if path_group["name"] != self.shared_utils.wan_ha_path_group_name
                ):
                    msg = (
                        "At least one path-group must be configured with preference '1' or 'preferred' for "
                        f"load-balance policy {lb_policy['name']}' to use CloudVision integration. "
                        "If this is an auto-generated policy, ensure that at least one default_preference "
                        "for a non excluded path-group is set to 'preferred' (or unset as this is the default)."
                    )
                    raise AristaAvdError(
                        msg,
                    )

        return strip_empties_from_list(
            [
                {
                    "name": vrf["name"],
                    "vni": self._get_vni_for_vrf_name(vrf["name"]),
                    "avts": [
                        {
                            "constraints": {
                                "jitter": lb_policy.get("jitter"),
                                "latency": lb_policy.get("latency"),
                                "lossrate": float(lb_policy["loss_rate"]) if "loss_rate" in lb_policy else None,
                                "hop_count": "lowest" if lb_policy.get("lowest_hop_count") else None,
                            },
                            "description": "",  # TODO: Not sure we have this field anywhere
                            "id": profile["id"],
                            "name": profile["name"],
                            "pathgroups": [
                                {
                                    "name": pathgroup["name"],
                                    "preference": "alternate" if pathgroup.get("priority", 1) > 1 else "preferred",
                                }
                                for pathgroup in lb_policy["path_groups"]
                            ],
                            "application_profiles": [
                                profile
                                for profile in get_all(get_item(avt_policy["matches"], "avt_profile", profile["name"], default={}), "application_profile")
                                if profile != "default"
                            ],
                        }
                        for profile in vrf["profiles"]
                        for lb_policy in [get_item(load_balance_policies, "name", self.shared_utils.generate_lb_policy_name(profile["name"]), required=True)]
                    ],
                }
                for vrf in avt_vrfs
                for avt_policy in [get_item(avt_policies, "name", vrf["policy"], required=True)]
            ],
        )

    @cached_property
    def _wan_virtual_topologies_vrfs(self: AvdStructuredConfigMetadata) -> list[dict]:
        """
        Unfiltered list of VRFs found under wan_virtual_topologies.

        Used to find VNI for each VRF used in cv_pathfinder.
        """
        return get(self._hostvars, "wan_virtual_topologies.vrfs", default=[])

    def _get_vni_for_vrf_name(self: AvdStructuredConfigMetadata, vrf_name: str) -> int:
        if (vrf := get_item(self._wan_virtual_topologies_vrfs, "name", vrf_name)) is None or (wan_vni := vrf.get("wan_vni")) is None:
            if vrf_name == "default":
                return 1

            msg = f"Unable to find the WAN VNI for VRF {vrf_name} during generation of cv_pathfinder metadata."
            raise AristaAvdError(msg)

        return wan_vni
