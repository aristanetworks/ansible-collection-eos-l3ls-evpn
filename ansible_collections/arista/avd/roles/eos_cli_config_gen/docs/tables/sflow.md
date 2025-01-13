<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>sflow</samp>](## "sflow") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;sample</samp>](## "sflow.sample") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;sample_input_subinterface</samp>](## "sflow.sample_input_subinterface") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;sample_output_subinterface</samp>](## "sflow.sample_output_subinterface") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;dangerous</samp>](## "sflow.dangerous") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;polling_interval</samp>](## "sflow.polling_interval") | Integer |  |  |  | Polling interval in seconds. |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "sflow.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "sflow.vrfs.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destinations</samp>](## "sflow.vrfs.[].destinations") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;destination</samp>](## "sflow.vrfs.[].destinations.[].destination") | String | Required, Unique |  |  | Sflow Destination IP Address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "sflow.vrfs.[].destinations.[].port") | Integer |  |  |  | Port Number |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "sflow.vrfs.[].source") | String |  |  |  | Source IP Address.<br>"source" and "source_interface" are mutually exclusive. If both are defined, "source_interface" takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "sflow.vrfs.[].source_interface") | String |  |  |  | Source Interface. |
    | [<samp>&nbsp;&nbsp;destinations</samp>](## "sflow.destinations") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;destination</samp>](## "sflow.destinations.[].destination") | String | Required, Unique |  |  | Sflow Destination IP Address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "sflow.destinations.[].port") | Integer |  |  |  | Port Number. |
    | [<samp>&nbsp;&nbsp;source</samp>](## "sflow.source") | String |  |  |  | Source IP Address.<br>"source" and "source_interface" are mutually exclusive. If both are defined, "source_interface" takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;source_interface</samp>](## "sflow.source_interface") | String |  |  |  | Source Interface. |
    | [<samp>&nbsp;&nbsp;extensions</samp>](## "sflow.extensions") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "sflow.extensions.[].name") | String | Required, Unique |  |  | Extension Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "sflow.extensions.[].enabled") | Boolean | Required |  |  | Enable or Disable Extension. |
    | [<samp>&nbsp;&nbsp;interface</samp>](## "sflow.interface") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;disable</samp>](## "sflow.interface.disable") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "sflow.interface.disable.default") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;egress</samp>](## "sflow.interface.egress") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_default</samp>](## "sflow.interface.egress.enable_default") | Boolean |  |  |  | Enable egress sFlow by default.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unmodified</samp>](## "sflow.interface.egress.unmodified") | Boolean |  |  |  | Enable egress sFlow unmodified.<br>Platform dependent feature.<br> |
    | [<samp>&nbsp;&nbsp;run</samp>](## "sflow.run") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;hardware_acceleration</samp>](## "sflow.hardware_acceleration") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "sflow.hardware_acceleration.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sample</samp>](## "sflow.hardware_acceleration.sample") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;modules</samp>](## "sflow.hardware_acceleration.modules") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "sflow.hardware_acceleration.modules.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "sflow.hardware_acceleration.modules.[].enabled") | Boolean |  | `True` |  |  |

=== "YAML"

    ```yaml
    sflow:
      sample: <int>
      sample_input_subinterface: <bool>
      sample_output_subinterface: <bool>
      dangerous: <bool>

      # Polling interval in seconds.
      polling_interval: <int>
      vrfs:
        - name: <str; required; unique>
          destinations:

              # Sflow Destination IP Address.
            - destination: <str; required; unique>

              # Port Number
              port: <int>

          # Source IP Address.
          # "source" and "source_interface" are mutually exclusive. If both are defined, "source_interface" takes precedence.
          source: <str>

          # Source Interface.
          source_interface: <str>
      destinations:

          # Sflow Destination IP Address.
        - destination: <str; required; unique>

          # Port Number.
          port: <int>

      # Source IP Address.
      # "source" and "source_interface" are mutually exclusive. If both are defined, "source_interface" takes precedence.
      source: <str>

      # Source Interface.
      source_interface: <str>
      extensions:

          # Extension Name.
        - name: <str; required; unique>

          # Enable or Disable Extension.
          enabled: <bool; required>
      interface:
        disable:
          default: <bool>
        egress:

          # Enable egress sFlow by default.
          enable_default: <bool>

          # Enable egress sFlow unmodified.
          # Platform dependent feature.
          unmodified: <bool>
      run: <bool>
      hardware_acceleration:
        enabled: <bool>
        sample: <int>
        modules:
          - name: <str; required; unique>
            enabled: <bool; default=True>
    ```
