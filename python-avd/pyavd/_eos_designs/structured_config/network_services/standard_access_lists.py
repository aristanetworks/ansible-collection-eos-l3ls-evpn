# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import append_if_not_duplicate

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class StandardAccessListsMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def standard_access_lists(self: AvdStructuredConfigNetworkServices) -> list | None:
        """
        return structured config for standard_access_lists.

        Used for to configure ACLs used by multicast RPs in each VRF
        """
        if not self.shared_utils.network_services_l3:
            return None

        standard_access_lists = []
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                for rp_entry in vrf.pim_rp_addresses or tenant.pim_rp_addresses:
                    if (rp_entry.nodes and self.shared_utils.hostname not in rp_entry.nodes) or not rp_entry.groups or not rp_entry.access_list_name:
                        continue

                    standard_access_list = {
                        "name": rp_entry.access_list_name,
                        "sequence_numbers": [
                            {
                                "sequence": (index) * 10,
                                "action": f"permit {group}",
                            }
                            for index, group in enumerate(rp_entry.groups, 1)
                        ],
                    }

                    append_if_not_duplicate(
                        list_of_dicts=standard_access_lists,
                        primary_key="name",
                        new_dict=standard_access_list,
                        context="PIM RP Address ACL for VRFs",
                        context_keys=["name"],
                    )

        if standard_access_lists:
            return standard_access_lists

        return None
