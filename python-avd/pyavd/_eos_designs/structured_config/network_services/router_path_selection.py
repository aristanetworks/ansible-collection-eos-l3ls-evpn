# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._utils import get

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class RouterPathSelectionMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def router_path_selection(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """Return structured config for router path-selection (DPS)."""
        if not self.shared_utils.is_wan_router:
            return

        self._wan_load_balance_policies()

        # When running CV Pathfinder, only load balance policies are configured
        # for AutoVPN, need also vrfs and policies.
        if self.inputs.wan_mode == "autovpn":
            vrfs = [
                {"name": vrf.name, "path_selection_policy": f"{vrf.policy}-WITH-CP" if vrf.name == "default" else vrf.policy} for vrf in self._filtered_wan_vrfs
            ]

            for vrf in vrfs:
                self.structured_config.router_path_selection.vrfs.append(EosCliConfigGen.RouterPathSelection.VrfsItem(**vrf))

            self._autovpn_policies()

    def _wan_load_balance_policies(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """Set list of load balance policies."""
        for policy in self._filtered_wan_policies:
            for match in policy.get("matches", []):
                if "load_balance_policy" in match:
                    lb_policy = EosCliConfigGen.RouterPathSelection.LoadBalancePoliciesItem()
                    lb_policy._update(
                        name=get(match["load_balance_policy"], "name", None),
                        lowest_hop_count=get(match["load_balance_policy"], "lowest_hop_count", None),
                        jitter=get(match["load_balance_policy"], "jitter", None),
                        latency=get(match["load_balance_policy"], "latency", None),
                        loss_rate=get(match["load_balance_policy"], "loss_rate", None),
                    )
                    for group in get(match["load_balance_policy"], "path_groups", None):
                        path_group_item = EosCliConfigGen.RouterPathSelection.LoadBalancePoliciesItem.PathGroupsItem(
                            name=group["name"], priority=get(group, "priority", None)
                        )
                        lb_policy.path_groups.append(path_group_item)
                    self.structured_config.router_path_selection.load_balance_policies.append(lb_policy)

            if (default_match := policy.get("default_match")) is not None and "load_balance_policy" in default_match:
                lb_policy = EosCliConfigGen.RouterPathSelection.LoadBalancePoliciesItem()
                lb_policy._update(
                    name=get(default_match["load_balance_policy"], "name", None),
                )
                for group in get(default_match["load_balance_policy"], "path_groups", None):
                    path_group_item = EosCliConfigGen.RouterPathSelection.LoadBalancePoliciesItem.PathGroupsItem(
                        name=get(group, "name", None), priority=get(group, "priority", None)
                    )
                    lb_policy.path_groups.append(path_group_item)
                self.structured_config.router_path_selection.load_balance_policies.append(lb_policy)

    def _autovpn_policies(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """Return a list of policies for AutoVPN."""
        for policy in self._filtered_wan_policies:
            policy_item = EosCliConfigGen.RouterPathSelection.PoliciesItem()
            policy_item.name = policy["name"]
            for index, match in enumerate(get(policy, "matches", default=[]), start=1):
                policy_item.rules.append(
                    EosCliConfigGen.RouterPathSelection.PoliciesItem.RulesItem(
                        id=10 * index,
                        application_profile=get(match, "application_profile"),
                        load_balance=get(match["load_balance_policy"], "name") if "load_balance_policy" in match else None,
                    )
                )
            if (default_match := policy.get("default_match")) is not None and "load_balance_policy" in default_match:
                policy_item.default_match.load_balance = get(default_match["load_balance_policy"], "name")
            self.structured_config.router_path_selection.policies.append(policy_item)
