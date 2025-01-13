<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>management_accounts</samp>](## "management_accounts") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;password</samp>](## "management_accounts.password") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;policy</samp>](## "management_accounts.password.policy") | String |  |  |  |  |

=== "YAML"

    ```yaml
    management_accounts:
      password:
        policy: <str>
    ```
