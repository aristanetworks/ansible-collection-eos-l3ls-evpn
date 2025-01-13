<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>flow_tracking</samp>](## "flow_tracking") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;sampled</samp>](## "flow_tracking.sampled") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation</samp>](## "flow_tracking.sampled.encapsulation") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_ipv6</samp>](## "flow_tracking.sampled.encapsulation.ipv4_ipv6") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp>](## "flow_tracking.sampled.encapsulation.mpls") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sample</samp>](## "flow_tracking.sampled.sample") | Integer |  |  | Min: 1<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;hardware_offload</samp>](## "flow_tracking.sampled.hardware_offload") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "flow_tracking.sampled.hardware_offload.ipv4") | Boolean |  |  |  | Configure hardware offload for IPv4 traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "flow_tracking.sampled.hardware_offload.ipv6") | Boolean |  |  |  | Configure hardware offload for IPv6 traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold_minimum</samp>](## "flow_tracking.sampled.hardware_offload.threshold_minimum") | Integer |  |  | Min: 1<br>Max: 4294967295 | Minimum number of samples. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trackers</samp>](## "flow_tracking.sampled.trackers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;table_size</samp>](## "flow_tracking.sampled.trackers.[].table_size") | Integer |  |  | Min: 1<br>Max: 614400 | Maximum number of entries in flow table.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;record_export</samp>](## "flow_tracking.sampled.trackers.[].record_export") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp>](## "flow_tracking.sampled.trackers.[].record_export.mpls") | Boolean |  |  |  | Export MPLS forwarding information. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_inactive_timeout</samp>](## "flow_tracking.sampled.trackers.[].record_export.on_inactive_timeout") | Integer |  |  | Min: 3000<br>Max: 900000 | Flow record inactive export timeout in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_interval</samp>](## "flow_tracking.sampled.trackers.[].record_export.on_interval") | Integer |  |  | Min: 1000<br>Max: 36000000 | Flow record export interval in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "flow_tracking.sampled.trackers.[].name") | String | Required, Unique |  |  | Tracker Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exporters</samp>](## "flow_tracking.sampled.trackers.[].exporters") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "flow_tracking.sampled.trackers.[].exporters.[].name") | String | Required, Unique |  |  | Exporter Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;collector</samp>](## "flow_tracking.sampled.trackers.[].exporters.[].collector") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host</samp>](## "flow_tracking.sampled.trackers.[].exporters.[].collector.host") | String |  |  |  | Collector IPv4 address or IPv6 address or fully qualified domain name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "flow_tracking.sampled.trackers.[].exporters.[].collector.port") | Integer |  |  | Min: 1<br>Max: 65535 | Collector Port Number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;format</samp>](## "flow_tracking.sampled.trackers.[].exporters.[].format") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipfix_version</samp>](## "flow_tracking.sampled.trackers.[].exporters.[].format.ipfix_version") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "flow_tracking.sampled.trackers.[].exporters.[].local_interface") | String |  |  |  | Local Source Interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;template_interval</samp>](## "flow_tracking.sampled.trackers.[].exporters.[].template_interval") | Integer |  |  | Min: 5000<br>Max: 3600000 | Template interval in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "flow_tracking.sampled.shutdown") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;hardware</samp>](## "flow_tracking.hardware") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;record</samp>](## "flow_tracking.hardware.record") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;format_ipfix_standard_timestamps_counters</samp>](## "flow_tracking.hardware.record.format_ipfix_standard_timestamps_counters") | Boolean |  |  |  | Enable software export of IPFIX data records. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trackers</samp>](## "flow_tracking.hardware.trackers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "flow_tracking.hardware.trackers.[].name") | String | Required, Unique |  |  | Tracker Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;record_export</samp>](## "flow_tracking.hardware.trackers.[].record_export") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_inactive_timeout</samp>](## "flow_tracking.hardware.trackers.[].record_export.on_inactive_timeout") | Integer |  |  | Min: 3000<br>Max: 900000 | Flow record inactive export timeout in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_interval</samp>](## "flow_tracking.hardware.trackers.[].record_export.on_interval") | Integer |  |  | Min: 1000<br>Max: 36000000 | Flow record export interval in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exporters</samp>](## "flow_tracking.hardware.trackers.[].exporters") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "flow_tracking.hardware.trackers.[].exporters.[].name") | String | Required, Unique |  |  | Exporter Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;collector</samp>](## "flow_tracking.hardware.trackers.[].exporters.[].collector") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host</samp>](## "flow_tracking.hardware.trackers.[].exporters.[].collector.host") | String |  |  |  | Collector IPv4 address or IPv6 address or fully qualified domain name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "flow_tracking.hardware.trackers.[].exporters.[].collector.port") | Integer |  |  | Min: 1<br>Max: 65535 | Collector Port Number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;format</samp>](## "flow_tracking.hardware.trackers.[].exporters.[].format") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipfix_version</samp>](## "flow_tracking.hardware.trackers.[].exporters.[].format.ipfix_version") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "flow_tracking.hardware.trackers.[].exporters.[].local_interface") | String |  |  |  | Local Source Interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;template_interval</samp>](## "flow_tracking.hardware.trackers.[].exporters.[].template_interval") | Integer |  |  | Min: 5000<br>Max: 3600000 | Template interval in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "flow_tracking.hardware.shutdown") | Boolean |  | `False` |  |  |
    | [<samp>flow_trackings</samp>](## "flow_trackings") <span style="color:red">removed</span> | List, items: Dictionary |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version v5.0.0. Use <samp>flow_tracking</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;-&nbsp;type</samp>](## "flow_trackings.[].type") | String | Required, Unique |  | Valid Values:<br>- <code>sampled</code> | Flow Tracking Type - only 'sampled' supported for now. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sample</samp>](## "flow_trackings.[].sample") | Integer |  |  | Min: 1<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trackers</samp>](## "flow_trackings.[].trackers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "flow_trackings.[].trackers.[].name") | String | Required, Unique |  |  | Tracker Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;record_export</samp>](## "flow_trackings.[].trackers.[].record_export") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_inactive_timeout</samp>](## "flow_trackings.[].trackers.[].record_export.on_inactive_timeout") | Integer |  |  | Min: 3000<br>Max: 900000 | Flow record inactive export timeout in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_interval</samp>](## "flow_trackings.[].trackers.[].record_export.on_interval") | Integer |  |  | Min: 1000<br>Max: 36000000 | Flow record export interval in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp>](## "flow_trackings.[].trackers.[].record_export.mpls") | Boolean |  |  |  | Export MPLS forwarding information. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exporters</samp>](## "flow_trackings.[].trackers.[].exporters") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "flow_trackings.[].trackers.[].exporters.[].name") | String | Required, Unique |  |  | Exporter Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;collector</samp>](## "flow_trackings.[].trackers.[].exporters.[].collector") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host</samp>](## "flow_trackings.[].trackers.[].exporters.[].collector.host") | String |  |  |  | Collector IPv4 address or IPv6 address or fully qualified domain name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "flow_trackings.[].trackers.[].exporters.[].collector.port") | Integer |  |  | Min: 1<br>Max: 65535 | Collector Port Number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;format</samp>](## "flow_trackings.[].trackers.[].exporters.[].format") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipfix_version</samp>](## "flow_trackings.[].trackers.[].exporters.[].format.ipfix_version") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "flow_trackings.[].trackers.[].exporters.[].local_interface") | String |  |  |  | Local Source Interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;template_interval</samp>](## "flow_trackings.[].trackers.[].exporters.[].template_interval") | Integer |  |  | Min: 5000<br>Max: 3600000 | Template interval in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;table_size</samp>](## "flow_trackings.[].trackers.[].table_size") | Integer |  |  | Min: 1<br>Max: 614400 | Maximum number of entries in flow table.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "flow_trackings.[].shutdown") | Boolean |  | `False` |  |  |

=== "YAML"

    ```yaml
    flow_tracking:
      sampled:
        encapsulation:
          ipv4_ipv6: <bool>
          mpls: <bool>
        sample: <int; 1-4294967295>
        hardware_offload:

          # Configure hardware offload for IPv4 traffic.
          ipv4: <bool>

          # Configure hardware offload for IPv6 traffic.
          ipv6: <bool>

          # Minimum number of samples.
          threshold_minimum: <int; 1-4294967295>
        trackers:

            # Maximum number of entries in flow table.
          - table_size: <int; 1-614400>
            record_export:

              # Export MPLS forwarding information.
              mpls: <bool>

              # Flow record inactive export timeout in milliseconds.
              on_inactive_timeout: <int; 3000-900000>

              # Flow record export interval in milliseconds.
              on_interval: <int; 1000-36000000>

            # Tracker Name.
            name: <str; required; unique>
            exporters:

                # Exporter Name.
              - name: <str; required; unique>
                collector:

                  # Collector IPv4 address or IPv6 address or fully qualified domain name.
                  host: <str>

                  # Collector Port Number.
                  port: <int; 1-65535>
                format:
                  ipfix_version: <int>

                # Local Source Interface.
                local_interface: <str>

                # Template interval in milliseconds.
                template_interval: <int; 5000-3600000>
        shutdown: <bool; default=False>
      hardware:
        record:

          # Enable software export of IPFIX data records.
          format_ipfix_standard_timestamps_counters: <bool>
        trackers:

            # Tracker Name.
          - name: <str; required; unique>
            record_export:

              # Flow record inactive export timeout in milliseconds.
              on_inactive_timeout: <int; 3000-900000>

              # Flow record export interval in milliseconds.
              on_interval: <int; 1000-36000000>
            exporters:

                # Exporter Name.
              - name: <str; required; unique>
                collector:

                  # Collector IPv4 address or IPv6 address or fully qualified domain name.
                  host: <str>

                  # Collector Port Number.
                  port: <int; 1-65535>
                format:
                  ipfix_version: <int>

                # Local Source Interface.
                local_interface: <str>

                # Template interval in milliseconds.
                template_interval: <int; 5000-3600000>
        shutdown: <bool; default=False>
    ```
