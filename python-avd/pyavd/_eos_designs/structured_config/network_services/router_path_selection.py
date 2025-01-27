# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import append_if_not_duplicate, get, strip_empties_from_dict

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class RouterPathSelectionMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def router_path_selection(self: AvdStructuredConfigNetworkServices) -> dict | None:
        """Return structured config for router path-selection (DPS)."""
        if not self.shared_utils.is_wan_router:
            return None

        router_path_selection = {
            "load_balance_policies": self._wan_load_balance_policies(),
        }

        # When running CV Pathfinder, only load balance policies are configured
        # for AutoVPN, need also vrfs and policies.
        if self.inputs.wan_mode == "autovpn":
            vrfs = [
                {"name": vrf.name, "path_selection_policy": f"{vrf.policy}-WITH-CP" if vrf.name == "default" else vrf.policy} for vrf in self._filtered_wan_vrfs
            ]

            router_path_selection.update(
                {
                    "policies": self._autovpn_policies(),
                    "vrfs": vrfs,
                },
            )

        return strip_empties_from_dict(router_path_selection)

    def _wan_load_balance_policies(self: AvdStructuredConfigNetworkServices) -> list:
        """Return a list of load balance policies."""
        load_balance_policies = []
        for policy in self._filtered_wan_policies:
            for match in policy.get("matches", []):
                append_if_not_duplicate(
                    list_of_dicts=load_balance_policies,
                    primary_key="name",
                    new_dict=match["load_balance_policy"],
                    context="Router Path-Selection load-balance policies.",
                    context_keys=["name"],
                )
            if (default_match := policy.get("default_match")) is not None:
                append_if_not_duplicate(
                    list_of_dicts=load_balance_policies,
                    primary_key="name",
                    new_dict=default_match["load_balance_policy"],
                    context="Router Path-Selection load-balance policies.",
                    context_keys=["name"],
                )

        return load_balance_policies

    def _autovpn_policies(self: AvdStructuredConfigNetworkServices) -> list:
        """Return a list of policies for AutoVPN."""
        policies = []
        for policy in self._filtered_wan_policies:
            autovpn_policy = {"name": policy["name"], "rules": []}
            for index, match in enumerate(get(policy, "matches", default=[]), start=1):
                autovpn_policy["rules"].append(
                    {
                        "id": 10 * index,
                        "application_profile": match["application_profile"],
                        "load_balance": match["load_balance_policy"]["name"],
                    },
                )
            if (default_match := policy.get("default_match")) is not None:
                autovpn_policy["default_match"] = {"load_balance": default_match["load_balance_policy"]["name"]}

            policies.append(strip_empties_from_dict(autovpn_policy))
        return policies
