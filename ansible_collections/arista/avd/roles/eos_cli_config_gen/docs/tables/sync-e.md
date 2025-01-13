<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>sync_e</samp>](## "sync_e") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;network_option</samp>](## "sync_e.network_option") | Integer | Required |  | Min: 1<br>Max: 2 |  |

=== "YAML"

    ```yaml
    sync_e:
      network_option: <int; 1-2; required>
    ```
