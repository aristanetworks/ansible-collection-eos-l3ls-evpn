<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>dot1x</samp>](## "dot1x") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;system_auth_control</samp>](## "dot1x.system_auth_control") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;protocol_lldp_bypass</samp>](## "dot1x.protocol_lldp_bypass") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;protocol_bpdu_bypass</samp>](## "dot1x.protocol_bpdu_bypass") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;dynamic_authorization</samp>](## "dot1x.dynamic_authorization") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;mac_based_authentication</samp>](## "dot1x.mac_based_authentication") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "dot1x.mac_based_authentication.delay") | Integer |  |  | Min: 0<br>Max: 300 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hold_period</samp>](## "dot1x.mac_based_authentication.hold_period") | Integer |  |  | Min: 1<br>Max: 300 |  |
    | [<samp>&nbsp;&nbsp;radius_av_pair_username_format</samp>](## "dot1x.radius_av_pair_username_format") | Dictionary |  |  |  | RADIUS AV-pair username settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;delimiter</samp>](## "dot1x.radius_av_pair_username_format.delimiter") | String | Required |  | Valid Values:<br>- <code>colon</code><br>- <code>hyphen</code><br>- <code>none</code><br>- <code>period</code> | Delimiter to use in MAC address string. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_string_case</samp>](## "dot1x.radius_av_pair_username_format.mac_string_case") | String | Required |  | Valid Values:<br>- <code>lowercase</code><br>- <code>uppercase</code> | MAC address string in lowercase/uppercase. |
    | [<samp>&nbsp;&nbsp;radius_av_pair</samp>](## "dot1x.radius_av_pair") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;service_type</samp>](## "dot1x.radius_av_pair.service_type") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;framed_mtu</samp>](## "dot1x.radius_av_pair.framed_mtu") | Integer |  |  | Min: 68<br>Max: 9236 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lldp</samp>](## "dot1x.radius_av_pair.lldp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;system_name</samp>](## "dot1x.radius_av_pair.lldp.system_name") | Dictionary |  |  |  | LLDP system name (LLDP TLV 5) av-pair. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "dot1x.radius_av_pair.lldp.system_name.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth_only</samp>](## "dot1x.radius_av_pair.lldp.system_name.auth_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;system_description</samp>](## "dot1x.radius_av_pair.lldp.system_description") | Dictionary |  |  |  | LLDP system description (LLDP TLV 6) av-pair. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "dot1x.radius_av_pair.lldp.system_description.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth_only</samp>](## "dot1x.radius_av_pair.lldp.system_description.auth_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dhcp</samp>](## "dot1x.radius_av_pair.dhcp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hostname</samp>](## "dot1x.radius_av_pair.dhcp.hostname") | Dictionary |  |  |  | Hostname (DHCP Option 12). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "dot1x.radius_av_pair.dhcp.hostname.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth_only</samp>](## "dot1x.radius_av_pair.dhcp.hostname.auth_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;parameter_request_list</samp>](## "dot1x.radius_av_pair.dhcp.parameter_request_list") | Dictionary |  |  |  | Parameters requested by host (DHCP Option 55). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "dot1x.radius_av_pair.dhcp.parameter_request_list.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth_only</samp>](## "dot1x.radius_av_pair.dhcp.parameter_request_list.auth_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vendor_class_id</samp>](## "dot1x.radius_av_pair.dhcp.vendor_class_id") | Dictionary |  |  |  | Vendor class identifier (DHCP Option 60). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "dot1x.radius_av_pair.dhcp.vendor_class_id.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth_only</samp>](## "dot1x.radius_av_pair.dhcp.vendor_class_id.auth_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;aaa</samp>](## "dot1x.aaa") | Dictionary |  |  |  | Configure AAA parameters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;unresponsive</samp>](## "dot1x.aaa.unresponsive") | Dictionary |  |  |  | Configure AAA timeout options. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eap_response</samp>](## "dot1x.aaa.unresponsive.eap_response") | String |  |  | Valid Values:<br>- <code>success</code><br>- <code>disabled</code> | EAP response to send. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "dot1x.aaa.unresponsive.action") | Dictionary |  |  |  | Set action for supplicant when AAA times out. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;apply_cached_results</samp>](## "dot1x.aaa.unresponsive.action.apply_cached_results") | Boolean |  |  |  | Use results from a previous AAA response. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cached_results_timeout</samp>](## "dot1x.aaa.unresponsive.action.cached_results_timeout") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time_duration</samp>](## "dot1x.aaa.unresponsive.action.cached_results_timeout.time_duration") | Integer |  |  | Min: 1 | Enable caching for a specific duration -<br><1-10000>      duration in days<br><1-14400000>   duration in minutes<br><1-240000>     duration in hours<br><1-864000000>  duration in seconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time_duration_unit</samp>](## "dot1x.aaa.unresponsive.action.cached_results_timeout.time_duration_unit") | String | Required |  | Valid Values:<br>- <code>days</code><br>- <code>hours</code><br>- <code>minutes</code><br>- <code>seconds</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;apply_alternate</samp>](## "dot1x.aaa.unresponsive.action.apply_alternate") | Boolean |  |  |  | Apply alternate action if primary action fails.<br>eg. aaa unresponsive action apply cached-results else traffic allow |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_allow</samp>](## "dot1x.aaa.unresponsive.action.traffic_allow") | Boolean |  |  |  | Set action for supplicant traffic when AAA times out. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_allow_vlan</samp>](## "dot1x.aaa.unresponsive.action.traffic_allow_vlan") | Integer |  |  | Min: 1<br>Max: 4094 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;phone_action</samp>](## "dot1x.aaa.unresponsive.phone_action") | Dictionary |  |  |  | Set action for supplicant when AAA times out. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;apply_cached_results</samp>](## "dot1x.aaa.unresponsive.phone_action.apply_cached_results") | Boolean |  |  |  | Use results from a previous AAA response. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cached_results_timeout</samp>](## "dot1x.aaa.unresponsive.phone_action.cached_results_timeout") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time_duration</samp>](## "dot1x.aaa.unresponsive.phone_action.cached_results_timeout.time_duration") | Integer |  |  | Min: 1 | Enable caching for a specific duration -<br><1-10000>      duration in days<br><1-14400000>   duration in minutes<br><1-240000>     duration in hours<br><1-864000000>  duration in seconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time_duration_unit</samp>](## "dot1x.aaa.unresponsive.phone_action.cached_results_timeout.time_duration_unit") | String | Required |  | Valid Values:<br>- <code>days</code><br>- <code>hours</code><br>- <code>minutes</code><br>- <code>seconds</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;apply_alternate</samp>](## "dot1x.aaa.unresponsive.phone_action.apply_alternate") | Boolean |  |  |  | Apply alternate action if primary action fails.<br>eg. aaa unresponsive phone action apply cached-results else traffic allow |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_allow</samp>](## "dot1x.aaa.unresponsive.phone_action.traffic_allow") | Boolean |  |  |  | Set action for supplicant traffic when AAA times out. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_action_reauthenticate</samp>](## "dot1x.aaa.unresponsive.recovery_action_reauthenticate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;accounting_update_interval</samp>](## "dot1x.aaa.accounting_update_interval") | Integer |  |  | Min: 5<br>Max: 65535 | Interval period in seconds. |
    | [<samp>&nbsp;&nbsp;captive_portal</samp>](## "dot1x.captive_portal") | Dictionary |  |  |  | Web authentication feature authenticates a supplicant through a web page, referred to as a captive portal. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "dot1x.captive_portal.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;url</samp>](## "dot1x.captive_portal.url") | String |  |  |  | Supported URL type:<br>  - http: http://<hostname>[:<port>]<br>  - https: https://<hostname>[:<port>] |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ssl_profile</samp>](## "dot1x.captive_portal.ssl_profile") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;start_limit_infinite</samp>](## "dot1x.captive_portal.start_limit_infinite") | Boolean |  |  |  | Set captive-portal start limit to infinte. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_list_ipv4</samp>](## "dot1x.captive_portal.access_list_ipv4") | String |  |  |  | Standard access-list name. |
    | [<samp>&nbsp;&nbsp;supplicant</samp>](## "dot1x.supplicant") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;profiles</samp>](## "dot1x.supplicant.profiles") | List, items: Dictionary |  |  |  | Dot1x supplicant profiles. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "dot1x.supplicant.profiles.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eap_method</samp>](## "dot1x.supplicant.profiles.[].eap_method") | String |  |  | Valid Values:<br>- <code>fast</code><br>- <code>tls</code> | Extensible Authentication Protocol method:<br>  - EAP Flexible Authentication via Secure Tunneling.<br>  - EAP with Transport Layer Security. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identity</samp>](## "dot1x.supplicant.profiles.[].identity") | String |  |  |  | User identity. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;passphrase_type</samp>](## "dot1x.supplicant.profiles.[].passphrase_type") | String |  | `7` | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;passphrase</samp>](## "dot1x.supplicant.profiles.[].passphrase") | String |  |  |  | Extensible Authentication Protocol password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ssl_profile</samp>](## "dot1x.supplicant.profiles.[].ssl_profile") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "dot1x.supplicant.logging") | Boolean |  |  |  | Enable supplicant logging. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;disconnect_cached_results_timeout</samp>](## "dot1x.supplicant.disconnect_cached_results_timeout") | Integer |  |  | Min: 60<br>Max: 65535 | Timeout in seconds for removing a disconnected supplicant. |

=== "YAML"

    ```yaml
    dot1x:
      system_auth_control: <bool>
      protocol_lldp_bypass: <bool>
      protocol_bpdu_bypass: <bool>
      dynamic_authorization: <bool>
      mac_based_authentication:
        delay: <int; 0-300>
        hold_period: <int; 1-300>

      # RADIUS AV-pair username settings.
      radius_av_pair_username_format:

        # Delimiter to use in MAC address string.
        delimiter: <str; "colon" | "hyphen" | "none" | "period"; required>

        # MAC address string in lowercase/uppercase.
        mac_string_case: <str; "lowercase" | "uppercase"; required>
      radius_av_pair:
        service_type: <bool>
        framed_mtu: <int; 68-9236>
        lldp:

          # LLDP system name (LLDP TLV 5) av-pair.
          system_name:
            enabled: <bool; required>
            auth_only: <bool>

          # LLDP system description (LLDP TLV 6) av-pair.
          system_description:
            enabled: <bool; required>
            auth_only: <bool>
        dhcp:

          # Hostname (DHCP Option 12).
          hostname:
            enabled: <bool; required>
            auth_only: <bool>

          # Parameters requested by host (DHCP Option 55).
          parameter_request_list:
            enabled: <bool; required>
            auth_only: <bool>

          # Vendor class identifier (DHCP Option 60).
          vendor_class_id:
            enabled: <bool; required>
            auth_only: <bool>

      # Configure AAA parameters.
      aaa:

        # Configure AAA timeout options.
        unresponsive:

          # EAP response to send.
          eap_response: <str; "success" | "disabled">

          # Set action for supplicant when AAA times out.
          action:

            # Use results from a previous AAA response.
            apply_cached_results: <bool>
            cached_results_timeout:

              # Enable caching for a specific duration -
              # <1-10000>      duration in days
              # <1-14400000>   duration in minutes
              # <1-240000>     duration in hours
              # <1-864000000>  duration in seconds
              time_duration: <int; >=1>
              time_duration_unit: <str; "days" | "hours" | "minutes" | "seconds"; required>

            # Apply alternate action if primary action fails.
            # eg. aaa unresponsive action apply cached-results else traffic allow
            apply_alternate: <bool>

            # Set action for supplicant traffic when AAA times out.
            traffic_allow: <bool>
            traffic_allow_vlan: <int; 1-4094>

          # Set action for supplicant when AAA times out.
          phone_action:

            # Use results from a previous AAA response.
            apply_cached_results: <bool>
            cached_results_timeout:

              # Enable caching for a specific duration -
              # <1-10000>      duration in days
              # <1-14400000>   duration in minutes
              # <1-240000>     duration in hours
              # <1-864000000>  duration in seconds
              time_duration: <int; >=1>
              time_duration_unit: <str; "days" | "hours" | "minutes" | "seconds"; required>

            # Apply alternate action if primary action fails.
            # eg. aaa unresponsive phone action apply cached-results else traffic allow
            apply_alternate: <bool>

            # Set action for supplicant traffic when AAA times out.
            traffic_allow: <bool>
          recovery_action_reauthenticate: <bool>

        # Interval period in seconds.
        accounting_update_interval: <int; 5-65535>

      # Web authentication feature authenticates a supplicant through a web page, referred to as a captive portal.
      captive_portal:
        enabled: <bool; required>

        # Supported URL type:
        #   - http: http://<hostname>[:<port>]
        #   - https: https://<hostname>[:<port>]
        url: <str>
        ssl_profile: <str>

        # Set captive-portal start limit to infinte.
        start_limit_infinite: <bool>

        # Standard access-list name.
        access_list_ipv4: <str>
      supplicant:

        # Dot1x supplicant profiles.
        profiles:
          - name: <str; required; unique>

            # Extensible Authentication Protocol method:
            #   - EAP Flexible Authentication via Secure Tunneling.
            #   - EAP with Transport Layer Security.
            eap_method: <str; "fast" | "tls">

            # User identity.
            identity: <str>
            passphrase_type: <str; "0" | "7" | "8a"; default="7">

            # Extensible Authentication Protocol password.
            passphrase: <str>
            ssl_profile: <str>

        # Enable supplicant logging.
        logging: <bool>

        # Timeout in seconds for removing a disconnected supplicant.
        disconnect_cached_results_timeout: <int; 60-65535>
    ```
