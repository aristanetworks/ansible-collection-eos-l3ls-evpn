<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>lldp</samp>](## "lldp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;timer</samp>](## "lldp.timer") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;timer_reinitialization</samp>](## "lldp.timer_reinitialization") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;holdtime</samp>](## "lldp.holdtime") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;management_address</samp>](## "lldp.management_address") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;vrf</samp>](## "lldp.vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;receive_packet_tagged_drop</samp>](## "lldp.receive_packet_tagged_drop") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;tlvs</samp>](## "lldp.tlvs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "lldp.tlvs.[].name") | String | Required, Unique |  | Valid Values:<br>- <code>link-aggregation</code><br>- <code>management-address</code><br>- <code>max-frame-size</code><br>- <code>med</code><br>- <code>port-description</code><br>- <code>port-vlan</code><br>- <code>power-via-mdi</code><br>- <code>system-capabilities</code><br>- <code>system-description</code><br>- <code>system-name</code><br>- <code>vlan-name</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transmit</samp>](## "lldp.tlvs.[].transmit") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;run</samp>](## "lldp.run") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    lldp:
      timer: <int>
      timer_reinitialization: <str>
      holdtime: <int>
      management_address: <str>
      vrf: <str>
      receive_packet_tagged_drop: <str>
      tlvs:
        - name: <str; "link-aggregation" | "management-address" | "max-frame-size" | "med" | "port-description" | "port-vlan" | "power-via-mdi" | "system-capabilities" | "system-description" | "system-name" | "vlan-name"; required; unique>
          transmit: <bool>
      run: <bool>
    ```
