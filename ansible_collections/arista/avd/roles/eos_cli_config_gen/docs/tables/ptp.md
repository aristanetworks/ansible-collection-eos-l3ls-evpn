<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ptp</samp>](## "ptp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;mode</samp>](## "ptp.mode") | String |  |  | Valid Values:<br>- <code>boundary</code><br>- <code>disabled</code><br>- <code>e2etransparent</code><br>- <code>gptp</code><br>- <code>ordinarymaster</code><br>- <code>p2ptransparent</code> |  |
    | [<samp>&nbsp;&nbsp;profile</samp>](## "ptp.profile") | String |  |  | Valid Values:<br>- <code>g8275.1</code><br>- <code>g8275.2</code> |  |
    | [<samp>&nbsp;&nbsp;mode_one_step</samp>](## "ptp.mode_one_step") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;forward_unicast</samp>](## "ptp.forward_unicast") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;clock_identity</samp>](## "ptp.clock_identity") | String |  |  |  | The clock-id in xx:xx:xx:xx:xx:xx format. |
    | [<samp>&nbsp;&nbsp;source</samp>](## "ptp.source") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "ptp.source.ip") | String |  |  |  | Source IP. |
    | [<samp>&nbsp;&nbsp;priority1</samp>](## "ptp.priority1") | Integer |  |  | Min: 0<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;priority2</samp>](## "ptp.priority2") | Integer |  |  | Min: 0<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;ttl</samp>](## "ptp.ttl") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;domain</samp>](## "ptp.domain") | Integer |  |  | Min: 0<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;message_type</samp>](## "ptp.message_type") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;general</samp>](## "ptp.message_type.general") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "ptp.message_type.general.dscp") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;event</samp>](## "ptp.message_type.event") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "ptp.message_type.event.dscp") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;monitor</samp>](## "ptp.monitor") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ptp.monitor.enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "ptp.monitor.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "ptp.monitor.threshold.offset_from_master") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "ptp.monitor.threshold.mean_path_delay") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "ptp.monitor.threshold.drop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset_from_master</samp>](## "ptp.monitor.threshold.drop.offset_from_master") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mean_path_delay</samp>](## "ptp.monitor.threshold.drop.mean_path_delay") | Integer |  |  | Min: 0<br>Max: 1000000000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;missing_message</samp>](## "ptp.monitor.missing_message") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intervals</samp>](## "ptp.monitor.missing_message.intervals") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "ptp.monitor.missing_message.intervals.announce") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "ptp.monitor.missing_message.intervals.follow_up") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "ptp.monitor.missing_message.intervals.sync") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_ids</samp>](## "ptp.monitor.missing_message.sequence_ids") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ptp.monitor.missing_message.sequence_ids.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "ptp.monitor.missing_message.sequence_ids.announce") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_resp</samp>](## "ptp.monitor.missing_message.sequence_ids.delay_resp") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;follow_up</samp>](## "ptp.monitor.missing_message.sequence_ids.follow_up") | Integer |  |  | Min: 2<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync</samp>](## "ptp.monitor.missing_message.sequence_ids.sync") | Integer |  |  | Min: 2<br>Max: 255 |  |

=== "YAML"

    ```yaml
    ptp:
      mode: <str; "boundary" | "disabled" | "e2etransparent" | "gptp" | "ordinarymaster" | "p2ptransparent">
      profile: <str; "g8275.1" | "g8275.2">
      mode_one_step: <bool>
      forward_unicast: <bool>

      # The clock-id in xx:xx:xx:xx:xx:xx format.
      clock_identity: <str>
      source:

        # Source IP.
        ip: <str>
      priority1: <int; 0-255>
      priority2: <int; 0-255>
      ttl: <int; 1-255>
      domain: <int; 0-255>
      message_type:
        general:
          dscp: <int>
        event:
          dscp: <int>
      monitor:
        enabled: <bool; default=True>
        threshold:
          offset_from_master: <int; 0-1000000000>
          mean_path_delay: <int; 0-1000000000>
          drop:
            offset_from_master: <int; 0-1000000000>
            mean_path_delay: <int; 0-1000000000>
        missing_message:
          intervals:
            announce: <int; 2-255>
            follow_up: <int; 2-255>
            sync: <int; 2-255>
          sequence_ids:
            enabled: <bool>
            announce: <int; 2-255>
            delay_resp: <int; 2-255>
            follow_up: <int; 2-255>
            sync: <int; 2-255>
    ```
