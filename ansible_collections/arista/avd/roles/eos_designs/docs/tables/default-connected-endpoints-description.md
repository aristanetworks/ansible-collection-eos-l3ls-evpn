<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>default_connected_endpoints_description</samp>](## "default_connected_endpoints_description") | String |  | `{endpoint_type!u}_{endpoint}{endpoint_port?<_}` |  | Default description or description template to be used on all ports to connected endpoints.<br>This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.<br>The available template fields are:<br>  - `endpoint_type`: The `type` from `connected_endpoints_keys` like `server`, `router` etc.<br>  - `endpoint`: The name of the connected endpoint<br>  - `endpoint_port`: The value from `endpoint_ports` for this switch port if set.<br>  - `port_channel_id`: The port-channel number for the switch.<br><br>By default the description is templated from the type, name and port of the endpoint if set. |
    | [<samp>default_connected_endpoints_port_channel_description</samp>](## "default_connected_endpoints_port_channel_description") | String |  | `{endpoint_type!u}_{endpoint}{endpoint_port_channel?<_}` |  | Default description or description template to be used on all port-channels to connected endpoints.<br>This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.<br>The available template fields are:<br>  - `endpoint_type`: The `type` from `connected_endpoints_keys` like `server`, `router` etc.<br>  - `endpoint`: The name of the connected endpoint<br>  - `endpoint_port_channel`: The value of `endpoint_port_channel` if set.<br>  - `port_channel_id`: The port-channel number for the switch.<br>  - `adapter_description`: The adapter's description if set.<br>  - `adapter_description_or_endpoint`: Helper alias of the adapter_description or endpoint.<br><br>By default the description is templated from the type, name and port-channel name of the endpoint if set. |

=== "YAML"

    ```yaml
    # Default description or description template to be used on all ports to connected endpoints.
    # This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
    # The available template fields are:
    #   - `endpoint_type`: The `type` from `connected_endpoints_keys` like `server`, `router` etc.
    #   - `endpoint`: The name of the connected endpoint
    #   - `endpoint_port`: The value from `endpoint_ports` for this switch port if set.
    #   - `port_channel_id`: The port-channel number for the switch.
    #
    # By default the description is templated from the type, name and port of the endpoint if set.
    default_connected_endpoints_description: <str; default="{endpoint_type!u}_{endpoint}{endpoint_port?<_}">

    # Default description or description template to be used on all port-channels to connected endpoints.
    # This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
    # The available template fields are:
    #   - `endpoint_type`: The `type` from `connected_endpoints_keys` like `server`, `router` etc.
    #   - `endpoint`: The name of the connected endpoint
    #   - `endpoint_port_channel`: The value of `endpoint_port_channel` if set.
    #   - `port_channel_id`: The port-channel number for the switch.
    #   - `adapter_description`: The adapter's description if set.
    #   - `adapter_description_or_endpoint`: Helper alias of the adapter_description or endpoint.
    #
    # By default the description is templated from the type, name and port-channel name of the endpoint if set.
    default_connected_endpoints_port_channel_description: <str; default="{endpoint_type!u}_{endpoint}{endpoint_port_channel?<_}">
    ```
