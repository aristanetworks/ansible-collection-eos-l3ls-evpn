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


class RouterMulticastMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def router_multicast(self: AvdStructuredConfigNetworkServices) -> dict | None:
        """
        return structured config for router_multicast.

        Used to enable multicast routing on the VRF.
        """
        if not self.shared_utils.network_services_l3:
            return None

        vrfs = []
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                if getattr(vrf, "_evpn_l3_multicast_enabled", False):
                    vrf_config = {"name": vrf.name, "ipv4": {"routing": True}}
                    append_if_not_duplicate(
                        list_of_dicts=vrfs,
                        primary_key="name",
                        new_dict=vrf_config,
                        context="Router Multicast for VRFs",
                        context_keys=["name"],
                    )

        if vrfs:
            return {"vrfs": vrfs}

        return None
