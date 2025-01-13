<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>queue_monitor_length</samp>](## "queue_monitor_length") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "queue_monitor_length.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;default_thresholds</samp>](## "queue_monitor_length.default_thresholds") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;high</samp>](## "queue_monitor_length.default_thresholds.high") | Integer | Required |  |  | Default high threshold for Ethernet Interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;low</samp>](## "queue_monitor_length.default_thresholds.low") | Integer |  |  |  | Default low threshold for Ethernet Interfaces.<br>Low threshold support is platform dependent.<br> |
    | [<samp>&nbsp;&nbsp;log</samp>](## "queue_monitor_length.log") | Integer |  |  |  | Logging interval in seconds. |
    | [<samp>&nbsp;&nbsp;notifying</samp>](## "queue_monitor_length.notifying") | Boolean |  |  |  | Should only be used for platforms supporting the "queue-monitor length notifying" CLI. |
    | [<samp>&nbsp;&nbsp;cpu</samp>](## "queue_monitor_length.cpu") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;thresholds</samp>](## "queue_monitor_length.cpu.thresholds") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;high</samp>](## "queue_monitor_length.cpu.thresholds.high") | Integer | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;low</samp>](## "queue_monitor_length.cpu.thresholds.low") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;tx_latency</samp>](## "queue_monitor_length.tx_latency") | Boolean |  |  |  | Enable tx-latency mode. |

=== "YAML"

    ```yaml
    queue_monitor_length:
      enabled: <bool; required>
      default_thresholds:

        # Default high threshold for Ethernet Interfaces.
        high: <int; required>

        # Default low threshold for Ethernet Interfaces.
        # Low threshold support is platform dependent.
        low: <int>

      # Logging interval in seconds.
      log: <int>

      # Should only be used for platforms supporting the "queue-monitor length notifying" CLI.
      notifying: <bool>
      cpu:
        thresholds:
          high: <int; required>
          low: <int>

      # Enable tx-latency mode.
      tx_latency: <bool>
    ```
