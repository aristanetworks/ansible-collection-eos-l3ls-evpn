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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_system_id_prefix</samp>](## "<node_type_keys.key>.defaults.isis_system_id_prefix") | String |  |  | Pattern: `[0-9a-f]{4}\.[0-9a-f]{4}` | (4.4 hexadecimal). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_maximum_paths</samp>](## "<node_type_keys.key>.defaults.isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;is_type</samp>](## "<node_type_keys.key>.defaults.is_type") | String |  |  | Valid Values:<br>- <code>level-1-2</code><br>- <code>level-1</code><br>- <code>level-2</code> | Overrides `isis_default_is_type`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;node_sid_base</samp>](## "<node_type_keys.key>.defaults.node_sid_base") | Integer |  | `0` |  | Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_system_id_prefix</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].isis_system_id_prefix") | String |  |  | Pattern: `[0-9a-f]{4}\.[0-9a-f]{4}` | (4.4 hexadecimal). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_maximum_paths</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;is_type</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].is_type") | String |  |  | Valid Values:<br>- <code>level-1-2</code><br>- <code>level-1</code><br>- <code>level-2</code> | Overrides `isis_default_is_type`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;node_sid_base</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].node_sid_base") | Integer |  | `0` |  | Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_system_id_prefix</samp>](## "<node_type_keys.key>.node_groups.[].isis_system_id_prefix") | String |  |  | Pattern: `[0-9a-f]{4}\.[0-9a-f]{4}` | (4.4 hexadecimal). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_maximum_paths</samp>](## "<node_type_keys.key>.node_groups.[].isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;is_type</samp>](## "<node_type_keys.key>.node_groups.[].is_type") | String |  |  | Valid Values:<br>- <code>level-1-2</code><br>- <code>level-1</code><br>- <code>level-2</code> | Overrides `isis_default_is_type`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;node_sid_base</samp>](## "<node_type_keys.key>.node_groups.[].node_sid_base") | Integer |  | `0` |  | Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_system_id_prefix</samp>](## "<node_type_keys.key>.nodes.[].isis_system_id_prefix") | String |  |  | Pattern: `[0-9a-f]{4}\.[0-9a-f]{4}` | (4.4 hexadecimal). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_maximum_paths</samp>](## "<node_type_keys.key>.nodes.[].isis_maximum_paths") | Integer |  |  |  | Number of path to configure in ECMP for ISIS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;is_type</samp>](## "<node_type_keys.key>.nodes.[].is_type") | String |  |  | Valid Values:<br>- <code>level-1-2</code><br>- <code>level-1</code><br>- <code>level-2</code> | Overrides `isis_default_is_type`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;node_sid_base</samp>](## "<node_type_keys.key>.nodes.[].node_sid_base") | Integer |  | `0` |  | Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:

        # (4.4 hexadecimal).
        isis_system_id_prefix: <str>

        # Number of path to configure in ECMP for ISIS.
        isis_maximum_paths: <int>

        # Overrides `isis_default_is_type`.
        is_type: <str; "level-1-2" | "level-1" | "level-2">

        # Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID.
        node_sid_base: <int; default=0>

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>

              # (4.4 hexadecimal).
              isis_system_id_prefix: <str>

              # Number of path to configure in ECMP for ISIS.
              isis_maximum_paths: <int>

              # Overrides `isis_default_is_type`.
              is_type: <str; "level-1-2" | "level-1" | "level-2">

              # Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID.
              node_sid_base: <int; default=0>

          # (4.4 hexadecimal).
          isis_system_id_prefix: <str>

          # Number of path to configure in ECMP for ISIS.
          isis_maximum_paths: <int>

          # Overrides `isis_default_is_type`.
          is_type: <str; "level-1-2" | "level-1" | "level-2">

          # Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID.
          node_sid_base: <int; default=0>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>

          # (4.4 hexadecimal).
          isis_system_id_prefix: <str>

          # Number of path to configure in ECMP for ISIS.
          isis_maximum_paths: <int>

          # Overrides `isis_default_is_type`.
          is_type: <str; "level-1-2" | "level-1" | "level-2">

          # Node-SID base for isis-sr underlay variants. Combined with node id to generate ISIS-SR node-SID.
          node_sid_base: <int; default=0>
    ```
