<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_tacacs_source_interfaces</samp>](## "ip_tacacs_source_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "ip_tacacs_source_interfaces.[].name") | String |  |  |  | Interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ip_tacacs_source_interfaces.[].vrf") | String |  |  |  |  |

=== "YAML"

    ```yaml
    ip_tacacs_source_interfaces:

        # Interface name.
      - name: <str>
        vrf: <str>
    ```
