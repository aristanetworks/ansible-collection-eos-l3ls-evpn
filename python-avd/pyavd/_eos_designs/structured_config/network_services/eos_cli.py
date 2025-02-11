# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class EosCliMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def eos_cli(self: AvdStructuredConfigNetworkServicesProtocol) -> str | None:
        """Return existing eos_cli plus any eos_cli from VRFs."""
        if not self.shared_utils.network_services_l3:
            return None

        eos_clis = []
        # Find any existing eos_cli set by AvdStructuredConfigBase.
        # Depending on the render() logic this may be in self.structured_config or in self._complete_structured_config
        if self.structured_config.eos_cli is not None:
            eos_clis.append(self.structured_config.eos_cli)
        elif hasattr(self, "_complete_structured_config") and self._complete_structured_config.eos_cli is not None:
            eos_clis.append(self._complete_structured_config.eos_cli)

        eos_clis.extend(vrf.raw_eos_cli for tenant in self.shared_utils.filtered_tenants for vrf in tenant.vrfs if vrf.raw_eos_cli is not None)

        if eos_clis:
            return "\n".join(eos_clis)

        return None
