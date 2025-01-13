<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>fabric_sflow</samp>](## "fabric_sflow") | Dictionary |  |  |  | Default enabling of sFlow for various interface types across the fabric.<br>sFlow can also be enabled/disabled under each of the specific data models.<br>For general sFlow settings see `sflow_settings`. |
    | [<samp>&nbsp;&nbsp;uplinks</samp>](## "fabric_sflow.uplinks") | Boolean |  |  |  | Enable sFlow on all fabric uplinks. |
    | [<samp>&nbsp;&nbsp;downlinks</samp>](## "fabric_sflow.downlinks") | Boolean |  |  |  | Enable sFlow on all fabric downlinks. |
    | [<samp>&nbsp;&nbsp;endpoints</samp>](## "fabric_sflow.endpoints") | Boolean |  |  |  | Enable sFlow on all endpoints ports. |
    | [<samp>&nbsp;&nbsp;l3_edge</samp>](## "fabric_sflow.l3_edge") | Boolean |  |  |  | Enable sFlow on all p2p_links defined under l3_edge. |
    | [<samp>&nbsp;&nbsp;core_interfaces</samp>](## "fabric_sflow.core_interfaces") | Boolean |  |  |  | Enable sFlow on all p2p_links defined under core_interfaces. |
    | [<samp>&nbsp;&nbsp;mlag_interfaces</samp>](## "fabric_sflow.mlag_interfaces") | Boolean |  |  |  | Enable sFlow on all MLAG peer interfaces. |
    | [<samp>&nbsp;&nbsp;l3_interfaces</samp>](## "fabric_sflow.l3_interfaces") | Boolean |  |  |  | Enable sFlow on all l3 interfaces. |
    | [<samp>sflow_settings</samp>](## "sflow_settings") | Dictionary |  |  |  | sFlow settings.<br>The sFlow process will only be configured if any interface is enabled for sFlow.<br>For default enabling of sFlow for various interface types across the fabric see `fabric_sflow`. |
    | [<samp>&nbsp;&nbsp;polling_interval</samp>](## "sflow_settings.polling_interval") | Integer |  |  |  | Interval in seconds for sending counter data to the sFlow collector. |
    | [<samp>&nbsp;&nbsp;sample</samp>](## "sflow_settings.sample") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "sflow_settings.sample.rate") | Integer |  |  | Min: 1<br>Max: 4294967295 | Packet sampling rate that defines the average number of ingress packets that pass through an interface for every packet that is sampled.<br>A rate of 16384 corresponds to an average sample of one per 16384 packets. |
    | [<samp>&nbsp;&nbsp;destinations</samp>](## "sflow_settings.destinations") | List, items: Dictionary | Required |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;destination</samp>](## "sflow_settings.destinations.[].destination") | String | Required |  |  | sFlow destination name or IP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "sflow_settings.destinations.[].port") | Integer |  |  | Min: 1<br>Max: 65535 | UDP Port number. The default port number for sFlow is 6343. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "sflow_settings.destinations.[].vrf") | String |  |  |  | If not set, the VRF is automatically picked up from the global setting `default_mgmt_method`.<br>The value of `vrf` will be interpreted according to these rules:<br>- `use_mgmt_interface_vrf` will configure the sFlow destination under the VRF set with `mgmt_interface_vrf` and set the `mgmt_interface` as sFlow source-interface.<br>  An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.<br>- `use_inband_mgmt_vrf` will configure the sFlow destination under the VRF set with `inband_mgmt_vrf` and set the `inband_mgmt_interface` as sFlow source-interface.<br>  An error will be raised if inband management is not configured for the device.<br>- Any other string will be used directly as the VRF name. Remember to set the `sflow_settings.vrfs[].source_interface` if needed. |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "sflow_settings.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "sflow_settings.vrfs.[].name") | String | Required, Unique |  |  | VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "sflow_settings.vrfs.[].source_interface") | String |  |  |  | Source interface to use for sFlow destinations in this VRF.<br>If set for the VRFs defined by `mgmt_interface_vrf` or `inband_mgmt_vrf`, this setting will take precedence. |

=== "YAML"

    ```yaml
    # Default enabling of sFlow for various interface types across the fabric.
    # sFlow can also be enabled/disabled under each of the specific data models.
    # For general sFlow settings see `sflow_settings`.
    fabric_sflow:

      # Enable sFlow on all fabric uplinks.
      uplinks: <bool>

      # Enable sFlow on all fabric downlinks.
      downlinks: <bool>

      # Enable sFlow on all endpoints ports.
      endpoints: <bool>

      # Enable sFlow on all p2p_links defined under l3_edge.
      l3_edge: <bool>

      # Enable sFlow on all p2p_links defined under core_interfaces.
      core_interfaces: <bool>

      # Enable sFlow on all MLAG peer interfaces.
      mlag_interfaces: <bool>

      # Enable sFlow on all l3 interfaces.
      l3_interfaces: <bool>

    # sFlow settings.
    # The sFlow process will only be configured if any interface is enabled for sFlow.
    # For default enabling of sFlow for various interface types across the fabric see `fabric_sflow`.
    sflow_settings:

      # Interval in seconds for sending counter data to the sFlow collector.
      polling_interval: <int>
      sample:

        # Packet sampling rate that defines the average number of ingress packets that pass through an interface for every packet that is sampled.
        # A rate of 16384 corresponds to an average sample of one per 16384 packets.
        rate: <int; 1-4294967295>
      destinations: # >=1 items; required

          # sFlow destination name or IP address.
        - destination: <str; required>

          # UDP Port number. The default port number for sFlow is 6343.
          port: <int; 1-65535>

          # If not set, the VRF is automatically picked up from the global setting `default_mgmt_method`.
          # The value of `vrf` will be interpreted according to these rules:
          # - `use_mgmt_interface_vrf` will configure the sFlow destination under the VRF set with `mgmt_interface_vrf` and set the `mgmt_interface` as sFlow source-interface.
          #   An error will be raised if `mgmt_ip` or `ipv6_mgmt_ip` are not configured for the device.
          # - `use_inband_mgmt_vrf` will configure the sFlow destination under the VRF set with `inband_mgmt_vrf` and set the `inband_mgmt_interface` as sFlow source-interface.
          #   An error will be raised if inband management is not configured for the device.
          # - Any other string will be used directly as the VRF name. Remember to set the `sflow_settings.vrfs[].source_interface` if needed.
          vrf: <str>
      vrfs:

          # VRF name.
        - name: <str; required; unique>

          # Source interface to use for sFlow destinations in this VRF.
          # If set for the VRFs defined by `mgmt_interface_vrf` or `inband_mgmt_vrf`, this setting will take precedence.
          source_interface: <str>
    ```
