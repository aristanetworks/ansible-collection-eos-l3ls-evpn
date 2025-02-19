# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
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
        """Set the structured config for ip_nat."""
        if not self.shared_utils.is_cv_pathfinder_client:
            return

        for policy_type in self._filtered_internet_exit_policy_types:
            if policy_type == "zscaler":
                pool = EosCliConfigGen.IpNat.PoolsItem(name="PORT-ONLY-POOL", type="port-only")
                pool.ranges.append_new(first_port=1500, last_port=65535)
                self.structured_config.ip_nat.pools.append(pool)

                profile = EosCliConfigGen.IpNat.ProfilesItem(name=self.get_internet_exit_nat_profile_name(policy_type))
                profile.source.dynamic.append_new(
                    access_list=self.get_internet_exit_nat_acl_name(policy_type),
                    pool_name="PORT-ONLY-POOL",
                    nat_type="pool",
                )
                self.structured_config.ip_nat.profiles.append(profile)

            if policy_type == "direct":
                profile = EosCliConfigGen.IpNat.ProfilesItem(name=self.get_internet_exit_nat_profile_name(policy_type))
                profile.source.dynamic.append_new(
                    access_list=self.get_internet_exit_nat_acl_name(policy_type),
                    nat_type="overload",
                )
                self.structured_config.ip_nat.profiles.append(profile)
