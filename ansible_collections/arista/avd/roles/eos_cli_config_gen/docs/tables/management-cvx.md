<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>management_cvx</samp>](## "management_cvx") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;shutdown</samp>](## "management_cvx.shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;server_hosts</samp>](## "management_cvx.server_hosts") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "management_cvx.server_hosts.[]") | String |  |  |  | IP or hostname. |
    | [<samp>&nbsp;&nbsp;source_interface</samp>](## "management_cvx.source_interface") | String |  |  |  | Interface name. |
    | [<samp>&nbsp;&nbsp;vrf</samp>](## "management_cvx.vrf") | String |  |  |  | VRF Name. |

=== "YAML"

    ```yaml
    management_cvx:
      shutdown: <bool>
      server_hosts:

          # IP or hostname.
        - <str>

      # Interface name.
      source_interface: <str>

      # VRF Name.
      vrf: <str>
    ```
