<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_extcommunity_lists_regexp</samp>](## "ip_extcommunity_lists_regexp") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "ip_extcommunity_lists_regexp.[].name") | String | Required, Unique |  |  | Community-list Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "ip_extcommunity_lists_regexp.[].entries") | List, items: Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;type</samp>](## "ip_extcommunity_lists_regexp.[].entries.[].type") | String | Required |  | Valid Values:<br>- <code>permit</code><br>- <code>deny</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;regexp</samp>](## "ip_extcommunity_lists_regexp.[].entries.[].regexp") | String | Required |  |  | Regular Expression. |

=== "YAML"

    ```yaml
    ip_extcommunity_lists_regexp:

        # Community-list Name.
      - name: <str; required; unique>
        entries: # required
          - type: <str; "permit" | "deny"; required>

            # Regular Expression.
            regexp: <str; required>
    ```
