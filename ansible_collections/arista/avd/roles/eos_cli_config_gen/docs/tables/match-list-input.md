<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>match_list_input</samp>](## "match_list_input") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;prefix_ipv4</samp>](## "match_list_input.prefix_ipv4") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "match_list_input.prefix_ipv4.[].name") | String | Required, Unique |  |  | Prefix-List Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefixes</samp>](## "match_list_input.prefix_ipv4.[].prefixes") | List, items: String | Required |  | Min Length: 1 | List of IPv4 prefixes (with the subnet mask e.g. 192.0.2.0/24). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "match_list_input.prefix_ipv4.[].prefixes.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;prefix_ipv6</samp>](## "match_list_input.prefix_ipv6") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "match_list_input.prefix_ipv6.[].name") | String | Required, Unique |  |  | Prefix-List Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefixes</samp>](## "match_list_input.prefix_ipv6.[].prefixes") | List, items: String | Required |  | Min Length: 1 | List of IPv6 prefixes (with the subnet mask e.g. 2001:db8:abcd:0013::/64). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "match_list_input.prefix_ipv6.[].prefixes.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;string</samp>](## "match_list_input.string") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "match_list_input.string.[].name") | String | Required, Unique |  |  | Match-list Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "match_list_input.string.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;sequence</samp>](## "match_list_input.string.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_regex</samp>](## "match_list_input.string.[].sequence_numbers.[].match_regex") | String | Required |  |  | Regular Expression. |

=== "YAML"

    ```yaml
    match_list_input:
      prefix_ipv4:

          # Prefix-List Name.
        - name: <str; required; unique>

          # List of IPv4 prefixes (with the subnet mask e.g. 192.0.2.0/24).
          prefixes: # >=1 items; required
            - <str>
      prefix_ipv6:

          # Prefix-List Name.
        - name: <str; required; unique>

          # List of IPv6 prefixes (with the subnet mask e.g. 2001:db8:abcd:0013::/64).
          prefixes: # >=1 items; required
            - <str>
      string:

          # Match-list Name.
        - name: <str; required; unique>
          sequence_numbers: # required

              # Sequence ID.
            - sequence: <int; required; unique>

              # Regular Expression.
              match_regex: <str; required>
    ```
