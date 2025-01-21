<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_virtual_router_mac_address_advertisement_interval</samp>](## "ip_virtual_router_mac_address_advertisement_interval") | Integer |  |  | Min: 0<br>Max: 86400 | Advertisement interval in seconds. |

=== "YAML"

    ```yaml
    # Advertisement interval in seconds.
    ip_virtual_router_mac_address_advertisement_interval: <int; 0-86400>
    ```
