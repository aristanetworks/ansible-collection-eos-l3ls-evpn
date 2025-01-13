<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;network_services_keys.name&gt;</samp>](## "<network_services_keys.name>") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "<network_services_keys.name>.[].name") | String | Required, Unique |  |  | Specify a tenant name.<br>Tenant provide a construct to group L3 VRFs and L2 VLANs.<br>Networks services can be filtered by tenant name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pseudowire_rt_base</samp>](## "<network_services_keys.name>.[].pseudowire_rt_base") | Integer |  |  |  | Pseudowire RT base, used to generate route targets for VPWS services.<br>Avoid overlapping route target spaces between different services.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;point_to_point_services</samp>](## "<network_services_keys.name>.[].point_to_point_services") | List, items: Dictionary |  |  |  | Point to point services (pseudowires).<br>Only supported for node types with "network_services.l1: true".<br>By default this is only set for node type "pe" with "design.type: mpls"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<network_services_keys.name>.[].point_to_point_services.[].name") | String | Required, Unique |  |  | Pseudowire name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "<network_services_keys.name>.[].point_to_point_services.[].type") | String |  | `vpws-pseudowire` | Valid Values:<br>- <code>vpws-pseudowire</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subinterfaces</samp>](## "<network_services_keys.name>.[].point_to_point_services.[].subinterfaces") | List, items: Dictionary |  |  |  | Subinterfaces will create subinterfaces and additional pseudowires/patch panel config for each endpoint. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;number</samp>](## "<network_services_keys.name>.[].point_to_point_services.[].subinterfaces.[].number") | Integer | Required, Unique |  |  | Subinterface number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;endpoints</samp>](## "<network_services_keys.name>.[].point_to_point_services.[].endpoints") | List, items: Dictionary |  |  | Min Length: 2<br>Max Length: 2 | Pseudowire terminating endpoints. Must have exactly two items. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "<network_services_keys.name>.[].point_to_point_services.[].endpoints.[].id") | Integer | Required |  |  | Pseudowire ID on this endpoint. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<network_services_keys.name>.[].point_to_point_services.[].endpoints.[].nodes") | List, items: String | Required |  | Min Length: 1 | Usually one node. With ESI multihoming we support two nodes per pseudowire endpoint. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].point_to_point_services.[].endpoints.[].nodes.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "<network_services_keys.name>.[].point_to_point_services.[].endpoints.[].interfaces") | List, items: String | Required |  | Min Length: 1 | Interfaces patched to the pseudowire on this endpoints.<br>The list of interfaces is mapped to the list of nodes, so they must have the same length.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].point_to_point_services.[].endpoints.[].interfaces.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_channel</samp>](## "<network_services_keys.name>.[].point_to_point_services.[].endpoints.[].port_channel") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "<network_services_keys.name>.[].point_to_point_services.[].endpoints.[].port_channel.mode") | String |  |  | Valid Values:<br>- <code>active</code><br>- <code>on</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;short_esi</samp>](## "<network_services_keys.name>.[].point_to_point_services.[].endpoints.[].port_channel.short_esi") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lldp_disable</samp>](## "<network_services_keys.name>.[].point_to_point_services.[].lldp_disable") | Boolean |  |  |  | Disable LLDP RX/TX on port mode pseudowire services. |

=== "YAML"

    ```yaml
    <network_services_keys.name>:

        # Specify a tenant name.
        # Tenant provide a construct to group L3 VRFs and L2 VLANs.
        # Networks services can be filtered by tenant name.
      - name: <str; required; unique>

        # Pseudowire RT base, used to generate route targets for VPWS services.
        # Avoid overlapping route target spaces between different services.
        pseudowire_rt_base: <int>

        # Point to point services (pseudowires).
        # Only supported for node types with "network_services.l1: true".
        # By default this is only set for node type "pe" with "design.type: mpls"
        point_to_point_services:

            # Pseudowire name.
          - name: <str; required; unique>
            type: <str; "vpws-pseudowire"; default="vpws-pseudowire">

            # Subinterfaces will create subinterfaces and additional pseudowires/patch panel config for each endpoint.
            subinterfaces:

                # Subinterface number.
              - number: <int; required; unique>

            # Pseudowire terminating endpoints. Must have exactly two items.
            endpoints: # 2-2 items

                # Pseudowire ID on this endpoint.
              - id: <int; required>

                # Usually one node. With ESI multihoming we support two nodes per pseudowire endpoint.
                nodes: # >=1 items; required
                  - <str>

                # Interfaces patched to the pseudowire on this endpoints.
                # The list of interfaces is mapped to the list of nodes, so they must have the same length.
                interfaces: # >=1 items; required
                  - <str>
                port_channel:
                  mode: <str; "active" | "on">
                  short_esi: <str>

            # Disable LLDP RX/TX on port mode pseudowire services.
            lldp_disable: <bool>
    ```
