<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>monitor_twamp</samp>](## "monitor_twamp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;twamp_light</samp>](## "monitor_twamp.twamp_light") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;reflector_defaults</samp>](## "monitor_twamp.twamp_light.reflector_defaults") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;listen_port</samp>](## "monitor_twamp.twamp_light.reflector_defaults.listen_port") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sender_defaults</samp>](## "monitor_twamp.twamp_light.sender_defaults") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_port</samp>](## "monitor_twamp.twamp_light.sender_defaults.destination_port") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_port</samp>](## "monitor_twamp.twamp_light.sender_defaults.source_port") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sender_profiles</samp>](## "monitor_twamp.twamp_light.sender_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_twamp.twamp_light.sender_profiles.[].name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;measurement_interval</samp>](## "monitor_twamp.twamp_light.sender_profiles.[].measurement_interval") | Integer |  |  | Min: 1<br>Max: 255 | Measuremnt interval in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;measurement_samples</samp>](## "monitor_twamp.twamp_light.sender_profiles.[].measurement_samples") | Integer |  |  | Min: 1<br>Max: 65535 | Number of samples used to calculate TWAMP light metrics. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;significance</samp>](## "monitor_twamp.twamp_light.sender_profiles.[].significance") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "monitor_twamp.twamp_light.sender_profiles.[].significance.value") | Integer | Required |  | Min: 1<br>Max: 1000000 | Significance value in microseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset</samp>](## "monitor_twamp.twamp_light.sender_profiles.[].significance.offset") | Integer | Required |  | Min: 1<br>Max: 1000000 | Offset in microseconds, used to round up calculated TWAMP light delay statistics. Must be smaller than significance value. |

=== "YAML"

    ```yaml
    monitor_twamp:
      twamp_light:
        reflector_defaults:
          listen_port: <int; 1-65535>
        sender_defaults:
          destination_port: <int; 1-65535>
          source_port: <int; 1-65535>
        sender_profiles:
          - name: <str; required>

            # Measuremnt interval in seconds.
            measurement_interval: <int; 1-255>

            # Number of samples used to calculate TWAMP light metrics.
            measurement_samples: <int; 1-65535>
            significance:

              # Significance value in microseconds.
              value: <int; 1-1000000; required>

              # Offset in microseconds, used to round up calculated TWAMP light delay statistics. Must be smaller than significance value.
              offset: <int; 1-1000000; required>
    ```
