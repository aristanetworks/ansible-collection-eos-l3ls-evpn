# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._eos_designs.structured_config.structured_config_generator import structured_config_contributor
from pyavd._errors import AristaAvdMissingVariableError

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

    from . import AvdStructuredConfigOverlayProtocol


class IpSecurityMixin(Protocol):
    """
    Mixin Class used to generate structured config for one key.

    Class should only be used as Mixin to a AvdStructuredConfig class.
    """

    @structured_config_contributor
    def ip_security(self: AvdStructuredConfigOverlayProtocol) -> None:
        """
        ip_security set based on wan_ipsec_profiles data_model.

        If `data_plane` is not configured, `control_plane` data is used for both
        Data Plane and Control Plane.
        """
        # TODO: - in future, the default algo/dh groups value must be clarified

        if not self.shared_utils.is_wan_router:
            return

        if not self.inputs.wan_ipsec_profiles:
            msg = "wan_ipsec_profiles"
            raise AristaAvdMissingVariableError(msg)
        if not self.inputs.wan_ipsec_profiles.control_plane:
            msg = "wan_ipsec_profiles.control_plane"
            raise AristaAvdMissingVariableError(msg)

        if self.shared_utils.is_wan_client and self.inputs.wan_ipsec_profiles.data_plane:
            self._append_data_plane(self.inputs.wan_ipsec_profiles.data_plane)
        self._append_control_plane(self.inputs.wan_ipsec_profiles.control_plane)

    def _append_data_plane(self: AvdStructuredConfigOverlayProtocol, data_plane_config: EosDesigns.WanIpsecProfiles.DataPlane) -> None:
        """In place update of ip_security for DataPlane."""
        ike_policy_name = data_plane_config.ike_policy_name if self.shared_utils.wan_ha_ipsec else None
        sa_policy_name = data_plane_config.sa_policy_name
        profile_name = data_plane_config.profile_name
        key = data_plane_config.shared_key

        # IKE policy for data-plane is not required for dynamic tunnels except for HA cases
        if self.shared_utils.wan_ha_ipsec:
            self.structured_config.ip_security.ike_policies.append_new(name=ike_policy_name, local_id=self.shared_utils.vtep_ip)
        self._set_sa_policy(sa_policy_name)
        self._profile(profile_name, ike_policy_name, sa_policy_name, key)

        # For data plane, adding key_controller by default
        self._key_controller(profile_name)

    def _append_control_plane(self: AvdStructuredConfigOverlayProtocol, control_plane_config: EosDesigns.WanIpsecProfiles.ControlPlane) -> None:
        """
        In place update of ip_security for control plane data.

        expected to be called AFTER _append_data_plane as CP is used for data-plane as well if not configured.
        """
        ike_policy_name = control_plane_config.ike_policy_name
        sa_policy_name = control_plane_config.sa_policy_name
        profile_name = control_plane_config.profile_name
        key = control_plane_config.shared_key

        self.structured_config.ip_security.ike_policies.append_new(name=ike_policy_name, local_id=self.shared_utils.vtep_ip)
        self._set_sa_policy(sa_policy_name)
        self._profile(profile_name, ike_policy_name, sa_policy_name, key)

        if not self.structured_config.ip_security.key_controller:
            # If there is no data plane IPSec profile, use the control plane one for key controller
            self._key_controller(profile_name)

    def _set_sa_policy(self: AvdStructuredConfigOverlayProtocol, name: str) -> None:
        """
        Set the SA policy.

        By default using aes256gcm128 as GCM variants give higher performance.
        """
        sa_policy = EosCliConfigGen.IpSecurity.SaPoliciesItem(name=name)
        if self.shared_utils.is_cv_pathfinder_router:
            # TODO: provide options to change this cv_pathfinder_wide
            sa_policy.esp.encryption = "aes256gcm128"
            sa_policy.pfs_dh_group = 14
        self.structured_config.ip_security.sa_policies.append(sa_policy)

    def _profile(self: AvdStructuredConfigOverlayProtocol, profile_name: str, ike_policy_name: str | None, sa_policy_name: str, key: str) -> None:
        """
        Set the IPsec Profile.

        The expectation is that potential None values are stripped later.

        Using connection start on all routers as using connection add on Pathfinders
        as suggested would prevent Pathfinders to establish IPsec tunnels between themselves
        which is undesirable.
        """
        if self.shared_utils.wan_role is not None:
            self.structured_config.ip_security.profiles.append_new(
                name=profile_name,
                ike_policy=ike_policy_name,
                sa_policy=sa_policy_name,
                connection="start",
                shared_key=key,
                mode="transport",
                dpd=EosCliConfigGen.IpSecurity.ProfilesItem.Dpd(interval=10, time=50, action="clear"),
            )

    def _key_controller(self: AvdStructuredConfigOverlayProtocol, profile_name: str) -> None:
        """Set the key_controller structure if the device is not a RR or pathfinder."""
        if self.shared_utils.is_wan_server:
            return
        self.structured_config.ip_security.key_controller.profile = profile_name
