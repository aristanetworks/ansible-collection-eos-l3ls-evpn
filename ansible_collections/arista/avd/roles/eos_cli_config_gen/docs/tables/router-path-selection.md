<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_path_selection</samp>](## "router_path_selection") | Dictionary |  |  |  | Dynamic path selection configuration. |
    | [<samp>&nbsp;&nbsp;peer_dynamic_source</samp>](## "router_path_selection.peer_dynamic_source") | String |  |  | Valid Values:<br>- <code>stun</code> | Source of dynamic peer discovery. |
    | [<samp>&nbsp;&nbsp;path_groups</samp>](## "router_path_selection.path_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_path_selection.path_groups.[].name") | String | Required, Unique |  |  | Path group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "router_path_selection.path_groups.[].id") | Integer |  |  | Min: 1<br>Max: 65535 | Path group ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipsec_profile</samp>](## "router_path_selection.path_groups.[].ipsec_profile") | String |  |  |  | IPSec profile for the path group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flow_assignment</samp>](## "router_path_selection.path_groups.[].flow_assignment") | String |  |  | Valid Values:<br>- <code>lan</code> | Flow assignment `lan` can not be configured in a path group with dynamic peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interfaces</samp>](## "router_path_selection.path_groups.[].local_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_path_selection.path_groups.[].local_interfaces.[].name") | String | Required, Unique |  | Pattern: `^(Port-Channel|Ethernet(\d+/)*)\d+(\.\d+)?$` | Local interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;public_address</samp>](## "router_path_selection.path_groups.[].local_interfaces.[].public_address") | String |  |  |  | Public IP assigned by NAT. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stun</samp>](## "router_path_selection.path_groups.[].local_interfaces.[].stun") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;server_profiles</samp>](## "router_path_selection.path_groups.[].local_interfaces.[].stun.server_profiles") | List, items: String | Required |  | Min Length: 1<br>Max Length: 12 | STUN server-profile names. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "router_path_selection.path_groups.[].local_interfaces.[].stun.server_profiles.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_ips</samp>](## "router_path_selection.path_groups.[].local_ips") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "router_path_selection.path_groups.[].local_ips.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;public_address</samp>](## "router_path_selection.path_groups.[].local_ips.[].public_address") | String |  |  |  | Public IP assigned by NAT. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stun</samp>](## "router_path_selection.path_groups.[].local_ips.[].stun") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;server_profiles</samp>](## "router_path_selection.path_groups.[].local_ips.[].stun.server_profiles") | List, items: String | Required |  | Min Length: 1<br>Max Length: 12 | STUN server-profile names. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "router_path_selection.path_groups.[].local_ips.[].stun.server_profiles.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic_peers</samp>](## "router_path_selection.path_groups.[].dynamic_peers") | Dictionary |  |  |  | Flow assignment `lan` can not be configured in a path group with dynamic peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_path_selection.path_groups.[].dynamic_peers.enabled") | Boolean |  |  |  | Enable `peer dynamic`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_local</samp>](## "router_path_selection.path_groups.[].dynamic_peers.ip_local") | Boolean |  |  |  | Prefer local IP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipsec</samp>](## "router_path_selection.path_groups.[].dynamic_peers.ipsec") | Boolean |  |  |  | IPsec configuration for dynamic peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static_peers</samp>](## "router_path_selection.path_groups.[].static_peers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;router_ip</samp>](## "router_path_selection.path_groups.[].static_peers.[].router_ip") | String | Required, Unique |  |  | Peer router IP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "router_path_selection.path_groups.[].static_peers.[].name") | String |  |  |  | Name of the site. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_addresses</samp>](## "router_path_selection.path_groups.[].static_peers.[].ipv4_addresses") | List, items: String |  |  |  | Static IPv4 addresses. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "router_path_selection.path_groups.[].static_peers.[].ipv4_addresses.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;keepalive</samp>](## "router_path_selection.path_groups.[].keepalive") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auto</samp>](## "router_path_selection.path_groups.[].keepalive.auto") | Boolean |  | `False` |  | Enable adaptive keepalive and feedback interval. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "router_path_selection.path_groups.[].keepalive.interval") | Integer |  |  | Min: 50<br>Max: 60000 | Interval in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;failure_threshold</samp>](## "router_path_selection.path_groups.[].keepalive.failure_threshold") | Integer |  |  | Min: 2<br>Max: 100 | Failure threshold in number of intervals. Required when `interval` is set. |
    | [<samp>&nbsp;&nbsp;load_balance_policies</samp>](## "router_path_selection.load_balance_policies") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_path_selection.load_balance_policies.[].name") | String | Required, Unique |  |  | Load-balance policy name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lowest_hop_count</samp>](## "router_path_selection.load_balance_policies.[].lowest_hop_count") | Boolean |  |  |  | Prefer paths with lowest hop-count. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;jitter</samp>](## "router_path_selection.load_balance_policies.[].jitter") | Integer |  |  | Min: 0<br>Max: 10000 | Jitter requirement for this load balance policy in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;latency</samp>](## "router_path_selection.load_balance_policies.[].latency") | Integer |  |  | Min: 0<br>Max: 10000 | One way delay requirement for this load balance policy in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loss_rate</samp>](## "router_path_selection.load_balance_policies.[].loss_rate") | String |  |  | Pattern: `^\d+(\.\d{1,2})?$` | Loss Rate requirement in percentage for this load balance policy.<br>Value between 0.00 and 100.00. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;path_groups</samp>](## "router_path_selection.load_balance_policies.[].path_groups") | List, items: Dictionary |  |  |  | List of path-groups to use for this load balance policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_path_selection.load_balance_policies.[].path_groups.[].name") | String | Required, Unique |  |  | Path-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "router_path_selection.load_balance_policies.[].path_groups.[].priority") | Integer |  |  | Min: 1<br>Max: 65535 | Priority for this path-group.<br>The EOS default value is 1. |
    | [<samp>&nbsp;&nbsp;policies</samp>](## "router_path_selection.policies") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_path_selection.policies.[].name") | String | Required, Unique |  |  | DPS policy name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_match</samp>](## "router_path_selection.policies.[].default_match") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;load_balance</samp>](## "router_path_selection.policies.[].default_match.load_balance") | String |  |  |  | Name of the load-balance policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rules</samp>](## "router_path_selection.policies.[].rules") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "router_path_selection.policies.[].rules.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 255 | Rule ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;application_profile</samp>](## "router_path_selection.policies.[].rules.[].application_profile") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;load_balance</samp>](## "router_path_selection.policies.[].rules.[].load_balance") | String |  |  |  | Name of the load-balance policy. |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "router_path_selection.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_path_selection.vrfs.[].name") | String | Required, Unique |  |  | VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;path_selection_policy</samp>](## "router_path_selection.vrfs.[].path_selection_policy") | String |  |  |  | DPS policy name to use for this VRF. |
    | [<samp>&nbsp;&nbsp;tcp_mss_ceiling</samp>](## "router_path_selection.tcp_mss_ceiling") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4_segment_size</samp>](## "router_path_selection.tcp_mss_ceiling.ipv4_segment_size") | String |  |  |  | Segment Size for IPv4.<br>Can be an integer in the range 64-65515 or "auto".<br>"auto" will enable auto-discovery which clamps the TCP MSS value to the minimum of all the direct paths<br>and multi-hop path MTU towards a remote VTEP (minus 40bytes to account for IP + TCP header). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "router_path_selection.tcp_mss_ceiling.direction") | String |  | `ingress` | Valid Values:<br>- <code>ingress</code> | Enforce on packets through DPS tunnel for a specific direction.<br>Only 'ingress' direction is supported. |

=== "YAML"

    ```yaml
    # Dynamic path selection configuration.
    router_path_selection:

      # Source of dynamic peer discovery.
      peer_dynamic_source: <str; "stun">
      path_groups:

          # Path group name.
        - name: <str; required; unique>

          # Path group ID.
          id: <int; 1-65535>

          # IPSec profile for the path group.
          ipsec_profile: <str>

          # Flow assignment `lan` can not be configured in a path group with dynamic peers.
          flow_assignment: <str; "lan">
          local_interfaces:

              # Local interface name.
            - name: <str; required; unique>

              # Public IP assigned by NAT.
              public_address: <str>
              stun:

                # STUN server-profile names.
                server_profiles: # 1-12 items; required
                  - <str>
          local_ips:
            - ip_address: <str; required; unique>

              # Public IP assigned by NAT.
              public_address: <str>
              stun:

                # STUN server-profile names.
                server_profiles: # 1-12 items; required
                  - <str>

          # Flow assignment `lan` can not be configured in a path group with dynamic peers.
          dynamic_peers:

            # Enable `peer dynamic`.
            enabled: <bool>

            # Prefer local IP address.
            ip_local: <bool>

            # IPsec configuration for dynamic peers.
            ipsec: <bool>
          static_peers:

              # Peer router IP.
            - router_ip: <str; required; unique>

              # Name of the site.
              name: <str>

              # Static IPv4 addresses.
              ipv4_addresses:
                - <str>
          keepalive:

            # Enable adaptive keepalive and feedback interval.
            auto: <bool; default=False>

            # Interval in milliseconds.
            interval: <int; 50-60000>

            # Failure threshold in number of intervals. Required when `interval` is set.
            failure_threshold: <int; 2-100>
      load_balance_policies:

          # Load-balance policy name.
        - name: <str; required; unique>

          # Prefer paths with lowest hop-count.
          lowest_hop_count: <bool>

          # Jitter requirement for this load balance policy in milliseconds.
          jitter: <int; 0-10000>

          # One way delay requirement for this load balance policy in milliseconds.
          latency: <int; 0-10000>

          # Loss Rate requirement in percentage for this load balance policy.
          # Value between 0.00 and 100.00.
          loss_rate: <str>

          # List of path-groups to use for this load balance policy.
          path_groups:

              # Path-group name.
            - name: <str; required; unique>

              # Priority for this path-group.
              # The EOS default value is 1.
              priority: <int; 1-65535>
      policies:

          # DPS policy name.
        - name: <str; required; unique>
          default_match:

            # Name of the load-balance policy.
            load_balance: <str>
          rules:

              # Rule ID.
            - id: <int; 1-255; required; unique>
              application_profile: <str; required>

              # Name of the load-balance policy.
              load_balance: <str>
      vrfs:

          # VRF name.
        - name: <str; required; unique>

          # DPS policy name to use for this VRF.
          path_selection_policy: <str>
      tcp_mss_ceiling:

        # Segment Size for IPv4.
        # Can be an integer in the range 64-65515 or "auto".
        # "auto" will enable auto-discovery which clamps the TCP MSS value to the minimum of all the direct paths
        # and multi-hop path MTU towards a remote VTEP (minus 40bytes to account for IP + TCP header).
        ipv4_segment_size: <str>

        # Enforce on packets through DPS tunnel for a specific direction.
        # Only 'ingress' direction is supported.
        direction: <str; "ingress"; default="ingress">
    ```
