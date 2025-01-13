<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mac_address_table</samp>](## "mac_address_table") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;aging_time</samp>](## "mac_address_table.aging_time") | Integer |  |  |  | Aging time in seconds. |
    | [<samp>&nbsp;&nbsp;notification_host_flap</samp>](## "mac_address_table.notification_host_flap") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "mac_address_table.notification_host_flap.logging") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;detection</samp>](## "mac_address_table.notification_host_flap.detection") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;window</samp>](## "mac_address_table.notification_host_flap.detection.window") | Integer |  |  | Min: 2<br>Max: 300 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;moves</samp>](## "mac_address_table.notification_host_flap.detection.moves") | Integer |  |  | Min: 2<br>Max: 10 |  |

=== "YAML"

    ```yaml
    mac_address_table:

      # Aging time in seconds.
      aging_time: <int>
      notification_host_flap:
        logging: <bool>
        detection:
          window: <int; 2-300>
          moves: <int; 2-10>
    ```
