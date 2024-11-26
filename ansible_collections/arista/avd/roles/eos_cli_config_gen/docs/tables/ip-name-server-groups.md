<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_name_server_groups</samp>](## "ip_name_server_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "ip_name_server_groups.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name_servers</samp>](## "ip_name_server_groups.[].name_servers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "ip_name_server_groups.[].name_servers.[].ip_address") | String | Required |  |  | IPv4 or IPv6 address for DNS server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ip_name_server_groups.[].name_servers.[].vrf") | String |  |  |  | VRF Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "ip_name_server_groups.[].name_servers.[].priority") | Integer |  |  | Min: 0<br>Max: 4 | Priority value (lower is first). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dns_domain</samp>](## "ip_name_server_groups.[].dns_domain") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_domain_list</samp>](## "ip_name_server_groups.[].ip_domain_list") | String |  |  |  | Set domain names to complete unqualified host names. |

=== "YAML"

    ```yaml
    ip_name_server_groups:
      - name: <str; required; unique>
        name_servers:

            # IPv4 or IPv6 address for DNS server.
          - ip_address: <str; required>

            # VRF Name.
            vrf: <str>

            # Priority value (lower is first).
            priority: <int; 0-4>
        dns_domain: <str>

        # Set domain names to complete unqualified host names.
        ip_domain_list: <str>
    ```
