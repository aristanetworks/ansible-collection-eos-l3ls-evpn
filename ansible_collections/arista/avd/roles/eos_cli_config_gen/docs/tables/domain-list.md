<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>domain_list</samp>](## "domain_list") | List, items: String |  |  |  | Search list of DNS domains. |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "domain_list.[]") | String |  |  |  | Domain name. |

=== "YAML"

    ```yaml
    # Search list of DNS domains.
    domain_list:

        # Domain name.
      - <str>
    ```
