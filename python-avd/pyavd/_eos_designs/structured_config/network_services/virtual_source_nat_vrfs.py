# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import append_if_not_duplicate, get_ip_from_ip_prefix, strip_null_from_data

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class VirtualSourceNatVrfsMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def virtual_source_nat_vrfs(self: AvdStructuredConfigNetworkServices) -> list | None:
        """
        Return structured config for virtual_source_nat_vrfs.

        Only used by VTEPs with L2 and L3 services
        Using data from loopback_interfaces to avoid duplicating logic
        """
        if not (self.shared_utils.overlay_vtep and self.shared_utils.network_services_l2 and self.shared_utils.network_services_l3):
            return None

        if (loopback_interfaces := self.loopback_interfaces) is None:
            return None

        virtual_source_nat_vrfs = []
        for loopback_interface in loopback_interfaces:
            if (vrf := loopback_interface.get("vrf", "default")) is None:
                continue

            # Using append_if_not_duplicate but with ignore_same_dict and ignore_keys.
            # It will append the dict unless the same "name" is already in the dict.
            # It will never raise since we only have these two keys.
            append_if_not_duplicate(
                virtual_source_nat_vrfs,
                primary_key="name",
                new_dict={
                    "name": vrf,
                    "ip_address": get_ip_from_ip_prefix(loopback_interface["ip_address"]) if "ip_address" in loopback_interface else None,
                    "ipv6_address": get_ip_from_ip_prefix(loopback_interface["ipv6_address"]) if "ipv6_address" in loopback_interface else None,
                },
                context="virtual_source_nat_vrfs",
                context_keys=["name"],
                ignore_same_dict=True,
                ignore_keys={"ip_address", "ipv6_address"},
            )

        if virtual_source_nat_vrfs:
            return strip_null_from_data(virtual_source_nat_vrfs)

        return None
