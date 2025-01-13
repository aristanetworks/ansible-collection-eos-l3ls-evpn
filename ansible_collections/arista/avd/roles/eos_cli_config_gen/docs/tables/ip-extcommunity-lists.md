<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_extcommunity_lists</samp>](## "ip_extcommunity_lists") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "ip_extcommunity_lists.[].name") | String | Required, Unique |  |  | Community-list Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "ip_extcommunity_lists.[].entries") | List, items: Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;type</samp>](## "ip_extcommunity_lists.[].entries.[].type") | String | Required |  | Valid Values:<br>- <code>permit</code><br>- <code>deny</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;extcommunities</samp>](## "ip_extcommunity_lists.[].entries.[].extcommunities") | String | Required |  |  | Communities as string.<br>Example: "65000:65000"<br> |

=== "YAML"

    ```yaml
    ip_extcommunity_lists:

        # Community-list Name.
      - name: <str; required; unique>
        entries: # required
          - type: <str; "permit" | "deny"; required>

            # Communities as string.
            # Example: "65000:65000"
            extcommunities: <str; required>
    ```
