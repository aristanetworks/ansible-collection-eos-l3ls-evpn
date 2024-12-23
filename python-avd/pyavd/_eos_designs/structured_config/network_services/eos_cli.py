# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class EosCliMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def eos_cli(self: AvdStructuredConfigNetworkServices) -> str | None:
        """Return existing eos_cli plus any eos_cli from VRFs."""
        if not self.shared_utils.network_services_l3:
            return None

        eos_clis = []
        if (eos_cli := self.structured_config.eos_cli) is not None:
            eos_clis.append(eos_cli)

        eos_clis.extend(vrf.raw_eos_cli for tenant in self.shared_utils.filtered_tenants for vrf in tenant.vrfs if vrf.raw_eos_cli is not None)

        if eos_clis:
            return "\n".join(eos_clis)

        return None
