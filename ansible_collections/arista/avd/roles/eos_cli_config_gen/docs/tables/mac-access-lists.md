<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mac_access_lists</samp>](## "mac_access_lists") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "mac_access_lists.[].name") | String | Required, Unique |  |  | MAC Access-list Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp>](## "mac_access_lists.[].counters_per_entry") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "mac_access_lists.[].entries") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;sequence</samp>](## "mac_access_lists.[].entries.[].sequence") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "mac_access_lists.[].entries.[].action") | String |  |  |  |  |

=== "YAML"

    ```yaml
    mac_access_lists:

        # MAC Access-list Name.
      - name: <str; required; unique>
        counters_per_entry: <bool>
        entries:
          - sequence: <int>
            action: <str>
    ```
