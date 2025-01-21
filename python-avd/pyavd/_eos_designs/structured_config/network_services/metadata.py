# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import get, get_all, strip_empties_from_list, strip_null_from_data

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class MetadataMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def metadata(self: AvdStructuredConfigNetworkServices) -> dict | None:
        """
        Generate metadata.cv_pathfinder for CV Pathfinder routers.

        Pathfinders will always have applications since we have the default control plane apps.
        Edge routers may have internet_exit_policies but not applications.
        """
        if not self.shared_utils.is_cv_pathfinder_router:
            return None

        cv_pathfinder_metadata = strip_null_from_data(
            {
                "internet_exit_policies": self.get_cv_pathfinder_metadata_internet_exit_policies(),
                "applications": self.get_cv_pathfinder_metadata_applications(),
            },
        )
        if not cv_pathfinder_metadata:
            return None

        return {"cv_pathfinder": cv_pathfinder_metadata}

    def get_cv_pathfinder_metadata_internet_exit_policies(self: AvdStructuredConfigNetworkServices) -> list[dict] | None:
        """Generate metadata.cv_pathfinder.internet_exit_policies if available."""
        if not self._filtered_internet_exit_policies_and_connections:
            return None

        internet_exit_polices = []
        for internet_exit_policy, connections in self._filtered_internet_exit_policies_and_connections:
            # Currently only supporting zscaler
            if internet_exit_policy.type != "zscaler":
                continue

            ufqdn, ipsec_key = self._get_ipsec_credentials(internet_exit_policy)
            internet_exit_polices.append(
                {
                    "name": internet_exit_policy.name,
                    "type": internet_exit_policy.type,
                    "city": self._zscaler_endpoints.device_location.city,
                    "country": self._zscaler_endpoints.device_location.country,
                    "upload_bandwidth": internet_exit_policy.zscaler.upload_bandwidth,
                    "download_bandwidth": internet_exit_policy.zscaler.download_bandwidth,
                    "firewall": internet_exit_policy.zscaler.firewall.enabled,
                    "ips_control": internet_exit_policy.zscaler.firewall.ips,
                    "acceptable_use_policy": internet_exit_policy.zscaler.acceptable_use_policy,
                    "vpn_credentials": [
                        {
                            "fqdn": ufqdn,
                            "vpn_type": "UFQDN",
                            "pre_shared_key": ipsec_key,
                        },
                    ],
                    "tunnels": [
                        {
                            "name": f"Tunnel{connection['tunnel_id']}",
                            "preference": "Preferred" if connection["preference"] == "primary" else "Alternate",
                            "endpoint": connection["endpoint"],
                        }
                        for connection in connections
                    ],
                },
            )

        return strip_empties_from_list(internet_exit_polices, (None, [], {}))

    def get_cv_pathfinder_metadata_applications(self: AvdStructuredConfigNetworkServices) -> dict | None:
        """Generate metadata.cv_pathfinder.applications if available."""
        if not self.shared_utils.is_cv_pathfinder_server or self.application_traffic_recognition is None:
            return None

        applications = get(self.application_traffic_recognition, "applications", default=[])
        user_defined_app_names = set(get_all(applications, "ipv4_applications.name") + get_all(applications, "ipv6_applications.name"))

        categories = get(self.application_traffic_recognition, "categories", default=[])
        cv_pathfinder_metadata_applications = {
            "profiles": [
                {
                    "name": profile["name"],
                    "builtin_applications": [
                        {
                            "name": application["name"],
                            # Metadata expects a list of services but AVD model only supports a single service
                            "services": get_all(application, "service"),
                        }
                        for application in get(profile, "applications", default=[])
                        if application["name"] not in user_defined_app_names
                    ],
                    "user_defined_applications": [
                        {
                            "name": application["name"],
                        }
                        for application in get(profile, "applications", default=[])
                        if application["name"] in user_defined_app_names
                    ],
                    "categories": [
                        {
                            "category": category["name"],
                            # Metadata expects a list of services but AVD model only supports a single service
                            "services": get_all(category, "service"),
                        }
                        for category in get(profile, "categories", default=[])
                    ],
                    "transport_protocols": get(profile, "application_transports", default=[]),
                }
                for profile in get(self.application_traffic_recognition, "application_profiles", default=[])
            ],
            "categories": {
                "builtin_applications": [
                    {
                        "name": application["name"],
                        "category": category["name"],
                        "service": get(category, "service"),
                    }
                    for category in categories
                    for application in get(category, "applications", default=[])
                    if application["name"] not in user_defined_app_names
                ],
                "user_defined_applications": [
                    {
                        "name": application["name"],
                        "category": category["name"],
                    }
                    for category in categories
                    for application in get(category, "applications", default=[])
                    if application["name"] in user_defined_app_names
                ],
            },
        }

        return strip_null_from_data(cv_pathfinder_metadata_applications, (None, [], {}))
