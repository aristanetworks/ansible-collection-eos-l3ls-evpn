<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>tacacs_servers</samp>](## "tacacs_servers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;timeout</samp>](## "tacacs_servers.timeout") | Integer |  |  | Min: 1<br>Max: 1000 | Timeout in seconds. |
    | [<samp>&nbsp;&nbsp;hosts</samp>](## "tacacs_servers.hosts") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;host</samp>](## "tacacs_servers.hosts.[].host") | String |  |  |  | Host IP address or name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "tacacs_servers.hosts.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "tacacs_servers.hosts.[].key") | String |  |  |  | Encrypted key. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "tacacs_servers.hosts.[].key_type") | String |  | `7` | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;single_connection</samp>](## "tacacs_servers.hosts.[].single_connection") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "tacacs_servers.hosts.[].timeout") | Integer |  |  | Min: 1<br>Max: 1000 | Timeout in seconds. |
    | [<samp>&nbsp;&nbsp;policy_unknown_mandatory_attribute_ignore</samp>](## "tacacs_servers.policy_unknown_mandatory_attribute_ignore") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    tacacs_servers:

      # Timeout in seconds.
      timeout: <int; 1-1000>
      hosts:

          # Host IP address or name.
        - host: <str>
          vrf: <str>

          # Encrypted key.
          key: <str>
          key_type: <str; "0" | "7" | "8a"; default="7">
          single_connection: <bool>

          # Timeout in seconds.
          timeout: <int; 1-1000>
      policy_unknown_mandatory_attribute_ignore: <bool>
    ```
