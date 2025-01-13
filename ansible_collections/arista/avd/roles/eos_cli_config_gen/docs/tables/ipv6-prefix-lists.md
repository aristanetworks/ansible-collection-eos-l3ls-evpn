<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ipv6_prefix_lists</samp>](## "ipv6_prefix_lists") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "ipv6_prefix_lists.[].name") | String | Required, Unique |  |  | Prefix-list Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "ipv6_prefix_lists.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;sequence</samp>](## "ipv6_prefix_lists.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ipv6_prefix_lists.[].sequence_numbers.[].action") | String | Required |  |  | Action as string.<br>Example: "permit 1b11:3a00:22b0:0082::/64 eq 128"<br> |

=== "YAML"

    ```yaml
    ipv6_prefix_lists:

        # Prefix-list Name.
      - name: <str; required; unique>
        sequence_numbers: # required

            # Sequence ID.
          - sequence: <int; required; unique>

            # Action as string.
            # Example: "permit 1b11:3a00:22b0:0082::/64 eq 128"
            action: <str; required>
    ```
