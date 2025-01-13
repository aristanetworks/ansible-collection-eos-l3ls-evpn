<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_nat</samp>](## "ip_nat") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;kernel_buffer_size</samp>](## "ip_nat.kernel_buffer_size") | Integer |  |  | Min: 1<br>Max: 64 | Buffer size in MB. |
    | [<samp>&nbsp;&nbsp;profiles</samp>](## "ip_nat.profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "ip_nat.profiles.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ip_nat.profiles.[].vrf") | String |  |  |  | Specify VRF for NAT profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "ip_nat.profiles.[].destination") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic</samp>](## "ip_nat.profiles.[].destination.dynamic") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;access_list</samp>](## "ip_nat.profiles.[].destination.dynamic.[].access_list") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "ip_nat.profiles.[].destination.dynamic.[].comment") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pool_name</samp>](## "ip_nat.profiles.[].destination.dynamic.[].pool_name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "ip_nat.profiles.[].destination.dynamic.[].priority") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "ip_nat.profiles.[].destination.static") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;access_list</samp>](## "ip_nat.profiles.[].destination.static.[].access_list") | String |  |  |  | 'access_list' and 'group' are mutual exclusive. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "ip_nat.profiles.[].destination.static.[].comment") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "ip_nat.profiles.[].destination.static.[].direction") | String |  |  | Valid Values:<br>- <code>egress</code><br>- <code>ingress</code> | Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.<br>EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "ip_nat.profiles.[].destination.static.[].group") | Integer |  |  | Min: 1<br>Max: 65535 | 'access_list' and 'group' are mutual exclusive. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;original_ip</samp>](## "ip_nat.profiles.[].destination.static.[].original_ip") | String |  |  |  | IPv4 address. The combination of `original_ip` and `original_port` must be unique. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;original_port</samp>](## "ip_nat.profiles.[].destination.static.[].original_port") | Integer |  |  | Min: 1<br>Max: 65535 | TCP/UDP port. The combination of `original_ip` and `original_port` must be unique. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "ip_nat.profiles.[].destination.static.[].priority") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "ip_nat.profiles.[].destination.static.[].protocol") | String |  |  | Valid Values:<br>- <code>udp</code><br>- <code>tcp</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;translated_ip</samp>](## "ip_nat.profiles.[].destination.static.[].translated_ip") | String | Required |  |  | IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;translated_port</samp>](## "ip_nat.profiles.[].destination.static.[].translated_port") | Integer |  |  | Min: 1<br>Max: 65535 | requires 'original_port'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "ip_nat.profiles.[].source") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic</samp>](## "ip_nat.profiles.[].source.dynamic") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;access_list</samp>](## "ip_nat.profiles.[].source.dynamic.[].access_list") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "ip_nat.profiles.[].source.dynamic.[].comment") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nat_type</samp>](## "ip_nat.profiles.[].source.dynamic.[].nat_type") | String | Required |  | Valid Values:<br>- <code>overload</code><br>- <code>pool</code><br>- <code>pool-address-only</code><br>- <code>pool-full-cone</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pool_name</samp>](## "ip_nat.profiles.[].source.dynamic.[].pool_name") | String |  |  |  | required if 'nat_type' is pool, pool-address-only or pool-full-cone.<br>ignored if 'nat_type' is overload.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "ip_nat.profiles.[].source.dynamic.[].priority") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "ip_nat.profiles.[].source.static") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;access_list</samp>](## "ip_nat.profiles.[].source.static.[].access_list") | String |  |  |  | 'access_list' and 'group' are mutual exclusive. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "ip_nat.profiles.[].source.static.[].comment") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "ip_nat.profiles.[].source.static.[].direction") | String |  |  | Valid Values:<br>- <code>egress</code><br>- <code>ingress</code> | Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.<br>EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "ip_nat.profiles.[].source.static.[].group") | Integer |  |  | Min: 1<br>Max: 65535 | 'access_list' and 'group' are mutual exclusive. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;original_ip</samp>](## "ip_nat.profiles.[].source.static.[].original_ip") | String |  |  |  | IPv4 address. The combination of `original_ip` and `original_port` must be unique. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;original_port</samp>](## "ip_nat.profiles.[].source.static.[].original_port") | Integer |  |  | Min: 1<br>Max: 65535 | TCP/UDP port. The combination of `original_ip` and `original_port` must be unique. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "ip_nat.profiles.[].source.static.[].priority") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "ip_nat.profiles.[].source.static.[].protocol") | String |  |  | Valid Values:<br>- <code>udp</code><br>- <code>tcp</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;translated_ip</samp>](## "ip_nat.profiles.[].source.static.[].translated_ip") | String | Required |  |  | IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;translated_port</samp>](## "ip_nat.profiles.[].source.static.[].translated_port") | Integer |  |  | Min: 1<br>Max: 65535 | requires 'original_port'. |
    | [<samp>&nbsp;&nbsp;pools</samp>](## "ip_nat.pools") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "ip_nat.pools.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "ip_nat.pools.[].type") | String |  | `ip-port` | Valid Values:<br>- <code>ip-port</code><br>- <code>port-only</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_length</samp>](## "ip_nat.pools.[].prefix_length") | Integer |  |  | Min: 16<br>Max: 32 | It is only used and required when `type` is `ip-port`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ranges</samp>](## "ip_nat.pools.[].ranges") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;first_ip</samp>](## "ip_nat.pools.[].ranges.[].first_ip") | String |  |  |  | IPv4 address.<br>Required when `type` is `ip-port` and ignored otherwise. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;last_ip</samp>](## "ip_nat.pools.[].ranges.[].last_ip") | String |  |  |  | IPv4 address.<br>Required when `type` is `ip-port` and ignored otherwise.<br>`first_ip` and `last_ip` ip addresses should lie in same subnet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;first_port</samp>](## "ip_nat.pools.[].ranges.[].first_port") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;last_port</samp>](## "ip_nat.pools.[].ranges.[].last_port") | Integer |  |  | Min: 1<br>Max: 65535 | Required when `first_port` is set.<br>`last_port` must be greater than or equal to `first_port`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;utilization_log_threshold</samp>](## "ip_nat.pools.[].utilization_log_threshold") | Integer |  |  | Min: 1<br>Max: 100 |  |
    | [<samp>&nbsp;&nbsp;synchronization</samp>](## "ip_nat.synchronization") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "ip_nat.synchronization.description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;expiry_interval</samp>](## "ip_nat.synchronization.expiry_interval") | Integer |  |  | Min: 60<br>Max: 3600 | In seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "ip_nat.synchronization.local_interface") | String |  |  |  | EOS interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_address</samp>](## "ip_nat.synchronization.peer_address") | String |  |  |  | IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;port_range</samp>](## "ip_nat.synchronization.port_range") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;first_port</samp>](## "ip_nat.synchronization.port_range.first_port") | Integer |  |  | Min: 1024<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;last_port</samp>](## "ip_nat.synchronization.port_range.last_port") | Integer |  |  | Min: 1024<br>Max: 65535 | >= first_port. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;split_disabled</samp>](## "ip_nat.synchronization.port_range.split_disabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "ip_nat.synchronization.shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;translation</samp>](## "ip_nat.translation") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;address_selection</samp>](## "ip_nat.translation.address_selection") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;any</samp>](## "ip_nat.translation.address_selection.any") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_field_source_ip</samp>](## "ip_nat.translation.address_selection.hash_field_source_ip") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters</samp>](## "ip_nat.translation.counters") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;low_mark</samp>](## "ip_nat.translation.low_mark") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;percentage</samp>](## "ip_nat.translation.low_mark.percentage") | Integer |  |  | Min: 1<br>Max: 99 | Used to render 'ip nat translation low-mark <percentage>'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_percentage</samp>](## "ip_nat.translation.low_mark.host_percentage") | Integer |  |  | Min: 1<br>Max: 99 | Used to render 'ip nat translation low-mark <host_percentage> host'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;max_entries</samp>](## "ip_nat.translation.max_entries") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;limit</samp>](## "ip_nat.translation.max_entries.limit") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_limit</samp>](## "ip_nat.translation.max_entries.host_limit") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_limits</samp>](## "ip_nat.translation.max_entries.ip_limits") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip</samp>](## "ip_nat.translation.max_entries.ip_limits.[].ip") | String | Required, Unique |  |  | IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;limit</samp>](## "ip_nat.translation.max_entries.ip_limits.[].limit") | Integer | Required |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;timeouts</samp>](## "ip_nat.translation.timeouts") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;protocol</samp>](## "ip_nat.translation.timeouts.[].protocol") | String | Required, Unique |  | Valid Values:<br>- <code>tcp</code><br>- <code>udp</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "ip_nat.translation.timeouts.[].timeout") | Integer | Required |  | Min: 0<br>Max: 4294967295 | In seconds. |

=== "YAML"

    ```yaml
    ip_nat:

      # Buffer size in MB.
      kernel_buffer_size: <int; 1-64>
      profiles:
        - name: <str; required; unique>

          # Specify VRF for NAT profile.
          vrf: <str>
          destination:
            dynamic:
              - access_list: <str; required; unique>
                comment: <str>
                pool_name: <str; required>
                priority: <int; 0-4294967295>
            static:

                # 'access_list' and 'group' are mutual exclusive.
              - access_list: <str>
                comment: <str>

                # Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
                # EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.
                direction: <str; "egress" | "ingress">

                # 'access_list' and 'group' are mutual exclusive.
                group: <int; 1-65535>

                # IPv4 address. The combination of `original_ip` and `original_port` must be unique.
                original_ip: <str>

                # TCP/UDP port. The combination of `original_ip` and `original_port` must be unique.
                original_port: <int; 1-65535>
                priority: <int; 0-4294967295>
                protocol: <str; "udp" | "tcp">

                # IPv4 address.
                translated_ip: <str; required>

                # requires 'original_port'.
                translated_port: <int; 1-65535>
          source:
            dynamic:
              - access_list: <str; required; unique>
                comment: <str>
                nat_type: <str; "overload" | "pool" | "pool-address-only" | "pool-full-cone"; required>

                # required if 'nat_type' is pool, pool-address-only or pool-full-cone.
                # ignored if 'nat_type' is overload.
                pool_name: <str>
                priority: <int; 0-4294967295>
            static:

                # 'access_list' and 'group' are mutual exclusive.
              - access_list: <str>
                comment: <str>

                # Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.
                # EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.
                direction: <str; "egress" | "ingress">

                # 'access_list' and 'group' are mutual exclusive.
                group: <int; 1-65535>

                # IPv4 address. The combination of `original_ip` and `original_port` must be unique.
                original_ip: <str>

                # TCP/UDP port. The combination of `original_ip` and `original_port` must be unique.
                original_port: <int; 1-65535>
                priority: <int; 0-4294967295>
                protocol: <str; "udp" | "tcp">

                # IPv4 address.
                translated_ip: <str; required>

                # requires 'original_port'.
                translated_port: <int; 1-65535>
      pools:
        - name: <str; required; unique>
          type: <str; "ip-port" | "port-only"; default="ip-port">

          # It is only used and required when `type` is `ip-port`.
          prefix_length: <int; 16-32>
          ranges:

              # IPv4 address.
              # Required when `type` is `ip-port` and ignored otherwise.
            - first_ip: <str>

              # IPv4 address.
              # Required when `type` is `ip-port` and ignored otherwise.
              # `first_ip` and `last_ip` ip addresses should lie in same subnet.
              last_ip: <str>
              first_port: <int; 1-65535>

              # Required when `first_port` is set.
              # `last_port` must be greater than or equal to `first_port`.
              last_port: <int; 1-65535>
          utilization_log_threshold: <int; 1-100>
      synchronization:
        description: <str>

        # In seconds.
        expiry_interval: <int; 60-3600>

        # EOS interface name.
        local_interface: <str>

        # IPv4 address.
        peer_address: <str>
        port_range:
          first_port: <int; 1024-65535>

          # >= first_port.
          last_port: <int; 1024-65535>
          split_disabled: <bool>
        shutdown: <bool>
      translation:
        address_selection:
          any: <bool>
          hash_field_source_ip: <bool>
        counters: <bool>
        low_mark:

          # Used to render 'ip nat translation low-mark <percentage>'.
          percentage: <int; 1-99>

          # Used to render 'ip nat translation low-mark <host_percentage> host'.
          host_percentage: <int; 1-99>
        max_entries:
          limit: <int; 0-4294967295>
          host_limit: <int; 0-4294967295>
          ip_limits:

              # IPv4 address.
            - ip: <str; required; unique>
              limit: <int; 0-4294967295; required>
        timeouts:
          - protocol: <str; "tcp" | "udp"; required; unique>

            # In seconds.
            timeout: <int; 0-4294967295; required>
    ```
