<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>interface_defaults</samp>](## "interface_defaults") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ethernet</samp>](## "interface_defaults.ethernet") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "interface_defaults.ethernet.shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;mtu</samp>](## "interface_defaults.mtu") | Integer |  |  |  |  |

=== "YAML"

    ```yaml
    interface_defaults:
      ethernet:
        shutdown: <bool>
      mtu: <int>
    ```
