# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

from pyavd._utils import append_if_not_duplicate

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class RouterPimSparseModeMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def router_pim_sparse_mode(self: AvdStructuredConfigNetworkServicesProtocol) -> dict | None:
        """
        Return structured config for router_pim.

        Used for to configure RPs on the VRF
        """
        if not self.shared_utils.network_services_l3:
            return None

        vrfs = []
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                if vrf_rps := getattr(vrf, "_pim_rp_addresses", None):
                    vrf_config = {
                        "name": vrf.name,
                        "ipv4": {
                            "rp_addresses": vrf_rps,
                        },
                    }
                    append_if_not_duplicate(
                        list_of_dicts=vrfs,
                        primary_key="name",
                        new_dict=vrf_config,
                        context="Router PIM Sparse-Mode for VRFs",
                        context_keys=["name"],
                    )
        if vrfs:
            return {"vrfs": vrfs}

        return None
