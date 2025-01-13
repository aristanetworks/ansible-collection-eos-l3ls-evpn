<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>network_services_keys</samp>](## "network_services_keys") | List, items: Dictionary |  | `[{'name': 'tenants'}]` |  | Network Services can be grouped by using separate keys.<br>The keys can be customized to provide a better better organization or grouping of your data.<br>`network_services_keys` should be defined in the top level group_vars for the fabric.<br>The default values will be overridden if defining this key, so it is recommended to copy the defaults and modify them.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "network_services_keys.[].name") | String | Required, Unique |  |  |  |

=== "YAML"

    ```yaml
    # Network Services can be grouped by using separate keys.
    # The keys can be customized to provide a better better organization or grouping of your data.
    # `network_services_keys` should be defined in the top level group_vars for the fabric.
    # The default values will be overridden if defining this key, so it is recommended to copy the defaults and modify them.
    network_services_keys: # default=[{'name': 'tenants'}]
      - name: <str; required; unique>
    ```
