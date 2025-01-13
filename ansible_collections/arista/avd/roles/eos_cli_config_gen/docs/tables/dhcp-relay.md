<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>dhcp_relay</samp>](## "dhcp_relay") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;servers</samp>](## "dhcp_relay.servers") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "dhcp_relay.servers.[]") | String |  |  |  | Server IP or Hostname. |
    | [<samp>&nbsp;&nbsp;tunnel_requests_disabled</samp>](## "dhcp_relay.tunnel_requests_disabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;mlag_peerlink_requests_disabled</samp>](## "dhcp_relay.mlag_peerlink_requests_disabled") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    dhcp_relay:
      servers:

          # Server IP or Hostname.
        - <str>
      tunnel_requests_disabled: <bool>
      mlag_peerlink_requests_disabled: <bool>
    ```
