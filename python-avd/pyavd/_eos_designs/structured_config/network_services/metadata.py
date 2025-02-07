# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._utils import get, get_all

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServicesProtocol


class MetadataMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def metadata(self: AvdStructuredConfigNetworkServicesProtocol) -> None:
        """
        Generate metadata.cv_pathfinder for CV Pathfinder routers.

        Pathfinders will always have applications since we have the default control plane apps.
        Edge routers may have internet_exit_policies but not applications.
        """
        if not self.shared_utils.is_cv_pathfinder_router:
            return
        if self._filtered_internet_exit_policies_and_connections:
            self.structured_config.metadata.cv_pathfinder._update(internet_exit_policies=self.get_cv_pathfinder_metadata_internet_exit_policies())
        if self.shared_utils.is_cv_pathfinder_server and self.application_traffic_recognition is not None:
            self.structured_config.metadata.cv_pathfinder._update(applications=self.get_cv_pathfinder_metadata_applications())

    def get_cv_pathfinder_metadata_internet_exit_policies(
        self: AvdStructuredConfigNetworkServicesProtocol,
    ) -> EosCliConfigGen.Metadata.CvPathfinder.InternetExitPolicies:
        """Generate metadata.cv_pathfinder.internet_exit_policies if available."""
        internet_exit_polices = EosCliConfigGen.Metadata.CvPathfinder.InternetExitPolicies()
        for internet_exit_policy, connections in self._filtered_internet_exit_policies_and_connections:
            # Currently only supporting zscaler
            if internet_exit_policy.type != "zscaler":
                continue

            ufqdn, ipsec_key = self._get_ipsec_credentials(internet_exit_policy)
            internet_exit_police = EosCliConfigGen.Metadata.CvPathfinder.InternetExitPoliciesItem(
                name=internet_exit_policy.name,
                type=internet_exit_policy.type,
                city=self._zscaler_endpoints.device_location.city,
                country=self._zscaler_endpoints.device_location.country,
                upload_bandwidth=internet_exit_policy.zscaler.upload_bandwidth,
                download_bandwidth=internet_exit_policy.zscaler.download_bandwidth,
                firewall=internet_exit_policy.zscaler.firewall.enabled,
                ips_control=internet_exit_policy.zscaler.firewall.ips,
                acceptable_use_policy=internet_exit_policy.zscaler.acceptable_use_policy,
            )
            internet_exit_police.vpn_credentials.append(
                EosCliConfigGen.Metadata.CvPathfinder.InternetExitPoliciesItem.VpnCredentialsItem(fqdn=ufqdn, vpn_type="UFQDN", pre_shared_key=ipsec_key)
            )
            tunnels = EosCliConfigGen.Metadata.CvPathfinder.InternetExitPoliciesItem.Tunnels()
            for connection in connections:
                tunnels.append(
                    EosCliConfigGen.Metadata.CvPathfinder.InternetExitPoliciesItem.TunnelsItem(
                        name=f"Tunnel{connection['tunnel_id']}",
                        preference="Preferred" if connection["preference"] == "primary" else "Alternate",
                        endpoint=connection["endpoint"],
                    )
                )
            internet_exit_police.tunnels = tunnels
            internet_exit_polices.append(internet_exit_police)
        return internet_exit_polices

    def get_cv_pathfinder_metadata_applications(self: AvdStructuredConfigNetworkServicesProtocol) -> EosCliConfigGen.Metadata.CvPathfinder.Applications:
        """Generate metadata.cv_pathfinder.applications if available."""
        applications = get(self.application_traffic_recognition, "applications", default=[])
        user_defined_app_names = set(get_all(applications, "ipv4_applications.name") + get_all(applications, "ipv6_applications.name"))

        categories = get(self.application_traffic_recognition, "categories", default=[])
        cv_pathfinder_metadata_applications = EosCliConfigGen.Metadata.CvPathfinder.Applications()
        profiles = EosCliConfigGen.Metadata.CvPathfinder.Applications.Profiles()
        for profile in get(self.application_traffic_recognition, "application_profiles", default=[]):
            application_profile = EosCliConfigGen.Metadata.CvPathfinder.Applications.ProfilesItem(
                name=profile["name"], transport_protocols=get(profile, "application_transports", default=[])
            )
            for application in get(profile, "applications", default=[]):
                if application["name"] not in user_defined_app_names:
                    profile_builtin_application = application_profile.BuiltinApplicationsItem(
                        name=application["name"], services=get_all(application, "service")
                    )
                    application_profile.builtin_applications.append(profile_builtin_application)
                if application["name"] in user_defined_app_names:
                    profile_user_defined_application = application_profile.UserDefinedApplicationsItem(name=application["name"])
                    application_profile.user_defined_applications.append(profile_user_defined_application)
            for category in get(profile, "categories", default=[]):
                profile_category = application_profile.CategoriesItem(category=category["name"], services=get_all(category, "service"))
                application_profile.categories.append(profile_category)
        cv_pathfinder_metadata_applications.profiles = profiles
        category_builtin_applications = EosCliConfigGen.Metadata.CvPathfinder.Applications.Categories.BuiltinApplications()
        category_user_defined_applications = EosCliConfigGen.Metadata.CvPathfinder.Applications.Categories.UserDefinedApplications()
        for category in categories:
            for application in get(category, "applications", default=[]):
                if application["name"] not in user_defined_app_names:
                    category_builtin_applications.append(
                        EosCliConfigGen.Metadata.CvPathfinder.Applications.Categories.BuiltinApplicationsItem(
                            name=application["name"], category=category["name"], services=get(category, "service")
                        )
                    )
                if application["name"] in user_defined_app_names:
                    category_user_defined_applications.append(
                        EosCliConfigGen.Metadata.CvPathfinder.Applications.Categories.UserDefinedApplicationsItem(
                            name=application["name"], category=category["name"]
                        )
                    )
        cv_pathfinder_metadata_applications.categories._update(
            builtin_applications=category_builtin_applications, user_defined_applications=category_user_defined_applications
        )
        return cv_pathfinder_metadata_applications
