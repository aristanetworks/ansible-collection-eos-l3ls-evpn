<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>system</samp>](## "system") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;control_plane</samp>](## "system.control_plane") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tcp_mss</samp>](## "system.control_plane.tcp_mss") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "system.control_plane.tcp_mss.ipv4") | Integer |  |  |  | Segment size. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "system.control_plane.tcp_mss.ipv6") | Integer |  |  |  | Segment size. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4_access_group_ingress_default</samp>](## "system.control_plane.ipv4_access_group_ingress_default") | String |  |  |  | ACL name to be used as the default CP ACL for all VRFs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4_access_groups</samp>](## "system.control_plane.ipv4_access_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;acl_name</samp>](## "system.control_plane.ipv4_access_groups.[].acl_name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "system.control_plane.ipv4_access_groups.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_ingress_default</samp>](## "system.control_plane.ipv6_access_group_ingress_default") | String |  |  |  | ACL name to be used as the default CP ACL for all VRFs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_groups</samp>](## "system.control_plane.ipv6_access_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;acl_name</samp>](## "system.control_plane.ipv6_access_groups.[].acl_name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "system.control_plane.ipv6_access_groups.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;l1</samp>](## "system.l1") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;unsupported_speed_action</samp>](## "system.l1.unsupported_speed_action") | String |  |  | Valid Values:<br>- <code>error</code><br>- <code>warn</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;unsupported_error_correction_action</samp>](## "system.l1.unsupported_error_correction_action") | String |  |  | Valid Values:<br>- <code>error</code><br>- <code>warn</code> |  |

=== "YAML"

    ```yaml
    system:
      control_plane:
        tcp_mss:

          # Segment size.
          ipv4: <int>

          # Segment size.
          ipv6: <int>

        # ACL name to be used as the default CP ACL for all VRFs.
        ipv4_access_group_ingress_default: <str>
        ipv4_access_groups:
          - acl_name: <str; required>
            vrf: <str>

        # ACL name to be used as the default CP ACL for all VRFs.
        ipv6_access_group_ingress_default: <str>
        ipv6_access_groups:
          - acl_name: <str; required>
            vrf: <str>
      l1:
        unsupported_speed_action: <str; "error" | "warn">
        unsupported_error_correction_action: <str; "error" | "warn">
    ```
