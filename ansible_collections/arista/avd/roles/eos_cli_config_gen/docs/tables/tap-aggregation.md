<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>tap_aggregation</samp>](## "tap_aggregation") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;mode</samp>](## "tap_aggregation.mode") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;exclusive</samp>](## "tap_aggregation.mode.exclusive") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "tap_aggregation.mode.exclusive.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "tap_aggregation.mode.exclusive.profile") | String |  |  |  | Profile Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_errdisable</samp>](## "tap_aggregation.mode.exclusive.no_errdisable") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "tap_aggregation.mode.exclusive.no_errdisable.[]") | String |  |  |  | Interface name e.g Ethernet1, Port-Channel1. |
    | [<samp>&nbsp;&nbsp;encapsulation_dot1br_strip</samp>](## "tap_aggregation.encapsulation_dot1br_strip") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;encapsulation_vn_tag_strip</samp>](## "tap_aggregation.encapsulation_vn_tag_strip") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;protocol_lldp_trap</samp>](## "tap_aggregation.protocol_lldp_trap") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;truncation_size</samp>](## "tap_aggregation.truncation_size") | Integer |  |  |  | Allowed truncation_size values vary depending on the platform.<br> |
    | [<samp>&nbsp;&nbsp;mac</samp>](## "tap_aggregation.mac") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;timestamp</samp>](## "tap_aggregation.mac.timestamp") | Dictionary |  |  |  | mac.timestamp.replace_source_mac and mac.timestamp.header.format are mutually exclsuive. If both are defined, replace_source_mac takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_source_mac</samp>](## "tap_aggregation.mac.timestamp.replace_source_mac") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;header</samp>](## "tap_aggregation.mac.timestamp.header") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;format</samp>](## "tap_aggregation.mac.timestamp.header.format") | String |  |  | Valid Values:<br>- <code>48-bit</code><br>- <code>64-bit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eth_type</samp>](## "tap_aggregation.mac.timestamp.header.eth_type") | Integer |  |  |  | EtherType. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;fcs_append</samp>](## "tap_aggregation.mac.fcs_append") | Boolean |  |  |  | mac.fcs_append and mac.fcs_error are mutually exclusive. If both are defined, mac.fcs_append takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;fcs_error</samp>](## "tap_aggregation.mac.fcs_error") | String |  |  | Valid Values:<br>- <code>correct</code><br>- <code>discard</code><br>- <code>pass-through</code> |  |

=== "YAML"

    ```yaml
    tap_aggregation:
      mode:
        exclusive:
          enabled: <bool>

          # Profile Name.
          profile: <str>
          no_errdisable:

              # Interface name e.g Ethernet1, Port-Channel1.
            - <str>
      encapsulation_dot1br_strip: <bool>
      encapsulation_vn_tag_strip: <bool>
      protocol_lldp_trap: <bool>

      # Allowed truncation_size values vary depending on the platform.
      truncation_size: <int>
      mac:

        # mac.timestamp.replace_source_mac and mac.timestamp.header.format are mutually exclsuive. If both are defined, replace_source_mac takes precedence.
        timestamp:
          replace_source_mac: <bool>
          header:
            format: <str; "48-bit" | "64-bit">

            # EtherType.
            eth_type: <int>

        # mac.fcs_append and mac.fcs_error are mutually exclusive. If both are defined, mac.fcs_append takes precedence.
        fcs_append: <bool>
        fcs_error: <str; "correct" | "discard" | "pass-through">
    ```
