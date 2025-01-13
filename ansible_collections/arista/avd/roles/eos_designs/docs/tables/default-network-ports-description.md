<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>default_network_ports_description</samp>](## "default_network_ports_description") | String |  | `{endpoint?}` |  | Default description or description template to be used on all ports defined under `network_ports`.<br>This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.<br>The available template fields are:<br>  - `endpoint_type`: Always set to `network_port`.<br>  - `endpoint`: The value of the `endpoint` key if set.<br>  - `port_channel_id`: The port-channel number for the switch.<br><br>By default the description is templated from the `endpoint` key if set. |
    | [<samp>default_network_ports_port_channel_description</samp>](## "default_network_ports_port_channel_description") | String |  | `{endpoint?}{endpoint_port_channel?<_}` |  | Default description or description template to be used on all port-channels defined under `network_ports`.<br>This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.<br>The available template fields are:<br>  - `endpoint_type`: Always set to `network_port`.<br>  - `endpoint`: The value of the `endpoint` key if set.<br>  - `endpoint_port_channel`: The value of `endpoint_port_channel` if set.<br>  - `port_channel_id`: The port-channel number for the switch.<br>  - `adapter_description`: The adapter's description if set.<br>  - `adapter_description_or_endpoint`: Helper alias of the adapter_description or endpoint.<br><br>By default the description is templated from the `endpoint` key if set. |

=== "YAML"

    ```yaml
    # Default description or description template to be used on all ports defined under `network_ports`.
    # This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
    # The available template fields are:
    #   - `endpoint_type`: Always set to `network_port`.
    #   - `endpoint`: The value of the `endpoint` key if set.
    #   - `port_channel_id`: The port-channel number for the switch.
    #
    # By default the description is templated from the `endpoint` key if set.
    default_network_ports_description: <str; default="{endpoint?}">

    # Default description or description template to be used on all port-channels defined under `network_ports`.
    # This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
    # The available template fields are:
    #   - `endpoint_type`: Always set to `network_port`.
    #   - `endpoint`: The value of the `endpoint` key if set.
    #   - `endpoint_port_channel`: The value of `endpoint_port_channel` if set.
    #   - `port_channel_id`: The port-channel number for the switch.
    #   - `adapter_description`: The adapter's description if set.
    #   - `adapter_description_or_endpoint`: Helper alias of the adapter_description or endpoint.
    #
    # By default the description is templated from the `endpoint` key if set.
    default_network_ports_port_channel_description: <str; default="{endpoint?}{endpoint_port_channel?<_}">
    ```
