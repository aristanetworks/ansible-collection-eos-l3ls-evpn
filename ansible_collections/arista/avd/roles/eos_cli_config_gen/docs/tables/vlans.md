<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>vlans</samp>](## "vlans") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;id</samp>](## "vlans.[].id") | Integer | Required, Unique |  |  | VLAN ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "vlans.[].name") | String |  |  |  | VLAN Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;state</samp>](## "vlans.[].state") | String |  |  | Valid Values:<br>- <code>active</code><br>- <code>suspend</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;address_locking</samp>](## "vlans.[].address_locking") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family</samp>](## "vlans.[].address_locking.address_family") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "vlans.[].address_locking.address_family.ipv4") | Boolean |  |  |  | Enable address locking for IPv4. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "vlans.[].address_locking.address_family.ipv6") | Boolean |  |  |  | Enable address locking for IPv6. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_enforcement_disabled</samp>](## "vlans.[].address_locking.ipv4_enforcement_disabled") | Boolean |  |  |  | Disable enforcement for IPv4 locked addresses. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "vlans.[].trunk_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "vlans.[].trunk_groups.[]") | String |  |  |  | Trunk Group Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;private_vlan</samp>](## "vlans.[].private_vlan") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "vlans.[].private_vlan.type") | String |  |  | Valid Values:<br>- <code>community</code><br>- <code>isolated</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primary_vlan</samp>](## "vlans.[].private_vlan.primary_vlan") | Integer |  |  |  | Primary VLAN ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tenant</samp>](## "vlans.[].tenant") | String |  |  |  | Key only used for documentation or validation purposes. |

=== "YAML"

    ```yaml
    vlans:

        # VLAN ID.
      - id: <int; required; unique>

        # VLAN Name.
        name: <str>
        state: <str; "active" | "suspend">
        address_locking:
          address_family:

            # Enable address locking for IPv4.
            ipv4: <bool>

            # Enable address locking for IPv6.
            ipv6: <bool>

          # Disable enforcement for IPv4 locked addresses.
          ipv4_enforcement_disabled: <bool>
        trunk_groups:

            # Trunk Group Name.
          - <str>
        private_vlan:
          type: <str; "community" | "isolated">

          # Primary VLAN ID.
          primary_vlan: <int>

        # Key only used for documentation or validation purposes.
        tenant: <str>
    ```
