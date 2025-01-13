<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_service_insertion</samp>](## "router_service_insertion") | Dictionary |  |  |  | Configure network services inserted to data forwarding. |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "router_service_insertion.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;connections</samp>](## "router_service_insertion.connections") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_service_insertion.connections.[].name") | String | Required, Unique |  |  | Connection name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ethernet_interface</samp>](## "router_service_insertion.connections.[].ethernet_interface") | Dictionary |  |  |  | Outgoing physical interface or subinterface to use for the connection.<br>If both `ethernet_interface` and `tunnel_interface` are configured, `ethernet_interface` will be used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "router_service_insertion.connections.[].ethernet_interface.name") | String | Required |  |  | e.g. Ethernet2 or Ethernet2/2.2 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop</samp>](## "router_service_insertion.connections.[].ethernet_interface.next_hop") | String | Required |  |  | Next-hop IPv4 address (without mask). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tunnel_interface</samp>](## "router_service_insertion.connections.[].tunnel_interface") | Dictionary |  |  |  | Outgoing tunnel interface(s) to use for this connection.<br>If both `ethernet_interface` and `tunnel_interface` are configured, `ethernet_interface` will be used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primary</samp>](## "router_service_insertion.connections.[].tunnel_interface.primary") | String |  |  |  | e.g. Tunnel2 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;secondary</samp>](## "router_service_insertion.connections.[].tunnel_interface.secondary") | String |  |  |  | e.g. Tunnel3 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;monitor_connectivity_host</samp>](## "router_service_insertion.connections.[].monitor_connectivity_host") | String |  |  |  | Name of the host defined under `monitor_connectivity.hosts` used to derive the health of the connection. |

=== "YAML"

    ```yaml
    # Configure network services inserted to data forwarding.
    router_service_insertion:
      enabled: <bool>
      connections:

          # Connection name.
        - name: <str; required; unique>

          # Outgoing physical interface or subinterface to use for the connection.
          # If both `ethernet_interface` and `tunnel_interface` are configured, `ethernet_interface` will be used.
          ethernet_interface:

            # e.g. Ethernet2 or Ethernet2/2.2
            name: <str; required>

            # Next-hop IPv4 address (without mask).
            next_hop: <str; required>

          # Outgoing tunnel interface(s) to use for this connection.
          # If both `ethernet_interface` and `tunnel_interface` are configured, `ethernet_interface` will be used.
          tunnel_interface:

            # e.g. Tunnel2
            primary: <str>

            # e.g. Tunnel3
            secondary: <str>

          # Name of the host defined under `monitor_connectivity.hosts` used to derive the health of the connection.
          monitor_connectivity_host: <str>
    ```
