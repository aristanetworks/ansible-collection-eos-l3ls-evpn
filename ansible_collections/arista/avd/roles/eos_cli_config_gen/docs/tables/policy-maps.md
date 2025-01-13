<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>policy_maps</samp>](## "policy_maps") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;pbr</samp>](## "policy_maps.pbr") | List, items: Dictionary |  |  |  | PBR Policy-Maps. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "policy_maps.pbr.[].name") | String | Required, Unique |  |  | Policy-Map Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;classes</samp>](## "policy_maps.pbr.[].classes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "policy_maps.pbr.[].classes.[].name") | String | Required, Unique |  |  | Class Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index</samp>](## "policy_maps.pbr.[].classes.[].index") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "policy_maps.pbr.[].classes.[].drop") | Boolean |  |  |  | 'drop' and 'set' are mutually exclusive. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set</samp>](## "policy_maps.pbr.[].classes.[].set") | Dictionary |  |  |  | Set Nexthop<br>'drop' and 'set' are mutually exclusive.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nexthop</samp>](## "policy_maps.pbr.[].classes.[].set.nexthop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "policy_maps.pbr.[].classes.[].set.nexthop.ip_address") | String |  |  |  | IPv4 or IPv6 Address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recursive</samp>](## "policy_maps.pbr.[].classes.[].set.nexthop.recursive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;qos</samp>](## "policy_maps.qos") | List, items: Dictionary |  |  |  | QOS Policy-Maps. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "policy_maps.qos.[].name") | String | Required, Unique |  |  | Policy-Map Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;classes</samp>](## "policy_maps.qos.[].classes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "policy_maps.qos.[].classes.[].name") | String | Required, Unique |  |  | Class Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set</samp>](## "policy_maps.qos.[].classes.[].set") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "policy_maps.qos.[].classes.[].set.cos") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "policy_maps.qos.[].classes.[].set.dscp") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp>](## "policy_maps.qos.[].classes.[].set.traffic_class") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop_precedence</samp>](## "policy_maps.qos.[].classes.[].set.drop_precedence") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;police</samp>](## "policy_maps.qos.[].classes.[].police") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "policy_maps.qos.[].classes.[].police.rate") | Integer |  |  |  | Specify rate.<br>Range in kbps <8-200000000>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_unit</samp>](## "policy_maps.qos.[].classes.[].police.rate_unit") | String |  | `bps` | Valid Values:<br>- <code>bps</code><br>- <code>kbps</code><br>- <code>mbps</code><br>- <code>pps</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_burst_size</samp>](## "policy_maps.qos.[].classes.[].police.rate_burst_size") | Integer |  |  |  | Range in bytes <256-128000000>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_burst_size_unit</samp>](## "policy_maps.qos.[].classes.[].police.rate_burst_size_unit") | String |  | `bytes` | Valid Values:<br>- <code>bytes</code><br>- <code>kbytes</code><br>- <code>mbytes</code><br>- <code>packets</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "policy_maps.qos.[].classes.[].police.action") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "policy_maps.qos.[].classes.[].police.action.type") | String |  |  | Valid Values:<br>- <code>dscp</code><br>- <code>drop-precedence</code> | Set action for policed traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp_value</samp>](## "policy_maps.qos.[].classes.[].police.action.dscp_value") | String |  |  |  | Set when action.type is set to "dscp". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;higher_rate</samp>](## "policy_maps.qos.[].classes.[].police.higher_rate") | Integer |  |  |  | Specify higher rate.<br>Range in kbps <lower_rate in kbps + 8 - lower_rate in kbps + 200000000>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;higher_rate_unit</samp>](## "policy_maps.qos.[].classes.[].police.higher_rate_unit") | String |  | `bps` | Valid Values:<br>- <code>bps</code><br>- <code>kbps</code><br>- <code>mbps</code><br>- <code>pps</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;higher_rate_burst_size</samp>](## "policy_maps.qos.[].classes.[].police.higher_rate_burst_size") | Integer |  |  |  | Range in bytes <256-128000000>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;higher_rate_burst_size_unit</samp>](## "policy_maps.qos.[].classes.[].police.higher_rate_burst_size_unit") | String |  | `bytes` | Valid Values:<br>- <code>bytes</code><br>- <code>kbytes</code><br>- <code>mbytes</code><br>- <code>packets</code> |  |
    | [<samp>&nbsp;&nbsp;copp_system_policy</samp>](## "policy_maps.copp_system_policy") | Dictionary |  |  |  | Control-plane policy configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;classes</samp>](## "policy_maps.copp_system_policy.classes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "policy_maps.copp_system_policy.classes.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shape</samp>](## "policy_maps.copp_system_policy.classes.[].shape") | Integer |  |  | Min: 0<br>Max: 10000000 | Maximum rate limit. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth</samp>](## "policy_maps.copp_system_policy.classes.[].bandwidth") | Integer |  |  | Min: 0<br>Max: 10000000 | Minimum bandwidth. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_unit</samp>](## "policy_maps.copp_system_policy.classes.[].rate_unit") | String |  |  | Valid Values:<br>- <code>pps</code><br>- <code>kbps</code> | The `rate_unit` must be defined for `shape` and `bandwidth`. |

=== "YAML"

    ```yaml
    policy_maps:

      # PBR Policy-Maps.
      pbr:

          # Policy-Map Name.
        - name: <str; required; unique>
          classes:

              # Class Name.
            - name: <str; required; unique>
              index: <int>

              # 'drop' and 'set' are mutually exclusive.
              drop: <bool>

              # Set Nexthop
              # 'drop' and 'set' are mutually exclusive.
              set:
                nexthop:

                  # IPv4 or IPv6 Address.
                  ip_address: <str>
                  recursive: <bool>

      # QOS Policy-Maps.
      qos:

          # Policy-Map Name.
        - name: <str; required; unique>
          classes:

              # Class Name.
            - name: <str; required; unique>
              set:
                cos: <int>
                dscp: <str>
                traffic_class: <int>
                drop_precedence: <int>
              police:

                # Specify rate.
                # Range in kbps <8-200000000>.
                rate: <int>
                rate_unit: <str; "bps" | "kbps" | "mbps" | "pps"; default="bps">

                # Range in bytes <256-128000000>.
                rate_burst_size: <int>
                rate_burst_size_unit: <str; "bytes" | "kbytes" | "mbytes" | "packets"; default="bytes">
                action:

                  # Set action for policed traffic.
                  type: <str; "dscp" | "drop-precedence">

                  # Set when action.type is set to "dscp".
                  dscp_value: <str>

                # Specify higher rate.
                # Range in kbps <lower_rate in kbps + 8 - lower_rate in kbps + 200000000>.
                higher_rate: <int>
                higher_rate_unit: <str; "bps" | "kbps" | "mbps" | "pps"; default="bps">

                # Range in bytes <256-128000000>.
                higher_rate_burst_size: <int>
                higher_rate_burst_size_unit: <str; "bytes" | "kbytes" | "mbytes" | "packets"; default="bytes">

      # Control-plane policy configuration.
      copp_system_policy:
        classes:
          - name: <str; required; unique>

            # Maximum rate limit.
            shape: <int; 0-10000000>

            # Minimum bandwidth.
            bandwidth: <int; 0-10000000>

            # The `rate_unit` must be defined for `shape` and `bandwidth`.
            rate_unit: <str; "pps" | "kbps">
    ```
