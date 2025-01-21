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
    | [<samp>&nbsp;&nbsp;qos</samp>](## "class_maps.qos") | List, items: Dictionary |  |  |  | Keys `dscp` and `ecn` are not mutually exclusive.<br>If both dscp and ecn are defined, CLI command would be:<br> - match dscp <dscp> ecn <ecn>.<br>If only dscp is defined, CLI command would be:<br>  - match dscp <dscp>.<br>If only ecn is defined, CLI command would be:<br>  - match ecn <ecn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "class_maps.qos.[].name") | String | Required, Unique |  |  | Class-Map Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "class_maps.qos.[].vlan") | String |  |  |  | VLAN value(s) or range(s) of VLAN values. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "class_maps.qos.[].cos") | String |  |  |  | CoS value(s) or range(s) of CoS values. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "class_maps.qos.[].ip") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "class_maps.qos.[].ip.access_group") | String |  |  |  | IPv4 Access-List Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "class_maps.qos.[].ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "class_maps.qos.[].ipv6.access_group") | String |  |  |  | IPv6 Access-List Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "class_maps.qos.[].dscp") | String |  |  |  | Match packets based on the DSCP value(s).<br>Accepted formats:<br>  - Single AF/EF PBH DSCP. Example: af12.<br>  - or Single CS DSCP. Example: cs1.<br>  - or Single decimal DSCP value. Example: 23.<br>  - or Range of decimal DSCP values. Examples: 1,3-10. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ecn</samp>](## "class_maps.qos.[].ecn") | String |  |  | Valid Values:<br>- <code>ce</code><br>- <code>ect</code><br>- <code>ect-ce</code><br>- <code>non-ect</code> | Match packets based on the ECN value.<br>Accepted values:<br>  - non-ect (matches 00).<br>  - ect (matches 01 an 10).<br>  - ce (matches 11).<br>  - ect-ce (matches 01, 10 and 11). |

=== "YAML"

    ```yaml
    class_maps:
      pbr:

          # Class-Map Name.
        - name: <str; required; unique>
          ip:

            # Standard Access-List Name.
            access_group: <str>

      # Keys `dscp` and `ecn` are not mutually exclusive.
      # If both dscp and ecn are defined, CLI command would be:
      #  - match dscp <dscp> ecn <ecn>.
      # If only dscp is defined, CLI command would be:
      #   - match dscp <dscp>.
      # If only ecn is defined, CLI command would be:
      #   - match ecn <ecn>.
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

          # Match packets based on the DSCP value(s).
          # Accepted formats:
          #   - Single AF/EF PBH DSCP. Example: af12.
          #   - or Single CS DSCP. Example: cs1.
          #   - or Single decimal DSCP value. Example: 23.
          #   - or Range of decimal DSCP values. Examples: 1,3-10.
          dscp: <str>

          # Match packets based on the ECN value.
          # Accepted values:
          #   - non-ect (matches 00).
          #   - ect (matches 01 an 10).
          #   - ce (matches 11).
          #   - ect-ce (matches 01, 10 and 11).
          ecn: <str; "ce" | "ect" | "ect-ce" | "non-ect">
    ```
