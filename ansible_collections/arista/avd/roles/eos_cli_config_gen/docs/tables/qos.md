<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>qos</samp>](## "qos") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;map</samp>](## "qos.map") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "qos.map.cos") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "qos.map.cos.[]") | String |  |  |  | Example: "0 1 to traffic-class 1"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "qos.map.dscp") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "qos.map.dscp.[]") | String |  |  |  | Example: "8 9 10 to traffic-class 1"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;exp</samp>](## "qos.map.exp") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "qos.map.exp.[]") | String |  |  |  | Example "0 to traffic-class 0"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp>](## "qos.map.traffic_class") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "qos.map.traffic_class.[]") | String |  |  |  | Example: "1 to dscp 32"<br> |
    | [<samp>&nbsp;&nbsp;rewrite_dscp</samp>](## "qos.rewrite_dscp") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;random_detect</samp>](## "qos.random_detect") | Dictionary |  |  |  | Global random-detect settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ecn</samp>](## "qos.random_detect.ecn") | Dictionary |  |  |  | Global ECN Configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allow_non_ect</samp>](## "qos.random_detect.ecn.allow_non_ect") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "qos.random_detect.ecn.allow_non_ect.enabled") | Boolean |  |  |  | Allow non-ect and set drop-precedence 1 in a policy map simultaneously.<br>Check which command is required for your platform. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;chip_based</samp>](## "qos.random_detect.ecn.allow_non_ect.chip_based") | Boolean |  |  |  | Allow non-ect chip-based. |

=== "YAML"

    ```yaml
    qos:
      map:
        cos:

            # Example: "0 1 to traffic-class 1"
          - <str>
        dscp:

            # Example: "8 9 10 to traffic-class 1"
          - <str>
        exp:

            # Example "0 to traffic-class 0"
          - <str>
        traffic_class:

            # Example: "1 to dscp 32"
          - <str>
      rewrite_dscp: <bool>

      # Global random-detect settings.
      random_detect:

        # Global ECN Configuration.
        ecn:
          allow_non_ect:

            # Allow non-ect and set drop-precedence 1 in a policy map simultaneously.
            # Check which command is required for your platform.
            enabled: <bool>

            # Allow non-ect chip-based.
            chip_based: <bool>
    ```
