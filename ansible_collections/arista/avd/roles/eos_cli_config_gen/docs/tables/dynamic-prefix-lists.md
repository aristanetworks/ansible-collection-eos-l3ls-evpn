<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>dynamic_prefix_lists</samp>](## "dynamic_prefix_lists") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "dynamic_prefix_lists.[].name") | String |  |  |  | Dynamic prefix-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;match_map</samp>](## "dynamic_prefix_lists.[].match_map") | String |  |  |  | Route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp>](## "dynamic_prefix_lists.[].prefix_list") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "dynamic_prefix_lists.[].prefix_list.ipv4") | String |  |  |  | Prefix-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "dynamic_prefix_lists.[].prefix_list.ipv6") | String |  |  |  | Prefix-list name. |

=== "YAML"

    ```yaml
    dynamic_prefix_lists:

        # Dynamic prefix-list name.
      - name: <str>

        # Route-map name.
        match_map: <str>
        prefix_list:

          # Prefix-list name.
          ipv4: <str>

          # Prefix-list name.
          ipv6: <str>
    ```
