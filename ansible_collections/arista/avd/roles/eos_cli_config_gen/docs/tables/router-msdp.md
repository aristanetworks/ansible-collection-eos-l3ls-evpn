<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_msdp</samp>](## "router_msdp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;originator_id_local_interface</samp>](## "router_msdp.originator_id_local_interface") | String |  |  |  | Interface to use for originator ID. |
    | [<samp>&nbsp;&nbsp;rejected_limit</samp>](## "router_msdp.rejected_limit") | Integer |  |  | Min: 0<br>Max: 40000 | Maximum number of rejected SA messages allowed in cache. |
    | [<samp>&nbsp;&nbsp;forward_register_packets</samp>](## "router_msdp.forward_register_packets") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;connection_retry_interval</samp>](## "router_msdp.connection_retry_interval") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;group_limits</samp>](## "router_msdp.group_limits") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;source_prefix</samp>](## "router_msdp.group_limits.[].source_prefix") | String | Required, Unique |  |  | Source address prefix. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;limit</samp>](## "router_msdp.group_limits.[].limit") | Integer | Required |  | Min: 0<br>Max: 40000 | Limit for SAs matching the source address prefix. |
    | [<samp>&nbsp;&nbsp;peers</samp>](## "router_msdp.peers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ipv4_address</samp>](## "router_msdp.peers.[].ipv4_address") | String | Required, Unique |  |  | Peer IP Address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_peer</samp>](## "router_msdp.peers.[].default_peer") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_msdp.peers.[].default_peer.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp>](## "router_msdp.peers.[].default_peer.prefix_list") | String |  |  |  | Prefix list to filter source of SA messages. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "router_msdp.peers.[].local_interface") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "router_msdp.peers.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "router_msdp.peers.[].disabled") | Boolean |  |  |  | Disable the MSDP peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sa_limit</samp>](## "router_msdp.peers.[].sa_limit") | Integer |  |  | Min: 0<br>Max: 40000 | Maximum number of SA messages allowed in cache. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mesh_groups</samp>](## "router_msdp.peers.[].mesh_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_msdp.peers.[].mesh_groups.[].name") | String | Required, Unique |  |  | Mesh group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;keepalive</samp>](## "router_msdp.peers.[].keepalive") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;keepalive_timer</samp>](## "router_msdp.peers.[].keepalive.keepalive_timer") | Integer | Required |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hold_timer</samp>](## "router_msdp.peers.[].keepalive.hold_timer") | Integer | Required |  | Min: 1<br>Max: 65535 | Must be greater than keepalive timer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sa_filter</samp>](## "router_msdp.peers.[].sa_filter") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;in_list</samp>](## "router_msdp.peers.[].sa_filter.in_list") | String |  |  |  | ACL to filter inbound SA messages. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;out_list</samp>](## "router_msdp.peers.[].sa_filter.out_list") | String |  |  |  | ACL to filter outbound SA messages. |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "router_msdp.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_msdp.vrfs.[].name") | String | Required, Unique |  |  | VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;originator_id_local_interface</samp>](## "router_msdp.vrfs.[].originator_id_local_interface") | String |  |  |  | Interface to use for originator ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rejected_limit</samp>](## "router_msdp.vrfs.[].rejected_limit") | Integer |  |  | Min: 0<br>Max: 40000 | Maximum number of rejected SA messages allowed in cache. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward_register_packets</samp>](## "router_msdp.vrfs.[].forward_register_packets") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connection_retry_interval</samp>](## "router_msdp.vrfs.[].connection_retry_interval") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group_limits</samp>](## "router_msdp.vrfs.[].group_limits") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;source_prefix</samp>](## "router_msdp.vrfs.[].group_limits.[].source_prefix") | String | Required, Unique |  |  | Source address prefix. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;limit</samp>](## "router_msdp.vrfs.[].group_limits.[].limit") | Integer | Required |  | Min: 0<br>Max: 40000 | Limit for SAs matching the source address prefix. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peers</samp>](## "router_msdp.vrfs.[].peers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ipv4_address</samp>](## "router_msdp.vrfs.[].peers.[].ipv4_address") | String | Required, Unique |  |  | Peer IP Address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_peer</samp>](## "router_msdp.vrfs.[].peers.[].default_peer") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_msdp.vrfs.[].peers.[].default_peer.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp>](## "router_msdp.vrfs.[].peers.[].default_peer.prefix_list") | String |  |  |  | Prefix list to filter source of SA messages. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "router_msdp.vrfs.[].peers.[].local_interface") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "router_msdp.vrfs.[].peers.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "router_msdp.vrfs.[].peers.[].disabled") | Boolean |  |  |  | Disable the MSDP peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sa_limit</samp>](## "router_msdp.vrfs.[].peers.[].sa_limit") | Integer |  |  | Min: 0<br>Max: 40000 | Maximum number of SA messages allowed in cache. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mesh_groups</samp>](## "router_msdp.vrfs.[].peers.[].mesh_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_msdp.vrfs.[].peers.[].mesh_groups.[].name") | String | Required, Unique |  |  | Mesh group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;keepalive</samp>](## "router_msdp.vrfs.[].peers.[].keepalive") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;keepalive_timer</samp>](## "router_msdp.vrfs.[].peers.[].keepalive.keepalive_timer") | Integer | Required |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hold_timer</samp>](## "router_msdp.vrfs.[].peers.[].keepalive.hold_timer") | Integer | Required |  | Min: 1<br>Max: 65535 | Must be greater than keepalive timer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sa_filter</samp>](## "router_msdp.vrfs.[].peers.[].sa_filter") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;in_list</samp>](## "router_msdp.vrfs.[].peers.[].sa_filter.in_list") | String |  |  |  | ACL to filter inbound SA messages. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;out_list</samp>](## "router_msdp.vrfs.[].peers.[].sa_filter.out_list") | String |  |  |  | ACL to filter outbound SA messages. |

=== "YAML"

    ```yaml
    router_msdp:

      # Interface to use for originator ID.
      originator_id_local_interface: <str>

      # Maximum number of rejected SA messages allowed in cache.
      rejected_limit: <int; 0-40000>
      forward_register_packets: <bool>
      connection_retry_interval: <int; 1-65535>
      group_limits:

          # Source address prefix.
        - source_prefix: <str; required; unique>

          # Limit for SAs matching the source address prefix.
          limit: <int; 0-40000; required>
      peers:

          # Peer IP Address.
        - ipv4_address: <str; required; unique>
          default_peer:
            enabled: <bool>

            # Prefix list to filter source of SA messages.
            prefix_list: <str>
          local_interface: <str>
          description: <str>

          # Disable the MSDP peer.
          disabled: <bool>

          # Maximum number of SA messages allowed in cache.
          sa_limit: <int; 0-40000>
          mesh_groups:

              # Mesh group name.
            - name: <str; required; unique>
          keepalive:
            keepalive_timer: <int; 1-65535; required>

            # Must be greater than keepalive timer.
            hold_timer: <int; 1-65535; required>
          sa_filter:

            # ACL to filter inbound SA messages.
            in_list: <str>

            # ACL to filter outbound SA messages.
            out_list: <str>
      vrfs:

          # VRF name.
        - name: <str; required; unique>

          # Interface to use for originator ID.
          originator_id_local_interface: <str>

          # Maximum number of rejected SA messages allowed in cache.
          rejected_limit: <int; 0-40000>
          forward_register_packets: <bool>
          connection_retry_interval: <int; 1-65535>
          group_limits:

              # Source address prefix.
            - source_prefix: <str; required; unique>

              # Limit for SAs matching the source address prefix.
              limit: <int; 0-40000; required>
          peers:

              # Peer IP Address.
            - ipv4_address: <str; required; unique>
              default_peer:
                enabled: <bool>

                # Prefix list to filter source of SA messages.
                prefix_list: <str>
              local_interface: <str>
              description: <str>

              # Disable the MSDP peer.
              disabled: <bool>

              # Maximum number of SA messages allowed in cache.
              sa_limit: <int; 0-40000>
              mesh_groups:

                  # Mesh group name.
                - name: <str; required; unique>
              keepalive:
                keepalive_timer: <int; 1-65535; required>

                # Must be greater than keepalive timer.
                hold_timer: <int; 1-65535; required>
              sa_filter:

                # ACL to filter inbound SA messages.
                in_list: <str>

                # ACL to filter outbound SA messages.
                out_list: <str>
    ```
