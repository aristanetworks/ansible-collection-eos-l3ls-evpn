<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>use_router_general_for_router_id</samp>](## "use_router_general_for_router_id") | Boolean |  | `False` |  | Use `router general` to set router ID for all routing protocols and VRFs. |

=== "YAML"

    ```yaml
    # Use `router general` to set router ID for all routing protocols and VRFs.
    use_router_general_for_router_id: <bool; default=False>
    ```
