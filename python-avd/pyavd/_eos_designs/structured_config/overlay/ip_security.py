# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from pyavd._utils import get, strip_null_from_data

from .utils import UtilsMixin

if TYPE_CHECKING:
    from . import AvdStructuredConfigOverlay


class IpSecurityMixin(UtilsMixin):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @cached_property
    def ip_security(self: AvdStructuredConfigOverlay) -> dict | None:
        """
        ip_security set based on wan_ipsec_profiles data_model.

        If `data_plane` is not configured, `control_plane` data is used for both
        Data Plane and Control Plane.
        """
        # TODO: - in future, the default algo/dh groups value must be clarified

        if not self.shared_utils.is_wan_router:
            return None

        wan_ipsec_profiles = get(self._hostvars, "wan_ipsec_profiles", required=True)

        # Structure initialization
        ip_security = {"ike_policies": [], "sa_policies": [], "profiles": []}

        if self.shared_utils.is_wan_client and (data_plane := get(wan_ipsec_profiles, "data_plane")) is not None:
            self._append_data_plane(ip_security, data_plane)
        control_plane = get(wan_ipsec_profiles, "control_plane", required=True)
        self._append_control_plane(ip_security, control_plane)

        return strip_null_from_data(ip_security)

    def _append_data_plane(self: AvdStructuredConfigOverlay, ip_security: dict, data_plane_config: dict) -> None:
        """In place update of ip_security for DataPlane."""
        ike_policy_name = get(data_plane_config, "ike_policy_name", default="DP-IKE-POLICY") if self.shared_utils.wan_ha_ipsec else None
        sa_policy_name = get(data_plane_config, "sa_policy_name", default="DP-SA-POLICY")
        profile_name = get(data_plane_config, "profile_name", default="DP-PROFILE")
        key = get(data_plane_config, "shared_key", required=True)

        # IKE policy for data-plane is not required for dynamic tunnels except for HA cases
        if self.shared_utils.wan_ha_ipsec:
            ip_security["ike_policies"].append(self._ike_policy(ike_policy_name))
        ip_security["sa_policies"].append(self._sa_policy(sa_policy_name))
        ip_security["profiles"].append(self._profile(profile_name, ike_policy_name, sa_policy_name, key))

        # For data plane, adding key_controller by default
        ip_security["key_controller"] = self._key_controller(profile_name)

    def _append_control_plane(self: AvdStructuredConfigOverlay, ip_security: dict, control_plane_config: dict) -> None:
        """
        In place update of ip_security for control plane data.

        expected to be called AFTER _append_data_plane as CP is used for data-plane as well if not configured.
        """
        ike_policy_name = get(control_plane_config, "ike_policy_name", default="CP-IKE-POLICY")
        sa_policy_name = get(control_plane_config, "sa_policy_name", default="CP-SA-POLICY")
        profile_name = get(control_plane_config, "profile_name", default="CP-PROFILE")
        key = get(control_plane_config, "shared_key", required=True)

        ip_security["ike_policies"].append(self._ike_policy(ike_policy_name))
        ip_security["sa_policies"].append(self._sa_policy(sa_policy_name))
        ip_security["profiles"].append(self._profile(profile_name, ike_policy_name, sa_policy_name, key))

        if not ip_security.get("key_controller"):
            # If there is no data plane IPSec profile, use the control plane one for key controller
            ip_security["key_controller"] = self._key_controller(profile_name)

    def _ike_policy(self: AvdStructuredConfigOverlay, name: str) -> dict | None:
        """Return an IKE policy."""
        return {
            "name": name,
            "local_id": self.shared_utils.vtep_ip,
        }

    def _sa_policy(self: AvdStructuredConfigOverlay, name: str) -> dict | None:
        """
        Return an SA policy.

        By default using aes256gcm128 as GCM variants give higher performance.
        """
        sa_policy = {"name": name}
        if self.shared_utils.is_cv_pathfinder_router:
            # TODO: provide options to change this cv_pathfinder_wide
            sa_policy["esp"] = {"encryption": "aes256gcm128"}
            sa_policy["pfs_dh_group"] = 14
        return sa_policy

    def _profile(self: AvdStructuredConfigOverlay, profile_name: str, ike_policy_name: str | None, sa_policy_name: str, key: str) -> dict | None:
        """
        Return one IPsec Profile.

        The expectation is that potential None values are stripped later.

        Using connection start on all routers as using connection add on Pathfinders
        as suggested would prevent Pathfinders to establish IPsec tunnels between themselves
        which is undesirable.
        """
        if self.shared_utils.wan_role is None:
            return None

        return {
            "name": profile_name,
            "ike_policy": ike_policy_name,
            "sa_policy": sa_policy_name,
            "connection": "start",
            "shared_key": key,
            "dpd": {"interval": 10, "time": 50, "action": "clear"},
            "mode": "transport",
        }

    def _key_controller(self: AvdStructuredConfigOverlay, profile_name: str) -> dict | None:
        """Return a key_controller structure if the device is not a RR or pathfinder."""
        return None if self.shared_utils.is_wan_server else {"profile": profile_name}
