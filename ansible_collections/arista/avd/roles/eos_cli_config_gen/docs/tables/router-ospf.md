<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_ospf</samp>](## "router_ospf") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;process_ids</samp>](## "router_ospf.process_ids") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "router_ospf.process_ids.[].id") | Integer | Required, Unique |  |  | OSPF Process ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "router_ospf.process_ids.[].vrf") | String |  |  |  | VRF Name for OSPF Process. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;passive_interface_default</samp>](## "router_ospf.process_ids.[].passive_interface_default") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "router_ospf.process_ids.[].router_id") | String |  |  |  | IPv4 Address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "router_ospf.process_ids.[].distance") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;external</samp>](## "router_ospf.process_ids.[].distance.external") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_area</samp>](## "router_ospf.process_ids.[].distance.inter_area") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;intra_area</samp>](## "router_ospf.process_ids.[].distance.intra_area") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;log_adjacency_changes_detail</samp>](## "router_ospf.process_ids.[].log_adjacency_changes_detail") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;network_prefixes</samp>](## "router_ospf.process_ids.[].network_prefixes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ipv4_prefix</samp>](## "router_ospf.process_ids.[].network_prefixes.[].ipv4_prefix") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "router_ospf.process_ids.[].network_prefixes.[].area") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd_enable</samp>](## "router_ospf.process_ids.[].bfd_enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd_adjacency_state_any</samp>](## "router_ospf.process_ids.[].bfd_adjacency_state_any") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_passive_interfaces</samp>](## "router_ospf.process_ids.[].no_passive_interfaces") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "router_ospf.process_ids.[].no_passive_interfaces.[]") | String |  |  |  | Interface Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distribute_list_in</samp>](## "router_ospf.process_ids.[].distribute_list_in") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospf.process_ids.[].distribute_list_in.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_lsa</samp>](## "router_ospf.process_ids.[].max_lsa") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "router_ospf.process_ids.[].timers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lsa</samp>](## "router_ospf.process_ids.[].timers.lsa") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rx_min_interval</samp>](## "router_ospf.process_ids.[].timers.lsa.rx_min_interval") | Integer |  |  | Min: 0<br>Max: 600000 | Min interval in msecs between accepting the same LSA. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tx_delay</samp>](## "router_ospf.process_ids.[].timers.lsa.tx_delay") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;initial</samp>](## "router_ospf.process_ids.[].timers.lsa.tx_delay.initial") | Integer |  |  | Min: 0<br>Max: 600000 | Delay to generate first occurrence of LSA in msecs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min</samp>](## "router_ospf.process_ids.[].timers.lsa.tx_delay.min") | Integer |  |  | Min: 1<br>Max: 600000 | Min delay between originating the same LSA in msecs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max</samp>](## "router_ospf.process_ids.[].timers.lsa.tx_delay.max") | Integer |  |  | Min: 1<br>Max: 600000 | 1-600000 Maximum delay between originating the same LSA in msec. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spf_delay</samp>](## "router_ospf.process_ids.[].timers.spf_delay") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;initial</samp>](## "router_ospf.process_ids.[].timers.spf_delay.initial") | Integer |  |  | Min: 0<br>Max: 600000 | Initial SPF schedule delay in msecs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min</samp>](## "router_ospf.process_ids.[].timers.spf_delay.min") | Integer |  |  | Min: 0<br>Max: 65535000 | Min Hold time between two SPFs in msecs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max</samp>](## "router_ospf.process_ids.[].timers.spf_delay.max") | Integer |  |  | Min: 0<br>Max: 65535000 | Max wait time between two SPFs in msecs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_information_originate</samp>](## "router_ospf.process_ids.[].default_information_originate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "router_ospf.process_ids.[].default_information_originate.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metric</samp>](## "router_ospf.process_ids.[].default_information_originate.metric") | Integer |  |  | Min: 1<br>Max: 65535 | Metric for default route. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metric_type</samp>](## "router_ospf.process_ids.[].default_information_originate.metric_type") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code> | OSPF metric type for default route. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summary_addresses</samp>](## "router_ospf.process_ids.[].summary_addresses") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "router_ospf.process_ids.[].summary_addresses.[].prefix") | String | Required, Unique |  |  | Summary Prefix Address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tag</samp>](## "router_ospf.process_ids.[].summary_addresses.[].tag") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;attribute_map</samp>](## "router_ospf.process_ids.[].summary_addresses.[].attribute_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;not_advertise</samp>](## "router_ospf.process_ids.[].summary_addresses.[].not_advertise") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute</samp>](## "router_ospf.process_ids.[].redistribute") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "router_ospf.process_ids.[].redistribute.static") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospf.process_ids.[].redistribute.static.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospf.process_ids.[].redistribute.static.route_map") | String |  |  |  | Route Map Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_ospf.process_ids.[].redistribute.static.include_leaked") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected</samp>](## "router_ospf.process_ids.[].redistribute.connected") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospf.process_ids.[].redistribute.connected.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospf.process_ids.[].redistribute.connected.route_map") | String |  |  |  | Route Map Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_ospf.process_ids.[].redistribute.connected.include_leaked") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_ospf.process_ids.[].redistribute.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospf.process_ids.[].redistribute.bgp.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_ospf.process_ids.[].redistribute.bgp.route_map") | String |  |  |  | Route Map Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_ospf.process_ids.[].redistribute.bgp.include_leaked") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auto_cost_reference_bandwidth</samp>](## "router_ospf.process_ids.[].auto_cost_reference_bandwidth") | Integer |  |  |  | Bandwidth in mbps. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;areas</samp>](## "router_ospf.process_ids.[].areas") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "router_ospf.process_ids.[].areas.[].id") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filter</samp>](## "router_ospf.process_ids.[].areas.[].filter") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;networks</samp>](## "router_ospf.process_ids.[].areas.[].filter.networks") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "router_ospf.process_ids.[].areas.[].filter.networks.[]") | String |  |  |  | IPv4 Prefix. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp>](## "router_ospf.process_ids.[].areas.[].filter.prefix_list") | String |  |  |  | Prefix-List Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "router_ospf.process_ids.[].areas.[].type") | String |  | `normal` | Valid Values:<br>- <code>normal</code><br>- <code>stub</code><br>- <code>nssa</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_summary</samp>](## "router_ospf.process_ids.[].areas.[].no_summary") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nssa_only</samp>](## "router_ospf.process_ids.[].areas.[].nssa_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_information_originate</samp>](## "router_ospf.process_ids.[].areas.[].default_information_originate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metric</samp>](## "router_ospf.process_ids.[].areas.[].default_information_originate.metric") | Integer |  |  | Min: 1<br>Max: 65535 | Metric for default route. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metric_type</samp>](## "router_ospf.process_ids.[].areas.[].default_information_originate.metric_type") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code> | OSPF metric type for default route. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_paths</samp>](## "router_ospf.process_ids.[].maximum_paths") | Integer |  |  | Min: 1<br>Max: 128 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_metric</samp>](## "router_ospf.process_ids.[].max_metric") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_lsa</samp>](## "router_ospf.process_ids.[].max_metric.router_lsa") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;external_lsa</samp>](## "router_ospf.process_ids.[].max_metric.router_lsa.external_lsa") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;override_metric</samp>](## "router_ospf.process_ids.[].max_metric.router_lsa.external_lsa.override_metric") | Integer |  |  | Min: 1<br>Max: 16777215 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_stub</samp>](## "router_ospf.process_ids.[].max_metric.router_lsa.include_stub") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_startup</samp>](## "router_ospf.process_ids.[].max_metric.router_lsa.on_startup") | String |  |  |  | "wait-for-bgp" or Integer 5-86400.<br>Example: "wait-for-bgp" Or "222"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summary_lsa</samp>](## "router_ospf.process_ids.[].max_metric.router_lsa.summary_lsa") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;override_metric</samp>](## "router_ospf.process_ids.[].max_metric.router_lsa.summary_lsa.override_metric") | Integer |  |  | Min: 1<br>Max: 16777215 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;graceful_restart</samp>](## "router_ospf.process_ids.[].graceful_restart") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_ospf.process_ids.[].graceful_restart.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;grace_period</samp>](## "router_ospf.process_ids.[].graceful_restart.grace_period") | Integer |  |  | Min: 1<br>Max: 1800 | Specify maximum time in seconds to wait for graceful-restart to complete. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;graceful_restart_helper</samp>](## "router_ospf.process_ids.[].graceful_restart_helper") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ldp_sync_default</samp>](## "router_ospf.process_ids.[].mpls_ldp_sync_default") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "router_ospf.process_ids.[].eos_cli") | String |  |  |  | Multiline EOS CLI rendered directly on the Router OSPF process ID in the final EOS configuration. |

=== "YAML"

    ```yaml
    router_ospf:
      process_ids:

          # OSPF Process ID.
        - id: <int; required; unique>

          # VRF Name for OSPF Process.
          vrf: <str>
          passive_interface_default: <bool>

          # IPv4 Address.
          router_id: <str>
          distance:
            external: <int; 1-255>
            inter_area: <int; 1-255>
            intra_area: <int; 1-255>
          log_adjacency_changes_detail: <bool>
          network_prefixes:
            - ipv4_prefix: <str; required; unique>
              area: <str>
          bfd_enable: <bool>
          bfd_adjacency_state_any: <bool>
          no_passive_interfaces:

              # Interface Name.
            - <str>
          distribute_list_in:
            route_map: <str>
          max_lsa: <int>
          timers:
            lsa:

              # Min interval in msecs between accepting the same LSA.
              rx_min_interval: <int; 0-600000>
              tx_delay:

                # Delay to generate first occurrence of LSA in msecs.
                initial: <int; 0-600000>

                # Min delay between originating the same LSA in msecs.
                min: <int; 1-600000>

                # 1-600000 Maximum delay between originating the same LSA in msec.
                max: <int; 1-600000>
            spf_delay:

              # Initial SPF schedule delay in msecs.
              initial: <int; 0-600000>

              # Min Hold time between two SPFs in msecs.
              min: <int; 0-65535000>

              # Max wait time between two SPFs in msecs.
              max: <int; 0-65535000>
          default_information_originate:
            always: <bool>

            # Metric for default route.
            metric: <int; 1-65535>

            # OSPF metric type for default route.
            metric_type: <int; 1 | 2>
          summary_addresses:

              # Summary Prefix Address.
            - prefix: <str; required; unique>
              tag: <int>
              attribute_map: <str>
              not_advertise: <bool>
          redistribute:
            static:
              enabled: <bool; required>

              # Route Map Name.
              route_map: <str>
              include_leaked: <bool>
            connected:
              enabled: <bool; required>

              # Route Map Name.
              route_map: <str>
              include_leaked: <bool>
            bgp:
              enabled: <bool; required>

              # Route Map Name.
              route_map: <str>
              include_leaked: <bool>

          # Bandwidth in mbps.
          auto_cost_reference_bandwidth: <int>
          areas:
            - id: <str; required; unique>
              filter:
                networks:

                    # IPv4 Prefix.
                  - <str>

                # Prefix-List Name.
                prefix_list: <str>
              type: <str; "normal" | "stub" | "nssa"; default="normal">
              no_summary: <bool>
              nssa_only: <bool>
              default_information_originate:

                # Metric for default route.
                metric: <int; 1-65535>

                # OSPF metric type for default route.
                metric_type: <int; 1 | 2>
          maximum_paths: <int; 1-128>
          max_metric:
            router_lsa:
              external_lsa:
                override_metric: <int; 1-16777215>
              include_stub: <bool>

              # "wait-for-bgp" or Integer 5-86400.
              # Example: "wait-for-bgp" Or "222"
              on_startup: <str>
              summary_lsa:
                override_metric: <int; 1-16777215>
          graceful_restart:
            enabled: <bool; required>

            # Specify maximum time in seconds to wait for graceful-restart to complete.
            grace_period: <int; 1-1800>
          graceful_restart_helper: <bool>
          mpls_ldp_sync_default: <bool>

          # Multiline EOS CLI rendered directly on the Router OSPF process ID in the final EOS configuration.
          eos_cli: <str>
    ```
