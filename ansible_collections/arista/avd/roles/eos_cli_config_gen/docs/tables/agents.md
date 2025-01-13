<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>agents</samp>](## "agents") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "agents.[].name") | String | Required, Unique |  |  | Agent name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;environment_variables</samp>](## "agents.[].environment_variables") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "agents.[].environment_variables.[].name") | String | Required, Unique |  |  | Environment variable name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "agents.[].environment_variables.[].value") | String | Required |  |  | Environment variable value. |

=== "YAML"

    ```yaml
    agents:

        # Agent name.
      - name: <str; required; unique>
        environment_variables: # >=1 items

            # Environment variable name.
          - name: <str; required; unique>

            # Environment variable value.
            value: <str; required>
    ```
