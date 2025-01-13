<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>access_lists</samp>](## "access_lists") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "access_lists.[].name") | String | Required, Unique |  |  | Access-list Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp>](## "access_lists.[].counters_per_entry") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;permit_response_traffic</samp>](## "access_lists.[].permit_response_traffic") | String |  |  | Valid Values:<br>- <code>nat</code> | Permit response traffic automatically based on NAT translations.<br>Minimum EOS version requirement 4.32.2F. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "access_lists.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;sequence</samp>](## "access_lists.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "access_lists.[].sequence_numbers.[].action") | String | Required |  |  | Action as string.<br>Example: "deny ip any any"<br> |

=== "YAML"

    ```yaml
    access_lists:

        # Access-list Name.
      - name: <str; required; unique>
        counters_per_entry: <bool>

        # Permit response traffic automatically based on NAT translations.
        # Minimum EOS version requirement 4.32.2F.
        permit_response_traffic: <str; "nat">
        sequence_numbers: # required

            # Sequence ID.
          - sequence: <int; required; unique>

            # Action as string.
            # Example: "deny ip any any"
            action: <str; required>
    ```
