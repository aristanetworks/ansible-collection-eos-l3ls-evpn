<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ipv4_prefix_list_catalog</samp>](## "ipv4_prefix_list_catalog") | List, items: Dictionary |  |  |  | IPv4 prefix-list catalog. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "ipv4_prefix_list_catalog.[].name") | String | Required, Unique |  |  | Prefix-list Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "ipv4_prefix_list_catalog.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;sequence</samp>](## "ipv4_prefix_list_catalog.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ipv4_prefix_list_catalog.[].sequence_numbers.[].action") | String | Required |  |  | Action as string.<br>Example: "permit 10.255.0.0/27 eq 32" |

=== "YAML"

    ```yaml
    # IPv4 prefix-list catalog.
    ipv4_prefix_list_catalog:

        # Prefix-list Name.
      - name: <str; required; unique>
        sequence_numbers: # required

            # Sequence ID.
          - sequence: <int; required; unique>

            # Action as string.
            # Example: "permit 10.255.0.0/27 eq 32"
            action: <str; required>
    ```
