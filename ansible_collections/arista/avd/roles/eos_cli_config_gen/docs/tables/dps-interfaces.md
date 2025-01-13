<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>dps_interfaces</samp>](## "dps_interfaces") | List, items: Dictionary |  |  | Min Length: 1<br>Max Length: 1 |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "dps_interfaces.[].name") | String | Required, Unique |  | Valid Values:<br>- <code>Dps1</code> | "Dps1" is currently the only supported interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "dps_interfaces.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "dps_interfaces.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "dps_interfaces.[].mtu") | Integer |  |  | Min: 68<br>Max: 65535 | Maximum Transmission Unit in bytes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "dps_interfaces.[].ip_address") | String |  |  |  | IPv4 address/mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;flow_tracker</samp>](## "dps_interfaces.[].flow_tracker") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sampled</samp>](## "dps_interfaces.[].flow_tracker.sampled") | String |  |  |  | Sampled flow tracker name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware</samp>](## "dps_interfaces.[].flow_tracker.hardware") | String |  |  |  | Hardware flow tracker name, |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tcp_mss_ceiling</samp>](## "dps_interfaces.[].tcp_mss_ceiling") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "dps_interfaces.[].tcp_mss_ceiling.ipv4") | Integer |  |  | Min: 64<br>Max: 65495 | Segment Size for IPv4. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "dps_interfaces.[].tcp_mss_ceiling.ipv6") | Integer |  |  | Min: 64<br>Max: 65475 | Segment Size for IPv6. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "dps_interfaces.[].tcp_mss_ceiling.direction") | String |  |  | Valid Values:<br>- <code>ingress</code><br>- <code>egress</code> | Optional direction ('ingress', 'egress')  for tcp mss ceiling. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "dps_interfaces.[].eos_cli") | String |  |  |  | Multiline String with EOS CLI rendered directly on the Dps interface in the final EOS configuration. |

=== "YAML"

    ```yaml
    dps_interfaces: # 1-1 items

        # "Dps1" is currently the only supported interface.
      - name: <str; "Dps1"; required; unique>
        description: <str>
        shutdown: <bool>

        # Maximum Transmission Unit in bytes.
        mtu: <int; 68-65535>

        # IPv4 address/mask.
        ip_address: <str>
        flow_tracker:

          # Sampled flow tracker name.
          sampled: <str>

          # Hardware flow tracker name,
          hardware: <str>
        tcp_mss_ceiling:

          # Segment Size for IPv4.
          ipv4: <int; 64-65495>

          # Segment Size for IPv6.
          ipv6: <int; 64-65475>

          # Optional direction ('ingress', 'egress')  for tcp mss ceiling.
          direction: <str; "ingress" | "egress">

        # Multiline String with EOS CLI rendered directly on the Dps interface in the final EOS configuration.
        eos_cli: <str>
    ```
