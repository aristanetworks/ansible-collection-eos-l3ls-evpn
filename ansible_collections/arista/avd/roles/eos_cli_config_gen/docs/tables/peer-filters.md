<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>peer_filters</samp>](## "peer_filters") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "peer_filters.[].name") | String | Required, Unique |  |  | Peer-filter Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "peer_filters.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;sequence</samp>](## "peer_filters.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match</samp>](## "peer_filters.[].sequence_numbers.[].match") | String | Required |  |  | Match as string.<br>Example: "as-range 1-100 result accept"<br> |

=== "YAML"

    ```yaml
    peer_filters:

        # Peer-filter Name.
      - name: <str; required; unique>
        sequence_numbers: # required

            # Sequence ID.
          - sequence: <int; required; unique>

            # Match as string.
            # Example: "as-range 1-100 result accept"
            match: <str; required>
    ```
