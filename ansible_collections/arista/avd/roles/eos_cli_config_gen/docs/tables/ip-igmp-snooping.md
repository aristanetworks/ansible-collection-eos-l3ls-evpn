<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_igmp_snooping</samp>](## "ip_igmp_snooping") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;globally_enabled</samp>](## "ip_igmp_snooping.globally_enabled") | Boolean |  | `True` |  | Activate or deactivate IGMP snooping for all vlans where `vlans` allows user to activate / deactivate IGMP snooping per vlan. |
    | [<samp>&nbsp;&nbsp;robustness_variable</samp>](## "ip_igmp_snooping.robustness_variable") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;restart_query_interval</samp>](## "ip_igmp_snooping.restart_query_interval") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;interface_restart_query</samp>](## "ip_igmp_snooping.interface_restart_query") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;fast_leave</samp>](## "ip_igmp_snooping.fast_leave") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;querier</samp>](## "ip_igmp_snooping.querier") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ip_igmp_snooping.querier.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;address</samp>](## "ip_igmp_snooping.querier.address") | String |  |  |  | IP Address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;query_interval</samp>](## "ip_igmp_snooping.querier.query_interval") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;max_response_time</samp>](## "ip_igmp_snooping.querier.max_response_time") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;last_member_query_interval</samp>](## "ip_igmp_snooping.querier.last_member_query_interval") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;last_member_query_count</samp>](## "ip_igmp_snooping.querier.last_member_query_count") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;startup_query_interval</samp>](## "ip_igmp_snooping.querier.startup_query_interval") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;startup_query_count</samp>](## "ip_igmp_snooping.querier.startup_query_count") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "ip_igmp_snooping.querier.version") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;proxy</samp>](## "ip_igmp_snooping.proxy") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;vlans</samp>](## "ip_igmp_snooping.vlans") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "ip_igmp_snooping.vlans.[].id") | Integer | Required, Unique |  |  | VLAN ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ip_igmp_snooping.vlans.[].enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;querier</samp>](## "ip_igmp_snooping.vlans.[].querier") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ip_igmp_snooping.vlans.[].querier.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address</samp>](## "ip_igmp_snooping.vlans.[].querier.address") | String |  |  |  | IP Address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;query_interval</samp>](## "ip_igmp_snooping.vlans.[].querier.query_interval") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_response_time</samp>](## "ip_igmp_snooping.vlans.[].querier.max_response_time") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;last_member_query_interval</samp>](## "ip_igmp_snooping.vlans.[].querier.last_member_query_interval") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;last_member_query_count</samp>](## "ip_igmp_snooping.vlans.[].querier.last_member_query_count") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;startup_query_interval</samp>](## "ip_igmp_snooping.vlans.[].querier.startup_query_interval") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;startup_query_count</samp>](## "ip_igmp_snooping.vlans.[].querier.startup_query_count") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "ip_igmp_snooping.vlans.[].querier.version") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_groups</samp>](## "ip_igmp_snooping.vlans.[].max_groups") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fast_leave</samp>](## "ip_igmp_snooping.vlans.[].fast_leave") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;proxy</samp>](## "ip_igmp_snooping.vlans.[].proxy") | Boolean |  |  |  | Global proxy settings should be enabled before enabling per-vlan.<br> |

=== "YAML"

    ```yaml
    ip_igmp_snooping:

      # Activate or deactivate IGMP snooping for all vlans where `vlans` allows user to activate / deactivate IGMP snooping per vlan.
      globally_enabled: <bool; default=True>
      robustness_variable: <int>
      restart_query_interval: <int>
      interface_restart_query: <int>
      fast_leave: <bool>
      querier:
        enabled: <bool>

        # IP Address.
        address: <str>
        query_interval: <int>
        max_response_time: <int>
        last_member_query_interval: <int>
        last_member_query_count: <int>
        startup_query_interval: <int>
        startup_query_count: <int>
        version: <int>
      proxy: <bool>
      vlans:

          # VLAN ID.
        - id: <int; required; unique>
          enabled: <bool>
          querier:
            enabled: <bool>

            # IP Address.
            address: <str>
            query_interval: <int>
            max_response_time: <int>
            last_member_query_interval: <int>
            last_member_query_count: <int>
            startup_query_interval: <int>
            startup_query_count: <int>
            version: <int>
          max_groups: <int>
          fast_leave: <bool>

          # Global proxy settings should be enabled before enabling per-vlan.
          proxy: <bool>
    ```
