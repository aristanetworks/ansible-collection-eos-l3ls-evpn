<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "<node_type_keys.key>") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "<node_type_keys.key>.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls_overlay_role</samp>](## "<node_type_keys.key>.defaults.mpls_overlay_role") | String |  |  | Valid Values:<br>- <code>client</code><br>- <code>server</code><br>- <code>none</code> | Set the default mpls overlay role.<br>Acting role in overlay control plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;overlay_address_families</samp>](## "<node_type_keys.key>.defaults.overlay_address_families") | List, items: String |  |  |  | Set the default overlay address families.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.defaults.overlay_address_families.[]") | String |  |  | Valid Values:<br>- <code>evpn</code><br>- <code>vpn-ipv4</code><br>- <code>vpn-ipv6</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls_route_reflectors</samp>](## "<node_type_keys.key>.defaults.mpls_route_reflectors") | List, items: String |  |  |  | List of inventory hostname acting as MPLS route-reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.defaults.mpls_route_reflectors.[]") | String |  |  |  | Inventory_hostname_of_mpls_route_reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_cluster_id</samp>](## "<node_type_keys.key>.defaults.bgp_cluster_id") | String |  |  |  | Set BGP cluster id. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_overlay_role</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mpls_overlay_role") | String |  |  | Valid Values:<br>- <code>client</code><br>- <code>server</code><br>- <code>none</code> | Set the default mpls overlay role.<br>Acting role in overlay control plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;overlay_address_families</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].overlay_address_families") | List, items: String |  |  |  | Set the default overlay address families.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].overlay_address_families.[]") | String |  |  | Valid Values:<br>- <code>evpn</code><br>- <code>vpn-ipv4</code><br>- <code>vpn-ipv6</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_route_reflectors</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mpls_route_reflectors") | List, items: String |  |  |  | List of inventory hostname acting as MPLS route-reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mpls_route_reflectors.[]") | String |  |  |  | Inventory_hostname_of_mpls_route_reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_cluster_id</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].bgp_cluster_id") | String |  |  |  | Set BGP cluster id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_overlay_role</samp>](## "<node_type_keys.key>.node_groups.[].mpls_overlay_role") | String |  |  | Valid Values:<br>- <code>client</code><br>- <code>server</code><br>- <code>none</code> | Set the default mpls overlay role.<br>Acting role in overlay control plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;overlay_address_families</samp>](## "<node_type_keys.key>.node_groups.[].overlay_address_families") | List, items: String |  |  |  | Set the default overlay address families.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].overlay_address_families.[]") | String |  |  | Valid Values:<br>- <code>evpn</code><br>- <code>vpn-ipv4</code><br>- <code>vpn-ipv6</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_route_reflectors</samp>](## "<node_type_keys.key>.node_groups.[].mpls_route_reflectors") | List, items: String |  |  |  | List of inventory hostname acting as MPLS route-reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].mpls_route_reflectors.[]") | String |  |  |  | Inventory_hostname_of_mpls_route_reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_cluster_id</samp>](## "<node_type_keys.key>.node_groups.[].bgp_cluster_id") | String |  |  |  | Set BGP cluster id. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_overlay_role</samp>](## "<node_type_keys.key>.nodes.[].mpls_overlay_role") | String |  |  | Valid Values:<br>- <code>client</code><br>- <code>server</code><br>- <code>none</code> | Set the default mpls overlay role.<br>Acting role in overlay control plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;overlay_address_families</samp>](## "<node_type_keys.key>.nodes.[].overlay_address_families") | List, items: String |  |  |  | Set the default overlay address families.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.nodes.[].overlay_address_families.[]") | String |  |  | Valid Values:<br>- <code>evpn</code><br>- <code>vpn-ipv4</code><br>- <code>vpn-ipv6</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_route_reflectors</samp>](## "<node_type_keys.key>.nodes.[].mpls_route_reflectors") | List, items: String |  |  |  | List of inventory hostname acting as MPLS route-reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.nodes.[].mpls_route_reflectors.[]") | String |  |  |  | Inventory_hostname_of_mpls_route_reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_cluster_id</samp>](## "<node_type_keys.key>.nodes.[].bgp_cluster_id") | String |  |  |  | Set BGP cluster id. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:

        # Set the default mpls overlay role.
        # Acting role in overlay control plane.
        mpls_overlay_role: <str; "client" | "server" | "none">

        # Set the default overlay address families.
        overlay_address_families:
          - <str; "evpn" | "vpn-ipv4" | "vpn-ipv6">

        # List of inventory hostname acting as MPLS route-reflectors.
        mpls_route_reflectors:

            # Inventory_hostname_of_mpls_route_reflectors.
          - <str>

        # Set BGP cluster id.
        bgp_cluster_id: <str>

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>

              # Set the default mpls overlay role.
              # Acting role in overlay control plane.
              mpls_overlay_role: <str; "client" | "server" | "none">

              # Set the default overlay address families.
              overlay_address_families:
                - <str; "evpn" | "vpn-ipv4" | "vpn-ipv6">

              # List of inventory hostname acting as MPLS route-reflectors.
              mpls_route_reflectors:

                  # Inventory_hostname_of_mpls_route_reflectors.
                - <str>

              # Set BGP cluster id.
              bgp_cluster_id: <str>

          # Set the default mpls overlay role.
          # Acting role in overlay control plane.
          mpls_overlay_role: <str; "client" | "server" | "none">

          # Set the default overlay address families.
          overlay_address_families:
            - <str; "evpn" | "vpn-ipv4" | "vpn-ipv6">

          # List of inventory hostname acting as MPLS route-reflectors.
          mpls_route_reflectors:

              # Inventory_hostname_of_mpls_route_reflectors.
            - <str>

          # Set BGP cluster id.
          bgp_cluster_id: <str>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>

          # Set the default mpls overlay role.
          # Acting role in overlay control plane.
          mpls_overlay_role: <str; "client" | "server" | "none">

          # Set the default overlay address families.
          overlay_address_families:
            - <str; "evpn" | "vpn-ipv4" | "vpn-ipv6">

          # List of inventory hostname acting as MPLS route-reflectors.
          mpls_route_reflectors:

              # Inventory_hostname_of_mpls_route_reflectors.
            - <str>

          # Set BGP cluster id.
          bgp_cluster_id: <str>
    ```
