# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import append_if_not_duplicate, get, get_item, strip_empties_from_dict

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class RouterAdaptiveVirtualTopologyMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def router_adaptive_virtual_topology(self: AvdStructuredConfigNetworkServices) -> dict | None:
        """Return structured config for profiles, policies and VRFs for router adaptive-virtual-topology (AVT)."""
        if not self.shared_utils.is_cv_pathfinder_router:
            return None

        router_adaptive_virtual_topology = {
            "profiles": self._cv_pathfinder_profiles(),
            "vrfs": self._cv_pathfinder_wan_vrfs(),
            "policies": self._cv_pathfinder_policies(),
        }

        return strip_empties_from_dict(router_adaptive_virtual_topology)

    def _cv_pathfinder_wan_vrfs(self: AvdStructuredConfigNetworkServices) -> list:
        """Return a list of WAN VRFs based on filtered tenants and the AVT."""
        # For CV Pathfinder, it is required to go through all the AVT profiles in the policy to assign an ID.
        wan_vrfs = []

        for vrf in self._filtered_wan_vrfs:
            wan_vrf = {"name": vrf.name, "policy": f"{vrf.policy}-WITH-CP" if vrf.name == "default" else vrf.policy, "profiles": []}

            # Need to allocate an ID for each profile in the policy, for now picked up from the input.
            policy = get_item(
                self._filtered_wan_policies,
                "name",
                wan_vrf["policy"],
                required=True,
                custom_error_msg=(f"The policy {wan_vrf['policy']} used in vrf {wan_vrf['name']} is not configured under 'wan_virtual_topologies.policies'."),
            )

            for match in policy.get("matches", []):
                wan_vrf["profiles"].append(
                    {
                        "name": get(match, "avt_profile", required=True),
                        "id": get(match, "id", required=True),
                    },
                )
            if (default_match := policy.get("default_match")) is not None:
                wan_vrf["profiles"].append(
                    {
                        "name": get(default_match, "avt_profile", required=True),
                        "id": get(default_match, "id", required=True),
                    },
                )

            wan_vrfs.append(wan_vrf)

        return wan_vrfs

    def _cv_pathfinder_policies(self: AvdStructuredConfigNetworkServices) -> list:
        """
        Build and return the CV Pathfinder policies based on the computed _filtered_wan_policies.

        It loops though the different match statements to build the appropriate entries
        by popping the load_balance_policy and id keys.
        """
        policies = []

        for policy in self._filtered_wan_policies:
            pathfinder_policy = {"name": policy["name"], "matches": []}
            for match in get(policy, "matches", default=[]):
                # popping id, load_balance_and internet-exit policy
                pathfinder_match = match.copy()
                pathfinder_match.pop("id")
                pathfinder_match.pop("load_balance_policy")
                pathfinder_match.pop("internet_exit_policy_name")
                pathfinder_policy["matches"].append(pathfinder_match)

            if (default_match := policy.get("default_match")) is not None:
                pathfinder_match = default_match.copy()
                pathfinder_match.pop("id")
                pathfinder_match.pop("load_balance_policy")
                pathfinder_match.pop("internet_exit_policy_name")
                pathfinder_policy["matches"].append(pathfinder_match)

            policies.append(strip_empties_from_dict(pathfinder_policy))

        return policies

    def _cv_pathfinder_profiles(self: AvdStructuredConfigNetworkServices) -> list:
        """Return a list of router adaptive-virtual-topology profiles for this router."""
        profiles = []
        for policy in self._filtered_wan_policies:
            for match in policy.get("matches", []):
                profile = {
                    "name": match["avt_profile"],
                    "load_balance_policy": match["load_balance_policy"]["name"],
                }
                if (internet_exit_policy_name := match["internet_exit_policy_name"]) is not None and internet_exit_policy_name in [
                    policy.name for policy, _connections in self._filtered_internet_exit_policies_and_connections
                ]:
                    profile["internet_exit_policy"] = internet_exit_policy_name

                append_if_not_duplicate(
                    list_of_dicts=profiles,
                    primary_key="name",
                    new_dict=profile,
                    context="Router Adaptive Virtual Topology profiles.",
                    context_keys=["name"],
                )
            if (default_match := policy.get("default_match")) is not None:
                profile = {
                    "name": default_match["avt_profile"],
                    "load_balance_policy": default_match["load_balance_policy"]["name"],
                }
                if (internet_exit_policy_name := default_match["internet_exit_policy_name"]) is not None and internet_exit_policy_name in [
                    policy.name for policy, _connections in self._filtered_internet_exit_policies_and_connections
                ]:
                    profile["internet_exit_policy"] = internet_exit_policy_name

                append_if_not_duplicate(
                    list_of_dicts=profiles,
                    primary_key="name",
                    new_dict=profile,
                    context="Router Adaptive Virtual Topology profiles.",
                    context_keys=["name"],
                )

        return profiles
