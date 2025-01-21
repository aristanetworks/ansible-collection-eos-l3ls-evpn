# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections import defaultdict
from functools import cached_property
from typing import TYPE_CHECKING

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class RouterInternetExitMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def router_internet_exit(self: AvdStructuredConfigNetworkServices) -> dict | None:
        """
        Return structured config for router_internet_exit.

        Only used for CV Pathfinder edge routers today
        """
        if not self._filtered_internet_exit_policies_and_connections:
            return None

        router_internet_exit = {}
        exit_groups_dict = defaultdict(lambda: {"local_connections": []})
        policies = []

        for policy, connections in self._filtered_internet_exit_policies_and_connections:
            policy_exit_groups = []
            # TODO: Today we use the order of the connection list to order the exit-groups inside the policy.
            #       This works for zscaler but later we may need to use some sorting intelligence as order matters.
            for connection in connections:
                exit_group_name = connection["exit_group"]
                exit_groups_dict[exit_group_name]["local_connections"].append({"name": connection["name"]})
                # Recording the exit_group in the policy
                if exit_group_name not in policy_exit_groups:
                    policy_exit_groups.append(exit_group_name)

            if policy.fallback_to_system_default:
                policy_exit_groups.append("system-default-exit-group")

            policies.append({"name": policy.name, "exit_groups": [{"name": exit_group_name} for exit_group_name in policy_exit_groups]})

        if exit_groups_dict:
            router_internet_exit["exit_groups"] = [
                {"name": exit_group_name, **exit_group_data} for exit_group_name, exit_group_data in exit_groups_dict.items()
            ]
        if policies:
            router_internet_exit["policies"] = policies

        if router_internet_exit:
            return router_internet_exit

        return None
