<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_community_lists</samp>](## "ip_community_lists") | List, items: Dictionary |  |  |  | Communities and regexp entries MUST not be configured in the same community-list.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "ip_community_lists.[].name") | String | Required, Unique |  |  | IP Community-list Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "ip_community_lists.[].entries") | List, items: Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;action</samp>](## "ip_community_lists.[].entries.[].action") | String | Required |  | Valid Values:<br>- <code>permit</code><br>- <code>deny</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;communities</samp>](## "ip_community_lists.[].entries.[].communities") | List, items: String |  |  |  | If defined, a standard community-list will be configured.<br>Supported community strings (case insensitive):<br>- GSHUT<br>- internet<br>- local-as<br>- no-advertise<br>- no-export<br>- <1-4294967040><br>- aa:nn<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "ip_community_lists.[].entries.[].communities.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;regexp</samp>](## "ip_community_lists.[].entries.[].regexp") | String |  |  |  | Regular Expression.<br>If defined, a regex community-list will be configured.<br> |

=== "YAML"

    ```yaml
    # Communities and regexp entries MUST not be configured in the same community-list.
    ip_community_lists:

        # IP Community-list Name.
      - name: <str; required; unique>
        entries: # required
          - action: <str; "permit" | "deny"; required>

            # If defined, a standard community-list will be configured.
            # Supported community strings (case insensitive):
            # - GSHUT
            # - internet
            # - local-as
            # - no-advertise
            # - no-export
            # - <1-4294967040>
            # - aa:nn
            communities:
              - <str>

            # Regular Expression.
            # If defined, a regex community-list will be configured.
            regexp: <str>
    ```
