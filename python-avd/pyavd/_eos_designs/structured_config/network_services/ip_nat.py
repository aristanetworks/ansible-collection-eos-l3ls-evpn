# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class IpNatMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def ip_nat(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """Returns structured config for ip_nat."""
        if not self.shared_utils.is_cv_pathfinder_client:
            return

        for policy_type in self._filtered_internet_exit_policy_types:
            pool, profile = self.get_internet_exit_nat_pool_and_profile(policy_type)
            if pool:
                self.structured_config.ip_nat.pools.append(pool)
            if profile:
                self.structured_config.ip_nat.profiles.append(profile)
