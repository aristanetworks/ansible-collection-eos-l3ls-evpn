<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>fabric_flow_tracking</samp>](## "fabric_flow_tracking") | Dictionary |  |  |  | Default enabling of flow-tracking(IPFIX) for various interface types across the fabric.<br>Flow Tracking can also be enabled/disabled under each of the specific data models.<br>For general flow-tracking settings see `flow_tracking_settings`. |
    | [<samp>&nbsp;&nbsp;uplinks</samp>](## "fabric_flow_tracking.uplinks") | Dictionary |  |  |  | Enable flow-tracking on all fabric uplinks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "fabric_flow_tracking.uplinks.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "fabric_flow_tracking.uplinks.name") | String |  | `FLOW-TRACKER` |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;downlinks</samp>](## "fabric_flow_tracking.downlinks") | Dictionary |  |  |  | Enable flow-tracking on all fabric downlinks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "fabric_flow_tracking.downlinks.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "fabric_flow_tracking.downlinks.name") | String |  | `FLOW-TRACKER` |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;endpoints</samp>](## "fabric_flow_tracking.endpoints") | Dictionary |  |  |  | Enable flow-tracking on all endpoints ports. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "fabric_flow_tracking.endpoints.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "fabric_flow_tracking.endpoints.name") | String |  | `FLOW-TRACKER` |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;l3_edge</samp>](## "fabric_flow_tracking.l3_edge") | Dictionary |  |  |  | Enable flow-tracking on all p2p_links defined under l3_edge. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "fabric_flow_tracking.l3_edge.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "fabric_flow_tracking.l3_edge.name") | String |  | `FLOW-TRACKER` |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;core_interfaces</samp>](## "fabric_flow_tracking.core_interfaces") | Dictionary |  |  |  | Enable flow-tracking on all p2p_links defined under core_interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "fabric_flow_tracking.core_interfaces.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "fabric_flow_tracking.core_interfaces.name") | String |  | `FLOW-TRACKER` |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;mlag_interfaces</samp>](## "fabric_flow_tracking.mlag_interfaces") | Dictionary |  |  |  | Enable flow-tracking on all MLAG peer interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "fabric_flow_tracking.mlag_interfaces.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "fabric_flow_tracking.mlag_interfaces.name") | String |  | `FLOW-TRACKER` |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;l3_interfaces</samp>](## "fabric_flow_tracking.l3_interfaces") | Dictionary |  |  |  | Enable flow-tracking on all node.l3_interfaces and network-services tenants.vrfs.l3_interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "fabric_flow_tracking.l3_interfaces.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "fabric_flow_tracking.l3_interfaces.name") | String |  | `FLOW-TRACKER` |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;dps_interfaces</samp>](## "fabric_flow_tracking.dps_interfaces") | Dictionary |  |  |  | Enable flow-tracking on all dps_interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "fabric_flow_tracking.dps_interfaces.enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "fabric_flow_tracking.dps_interfaces.name") | String |  | `FLOW-TRACKER` |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;direct_wan_ha_links</samp>](## "fabric_flow_tracking.direct_wan_ha_links") | Dictionary |  |  |  | Enable flow-tracking on all direct WAN HA links. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "fabric_flow_tracking.direct_wan_ha_links.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "fabric_flow_tracking.direct_wan_ha_links.name") | String |  | `FLOW-TRACKER` |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>flow_tracking_settings</samp>](## "flow_tracking_settings") | Dictionary |  |  |  | Define the flow tracking parameters for this topology. |
    | [<samp>&nbsp;&nbsp;sampled</samp>](## "flow_tracking_settings.sampled") | Dictionary |  |  |  | The options relevant only for flow tracker type sampled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation</samp>](## "flow_tracking_settings.sampled.encapsulation") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_ipv6</samp>](## "flow_tracking_settings.sampled.encapsulation.ipv4_ipv6") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp>](## "flow_tracking_settings.sampled.encapsulation.mpls") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sample</samp>](## "flow_tracking_settings.sampled.sample") | Integer |  | `10000` | Min: 1<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hardware_offload</samp>](## "flow_tracking_settings.sampled.hardware_offload") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "flow_tracking_settings.sampled.hardware_offload.ipv4") | Boolean |  |  |  | Configure hardware offload for IPv4 traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "flow_tracking_settings.sampled.hardware_offload.ipv6") | Boolean |  |  |  | Configure hardware offload for IPv6 traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold_minimum</samp>](## "flow_tracking_settings.sampled.hardware_offload.threshold_minimum") | Integer |  |  | Min: 1<br>Max: 4294967295 | Minimum number of samples. |
    | [<samp>&nbsp;&nbsp;hardware</samp>](## "flow_tracking_settings.hardware") | Dictionary |  |  |  | The options relevant only for flow tracker type hardware. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;record</samp>](## "flow_tracking_settings.hardware.record") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;format_ipfix_standard_timestamps_counters</samp>](## "flow_tracking_settings.hardware.record.format_ipfix_standard_timestamps_counters") | Boolean |  |  |  | Enable software export of IPFIX data records. |
    | [<samp>&nbsp;&nbsp;trackers</samp>](## "flow_tracking_settings.trackers") | List, items: Dictionary |  | See (+) on YAML tab |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "flow_tracking_settings.trackers.[].name") | String | Required, Unique |  |  | Tracker Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sampled</samp>](## "flow_tracking_settings.trackers.[].sampled") | Dictionary |  |  |  | The options relevant only for flow tracker type sampled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;table_size</samp>](## "flow_tracking_settings.trackers.[].sampled.table_size") | Integer |  |  | Min: 1<br>Max: 614400 | Maximum number of entries in flow table.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;record_export</samp>](## "flow_tracking_settings.trackers.[].sampled.record_export") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp>](## "flow_tracking_settings.trackers.[].sampled.record_export.mpls") | Boolean |  |  |  | Export MPLS forwarding information. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;record_export</samp>](## "flow_tracking_settings.trackers.[].record_export") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_inactive_timeout</samp>](## "flow_tracking_settings.trackers.[].record_export.on_inactive_timeout") | Integer |  |  | Min: 3000<br>Max: 900000 | Flow record inactive export timeout in milliseconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_interval</samp>](## "flow_tracking_settings.trackers.[].record_export.on_interval") | Integer |  |  | Min: 1000<br>Max: 36000000 | Flow record export interval in milliseconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exporters</samp>](## "flow_tracking_settings.trackers.[].exporters") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "flow_tracking_settings.trackers.[].exporters.[].name") | String | Required, Unique |  |  | Exporter Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;collector</samp>](## "flow_tracking_settings.trackers.[].exporters.[].collector") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host</samp>](## "flow_tracking_settings.trackers.[].exporters.[].collector.host") | String |  |  |  | Collector IPv4 address or IPv6 address or fully qualified domain name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "flow_tracking_settings.trackers.[].exporters.[].collector.port") | Integer |  |  | Min: 1<br>Max: 65535 | Collector Port Number |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;format</samp>](## "flow_tracking_settings.trackers.[].exporters.[].format") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipfix_version</samp>](## "flow_tracking_settings.trackers.[].exporters.[].format.ipfix_version") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "flow_tracking_settings.trackers.[].exporters.[].local_interface") | String |  |  |  | Local Source Interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;template_interval</samp>](## "flow_tracking_settings.trackers.[].exporters.[].template_interval") | Integer |  |  | Min: 5000<br>Max: 3600000 | Template interval in milliseconds |

=== "YAML"

    ```yaml
    # Default enabling of flow-tracking(IPFIX) for various interface types across the fabric.
    # Flow Tracking can also be enabled/disabled under each of the specific data models.
    # For general flow-tracking settings see `flow_tracking_settings`.
    fabric_flow_tracking:

      # Enable flow-tracking on all fabric uplinks.
      uplinks:
        enabled: <bool; default=False>

        # Flow tracker name as defined in flow_tracking_settings.
        name: <str; default="FLOW-TRACKER">

      # Enable flow-tracking on all fabric downlinks.
      downlinks:
        enabled: <bool; default=False>

        # Flow tracker name as defined in flow_tracking_settings.
        name: <str; default="FLOW-TRACKER">

      # Enable flow-tracking on all endpoints ports.
      endpoints:
        enabled: <bool; default=False>

        # Flow tracker name as defined in flow_tracking_settings.
        name: <str; default="FLOW-TRACKER">

      # Enable flow-tracking on all p2p_links defined under l3_edge.
      l3_edge:
        enabled: <bool; default=False>

        # Flow tracker name as defined in flow_tracking_settings.
        name: <str; default="FLOW-TRACKER">

      # Enable flow-tracking on all p2p_links defined under core_interfaces.
      core_interfaces:
        enabled: <bool; default=False>

        # Flow tracker name as defined in flow_tracking_settings.
        name: <str; default="FLOW-TRACKER">

      # Enable flow-tracking on all MLAG peer interfaces.
      mlag_interfaces:
        enabled: <bool; default=False>

        # Flow tracker name as defined in flow_tracking_settings.
        name: <str; default="FLOW-TRACKER">

      # Enable flow-tracking on all node.l3_interfaces and network-services tenants.vrfs.l3_interfaces.
      l3_interfaces:
        enabled: <bool; default=False>

        # Flow tracker name as defined in flow_tracking_settings.
        name: <str; default="FLOW-TRACKER">

      # Enable flow-tracking on all dps_interfaces.
      dps_interfaces:
        enabled: <bool; default=True>

        # Flow tracker name as defined in flow_tracking_settings.
        name: <str; default="FLOW-TRACKER">

      # Enable flow-tracking on all direct WAN HA links.
      direct_wan_ha_links:
        enabled: <bool; default=False>

        # Flow tracker name as defined in flow_tracking_settings.
        name: <str; default="FLOW-TRACKER">

    # Define the flow tracking parameters for this topology.
    flow_tracking_settings:

      # The options relevant only for flow tracker type sampled.
      sampled:
        encapsulation:
          ipv4_ipv6: <bool>
          mpls: <bool>
        sample: <int; 1-4294967295; default=10000>
        hardware_offload:

          # Configure hardware offload for IPv4 traffic.
          ipv4: <bool>

          # Configure hardware offload for IPv6 traffic.
          ipv6: <bool>

          # Minimum number of samples.
          threshold_minimum: <int; 1-4294967295>

      # The options relevant only for flow tracker type hardware.
      hardware:
        record:

          # Enable software export of IPFIX data records.
          format_ipfix_standard_timestamps_counters: <bool>
      trackers: # (1)!

          # Tracker Name
        - name: <str; required; unique>

          # The options relevant only for flow tracker type sampled.
          sampled:

            # Maximum number of entries in flow table.
            table_size: <int; 1-614400>
            record_export:

              # Export MPLS forwarding information.
              mpls: <bool>
          record_export:

            # Flow record inactive export timeout in milliseconds
            on_inactive_timeout: <int; 3000-900000>

            # Flow record export interval in milliseconds
            on_interval: <int; 1000-36000000>
          exporters:

              # Exporter Name
            - name: <str; required; unique>
              collector:

                # Collector IPv4 address or IPv6 address or fully qualified domain name
                host: <str>

                # Collector Port Number
                port: <int; 1-65535>
              format:
                ipfix_version: <int>

              # Local Source Interface
              local_interface: <str>

              # Template interval in milliseconds
              template_interval: <int; 5000-3600000>
    ```

    1. Default Value

        ```yaml
        trackers:
        - exporters:
          - collector:
              host: 127.0.0.1
            local_interface: Loopback0
            name: CV-TELEMETRY
            template_interval: 3600000
          name: FLOW-TRACKER
          record_export:
            on_inactive_timeout: 70000
            on_interval: 300000
        ```
