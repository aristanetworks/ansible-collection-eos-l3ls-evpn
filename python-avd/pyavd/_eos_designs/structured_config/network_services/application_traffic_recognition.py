# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property, partial
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdInvalidInputsError
from pyavd._utils import append_if_not_duplicate, get, get_item, strip_empties_from_dict

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigNetworkServices


class ApplicationTrafficRecognitionMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def application_traffic_recognition(self: AvdStructuredConfigNetworkServices) -> dict | None:
        """Return structured config for application_traffic_recognition if wan router."""
        if not self.shared_utils.is_wan_router:
            return None

        filtered_application_classification = self._filtered_application_classification()

        self._generate_control_plane_application_profile(filtered_application_classification)

        return strip_empties_from_dict(filtered_application_classification)

    #  self._wan_control_plane_application_profile is defined in utils.py
    @cached_property
    def _wan_control_plane_application(self: AvdStructuredConfigNetworkServices) -> str:
        return "APP-CONTROL-PLANE"

    @cached_property
    def _wan_cp_app_dst_prefix(self: AvdStructuredConfigNetworkServices) -> str:
        return "PFX-PATHFINDERS"

    @cached_property
    def _wan_cp_app_src_prefix(self: AvdStructuredConfigNetworkServices) -> str:
        return "PFX-LOCAL-VTEP-IP"

    def _generate_control_plane_application_profile(self: AvdStructuredConfigNetworkServices, app_dict: dict) -> None:
        """
        Generate an application profile using a single application matching.

        * the device Pathfinders vtep_ips as destination for non Pathfinders.
        * the device Pathfinder vtep_ip as source.

        Create a structure as follow. If any object already exist, it is kept as defined by user and override the defaults.

        Edge and Transit:

            application_traffic_recognition:
              application_profiles:
                - name: APP-PROFILE-CONTROL-PLANE
                  applications:
                    - name: APP-CONTROL-PLANE
              applications:
                ipv4_applications:
                  - name: APP-CONTROL-PLANE
                    dest_prefix_set_name: PFX-PATHFINDERS
              field_sets:
                ipv4_prefixes:
                  - name: PFX-PATHFINDERS
                    prefix_values: [Pathfinder to which the router is connected vtep_ips]

        Pathfinder:

            application_traffic_recognition:
              application_profiles:
                - name: APP-PROFILE-CONTROL-PLANE
                  applications:
                    - name: APP-CONTROL-PLANE
              applications:
                ipv4_applications:
                  - name: APP-CONTROL-PLANE
                    src_prefix_set_name: PFX-LOCAL-VTEP-IP
              field_sets:
                ipv4_prefixes:
                  - name: PFX-LOCAL-VTEP-IP
                    prefix_values: [Pathfinder vtep_ip]
        """
        # Adding the application-profile
        application_profiles = get(app_dict, "application_profiles", [])
        if get_item(application_profiles, "name", self._wan_control_plane_application_profile_name) is not None:
            return
        app_dict.setdefault("application_profiles", []).append(
            {
                "name": self._wan_control_plane_application_profile_name,
                "applications": [
                    {
                        "name": self._wan_control_plane_application,
                    },
                ],
            },
        )
        # Adding the application
        ipv4_applications = get(app_dict, "applications.ipv4_applications", [])
        if get_item(ipv4_applications, "name", self._wan_control_plane_application) is not None:
            return
        if self.shared_utils.is_wan_client:
            app_dict.setdefault("applications", {}).setdefault("ipv4_applications", []).append(
                {
                    "name": self._wan_control_plane_application,
                    "dest_prefix_set_name": self._wan_cp_app_dst_prefix,
                },
            )
            # Adding the field-set based on the connected Pathfinder router-ids
            ipv4_prefixes_field_sets = get(app_dict, "field_sets.ipv4_prefixes", [])
            if get_item(ipv4_prefixes_field_sets, "name", self._wan_cp_app_dst_prefix) is not None:
                return
            pathfinder_vtep_ips = [f"{wan_rs.vtep_ip}/32" for wan_rs in self.shared_utils.filtered_wan_route_servers]
            app_dict.setdefault("field_sets", {}).setdefault("ipv4_prefixes", []).append(
                {
                    "name": self._wan_cp_app_dst_prefix,
                    "prefix_values": pathfinder_vtep_ips,
                },
            )
        elif self.shared_utils.is_wan_server:
            app_dict.setdefault("applications", {}).setdefault("ipv4_applications", []).append(
                {
                    "name": self._wan_control_plane_application,
                    "src_prefix_set_name": self._wan_cp_app_src_prefix,
                },
            )
            app_dict.setdefault("field_sets", {}).setdefault("ipv4_prefixes", []).append(
                {"name": self._wan_cp_app_src_prefix, "prefix_values": [f"{self.shared_utils.vtep_ip}/32"]},
            )

    def _filtered_application_classification(self: AvdStructuredConfigNetworkServices) -> dict:
        """
        Based on the filtered policies local to the device, filter which application profiles should be configured on the device.

        Supports only `application_classification.applications.ipv4_applications` for now.

        For applications - the existence cannot be verified as there are 4000+ applications built-in in the DPI engine used by EOS.
        """
        # Application profiles first
        application_profiles = []

        append_dict_to_list_of_dicts = partial(append_if_not_duplicate, primary_key="name", context="Application traffic recognition", context_keys=["name"])

        for policy in self._filtered_wan_policies:
            if policy.get("is_default") and self._wan_control_plane_application_profile_name in self.inputs.application_classification.application_profiles:
                append_dict_to_list_of_dicts(
                    list_of_dicts=application_profiles,
                    new_dict=self.inputs.application_classification.application_profiles[self._wan_control_plane_application_profile_name]._as_dict(),
                )

            for match in get(policy, "matches", []):
                application_profile = get(match, "application_profile", required=True)

                if application_profile not in self.inputs.application_classification.application_profiles:
                    if application_profile == self._wan_control_plane_application_profile_name:
                        # Ignore for control plane as it could be injected later.
                        continue

                    msg = (
                        f"The application profile {application_profile} used in policy {policy['name']} "
                        "is not defined in 'application_classification.application_profiles'."
                    )
                    raise AristaAvdInvalidInputsError(msg)

                append_dict_to_list_of_dicts(
                    list_of_dicts=application_profiles, new_dict=self.inputs.application_classification.application_profiles[application_profile]._as_dict()
                )

            if (default_match := policy.get("default_match")) is not None:
                application_profile = get(default_match, "application_profile", default="default")
                if application_profile != "default":
                    if application_profile not in self.inputs.application_classification.application_profiles:
                        msg = (
                            f"The application profile {application_profile} used in policy {policy['name']} "
                            "is not defined in 'application_classification.application_profiles'."
                        )
                        raise AristaAvdInvalidInputsError(msg)

                    append_dict_to_list_of_dicts(
                        list_of_dicts=application_profiles, new_dict=self.inputs.application_classification.application_profiles[application_profile]._as_dict()
                    )

        output = {"application_profiles": application_profiles}
        # Now handle categories, applicaations
        categories = []
        applications = []

        for application_profile in application_profiles:
            for category in get(application_profile, "categories", default=[]):
                if category["name"] not in self.inputs.application_classification.categories:
                    msg = (
                        f"The application profile {application_profile['name']} uses the category {category['name']} "
                        "undefined in 'application_classification.categories'."
                    )
                    raise AristaAvdInvalidInputsError(msg)
                append_dict_to_list_of_dicts(new_dict=self.inputs.application_classification.categories[category["name"]]._as_dict(), list_of_dicts=categories)
            # Applications in application profiles
            for application in get(application_profile, "applications", default=[]):
                if application["name"] in self.inputs.application_classification.applications.ipv4_applications:
                    append_dict_to_list_of_dicts(
                        new_dict=self.inputs.application_classification.applications.ipv4_applications[application["name"]]._as_dict(),
                        list_of_dicts=applications,
                    )
        # Applications in categories
        for category in categories:
            for application in get(category, "applications", default=[]):
                if application["name"] in self.inputs.application_classification.applications.ipv4_applications:
                    append_dict_to_list_of_dicts(
                        new_dict=self.inputs.application_classification.applications.ipv4_applications[application["name"]]._as_dict(),
                        list_of_dicts=applications,
                    )

        output["categories"] = categories
        # IPv4 only for now
        output["applications"] = {"ipv4_applications": applications}
        # Now filtering port sets and ipv4 sets
        l4_ports = []
        ipv4_prefixes = []
        for application in applications:
            for prefix_set_key in ("src_prefix_set_name", "dest_prefix_set_name"):
                if (prefix_set_name := get(application, prefix_set_key)) is not None:
                    if prefix_set_name not in self.inputs.application_classification.field_sets.ipv4_prefixes:
                        msg = (
                            f"The IPv4 prefix field set {prefix_set_name} used in the application {application} "
                            "is undefined in 'application_classification.fields_sets.ipv4_prefixes'."
                        )
                        raise AristaAvdInvalidInputsError(msg)
                    append_dict_to_list_of_dicts(
                        new_dict=self.inputs.application_classification.field_sets.ipv4_prefixes[prefix_set_name]._as_dict(), list_of_dicts=ipv4_prefixes
                    )

            for port_set_key in ("udp_src_port_set_name", "udp_dest_port_set_name", "tcp_src_port_set_name", "tcp_dest_port_set_name"):
                if (port_set_name := get(application, port_set_key)) is not None:
                    if port_set_name not in self.inputs.application_classification.field_sets.l4_ports:
                        msg = (
                            f"The L4 Ports field set {port_set_name} used in the application {application} "
                            "is undefined in 'application_classification.fields_sets.l4_ports'."
                        )
                        raise AristaAvdInvalidInputsError(msg)
                    append_dict_to_list_of_dicts(
                        new_dict=self.inputs.application_classification.field_sets.l4_ports[port_set_name]._as_dict(), list_of_dicts=l4_ports
                    )

        output["field_sets"] = {
            "l4_ports": l4_ports,
            "ipv4_prefixes": ipv4_prefixes,
        }

        return output
