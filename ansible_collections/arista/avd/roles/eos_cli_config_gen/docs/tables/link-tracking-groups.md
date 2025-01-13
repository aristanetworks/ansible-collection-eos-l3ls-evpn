<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>link_tracking_groups</samp>](## "link_tracking_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "link_tracking_groups.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;links_minimum</samp>](## "link_tracking_groups.[].links_minimum") | Integer |  |  | Min: 1<br>Max: 100000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;recovery_delay</samp>](## "link_tracking_groups.[].recovery_delay") | Integer |  |  | Min: 0<br>Max: 3600 |  |

=== "YAML"

    ```yaml
    link_tracking_groups:
      - name: <str; required; unique>
        links_minimum: <int; 1-100000>
        recovery_delay: <int; 0-3600>
    ```
