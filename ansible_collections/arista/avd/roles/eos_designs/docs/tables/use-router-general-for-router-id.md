<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>use_router_general_for_router_id</samp>](## "use_router_general_for_router_id") | Boolean |  | `False` |  | This setting allows to use `router_id` set under `router_general_settings` as BGP router-id. |

=== "YAML"

    ```yaml
    # This setting allows to use `router_id` set under `router_general_settings` as BGP router-id.
    use_router_general_for_router_id: <bool; default=False>
    ```
