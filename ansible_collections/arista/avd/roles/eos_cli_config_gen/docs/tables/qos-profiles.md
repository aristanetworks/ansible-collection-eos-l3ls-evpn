<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>qos_profiles</samp>](## "qos_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "qos_profiles.[].name") | String | Required, Unique |  |  | Profile-Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trust</samp>](## "qos_profiles.[].trust") | String |  |  | Valid Values:<br>- <code>cos</code><br>- <code>dscp</code><br>- <code>disabled</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "qos_profiles.[].cos") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "qos_profiles.[].dscp") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shape</samp>](## "qos_profiles.[].shape") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "qos_profiles.[].shape.rate") | String |  |  |  | Supported options are platform dependent.<br>Example: "< rate > kbps", "1-100 percent", "< rate > pps"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;service_policy</samp>](## "qos_profiles.[].service_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "qos_profiles.[].service_policy.type") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_input</samp>](## "qos_profiles.[].service_policy.type.qos_input") | String |  |  |  | Policy-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tx_queues</samp>](## "qos_profiles.[].tx_queues") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "qos_profiles.[].tx_queues.[].id") | Integer | Required, Unique |  |  | TX-Queue ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_percent</samp>](## "qos_profiles.[].tx_queues.[].bandwidth_percent") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_guaranteed_percent</samp>](## "qos_profiles.[].tx_queues.[].bandwidth_guaranteed_percent") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "qos_profiles.[].tx_queues.[].priority") | String |  |  | Valid Values:<br>- <code>priority strict</code><br>- <code>no priority</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shape</samp>](## "qos_profiles.[].tx_queues.[].shape") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "qos_profiles.[].tx_queues.[].shape.rate") | String |  |  |  | Supported options are platform dependent.<br>Example: "< rate > kbps", "1-100 percent", "< rate > pps"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "qos_profiles.[].tx_queues.[].comment") | String |  |  |  | Text comment added to queue. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;random_detect</samp>](## "qos_profiles.[].tx_queues.[].random_detect") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ecn</samp>](## "qos_profiles.[].tx_queues.[].random_detect.ecn") | Dictionary |  |  |  | Explicit Congestion Notification. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;count</samp>](## "qos_profiles.[].tx_queues.[].random_detect.ecn.count") | Boolean |  |  |  | Enable counter for random-detect ECNs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "qos_profiles.[].tx_queues.[].random_detect.ecn.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;units</samp>](## "qos_profiles.[].tx_queues.[].random_detect.ecn.threshold.units") | String | Required |  | Valid Values:<br>- <code>segments</code><br>- <code>bytes</code><br>- <code>kbytes</code><br>- <code>mbytes</code><br>- <code>milliseconds</code> | Units to be used for the threshold values.<br>This should be one of segments, byte, kbytes, mbytes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min</samp>](## "qos_profiles.[].tx_queues.[].random_detect.ecn.threshold.min") | Integer | Required |  | Min: 1 | Random-detect ECN minimum-threshold. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max</samp>](## "qos_profiles.[].tx_queues.[].random_detect.ecn.threshold.max") | Integer | Required |  | Min: 1 | Random-detect ECN maximum-threshold. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_probability</samp>](## "qos_profiles.[].tx_queues.[].random_detect.ecn.threshold.max_probability") | Integer |  |  | Min: 1<br>Max: 100 | Random-detect ECN maximum mark probability. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "qos_profiles.[].tx_queues.[].random_detect.ecn.threshold.weight") | Integer |  |  | Min: 0<br>Max: 15 | Random-detect ECN weight. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "qos_profiles.[].tx_queues.[].random_detect.drop") | Dictionary |  |  |  | Set WRED parameters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "qos_profiles.[].tx_queues.[].random_detect.drop.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;units</samp>](## "qos_profiles.[].tx_queues.[].random_detect.drop.threshold.units") | String | Required |  | Valid Values:<br>- <code>segments</code><br>- <code>bytes</code><br>- <code>kbytes</code><br>- <code>mbytes</code><br>- <code>microseconds</code><br>- <code>milliseconds</code> | Units to be used for the threshold values. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop_precedence</samp>](## "qos_profiles.[].tx_queues.[].random_detect.drop.threshold.drop_precedence") | Integer |  |  | Min: 0<br>Max: 2 | Specify Drop Precedence value. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min</samp>](## "qos_profiles.[].tx_queues.[].random_detect.drop.threshold.min") | Integer | Required |  | Min: 1 | WRED minimum-threshold. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max</samp>](## "qos_profiles.[].tx_queues.[].random_detect.drop.threshold.max") | Integer | Required |  | Min: 1 | WRED maximum-threshold. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop_probability</samp>](## "qos_profiles.[].tx_queues.[].random_detect.drop.threshold.drop_probability") | Integer | Required |  | Min: 1<br>Max: 100 | WRED drop probability. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "qos_profiles.[].tx_queues.[].random_detect.drop.threshold.weight") | Integer |  |  | Min: 0<br>Max: 15 | WRED weight. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uc_tx_queues</samp>](## "qos_profiles.[].uc_tx_queues") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "qos_profiles.[].uc_tx_queues.[].id") | Integer | Required, Unique |  |  | UC TX queue ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_percent</samp>](## "qos_profiles.[].uc_tx_queues.[].bandwidth_percent") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_guaranteed_percent</samp>](## "qos_profiles.[].uc_tx_queues.[].bandwidth_guaranteed_percent") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "qos_profiles.[].uc_tx_queues.[].priority") | String |  |  | Valid Values:<br>- <code>priority strict</code><br>- <code>no priority</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shape</samp>](## "qos_profiles.[].uc_tx_queues.[].shape") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "qos_profiles.[].uc_tx_queues.[].shape.rate") | String |  |  |  | Supported options are platform dependent.<br>Example: "< rate > kbps", "1-100 percent", "< rate > pps"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "qos_profiles.[].uc_tx_queues.[].comment") | String |  |  |  | Text comment added to queue. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;random_detect</samp>](## "qos_profiles.[].uc_tx_queues.[].random_detect") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ecn</samp>](## "qos_profiles.[].uc_tx_queues.[].random_detect.ecn") | Dictionary |  |  |  | Explicit Congestion Notification. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;count</samp>](## "qos_profiles.[].uc_tx_queues.[].random_detect.ecn.count") | Boolean |  |  |  | Enable counter for random-detect ECNs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "qos_profiles.[].uc_tx_queues.[].random_detect.ecn.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;units</samp>](## "qos_profiles.[].uc_tx_queues.[].random_detect.ecn.threshold.units") | String | Required |  | Valid Values:<br>- <code>segments</code><br>- <code>bytes</code><br>- <code>kbytes</code><br>- <code>mbytes</code><br>- <code>milliseconds</code> | Unit to be used for the threshold values. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min</samp>](## "qos_profiles.[].uc_tx_queues.[].random_detect.ecn.threshold.min") | Integer | Required |  | Min: 1 | Random-detect ECN minimum-threshold. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max</samp>](## "qos_profiles.[].uc_tx_queues.[].random_detect.ecn.threshold.max") | Integer | Required |  | Min: 1 | Random-detect ECN maximum-threshold. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_probability</samp>](## "qos_profiles.[].uc_tx_queues.[].random_detect.ecn.threshold.max_probability") | Integer |  |  | Min: 1<br>Max: 100 | Random-detect ECN maximum mark probability. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "qos_profiles.[].uc_tx_queues.[].random_detect.ecn.threshold.weight") | Integer |  |  | Min: 0<br>Max: 15 | Random-detect ECN weight. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "qos_profiles.[].uc_tx_queues.[].random_detect.drop") | Dictionary |  |  |  | Set WRED parameters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "qos_profiles.[].uc_tx_queues.[].random_detect.drop.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;units</samp>](## "qos_profiles.[].uc_tx_queues.[].random_detect.drop.threshold.units") | String | Required |  | Valid Values:<br>- <code>segments</code><br>- <code>bytes</code><br>- <code>kbytes</code><br>- <code>mbytes</code><br>- <code>microseconds</code><br>- <code>milliseconds</code> | Units to be used for the threshold values. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop_precedence</samp>](## "qos_profiles.[].uc_tx_queues.[].random_detect.drop.threshold.drop_precedence") | Integer |  |  | Min: 0<br>Max: 2 | Specify Drop Precedence value. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min</samp>](## "qos_profiles.[].uc_tx_queues.[].random_detect.drop.threshold.min") | Integer | Required |  | Min: 1 | WRED minimum-threshold. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max</samp>](## "qos_profiles.[].uc_tx_queues.[].random_detect.drop.threshold.max") | Integer | Required |  | Min: 1 | WRED maximum-threshold. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop_probability</samp>](## "qos_profiles.[].uc_tx_queues.[].random_detect.drop.threshold.drop_probability") | Integer | Required |  | Min: 1<br>Max: 100 | WRED drop probability. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "qos_profiles.[].uc_tx_queues.[].random_detect.drop.threshold.weight") | Integer |  |  | Min: 0<br>Max: 15 | WRED weight. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mc_tx_queues</samp>](## "qos_profiles.[].mc_tx_queues") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "qos_profiles.[].mc_tx_queues.[].id") | Integer | Required, Unique |  |  | MC TX queue ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_percent</samp>](## "qos_profiles.[].mc_tx_queues.[].bandwidth_percent") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bandwidth_guaranteed_percent</samp>](## "qos_profiles.[].mc_tx_queues.[].bandwidth_guaranteed_percent") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "qos_profiles.[].mc_tx_queues.[].priority") | String |  |  | Valid Values:<br>- <code>priority strict</code><br>- <code>no priority</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shape</samp>](## "qos_profiles.[].mc_tx_queues.[].shape") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "qos_profiles.[].mc_tx_queues.[].shape.rate") | String |  |  |  | Supported options are platform dependent.<br>Example: "< rate > kbps", "1-100 percent", "< rate > pps"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "qos_profiles.[].mc_tx_queues.[].comment") | String |  |  |  | Text comment added to queue.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;priority_flow_control</samp>](## "qos_profiles.[].priority_flow_control") | Dictionary |  |  |  | Priority Flow Control settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "qos_profiles.[].priority_flow_control.enabled") | Boolean |  |  |  | Enable Priority Flow control.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;watchdog</samp>](## "qos_profiles.[].priority_flow_control.watchdog") | Dictionary |  |  |  | Watchdog can detect stuck transmit queues.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "qos_profiles.[].priority_flow_control.watchdog.enabled") | Boolean | Required |  |  | Enable the watchdog on stuck transmit queues.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "qos_profiles.[].priority_flow_control.watchdog.action") | String |  |  | Valid Values:<br>- <code>drop</code><br>- <code>notify-only</code> | Override the default error-disable action to either drop<br>traffic on the stuck queue or notify-only<br>without making any actions on the stuck queue.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timer</samp>](## "qos_profiles.[].priority_flow_control.watchdog.timer") | Dictionary |  |  |  | Timer thresholds whilst monitoring queues.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "qos_profiles.[].priority_flow_control.watchdog.timer.timeout") | String | Required |  | Pattern: `^\d+(\.\d{1,2})?$` | Timeout in seconds after which port should be errdisabled or<br>should start dropping on congested priorities.<br>This should be decimal with up to 2 decimal point.<br>Example: 0.01 or 60<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;polling_interval</samp>](## "qos_profiles.[].priority_flow_control.watchdog.timer.polling_interval") | String | Required |  | Pattern: `^auto|\d+(\.\d{1,3})?$` | Time interval in seconds at which the watchdog should poll the queues.<br>This should be decimal with up to 3 decimal point or set<br>to 'auto' based on recovery_time and timeout values.<br>Example: 0.005 or 60<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_time</samp>](## "qos_profiles.[].priority_flow_control.watchdog.timer.recovery_time") | String | Required |  | Pattern: `^\d+(\.\d{1,2})?$` | Recovery-time in seconds after which stuck queue should<br>recover and start forwarding again.<br>This should be decimal with up to 2 decimal point.<br>Example: 0.01 or 60<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forced</samp>](## "qos_profiles.[].priority_flow_control.watchdog.timer.forced") | Boolean |  |  |  | Force recover any stuck queue(s) after the duration,<br>irrespective of whether PFC frames are being<br>received or not.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priorities</samp>](## "qos_profiles.[].priority_flow_control.priorities") | List, items: Dictionary |  |  |  | Set the drop/no_drop on each queue.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;priority</samp>](## "qos_profiles.[].priority_flow_control.priorities.[].priority") | Integer | Required, Unique |  | Min: 0<br>Max: 7 | Priority queue number (COS value).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_drop</samp>](## "qos_profiles.[].priority_flow_control.priorities.[].no_drop") | Boolean | Required |  |  | Enable Priority Flow Control frames on this queue.<br> |

=== "YAML"

    ```yaml
    qos_profiles:

        # Profile-Name.
      - name: <str; required; unique>
        trust: <str; "cos" | "dscp" | "disabled">
        cos: <int>
        dscp: <int>
        shape:

          # Supported options are platform dependent.
          # Example: "< rate > kbps", "1-100 percent", "< rate > pps"
          rate: <str>
        service_policy:
          type:

            # Policy-map name.
            qos_input: <str>
        tx_queues:

            # TX-Queue ID.
          - id: <int; required; unique>
            bandwidth_percent: <int>
            bandwidth_guaranteed_percent: <int>
            priority: <str; "priority strict" | "no priority">
            shape:

              # Supported options are platform dependent.
              # Example: "< rate > kbps", "1-100 percent", "< rate > pps"
              rate: <str>

            # Text comment added to queue.
            comment: <str>
            random_detect:

              # Explicit Congestion Notification.
              ecn:

                # Enable counter for random-detect ECNs.
                count: <bool>
                threshold:

                  # Units to be used for the threshold values.
                  # This should be one of segments, byte, kbytes, mbytes.
                  units: <str; "segments" | "bytes" | "kbytes" | "mbytes" | "milliseconds"; required>

                  # Random-detect ECN minimum-threshold.
                  min: <int; >=1; required>

                  # Random-detect ECN maximum-threshold.
                  max: <int; >=1; required>

                  # Random-detect ECN maximum mark probability.
                  max_probability: <int; 1-100>

                  # Random-detect ECN weight.
                  weight: <int; 0-15>

              # Set WRED parameters.
              drop:
                threshold:

                  # Units to be used for the threshold values.
                  units: <str; "segments" | "bytes" | "kbytes" | "mbytes" | "microseconds" | "milliseconds"; required>

                  # Specify Drop Precedence value.
                  drop_precedence: <int; 0-2>

                  # WRED minimum-threshold.
                  min: <int; >=1; required>

                  # WRED maximum-threshold.
                  max: <int; >=1; required>

                  # WRED drop probability.
                  drop_probability: <int; 1-100; required>

                  # WRED weight.
                  weight: <int; 0-15>
        uc_tx_queues:

            # UC TX queue ID.
          - id: <int; required; unique>
            bandwidth_percent: <int>
            bandwidth_guaranteed_percent: <int>
            priority: <str; "priority strict" | "no priority">
            shape:

              # Supported options are platform dependent.
              # Example: "< rate > kbps", "1-100 percent", "< rate > pps"
              rate: <str>

            # Text comment added to queue.
            comment: <str>
            random_detect:

              # Explicit Congestion Notification.
              ecn:

                # Enable counter for random-detect ECNs.
                count: <bool>
                threshold:

                  # Unit to be used for the threshold values.
                  units: <str; "segments" | "bytes" | "kbytes" | "mbytes" | "milliseconds"; required>

                  # Random-detect ECN minimum-threshold.
                  min: <int; >=1; required>

                  # Random-detect ECN maximum-threshold.
                  max: <int; >=1; required>

                  # Random-detect ECN maximum mark probability.
                  max_probability: <int; 1-100>

                  # Random-detect ECN weight.
                  weight: <int; 0-15>

              # Set WRED parameters.
              drop:
                threshold:

                  # Units to be used for the threshold values.
                  units: <str; "segments" | "bytes" | "kbytes" | "mbytes" | "microseconds" | "milliseconds"; required>

                  # Specify Drop Precedence value.
                  drop_precedence: <int; 0-2>

                  # WRED minimum-threshold.
                  min: <int; >=1; required>

                  # WRED maximum-threshold.
                  max: <int; >=1; required>

                  # WRED drop probability.
                  drop_probability: <int; 1-100; required>

                  # WRED weight.
                  weight: <int; 0-15>
        mc_tx_queues:

            # MC TX queue ID.
          - id: <int; required; unique>
            bandwidth_percent: <int>
            bandwidth_guaranteed_percent: <int>
            priority: <str; "priority strict" | "no priority">
            shape:

              # Supported options are platform dependent.
              # Example: "< rate > kbps", "1-100 percent", "< rate > pps"
              rate: <str>

            # Text comment added to queue.
            comment: <str>

        # Priority Flow Control settings.
        priority_flow_control:

          # Enable Priority Flow control.
          enabled: <bool>

          # Watchdog can detect stuck transmit queues.
          watchdog:

            # Enable the watchdog on stuck transmit queues.
            enabled: <bool; required>

            # Override the default error-disable action to either drop
            # traffic on the stuck queue or notify-only
            # without making any actions on the stuck queue.
            action: <str; "drop" | "notify-only">

            # Timer thresholds whilst monitoring queues.
            timer:

              # Timeout in seconds after which port should be errdisabled or
              # should start dropping on congested priorities.
              # This should be decimal with up to 2 decimal point.
              # Example: 0.01 or 60
              timeout: <str; required>

              # Time interval in seconds at which the watchdog should poll the queues.
              # This should be decimal with up to 3 decimal point or set
              # to 'auto' based on recovery_time and timeout values.
              # Example: 0.005 or 60
              polling_interval: <str; required>

              # Recovery-time in seconds after which stuck queue should
              # recover and start forwarding again.
              # This should be decimal with up to 2 decimal point.
              # Example: 0.01 or 60
              recovery_time: <str; required>

              # Force recover any stuck queue(s) after the duration,
              # irrespective of whether PFC frames are being
              # received or not.
              forced: <bool>

          # Set the drop/no_drop on each queue.
          priorities:

              # Priority queue number (COS value).
            - priority: <int; 0-7; required; unique>

              # Enable Priority Flow Control frames on this queue.
              no_drop: <bool; required>
    ```
