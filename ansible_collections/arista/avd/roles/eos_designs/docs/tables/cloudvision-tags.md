<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cv_tags_topology_type</samp>](## "cv_tags_topology_type") | String |  |  | Valid Values:<br>- <code>leaf</code><br>- <code>spine</code><br>- <code>core</code><br>- <code>edge</code> | PREVIEW: This key is currently not supported<br>Device type that CloudVision should use when generating the Topology. Defaults to the setting under node_type_keys. |
    | [<samp>generate_cv_tags</samp>](## "generate_cv_tags") | Dictionary |  |  |  | PREVIEW: This key is currently not supported<br>Generate CloudVision Tags based on AVD data. |
    | [<samp>&nbsp;&nbsp;topology_hints</samp>](## "generate_cv_tags.topology_hints") | Boolean |  | `False` |  | Enable the generation of CloudVision Topology Tags (hints). |
    | [<samp>&nbsp;&nbsp;interface_tags</samp>](## "generate_cv_tags.interface_tags") | List, items: Dictionary |  |  |  | List of interface tags that should be generated. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "generate_cv_tags.interface_tags.[].name") | String | Required, Unique |  |  | Tag name to be assigned to generated tags. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;data_path</samp>](## "generate_cv_tags.interface_tags.[].data_path") | String |  |  |  | Structured config field/key path to be used to find the value for the tag. Dot notation is supported to reference values inside dictionaries.<br>For Example: 'data_path: channel_group.id' would set the tag with the value of the channel id of the interface. If there is no channel id, the tag is not created.<br>`data_path` is ignored if `value` is set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "generate_cv_tags.interface_tags.[].value") | String |  |  |  | Value to be assigned to the tag. |
    | [<samp>&nbsp;&nbsp;device_tags</samp>](## "generate_cv_tags.device_tags") | List, items: Dictionary |  |  |  | List of device tags that should be generated. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "generate_cv_tags.device_tags.[].name") | String | Required |  |  | Tag name to be assigned to generated tags. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;data_path</samp>](## "generate_cv_tags.device_tags.[].data_path") | String |  |  |  | Structured config field/key path to be used to find the value for the tag. Dot notation is supported to reference values inside dictionaries.<br>For Example: 'data_path: router_bfd.multihop.interval' would set the tag with the value of the interval for multihop bfd. If this value is not specified in the structured config, the tag is not created.<br>`data_path` is ignored if `value` is set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "generate_cv_tags.device_tags.[].value") | String |  |  |  | Value to be assigned to the tag. |
    | [<samp>custom_node_type_keys</samp>](## "custom_node_type_keys") | List, items: Dictionary |  |  |  | Define Custom Node Type Keys, to specify the properties of each node type in the fabric.<br>This allows for complete customization of the fabric layout and functionality.<br>`custom_node_type_keys` should be defined in top level group_var for the fabric.<br>These values will be combined with the defaults; custom node type keys named the same as a<br>default node_type_key will replace the default. |
    | [<samp>&nbsp;&nbsp;-&nbsp;key</samp>](## "custom_node_type_keys.[].key") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;cv_tags_topology_type</samp>](## "custom_node_type_keys.[].cv_tags_topology_type") | String |  |  | Valid Values:<br>- <code>leaf</code><br>- <code>spine</code><br>- <code>core</code><br>- <code>edge</code> | PREVIEW: This key is currently not supported<br>Type that CloudVision should use when generating the Topology. |
    | [<samp>node_type_keys</samp>](## "node_type_keys") | List, items: Dictionary |  |  |  | Define Node Type Keys, to specify the properties of each node type in the fabric.<br>This allows for complete customization of the fabric layout and functionality.<br>`node_type_keys` should be defined in top level group_var for the fabric.<br><br>The default values will be overridden if this key is defined.<br>If you need to change all the existing `node_type_keys`, it is recommended to copy the defaults and modify them.<br>If you need to add custom `node_type_keys`, create them under `custom_node_type_keys` - if named identically to default `node_type_keys` entries,<br>custom entries will replace the equivalent default entry. |
    | [<samp>&nbsp;&nbsp;-&nbsp;key</samp>](## "node_type_keys.[].key") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;cv_tags_topology_type</samp>](## "node_type_keys.[].cv_tags_topology_type") | String |  |  | Valid Values:<br>- <code>leaf</code><br>- <code>spine</code><br>- <code>core</code><br>- <code>edge</code> | PREVIEW: This key is currently not supported<br>Type that CloudVision should use when generating the Topology. |

=== "YAML"

    ```yaml
    # PREVIEW: This key is currently not supported
    # Device type that CloudVision should use when generating the Topology. Defaults to the setting under node_type_keys.
    cv_tags_topology_type: <str; "leaf" | "spine" | "core" | "edge">

    # PREVIEW: This key is currently not supported
    # Generate CloudVision Tags based on AVD data.
    generate_cv_tags:

      # Enable the generation of CloudVision Topology Tags (hints).
      topology_hints: <bool; default=False>

      # List of interface tags that should be generated.
      interface_tags:

          # Tag name to be assigned to generated tags.
        - name: <str; required; unique>

          # Structured config field/key path to be used to find the value for the tag. Dot notation is supported to reference values inside dictionaries.
          # For Example: 'data_path: channel_group.id' would set the tag with the value of the channel id of the interface. If there is no channel id, the tag is not created.
          # `data_path` is ignored if `value` is set.
          data_path: <str>

          # Value to be assigned to the tag.
          value: <str>

      # List of device tags that should be generated.
      device_tags:

          # Tag name to be assigned to generated tags.
        - name: <str; required>

          # Structured config field/key path to be used to find the value for the tag. Dot notation is supported to reference values inside dictionaries.
          # For Example: 'data_path: router_bfd.multihop.interval' would set the tag with the value of the interval for multihop bfd. If this value is not specified in the structured config, the tag is not created.
          # `data_path` is ignored if `value` is set.
          data_path: <str>

          # Value to be assigned to the tag.
          value: <str>

    # Define Custom Node Type Keys, to specify the properties of each node type in the fabric.
    # This allows for complete customization of the fabric layout and functionality.
    # `custom_node_type_keys` should be defined in top level group_var for the fabric.
    # These values will be combined with the defaults; custom node type keys named the same as a
    # default node_type_key will replace the default.
    custom_node_type_keys:
      - key: <str; required; unique>

        # PREVIEW: This key is currently not supported
        # Type that CloudVision should use when generating the Topology.
        cv_tags_topology_type: <str; "leaf" | "spine" | "core" | "edge">

    # Define Node Type Keys, to specify the properties of each node type in the fabric.
    # This allows for complete customization of the fabric layout and functionality.
    # `node_type_keys` should be defined in top level group_var for the fabric.
    #
    # The default values will be overridden if this key is defined.
    # If you need to change all the existing `node_type_keys`, it is recommended to copy the defaults and modify them.
    # If you need to add custom `node_type_keys`, create them under `custom_node_type_keys` - if named identically to default `node_type_keys` entries,
    # custom entries will replace the equivalent default entry.
    node_type_keys:
      - key: <str; required; unique>

        # PREVIEW: This key is currently not supported
        # Type that CloudVision should use when generating the Topology.
        cv_tags_topology_type: <str; "leaf" | "spine" | "core" | "edge">
    ```
