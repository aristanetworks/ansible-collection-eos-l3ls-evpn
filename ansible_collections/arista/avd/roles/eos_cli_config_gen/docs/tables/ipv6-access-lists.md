<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ipv6_access_lists</samp>](## "ipv6_access_lists") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "ipv6_access_lists.[].name") | String | Required, Unique |  |  | IPv6 Access-list Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp>](## "ipv6_access_lists.[].counters_per_entry") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "ipv6_access_lists.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;sequence</samp>](## "ipv6_access_lists.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ipv6_access_lists.[].sequence_numbers.[].action") | String | Required |  |  | Action as string.<br>Example: "deny ipv6 any any"<br> |

=== "YAML"

    ```yaml
    ipv6_access_lists:

        # IPv6 Access-list Name.
      - name: <str; required; unique>
        counters_per_entry: <bool>
        sequence_numbers: # required

            # Sequence ID.
          - sequence: <int; required; unique>

            # Action as string.
            # Example: "deny ipv6 any any"
            action: <str; required>
    ```
