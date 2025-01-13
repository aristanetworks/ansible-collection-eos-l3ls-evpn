<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>vlan_internal_order</samp>](## "vlan_internal_order") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;allocation</samp>](## "vlan_internal_order.allocation") | String | Required |  | Valid Values:<br>- <code>ascending</code><br>- <code>descending</code> |  |
    | [<samp>&nbsp;&nbsp;range</samp>](## "vlan_internal_order.range") | Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;beginning</samp>](## "vlan_internal_order.range.beginning") | Integer | Required |  | Min: 2<br>Max: 4094 | First VLAN ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ending</samp>](## "vlan_internal_order.range.ending") | Integer | Required |  | Min: 2<br>Max: 4094 | Last VLAN ID. |

=== "YAML"

    ```yaml
    vlan_internal_order:
      allocation: <str; "ascending" | "descending"; required>
      range: # required

        # First VLAN ID.
        beginning: <int; 2-4094; required>

        # Last VLAN ID.
        ending: <int; 2-4094; required>
    ```
