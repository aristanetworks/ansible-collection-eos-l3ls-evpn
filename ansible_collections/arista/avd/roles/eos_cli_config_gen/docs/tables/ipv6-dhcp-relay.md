<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ipv6_dhcp_relay</samp>](## "ipv6_dhcp_relay") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;always_on</samp>](## "ipv6_dhcp_relay.always_on") | Boolean |  |  |  | DhcpRelay Agent will be in always-on mode, off by default. |
    | [<samp>&nbsp;&nbsp;all_subnets</samp>](## "ipv6_dhcp_relay.all_subnets") | Boolean |  |  |  | Allow forwarding requests with additional IPv6 addresses in the gateway address "giaddr" field. |
    | [<samp>&nbsp;&nbsp;option</samp>](## "ipv6_dhcp_relay.option") | Dictionary |  |  |  | Insert DHCP Option. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;link_layer_address</samp>](## "ipv6_dhcp_relay.option.link_layer_address") | Boolean |  |  |  | Add Option 79 (Link Layer Address Option). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;remote_id_format</samp>](## "ipv6_dhcp_relay.option.remote_id_format") | String |  |  | Valid Values:<br>- <code>%m:%i</code><br>- <code>%m:%p</code> | Add RemoteID option 37 in format MAC address and interface ID (`%m:%i`) or MAC address and interface name (`%m:%p`). |

=== "YAML"

    ```yaml
    ipv6_dhcp_relay:

      # DhcpRelay Agent will be in always-on mode, off by default.
      always_on: <bool>

      # Allow forwarding requests with additional IPv6 addresses in the gateway address "giaddr" field.
      all_subnets: <bool>

      # Insert DHCP Option.
      option:

        # Add Option 79 (Link Layer Address Option).
        link_layer_address: <bool>

        # Add RemoteID option 37 in format MAC address and interface ID (`%m:%i`) or MAC address and interface name (`%m:%p`).
        remote_id_format: <str; "%m:%i" | "%m:%p">
    ```
