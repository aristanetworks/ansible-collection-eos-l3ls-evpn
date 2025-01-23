# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from .utils import UtilsMixin


class PrefixListsMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def prefix_lists(self) -> list | None:
        """
        Return structured config for prefix_lists.

        Covers EVPN services in VRF "default" and redistribution of connected to BGP
        """
        # Get prefix-lists from EVPN services in VRF "default" (if any)
        prefix_lists = self._prefix_lists_vrf_default()

        # Add prefix-list for VRFs where MLAG iBGP peering should not be redistributed
        if mlag_prefixes := self._mlag_ibgp_peering_subnets_without_redistribution:
            prefix_list = {"name": "PL-MLAG-PEER-VRFS", "sequence_numbers": []}
            for index, mlag_prefix in enumerate(mlag_prefixes):
                sequence = 10 * (index + 1)
                prefix_list["sequence_numbers"].append({"sequence": sequence, "action": f"permit {mlag_prefix}"})

            prefix_lists.append(prefix_list)

        if prefix_lists:
            return prefix_lists

        return None

    def _prefix_lists_vrf_default(self) -> list:
        """prefix_lists for EVPN services in VRF "default"."""
        if not self._vrf_default_evpn:
            return []

        subnets = self._vrf_default_ipv4_subnets
        static_routes = self._vrf_default_ipv4_static_routes["static_routes"]
        if not subnets and not static_routes:
            return []

        prefix_lists = []
        if subnets:
            prefix_list = {"name": "PL-SVI-VRF-DEFAULT", "sequence_numbers": []}
            for index, subnet in enumerate(subnets):
                sequence = 10 * (index + 1)
                prefix_list["sequence_numbers"].append({"sequence": sequence, "action": f"permit {subnet}"})
            prefix_lists.append(prefix_list)

        if static_routes:
            prefix_list = {"name": "PL-STATIC-VRF-DEFAULT", "sequence_numbers": []}
            for index, static_route in enumerate(static_routes):
                sequence = 10 * (index + 1)
                prefix_list["sequence_numbers"].append({"sequence": sequence, "action": f"permit {static_route}"})
            prefix_lists.append(prefix_list)
        return prefix_lists
