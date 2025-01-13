<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>management_console</samp>](## "management_console") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;idle_timeout</samp>](## "management_console.idle_timeout") | Integer |  |  | Min: 0<br>Max: 86400 |  |

=== "YAML"

    ```yaml
    management_console:
      idle_timeout: <int; 0-86400>
    ```
