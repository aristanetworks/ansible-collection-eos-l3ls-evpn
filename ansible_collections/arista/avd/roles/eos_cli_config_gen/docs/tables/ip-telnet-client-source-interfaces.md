<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_telnet_client_source_interfaces</samp>](## "ip_telnet_client_source_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "ip_telnet_client_source_interfaces.[].name") | String | Required |  |  | Interface Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ip_telnet_client_source_interfaces.[].vrf") | String |  |  |  | VRF Name. |

=== "YAML"

    ```yaml
    ip_telnet_client_source_interfaces:

        # Interface Name.
      - name: <str; required>

        # VRF Name.
        vrf: <str>
    ```
