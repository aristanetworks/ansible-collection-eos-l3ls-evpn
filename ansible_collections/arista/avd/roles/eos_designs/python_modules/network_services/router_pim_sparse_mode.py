# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property

from ansible_collections.arista.avd.plugins.plugin_utils.utils import append_if_not_duplicate, get
from ansible_collections.arista.avd.roles.eos_designs.python_modules.network_services.utils import UtilsMixin


class RouterPimSparseModeMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.
    Class should only be used as Mixin to a AvdStructuredConfig class
    """

    @cached_property
    def router_pim_sparse_mode(self) -> dict | None:
        """
        return structured config for router_pim

        Used for to configure RPs on the VRF
        """

        if not self.shared_utils.network_services_l3:
            return None

        vrfs = []
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant["vrfs"]:
                if vrf_rps := get(vrf, "_pim_rp_addresses"):
                    vrf_config = {
                        "name": vrf["name"],
                        "ipv4": {
                            "rp_addresses": vrf_rps,
                        },
                    }
                    append_if_not_duplicate(
                        list_of_dicts=vrfs, primary_key="name", new_dict=vrf_config, context="Router PIM Sparse-Mode for VRFs", context_keys=["name"]
                    )
        if vrfs:
            return {"vrfs": vrfs}

        return None
