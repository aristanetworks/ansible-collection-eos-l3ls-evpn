<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>wan_encapsulation</samp>](## "wan_encapsulation") | String |  | `path-selection` | Valid Values:<br>- <code>path-selection</code><br>- <code>vxlan</code> | Select the encapsulation to use for EVPN peerings for WAN BGP peers. |
    | [<samp>wan_ha</samp>](## "wan_ha") | Dictionary |  |  |  | PREVIEW: The `wan_ha` key is currently not supported. |
    | [<samp>&nbsp;&nbsp;lan_ha_path_group_name</samp>](## "wan_ha.lan_ha_path_group_name") | String |  | `LAN_HA` |  | When WAN HA is enabled for a site if `wan_mode: cv-pathfinder`, a default path-group is injected to form DPS tunnels over LAN.<br>This key allows to overwrite the default LAN HA path-group name. |
    | [<samp>wan_ipsec_profiles</samp>](## "wan_ipsec_profiles") | Dictionary |  |  |  | Define IPsec profiles parameters for WAN configuration. |
    | [<samp>&nbsp;&nbsp;control_plane</samp>](## "wan_ipsec_profiles.control_plane") | Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ike_policy_name</samp>](## "wan_ipsec_profiles.control_plane.ike_policy_name") | String |  | `CP-IKE-POLICY` |  | Name of the IKE policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sa_policy_name</samp>](## "wan_ipsec_profiles.control_plane.sa_policy_name") | String |  | `CP-SA-POLICY` |  | Name of the SA policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;profile_name</samp>](## "wan_ipsec_profiles.control_plane.profile_name") | String |  | `CP-PROFILE` |  | Name of the IPSec profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shared_key</samp>](## "wan_ipsec_profiles.control_plane.shared_key") | String | Required |  |  | The IPSec shared key.<br>This variable is sensitive and SHOULD be configured using some vault mechanism. |
    | [<samp>&nbsp;&nbsp;data_plane</samp>](## "wan_ipsec_profiles.data_plane") | Dictionary |  |  |  | If `data_plane` is not defined, `control_plane` information is used for both. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ike_policy_name</samp>](## "wan_ipsec_profiles.data_plane.ike_policy_name") | String |  | `DP-IKE-POLICY` |  | Name of the IKE policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sa_policy_name</samp>](## "wan_ipsec_profiles.data_plane.sa_policy_name") | String |  | `DP-SA-POLICY` |  | Name of the SA policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;profile_name</samp>](## "wan_ipsec_profiles.data_plane.profile_name") | String |  | `DP-PROFILE` |  | Name of the IPSec profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shared_key</samp>](## "wan_ipsec_profiles.data_plane.shared_key") | String | Required |  |  | The type 7 encrypted IPSec shared key.<br>This variable is sensitive and should be configured using some vault mechanism. |
    | [<samp>wan_mode</samp>](## "wan_mode") | String |  | `cv-pathfinder` | Valid Values:<br>- <code>autovpn</code><br>- <code>cv-pathfinder</code> | Select if the WAN should be run using CV Pathfinder or AutoVPN only. |
    | [<samp>wan_stun_dtls_disable</samp>](## "wan_stun_dtls_disable") | Boolean |  | `False` |  | WAN STUN connections are authenticated and secured with DTLS by default.<br>For CV Pathfinder deployments CloudVision will automatically deploy certificates on the devices.<br>In case of AutoVPN the certificates must be deployed manually to all devices.<br><br>For LAB environments this can be disabled, if there are no certificates available.<br>This should NOT be disabled for a WAN network connected to the internet, since it will leave the STUN service exposed with no authentication. |
    | [<samp>wan_stun_dtls_profile_name</samp>](## "wan_stun_dtls_profile_name") | String |  | `STUN-DTLS` |  | Name of the SSL profile used for DTLS on WAN STUN connections.<br>When using automatic ceritficate deployment via CloudVision this name must be the same on all WAN routers. |

=== "YAML"

    ```yaml
    # Select the encapsulation to use for EVPN peerings for WAN BGP peers.
    wan_encapsulation: <str; "path-selection" | "vxlan"; default="path-selection">

    # PREVIEW: The `wan_ha` key is currently not supported.
    wan_ha:

      # When WAN HA is enabled for a site if `wan_mode: cv-pathfinder`, a default path-group is injected to form DPS tunnels over LAN.
      # This key allows to overwrite the default LAN HA path-group name.
      lan_ha_path_group_name: <str; default="LAN_HA">

    # Define IPsec profiles parameters for WAN configuration.
    wan_ipsec_profiles:
      control_plane: # required

        # Name of the IKE policy.
        ike_policy_name: <str; default="CP-IKE-POLICY">

        # Name of the SA policy.
        sa_policy_name: <str; default="CP-SA-POLICY">

        # Name of the IPSec profile.
        profile_name: <str; default="CP-PROFILE">

        # The IPSec shared key.
        # This variable is sensitive and SHOULD be configured using some vault mechanism.
        shared_key: <str; required>

      # If `data_plane` is not defined, `control_plane` information is used for both.
      data_plane:

        # Name of the IKE policy.
        ike_policy_name: <str; default="DP-IKE-POLICY">

        # Name of the SA policy.
        sa_policy_name: <str; default="DP-SA-POLICY">

        # Name of the IPSec profile.
        profile_name: <str; default="DP-PROFILE">

        # The type 7 encrypted IPSec shared key.
        # This variable is sensitive and should be configured using some vault mechanism.
        shared_key: <str; required>

    # Select if the WAN should be run using CV Pathfinder or AutoVPN only.
    wan_mode: <str; "autovpn" | "cv-pathfinder"; default="cv-pathfinder">

    # WAN STUN connections are authenticated and secured with DTLS by default.
    # For CV Pathfinder deployments CloudVision will automatically deploy certificates on the devices.
    # In case of AutoVPN the certificates must be deployed manually to all devices.
    #
    # For LAB environments this can be disabled, if there are no certificates available.
    # This should NOT be disabled for a WAN network connected to the internet, since it will leave the STUN service exposed with no authentication.
    wan_stun_dtls_disable: <bool; default=False>

    # Name of the SSL profile used for DTLS on WAN STUN connections.
    # When using automatic ceritficate deployment via CloudVision this name must be the same on all WAN routers.
    wan_stun_dtls_profile_name: <str; default="STUN-DTLS">
    ```
