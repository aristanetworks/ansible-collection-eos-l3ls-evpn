<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>default_node_types</samp>](## "default_node_types") | List, items: Dictionary |  |  |  | Uses hostname matches against a regular expression to determine the node type. |
    | [<samp>&nbsp;&nbsp;-&nbsp;node_type</samp>](## "default_node_types.[].node_type") | String | Required, Unique |  |  | Resulting node type when regex matches. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;match_hostnames</samp>](## "default_node_types.[].match_hostnames") | List, items: String | Required |  |  | Regular expressions to match against hostnames. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "default_node_types.[].match_hostnames.[]") | String | Required |  |  | Regex needs to match full hostname (i.e. is bounded by ^ and $ elements). |

=== "YAML"

    ```yaml
    # Uses hostname matches against a regular expression to determine the node type.
    default_node_types:

        # Resulting node type when regex matches.
      - node_type: <str; required; unique>

        # Regular expressions to match against hostnames.
        match_hostnames: # required

            # Regex needs to match full hostname (i.e. is bounded by ^ and $ elements).
          - <str; required>
    ```
