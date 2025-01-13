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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_pool</samp>](## "<node_type_keys.key>.defaults.loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_address</samp>](## "<node_type_keys.key>.defaults.loopback_ipv4_address") | String |  |  | Format: ipv4 | IPv4 address without mask for Loopback0.<br>When set, it takes precedence over `loopback_ipv4_pool`.<br>Note: AVD does not check for validity of the IPv4 address and does not catch duplicates. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_pool</samp>](## "<node_type_keys.key>.defaults.vtep_loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for VTEP-Loopback allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_address</samp>](## "<node_type_keys.key>.defaults.vtep_loopback_ipv4_address") | String |  |  | Format: ipv4 | IPv4 address without mask for VTEP-Loopback.<br>When set, it takes precedence over `vtep_loopback_ipv4_pool`.<br>Note: AVD does not check for validity of the IPv4 address and does not catch duplicates. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_offset</samp>](## "<node_type_keys.key>.defaults.loopback_ipv4_offset") | Integer |  | `0` |  | Offset all assigned loopback IP addresses.<br>Required when the < loopback_ipv4_pool > is same for 2 different node_types (like spine and l3leaf) to avoid over-lapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_pool</samp>](## "<node_type_keys.key>.defaults.loopback_ipv6_pool") | String |  |  | Format: ipv6_cidr | IPv6 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_offset</samp>](## "<node_type_keys.key>.defaults.loopback_ipv6_offset") | Integer |  | `0` |  | Offset all assigned loopback IPv6 addresses.<br>Required when the < loopback_ipv6_pool > is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vtep</samp>](## "<node_type_keys.key>.defaults.vtep") | Boolean |  |  |  | Node is configured as a VTEP when applicable based on 'overlay_routing_protocol'.<br>Overrides VTEP setting inherited from node_type_keys. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback</samp>](## "<node_type_keys.key>.defaults.vtep_loopback") | String |  |  | Pattern: `Loopback[\d/]+` | Set VXLAN source interface. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_pool</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_address</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].loopback_ipv4_address") | String |  |  | Format: ipv4 | IPv4 address without mask for Loopback0.<br>When set, it takes precedence over `loopback_ipv4_pool`.<br>Note: AVD does not check for validity of the IPv4 address and does not catch duplicates. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_pool</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].vtep_loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for VTEP-Loopback allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_address</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].vtep_loopback_ipv4_address") | String |  |  | Format: ipv4 | IPv4 address without mask for VTEP-Loopback.<br>When set, it takes precedence over `vtep_loopback_ipv4_pool`.<br>Note: AVD does not check for validity of the IPv4 address and does not catch duplicates. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_offset</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].loopback_ipv4_offset") | Integer |  | `0` |  | Offset all assigned loopback IP addresses.<br>Required when the < loopback_ipv4_pool > is same for 2 different node_types (like spine and l3leaf) to avoid over-lapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_pool</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].loopback_ipv6_pool") | String |  |  | Format: ipv6_cidr | IPv6 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_offset</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].loopback_ipv6_offset") | Integer |  | `0` |  | Offset all assigned loopback IPv6 addresses.<br>Required when the < loopback_ipv6_pool > is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].vtep") | Boolean |  |  |  | Node is configured as a VTEP when applicable based on 'overlay_routing_protocol'.<br>Overrides VTEP setting inherited from node_type_keys. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].vtep_loopback") | String |  |  | Pattern: `Loopback[\d/]+` | Set VXLAN source interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_pool</samp>](## "<node_type_keys.key>.node_groups.[].loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_address</samp>](## "<node_type_keys.key>.node_groups.[].loopback_ipv4_address") | String |  |  | Format: ipv4 | IPv4 address without mask for Loopback0.<br>When set, it takes precedence over `loopback_ipv4_pool`.<br>Note: AVD does not check for validity of the IPv4 address and does not catch duplicates. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_pool</samp>](## "<node_type_keys.key>.node_groups.[].vtep_loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for VTEP-Loopback allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_address</samp>](## "<node_type_keys.key>.node_groups.[].vtep_loopback_ipv4_address") | String |  |  | Format: ipv4 | IPv4 address without mask for VTEP-Loopback.<br>When set, it takes precedence over `vtep_loopback_ipv4_pool`.<br>Note: AVD does not check for validity of the IPv4 address and does not catch duplicates. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_offset</samp>](## "<node_type_keys.key>.node_groups.[].loopback_ipv4_offset") | Integer |  | `0` |  | Offset all assigned loopback IP addresses.<br>Required when the < loopback_ipv4_pool > is same for 2 different node_types (like spine and l3leaf) to avoid over-lapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_pool</samp>](## "<node_type_keys.key>.node_groups.[].loopback_ipv6_pool") | String |  |  | Format: ipv6_cidr | IPv6 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_offset</samp>](## "<node_type_keys.key>.node_groups.[].loopback_ipv6_offset") | Integer |  | `0` |  | Offset all assigned loopback IPv6 addresses.<br>Required when the < loopback_ipv6_pool > is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep</samp>](## "<node_type_keys.key>.node_groups.[].vtep") | Boolean |  |  |  | Node is configured as a VTEP when applicable based on 'overlay_routing_protocol'.<br>Overrides VTEP setting inherited from node_type_keys. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback</samp>](## "<node_type_keys.key>.node_groups.[].vtep_loopback") | String |  |  | Pattern: `Loopback[\d/]+` | Set VXLAN source interface. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_pool</samp>](## "<node_type_keys.key>.nodes.[].loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_address</samp>](## "<node_type_keys.key>.nodes.[].loopback_ipv4_address") | String |  |  | Format: ipv4 | IPv4 address without mask for Loopback0.<br>When set, it takes precedence over `loopback_ipv4_pool`.<br>Note: AVD does not check for validity of the IPv4 address and does not catch duplicates. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_pool</samp>](## "<node_type_keys.key>.nodes.[].vtep_loopback_ipv4_pool") | String |  |  | Format: ipv4_cidr | IPv4 subnet for VTEP-Loopback allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback_ipv4_address</samp>](## "<node_type_keys.key>.nodes.[].vtep_loopback_ipv4_address") | String |  |  | Format: ipv4 | IPv4 address without mask for VTEP-Loopback.<br>When set, it takes precedence over `vtep_loopback_ipv4_pool`.<br>Note: AVD does not check for validity of the IPv4 address and does not catch duplicates. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv4_offset</samp>](## "<node_type_keys.key>.nodes.[].loopback_ipv4_offset") | Integer |  | `0` |  | Offset all assigned loopback IP addresses.<br>Required when the < loopback_ipv4_pool > is same for 2 different node_types (like spine and l3leaf) to avoid over-lapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_pool</samp>](## "<node_type_keys.key>.nodes.[].loopback_ipv6_pool") | String |  |  | Format: ipv6_cidr | IPv6 subnet for Loopback0 allocation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ipv6_offset</samp>](## "<node_type_keys.key>.nodes.[].loopback_ipv6_offset") | Integer |  | `0` |  | Offset all assigned loopback IPv6 addresses.<br>Required when the < loopback_ipv6_pool > is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.<br>For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep</samp>](## "<node_type_keys.key>.nodes.[].vtep") | Boolean |  |  |  | Node is configured as a VTEP when applicable based on 'overlay_routing_protocol'.<br>Overrides VTEP setting inherited from node_type_keys. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_loopback</samp>](## "<node_type_keys.key>.nodes.[].vtep_loopback") | String |  |  | Pattern: `Loopback[\d/]+` | Set VXLAN source interface. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:

        # IPv4 subnet for Loopback0 allocation.
        loopback_ipv4_pool: <str>

        # IPv4 address without mask for Loopback0.
        # When set, it takes precedence over `loopback_ipv4_pool`.
        # Note: AVD does not check for validity of the IPv4 address and does not catch duplicates.
        loopback_ipv4_address: <str>

        # IPv4 subnet for VTEP-Loopback allocation.
        vtep_loopback_ipv4_pool: <str>

        # IPv4 address without mask for VTEP-Loopback.
        # When set, it takes precedence over `vtep_loopback_ipv4_pool`.
        # Note: AVD does not check for validity of the IPv4 address and does not catch duplicates.
        vtep_loopback_ipv4_address: <str>

        # Offset all assigned loopback IP addresses.
        # Required when the < loopback_ipv4_pool > is same for 2 different node_types (like spine and l3leaf) to avoid over-lapping IPs.
        # For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.
        loopback_ipv4_offset: <int; default=0>

        # IPv6 subnet for Loopback0 allocation.
        loopback_ipv6_pool: <str>

        # Offset all assigned loopback IPv6 addresses.
        # Required when the < loopback_ipv6_pool > is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.
        # For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.
        loopback_ipv6_offset: <int; default=0>

        # Node is configured as a VTEP when applicable based on 'overlay_routing_protocol'.
        # Overrides VTEP setting inherited from node_type_keys.
        vtep: <bool>

        # Set VXLAN source interface.
        vtep_loopback: <str>

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>

              # IPv4 subnet for Loopback0 allocation.
              loopback_ipv4_pool: <str>

              # IPv4 address without mask for Loopback0.
              # When set, it takes precedence over `loopback_ipv4_pool`.
              # Note: AVD does not check for validity of the IPv4 address and does not catch duplicates.
              loopback_ipv4_address: <str>

              # IPv4 subnet for VTEP-Loopback allocation.
              vtep_loopback_ipv4_pool: <str>

              # IPv4 address without mask for VTEP-Loopback.
              # When set, it takes precedence over `vtep_loopback_ipv4_pool`.
              # Note: AVD does not check for validity of the IPv4 address and does not catch duplicates.
              vtep_loopback_ipv4_address: <str>

              # Offset all assigned loopback IP addresses.
              # Required when the < loopback_ipv4_pool > is same for 2 different node_types (like spine and l3leaf) to avoid over-lapping IPs.
              # For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.
              loopback_ipv4_offset: <int; default=0>

              # IPv6 subnet for Loopback0 allocation.
              loopback_ipv6_pool: <str>

              # Offset all assigned loopback IPv6 addresses.
              # Required when the < loopback_ipv6_pool > is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.
              # For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.
              loopback_ipv6_offset: <int; default=0>

              # Node is configured as a VTEP when applicable based on 'overlay_routing_protocol'.
              # Overrides VTEP setting inherited from node_type_keys.
              vtep: <bool>

              # Set VXLAN source interface.
              vtep_loopback: <str>

          # IPv4 subnet for Loopback0 allocation.
          loopback_ipv4_pool: <str>

          # IPv4 address without mask for Loopback0.
          # When set, it takes precedence over `loopback_ipv4_pool`.
          # Note: AVD does not check for validity of the IPv4 address and does not catch duplicates.
          loopback_ipv4_address: <str>

          # IPv4 subnet for VTEP-Loopback allocation.
          vtep_loopback_ipv4_pool: <str>

          # IPv4 address without mask for VTEP-Loopback.
          # When set, it takes precedence over `vtep_loopback_ipv4_pool`.
          # Note: AVD does not check for validity of the IPv4 address and does not catch duplicates.
          vtep_loopback_ipv4_address: <str>

          # Offset all assigned loopback IP addresses.
          # Required when the < loopback_ipv4_pool > is same for 2 different node_types (like spine and l3leaf) to avoid over-lapping IPs.
          # For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.
          loopback_ipv4_offset: <int; default=0>

          # IPv6 subnet for Loopback0 allocation.
          loopback_ipv6_pool: <str>

          # Offset all assigned loopback IPv6 addresses.
          # Required when the < loopback_ipv6_pool > is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.
          # For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.
          loopback_ipv6_offset: <int; default=0>

          # Node is configured as a VTEP when applicable based on 'overlay_routing_protocol'.
          # Overrides VTEP setting inherited from node_type_keys.
          vtep: <bool>

          # Set VXLAN source interface.
          vtep_loopback: <str>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>

          # IPv4 subnet for Loopback0 allocation.
          loopback_ipv4_pool: <str>

          # IPv4 address without mask for Loopback0.
          # When set, it takes precedence over `loopback_ipv4_pool`.
          # Note: AVD does not check for validity of the IPv4 address and does not catch duplicates.
          loopback_ipv4_address: <str>

          # IPv4 subnet for VTEP-Loopback allocation.
          vtep_loopback_ipv4_pool: <str>

          # IPv4 address without mask for VTEP-Loopback.
          # When set, it takes precedence over `vtep_loopback_ipv4_pool`.
          # Note: AVD does not check for validity of the IPv4 address and does not catch duplicates.
          vtep_loopback_ipv4_address: <str>

          # Offset all assigned loopback IP addresses.
          # Required when the < loopback_ipv4_pool > is same for 2 different node_types (like spine and l3leaf) to avoid over-lapping IPs.
          # For example, set the minimum offset l3leaf.defaults.loopback_ipv4_offset: < total # spine switches > or vice versa.
          loopback_ipv4_offset: <int; default=0>

          # IPv6 subnet for Loopback0 allocation.
          loopback_ipv6_pool: <str>

          # Offset all assigned loopback IPv6 addresses.
          # Required when the < loopback_ipv6_pool > is same for 2 different node_types (like spine and l3leaf) to avoid overlapping IPs.
          # For example, set the minimum offset l3leaf.defaults.loopback_ipv6_offset: < total # spine switches > or vice versa.
          loopback_ipv6_offset: <int; default=0>

          # Node is configured as a VTEP when applicable based on 'overlay_routing_protocol'.
          # Overrides VTEP setting inherited from node_type_keys.
          vtep: <bool>

          # Set VXLAN source interface.
          vtep_loopback: <str>
    ```
