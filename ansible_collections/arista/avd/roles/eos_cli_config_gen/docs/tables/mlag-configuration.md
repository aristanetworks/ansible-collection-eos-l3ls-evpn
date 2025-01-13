<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mlag_configuration</samp>](## "mlag_configuration") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;domain_id</samp>](## "mlag_configuration.domain_id") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;heartbeat_interval</samp>](## "mlag_configuration.heartbeat_interval") | Integer |  |  |  | Heartbeat interval in milliseconds. |
    | [<samp>&nbsp;&nbsp;local_interface</samp>](## "mlag_configuration.local_interface") | String |  |  |  | Local Interface Name. |
    | [<samp>&nbsp;&nbsp;peer_address</samp>](## "mlag_configuration.peer_address") | String |  |  |  | IPv4 or IPv6 Address. |
    | [<samp>&nbsp;&nbsp;peer_address_heartbeat</samp>](## "mlag_configuration.peer_address_heartbeat") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_ip</samp>](## "mlag_configuration.peer_address_heartbeat.peer_ip") | String |  |  |  | IPv4 or IPv6 Address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "mlag_configuration.peer_address_heartbeat.vrf") | String |  |  |  | VRF Name. |
    | [<samp>&nbsp;&nbsp;dual_primary_detection_delay</samp>](## "mlag_configuration.dual_primary_detection_delay") | Integer |  |  | Min: 0<br>Max: 86400 | Delay in seconds. |
    | [<samp>&nbsp;&nbsp;dual_primary_recovery_delay_mlag</samp>](## "mlag_configuration.dual_primary_recovery_delay_mlag") | Integer |  |  | Min: 0<br>Max: 86400 | Delay in seconds. |
    | [<samp>&nbsp;&nbsp;dual_primary_recovery_delay_non_mlag</samp>](## "mlag_configuration.dual_primary_recovery_delay_non_mlag") | Integer |  |  | Min: 0<br>Max: 86400 | Delay in seconds. |
    | [<samp>&nbsp;&nbsp;peer_link</samp>](## "mlag_configuration.peer_link") | String |  |  |  | Port-Channel interface name. |
    | [<samp>&nbsp;&nbsp;reload_delay_mlag</samp>](## "mlag_configuration.reload_delay_mlag") | String |  |  |  | Delay in seconds <0-86400> or 'infinity'. |
    | [<samp>&nbsp;&nbsp;reload_delay_non_mlag</samp>](## "mlag_configuration.reload_delay_non_mlag") | String |  |  |  | Delay in seconds <0-86400> or 'infinity'. |

=== "YAML"

    ```yaml
    mlag_configuration:
      domain_id: <str>

      # Heartbeat interval in milliseconds.
      heartbeat_interval: <int>

      # Local Interface Name.
      local_interface: <str>

      # IPv4 or IPv6 Address.
      peer_address: <str>
      peer_address_heartbeat:

        # IPv4 or IPv6 Address.
        peer_ip: <str>

        # VRF Name.
        vrf: <str>

      # Delay in seconds.
      dual_primary_detection_delay: <int; 0-86400>

      # Delay in seconds.
      dual_primary_recovery_delay_mlag: <int; 0-86400>

      # Delay in seconds.
      dual_primary_recovery_delay_non_mlag: <int; 0-86400>

      # Port-Channel interface name.
      peer_link: <str>

      # Delay in seconds <0-86400> or 'infinity'.
      reload_delay_mlag: <str>

      # Delay in seconds <0-86400> or 'infinity'.
      reload_delay_non_mlag: <str>
    ```
