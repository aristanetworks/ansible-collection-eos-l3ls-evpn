<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>management_api_models</samp>](## "management_api_models") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;providers</samp>](## "management_api_models.providers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "management_api_models.providers.[].name") | String |  |  | Valid Values:<br>- <code>sysdb</code><br>- <code>smash</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;paths</samp>](## "management_api_models.providers.[].paths") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;path</samp>](## "management_api_models.providers.[].paths.[].path") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "management_api_models.providers.[].paths.[].disabled") | Boolean |  | `False` |  |  |

=== "YAML"

    ```yaml
    management_api_models:
      providers:
        - name: <str; "sysdb" | "smash">
          paths:
            - path: <str>
              disabled: <bool; default=False>
    ```
