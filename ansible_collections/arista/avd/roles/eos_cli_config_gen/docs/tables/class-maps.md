<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>class_maps</samp>](## "class_maps") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;pbr</samp>](## "class_maps.pbr") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "class_maps.pbr.[].name") | String | Required, Unique |  |  | Class-Map Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "class_maps.pbr.[].ip") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "class_maps.pbr.[].ip.access_group") | String |  |  |  | Standard Access-List Name. |
    | [<samp>&nbsp;&nbsp;qos</samp>](## "class_maps.qos") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "class_maps.qos.[].name") | String | Required, Unique |  |  | Class-Map Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "class_maps.qos.[].vlan") | String |  |  |  | VLAN value(s) or range(s) of VLAN values. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "class_maps.qos.[].cos") | String |  |  |  | CoS value(s) or range(s) of CoS values. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "class_maps.qos.[].ip") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "class_maps.qos.[].ip.access_group") | String |  |  |  | IPv4 Access-List Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "class_maps.qos.[].ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "class_maps.qos.[].ipv6.access_group") | String |  |  |  | IPv6 Access-List Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "class_maps.qos.[].dscp") | Dictionary |  |  |  | It allows match on either DSCP, ECN or both for the IPV4 and IPV6 packets. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp_value</samp>](## "class_maps.qos.[].dscp.dscp_value") | String |  |  |  | DSCP/ECN match classifies the precedence of incoming packets based on the value present in the IP header. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ecn</samp>](## "class_maps.qos.[].dscp.ecn") | String |  |  | Valid Values:<br>- <code>ce</code><br>- <code>ect</code><br>- <code>ect-ce</code><br>- <code>non-ect</code> | DSCP is the six most significant bits and ECN represents the two least significant bits of the IPv4 8-bit ToS field and IPv6 8-bit TC field. |

=== "YAML"

    ```yaml
    class_maps:
      pbr:

          # Class-Map Name.
        - name: <str; required; unique>
          ip:

            # Standard Access-List Name.
            access_group: <str>
      qos:

          # Class-Map Name.
        - name: <str; required; unique>

          # VLAN value(s) or range(s) of VLAN values.
          vlan: <str>

          # CoS value(s) or range(s) of CoS values.
          cos: <str>
          ip:

            # IPv4 Access-List Name.
            access_group: <str>
          ipv6:

            # IPv6 Access-List Name.
            access_group: <str>

          # It allows match on either DSCP, ECN or both for the IPV4 and IPV6 packets.
          dscp:

            # DSCP/ECN match classifies the precedence of incoming packets based on the value present in the IP header.
            dscp_value: <str>

            # DSCP is the six most significant bits and ECN represents the two least significant bits of the IPv4 8-bit ToS field and IPv6 8-bit TC field.
            ecn: <str; "ce" | "ect" | "ect-ce" | "non-ect">
    ```
