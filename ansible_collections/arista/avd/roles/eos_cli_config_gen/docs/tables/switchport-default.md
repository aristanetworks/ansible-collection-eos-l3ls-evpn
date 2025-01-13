<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>switchport_default</samp>](## "switchport_default") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;mode</samp>](## "switchport_default.mode") | String |  |  | Valid Values:<br>- <code>routed</code><br>- <code>access</code> |  |
    | [<samp>&nbsp;&nbsp;phone</samp>](## "switchport_default.phone") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "switchport_default.phone.cos") | Integer |  |  | Min: 0<br>Max: 7 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk</samp>](## "switchport_default.phone.trunk") | String |  |  | Valid Values:<br>- <code>tagged</code><br>- <code>untagged</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "switchport_default.phone.vlan") | Integer |  |  | Min: 1<br>Max: 4094 | VLAN ID. |

=== "YAML"

    ```yaml
    switchport_default:
      mode: <str; "routed" | "access">
      phone:
        cos: <int; 0-7>
        trunk: <str; "tagged" | "untagged">

        # VLAN ID.
        vlan: <int; 1-4094>
    ```
