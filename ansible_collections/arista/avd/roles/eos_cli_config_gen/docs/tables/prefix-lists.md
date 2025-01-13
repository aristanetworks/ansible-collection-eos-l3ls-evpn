<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>prefix_lists</samp>](## "prefix_lists") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "prefix_lists.[].name") | String | Required, Unique |  |  | Prefix-list Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "prefix_lists.[].sequence_numbers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;sequence</samp>](## "prefix_lists.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "prefix_lists.[].sequence_numbers.[].action") | String | Required |  |  | Action as string.<br>Example: "permit 10.255.0.0/27 eq 32"<br> |

=== "YAML"

    ```yaml
    prefix_lists:

        # Prefix-list Name.
      - name: <str; required; unique>
        sequence_numbers:

            # Sequence ID.
          - sequence: <int; required; unique>

            # Action as string.
            # Example: "permit 10.255.0.0/27 eq 32"
            action: <str; required>
    ```
