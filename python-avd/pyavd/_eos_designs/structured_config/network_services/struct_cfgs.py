# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import append_if_not_duplicate

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class StructCfgsMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def struct_cfgs(self: AvdStructuredConfigNetworkServices) -> list | None:
        """Return the combined structured config from VRFs."""
        if not self.shared_utils.network_services_l3:
            return None

        vrf_struct_cfgs = []
        for tenant in self.shared_utils.filtered_tenants:
            for vrf in tenant.vrfs:
                if vrf.structured_config:
                    # Inserting VRF into structured_config to perform duplication checks
                    vrf_struct_cfg = {"vrf": vrf.name, "struct_cfg": vrf.structured_config._as_dict()}
                    append_if_not_duplicate(
                        list_of_dicts=vrf_struct_cfgs,
                        primary_key="vrf",
                        new_dict=vrf_struct_cfg,
                        context="Structured Config for VRF '{vrf['name']}'",
                        context_keys=["vrf"],
                    )

        if vrf_struct_cfgs:
            return [vrf_struct_cfg["struct_cfg"] for vrf_struct_cfg in vrf_struct_cfgs]

        return None
