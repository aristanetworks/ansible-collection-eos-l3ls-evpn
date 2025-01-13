<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_domain_lookup</samp>](## "ip_domain_lookup") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;source_interfaces</samp>](## "ip_domain_lookup.source_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "ip_domain_lookup.source_interfaces.[].name") | String | Required, Unique |  |  | Source Interface.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ip_domain_lookup.source_interfaces.[].vrf") | String |  |  |  |  |

=== "YAML"

    ```yaml
    ip_domain_lookup:
      source_interfaces:

          # Source Interface.
        - name: <str; required; unique>
          vrf: <str>
    ```
