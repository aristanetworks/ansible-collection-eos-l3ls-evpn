# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import strip_null_from_data

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class IpSecurityMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def ip_security(self: AvdStructuredConfigNetworkServices) -> dict | None:
        """ip_security set based on cv_pathfinder_internet_exit_policies."""
        if not self._filtered_internet_exit_policies_and_connections:
            return None

        ip_security = {"ike_policies": [], "sa_policies": [], "profiles": []}
        for internet_exit_policy, _connections in self._filtered_internet_exit_policies_and_connections:
            # Currently we only need ipsec for zscaler.
            if internet_exit_policy.type != "zscaler":
                continue

            policy_name = internet_exit_policy.name
            encrypt_traffic = internet_exit_policy.zscaler.encrypt_traffic
            ike_policy_name = f"IE-{policy_name}-IKE-POLICY"
            sa_policy_name = f"IE-{policy_name}-SA-POLICY"
            profile_name = f"IE-{policy_name}-PROFILE"
            ufqdn, ipsec_key = self._get_ipsec_credentials(internet_exit_policy)

            ip_security["ike_policies"].append(
                {
                    "name": ike_policy_name,
                    "local_id_fqdn": ufqdn,
                    "ike_lifetime": 24,
                    "encryption": "aes256",
                    "dh_group": 24,
                },
            )
            ip_security["sa_policies"].append(
                {
                    "name": sa_policy_name,
                    "pfs_dh_group": 24,
                    "sa_lifetime": {"value": 8},
                    "esp": {
                        "integrity": "sha256",
                        "encryption": "aes256" if encrypt_traffic else "disabled",
                    },
                },
            )
            ip_security["profiles"].append(
                {
                    "name": profile_name,
                    "ike_policy": ike_policy_name,
                    "sa_policy": sa_policy_name,
                    "shared_key": ipsec_key,
                    "dpd": {
                        "interval": 10,
                        "time": 60,
                        "action": "clear",
                    },
                    "connection": "start",
                },
            )

        return strip_null_from_data(ip_security) or None
