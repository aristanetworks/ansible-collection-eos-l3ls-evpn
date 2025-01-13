<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_dhcp_relay</samp>](## "ip_dhcp_relay") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;always_on</samp>](## "ip_dhcp_relay.always_on") | Boolean |  |  |  | DhcpRelay Agent will be in always-on mode. |
    | [<samp>&nbsp;&nbsp;all_subnets</samp>](## "ip_dhcp_relay.all_subnets") | Boolean |  |  |  | Allow forwarding requests with secondary IP addresses in the gateway address "giaddr" field. |
    | [<samp>&nbsp;&nbsp;information_option</samp>](## "ip_dhcp_relay.information_option") | Boolean |  |  |  | Insert Option-82 information. |

=== "YAML"

    ```yaml
    ip_dhcp_relay:

      # DhcpRelay Agent will be in always-on mode.
      always_on: <bool>

      # Allow forwarding requests with secondary IP addresses in the gateway address "giaddr" field.
      all_subnets: <bool>

      # Insert Option-82 information.
      information_option: <bool>
    ```
