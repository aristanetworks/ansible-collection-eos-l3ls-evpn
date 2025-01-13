<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>community_lists</samp>](## "community_lists") <span style="color:red">deprecated</span> | List, items: Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>ip_community_lists</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "community_lists.[].name") | String | Required, Unique |  |  | Community-list Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "community_lists.[].action") | String | Required |  |  | Action as string.<br>Example: "permit GSHUT 65123:123"<br> |

=== "YAML"

    ```yaml
    # This key is deprecated.
    # Support will be removed in AVD version 6.0.0.
    # Use <samp>ip_community_lists</samp> instead.
    community_lists:

        # Community-list Name.
      - name: <str; required; unique>

        # Action as string.
        # Example: "permit GSHUT 65123:123"
        action: <str; required>
    ```
