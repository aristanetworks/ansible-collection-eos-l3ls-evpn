# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class StructCfgsMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def struct_cfgs(self: AvdStructuredConfigNetworkServices) -> None:
        """Return the combined structured config from VRFs."""
        if not self.shared_utils.network_services_l3:
            return None

        for tenant in self.shared_utils.filtered_tenants:
            self.custom_structured_configs.root.extend(vrf.structured_config for vrf in tenant.vrfs if vrf.structured_config)

        return None
