<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>aaa_server_groups</samp>](## "aaa_server_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "aaa_server_groups.[].name") | String | Required, Unique |  |  | Group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_server_groups.[].type") | String |  |  | Valid Values:<br>- <code>tacacs+</code><br>- <code>radius</code><br>- <code>ldap</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;servers</samp>](## "aaa_server_groups.[].servers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;server</samp>](## "aaa_server_groups.[].servers.[].server") | String |  |  |  | Hostname or IP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "aaa_server_groups.[].servers.[].vrf") | String |  |  |  | VRF name. |

=== "YAML"

    ```yaml
    aaa_server_groups:

        # Group name.
      - name: <str; required; unique>
        type: <str; "tacacs+" | "radius" | "ldap">
        servers:

            # Hostname or IP address.
          - server: <str>

            # VRF name.
            vrf: <str>
    ```
