<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>event_handlers</samp>](## "event_handlers") | List, items: Dictionary |  |  |  | Gives the ability to monitor and react to Syslog messages.<br>Event Handlers provide a powerful and flexible tool that can be used to apply self-healing actions,<br>customize the system behavior, and implement workarounds to problems discovered in the field.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "event_handlers.[].name") | String | Required, Unique |  |  | Event Handler Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;actions</samp>](## "event_handlers.[].actions") | Dictionary |  |  |  | Note: `bash_command` and `log` are mutually exclusive. `bash_command` takes precedence over `log`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bash_command</samp>](## "event_handlers.[].actions.bash_command") | String |  |  |  | Define BASH command action. Command could be multiline also. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;log</samp>](## "event_handlers.[].actions.log") | Boolean |  |  |  | Log a message when the event is triggered. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;increment_device_health_metric</samp>](## "event_handlers.[].actions.increment_device_health_metric") | String |  |  |  | Name of device-health metric. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "event_handlers.[].delay") | Integer |  |  |  | Event-handler delay in seconds.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger</samp>](## "event_handlers.[].trigger") | String |  |  | Valid Values:<br>- <code>on-boot</code><br>- <code>on-counters</code><br>- <code>on-intf</code><br>- <code>on-logging</code><br>- <code>on-maintenance</code><br>- <code>on-startup-config</code><br>- <code>vm-tracer vm</code> | Configure event trigger condition.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger_on_counters</samp>](## "event_handlers.[].trigger_on_counters") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;condition</samp>](## "event_handlers.[].trigger_on_counters.condition") | String |  |  |  | Set the logical expression to evaluate. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;granularity_per_source</samp>](## "event_handlers.[].trigger_on_counters.granularity_per_source") | Boolean |  |  |  | Set the granularity of event counting for a wildcarded condition.<br>Example -<br>  condition ( Arad*.IptCrcErrCnt.delta > 100 ) and ( Arad*.UcFifoFullDrop.delta > 100 )<br>  [* wildcard is used here] |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;poll_interval</samp>](## "event_handlers.[].trigger_on_counters.poll_interval") | Integer |  |  | Min: 1<br>Max: 1000000 | Set the polling interval in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger_on_logging</samp>](## "event_handlers.[].trigger_on_logging") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;poll_interval</samp>](## "event_handlers.[].trigger_on_logging.poll_interval") | Integer |  |  | Min: 1<br>Max: 1000000 | Set the polling interval in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;regex</samp>](## "event_handlers.[].trigger_on_logging.regex") | String |  |  |  | Regular expression to use for searching log messages. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger_on_intf</samp>](## "event_handlers.[].trigger_on_intf") | Dictionary |  |  |  | Trigger condition occurs on specified interface changes.<br>Note: Any one of the `ip`, `ipv6` and `operstatus` key needs to be defined along with the `interface`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "event_handlers.[].trigger_on_intf.interface") | String | Required |  |  | Interface name.<br>Example - Ethernet4<br>          Loopback4-6<br>          Port-channel4,7 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "event_handlers.[].trigger_on_intf.ip") | Boolean |  |  |  | Action is triggered upon changes to interface IP address assignment. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "event_handlers.[].trigger_on_intf.ipv6") | Boolean |  |  |  | Action is triggered upon changes to interface ipv6 address assignment. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;operstatus</samp>](## "event_handlers.[].trigger_on_intf.operstatus") | Boolean |  |  |  | Action is triggered upon changes to interface operStatus. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trigger_on_maintenance</samp>](## "event_handlers.[].trigger_on_maintenance") | Dictionary |  |  |  | Settings required for trigger 'on-maintenance'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;operation</samp>](## "event_handlers.[].trigger_on_maintenance.operation") | String | Required |  | Valid Values:<br>- <code>enter</code><br>- <code>exit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_peer</samp>](## "event_handlers.[].trigger_on_maintenance.bgp_peer") | String |  |  |  | Ipv4/Ipv6 address or peer group name.<br>Trigger condition occurs on maintenance operation of specified BGP peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "event_handlers.[].trigger_on_maintenance.action") | String | Required |  | Valid Values:<br>- <code>after</code><br>- <code>before</code><br>- <code>all</code><br>- <code>begin</code><br>- <code>end</code> | Action for maintenance operation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stage</samp>](## "event_handlers.[].trigger_on_maintenance.stage") | String |  |  | Valid Values:<br>- <code>bgp</code><br>- <code>linkdown</code><br>- <code>mlag</code><br>- <code>ratemon</code> | Action is triggered after/before specified stage. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "event_handlers.[].trigger_on_maintenance.vrf") | String |  |  |  | VRF name. VRF can be defined for "bgp_peer" only. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "event_handlers.[].trigger_on_maintenance.interface") | String |  |  |  | Trigger condition occurs on maintenance operation of specified interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "event_handlers.[].trigger_on_maintenance.unit") | String |  |  |  | Name of unit. Trigger condition occurs on maintenance operation of specified unit |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;asynchronous</samp>](## "event_handlers.[].asynchronous") | Boolean |  | `False` |  | Set the action to be non-blocking.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action_type</samp>](## "event_handlers.[].action_type") <span style="color:red">removed</span> | String |  |  | Valid Values:<br>- <code>bash</code><br>- <code>increment</code><br>- <code>log</code> | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>event_handlers.actions</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "event_handlers.[].action") <span style="color:red">removed</span> | String |  |  |  | Command to execute.<br><span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>event_handlers.actions.bash_command</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;regex</samp>](## "event_handlers.[].regex") <span style="color:red">removed</span> | String |  |  |  | Regular expression to use for searching log messages. Required for on-logging trigger.<br><span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>event_handlers.trigger_on_logging.regex</samp> instead.</span> |
    | [<samp>ipv6_mgmt_destination_networks</samp>](## "ipv6_mgmt_destination_networks") | List, items: String |  |  |  | List of IPv6 prefixes to configure as static routes towards the OOB IPv6 Management interface gateway.<br>Replaces the default route.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "ipv6_mgmt_destination_networks.[]") | String |  |  |  | IPv6_network/Mask. |
    | [<samp>ipv6_mgmt_gateway</samp>](## "ipv6_mgmt_gateway") | String |  |  | Format: ipv6 | OOB Management interface gateway in IPv6 format.<br>Used as next-hop for default gateway or static routes defined under 'ipv6_mgmt_destination_networks'.<br> |
    | [<samp>local_users</samp>](## "local_users") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "local_users.[].name") | String | Required, Unique |  |  | Username. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "local_users.[].disabled") | Boolean |  |  |  | If true, the user will be removed and all other settings are ignored.<br>Useful for removing the default "admin" user.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;privilege</samp>](## "local_users.[].privilege") | Integer |  |  | Min: 0<br>Max: 15 | Initial privilege level with local EXEC authorization.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "local_users.[].role") | String |  |  |  | EOS RBAC Role to be assigned to the user such as "network-admin" or "network-operator".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sha512_password</samp>](## "local_users.[].sha512_password") | String |  |  |  | SHA512 Hash of Password.<br>Must be the hash of the password. By default EOS salts the password with the username, so the simplest is to generate the hash on an EOS device using the same username.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;no_password</samp>](## "local_users.[].no_password") | Boolean |  |  |  | If set a password will not be configured for this user. "sha512_password" MUST not be defined for this user.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ssh_key</samp>](## "local_users.[].ssh_key") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;secondary_ssh_key</samp>](## "local_users.[].secondary_ssh_key") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shell</samp>](## "local_users.[].shell") | String |  |  | Valid Values:<br>- <code>/bin/bash</code><br>- <code>/bin/sh</code><br>- <code>/sbin/nologin</code> | Specify shell for the user.<br> |
    | [<samp>management_eapi</samp>](## "management_eapi") | Dictionary |  |  |  | Default is HTTPS management eAPI enabled.<br>The VRF is set to < mgmt_interface_vrf >.<br> |
    | [<samp>&nbsp;&nbsp;enable_http</samp>](## "management_eapi.enable_http") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;enable_https</samp>](## "management_eapi.enable_https") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;default_services</samp>](## "management_eapi.default_services") | Boolean |  |  |  |  |
    | [<samp>name_servers</samp>](## "name_servers") | List, items: String |  |  |  | List of DNS servers. The VRF is set to < mgmt_interface_vrf >. |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "name_servers.[]") | String |  |  |  | IPv4 or IPv6 address. |
    | [<samp>ntp_settings</samp>](## "ntp_settings") | Dictionary |  |  |  | NTP settings |
    | [<samp>&nbsp;&nbsp;server_vrf</samp>](## "ntp_settings.server_vrf") | String |  |  |  | EOS only supports NTP servers in one VRF, so this VRF is used for all NTP servers and one local-interface.<br>- `use_mgmt_interface_vrf` will configure the NTP server(s) under the VRF set with `mgmt_interface_vrf` and set the `mgmt_interface` as NTP local-interface.<br>  An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.<br>- `use_inband_mgmt_vrf` will configure the NTP server(s) under the VRF set with `inband_mgmt_vrf` and set the `inband_mgmt_interface` as NTP local-interface.<br>  An error will be raised if inband management is not configured for the device.<br>- Any other string will be used directly as the VRF name but local interface must be set with `custom_structured_configuration_ntp` if needed.<br>If not set, the VRF is automatically picked up from the global setting `default_mgmt_method`. |
    | [<samp>&nbsp;&nbsp;servers</samp>](## "ntp_settings.servers") | List, items: Dictionary |  |  |  | The first server is always set as "preferred". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "ntp_settings.servers.[].name") | String |  |  |  | IP or hostname e.g., 2.2.2.55, 2001:db8::55, ie.pool.ntp.org. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;burst</samp>](## "ntp_settings.servers.[].burst") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;iburst</samp>](## "ntp_settings.servers.[].iburst") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "ntp_settings.servers.[].key") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maxpoll</samp>](## "ntp_settings.servers.[].maxpoll") | Integer |  |  | Min: 3<br>Max: 17 | Value of maxpoll between 3 - 17 (Logarithmic). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minpoll</samp>](## "ntp_settings.servers.[].minpoll") | Integer |  |  | Min: 3<br>Max: 17 | Value of minpoll between 3 - 17 (Logarithmic). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "ntp_settings.servers.[].version") | Integer |  |  | Min: 1<br>Max: 4 |  |
    | [<samp>&nbsp;&nbsp;authenticate</samp>](## "ntp_settings.authenticate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;authenticate_servers_only</samp>](## "ntp_settings.authenticate_servers_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;authentication_keys</samp>](## "ntp_settings.authentication_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "ntp_settings.authentication_keys.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 65534 | Key identifier. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "ntp_settings.authentication_keys.[].hash_algorithm") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>sha1</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "ntp_settings.authentication_keys.[].key") | String |  |  |  | Obfuscated key. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "ntp_settings.authentication_keys.[].key_type") | String |  |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> |  |
    | [<samp>&nbsp;&nbsp;trusted_keys</samp>](## "ntp_settings.trusted_keys") | String |  |  |  | List of trusted-keys as string ex. 10-12,15. |
    | [<samp>timezone</samp>](## "timezone") | String |  |  |  | Clock timezone like "CET" or "US/Pacific". |

=== "YAML"

    ```yaml
    # Gives the ability to monitor and react to Syslog messages.
    # Event Handlers provide a powerful and flexible tool that can be used to apply self-healing actions,
    # customize the system behavior, and implement workarounds to problems discovered in the field.
    event_handlers:

        # Event Handler Name.
      - name: <str; required; unique>

        # Note: `bash_command` and `log` are mutually exclusive. `bash_command` takes precedence over `log`.
        actions:

          # Define BASH command action. Command could be multiline also.
          bash_command: <str>

          # Log a message when the event is triggered.
          log: <bool>

          # Name of device-health metric.
          increment_device_health_metric: <str>

        # Event-handler delay in seconds.
        delay: <int>

        # Configure event trigger condition.
        trigger: <str; "on-boot" | "on-counters" | "on-intf" | "on-logging" | "on-maintenance" | "on-startup-config" | "vm-tracer vm">
        trigger_on_counters:

          # Set the logical expression to evaluate.
          condition: <str>

          # Set the granularity of event counting for a wildcarded condition.
          # Example -
          #   condition ( Arad*.IptCrcErrCnt.delta > 100 ) and ( Arad*.UcFifoFullDrop.delta > 100 )
          #   [* wildcard is used here]
          granularity_per_source: <bool>

          # Set the polling interval in seconds.
          poll_interval: <int; 1-1000000>
        trigger_on_logging:

          # Set the polling interval in seconds.
          poll_interval: <int; 1-1000000>

          # Regular expression to use for searching log messages.
          regex: <str>

        # Trigger condition occurs on specified interface changes.
        # Note: Any one of the `ip`, `ipv6` and `operstatus` key needs to be defined along with the `interface`.
        trigger_on_intf:

          # Interface name.
          # Example - Ethernet4
          #           Loopback4-6
          #           Port-channel4,7
          interface: <str; required>

          # Action is triggered upon changes to interface IP address assignment.
          ip: <bool>

          # Action is triggered upon changes to interface ipv6 address assignment.
          ipv6: <bool>

          # Action is triggered upon changes to interface operStatus.
          operstatus: <bool>

        # Settings required for trigger 'on-maintenance'.
        trigger_on_maintenance:
          operation: <str; "enter" | "exit"; required>

          # Ipv4/Ipv6 address or peer group name.
          # Trigger condition occurs on maintenance operation of specified BGP peer.
          bgp_peer: <str>

          # Action for maintenance operation.
          action: <str; "after" | "before" | "all" | "begin" | "end"; required>

          # Action is triggered after/before specified stage.
          stage: <str; "bgp" | "linkdown" | "mlag" | "ratemon">

          # VRF name. VRF can be defined for "bgp_peer" only.
          vrf: <str>

          # Trigger condition occurs on maintenance operation of specified interface.
          interface: <str>

          # Name of unit. Trigger condition occurs on maintenance operation of specified unit
          unit: <str>

        # Set the action to be non-blocking.
        asynchronous: <bool; default=False>

    # List of IPv6 prefixes to configure as static routes towards the OOB IPv6 Management interface gateway.
    # Replaces the default route.
    ipv6_mgmt_destination_networks:

        # IPv6_network/Mask.
      - <str>

    # OOB Management interface gateway in IPv6 format.
    # Used as next-hop for default gateway or static routes defined under 'ipv6_mgmt_destination_networks'.
    ipv6_mgmt_gateway: <str>
    local_users:

        # Username.
      - name: <str; required; unique>

        # If true, the user will be removed and all other settings are ignored.
        # Useful for removing the default "admin" user.
        disabled: <bool>

        # Initial privilege level with local EXEC authorization.
        privilege: <int; 0-15>

        # EOS RBAC Role to be assigned to the user such as "network-admin" or "network-operator".
        role: <str>

        # SHA512 Hash of Password.
        # Must be the hash of the password. By default EOS salts the password with the username, so the simplest is to generate the hash on an EOS device using the same username.
        sha512_password: <str>

        # If set a password will not be configured for this user. "sha512_password" MUST not be defined for this user.
        no_password: <bool>
        ssh_key: <str>
        secondary_ssh_key: <str>

        # Specify shell for the user.
        shell: <str; "/bin/bash" | "/bin/sh" | "/sbin/nologin">

    # Default is HTTPS management eAPI enabled.
    # The VRF is set to < mgmt_interface_vrf >.
    management_eapi:
      enable_http: <bool; default=False>
      enable_https: <bool; default=True>
      default_services: <bool>

    # List of DNS servers. The VRF is set to < mgmt_interface_vrf >.
    name_servers:

        # IPv4 or IPv6 address.
      - <str>

    # NTP settings
    ntp_settings:

      # EOS only supports NTP servers in one VRF, so this VRF is used for all NTP servers and one local-interface.
      # - `use_mgmt_interface_vrf` will configure the NTP server(s) under the VRF set with `mgmt_interface_vrf` and set the `mgmt_interface` as NTP local-interface.
      #   An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.
      # - `use_inband_mgmt_vrf` will configure the NTP server(s) under the VRF set with `inband_mgmt_vrf` and set the `inband_mgmt_interface` as NTP local-interface.
      #   An error will be raised if inband management is not configured for the device.
      # - Any other string will be used directly as the VRF name but local interface must be set with `custom_structured_configuration_ntp` if needed.
      # If not set, the VRF is automatically picked up from the global setting `default_mgmt_method`.
      server_vrf: <str>

      # The first server is always set as "preferred".
      servers:

          # IP or hostname e.g., 2.2.2.55, 2001:db8::55, ie.pool.ntp.org.
        - name: <str>
          burst: <bool>
          iburst: <bool>
          key: <int; 1-65535>

          # Value of maxpoll between 3 - 17 (Logarithmic).
          maxpoll: <int; 3-17>

          # Value of minpoll between 3 - 17 (Logarithmic).
          minpoll: <int; 3-17>
          version: <int; 1-4>
      authenticate: <bool>
      authenticate_servers_only: <bool>
      authentication_keys:

          # Key identifier.
        - id: <int; 1-65534; required; unique>
          hash_algorithm: <str; "md5" | "sha1">

          # Obfuscated key.
          key: <str>
          key_type: <str; "0" | "7" | "8a">

      # List of trusted-keys as string ex. 10-12,15.
      trusted_keys: <str>

    # Clock timezone like "CET" or "US/Pacific".
    timezone: <str>
    ```
