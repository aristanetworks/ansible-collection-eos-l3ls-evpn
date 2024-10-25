<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_bgp</samp>](## "router_bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;as</samp>](## "router_bgp.as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;as_notation</samp>](## "router_bgp.as_notation") | String |  |  | Valid Values:<br>- <code>asdot</code><br>- <code>asplain</code> | BGP AS can be deplayed in the asplain <1-4294967295> or asdot notation "<1-65535>.<0-65535>". This flag indicates which mode is preferred - asplain is the default. |
    | [<samp>&nbsp;&nbsp;router_id</samp>](## "router_bgp.router_id") | String |  |  |  | In IP address format A.B.C.D. |
    | [<samp>&nbsp;&nbsp;distance</samp>](## "router_bgp.distance") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;external_routes</samp>](## "router_bgp.distance.external_routes") | Integer | Required |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;internal_routes</samp>](## "router_bgp.distance.internal_routes") | Integer | Required |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;local_routes</samp>](## "router_bgp.distance.local_routes") | Integer | Required |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;graceful_restart</samp>](## "router_bgp.graceful_restart") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.graceful_restart.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;restart_time</samp>](## "router_bgp.graceful_restart.restart_time") | Integer |  |  | Min: 1<br>Max: 3600 | Number of seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;stalepath_time</samp>](## "router_bgp.graceful_restart.stalepath_time") | Integer |  |  | Min: 1<br>Max: 3600 | Number of seconds. |
    | [<samp>&nbsp;&nbsp;graceful_restart_helper</samp>](## "router_bgp.graceful_restart_helper") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.graceful_restart_helper.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;restart_time</samp>](## "router_bgp.graceful_restart_helper.restart_time") | Integer |  |  | Min: 1<br>Max: 100000000 | Number of seconds<br>graceful-restart-help long-lived and restart-time are mutually exclusive in CLI.<br>restart-time will take precedence if both are configured.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;long_lived</samp>](## "router_bgp.graceful_restart_helper.long_lived") | Boolean |  |  |  | graceful-restart-help long-lived and restart-time are mutually exclusive in CLI.<br>restart-time will take precedence if both are configured.<br> |
    | [<samp>&nbsp;&nbsp;maximum_paths</samp>](## "router_bgp.maximum_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;paths</samp>](## "router_bgp.maximum_paths.paths") | Integer | Required |  | Min: 1<br>Max: 600 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ecmp</samp>](## "router_bgp.maximum_paths.ecmp") | Integer |  |  | Min: 1<br>Max: 600 |  |
    | [<samp>&nbsp;&nbsp;updates</samp>](## "router_bgp.updates") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;wait_for_convergence</samp>](## "router_bgp.updates.wait_for_convergence") | Boolean |  |  |  | Disables FIB updates and route advertisement when the BGP instance is initiated until the BGP convergence state is reached.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;wait_install</samp>](## "router_bgp.updates.wait_install") | Boolean |  |  |  | Do not advertise reachability to a prefix until that prefix has been installed in hardware.<br>This will eliminate any temporary black holes due to a BGP speaker advertising reachability to a prefix that may not yet be installed into the forwarding plane.<br> |
    | [<samp>&nbsp;&nbsp;bgp_cluster_id</samp>](## "router_bgp.bgp_cluster_id") | String |  |  |  | IP Address A.B.C.D. |
    | [<samp>&nbsp;&nbsp;bgp_defaults</samp>](## "router_bgp.bgp_defaults") | List, items: String |  |  |  | BGP command as string. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "router_bgp.bgp_defaults.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;bgp</samp>](## "router_bgp.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "router_bgp.bgp.default") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_unicast</samp>](## "router_bgp.bgp.default.ipv4_unicast") | Boolean |  |  |  | Default activation of IPv4 unicast address-family on all IPv4 neighbors (EOS default = True). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_unicast_transport_ipv6</samp>](## "router_bgp.bgp.default.ipv4_unicast_transport_ipv6") | Boolean |  |  |  | Default activation of IPv4 unicast address-family on all IPv6 neighbors (EOS default == False). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;route_reflector_preserve_attributes</samp>](## "router_bgp.bgp.route_reflector_preserve_attributes") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.bgp.route_reflector_preserve_attributes.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "router_bgp.bgp.route_reflector_preserve_attributes.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bestpath</samp>](## "router_bgp.bgp.bestpath") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;d_path</samp>](## "router_bgp.bgp.bestpath.d_path") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.bgp.additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.bgp.additional_paths.receive") | Boolean |  |  |  | Enable or disable reception of additional-paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send</samp>](## "router_bgp.bgp.additional_paths.send") | String |  |  | Valid Values:<br>- <code>any</code><br>- <code>backup</code><br>- <code>ecmp</code><br>- <code>limit</code><br>- <code>disabled</code> | Select an option to send multiple paths for same prefix through bgp updates.<br>any: Send any eligible path.<br>backup: Best path and installed backup path.<br>ecmp: All paths in best path ECMP group.<br>limit: Limit to n eligible paths.<br>disabled: Disable sending any paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_limit</samp>](## "router_bgp.bgp.additional_paths.send_limit") | Integer |  |  | Min: 2<br>Max: 64 | Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;redistribute_internal</samp>](## "router_bgp.bgp.redistribute_internal") | Boolean |  |  |  | Allow redistribution of iBGP routes into an Interior Gateway Protocol (IGP). EOS default is true. |
    | [<samp>&nbsp;&nbsp;listen_ranges</samp>](## "router_bgp.listen_ranges") | List, items: Dictionary |  |  |  | Improved "listen_ranges" data model to support multiple listen ranges and additional filter capabilities.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "router_bgp.listen_ranges.[].prefix") | String |  |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_id_include_router_id</samp>](## "router_bgp.listen_ranges.[].peer_id_include_router_id") | Boolean |  |  |  | Include router ID as part of peer filter. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp>](## "router_bgp.listen_ranges.[].peer_group") | String |  |  |  | Peer group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_filter</samp>](## "router_bgp.listen_ranges.[].peer_filter") | String |  |  |  | Peer-filter name.<br>note: `peer_filter` or `remote_as` is required but mutually exclusive.<br>If both are defined, `peer_filter` takes precedence<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "router_bgp.listen_ranges.[].remote_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_bgp.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "router_bgp.peer_groups.[].type") | String |  |  |  | Key only used for documentation or validation purposes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "router_bgp.peer_groups.[].remote_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "router_bgp.peer_groups.[].local_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "router_bgp.peer_groups.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "router_bgp.peer_groups.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as_path</samp>](## "router_bgp.peer_groups.[].as_path") | Dictionary |  |  |  | BGP AS-PATH options. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as_replace_out</samp>](## "router_bgp.peer_groups.[].as_path.remote_as_replace_out") | Boolean |  |  |  | Replace AS number with local AS number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prepend_own_disabled</samp>](## "router_bgp.peer_groups.[].as_path.prepend_own_disabled") | Boolean |  |  |  | Disable prepending own AS number to AS path. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as</samp>](## "router_bgp.peer_groups.[].remove_private_as") | Dictionary |  |  |  | Remove private AS numbers in outbound AS path. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.peer_groups.[].remove_private_as.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "router_bgp.peer_groups.[].remove_private_as.all") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "router_bgp.peer_groups.[].remove_private_as.replace_as") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as_ingress</samp>](## "router_bgp.peer_groups.[].remove_private_as_ingress") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.peer_groups.[].remove_private_as_ingress.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "router_bgp.peer_groups.[].remove_private_as_ingress.replace_as") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_unchanged</samp>](## "router_bgp.peer_groups.[].next_hop_unchanged") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_source</samp>](## "router_bgp.peer_groups.[].update_source") | String |  |  |  | IP address or interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_reflector_client</samp>](## "router_bgp.peer_groups.[].route_reflector_client") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "router_bgp.peer_groups.[].bfd") | Boolean |  |  |  | Enable BFD. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd_timers</samp>](## "router_bgp.peer_groups.[].bfd_timers") | Dictionary |  |  |  | Override default BFD timers. BFD must be enabled with `bfd: true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "router_bgp.peer_groups.[].bfd_timers.interval") | Integer | Required |  | Min: 50<br>Max: 60000 | Interval in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp>](## "router_bgp.peer_groups.[].bfd_timers.min_rx") | Integer | Required |  | Min: 50<br>Max: 60000 | Rate in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "router_bgp.peer_groups.[].bfd_timers.multiplier") | Integer | Required |  | Min: 3<br>Max: 50 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp_multihop</samp>](## "router_bgp.peer_groups.[].ebgp_multihop") | Integer |  |  | Min: 1<br>Max: 255 | Time-to-live in range of hops. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp>](## "router_bgp.peer_groups.[].next_hop_self") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "router_bgp.peer_groups.[].password") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;passive</samp>](## "router_bgp.peer_groups.[].passive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "router_bgp.peer_groups.[].default_originate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.peer_groups.[].default_originate.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "router_bgp.peer_groups.[].default_originate.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.peer_groups.[].default_originate.route_map") | String |  |  |  | Route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_community</samp>](## "router_bgp.peer_groups.[].send_community") | String |  |  |  | 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "router_bgp.peer_groups.[].maximum_routes") | Integer |  |  | Min: 0<br>Max: 4294967294 | Maximum number of routes (0 means unlimited). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_limit</samp>](## "router_bgp.peer_groups.[].maximum_routes_warning_limit") | String |  |  |  | Maximum number of routes after which a warning is issued (0 means never warn) or<br>Percentage of maximum number of routes at which to warn ("<1-100> percent").<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_only</samp>](## "router_bgp.peer_groups.[].maximum_routes_warning_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.peer_groups.[].missing_policy") | Dictionary |  |  |  | Missing policy configuration for all address-families. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in</samp>](## "router_bgp.peer_groups.[].missing_policy.direction_in") | Dictionary |  |  |  | Missing policy inbound direction. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "router_bgp.peer_groups.[].missing_policy.direction_in.action") | String | Required |  | Valid Values:<br>- <code>deny</code><br>- <code>permit</code><br>- <code>deny-in-out</code> | Missing policy action. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_community_list</samp>](## "router_bgp.peer_groups.[].missing_policy.direction_in.include_community_list") | Boolean |  |  |  | Include community-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_prefix_list</samp>](## "router_bgp.peer_groups.[].missing_policy.direction_in.include_prefix_list") | Boolean |  |  |  | Include prefix-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_sub_route_map</samp>](## "router_bgp.peer_groups.[].missing_policy.direction_in.include_sub_route_map") | Boolean |  |  |  | Include sub-route-map references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out</samp>](## "router_bgp.peer_groups.[].missing_policy.direction_out") | Dictionary |  |  |  | Missing policy outbound direction. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "router_bgp.peer_groups.[].missing_policy.direction_out.action") | String | Required |  | Valid Values:<br>- <code>deny</code><br>- <code>permit</code><br>- <code>deny-in-out</code> | Missing policy action. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_community_list</samp>](## "router_bgp.peer_groups.[].missing_policy.direction_out.include_community_list") | Boolean |  |  |  | Include community-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_prefix_list</samp>](## "router_bgp.peer_groups.[].missing_policy.direction_out.include_prefix_list") | Boolean |  |  |  | Include prefix-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_sub_route_map</samp>](## "router_bgp.peer_groups.[].missing_policy.direction_out.include_sub_route_map") | Boolean |  |  |  | Include sub-route-map references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_bandwidth</samp>](## "router_bgp.peer_groups.[].link_bandwidth") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.peer_groups.[].link_bandwidth.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "router_bgp.peer_groups.[].link_bandwidth.default") | String |  |  |  | nn.nn(K|M|G) link speed in bits/second. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allowas_in</samp>](## "router_bgp.peer_groups.[].allowas_in") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.peer_groups.[].allowas_in.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;times</samp>](## "router_bgp.peer_groups.[].allowas_in.times") | Integer |  |  | Min: 1<br>Max: 10 | Number of local ASNs allowed in a BGP update. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "router_bgp.peer_groups.[].weight") | Integer |  |  | Min: 0<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "router_bgp.peer_groups.[].timers") | String |  |  |  | BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rib_in_pre_policy_retain</samp>](## "router_bgp.peer_groups.[].rib_in_pre_policy_retain") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.peer_groups.[].rib_in_pre_policy_retain.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "router_bgp.peer_groups.[].rib_in_pre_policy_retain.all") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session_tracker</samp>](## "router_bgp.peer_groups.[].session_tracker") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shared_secret</samp>](## "router_bgp.peer_groups.[].shared_secret") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "router_bgp.peer_groups.[].shared_secret.profile") | String | Required |  |  | Name of profile defined under `management_security`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "router_bgp.peer_groups.[].shared_secret.hash_algorithm") | String | Required |  | Valid Values:<br>- <code>aes-128-cmac-96</code><br>- <code>hmac-sha-256</code><br>- <code>hmac-sha1-96</code> | Note: Algorithm hmac-sha-256 requires EOS version 4.31.1F and above. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl_maximum_hops</samp>](## "router_bgp.peer_groups.[].ttl_maximum_hops") | Integer |  |  | Min: 0<br>Max: 254 | Maximum number of hops. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_filter</samp>](## "router_bgp.peer_groups.[].peer_filter") <span style="color:red">removed</span> | String |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>router_bgp.listen_ranges[].peer_filter</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_listen_range_prefix</samp>](## "router_bgp.peer_groups.[].bgp_listen_range_prefix") <span style="color:red">removed</span> | String |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>router_bgp.listen_ranges[].bgp_listen_range_prefix</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;neighbors</samp>](## "router_bgp.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "router_bgp.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp>](## "router_bgp.neighbors.[].peer_group") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "router_bgp.neighbors.[].remote_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "router_bgp.neighbors.[].local_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as_path</samp>](## "router_bgp.neighbors.[].as_path") | Dictionary |  |  |  | BGP AS-PATH options. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as_replace_out</samp>](## "router_bgp.neighbors.[].as_path.remote_as_replace_out") | Boolean |  |  |  | Replace AS number with local AS number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prepend_own_disabled</samp>](## "router_bgp.neighbors.[].as_path.prepend_own_disabled") | Boolean |  |  |  | Disable prepending own AS number to AS path. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "router_bgp.neighbors.[].peer") | String |  |  |  | Key only used for documentation or validation purposes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "router_bgp.neighbors.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_reflector_client</samp>](## "router_bgp.neighbors.[].route_reflector_client") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "router_bgp.neighbors.[].password") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;passive</samp>](## "router_bgp.neighbors.[].passive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "router_bgp.neighbors.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_source</samp>](## "router_bgp.neighbors.[].update_source") | String |  |  |  | Source Interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "router_bgp.neighbors.[].bfd") | Boolean |  |  |  | Enable BFD. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd_timers</samp>](## "router_bgp.neighbors.[].bfd_timers") | Dictionary |  |  |  | Override default BFD timers. BFD must be enabled with `bfd: true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "router_bgp.neighbors.[].bfd_timers.interval") | Integer | Required |  | Min: 50<br>Max: 60000 | Interval in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp>](## "router_bgp.neighbors.[].bfd_timers.min_rx") | Integer | Required |  | Min: 50<br>Max: 60000 | Rate in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "router_bgp.neighbors.[].bfd_timers.multiplier") | Integer | Required |  | Min: 3<br>Max: 50 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "router_bgp.neighbors.[].weight") | Integer |  |  | Min: 0<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "router_bgp.neighbors.[].timers") | String |  |  |  | BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "router_bgp.neighbors.[].default_originate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.neighbors.[].default_originate.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "router_bgp.neighbors.[].default_originate.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.neighbors.[].default_originate.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_community</samp>](## "router_bgp.neighbors.[].send_community") | String |  |  |  | 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "router_bgp.neighbors.[].maximum_routes") | Integer |  |  | Min: 0<br>Max: 4294967294 | Maximum number of routes (0 means unlimited). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_limit</samp>](## "router_bgp.neighbors.[].maximum_routes_warning_limit") | String |  |  |  | Maximum number of routes after which a warning is issued (0 means never warn) or<br>Percentage of maximum number of routes at which to warn ("<1-100> percent").<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_only</samp>](## "router_bgp.neighbors.[].maximum_routes_warning_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.neighbors.[].missing_policy") | Dictionary |  |  |  | Missing policy configuration for all address-families. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in</samp>](## "router_bgp.neighbors.[].missing_policy.direction_in") | Dictionary |  |  |  | Missing policy inbound direction. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "router_bgp.neighbors.[].missing_policy.direction_in.action") | String | Required |  | Valid Values:<br>- <code>deny</code><br>- <code>permit</code><br>- <code>deny-in-out</code> | Missing policy action. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_community_list</samp>](## "router_bgp.neighbors.[].missing_policy.direction_in.include_community_list") | Boolean |  |  |  | Include community-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_prefix_list</samp>](## "router_bgp.neighbors.[].missing_policy.direction_in.include_prefix_list") | Boolean |  |  |  | Include prefix-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_sub_route_map</samp>](## "router_bgp.neighbors.[].missing_policy.direction_in.include_sub_route_map") | Boolean |  |  |  | Include sub-route-map references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out</samp>](## "router_bgp.neighbors.[].missing_policy.direction_out") | Dictionary |  |  |  | Missing policy outbound direction. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "router_bgp.neighbors.[].missing_policy.direction_out.action") | String | Required |  | Valid Values:<br>- <code>deny</code><br>- <code>permit</code><br>- <code>deny-in-out</code> | Missing policy action. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_community_list</samp>](## "router_bgp.neighbors.[].missing_policy.direction_out.include_community_list") | Boolean |  |  |  | Include community-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_prefix_list</samp>](## "router_bgp.neighbors.[].missing_policy.direction_out.include_prefix_list") | Boolean |  |  |  | Include prefix-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_sub_route_map</samp>](## "router_bgp.neighbors.[].missing_policy.direction_out.include_sub_route_map") | Boolean |  |  |  | Include sub-route-map references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allowas_in</samp>](## "router_bgp.neighbors.[].allowas_in") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.neighbors.[].allowas_in.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;times</samp>](## "router_bgp.neighbors.[].allowas_in.times") | Integer |  |  | Min: 1<br>Max: 10 | Number of local ASNs allowed in a BGP update. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp_multihop</samp>](## "router_bgp.neighbors.[].ebgp_multihop") | Integer |  |  | Min: 1<br>Max: 255 | Time-to-live in range of hops. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp>](## "router_bgp.neighbors.[].next_hop_self") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_bandwidth</samp>](## "router_bgp.neighbors.[].link_bandwidth") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.neighbors.[].link_bandwidth.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "router_bgp.neighbors.[].link_bandwidth.default") | String |  |  |  | nn.nn(K|M|G) link speed in bits/second. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rib_in_pre_policy_retain</samp>](## "router_bgp.neighbors.[].rib_in_pre_policy_retain") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.neighbors.[].rib_in_pre_policy_retain.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "router_bgp.neighbors.[].rib_in_pre_policy_retain.all") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as</samp>](## "router_bgp.neighbors.[].remove_private_as") | Dictionary |  |  |  | Remove private AS numbers in outbound AS path. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.neighbors.[].remove_private_as.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "router_bgp.neighbors.[].remove_private_as.all") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "router_bgp.neighbors.[].remove_private_as.replace_as") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as_ingress</samp>](## "router_bgp.neighbors.[].remove_private_as_ingress") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.neighbors.[].remove_private_as_ingress.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "router_bgp.neighbors.[].remove_private_as_ingress.replace_as") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session_tracker</samp>](## "router_bgp.neighbors.[].session_tracker") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shared_secret</samp>](## "router_bgp.neighbors.[].shared_secret") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "router_bgp.neighbors.[].shared_secret.profile") | String | Required |  |  | Name of profile defined under `management_security`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "router_bgp.neighbors.[].shared_secret.hash_algorithm") | String | Required |  | Valid Values:<br>- <code>aes-128-cmac-96</code><br>- <code>hmac-sha-256</code><br>- <code>hmac-sha1-96</code> | Note: Algorithm hmac-sha-256 requires EOS version 4.31.1F and above. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl_maximum_hops</samp>](## "router_bgp.neighbors.[].ttl_maximum_hops") | Integer |  |  | Min: 0<br>Max: 254 | Maximum number of hops. |
    | [<samp>&nbsp;&nbsp;neighbor_interfaces</samp>](## "router_bgp.neighbor_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_bgp.neighbor_interfaces.[].name") | String | Required, Unique |  |  | Interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "router_bgp.neighbor_interfaces.[].remote_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "router_bgp.neighbor_interfaces.[].peer") | String |  |  |  | Key only used for documentation or validation purposes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp>](## "router_bgp.neighbor_interfaces.[].peer_group") | String |  | `Peer-group name` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "router_bgp.neighbor_interfaces.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_filter</samp>](## "router_bgp.neighbor_interfaces.[].peer_filter") | String |  |  |  | Peer-filter name. |
    | [<samp>&nbsp;&nbsp;aggregate_addresses</samp>](## "router_bgp.aggregate_addresses") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "router_bgp.aggregate_addresses.[].prefix") | String | Required, Unique |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;advertise_only</samp>](## "router_bgp.aggregate_addresses.[].advertise_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as_set</samp>](## "router_bgp.aggregate_addresses.[].as_set") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summary_only</samp>](## "router_bgp.aggregate_addresses.[].summary_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;attribute_map</samp>](## "router_bgp.aggregate_addresses.[].attribute_map") | String |  |  |  | Route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_map</samp>](## "router_bgp.aggregate_addresses.[].match_map") | String |  |  |  | Route-map name. |
    | [<samp>&nbsp;&nbsp;redistribute</samp>](## "router_bgp.redistribute") | Dictionary |  |  |  | Redistribute routes in to BGP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;attached_host</samp>](## "router_bgp.redistribute.attached_host") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.redistribute.attached_host.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.redistribute.attached_host.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.redistribute.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.redistribute.bgp.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.redistribute.bgp.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;connected</samp>](## "router_bgp.redistribute.connected") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.redistribute.connected.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.redistribute.connected.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.redistribute.connected.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.redistribute.connected.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dynamic</samp>](## "router_bgp.redistribute.dynamic") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.redistribute.dynamic.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.redistribute.dynamic.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.redistribute.dynamic.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis</samp>](## "router_bgp.redistribute.isis") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.redistribute.isis.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_level</samp>](## "router_bgp.redistribute.isis.isis_level") | String |  |  | Valid Values:<br>- <code>level-1</code><br>- <code>level-2</code><br>- <code>level-1-2</code> | Redistribute IS-IS route level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.redistribute.isis.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.redistribute.isis.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.redistribute.isis.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "router_bgp.redistribute.ospf") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.redistribute.ospf.enabled") | Boolean |  |  |  | Redistribute OSPF routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_external</samp>](## "router_bgp.redistribute.ospf.match_external") | Dictionary |  |  |  | Redistribute OSPF routes learned from external sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.redistribute.ospf.match_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.redistribute.ospf.match_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.redistribute.ospf.match_external.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_internal</samp>](## "router_bgp.redistribute.ospf.match_internal") | Dictionary |  |  |  | Redistribute OSPF routes learned from internal sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.redistribute.ospf.match_internal.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.redistribute.ospf.match_internal.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.redistribute.ospf.match_internal.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_nssa_external</samp>](## "router_bgp.redistribute.ospf.match_nssa_external") | Dictionary |  |  |  | Redistribute OSPF routes learned from external NSSA sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.redistribute.ospf.match_nssa_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nssa_type</samp>](## "router_bgp.redistribute.ospf.match_nssa_external.nssa_type") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code> | NSSA External Type Number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.redistribute.ospf.match_nssa_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.redistribute.ospf.match_nssa_external.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.redistribute.ospf.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.redistribute.ospf.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospfv3</samp>](## "router_bgp.redistribute.ospfv3") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.redistribute.ospfv3.enabled") | Boolean |  |  |  | Redistribute OSPFv3 routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_external</samp>](## "router_bgp.redistribute.ospfv3.match_external") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from external sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.redistribute.ospfv3.match_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.redistribute.ospfv3.match_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.redistribute.ospfv3.match_external.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_internal</samp>](## "router_bgp.redistribute.ospfv3.match_internal") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from internal sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.redistribute.ospfv3.match_internal.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.redistribute.ospfv3.match_internal.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.redistribute.ospfv3.match_internal.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_nssa_external</samp>](## "router_bgp.redistribute.ospfv3.match_nssa_external") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from external NSSA sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.redistribute.ospfv3.match_nssa_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nssa_type</samp>](## "router_bgp.redistribute.ospfv3.match_nssa_external.nssa_type") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code> | NSSA External Type Number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.redistribute.ospfv3.match_nssa_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.redistribute.ospfv3.match_nssa_external.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.redistribute.ospfv3.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.redistribute.ospfv3.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rip</samp>](## "router_bgp.redistribute.rip") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.redistribute.rip.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.redistribute.rip.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "router_bgp.redistribute.static") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.redistribute.static.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.redistribute.static.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.redistribute.static.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.redistribute.static.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;user</samp>](## "router_bgp.redistribute.user") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.redistribute.user.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.redistribute.user.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;redistribute_routes</samp>](## "router_bgp.redistribute_routes") <span style="color:red">deprecated</span> | List, items: Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>redistribute</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;source_protocol</samp>](## "router_bgp.redistribute_routes.[].source_protocol") | String | Required |  | Valid Values:<br>- <code>attached-host</code><br>- <code>bgp</code><br>- <code>connected</code><br>- <code>dynamic</code><br>- <code>isis</code><br>- <code>ospf</code><br>- <code>ospfv3</code><br>- <code>rip</code><br>- <code>static</code><br>- <code>user</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.redistribute_routes.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.redistribute_routes.[].rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.<br>Only applicable if `source_protocol` is one of `connected`, `static`, `isis`, `user`, `dynamic`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.redistribute_routes.[].include_leaked") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf_route_type</samp>](## "router_bgp.redistribute_routes.[].ospf_route_type") | String |  |  | Valid Values:<br>- <code>external</code><br>- <code>internal</code><br>- <code>nssa-external</code><br>- <code>nssa-external 1</code><br>- <code>nssa-external 2</code> | Routes learned by the OSPF protocol.<br>The `ospf_route_type` is valid for source_protocols 'ospf' and 'ospfv3'.<br> |
    | [<samp>&nbsp;&nbsp;vlan_aware_bundles</samp>](## "router_bgp.vlan_aware_bundles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_bgp.vlan_aware_bundles.[].name") | String | Required, Unique |  |  | VLAN aware bundle name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenant</samp>](## "router_bgp.vlan_aware_bundles.[].tenant") | String |  |  |  | Key only used for documentation or validation purposes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "router_bgp.vlan_aware_bundles.[].description") | String |  |  |  | Key only used for documentation or validation purposes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd</samp>](## "router_bgp.vlan_aware_bundles.[].rd") | String |  |  |  | Route distinguisher. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd_evpn_domain</samp>](## "router_bgp.vlan_aware_bundles.[].rd_evpn_domain") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain</samp>](## "router_bgp.vlan_aware_bundles.[].rd_evpn_domain.domain") | String |  |  | Valid Values:<br>- <code>remote</code><br>- <code>all</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd</samp>](## "router_bgp.vlan_aware_bundles.[].rd_evpn_domain.rd") | String |  |  |  | Route distinguisher. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_targets</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;both</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.both") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.both.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.import") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.import.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;export</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.export") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.export.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_evpn_domains</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.import_evpn_domains") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;domain</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.import_evpn_domains.[].domain") | String |  |  | Valid Values:<br>- <code>remote</code><br>- <code>all</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.import_evpn_domains.[].route_target") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;export_evpn_domains</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.export_evpn_domains") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;domain</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.export_evpn_domains.[].domain") | String |  |  | Valid Values:<br>- <code>remote</code><br>- <code>all</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.export_evpn_domains.[].route_target") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_export_evpn_domains</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.import_export_evpn_domains") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;domain</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.import_export_evpn_domains.[].domain") | String |  |  | Valid Values:<br>- <code>remote</code><br>- <code>all</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "router_bgp.vlan_aware_bundles.[].route_targets.import_export_evpn_domains.[].route_target") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_routes</samp>](## "router_bgp.vlan_aware_bundles.[].redistribute_routes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "router_bgp.vlan_aware_bundles.[].redistribute_routes.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_redistribute_routes</samp>](## "router_bgp.vlan_aware_bundles.[].no_redistribute_routes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "router_bgp.vlan_aware_bundles.[].no_redistribute_routes.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "router_bgp.vlan_aware_bundles.[].vlan") | String |  |  |  | VLAN range as string. Example "100-200,300". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "router_bgp.vlan_aware_bundles.[].eos_cli") | String |  |  |  | Multiline EOS CLI rendered directly on the Router BGP, VLAN-aware-bundle definition in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;vlans</samp>](## "router_bgp.vlans") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "router_bgp.vlans.[].id") | Integer | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenant</samp>](## "router_bgp.vlans.[].tenant") | String |  |  |  | Key only used for documentation or validation purposes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd</samp>](## "router_bgp.vlans.[].rd") | String |  |  |  | Route distinguisher. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd_evpn_domain</samp>](## "router_bgp.vlans.[].rd_evpn_domain") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain</samp>](## "router_bgp.vlans.[].rd_evpn_domain.domain") | String |  |  | Valid Values:<br>- <code>remote</code><br>- <code>all</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd</samp>](## "router_bgp.vlans.[].rd_evpn_domain.rd") | String |  |  |  | Route distinguisher. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_targets</samp>](## "router_bgp.vlans.[].route_targets") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;both</samp>](## "router_bgp.vlans.[].route_targets.both") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "router_bgp.vlans.[].route_targets.both.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import</samp>](## "router_bgp.vlans.[].route_targets.import") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "router_bgp.vlans.[].route_targets.import.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;export</samp>](## "router_bgp.vlans.[].route_targets.export") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "router_bgp.vlans.[].route_targets.export.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_evpn_domains</samp>](## "router_bgp.vlans.[].route_targets.import_evpn_domains") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;domain</samp>](## "router_bgp.vlans.[].route_targets.import_evpn_domains.[].domain") | String |  |  | Valid Values:<br>- <code>remote</code><br>- <code>all</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "router_bgp.vlans.[].route_targets.import_evpn_domains.[].route_target") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;export_evpn_domains</samp>](## "router_bgp.vlans.[].route_targets.export_evpn_domains") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;domain</samp>](## "router_bgp.vlans.[].route_targets.export_evpn_domains.[].domain") | String |  |  | Valid Values:<br>- <code>remote</code><br>- <code>all</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "router_bgp.vlans.[].route_targets.export_evpn_domains.[].route_target") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_export_evpn_domains</samp>](## "router_bgp.vlans.[].route_targets.import_export_evpn_domains") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;domain</samp>](## "router_bgp.vlans.[].route_targets.import_export_evpn_domains.[].domain") | String |  |  | Valid Values:<br>- <code>remote</code><br>- <code>all</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "router_bgp.vlans.[].route_targets.import_export_evpn_domains.[].route_target") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_routes</samp>](## "router_bgp.vlans.[].redistribute_routes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "router_bgp.vlans.[].redistribute_routes.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_redistribute_routes</samp>](## "router_bgp.vlans.[].no_redistribute_routes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "router_bgp.vlans.[].no_redistribute_routes.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "router_bgp.vlans.[].eos_cli") | String |  |  |  | Multiline EOS CLI rendered directly on the Router BGP, VLAN definition in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;vpws</samp>](## "router_bgp.vpws") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_bgp.vpws.[].name") | String | Required, Unique |  |  | VPWS instance name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd</samp>](## "router_bgp.vpws.[].rd") | String |  |  |  | Route distinguisher. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_targets</samp>](## "router_bgp.vpws.[].route_targets") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_export</samp>](## "router_bgp.vpws.[].route_targets.import_export") | String |  |  |  | Route Target. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_control_word</samp>](## "router_bgp.vpws.[].mpls_control_word") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;label_flow</samp>](## "router_bgp.vpws.[].label_flow") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "router_bgp.vpws.[].mtu") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pseudowires</samp>](## "router_bgp.vpws.[].pseudowires") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_bgp.vpws.[].pseudowires.[].name") | String | Required, Unique |  |  | Pseudowire name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id_local</samp>](## "router_bgp.vpws.[].pseudowires.[].id_local") | Integer |  |  |  | Must match id_remote on other pe. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id_remote</samp>](## "router_bgp.vpws.[].pseudowires.[].id_remote") | Integer |  |  |  | Must match id_local on other pe. |
    | [<samp>&nbsp;&nbsp;address_family_evpn</samp>](## "router_bgp.address_family_evpn") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;domain_identifier</samp>](## "router_bgp.address_family_evpn.domain_identifier") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbor_default</samp>](## "router_bgp.address_family_evpn.neighbor_default") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation</samp>](## "router_bgp.address_family_evpn.neighbor_default.encapsulation") | String |  |  | Valid Values:<br>- <code>vxlan</code><br>- <code>mpls</code><br>- <code>path-selection</code> | Transport encapsulation for neighbor. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self_source_interface</samp>](## "router_bgp.address_family_evpn.neighbor_default.next_hop_self_source_interface") | String |  |  |  | Source interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self_received_evpn_routes</samp>](## "router_bgp.address_family_evpn.neighbor_default.next_hop_self_received_evpn_routes") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "router_bgp.address_family_evpn.neighbor_default.next_hop_self_received_evpn_routes.enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inter_domain</samp>](## "router_bgp.address_family_evpn.neighbor_default.next_hop_self_received_evpn_routes.inter_domain") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;next_hop_mpls_resolution_ribs</samp>](## "router_bgp.address_family_evpn.next_hop_mpls_resolution_ribs") | List, items: Dictionary |  |  | Min Length: 1<br>Max Length: 3 | Specify the RIBs used to resolve MPLS next-hops. The order of this list determines the order of RIB lookups. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;rib_type</samp>](## "router_bgp.address_family_evpn.next_hop_mpls_resolution_ribs.[].rib_type") | String | Required |  | Valid Values:<br>- <code>system-connected</code><br>- <code>tunnel-rib-colored</code><br>- <code>tunnel-rib</code> | Type of RIB. For 'tunnel-rib', use 'rib_name' to specify the name of the Tunnel-RIB to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rib_name</samp>](## "router_bgp.address_family_evpn.next_hop_mpls_resolution_ribs.[].rib_name") | String |  |  |  | The name of the tunnel-rib to use when using 'tunnel-rib' type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.address_family_evpn.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "router_bgp.address_family_evpn.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_evpn.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_in</samp>](## "router_bgp.address_family_evpn.neighbors.[].rcf_in") | String |  |  |  | Inbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_out</samp>](## "router_bgp.address_family_evpn.neighbors.[].rcf_out") | String |  |  |  | Outbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_route</samp>](## "router_bgp.address_family_evpn.neighbors.[].default_route") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_evpn.neighbors.[].default_route.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.address_family_evpn.neighbors.[].default_route.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_evpn.neighbors.[].default_route.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.address_family_evpn.neighbors.[].additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.address_family_evpn.neighbors.[].additional_paths.receive") | Boolean |  |  |  | Enable or disable reception of additional-paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send</samp>](## "router_bgp.address_family_evpn.neighbors.[].additional_paths.send") | String |  |  | Valid Values:<br>- <code>any</code><br>- <code>backup</code><br>- <code>ecmp</code><br>- <code>limit</code><br>- <code>disabled</code> | Select an option to send multiple paths for same prefix through bgp updates.<br>any: Send any eligible path.<br>backup: Best path and installed backup path.<br>ecmp: All paths in best path ECMP group.<br>limit: Limit to n eligible paths.<br>disabled: Disable sending any paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_limit</samp>](## "router_bgp.address_family_evpn.neighbors.[].additional_paths.send_limit") | Integer |  |  | Min: 2<br>Max: 64 | Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation</samp>](## "router_bgp.address_family_evpn.neighbors.[].encapsulation") | String |  |  | Valid Values:<br>- <code>vxlan</code><br>- <code>mpls</code><br>- <code>path-selection</code> | Transport encapsulation for the neighbor. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_evpn.peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_bgp.address_family_evpn.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_evpn.peer_groups.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_evpn.peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_evpn.peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_in</samp>](## "router_bgp.address_family_evpn.peer_groups.[].rcf_in") | String |  |  |  | Inbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_out</samp>](## "router_bgp.address_family_evpn.peer_groups.[].rcf_out") | String |  |  |  | Outbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_route</samp>](## "router_bgp.address_family_evpn.peer_groups.[].default_route") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_evpn.peer_groups.[].default_route.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.address_family_evpn.peer_groups.[].default_route.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_evpn.peer_groups.[].default_route.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain_remote</samp>](## "router_bgp.address_family_evpn.peer_groups.[].domain_remote") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation</samp>](## "router_bgp.address_family_evpn.peer_groups.[].encapsulation") | String |  |  | Valid Values:<br>- <code>vxlan</code><br>- <code>mpls</code><br>- <code>path-selection</code> | Transport encapsulation for the peer-group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.address_family_evpn.peer_groups.[].additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.address_family_evpn.peer_groups.[].additional_paths.receive") | Boolean |  |  |  | Enable or disable reception of additional-paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send</samp>](## "router_bgp.address_family_evpn.peer_groups.[].additional_paths.send") | String |  |  | Valid Values:<br>- <code>any</code><br>- <code>backup</code><br>- <code>ecmp</code><br>- <code>limit</code><br>- <code>disabled</code> | Select an option to send multiple paths for same prefix through bgp updates.<br>any: Send any eligible path.<br>backup: Best path and installed backup path.<br>ecmp: All paths in best path ECMP group.<br>limit: Limit to n eligible paths.<br>disabled: Disable sending any paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_limit</samp>](## "router_bgp.address_family_evpn.peer_groups.[].additional_paths.send_limit") | Integer |  |  | Min: 2<br>Max: 64 | Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_hostflap_detection</samp>](## "router_bgp.address_family_evpn.evpn_hostflap_detection") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_evpn.evpn_hostflap_detection.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;window</samp>](## "router_bgp.address_family_evpn.evpn_hostflap_detection.window") | Integer |  |  | Min: 0<br>Max: 4294967295 | Time (in seconds) to detect a MAC duplication issue. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "router_bgp.address_family_evpn.evpn_hostflap_detection.threshold") | Integer |  |  | Min: 0<br>Max: 4294967295 | Minimum number of MAC moves that indicate a MAC Duplication issue. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expiry_timeout</samp>](## "router_bgp.address_family_evpn.evpn_hostflap_detection.expiry_timeout") | Integer |  |  | Min: 0<br>Max: 4294967295 | Time (in seconds) to purge a MAC duplication issue. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;next_hop</samp>](## "router_bgp.address_family_evpn.next_hop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;resolution_disabled</samp>](## "router_bgp.address_family_evpn.next_hop.resolution_disabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;route</samp>](## "router_bgp.address_family_evpn.route") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_match_failure_action</samp>](## "router_bgp.address_family_evpn.route.import_match_failure_action") | String |  |  | Valid Values:<br>- <code>discard</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_ethernet_segment_ip_mass_withdraw</samp>](## "router_bgp.address_family_evpn.route.import_ethernet_segment_ip_mass_withdraw") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_overlay_index_gateway</samp>](## "router_bgp.address_family_evpn.route.import_overlay_index_gateway") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;export_ethernet_segment_ip_mass_withdraw</samp>](## "router_bgp.address_family_evpn.route.export_ethernet_segment_ip_mass_withdraw") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;next_hop_unchanged</samp>](## "router_bgp.address_family_evpn.next_hop_unchanged") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.address_family_evpn.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.address_family_evpn.bgp.additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.address_family_evpn.bgp.additional_paths.receive") | Boolean |  |  |  | Enable or disable reception of additional-paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send</samp>](## "router_bgp.address_family_evpn.bgp.additional_paths.send") | String |  |  | Valid Values:<br>- <code>any</code><br>- <code>backup</code><br>- <code>ecmp</code><br>- <code>limit</code><br>- <code>disabled</code> | Select an option to send multiple paths for same prefix through bgp updates.<br>any: Send any eligible path.<br>backup: Best path and installed backup path.<br>ecmp: All paths in best path ECMP group.<br>limit: Limit to n eligible paths.<br>disabled: Disable sending any paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_limit</samp>](## "router_bgp.address_family_evpn.bgp.additional_paths.send_limit") | Integer |  |  | Min: 2<br>Max: 64 | Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;layer_2_fec_in_place_update</samp>](## "router_bgp.address_family_evpn.layer_2_fec_in_place_update") | Dictionary |  |  |  | BGP layer-2 in-place FEC operation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_evpn.layer_2_fec_in_place_update.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "router_bgp.address_family_evpn.layer_2_fec_in_place_update.timeout") | Integer |  |  | Min: 0<br>Max: 300 | In-place FEC update tracking timeout in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_additional_paths</samp>](## "router_bgp.address_family_evpn.bgp_additional_paths") <span style="color:red">deprecated</span> | Dictionary |  |  |  | BGP additional-paths commands.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>bgp.additional_paths</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.address_family_evpn.bgp_additional_paths.receive") | Boolean |  |  |  | Receive multiple paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send</samp>](## "router_bgp.address_family_evpn.bgp_additional_paths.send") | Dictionary |  |  |  | Send multiple paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;any</samp>](## "router_bgp.address_family_evpn.bgp_additional_paths.send.any") | Boolean |  |  |  | Any eligible path. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;backup</samp>](## "router_bgp.address_family_evpn.bgp_additional_paths.send.backup") | Boolean |  |  |  | Best path and installed backup path. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ecmp</samp>](## "router_bgp.address_family_evpn.bgp_additional_paths.send.ecmp") | Boolean |  |  |  | All paths in best path ECMP group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ecmp_limit</samp>](## "router_bgp.address_family_evpn.bgp_additional_paths.send.ecmp_limit") | Integer |  |  | Min: 2<br>Max: 64 | Amount of ECMP paths to send. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;limit</samp>](## "router_bgp.address_family_evpn.bgp_additional_paths.send.limit") | Integer |  |  | Min: 2<br>Max: 64 | Amount of paths to send. |
    | [<samp>&nbsp;&nbsp;address_family_rtc</samp>](## "router_bgp.address_family_rtc") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_rtc.peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_bgp.address_family_rtc.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_rtc.peer_groups.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_route_target</samp>](## "router_bgp.address_family_rtc.peer_groups.[].default_route_target") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;only</samp>](## "router_bgp.address_family_rtc.peer_groups.[].default_route_target.only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encoding_origin_as_omit</samp>](## "router_bgp.address_family_rtc.peer_groups.[].default_route_target.encoding_origin_as_omit") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;address_family_ipv4</samp>](## "router_bgp.address_family_ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;networks</samp>](## "router_bgp.address_family_ipv4.networks") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "router_bgp.address_family_ipv4.networks.[].prefix") | String | Required, Unique |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4.networks.[].route_map") | String |  |  |  | Route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.address_family_ipv4.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.address_family_ipv4.bgp.additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;install</samp>](## "router_bgp.address_family_ipv4.bgp.additional_paths.install") | Boolean |  |  |  | Install BGP backup path. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;install_ecmp_primary</samp>](## "router_bgp.address_family_ipv4.bgp.additional_paths.install_ecmp_primary") | Boolean |  |  |  | Allow additional path with ECMP primary path. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.address_family_ipv4.bgp.additional_paths.receive") | Boolean |  |  |  | Enable or disable reception of additional-paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send</samp>](## "router_bgp.address_family_ipv4.bgp.additional_paths.send") | String |  |  | Valid Values:<br>- <code>any</code><br>- <code>backup</code><br>- <code>ecmp</code><br>- <code>limit</code><br>- <code>disabled</code> | Select an option to send multiple paths for same prefix through bgp updates.<br>any: Send any eligible path.<br>backup: Best path and installed backup path.<br>ecmp: All paths in best path ECMP group.<br>limit: Limit to n eligible paths.<br>disabled: Disable sending any paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_limit</samp>](## "router_bgp.address_family_ipv4.bgp.additional_paths.send_limit") | Integer |  |  | Min: 2<br>Max: 64 | Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_internal</samp>](## "router_bgp.address_family_ipv4.bgp.redistribute_internal") | Boolean |  |  |  | Allow redistribution of iBGP routes into an Interior Gateway Protocol (IGP). EOS default is true. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_ipv4.peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_in</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].rcf_in") | String |  |  |  | Inbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_out</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].rcf_out") | String |  |  |  | Outbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].default_originate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].default_originate.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].default_originate.route_map") | String |  |  |  | Route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].prefix_list_in") | String |  |  |  | Inbound prefix-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].prefix_list_out") | String |  |  |  | Outbound prefix-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].additional_paths.prefix_list") | String |  |  |  | Apply the configurations only to the routes matching the prefix list. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].additional_paths.receive") | Boolean |  |  |  | Enable or disable reception of additional-paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].additional_paths.send") | String |  |  | Valid Values:<br>- <code>any</code><br>- <code>backup</code><br>- <code>ecmp</code><br>- <code>limit</code><br>- <code>disabled</code> | Select an option to send multiple paths for same prefix through bgp updates.<br>any: Send any eligible path.<br>backup: Best path and installed backup path.<br>ecmp: All paths in best path ECMP group.<br>limit: Limit to n eligible paths.<br>disabled: Disable sending any paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_limit</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].additional_paths.send_limit") | Integer |  |  | Min: 2<br>Max: 64 | Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].next_hop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv6</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].next_hop.address_family_ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].next_hop.address_family_ipv6.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;originate</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].next_hop.address_family_ipv6.originate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv6_originate</samp>](## "router_bgp.address_family_ipv4.peer_groups.[].next_hop.address_family_ipv6_originate") <span style="color:red">removed</span> | Boolean |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>address_family_ipv6</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.address_family_ipv4.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "router_bgp.address_family_ipv4.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv4.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_ipv4.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_ipv4.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_in</samp>](## "router_bgp.address_family_ipv4.neighbors.[].rcf_in") | String |  |  |  | Inbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_out</samp>](## "router_bgp.address_family_ipv4.neighbors.[].rcf_out") | String |  |  |  | Outbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp>](## "router_bgp.address_family_ipv4.neighbors.[].prefix_list_in") | String |  |  |  | Inbound prefix-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp>](## "router_bgp.address_family_ipv4.neighbors.[].prefix_list_out") | String |  |  |  | Prefix-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "router_bgp.address_family_ipv4.neighbors.[].default_originate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "router_bgp.address_family_ipv4.neighbors.[].default_originate.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4.neighbors.[].default_originate.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.address_family_ipv4.neighbors.[].additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp>](## "router_bgp.address_family_ipv4.neighbors.[].additional_paths.prefix_list") | String |  |  |  | Apply the configurations only to the routes matching the prefix list. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.address_family_ipv4.neighbors.[].additional_paths.receive") | Boolean |  |  |  | Enable or disable reception of additional-paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send</samp>](## "router_bgp.address_family_ipv4.neighbors.[].additional_paths.send") | String |  |  | Valid Values:<br>- <code>any</code><br>- <code>backup</code><br>- <code>ecmp</code><br>- <code>limit</code><br>- <code>disabled</code> | Select an option to send multiple paths for same prefix through bgp updates.<br>any: Send any eligible path.<br>backup: Best path and installed backup path.<br>ecmp: All paths in best path ECMP group.<br>limit: Limit to n eligible paths.<br>disabled: Disable sending any paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_limit</samp>](## "router_bgp.address_family_ipv4.neighbors.[].additional_paths.send_limit") | Integer |  |  | Min: 2<br>Max: 64 | Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;redistribute</samp>](## "router_bgp.address_family_ipv4.redistribute") | Dictionary |  |  |  | Redistribute routes in to BGP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;attached_host</samp>](## "router_bgp.address_family_ipv4.redistribute.attached_host") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4.redistribute.attached_host.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4.redistribute.attached_host.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.address_family_ipv4.redistribute.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4.redistribute.bgp.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4.redistribute.bgp.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected</samp>](## "router_bgp.address_family_ipv4.redistribute.connected") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4.redistribute.connected.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4.redistribute.connected.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.address_family_ipv4.redistribute.connected.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.address_family_ipv4.redistribute.connected.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic</samp>](## "router_bgp.address_family_ipv4.redistribute.dynamic") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4.redistribute.dynamic.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4.redistribute.dynamic.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.address_family_ipv4.redistribute.dynamic.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis</samp>](## "router_bgp.address_family_ipv4.redistribute.isis") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4.redistribute.isis.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_level</samp>](## "router_bgp.address_family_ipv4.redistribute.isis.isis_level") | String |  |  | Valid Values:<br>- <code>level-1</code><br>- <code>level-2</code><br>- <code>level-1-2</code> | Redistribute IS-IS route level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4.redistribute.isis.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.address_family_ipv4.redistribute.isis.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.address_family_ipv4.redistribute.isis.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "router_bgp.address_family_ipv4.redistribute.ospf") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4.redistribute.ospf.enabled") | Boolean |  |  |  | Redistribute OSPF routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_external</samp>](## "router_bgp.address_family_ipv4.redistribute.ospf.match_external") | Dictionary |  |  |  | Redistribute OSPF routes learned from external sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4.redistribute.ospf.match_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4.redistribute.ospf.match_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.address_family_ipv4.redistribute.ospf.match_external.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_internal</samp>](## "router_bgp.address_family_ipv4.redistribute.ospf.match_internal") | Dictionary |  |  |  | Redistribute OSPF routes learned from internal sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4.redistribute.ospf.match_internal.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4.redistribute.ospf.match_internal.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.address_family_ipv4.redistribute.ospf.match_internal.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_nssa_external</samp>](## "router_bgp.address_family_ipv4.redistribute.ospf.match_nssa_external") | Dictionary |  |  |  | Redistribute OSPF routes learned from external NSSA sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4.redistribute.ospf.match_nssa_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nssa_type</samp>](## "router_bgp.address_family_ipv4.redistribute.ospf.match_nssa_external.nssa_type") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code> | NSSA External Type Number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4.redistribute.ospf.match_nssa_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.address_family_ipv4.redistribute.ospf.match_nssa_external.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4.redistribute.ospf.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.address_family_ipv4.redistribute.ospf.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospfv3</samp>](## "router_bgp.address_family_ipv4.redistribute.ospfv3") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4.redistribute.ospfv3.enabled") | Boolean |  |  |  | Redistribute OSPFv3 routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_external</samp>](## "router_bgp.address_family_ipv4.redistribute.ospfv3.match_external") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from external sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4.redistribute.ospfv3.match_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4.redistribute.ospfv3.match_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.address_family_ipv4.redistribute.ospfv3.match_external.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_internal</samp>](## "router_bgp.address_family_ipv4.redistribute.ospfv3.match_internal") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from internal sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4.redistribute.ospfv3.match_internal.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4.redistribute.ospfv3.match_internal.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.address_family_ipv4.redistribute.ospfv3.match_internal.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_nssa_external</samp>](## "router_bgp.address_family_ipv4.redistribute.ospfv3.match_nssa_external") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from external NSSA sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4.redistribute.ospfv3.match_nssa_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nssa_type</samp>](## "router_bgp.address_family_ipv4.redistribute.ospfv3.match_nssa_external.nssa_type") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code> | NSSA External Type Number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4.redistribute.ospfv3.match_nssa_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.address_family_ipv4.redistribute.ospfv3.match_nssa_external.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4.redistribute.ospfv3.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.address_family_ipv4.redistribute.ospfv3.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rip</samp>](## "router_bgp.address_family_ipv4.redistribute.rip") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4.redistribute.rip.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4.redistribute.rip.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "router_bgp.address_family_ipv4.redistribute.static") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4.redistribute.static.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4.redistribute.static.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.address_family_ipv4.redistribute.static.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.address_family_ipv4.redistribute.static.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;user</samp>](## "router_bgp.address_family_ipv4.redistribute.user") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4.redistribute.user.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.address_family_ipv4.redistribute.user.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;redistribute_routes</samp>](## "router_bgp.address_family_ipv4.redistribute_routes") <span style="color:red">deprecated</span> | List, items: Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>redistribute</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;source_protocol</samp>](## "router_bgp.address_family_ipv4.redistribute_routes.[].source_protocol") | String | Required |  | Valid Values:<br>- <code>attached-host</code><br>- <code>bgp</code><br>- <code>connected</code><br>- <code>dynamic</code><br>- <code>isis</code><br>- <code>ospf</code><br>- <code>ospfv3</code><br>- <code>rip</code><br>- <code>static</code><br>- <code>user</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4.redistribute_routes.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.address_family_ipv4.redistribute_routes.[].include_leaked") | Boolean |  |  |  | Only applicable if `source_protocol` is one of `connected`, `static`, `isis`, `ospf`, `ospfv3`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.address_family_ipv4.redistribute_routes.[].rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.<br>Only applicable if `source_protocol` is one of `connected`, `static`, `isis`, `user`, `dynamic`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf_route_type</samp>](## "router_bgp.address_family_ipv4.redistribute_routes.[].ospf_route_type") | String |  |  | Valid Values:<br>- <code>external</code><br>- <code>internal</code><br>- <code>nssa-external</code><br>- <code>nssa-external 1</code><br>- <code>nssa-external 2</code> | Routes learned by the OSPF protocol.<br>The `ospf_route_type` is valid for source_protocols 'ospf' and 'ospfv3'.<br> |
    | [<samp>&nbsp;&nbsp;address_family_ipv4_labeled_unicast</samp>](## "router_bgp.address_family_ipv4_labeled_unicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;aigp_session</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.aigp_session") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;confederation</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.aigp_session.confederation") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.aigp_session.ebgp") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ibgp</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.aigp_session.ibgp") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.bgp.additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.bgp.additional_paths.receive") | Boolean |  |  |  | Enable or disable reception of additional-paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.bgp.additional_paths.send") | String |  |  | Valid Values:<br>- <code>any</code><br>- <code>backup</code><br>- <code>ecmp</code><br>- <code>limit</code><br>- <code>disabled</code> | Select an option to send multiple paths for same prefix through bgp updates.<br>any: Send any eligible path.<br>backup: Best path and installed backup path.<br>ecmp: All paths in best path ECMP group.<br>limit: Limit to n eligible paths.<br>disabled: Disable sending any paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_limit</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.bgp.additional_paths.send_limit") | Integer |  |  | Min: 2<br>Max: 64 | Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.bgp.missing_policy") | Dictionary |  |  |  | Missing policy configuration for all address-families. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.bgp.missing_policy.direction_in") | Dictionary |  |  |  | Missing policy inbound direction. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.bgp.missing_policy.direction_in.action") | String | Required |  | Valid Values:<br>- <code>deny</code><br>- <code>permit</code><br>- <code>deny-in-out</code> | Missing policy action. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_community_list</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.bgp.missing_policy.direction_in.include_community_list") | Boolean |  |  |  | Include community-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_prefix_list</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.bgp.missing_policy.direction_in.include_prefix_list") | Boolean |  |  |  | Include prefix-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_sub_route_map</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.bgp.missing_policy.direction_in.include_sub_route_map") | Boolean |  |  |  | Include sub-route-map references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.bgp.missing_policy.direction_out") | Dictionary |  |  |  | Missing policy outbound direction. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.bgp.missing_policy.direction_out.action") | String | Required |  | Valid Values:<br>- <code>deny</code><br>- <code>permit</code><br>- <code>deny-in-out</code> | Missing policy action. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_community_list</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.bgp.missing_policy.direction_out.include_community_list") | Boolean |  |  |  | Include community-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_prefix_list</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.bgp.missing_policy.direction_out.include_prefix_list") | Boolean |  |  |  | Include prefix-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_sub_route_map</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.bgp.missing_policy.direction_out.include_sub_route_map") | Boolean |  |  |  | Include sub-route-map references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_unchanged</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.bgp.next_hop_unchanged") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;graceful_restart</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.graceful_restart") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;label_local_termination</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.label_local_termination") | String |  |  | Valid Values:<br>- <code>explicit-null</code><br>- <code>implicit-null</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lfib_entry_installation_skipped</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.lfib_entry_installation_skipped") | Boolean |  |  |  | Skip LFIB entry installation and next hop self route advertisements. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbor_default</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbor_default") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbor_default.next_hop_self") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].additional_paths.receive") | Boolean |  |  |  | Enable or disable reception of additional-paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].additional_paths.send") | String |  |  | Valid Values:<br>- <code>any</code><br>- <code>backup</code><br>- <code>ecmp</code><br>- <code>limit</code><br>- <code>disabled</code> | Select an option to send multiple paths for same prefix through bgp updates.<br>any: Send any eligible path.<br>backup: Best path and installed backup path.<br>ecmp: All paths in best path ECMP group.<br>limit: Limit to n eligible paths.<br>disabled: Disable sending any paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_limit</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].additional_paths.send_limit") | Integer |  |  | Min: 2<br>Max: 64 | Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;aigp_session</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].aigp_session") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;graceful_restart</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].graceful_restart") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;graceful_restart_helper</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].graceful_restart_helper") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stale_route_map</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].graceful_restart_helper.stale_route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_advertised_routes</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].maximum_advertised_routes") | Integer |  |  | Min: 0<br>Max: 4294967294 | Maximum number of routes (0 means unlimited). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_advertised_routes_warning_limit</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].maximum_advertised_routes_warning_limit") | String |  |  |  | Maximum number of routes after which a warning is issued (0 means never warn) or<br>Percentage of maximum number of routes at which to warn ("<1-100> percent").<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].missing_policy") | Dictionary |  |  |  | Missing policy configuration for BGP Labeled-Unicast neighbor. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].missing_policy.direction_in") | Dictionary |  |  |  | Missing policy inbound direction. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].missing_policy.direction_in.action") | String | Required |  | Valid Values:<br>- <code>deny</code><br>- <code>permit</code><br>- <code>deny-in-out</code> | Missing policy action. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_community_list</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].missing_policy.direction_in.include_community_list") | Boolean |  |  |  | Include community-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_prefix_list</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].missing_policy.direction_in.include_prefix_list") | Boolean |  |  |  | Include prefix-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_sub_route_map</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].missing_policy.direction_in.include_sub_route_map") | Boolean |  |  |  | Include sub-route-map references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].missing_policy.direction_out") | Dictionary |  |  |  | Missing policy outbound direction. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].missing_policy.direction_out.action") | String | Required |  | Valid Values:<br>- <code>deny</code><br>- <code>permit</code><br>- <code>deny-in-out</code> | Missing policy action. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_community_list</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].missing_policy.direction_out.include_community_list") | Boolean |  |  |  | Include community-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_prefix_list</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].missing_policy.direction_out.include_prefix_list") | Boolean |  |  |  | Include prefix-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_sub_route_map</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].missing_policy.direction_out.include_sub_route_map") | Boolean |  |  |  | Include sub-route-map references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multi_path</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].multi_path") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_resolution</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].next_hop_resolution") <span style="color:red">removed</span> | Dictionary |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].next_hop_self") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self_source_interface</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].next_hop_self_source_interface") | String |  |  |  | Source interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self_v4_mapped_v6_source_interface</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].next_hop_self_v4_mapped_v6_source_interface") | String |  |  |  | v4-mapped-v6 source interface name. Takes precedence over the next_hop_self_source_interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_unchanged</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].next_hop_unchanged") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_in</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].rcf_in") | String |  |  |  | Inbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_out</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].rcf_out") | String |  |  |  | Outbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].additional_paths.receive") | Boolean |  |  |  | Enable or disable reception of additional-paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].additional_paths.send") | String |  |  | Valid Values:<br>- <code>any</code><br>- <code>backup</code><br>- <code>ecmp</code><br>- <code>limit</code><br>- <code>disabled</code> | Select an option to send multiple paths for same prefix through bgp updates.<br>any: Send any eligible path.<br>backup: Best path and installed backup path.<br>ecmp: All paths in best path ECMP group.<br>limit: Limit to n eligible paths.<br>disabled: Disable sending any paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_limit</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].additional_paths.send_limit") | Integer |  |  | Min: 2<br>Max: 64 | Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;aigp_session</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].aigp_session") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;graceful_restart</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].graceful_restart") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;graceful_restart_helper</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].graceful_restart_helper") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;stale_route_map</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].graceful_restart_helper.stale_route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_advertised_routes</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].maximum_advertised_routes") | Integer |  |  | Min: 0<br>Max: 4294967294 | Maximum number of routes (0 means unlimited). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_advertised_routes_warning_limit</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].maximum_advertised_routes_warning_limit") | String |  |  |  | Maximum number of routes after which a warning is issued (0 means never warn) or<br>Percentage of maximum number of routes at which to warn ("<1-100> percent").<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].missing_policy") | Dictionary |  |  |  | Missing policy configuration for BGP Labeled-Unicast neighbor. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].missing_policy.direction_in") | Dictionary |  |  |  | Missing policy inbound direction. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].missing_policy.direction_in.action") | String | Required |  | Valid Values:<br>- <code>deny</code><br>- <code>permit</code><br>- <code>deny-in-out</code> | Missing policy action. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_community_list</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].missing_policy.direction_in.include_community_list") | Boolean |  |  |  | Include community-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_prefix_list</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].missing_policy.direction_in.include_prefix_list") | Boolean |  |  |  | Include prefix-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_sub_route_map</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].missing_policy.direction_in.include_sub_route_map") | Boolean |  |  |  | Include sub-route-map references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].missing_policy.direction_out") | Dictionary |  |  |  | Missing policy outbound direction. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].missing_policy.direction_out.action") | String | Required |  | Valid Values:<br>- <code>deny</code><br>- <code>permit</code><br>- <code>deny-in-out</code> | Missing policy action. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_community_list</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].missing_policy.direction_out.include_community_list") | Boolean |  |  |  | Include community-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_prefix_list</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].missing_policy.direction_out.include_prefix_list") | Boolean |  |  |  | Include prefix-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_sub_route_map</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].missing_policy.direction_out.include_sub_route_map") | Boolean |  |  |  | Include sub-route-map references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multi_path</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].multi_path") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_resolution</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].next_hop_resolution") <span style="color:red">removed</span> | Dictionary |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].next_hop_self") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self_source_interface</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].next_hop_self_source_interface") | String |  |  |  | Source interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self_v4_mapped_v6_source_interface</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].next_hop_self_v4_mapped_v6_source_interface") | String |  |  |  | v4-mapped-v6 source interface name. Takes precedence over the next_hop_self_source_interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_unchanged</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].next_hop_unchanged") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_in</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].rcf_in") | String |  |  |  | Inbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_out</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].rcf_out") | String |  |  |  | Outbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;networks</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.networks") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.networks.[].prefix") | String | Required, Unique |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.networks.[].route_map") | String |  |  |  | Route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;next_hops</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.next_hops") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.next_hops.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lfib_backup_ip_forwarding</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.next_hops.[].lfib_backup_ip_forwarding") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;next_hop_resolution_ribs</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.next_hop_resolution_ribs") | List, items: Dictionary |  |  | Min Length: 1<br>Max Length: 3 | Specify the RIBs used to resolve next-hops. The order of this list determines the order of RIB lookups. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;rib_type</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.next_hop_resolution_ribs.[].rib_type") | String | Required |  | Valid Values:<br>- <code>system-connected</code><br>- <code>tunnel-rib-colored</code><br>- <code>tunnel-rib</code> | Type of RIB. For 'tunnel-rib', use 'rib_name' to specify the name of the Tunnel-RIB to use. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rib_name</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.next_hop_resolution_ribs.[].rib_name") | String |  |  |  | The name of the tunnel-rib to use when using 'tunnel-rib' type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tunnel_source_protocols</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.tunnel_source_protocols") | List, items: Dictionary |  |  | Min Length: 1<br>Max Length: 2 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;protocol</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.tunnel_source_protocols.[].protocol") | String | Required, Unique |  | Valid Values:<br>- <code>isis segment-routing</code><br>- <code>ldp</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.tunnel_source_protocols.[].rcf") | String |  |  |  | Optional RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;update_wait_for_convergence</samp>](## "router_bgp.address_family_ipv4_labeled_unicast.update_wait_for_convergence") | Boolean |  |  |  | Wait for BGP to converge before sending out any route updates. |
    | [<samp>&nbsp;&nbsp;address_family_ipv4_multicast</samp>](## "router_bgp.address_family_ipv4_multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.address_family_ipv4_multicast.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.address_family_ipv4_multicast.bgp.additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.address_family_ipv4_multicast.bgp.additional_paths.receive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_ipv4_multicast.peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_bgp.address_family_ipv4_multicast.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv4_multicast.peer_groups.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_ipv4_multicast.peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_ipv4_multicast.peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.address_family_ipv4_multicast.peer_groups.[].additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.address_family_ipv4_multicast.peer_groups.[].additional_paths.receive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.address_family_ipv4_multicast.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "router_bgp.address_family_ipv4_multicast.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv4_multicast.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_ipv4_multicast.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_ipv4_multicast.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.address_family_ipv4_multicast.neighbors.[].additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.address_family_ipv4_multicast.neighbors.[].additional_paths.receive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;redistribute</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute") | Dictionary |  |  |  | Redistribute routes in to BGP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;attached_host</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.attached_host") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.attached_host.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.attached_host.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.connected") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.connected.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.connected.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.isis") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.isis.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_level</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.isis.isis_level") | String |  |  | Valid Values:<br>- <code>level-1</code><br>- <code>level-2</code><br>- <code>level-1-2</code> | Redistribute IS-IS route level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.isis.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.isis.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.isis.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.ospf") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.ospf.enabled") | Boolean |  |  |  | Redistribute OSPF routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_external</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.ospf.match_external") | Dictionary |  |  |  | Redistribute OSPF routes learned from external sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.ospf.match_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.ospf.match_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_internal</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.ospf.match_internal") | Dictionary |  |  |  | Redistribute OSPF routes learned from internal sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.ospf.match_internal.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.ospf.match_internal.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_nssa_external</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.ospf.match_nssa_external") | Dictionary |  |  |  | Redistribute OSPF routes learned from external NSSA sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.ospf.match_nssa_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nssa_type</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.ospf.match_nssa_external.nssa_type") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code> | NSSA External Type Number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.ospf.match_nssa_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.ospf.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospfv3</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.ospfv3") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.ospfv3.enabled") | Boolean |  |  |  | Redistribute OSPFv3 routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_external</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.ospfv3.match_external") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from external sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.ospfv3.match_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.ospfv3.match_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_internal</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.ospfv3.match_internal") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from internal sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.ospfv3.match_internal.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.ospfv3.match_internal.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_nssa_external</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.ospfv3.match_nssa_external") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from external NSSA sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.ospfv3.match_nssa_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nssa_type</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.ospfv3.match_nssa_external.nssa_type") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code> | NSSA External Type Number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.ospfv3.match_nssa_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.ospfv3.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.static") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.static.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute.static.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;redistribute_routes</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute_routes") <span style="color:red">deprecated</span> | List, items: Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>redistribute</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;source_protocol</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute_routes.[].source_protocol") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute_routes.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute_routes.[].include_leaked") | Boolean |  |  |  | Only applicable if `source_protocol` is `isis`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute_routes.[].rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.<br>Only applicable if `source_protocol` is `isis`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf_route_type</samp>](## "router_bgp.address_family_ipv4_multicast.redistribute_routes.[].ospf_route_type") | String |  |  | Valid Values:<br>- <code>external</code><br>- <code>internal</code><br>- <code>nssa-external</code><br>- <code>nssa-external 1</code><br>- <code>nssa-external 2</code> | Routes learned by the OSPF protocol.<br>The `ospf_route_type` is valid for source_protocols 'ospf' and 'ospfv3'.<br> |
    | [<samp>&nbsp;&nbsp;address_family_ipv4_sr_te</samp>](## "router_bgp.address_family_ipv4_sr_te") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.address_family_ipv4_sr_te.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "router_bgp.address_family_ipv4_sr_te.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv4_sr_te.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_ipv4_sr_te.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_ipv4_sr_te.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_ipv4_sr_te.peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_bgp.address_family_ipv4_sr_te.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv4_sr_te.peer_groups.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_ipv4_sr_te.peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_ipv4_sr_te.peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;address_family_ipv6</samp>](## "router_bgp.address_family_ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;networks</samp>](## "router_bgp.address_family_ipv6.networks") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "router_bgp.address_family_ipv6.networks.[].prefix") | String | Required, Unique |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6.networks.[].route_map") | String |  |  |  | Route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.address_family_ipv6.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_internal</samp>](## "router_bgp.address_family_ipv6.bgp.redistribute_internal") | Boolean |  |  |  | Allow redistribution of iBGP routes into an Interior Gateway Protocol (IGP). EOS default is true. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.address_family_ipv6.bgp.additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;install</samp>](## "router_bgp.address_family_ipv6.bgp.additional_paths.install") | Boolean |  |  |  | Install BGP backup path. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;install_ecmp_primary</samp>](## "router_bgp.address_family_ipv6.bgp.additional_paths.install_ecmp_primary") | Boolean |  |  |  | Allow additional path with ECMP primary path. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.address_family_ipv6.bgp.additional_paths.receive") | Boolean |  |  |  | Enable or disable reception of additional-paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send</samp>](## "router_bgp.address_family_ipv6.bgp.additional_paths.send") | String |  |  | Valid Values:<br>- <code>any</code><br>- <code>backup</code><br>- <code>ecmp</code><br>- <code>limit</code><br>- <code>disabled</code> | Select an option to send multiple paths for same prefix through bgp updates.<br>any: Send any eligible path.<br>backup: Best path and installed backup path.<br>ecmp: All paths in best path ECMP group.<br>limit: Limit to n eligible paths.<br>disabled: Disable sending any paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_limit</samp>](## "router_bgp.address_family_ipv6.bgp.additional_paths.send_limit") | Integer |  |  | Min: 2<br>Max: 64 | Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_ipv6.peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_bgp.address_family_ipv6.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv6.peer_groups.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_ipv6.peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_ipv6.peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_in</samp>](## "router_bgp.address_family_ipv6.peer_groups.[].rcf_in") | String |  |  |  | Inbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_out</samp>](## "router_bgp.address_family_ipv6.peer_groups.[].rcf_out") | String |  |  |  | Outbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp>](## "router_bgp.address_family_ipv6.peer_groups.[].prefix_list_in") | String |  |  |  | Inbound prefix-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp>](## "router_bgp.address_family_ipv6.peer_groups.[].prefix_list_out") | String |  |  |  | Outbound prefix-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.address_family_ipv6.peer_groups.[].additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp>](## "router_bgp.address_family_ipv6.peer_groups.[].additional_paths.prefix_list") | String |  |  |  | Apply the configurations only to the routes matching the prefix list. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.address_family_ipv6.peer_groups.[].additional_paths.receive") | Boolean |  |  |  | Enable or disable reception of additional-paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send</samp>](## "router_bgp.address_family_ipv6.peer_groups.[].additional_paths.send") | String |  |  | Valid Values:<br>- <code>any</code><br>- <code>backup</code><br>- <code>ecmp</code><br>- <code>limit</code><br>- <code>disabled</code> | Select an option to send multiple paths for same prefix through bgp updates.<br>any: Send any eligible path.<br>backup: Best path and installed backup path.<br>ecmp: All paths in best path ECMP group.<br>limit: Limit to n eligible paths.<br>disabled: Disable sending any paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_limit</samp>](## "router_bgp.address_family_ipv6.peer_groups.[].additional_paths.send_limit") | Integer |  |  | Min: 2<br>Max: 64 | Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.address_family_ipv6.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "router_bgp.address_family_ipv6.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv6.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_ipv6.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_ipv6.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_in</samp>](## "router_bgp.address_family_ipv6.neighbors.[].rcf_in") | String |  |  |  | Inbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_out</samp>](## "router_bgp.address_family_ipv6.neighbors.[].rcf_out") | String |  |  |  | Outbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp>](## "router_bgp.address_family_ipv6.neighbors.[].prefix_list_in") | String |  |  |  | Inbound prefix-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp>](## "router_bgp.address_family_ipv6.neighbors.[].prefix_list_out") | String |  |  |  | Outbound prefix-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.address_family_ipv6.neighbors.[].additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp>](## "router_bgp.address_family_ipv6.neighbors.[].additional_paths.prefix_list") | String |  |  |  | Apply the configurations only to the routes matching the prefix list. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.address_family_ipv6.neighbors.[].additional_paths.receive") | Boolean |  |  |  | Enable or disable reception of additional-paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send</samp>](## "router_bgp.address_family_ipv6.neighbors.[].additional_paths.send") | String |  |  | Valid Values:<br>- <code>any</code><br>- <code>backup</code><br>- <code>ecmp</code><br>- <code>limit</code><br>- <code>disabled</code> | Select an option to send multiple paths for same prefix through bgp updates.<br>any: Send any eligible path.<br>backup: Best path and installed backup path.<br>ecmp: All paths in best path ECMP group.<br>limit: Limit to n eligible paths.<br>disabled: Disable sending any paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_limit</samp>](## "router_bgp.address_family_ipv6.neighbors.[].additional_paths.send_limit") | Integer |  |  | Min: 2<br>Max: 64 | Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;redistribute</samp>](## "router_bgp.address_family_ipv6.redistribute") | Dictionary |  |  |  | Redistribute routes in to BGP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;attached_host</samp>](## "router_bgp.address_family_ipv6.redistribute.attached_host") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv6.redistribute.attached_host.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6.redistribute.attached_host.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.address_family_ipv6.redistribute.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv6.redistribute.bgp.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6.redistribute.bgp.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected</samp>](## "router_bgp.address_family_ipv6.redistribute.connected") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv6.redistribute.connected.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6.redistribute.connected.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.address_family_ipv6.redistribute.connected.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.address_family_ipv6.redistribute.connected.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dhcp</samp>](## "router_bgp.address_family_ipv6.redistribute.dhcp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv6.redistribute.dhcp.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6.redistribute.dhcp.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic</samp>](## "router_bgp.address_family_ipv6.redistribute.dynamic") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv6.redistribute.dynamic.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6.redistribute.dynamic.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.address_family_ipv6.redistribute.dynamic.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis</samp>](## "router_bgp.address_family_ipv6.redistribute.isis") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv6.redistribute.isis.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_level</samp>](## "router_bgp.address_family_ipv6.redistribute.isis.isis_level") | String |  |  | Valid Values:<br>- <code>level-1</code><br>- <code>level-2</code><br>- <code>level-1-2</code> | Redistribute IS-IS route level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6.redistribute.isis.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.address_family_ipv6.redistribute.isis.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.address_family_ipv6.redistribute.isis.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospfv3</samp>](## "router_bgp.address_family_ipv6.redistribute.ospfv3") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv6.redistribute.ospfv3.enabled") | Boolean |  |  |  | Redistribute OSPFv3 routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_external</samp>](## "router_bgp.address_family_ipv6.redistribute.ospfv3.match_external") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from external sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv6.redistribute.ospfv3.match_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6.redistribute.ospfv3.match_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.address_family_ipv6.redistribute.ospfv3.match_external.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_internal</samp>](## "router_bgp.address_family_ipv6.redistribute.ospfv3.match_internal") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from internal sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv6.redistribute.ospfv3.match_internal.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6.redistribute.ospfv3.match_internal.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.address_family_ipv6.redistribute.ospfv3.match_internal.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_nssa_external</samp>](## "router_bgp.address_family_ipv6.redistribute.ospfv3.match_nssa_external") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from external NSSA sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv6.redistribute.ospfv3.match_nssa_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nssa_type</samp>](## "router_bgp.address_family_ipv6.redistribute.ospfv3.match_nssa_external.nssa_type") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code> | NSSA External Type Number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6.redistribute.ospfv3.match_nssa_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.address_family_ipv6.redistribute.ospfv3.match_nssa_external.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6.redistribute.ospfv3.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.address_family_ipv6.redistribute.ospfv3.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "router_bgp.address_family_ipv6.redistribute.static") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv6.redistribute.static.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6.redistribute.static.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.address_family_ipv6.redistribute.static.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.address_family_ipv6.redistribute.static.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;user</samp>](## "router_bgp.address_family_ipv6.redistribute.user") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv6.redistribute.user.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.address_family_ipv6.redistribute.user.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;redistribute_routes</samp>](## "router_bgp.address_family_ipv6.redistribute_routes") <span style="color:red">deprecated</span> | List, items: Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>redistribute</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;source_protocol</samp>](## "router_bgp.address_family_ipv6.redistribute_routes.[].source_protocol") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6.redistribute_routes.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.address_family_ipv6.redistribute_routes.[].include_leaked") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.address_family_ipv6.redistribute_routes.[].rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.<br>Only used if `source_protocol` is one of `connected`, `static`, `isis`, `user`, `dynamic`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf_route_type</samp>](## "router_bgp.address_family_ipv6.redistribute_routes.[].ospf_route_type") | String |  |  | Valid Values:<br>- <code>external</code><br>- <code>internal</code><br>- <code>nssa-external</code><br>- <code>nssa-external 1</code><br>- <code>nssa-external 2</code> | Routes learned by the OSPF protocol.<br>The `ospf_route_type` is valid for source_protocols 'ospfv3'.<br> |
    | [<samp>&nbsp;&nbsp;address_family_ipv6_multicast</samp>](## "router_bgp.address_family_ipv6_multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.address_family_ipv6_multicast.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.address_family_ipv6_multicast.bgp.missing_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in_action</samp>](## "router_bgp.address_family_ipv6_multicast.bgp.missing_policy.direction_in_action") | String |  |  | Valid Values:<br>- <code>deny</code><br>- <code>deny-in-out</code><br>- <code>permit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out_action</samp>](## "router_bgp.address_family_ipv6_multicast.bgp.missing_policy.direction_out_action") | String |  |  | Valid Values:<br>- <code>deny</code><br>- <code>deny-in-out</code><br>- <code>permit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.address_family_ipv6_multicast.bgp.additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.address_family_ipv6_multicast.bgp.additional_paths.receive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.address_family_ipv6_multicast.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "router_bgp.address_family_ipv6_multicast.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv6_multicast.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_ipv6_multicast.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_ipv6_multicast.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.address_family_ipv6_multicast.neighbors.[].additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.address_family_ipv6_multicast.neighbors.[].additional_paths.receive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_ipv6_multicast.peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_bgp.address_family_ipv6_multicast.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv6_multicast.peer_groups.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.address_family_ipv6_multicast.peer_groups.[].additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.address_family_ipv6_multicast.peer_groups.[].additional_paths.receive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;networks</samp>](## "router_bgp.address_family_ipv6_multicast.networks") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "router_bgp.address_family_ipv6_multicast.networks.[].prefix") | String | Required, Unique |  |  | IPv6 prefix "A:B:C:D:E:F:G:H/I". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6_multicast.networks.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;redistribute</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute") | Dictionary |  |  |  | Redistribute routes in to BGP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.connected") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.connected.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.connected.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.isis") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.isis.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_level</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.isis.isis_level") | String |  |  | Valid Values:<br>- <code>level-1</code><br>- <code>level-2</code><br>- <code>level-1-2</code> | Redistribute IS-IS route level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.isis.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.isis.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.isis.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.ospf") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.ospf.enabled") | Boolean |  |  |  | Redistribute OSPF routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_external</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.ospf.match_external") | Dictionary |  |  |  | Redistribute OSPF routes learned from external sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.ospf.match_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.ospf.match_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_internal</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.ospf.match_internal") | Dictionary |  |  |  | Redistribute OSPF routes learned from internal sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.ospf.match_internal.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.ospf.match_internal.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_nssa_external</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.ospf.match_nssa_external") | Dictionary |  |  |  | Redistribute OSPF routes learned from external NSSA sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.ospf.match_nssa_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nssa_type</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.ospf.match_nssa_external.nssa_type") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code> | NSSA External Type Number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.ospf.match_nssa_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.ospf.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospfv3</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.ospfv3") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.ospfv3.enabled") | Boolean |  |  |  | Redistribute OSPFv3 routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_external</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.ospfv3.match_external") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from external sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.ospfv3.match_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.ospfv3.match_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_internal</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.ospfv3.match_internal") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from internal sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.ospfv3.match_internal.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.ospfv3.match_internal.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_nssa_external</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.ospfv3.match_nssa_external") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from external NSSA sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.ospfv3.match_nssa_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nssa_type</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.ospfv3.match_nssa_external.nssa_type") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code> | NSSA External Type Number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.ospfv3.match_nssa_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.ospfv3.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.static") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.static.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute.static.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;redistribute_routes</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute_routes") <span style="color:red">deprecated</span> | List, items: Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>redistribute</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;source_protocol</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute_routes.[].source_protocol") | String | Required |  | Valid Values:<br>- <code>connected</code><br>- <code>isis</code><br>- <code>ospf</code><br>- <code>ospfv3</code><br>- <code>static</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute_routes.[].include_leaked") | Boolean |  |  |  | Only applicable if `source_protocol` is `isis`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute_routes.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute_routes.[].rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.<br>Only applicable if `source_protocol` is `isis`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf_route_type</samp>](## "router_bgp.address_family_ipv6_multicast.redistribute_routes.[].ospf_route_type") | String |  |  | Valid Values:<br>- <code>external</code><br>- <code>internal</code><br>- <code>nssa-external</code><br>- <code>nssa-external 1</code><br>- <code>nssa-external 2</code> | Routes learned by the OSPF protocol.<br>The `ospf_route_type` is valid for source_protocols 'ospf' and 'ospfv3'.<br> |
    | [<samp>&nbsp;&nbsp;address_family_ipv6_sr_te</samp>](## "router_bgp.address_family_ipv6_sr_te") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.address_family_ipv6_sr_te.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "router_bgp.address_family_ipv6_sr_te.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv6_sr_te.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_ipv6_sr_te.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_ipv6_sr_te.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_ipv6_sr_te.peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_bgp.address_family_ipv6_sr_te.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_ipv6_sr_te.peer_groups.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_ipv6_sr_te.peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_ipv6_sr_te.peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;address_family_link_state</samp>](## "router_bgp.address_family_link_state") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.address_family_link_state.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.address_family_link_state.bgp.missing_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in_action</samp>](## "router_bgp.address_family_link_state.bgp.missing_policy.direction_in_action") | String |  |  | Valid Values:<br>- <code>deny</code><br>- <code>deny-in-out</code><br>- <code>permit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out_action</samp>](## "router_bgp.address_family_link_state.bgp.missing_policy.direction_out_action") | String |  |  | Valid Values:<br>- <code>deny</code><br>- <code>deny-in-out</code><br>- <code>permit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_link_state.peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_bgp.address_family_link_state.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_link_state.peer_groups.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.address_family_link_state.peer_groups.[].missing_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in_action</samp>](## "router_bgp.address_family_link_state.peer_groups.[].missing_policy.direction_in_action") | String |  |  | Valid Values:<br>- <code>deny</code><br>- <code>deny-in-out</code><br>- <code>permit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out_action</samp>](## "router_bgp.address_family_link_state.peer_groups.[].missing_policy.direction_out_action") | String |  |  | Valid Values:<br>- <code>deny</code><br>- <code>deny-in-out</code><br>- <code>permit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.address_family_link_state.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "router_bgp.address_family_link_state.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_link_state.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.address_family_link_state.neighbors.[].missing_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in_action</samp>](## "router_bgp.address_family_link_state.neighbors.[].missing_policy.direction_in_action") | String |  |  | Valid Values:<br>- <code>deny</code><br>- <code>deny-in-out</code><br>- <code>permit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out_action</samp>](## "router_bgp.address_family_link_state.neighbors.[].missing_policy.direction_out_action") | String |  |  | Valid Values:<br>- <code>deny</code><br>- <code>deny-in-out</code><br>- <code>permit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;path_selection</samp>](## "router_bgp.address_family_link_state.path_selection") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;roles</samp>](## "router_bgp.address_family_link_state.path_selection.roles") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;producer</samp>](## "router_bgp.address_family_link_state.path_selection.roles.producer") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;consumer</samp>](## "router_bgp.address_family_link_state.path_selection.roles.consumer") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;propagator</samp>](## "router_bgp.address_family_link_state.path_selection.roles.propagator") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;address_family_flow_spec_ipv4</samp>](## "router_bgp.address_family_flow_spec_ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.address_family_flow_spec_ipv4.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.address_family_flow_spec_ipv4.bgp.missing_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in_action</samp>](## "router_bgp.address_family_flow_spec_ipv4.bgp.missing_policy.direction_in_action") | String |  |  | Valid Values:<br>- <code>deny</code><br>- <code>deny-in-out</code><br>- <code>permit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out_action</samp>](## "router_bgp.address_family_flow_spec_ipv4.bgp.missing_policy.direction_out_action") | String |  |  | Valid Values:<br>- <code>deny</code><br>- <code>deny-in-out</code><br>- <code>permit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.address_family_flow_spec_ipv4.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "router_bgp.address_family_flow_spec_ipv4.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_flow_spec_ipv4.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_flow_spec_ipv4.peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_bgp.address_family_flow_spec_ipv4.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_flow_spec_ipv4.peer_groups.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;address_family_flow_spec_ipv6</samp>](## "router_bgp.address_family_flow_spec_ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.address_family_flow_spec_ipv6.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.address_family_flow_spec_ipv6.bgp.missing_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in_action</samp>](## "router_bgp.address_family_flow_spec_ipv6.bgp.missing_policy.direction_in_action") | String |  |  | Valid Values:<br>- <code>deny</code><br>- <code>deny-in-out</code><br>- <code>permit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out_action</samp>](## "router_bgp.address_family_flow_spec_ipv6.bgp.missing_policy.direction_out_action") | String |  |  | Valid Values:<br>- <code>deny</code><br>- <code>deny-in-out</code><br>- <code>permit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.address_family_flow_spec_ipv6.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "router_bgp.address_family_flow_spec_ipv6.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_flow_spec_ipv6.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_flow_spec_ipv6.peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_bgp.address_family_flow_spec_ipv6.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_flow_spec_ipv6.peer_groups.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;address_family_path_selection</samp>](## "router_bgp.address_family_path_selection") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.address_family_path_selection.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.address_family_path_selection.bgp.additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.address_family_path_selection.bgp.additional_paths.receive") | Boolean |  |  |  | Enable or disable reception of additional-paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send</samp>](## "router_bgp.address_family_path_selection.bgp.additional_paths.send") | String |  |  | Valid Values:<br>- <code>any</code><br>- <code>backup</code><br>- <code>ecmp</code><br>- <code>limit</code><br>- <code>disabled</code> | Select an option to send multiple paths for same prefix through bgp updates.<br>any: Send any eligible path.<br>backup: Best path and installed backup path.<br>ecmp: All paths in best path ECMP group.<br>limit: Limit to n eligible paths.<br>disabled: Disable sending any paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_limit</samp>](## "router_bgp.address_family_path_selection.bgp.additional_paths.send_limit") | Integer |  |  | Min: 2<br>Max: 64 | Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.address_family_path_selection.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "router_bgp.address_family_path_selection.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_path_selection.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.address_family_path_selection.neighbors.[].additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.address_family_path_selection.neighbors.[].additional_paths.receive") | Boolean |  |  |  | Enable or disable reception of additional-paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send</samp>](## "router_bgp.address_family_path_selection.neighbors.[].additional_paths.send") | String |  |  | Valid Values:<br>- <code>any</code><br>- <code>backup</code><br>- <code>ecmp</code><br>- <code>limit</code><br>- <code>disabled</code> | Select an option to send multiple paths for same prefix through bgp updates.<br>any: Send any eligible path.<br>backup: Best path and installed backup path.<br>ecmp: All paths in best path ECMP group.<br>limit: Limit to n eligible paths.<br>disabled: Disable sending any paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_limit</samp>](## "router_bgp.address_family_path_selection.neighbors.[].additional_paths.send_limit") | Integer |  |  | Min: 2<br>Max: 64 | Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_path_selection.peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_bgp.address_family_path_selection.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_path_selection.peer_groups.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.address_family_path_selection.peer_groups.[].additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.address_family_path_selection.peer_groups.[].additional_paths.receive") | Boolean |  |  |  | Enable or disable reception of additional-paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send</samp>](## "router_bgp.address_family_path_selection.peer_groups.[].additional_paths.send") | String |  |  | Valid Values:<br>- <code>any</code><br>- <code>backup</code><br>- <code>ecmp</code><br>- <code>limit</code><br>- <code>disabled</code> | Select an option to send multiple paths for same prefix through bgp updates.<br>any: Send any eligible path.<br>backup: Best path and installed backup path.<br>ecmp: All paths in best path ECMP group.<br>limit: Limit to n eligible paths.<br>disabled: Disable sending any paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_limit</samp>](## "router_bgp.address_family_path_selection.peer_groups.[].additional_paths.send_limit") | Integer |  |  | Min: 2<br>Max: 64 | Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`. |
    | [<samp>&nbsp;&nbsp;address_family_vpn_ipv4</samp>](## "router_bgp.address_family_vpn_ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;domain_identifier</samp>](## "router_bgp.address_family_vpn_ipv4.domain_identifier") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_vpn_ipv4.peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_bgp.address_family_vpn_ipv4.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_vpn_ipv4.peer_groups.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_vpn_ipv4.peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_vpn_ipv4.peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_in</samp>](## "router_bgp.address_family_vpn_ipv4.peer_groups.[].rcf_in") | String |  |  |  | Inbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_out</samp>](## "router_bgp.address_family_vpn_ipv4.peer_groups.[].rcf_out") | String |  |  |  | Outbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_route</samp>](## "router_bgp.address_family_vpn_ipv4.peer_groups.[].default_route") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_vpn_ipv4.peer_groups.[].default_route.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.address_family_vpn_ipv4.peer_groups.[].default_route.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_vpn_ipv4.peer_groups.[].default_route.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;route</samp>](## "router_bgp.address_family_vpn_ipv4.route") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_match_failure_action</samp>](## "router_bgp.address_family_vpn_ipv4.route.import_match_failure_action") | String |  |  | Valid Values:<br>- <code>discard</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.address_family_vpn_ipv4.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "router_bgp.address_family_vpn_ipv4.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_vpn_ipv4.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_vpn_ipv4.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_vpn_ipv4.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_in</samp>](## "router_bgp.address_family_vpn_ipv4.neighbors.[].rcf_in") | String |  |  |  | Inbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_out</samp>](## "router_bgp.address_family_vpn_ipv4.neighbors.[].rcf_out") | String |  |  |  | Outbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_route</samp>](## "router_bgp.address_family_vpn_ipv4.neighbors.[].default_route") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_vpn_ipv4.neighbors.[].default_route.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.address_family_vpn_ipv4.neighbors.[].default_route.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_vpn_ipv4.neighbors.[].default_route.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbor_default_encapsulation_mpls_next_hop_self</samp>](## "router_bgp.address_family_vpn_ipv4.neighbor_default_encapsulation_mpls_next_hop_self") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "router_bgp.address_family_vpn_ipv4.neighbor_default_encapsulation_mpls_next_hop_self.source_interface") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;address_family_vpn_ipv6</samp>](## "router_bgp.address_family_vpn_ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;domain_identifier</samp>](## "router_bgp.address_family_vpn_ipv6.domain_identifier") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_groups</samp>](## "router_bgp.address_family_vpn_ipv6.peer_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_bgp.address_family_vpn_ipv6.peer_groups.[].name") | String | Required, Unique |  |  | Peer-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_vpn_ipv6.peer_groups.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_vpn_ipv6.peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_vpn_ipv6.peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_in</samp>](## "router_bgp.address_family_vpn_ipv6.peer_groups.[].rcf_in") | String |  |  |  | Inbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_out</samp>](## "router_bgp.address_family_vpn_ipv6.peer_groups.[].rcf_out") | String |  |  |  | Outbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_route</samp>](## "router_bgp.address_family_vpn_ipv6.peer_groups.[].default_route") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_vpn_ipv6.peer_groups.[].default_route.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.address_family_vpn_ipv6.peer_groups.[].default_route.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_vpn_ipv6.peer_groups.[].default_route.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;route</samp>](## "router_bgp.address_family_vpn_ipv6.route") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import_match_failure_action</samp>](## "router_bgp.address_family_vpn_ipv6.route.import_match_failure_action") | String |  |  | Valid Values:<br>- <code>discard</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.address_family_vpn_ipv6.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "router_bgp.address_family_vpn_ipv6.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.address_family_vpn_ipv6.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.address_family_vpn_ipv6.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.address_family_vpn_ipv6.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_in</samp>](## "router_bgp.address_family_vpn_ipv6.neighbors.[].rcf_in") | String |  |  |  | Inbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_out</samp>](## "router_bgp.address_family_vpn_ipv6.neighbors.[].rcf_out") | String |  |  |  | Outbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_route</samp>](## "router_bgp.address_family_vpn_ipv6.neighbors.[].default_route") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.address_family_vpn_ipv6.neighbors.[].default_route.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.address_family_vpn_ipv6.neighbors.[].default_route.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.address_family_vpn_ipv6.neighbors.[].default_route.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbor_default_encapsulation_mpls_next_hop_self</samp>](## "router_bgp.address_family_vpn_ipv6.neighbor_default_encapsulation_mpls_next_hop_self") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "router_bgp.address_family_vpn_ipv6.neighbor_default_encapsulation_mpls_next_hop_self.source_interface") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "router_bgp.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_bgp.vrfs.[].name") | String | Required, Unique |  |  | VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.vrfs.[].bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_internal</samp>](## "router_bgp.vrfs.[].bgp.redistribute_internal") | Boolean |  |  |  | Allow redistribution of iBGP routes into an Interior Gateway Protocol (IGP). EOS default is true. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.vrfs.[].bgp.additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;install</samp>](## "router_bgp.vrfs.[].bgp.additional_paths.install") | Boolean |  |  |  | Install BGP backup path. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;install_ecmp_primary</samp>](## "router_bgp.vrfs.[].bgp.additional_paths.install_ecmp_primary") | Boolean |  |  |  | Allow additional path with ECMP primary path. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.vrfs.[].bgp.additional_paths.receive") | Boolean |  |  |  | Enable or disable reception of additional-paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send</samp>](## "router_bgp.vrfs.[].bgp.additional_paths.send") | String |  |  | Valid Values:<br>- <code>any</code><br>- <code>backup</code><br>- <code>ecmp</code><br>- <code>limit</code><br>- <code>disabled</code> | Select an option to send multiple paths for same prefix through bgp updates.<br>any: Send any eligible path.<br>backup: Best path and installed backup path.<br>ecmp: All paths in best path ECMP group.<br>limit: Limit to n eligible paths.<br>disabled: Disable sending any paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_limit</samp>](## "router_bgp.vrfs.[].bgp.additional_paths.send_limit") | Integer |  |  | Min: 2<br>Max: 64 | Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd</samp>](## "router_bgp.vrfs.[].rd") | String |  |  |  | Route distinguisher. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_multicast</samp>](## "router_bgp.vrfs.[].evpn_multicast") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_multicast_address_family</samp>](## "router_bgp.vrfs.[].evpn_multicast_address_family") | Dictionary |  |  |  | Enable per-AF EVPN multicast settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "router_bgp.vrfs.[].evpn_multicast_address_family.ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transit</samp>](## "router_bgp.vrfs.[].evpn_multicast_address_family.ipv4.transit") | Boolean |  |  |  | Enable EVPN multicast transit mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_multicast_gateway_dr_election</samp>](## "router_bgp.vrfs.[].evpn_multicast_gateway_dr_election") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "router_bgp.vrfs.[].evpn_multicast_gateway_dr_election.algorithm") | String | Required |  | Valid Values:<br>- <code>hrw</code><br>- <code>modulus</code><br>- <code>preference</code> | DR election algorithms:<br>  hrw: Default selection based on highest random weight.<br>  modulus: Selection based on VLAN ID modulo number of candidates.<br>  preference: Selection based on a configured preference value. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preference_value</samp>](## "router_bgp.vrfs.[].evpn_multicast_gateway_dr_election.preference_value") | Integer |  |  | Min: 0<br>Max: 65535 | Required when `algorithm` is `preference`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_route_exports</samp>](## "router_bgp.vrfs.[].default_route_exports") | List, items: Dictionary |  |  |  | Enable default-originate per VRF/address-family. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;address_family</samp>](## "router_bgp.vrfs.[].default_route_exports.[].address_family") | String | Required, Unique |  | Valid Values:<br>- <code>evpn</code><br>- <code>vpn-ipv4</code><br>- <code>vpn-ipv6</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "router_bgp.vrfs.[].default_route_exports.[].always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].default_route_exports.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.vrfs.[].default_route_exports.[].rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_targets</samp>](## "router_bgp.vrfs.[].route_targets") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;import</samp>](## "router_bgp.vrfs.[].route_targets.import") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;address_family</samp>](## "router_bgp.vrfs.[].route_targets.import.[].address_family") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_targets</samp>](## "router_bgp.vrfs.[].route_targets.import.[].route_targets") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "router_bgp.vrfs.[].route_targets.import.[].route_targets.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].route_targets.import.[].route_map") | String |  |  |  | Only applicable if `address_family` is one of `evpn`, `vpn-ipv4` or `vpn-ipv6`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.vrfs.[].route_targets.import.[].rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>Only applicable if `address_family` is one of `evpn`, `vpn-ipv4` or `vpn-ipv6`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vpn_route_filter_rcf</samp>](## "router_bgp.vrfs.[].route_targets.import.[].vpn_route_filter_rcf") | String |  |  |  | RCF function name with parenthesis for filtering VPN routes. Also requires `rcf` to be set.<br>Example: MyFunction(myarg).<br>Only applicable if `address_family` is one of `vpn-ipv4` or `vpn-ipv6`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;export</samp>](## "router_bgp.vrfs.[].route_targets.export") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;address_family</samp>](## "router_bgp.vrfs.[].route_targets.export.[].address_family") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_targets</samp>](## "router_bgp.vrfs.[].route_targets.export.[].route_targets") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "router_bgp.vrfs.[].route_targets.export.[].route_targets.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].route_targets.export.[].route_map") | String |  |  |  | Only applicable if `address_family` is one of `evpn`, `vpn-ipv4` or `vpn-ipv6`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.vrfs.[].route_targets.export.[].rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>Only applicable if `address_family` is one of `evpn`, `vpn-ipv4` or `vpn-ipv6`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vpn_route_filter_rcf</samp>](## "router_bgp.vrfs.[].route_targets.export.[].vpn_route_filter_rcf") | String |  |  |  | RCF function name with parenthesis for filtering VPN routes. Also requires `rcf` to be set.<br>Example: MyFunction(myarg).<br>Only applicable if `address_family` is one of `vpn-ipv4` or `vpn-ipv6`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;router_id</samp>](## "router_bgp.vrfs.[].router_id") | String |  |  |  | in IP address format A.B.C.D. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "router_bgp.vrfs.[].timers") | String |  |  |  | BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;networks</samp>](## "router_bgp.vrfs.[].networks") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "router_bgp.vrfs.[].networks.[].prefix") | String | Required, Unique |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].networks.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_paths</samp>](## "router_bgp.vrfs.[].maximum_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;paths</samp>](## "router_bgp.vrfs.[].maximum_paths.paths") | Integer | Required |  | Min: 1<br>Max: 600 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ecmp</samp>](## "router_bgp.vrfs.[].maximum_paths.ecmp") | Integer |  |  | Min: 1<br>Max: 600 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;updates</samp>](## "router_bgp.vrfs.[].updates") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wait_for_convergence</samp>](## "router_bgp.vrfs.[].updates.wait_for_convergence") | Boolean |  |  |  | Disables FIB updates and route advertisement when the BGP instance is initiated until the BGP convergence state is reached.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wait_install</samp>](## "router_bgp.vrfs.[].updates.wait_install") | Boolean |  |  |  | Do not advertise reachability to a prefix until that prefix has been installed in hardware.<br>This will eliminate any temporary black holes due to a BGP speaker advertising reachability to a prefix that may not yet be installed into the forwarding plane.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;listen_ranges</samp>](## "router_bgp.vrfs.[].listen_ranges") | List, items: Dictionary |  |  |  | Improved "listen_ranges" data model to support multiple listen ranges and additional filter capabilities.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "router_bgp.vrfs.[].listen_ranges.[].prefix") | String |  |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_id_include_router_id</samp>](## "router_bgp.vrfs.[].listen_ranges.[].peer_id_include_router_id") | Boolean |  |  |  | Include router ID as part of peer filter. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp>](## "router_bgp.vrfs.[].listen_ranges.[].peer_group") | String |  |  |  | Peer-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_filter</samp>](## "router_bgp.vrfs.[].listen_ranges.[].peer_filter") | String |  |  |  | Peer-filter name.<br>note: `peer_filter`` or `remote_as` is required but mutually exclusive.<br>If both are defined, peer_filter takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "router_bgp.vrfs.[].listen_ranges.[].remote_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.vrfs.[].neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "router_bgp.vrfs.[].neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp>](## "router_bgp.vrfs.[].neighbors.[].peer_group") | String |  |  |  | Peer-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "router_bgp.vrfs.[].neighbors.[].remote_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "router_bgp.vrfs.[].neighbors.[].password") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;passive</samp>](## "router_bgp.vrfs.[].neighbors.[].passive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as</samp>](## "router_bgp.vrfs.[].neighbors.[].remove_private_as") | Dictionary |  |  |  | Remove private AS numbers in outbound AS path. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].neighbors.[].remove_private_as.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "router_bgp.vrfs.[].neighbors.[].remove_private_as.all") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "router_bgp.vrfs.[].neighbors.[].remove_private_as.replace_as") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as_ingress</samp>](## "router_bgp.vrfs.[].neighbors.[].remove_private_as_ingress") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].neighbors.[].remove_private_as_ingress.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "router_bgp.vrfs.[].neighbors.[].remove_private_as_ingress.replace_as") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "router_bgp.vrfs.[].neighbors.[].weight") | Integer |  |  | Min: 0<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "router_bgp.vrfs.[].neighbors.[].local_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as_path</samp>](## "router_bgp.vrfs.[].neighbors.[].as_path") | Dictionary |  |  |  | BGP AS-PATH options. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as_replace_out</samp>](## "router_bgp.vrfs.[].neighbors.[].as_path.remote_as_replace_out") | Boolean |  |  |  | Replace AS number with local AS number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prepend_own_disabled</samp>](## "router_bgp.vrfs.[].neighbors.[].as_path.prepend_own_disabled") | Boolean |  |  |  | Disable prepending own AS number to AS path. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "router_bgp.vrfs.[].neighbors.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_reflector_client</samp>](## "router_bgp.vrfs.[].neighbors.[].route_reflector_client") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp_multihop</samp>](## "router_bgp.vrfs.[].neighbors.[].ebgp_multihop") | Integer |  |  | Min: 1<br>Max: 255 | Time-to-live in range of hops. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp>](## "router_bgp.vrfs.[].neighbors.[].next_hop_self") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "router_bgp.vrfs.[].neighbors.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "router_bgp.vrfs.[].neighbors.[].bfd") | Boolean |  |  |  | Enable BFD. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd_timers</samp>](## "router_bgp.vrfs.[].neighbors.[].bfd_timers") | Dictionary |  |  |  | Override default BFD timers. BFD must be enabled with `bfd: true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "router_bgp.vrfs.[].neighbors.[].bfd_timers.interval") | Integer | Required |  | Min: 50<br>Max: 60000 | Interval in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp>](## "router_bgp.vrfs.[].neighbors.[].bfd_timers.min_rx") | Integer | Required |  | Min: 50<br>Max: 60000 | Rate in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "router_bgp.vrfs.[].neighbors.[].bfd_timers.multiplier") | Integer | Required |  | Min: 3<br>Max: 50 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "router_bgp.vrfs.[].neighbors.[].timers") | String |  |  |  | BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rib_in_pre_policy_retain</samp>](## "router_bgp.vrfs.[].neighbors.[].rib_in_pre_policy_retain") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].neighbors.[].rib_in_pre_policy_retain.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "router_bgp.vrfs.[].neighbors.[].rib_in_pre_policy_retain.all") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_community</samp>](## "router_bgp.vrfs.[].neighbors.[].send_community") | String |  |  |  | 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "router_bgp.vrfs.[].neighbors.[].maximum_routes") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_limit</samp>](## "router_bgp.vrfs.[].neighbors.[].maximum_routes_warning_limit") | String |  |  |  | Maximum number of routes after which a warning is issued (0 means never warn) or<br>Percentage of maximum number of routes at which to warn ("<1-100> percent").<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_only</samp>](## "router_bgp.vrfs.[].neighbors.[].maximum_routes_warning_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allowas_in</samp>](## "router_bgp.vrfs.[].neighbors.[].allowas_in") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].neighbors.[].allowas_in.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;times</samp>](## "router_bgp.vrfs.[].neighbors.[].allowas_in.times") | Integer |  |  | Min: 1<br>Max: 10 | Number of local ASNs allowed in a BGP update. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "router_bgp.vrfs.[].neighbors.[].default_originate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].neighbors.[].default_originate.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "router_bgp.vrfs.[].neighbors.[].default_originate.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].neighbors.[].default_originate.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_source</samp>](## "router_bgp.vrfs.[].neighbors.[].update_source") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.vrfs.[].neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.vrfs.[].neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.vrfs.[].neighbors.[].additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.vrfs.[].neighbors.[].additional_paths.receive") | Boolean |  |  |  | Enable or disable reception of additional-paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send</samp>](## "router_bgp.vrfs.[].neighbors.[].additional_paths.send") | String |  |  | Valid Values:<br>- <code>any</code><br>- <code>backup</code><br>- <code>ecmp</code><br>- <code>limit</code><br>- <code>disabled</code> | Select an option to send multiple paths for same prefix through bgp updates.<br>any: Send any eligible path.<br>backup: Best path and installed backup path.<br>ecmp: All paths in best path ECMP group.<br>limit: Limit to n eligible paths.<br>disabled: Disable sending any paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_limit</samp>](## "router_bgp.vrfs.[].neighbors.[].additional_paths.send_limit") | Integer |  |  | Min: 2<br>Max: 64 | Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp>](## "router_bgp.vrfs.[].neighbors.[].prefix_list_in") <span style="color:red">removed</span> | String |  |  |  | Inbound prefix-list name.<span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>router_bgp.vrfs[].address_family_ipv4.neighbors[].prefix_list_in or router_bgp.vrfs[].address_family_ipv6.neighbors[].prefix_list_in</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp>](## "router_bgp.vrfs.[].neighbors.[].prefix_list_out") <span style="color:red">removed</span> | String |  |  |  | Outbound prefix-list name.<span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>router_bgp.vrfs[].address_family_ipv4.neighbors[].prefix_list_out or router_bgp.vrfs[].address_family_ipv6.neighbors[].prefix_list_out</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbor_interfaces</samp>](## "router_bgp.vrfs.[].neighbor_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_bgp.vrfs.[].neighbor_interfaces.[].name") | String | Required, Unique |  |  | Interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "router_bgp.vrfs.[].neighbor_interfaces.[].remote_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp>](## "router_bgp.vrfs.[].neighbor_interfaces.[].peer_group") | String |  |  |  | Peer-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_filter</samp>](## "router_bgp.vrfs.[].neighbor_interfaces.[].peer_filter") | String |  |  |  | Peer-filter name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "router_bgp.vrfs.[].neighbor_interfaces.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute</samp>](## "router_bgp.vrfs.[].redistribute") | Dictionary |  |  |  | Redistribute routes in to BGP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;attached_host</samp>](## "router_bgp.vrfs.[].redistribute.attached_host") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].redistribute.attached_host.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].redistribute.attached_host.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.vrfs.[].redistribute.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].redistribute.bgp.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].redistribute.bgp.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected</samp>](## "router_bgp.vrfs.[].redistribute.connected") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].redistribute.connected.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].redistribute.connected.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.vrfs.[].redistribute.connected.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].redistribute.connected.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic</samp>](## "router_bgp.vrfs.[].redistribute.dynamic") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].redistribute.dynamic.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].redistribute.dynamic.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.vrfs.[].redistribute.dynamic.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis</samp>](## "router_bgp.vrfs.[].redistribute.isis") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].redistribute.isis.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_level</samp>](## "router_bgp.vrfs.[].redistribute.isis.isis_level") | String |  |  | Valid Values:<br>- <code>level-1</code><br>- <code>level-2</code><br>- <code>level-1-2</code> | Redistribute IS-IS route level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].redistribute.isis.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.vrfs.[].redistribute.isis.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].redistribute.isis.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "router_bgp.vrfs.[].redistribute.ospf") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].redistribute.ospf.enabled") | Boolean |  |  |  | Redistribute OSPF routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_external</samp>](## "router_bgp.vrfs.[].redistribute.ospf.match_external") | Dictionary |  |  |  | Redistribute OSPF routes learned from external sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].redistribute.ospf.match_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].redistribute.ospf.match_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].redistribute.ospf.match_external.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_internal</samp>](## "router_bgp.vrfs.[].redistribute.ospf.match_internal") | Dictionary |  |  |  | Redistribute OSPF routes learned from internal sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].redistribute.ospf.match_internal.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].redistribute.ospf.match_internal.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].redistribute.ospf.match_internal.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_nssa_external</samp>](## "router_bgp.vrfs.[].redistribute.ospf.match_nssa_external") | Dictionary |  |  |  | Redistribute OSPF routes learned from external NSSA sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].redistribute.ospf.match_nssa_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nssa_type</samp>](## "router_bgp.vrfs.[].redistribute.ospf.match_nssa_external.nssa_type") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code> | NSSA External Type Number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].redistribute.ospf.match_nssa_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].redistribute.ospf.match_nssa_external.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].redistribute.ospf.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].redistribute.ospf.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospfv3</samp>](## "router_bgp.vrfs.[].redistribute.ospfv3") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].redistribute.ospfv3.enabled") | Boolean |  |  |  | Redistribute OSPFv3 routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_external</samp>](## "router_bgp.vrfs.[].redistribute.ospfv3.match_external") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from external sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].redistribute.ospfv3.match_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].redistribute.ospfv3.match_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].redistribute.ospfv3.match_external.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_internal</samp>](## "router_bgp.vrfs.[].redistribute.ospfv3.match_internal") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from internal sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].redistribute.ospfv3.match_internal.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].redistribute.ospfv3.match_internal.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].redistribute.ospfv3.match_internal.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_nssa_external</samp>](## "router_bgp.vrfs.[].redistribute.ospfv3.match_nssa_external") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from external NSSA sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].redistribute.ospfv3.match_nssa_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nssa_type</samp>](## "router_bgp.vrfs.[].redistribute.ospfv3.match_nssa_external.nssa_type") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code> | NSSA External Type Number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].redistribute.ospfv3.match_nssa_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].redistribute.ospfv3.match_nssa_external.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].redistribute.ospfv3.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].redistribute.ospfv3.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rip</samp>](## "router_bgp.vrfs.[].redistribute.rip") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].redistribute.rip.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].redistribute.rip.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "router_bgp.vrfs.[].redistribute.static") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].redistribute.static.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].redistribute.static.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.vrfs.[].redistribute.static.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].redistribute.static.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;user</samp>](## "router_bgp.vrfs.[].redistribute.user") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].redistribute.user.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.vrfs.[].redistribute.user.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_routes</samp>](## "router_bgp.vrfs.[].redistribute_routes") <span style="color:red">deprecated</span> | List, items: Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>redistribute</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;source_protocol</samp>](## "router_bgp.vrfs.[].redistribute_routes.[].source_protocol") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].redistribute_routes.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].redistribute_routes.[].include_leaked") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.vrfs.[].redistribute_routes.[].rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.<br>Only applicable if `source_protocol` is one of `connected`, `dynamic`, `isis`, `static` and `user`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf_route_type</samp>](## "router_bgp.vrfs.[].redistribute_routes.[].ospf_route_type") | String |  |  | Valid Values:<br>- <code>external</code><br>- <code>internal</code><br>- <code>nssa-external</code><br>- <code>nssa-external 1</code><br>- <code>nssa-external 2</code> | Routes learned by the OSPF protocol.<br>The `ospf_route_type` is valid for source_protocols 'ospf' and 'ospfv3'.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;aggregate_addresses</samp>](## "router_bgp.vrfs.[].aggregate_addresses") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "router_bgp.vrfs.[].aggregate_addresses.[].prefix") | String | Required, Unique |  |  | IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;advertise_only</samp>](## "router_bgp.vrfs.[].aggregate_addresses.[].advertise_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as_set</samp>](## "router_bgp.vrfs.[].aggregate_addresses.[].as_set") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;summary_only</samp>](## "router_bgp.vrfs.[].aggregate_addresses.[].summary_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;attribute_map</samp>](## "router_bgp.vrfs.[].aggregate_addresses.[].attribute_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_map</samp>](## "router_bgp.vrfs.[].aggregate_addresses.[].match_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv4</samp>](## "router_bgp.vrfs.[].address_family_ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.vrfs.[].address_family_ipv4.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.vrfs.[].address_family_ipv4.bgp.missing_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in_action</samp>](## "router_bgp.vrfs.[].address_family_ipv4.bgp.missing_policy.direction_in_action") | String |  |  | Valid Values:<br>- <code>deny</code><br>- <code>deny-in-out</code><br>- <code>permit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out_action</samp>](## "router_bgp.vrfs.[].address_family_ipv4.bgp.missing_policy.direction_out_action") | String |  |  | Valid Values:<br>- <code>deny</code><br>- <code>deny-in-out</code><br>- <code>permit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.vrfs.[].address_family_ipv4.bgp.additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;install</samp>](## "router_bgp.vrfs.[].address_family_ipv4.bgp.additional_paths.install") | Boolean |  |  |  | Install BGP backup path. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;install_ecmp_primary</samp>](## "router_bgp.vrfs.[].address_family_ipv4.bgp.additional_paths.install_ecmp_primary") | Boolean |  |  |  | Allow additional path with ECMP primary path. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.vrfs.[].address_family_ipv4.bgp.additional_paths.receive") | Boolean |  |  |  | Enable or disable reception of additional-paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send</samp>](## "router_bgp.vrfs.[].address_family_ipv4.bgp.additional_paths.send") | String |  |  | Valid Values:<br>- <code>any</code><br>- <code>backup</code><br>- <code>ecmp</code><br>- <code>limit</code><br>- <code>disabled</code> | Select an option to send multiple paths for same prefix through bgp updates.<br>any: Send any eligible path.<br>backup: Best path and installed backup path.<br>ecmp: All paths in best path ECMP group.<br>limit: Limit to n eligible paths.<br>disabled: Disable sending any paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_limit</samp>](## "router_bgp.vrfs.[].address_family_ipv4.bgp.additional_paths.send_limit") | Integer |  |  | Min: 2<br>Max: 64 | Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_internal</samp>](## "router_bgp.vrfs.[].address_family_ipv4.bgp.redistribute_internal") | Boolean |  |  |  | Allow redistribution of iBGP routes into an Interior Gateway Protocol (IGP). EOS default is true. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.vrfs.[].address_family_ipv4.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "router_bgp.vrfs.[].address_family_ipv4.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.vrfs.[].address_family_ipv4.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.vrfs.[].address_family_ipv4.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.vrfs.[].address_family_ipv4.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_in</samp>](## "router_bgp.vrfs.[].address_family_ipv4.neighbors.[].rcf_in") | String |  |  |  | Inbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_out</samp>](## "router_bgp.vrfs.[].address_family_ipv4.neighbors.[].rcf_out") | String |  |  |  | Outbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp>](## "router_bgp.vrfs.[].address_family_ipv4.neighbors.[].prefix_list_in") | String |  |  |  | Inbound prefix-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp>](## "router_bgp.vrfs.[].address_family_ipv4.neighbors.[].prefix_list_out") | String |  |  |  | Outbound prefix-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop</samp>](## "router_bgp.vrfs.[].address_family_ipv4.neighbors.[].next_hop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv6</samp>](## "router_bgp.vrfs.[].address_family_ipv4.neighbors.[].next_hop.address_family_ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4.neighbors.[].next_hop.address_family_ipv6.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;originate</samp>](## "router_bgp.vrfs.[].address_family_ipv4.neighbors.[].next_hop.address_family_ipv6.originate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.vrfs.[].address_family_ipv4.neighbors.[].additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.vrfs.[].address_family_ipv4.neighbors.[].additional_paths.receive") | Boolean |  |  |  | Enable or disable reception of additional-paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send</samp>](## "router_bgp.vrfs.[].address_family_ipv4.neighbors.[].additional_paths.send") | String |  |  | Valid Values:<br>- <code>any</code><br>- <code>backup</code><br>- <code>ecmp</code><br>- <code>limit</code><br>- <code>disabled</code> | Select an option to send multiple paths for same prefix through bgp updates.<br>any: Send any eligible path.<br>backup: Best path and installed backup path.<br>ecmp: All paths in best path ECMP group.<br>limit: Limit to n eligible paths.<br>disabled: Disable sending any paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_limit</samp>](## "router_bgp.vrfs.[].address_family_ipv4.neighbors.[].additional_paths.send_limit") | Integer |  |  | Min: 2<br>Max: 64 | Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;networks</samp>](## "router_bgp.vrfs.[].address_family_ipv4.networks") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "router_bgp.vrfs.[].address_family_ipv4.networks.[].prefix") | String | Required, Unique |  |  | IPv4 prefix "A.B.C.D/E". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4.networks.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute") | Dictionary |  |  |  | Redistribute routes in to BGP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;attached_host</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.attached_host") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.attached_host.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.attached_host.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.bgp.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.bgp.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.connected") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.connected.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.connected.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.connected.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.connected.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.dynamic") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.dynamic.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.dynamic.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.dynamic.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.isis") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.isis.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_level</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.isis.isis_level") | String |  |  | Valid Values:<br>- <code>level-1</code><br>- <code>level-2</code><br>- <code>level-1-2</code> | Redistribute IS-IS route level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.isis.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.isis.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.isis.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospf") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospf.enabled") | Boolean |  |  |  | Redistribute OSPF routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_external</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospf.match_external") | Dictionary |  |  |  | Redistribute OSPF routes learned from external sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospf.match_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospf.match_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospf.match_external.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_internal</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospf.match_internal") | Dictionary |  |  |  | Redistribute OSPF routes learned from internal sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospf.match_internal.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospf.match_internal.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospf.match_internal.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_nssa_external</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospf.match_nssa_external") | Dictionary |  |  |  | Redistribute OSPF routes learned from external NSSA sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospf.match_nssa_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nssa_type</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospf.match_nssa_external.nssa_type") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code> | NSSA External Type Number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospf.match_nssa_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospf.match_nssa_external.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospf.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospf.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospfv3</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospfv3") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospfv3.enabled") | Boolean |  |  |  | Redistribute OSPFv3 routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_external</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospfv3.match_external") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from external sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospfv3.match_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospfv3.match_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospfv3.match_external.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_internal</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospfv3.match_internal") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from internal sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospfv3.match_internal.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospfv3.match_internal.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospfv3.match_internal.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_nssa_external</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospfv3.match_nssa_external") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from external NSSA sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospfv3.match_nssa_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nssa_type</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospfv3.match_nssa_external.nssa_type") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code> | NSSA External Type Number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospfv3.match_nssa_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospfv3.match_nssa_external.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospfv3.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.ospfv3.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rip</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.rip") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.rip.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.rip.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.static") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.static.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.static.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.static.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.static.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;user</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.user") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.user.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute.user.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_routes</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute_routes") <span style="color:red">deprecated</span> | List, items: Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>redistribute</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;source_protocol</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute_routes.[].source_protocol") | String | Required |  | Valid Values:<br>- <code>attached-host</code><br>- <code>bgp</code><br>- <code>connected</code><br>- <code>dynamic</code><br>- <code>isis</code><br>- <code>ospf</code><br>- <code>ospfv3</code><br>- <code>rip</code><br>- <code>static</code><br>- <code>user</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute_routes.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute_routes.[].include_leaked") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute_routes.[].rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.<br>Only applicable if `source_protocol` is one of `connected`, `dynamic`, `isis`, `static` and `user`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf_route_type</samp>](## "router_bgp.vrfs.[].address_family_ipv4.redistribute_routes.[].ospf_route_type") | String |  |  | Valid Values:<br>- <code>external</code><br>- <code>internal</code><br>- <code>nssa-external</code><br>- <code>nssa-external 1</code><br>- <code>nssa-external 2</code> | Routes learned by the OSPF protocol.<br>The `ospf_route_type` is valid for source_protocols 'ospf' and 'ospfv3'.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv6</samp>](## "router_bgp.vrfs.[].address_family_ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.vrfs.[].address_family_ipv6.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.vrfs.[].address_family_ipv6.bgp.missing_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in_action</samp>](## "router_bgp.vrfs.[].address_family_ipv6.bgp.missing_policy.direction_in_action") | String |  |  | Valid Values:<br>- <code>deny</code><br>- <code>deny-in-out</code><br>- <code>permit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out_action</samp>](## "router_bgp.vrfs.[].address_family_ipv6.bgp.missing_policy.direction_out_action") | String |  |  | Valid Values:<br>- <code>deny</code><br>- <code>deny-in-out</code><br>- <code>permit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.vrfs.[].address_family_ipv6.bgp.additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;install</samp>](## "router_bgp.vrfs.[].address_family_ipv6.bgp.additional_paths.install") | Boolean |  |  |  | Install BGP backup path. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;install_ecmp_primary</samp>](## "router_bgp.vrfs.[].address_family_ipv6.bgp.additional_paths.install_ecmp_primary") | Boolean |  |  |  | Allow additional path with ECMP primary path. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.vrfs.[].address_family_ipv6.bgp.additional_paths.receive") | Boolean |  |  |  | Enable or disable reception of additional-paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send</samp>](## "router_bgp.vrfs.[].address_family_ipv6.bgp.additional_paths.send") | String |  |  | Valid Values:<br>- <code>any</code><br>- <code>backup</code><br>- <code>ecmp</code><br>- <code>limit</code><br>- <code>disabled</code> | Select an option to send multiple paths for same prefix through bgp updates.<br>any: Send any eligible path.<br>backup: Best path and installed backup path.<br>ecmp: All paths in best path ECMP group.<br>limit: Limit to n eligible paths.<br>disabled: Disable sending any paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_limit</samp>](## "router_bgp.vrfs.[].address_family_ipv6.bgp.additional_paths.send_limit") | Integer |  |  | Min: 2<br>Max: 64 | Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_internal</samp>](## "router_bgp.vrfs.[].address_family_ipv6.bgp.redistribute_internal") | Boolean |  |  |  | Allow redistribution of iBGP routes into an Interior Gateway Protocol (IGP). EOS default is true. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.vrfs.[].address_family_ipv6.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "router_bgp.vrfs.[].address_family_ipv6.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.vrfs.[].address_family_ipv6.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.vrfs.[].address_family_ipv6.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.vrfs.[].address_family_ipv6.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_in</samp>](## "router_bgp.vrfs.[].address_family_ipv6.neighbors.[].rcf_in") | String |  |  |  | Inbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_out</samp>](## "router_bgp.vrfs.[].address_family_ipv6.neighbors.[].rcf_out") | String |  |  |  | Outbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp>](## "router_bgp.vrfs.[].address_family_ipv6.neighbors.[].prefix_list_in") | String |  |  |  | Inbound prefix-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp>](## "router_bgp.vrfs.[].address_family_ipv6.neighbors.[].prefix_list_out") | String |  |  |  | Outbound prefix-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.vrfs.[].address_family_ipv6.neighbors.[].additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.vrfs.[].address_family_ipv6.neighbors.[].additional_paths.receive") | Boolean |  |  |  | Enable or disable reception of additional-paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send</samp>](## "router_bgp.vrfs.[].address_family_ipv6.neighbors.[].additional_paths.send") | String |  |  | Valid Values:<br>- <code>any</code><br>- <code>backup</code><br>- <code>ecmp</code><br>- <code>limit</code><br>- <code>disabled</code> | Select an option to send multiple paths for same prefix through bgp updates.<br>any: Send any eligible path.<br>backup: Best path and installed backup path.<br>ecmp: All paths in best path ECMP group.<br>limit: Limit to n eligible paths.<br>disabled: Disable sending any paths. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_limit</samp>](## "router_bgp.vrfs.[].address_family_ipv6.neighbors.[].additional_paths.send_limit") | Integer |  |  | Min: 2<br>Max: 64 | Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;networks</samp>](## "router_bgp.vrfs.[].address_family_ipv6.networks") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "router_bgp.vrfs.[].address_family_ipv6.networks.[].prefix") | String | Required, Unique |  |  | IPv6 prefix "A:B:C:D:E:F:G:H/I". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6.networks.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute") | Dictionary |  |  |  | Redistribute routes in to BGP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;attached_host</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.attached_host") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.attached_host.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.attached_host.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.bgp.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.bgp.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.connected") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.connected.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.connected.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.connected.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.connected.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dhcp</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.dhcp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.dhcp.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.dhcp.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.dynamic") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.dynamic.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.dynamic.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.dynamic.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.isis") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.isis.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_level</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.isis.isis_level") | String |  |  | Valid Values:<br>- <code>level-1</code><br>- <code>level-2</code><br>- <code>level-1-2</code> | Redistribute IS-IS route level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.isis.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.isis.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.isis.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospfv3</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.ospfv3") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.ospfv3.enabled") | Boolean |  |  |  | Redistribute OSPFv3 routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_external</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.ospfv3.match_external") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from external sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.ospfv3.match_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.ospfv3.match_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.ospfv3.match_external.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_internal</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.ospfv3.match_internal") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from internal sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.ospfv3.match_internal.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.ospfv3.match_internal.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.ospfv3.match_internal.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_nssa_external</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.ospfv3.match_nssa_external") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from external NSSA sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.ospfv3.match_nssa_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nssa_type</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.ospfv3.match_nssa_external.nssa_type") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code> | NSSA External Type Number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.ospfv3.match_nssa_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.ospfv3.match_nssa_external.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.ospfv3.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.ospfv3.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.static") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.static.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.static.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.static.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.static.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;user</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.user") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.user.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute.user.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_routes</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute_routes") <span style="color:red">deprecated</span> | List, items: Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>redistribute</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;source_protocol</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute_routes.[].source_protocol") | String | Required |  | Valid Values:<br>- <code>attached-host</code><br>- <code>bgp</code><br>- <code>connected</code><br>- <code>dhcp</code><br>- <code>dynamic</code><br>- <code>isis</code><br>- <code>ospfv3</code><br>- <code>static</code><br>- <code>user</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute_routes.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute_routes.[].include_leaked") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute_routes.[].rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.<br>Only applicable if `source_protocol` is one of `connected`, `dynamic`, `isis`, `static` and `user`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf_route_type</samp>](## "router_bgp.vrfs.[].address_family_ipv6.redistribute_routes.[].ospf_route_type") | String |  |  | Valid Values:<br>- <code>external</code><br>- <code>internal</code><br>- <code>nssa-external</code><br>- <code>nssa-external 1</code><br>- <code>nssa-external 2</code> | Routes learned by the OSPF protocol.<br>The `ospf_route_type` is valid for source_protocols 'ospfv3'.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv4_multicast</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.bgp.missing_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in_action</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.bgp.missing_policy.direction_in_action") | String |  |  | Valid Values:<br>- <code>deny</code><br>- <code>deny-in-out</code><br>- <code>permit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out_action</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.bgp.missing_policy.direction_out_action") | String |  |  | Valid Values:<br>- <code>deny</code><br>- <code>deny-in-out</code><br>- <code>permit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.bgp.additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.bgp.additional_paths.receive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.neighbors.[].additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.neighbors.[].additional_paths.receive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;networks</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.networks") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.networks.[].prefix") | String | Required, Unique |  |  | IPv6 prefix "A.B.C.D/E". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.networks.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute") | Dictionary |  |  |  | Redistribute routes in to BGP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;attached_host</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.attached_host") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.attached_host.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.attached_host.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.connected") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.connected.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.connected.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.isis") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.isis.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_level</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.isis.isis_level") | String |  |  | Valid Values:<br>- <code>level-1</code><br>- <code>level-2</code><br>- <code>level-1-2</code> | Redistribute IS-IS route level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.isis.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.isis.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.isis.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospf") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospf.enabled") | Boolean |  |  |  | Redistribute OSPF routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_external</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospf.match_external") | Dictionary |  |  |  | Redistribute OSPF routes learned from external sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospf.match_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospf.match_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_internal</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospf.match_internal") | Dictionary |  |  |  | Redistribute OSPF routes learned from internal sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospf.match_internal.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospf.match_internal.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_nssa_external</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospf.match_nssa_external") | Dictionary |  |  |  | Redistribute OSPF routes learned from external NSSA sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospf.match_nssa_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nssa_type</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospf.match_nssa_external.nssa_type") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code> | NSSA External Type Number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospf.match_nssa_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospf.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospfv3</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospfv3") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospfv3.enabled") | Boolean |  |  |  | Redistribute OSPFv3 routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_external</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospfv3.match_external") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from external sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospfv3.match_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospfv3.match_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospfv3.match_external.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_internal</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospfv3.match_internal") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from internal sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospfv3.match_internal.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospfv3.match_internal.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospfv3.match_internal.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_nssa_external</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospfv3.match_nssa_external") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from external NSSA sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospfv3.match_nssa_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nssa_type</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospfv3.match_nssa_external.nssa_type") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code> | NSSA External Type Number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospfv3.match_nssa_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospfv3.match_nssa_external.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospfv3.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.ospfv3.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.static") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.static.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute.static.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_routes</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute_routes") <span style="color:red">deprecated</span> | List, items: Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>redistribute</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;source_protocol</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute_routes.[].source_protocol") | String | Required |  | Valid Values:<br>- <code>attached-host</code><br>- <code>connected</code><br>- <code>isis</code><br>- <code>ospf</code><br>- <code>ospfv3</code><br>- <code>static</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute_routes.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute_routes.[].include_leaked") | Boolean |  |  |  | Only applicable if `source_protocol` is `isis`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute_routes.[].rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.<br>Only applicable if `source_protocol` is `isis`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf_route_type</samp>](## "router_bgp.vrfs.[].address_family_ipv4_multicast.redistribute_routes.[].ospf_route_type") | String |  |  | Valid Values:<br>- <code>external</code><br>- <code>internal</code><br>- <code>nssa-external</code><br>- <code>nssa-external 1</code><br>- <code>nssa-external 2</code> | Routes learned by the OSPF protocol.<br>The `ospf_route_type` is valid for source_protocols 'ospf' and 'ospfv3'.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv6_multicast</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.bgp.missing_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in_action</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.bgp.missing_policy.direction_in_action") | String |  |  | Valid Values:<br>- <code>deny</code><br>- <code>deny-in-out</code><br>- <code>permit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out_action</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.bgp.missing_policy.direction_out_action") | String |  |  | Valid Values:<br>- <code>deny</code><br>- <code>deny-in-out</code><br>- <code>permit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.bgp.additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.bgp.additional_paths.receive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.neighbors.[].route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.neighbors.[].route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_paths</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.neighbors.[].additional_paths") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.neighbors.[].additional_paths.receive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;networks</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.networks") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.networks.[].prefix") | String | Required, Unique |  |  | IPv6 prefix "A:B:C:D:E:F:G:H/I". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.networks.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute") | Dictionary |  |  |  | Redistribute routes in to BGP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.connected") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.connected.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.connected.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.isis") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.isis.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_level</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.isis.isis_level") | String |  |  | Valid Values:<br>- <code>level-1</code><br>- <code>level-2</code><br>- <code>level-1-2</code> | Redistribute IS-IS route level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.isis.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.isis.rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.isis.include_leaked") | Boolean |  |  |  | Include following routes while redistributing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospf") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospf.enabled") | Boolean |  |  |  | Redistribute OSPF routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_external</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospf.match_external") | Dictionary |  |  |  | Redistribute OSPF routes learned from external sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospf.match_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospf.match_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_internal</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospf.match_internal") | Dictionary |  |  |  | Redistribute OSPF routes learned from internal sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospf.match_internal.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospf.match_internal.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_nssa_external</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospf.match_nssa_external") | Dictionary |  |  |  | Redistribute OSPF routes learned from external NSSA sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospf.match_nssa_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nssa_type</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospf.match_nssa_external.nssa_type") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code> | NSSA External Type Number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospf.match_nssa_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospf.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospfv3</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospfv3") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospfv3.enabled") | Boolean |  |  |  | Redistribute OSPFv3 routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_external</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospfv3.match_external") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from external sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospfv3.match_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospfv3.match_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_internal</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospfv3.match_internal") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from internal sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospfv3.match_internal.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospfv3.match_internal.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match_nssa_external</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospfv3.match_nssa_external") | Dictionary |  |  |  | Redistribute OSPFv3 routes learned from external NSSA sources. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospfv3.match_nssa_external.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nssa_type</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospfv3.match_nssa_external.nssa_type") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code> | NSSA External Type Number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospfv3.match_nssa_external.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.ospfv3.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.static") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.static.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute.static.route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_routes</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute_routes") <span style="color:red">deprecated</span> | List, items: Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>redistribute</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;source_protocol</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute_routes.[].source_protocol") | String | Required |  | Valid Values:<br>- <code>connected</code><br>- <code>isis</code><br>- <code>ospf</code><br>- <code>ospfv3</code><br>- <code>static</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute_routes.[].route_map") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_leaked</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute_routes.[].include_leaked") | Boolean |  |  |  | Only applicable if `source_protocol` is `isis`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute_routes.[].rcf") | String |  |  |  | RCF function name with parenthesis.<br>Example: MyFunction(myarg).<br>`route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.<br>Only applicable if `source_protocol` is `isis`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf_route_type</samp>](## "router_bgp.vrfs.[].address_family_ipv6_multicast.redistribute_routes.[].ospf_route_type") | String |  |  | Valid Values:<br>- <code>external</code><br>- <code>internal</code><br>- <code>nssa-external</code><br>- <code>nssa-external 1</code><br>- <code>nssa-external 2</code> | Routes learned by the OSPF protocol.<br>The `ospf_route_type` is valid for source_protocols 'ospf' and 'ospfv3'.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_flow_spec_ipv4</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv4.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv4.bgp.missing_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in_action</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv4.bgp.missing_policy.direction_in_action") | String |  |  | Valid Values:<br>- <code>deny</code><br>- <code>deny-in-out</code><br>- <code>permit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out_action</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv4.bgp.missing_policy.direction_out_action") | String |  |  | Valid Values:<br>- <code>deny</code><br>- <code>deny-in-out</code><br>- <code>permit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv4.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv4.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv4.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_flow_spec_ipv6</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv6.bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv6.bgp.missing_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in_action</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv6.bgp.missing_policy.direction_in_action") | String |  |  | Valid Values:<br>- <code>deny</code><br>- <code>deny-in-out</code><br>- <code>permit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out_action</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv6.bgp.missing_policy.direction_out_action") | String |  |  | Valid Values:<br>- <code>deny</code><br>- <code>deny-in-out</code><br>- <code>permit</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv6.neighbors") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv6.neighbors.[].ip_address") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "router_bgp.vrfs.[].address_family_flow_spec_ipv6.neighbors.[].activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "router_bgp.vrfs.[].eos_cli") | String |  |  |  | Multiline EOS CLI rendered directly on the Router BGP, VRF definition in the final EOS configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_families</samp>](## "router_bgp.vrfs.[].address_families") <span style="color:red">removed</span> | List |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>address_family_*</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;session_trackers</samp>](## "router_bgp.session_trackers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_bgp.session_trackers.[].name") | String | Required, Unique |  |  | Name of session tracker. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery_delay</samp>](## "router_bgp.session_trackers.[].recovery_delay") | Integer |  |  | Min: 1<br>Max: 3600 | Recovery delay in seconds. |
    | [<samp>&nbsp;&nbsp;eos_cli</samp>](## "router_bgp.eos_cli") | String |  |  |  | Multiline EOS CLI rendered directly on the Router BGP in the final EOS configuration. |

=== "YAML"

    ```yaml
    router_bgp:

      # BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
      # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
      as: <str>

      # BGP AS can be deplayed in the asplain <1-4294967295> or asdot notation "<1-65535>.<0-65535>". This flag indicates which mode is preferred - asplain is the default.
      as_notation: <str; "asdot" | "asplain">

      # In IP address format A.B.C.D.
      router_id: <str>
      distance:
        external_routes: <int; 1-255; required>
        internal_routes: <int; 1-255; required>
        local_routes: <int; 1-255; required>
      graceful_restart:
        enabled: <bool>

        # Number of seconds.
        restart_time: <int; 1-3600>

        # Number of seconds.
        stalepath_time: <int; 1-3600>
      graceful_restart_helper:
        enabled: <bool>

        # Number of seconds
        # graceful-restart-help long-lived and restart-time are mutually exclusive in CLI.
        # restart-time will take precedence if both are configured.
        restart_time: <int; 1-100000000>

        # graceful-restart-help long-lived and restart-time are mutually exclusive in CLI.
        # restart-time will take precedence if both are configured.
        long_lived: <bool>
      maximum_paths:
        paths: <int; 1-600; required>
        ecmp: <int; 1-600>
      updates:

        # Disables FIB updates and route advertisement when the BGP instance is initiated until the BGP convergence state is reached.
        wait_for_convergence: <bool>

        # Do not advertise reachability to a prefix until that prefix has been installed in hardware.
        # This will eliminate any temporary black holes due to a BGP speaker advertising reachability to a prefix that may not yet be installed into the forwarding plane.
        wait_install: <bool>

      # IP Address A.B.C.D.
      bgp_cluster_id: <str>

      # BGP command as string.
      bgp_defaults:
        - <str>
      bgp:
        default:

          # Default activation of IPv4 unicast address-family on all IPv4 neighbors (EOS default = True).
          ipv4_unicast: <bool>

          # Default activation of IPv4 unicast address-family on all IPv6 neighbors (EOS default == False).
          ipv4_unicast_transport_ipv6: <bool>
        route_reflector_preserve_attributes:
          enabled: <bool>
          always: <bool>
        bestpath:
          d_path: <bool>
        additional_paths:

          # Enable or disable reception of additional-paths.
          receive: <bool>

          # Select an option to send multiple paths for same prefix through bgp updates.
          # any: Send any eligible path.
          # backup: Best path and installed backup path.
          # ecmp: All paths in best path ECMP group.
          # limit: Limit to n eligible paths.
          # disabled: Disable sending any paths.
          send: <str; "any" | "backup" | "ecmp" | "limit" | "disabled">

          # Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`.
          send_limit: <int; 2-64>

        # Allow redistribution of iBGP routes into an Interior Gateway Protocol (IGP). EOS default is true.
        redistribute_internal: <bool>

      # Improved "listen_ranges" data model to support multiple listen ranges and additional filter capabilities.
      listen_ranges:

          # IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I".
        - prefix: <str>

          # Include router ID as part of peer filter.
          peer_id_include_router_id: <bool>

          # Peer group name.
          peer_group: <str>

          # Peer-filter name.
          # note: `peer_filter` or `remote_as` is required but mutually exclusive.
          # If both are defined, `peer_filter` takes precedence
          peer_filter: <str>

          # BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
          # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
          remote_as: <str>
      peer_groups:

          # Peer-group name.
        - name: <str; required; unique>

          # Key only used for documentation or validation purposes.
          type: <str>

          # BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
          # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
          remote_as: <str>

          # BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
          # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
          local_as: <str>
          description: <str>
          shutdown: <bool>

          # BGP AS-PATH options.
          as_path:

            # Replace AS number with local AS number.
            remote_as_replace_out: <bool>

            # Disable prepending own AS number to AS path.
            prepend_own_disabled: <bool>

          # Remove private AS numbers in outbound AS path.
          remove_private_as:
            enabled: <bool>
            all: <bool>
            replace_as: <bool>
          remove_private_as_ingress:
            enabled: <bool>
            replace_as: <bool>
          next_hop_unchanged: <bool>

          # IP address or interface name.
          update_source: <str>
          route_reflector_client: <bool>

          # Enable BFD.
          bfd: <bool>

          # Override default BFD timers. BFD must be enabled with `bfd: true`.
          bfd_timers:

            # Interval in milliseconds.
            interval: <int; 50-60000; required>

            # Rate in milliseconds.
            min_rx: <int; 50-60000; required>
            multiplier: <int; 3-50; required>

          # Time-to-live in range of hops.
          ebgp_multihop: <int; 1-255>
          next_hop_self: <bool>
          password: <str>
          passive: <bool>
          default_originate:
            enabled: <bool>
            always: <bool>

            # Route-map name.
            route_map: <str>

          # 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)'.
          send_community: <str>

          # Maximum number of routes (0 means unlimited).
          maximum_routes: <int; 0-4294967294>

          # Maximum number of routes after which a warning is issued (0 means never warn) or
          # Percentage of maximum number of routes at which to warn ("<1-100> percent").
          maximum_routes_warning_limit: <str>
          maximum_routes_warning_only: <bool>

          # Missing policy configuration for all address-families.
          missing_policy:

            # Missing policy inbound direction.
            direction_in:

              # Missing policy action.
              action: <str; "deny" | "permit" | "deny-in-out"; required>

              # Include community-list references in missing policy decision.
              include_community_list: <bool>

              # Include prefix-list references in missing policy decision.
              include_prefix_list: <bool>

              # Include sub-route-map references in missing policy decision.
              include_sub_route_map: <bool>

            # Missing policy outbound direction.
            direction_out:

              # Missing policy action.
              action: <str; "deny" | "permit" | "deny-in-out"; required>

              # Include community-list references in missing policy decision.
              include_community_list: <bool>

              # Include prefix-list references in missing policy decision.
              include_prefix_list: <bool>

              # Include sub-route-map references in missing policy decision.
              include_sub_route_map: <bool>
          link_bandwidth:
            enabled: <bool>

            # nn.nn(K|M|G) link speed in bits/second.
            default: <str>
          allowas_in:
            enabled: <bool>

            # Number of local ASNs allowed in a BGP update.
            times: <int; 1-10>
          weight: <int; 0-65535>

          # BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>".
          timers: <str>
          rib_in_pre_policy_retain:
            enabled: <bool>
            all: <bool>

          # Inbound route-map name.
          route_map_in: <str>

          # Outbound route-map name.
          route_map_out: <str>
          session_tracker: <str>
          shared_secret:

            # Name of profile defined under `management_security`.
            profile: <str; required>

            # Note: Algorithm hmac-sha-256 requires EOS version 4.31.1F and above.
            hash_algorithm: <str; "aes-128-cmac-96" | "hmac-sha-256" | "hmac-sha1-96"; required>

          # Maximum number of hops.
          ttl_maximum_hops: <int; 0-254>
      neighbors:
        - ip_address: <str; required; unique>
          peer_group: <str>

          # BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
          # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
          remote_as: <str>

          # BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
          # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
          local_as: <str>

          # BGP AS-PATH options.
          as_path:

            # Replace AS number with local AS number.
            remote_as_replace_out: <bool>

            # Disable prepending own AS number to AS path.
            prepend_own_disabled: <bool>

          # Key only used for documentation or validation purposes.
          peer: <str>
          description: <str>
          route_reflector_client: <bool>
          password: <str>
          passive: <bool>
          shutdown: <bool>

          # Source Interface.
          update_source: <str>

          # Enable BFD.
          bfd: <bool>

          # Override default BFD timers. BFD must be enabled with `bfd: true`.
          bfd_timers:

            # Interval in milliseconds.
            interval: <int; 50-60000; required>

            # Rate in milliseconds.
            min_rx: <int; 50-60000; required>
            multiplier: <int; 3-50; required>
          weight: <int; 0-65535>

          # BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>".
          timers: <str>

          # Inbound route-map name.
          route_map_in: <str>

          # Outbound route-map name.
          route_map_out: <str>
          default_originate:
            enabled: <bool>
            always: <bool>
            route_map: <str>

          # 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)'.
          send_community: <str>

          # Maximum number of routes (0 means unlimited).
          maximum_routes: <int; 0-4294967294>

          # Maximum number of routes after which a warning is issued (0 means never warn) or
          # Percentage of maximum number of routes at which to warn ("<1-100> percent").
          maximum_routes_warning_limit: <str>
          maximum_routes_warning_only: <bool>

          # Missing policy configuration for all address-families.
          missing_policy:

            # Missing policy inbound direction.
            direction_in:

              # Missing policy action.
              action: <str; "deny" | "permit" | "deny-in-out"; required>

              # Include community-list references in missing policy decision.
              include_community_list: <bool>

              # Include prefix-list references in missing policy decision.
              include_prefix_list: <bool>

              # Include sub-route-map references in missing policy decision.
              include_sub_route_map: <bool>

            # Missing policy outbound direction.
            direction_out:

              # Missing policy action.
              action: <str; "deny" | "permit" | "deny-in-out"; required>

              # Include community-list references in missing policy decision.
              include_community_list: <bool>

              # Include prefix-list references in missing policy decision.
              include_prefix_list: <bool>

              # Include sub-route-map references in missing policy decision.
              include_sub_route_map: <bool>
          allowas_in:
            enabled: <bool>

            # Number of local ASNs allowed in a BGP update.
            times: <int; 1-10>

          # Time-to-live in range of hops.
          ebgp_multihop: <int; 1-255>
          next_hop_self: <bool>
          link_bandwidth:
            enabled: <bool>

            # nn.nn(K|M|G) link speed in bits/second.
            default: <str>
          rib_in_pre_policy_retain:
            enabled: <bool>
            all: <bool>

          # Remove private AS numbers in outbound AS path.
          remove_private_as:
            enabled: <bool>
            all: <bool>
            replace_as: <bool>
          remove_private_as_ingress:
            enabled: <bool>
            replace_as: <bool>
          session_tracker: <str>
          shared_secret:

            # Name of profile defined under `management_security`.
            profile: <str; required>

            # Note: Algorithm hmac-sha-256 requires EOS version 4.31.1F and above.
            hash_algorithm: <str; "aes-128-cmac-96" | "hmac-sha-256" | "hmac-sha1-96"; required>

          # Maximum number of hops.
          ttl_maximum_hops: <int; 0-254>
      neighbor_interfaces:

          # Interface name.
        - name: <str; required; unique>

          # BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
          # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
          remote_as: <str>

          # Key only used for documentation or validation purposes.
          peer: <str>
          peer_group: <str; default="Peer-group name">
          description: <str>

          # Peer-filter name.
          peer_filter: <str>
      aggregate_addresses:

          # IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I".
        - prefix: <str; required; unique>
          advertise_only: <bool>
          as_set: <bool>
          summary_only: <bool>

          # Route-map name.
          attribute_map: <str>

          # Route-map name.
          match_map: <str>

      # Redistribute routes in to BGP.
      redistribute:
        attached_host:
          enabled: <bool; required>
          route_map: <str>
        bgp:
          enabled: <bool; required>
          route_map: <str>
        connected:
          enabled: <bool; required>
          route_map: <str>

          # RCF function name with parenthesis.
          # Example: MyFunction(myarg).
          # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
          rcf: <str>

          # Include following routes while redistributing.
          include_leaked: <bool>
        dynamic:
          enabled: <bool; required>
          route_map: <str>

          # RCF function name with parenthesis.
          # Example: MyFunction(myarg).
          # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
          rcf: <str>
        isis:
          enabled: <bool; required>

          # Redistribute IS-IS route level.
          isis_level: <str; "level-1" | "level-2" | "level-1-2">
          route_map: <str>

          # RCF function name with parenthesis.
          # Example: MyFunction(myarg).
          # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
          rcf: <str>

          # Include following routes while redistributing.
          include_leaked: <bool>
        ospf:

          # Redistribute OSPF routes.
          enabled: <bool>

          # Redistribute OSPF routes learned from external sources.
          match_external:
            enabled: <bool; required>
            route_map: <str>

            # Include following routes while redistributing.
            include_leaked: <bool>

          # Redistribute OSPF routes learned from internal sources.
          match_internal:
            enabled: <bool; required>
            route_map: <str>

            # Include following routes while redistributing.
            include_leaked: <bool>

          # Redistribute OSPF routes learned from external NSSA sources.
          match_nssa_external:
            enabled: <bool; required>

            # NSSA External Type Number.
            nssa_type: <int; 1 | 2>
            route_map: <str>

            # Include following routes while redistributing.
            include_leaked: <bool>
          route_map: <str>

          # Include following routes while redistributing.
          include_leaked: <bool>
        ospfv3:

          # Redistribute OSPFv3 routes.
          enabled: <bool>

          # Redistribute OSPFv3 routes learned from external sources.
          match_external:
            enabled: <bool; required>
            route_map: <str>

            # Include following routes while redistributing.
            include_leaked: <bool>

          # Redistribute OSPFv3 routes learned from internal sources.
          match_internal:
            enabled: <bool; required>
            route_map: <str>

            # Include following routes while redistributing.
            include_leaked: <bool>

          # Redistribute OSPFv3 routes learned from external NSSA sources.
          match_nssa_external:
            enabled: <bool; required>

            # NSSA External Type Number.
            nssa_type: <int; 1 | 2>
            route_map: <str>

            # Include following routes while redistributing.
            include_leaked: <bool>
          route_map: <str>

          # Include following routes while redistributing.
          include_leaked: <bool>
        rip:
          enabled: <bool; required>
          route_map: <str>
        static:
          enabled: <bool; required>
          route_map: <str>

          # RCF function name with parenthesis.
          # Example: MyFunction(myarg).
          # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
          rcf: <str>

          # Include following routes while redistributing.
          include_leaked: <bool>
        user:
          enabled: <bool; required>

          # RCF function name with parenthesis.
          # Example: MyFunction(myarg).
          # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
          rcf: <str>
      # This key is deprecated.
      # Support will be removed in AVD version 6.0.0.
      # Use <samp>redistribute</samp> instead.
      redistribute_routes:
        - source_protocol: <str; "attached-host" | "bgp" | "connected" | "dynamic" | "isis" | "ospf" | "ospfv3" | "rip" | "static" | "user"; required>
          route_map: <str>

          # RCF function name with parenthesis.
          # Example: MyFunction(myarg).
          # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
          # Only applicable if `source_protocol` is one of `connected`, `static`, `isis`, `user`, `dynamic`.
          rcf: <str>
          include_leaked: <bool>

          # Routes learned by the OSPF protocol.
          # The `ospf_route_type` is valid for source_protocols 'ospf' and 'ospfv3'.
          ospf_route_type: <str; "external" | "internal" | "nssa-external" | "nssa-external 1" | "nssa-external 2">
      vlan_aware_bundles:

          # VLAN aware bundle name.
        - name: <str; required; unique>

          # Key only used for documentation or validation purposes.
          tenant: <str>

          # Key only used for documentation or validation purposes.
          description: <str>

          # Route distinguisher.
          rd: <str>
          rd_evpn_domain:
            domain: <str; "remote" | "all">

            # Route distinguisher.
            rd: <str>
          route_targets:
            both:
              - <str>
            import:
              - <str>
            export:
              - <str>
            import_evpn_domains:
              - domain: <str; "remote" | "all">
                route_target: <str>
            export_evpn_domains:
              - domain: <str; "remote" | "all">
                route_target: <str>
            import_export_evpn_domains:
              - domain: <str; "remote" | "all">
                route_target: <str>
          redistribute_routes:
            - <str>
          no_redistribute_routes:
            - <str>

          # VLAN range as string. Example "100-200,300".
          vlan: <str>

          # Multiline EOS CLI rendered directly on the Router BGP, VLAN-aware-bundle definition in the final EOS configuration.
          eos_cli: <str>
      vlans:
        - id: <int; required; unique>

          # Key only used for documentation or validation purposes.
          tenant: <str>

          # Route distinguisher.
          rd: <str>
          rd_evpn_domain:
            domain: <str; "remote" | "all">

            # Route distinguisher.
            rd: <str>
          route_targets:
            both:
              - <str>
            import:
              - <str>
            export:
              - <str>
            import_evpn_domains:
              - domain: <str; "remote" | "all">
                route_target: <str>
            export_evpn_domains:
              - domain: <str; "remote" | "all">
                route_target: <str>
            import_export_evpn_domains:
              - domain: <str; "remote" | "all">
                route_target: <str>
          redistribute_routes:
            - <str>
          no_redistribute_routes:
            - <str>

          # Multiline EOS CLI rendered directly on the Router BGP, VLAN definition in the final EOS configuration.
          eos_cli: <str>
      vpws:

          # VPWS instance name.
        - name: <str; required; unique>

          # Route distinguisher.
          rd: <str>
          route_targets:

            # Route Target.
            import_export: <str>
          mpls_control_word: <bool>
          label_flow: <bool>
          mtu: <int>
          pseudowires:

              # Pseudowire name.
            - name: <str; required; unique>

              # Must match id_remote on other pe.
              id_local: <int>

              # Must match id_local on other pe.
              id_remote: <int>
      address_family_evpn:
        domain_identifier: <str>
        neighbor_default:

          # Transport encapsulation for neighbor.
          encapsulation: <str; "vxlan" | "mpls" | "path-selection">

          # Source interface name.
          next_hop_self_source_interface: <str>
          next_hop_self_received_evpn_routes:
            enable: <bool>
            inter_domain: <bool>

        # Specify the RIBs used to resolve MPLS next-hops. The order of this list determines the order of RIB lookups.
        next_hop_mpls_resolution_ribs: # 1-3 items

            # Type of RIB. For 'tunnel-rib', use 'rib_name' to specify the name of the Tunnel-RIB to use.
          - rib_type: <str; "system-connected" | "tunnel-rib-colored" | "tunnel-rib"; required>

            # The name of the tunnel-rib to use when using 'tunnel-rib' type.
            rib_name: <str>
        neighbors:
          - ip_address: <str; required; unique>
            activate: <bool>

            # Inbound RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            rcf_in: <str>

            # Outbound RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            rcf_out: <str>
            default_route:
              enabled: <bool>

              # RCF function name with parenthesis.
              # Example: MyFunction(myarg).
              rcf: <str>
              route_map: <str>
            additional_paths:

              # Enable or disable reception of additional-paths.
              receive: <bool>

              # Select an option to send multiple paths for same prefix through bgp updates.
              # any: Send any eligible path.
              # backup: Best path and installed backup path.
              # ecmp: All paths in best path ECMP group.
              # limit: Limit to n eligible paths.
              # disabled: Disable sending any paths.
              send: <str; "any" | "backup" | "ecmp" | "limit" | "disabled">

              # Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`.
              send_limit: <int; 2-64>

            # Transport encapsulation for the neighbor.
            encapsulation: <str; "vxlan" | "mpls" | "path-selection">
        peer_groups:

            # Peer-group name.
          - name: <str; required; unique>
            activate: <bool>

            # Inbound route-map name.
            route_map_in: <str>

            # Outbound route-map name.
            route_map_out: <str>

            # Inbound RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            rcf_in: <str>

            # Outbound RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            rcf_out: <str>
            default_route:
              enabled: <bool>

              # RCF function name with parenthesis.
              # Example: MyFunction(myarg).
              rcf: <str>
              route_map: <str>
            domain_remote: <bool>

            # Transport encapsulation for the peer-group.
            encapsulation: <str; "vxlan" | "mpls" | "path-selection">
            additional_paths:

              # Enable or disable reception of additional-paths.
              receive: <bool>

              # Select an option to send multiple paths for same prefix through bgp updates.
              # any: Send any eligible path.
              # backup: Best path and installed backup path.
              # ecmp: All paths in best path ECMP group.
              # limit: Limit to n eligible paths.
              # disabled: Disable sending any paths.
              send: <str; "any" | "backup" | "ecmp" | "limit" | "disabled">

              # Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`.
              send_limit: <int; 2-64>
        evpn_hostflap_detection:
          enabled: <bool>

          # Time (in seconds) to detect a MAC duplication issue.
          window: <int; 0-4294967295>

          # Minimum number of MAC moves that indicate a MAC Duplication issue.
          threshold: <int; 0-4294967295>

          # Time (in seconds) to purge a MAC duplication issue.
          expiry_timeout: <int; 0-4294967295>
        next_hop:
          resolution_disabled: <bool>
        route:
          import_match_failure_action: <str; "discard">
          import_ethernet_segment_ip_mass_withdraw: <bool>
          import_overlay_index_gateway: <bool>
          export_ethernet_segment_ip_mass_withdraw: <bool>
        next_hop_unchanged: <bool>
        bgp:
          additional_paths:

            # Enable or disable reception of additional-paths.
            receive: <bool>

            # Select an option to send multiple paths for same prefix through bgp updates.
            # any: Send any eligible path.
            # backup: Best path and installed backup path.
            # ecmp: All paths in best path ECMP group.
            # limit: Limit to n eligible paths.
            # disabled: Disable sending any paths.
            send: <str; "any" | "backup" | "ecmp" | "limit" | "disabled">

            # Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`.
            send_limit: <int; 2-64>

        # BGP layer-2 in-place FEC operation.
        layer_2_fec_in_place_update:
          enabled: <bool; required>

          # In-place FEC update tracking timeout in seconds.
          timeout: <int; 0-300>

        # BGP additional-paths commands.
        # This key is deprecated.
        # Support will be removed in AVD version 6.0.0.
        # Use <samp>bgp.additional_paths</samp> instead.
        bgp_additional_paths:

          # Receive multiple paths.
          receive: <bool>

          # Send multiple paths.
          send:

            # Any eligible path.
            any: <bool>

            # Best path and installed backup path.
            backup: <bool>

            # All paths in best path ECMP group.
            ecmp: <bool>

            # Amount of ECMP paths to send.
            ecmp_limit: <int; 2-64>

            # Amount of paths to send.
            limit: <int; 2-64>
      address_family_rtc:
        peer_groups:

            # Peer-group name.
          - name: <str; required; unique>
            activate: <bool>
            default_route_target:
              only: <bool>
              encoding_origin_as_omit: <str>
      address_family_ipv4:
        networks:

            # IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I".
          - prefix: <str; required; unique>

            # Route-map name.
            route_map: <str>
        bgp:
          additional_paths:

            # Install BGP backup path.
            install: <bool>

            # Allow additional path with ECMP primary path.
            install_ecmp_primary: <bool>

            # Enable or disable reception of additional-paths.
            receive: <bool>

            # Select an option to send multiple paths for same prefix through bgp updates.
            # any: Send any eligible path.
            # backup: Best path and installed backup path.
            # ecmp: All paths in best path ECMP group.
            # limit: Limit to n eligible paths.
            # disabled: Disable sending any paths.
            send: <str; "any" | "backup" | "ecmp" | "limit" | "disabled">

            # Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`.
            send_limit: <int; 2-64>

          # Allow redistribution of iBGP routes into an Interior Gateway Protocol (IGP). EOS default is true.
          redistribute_internal: <bool>
        peer_groups:

            # Peer-group name.
          - name: <str; required; unique>
            activate: <bool>

            # Inbound route-map name.
            route_map_in: <str>

            # Outbound route-map name.
            route_map_out: <str>

            # Inbound RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            rcf_in: <str>

            # Outbound RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            rcf_out: <str>
            default_originate:
              always: <bool>

              # Route-map name.
              route_map: <str>

            # Inbound prefix-list name.
            prefix_list_in: <str>

            # Outbound prefix-list name.
            prefix_list_out: <str>
            additional_paths:

              # Apply the configurations only to the routes matching the prefix list.
              prefix_list: <str>

              # Enable or disable reception of additional-paths.
              receive: <bool>

              # Select an option to send multiple paths for same prefix through bgp updates.
              # any: Send any eligible path.
              # backup: Best path and installed backup path.
              # ecmp: All paths in best path ECMP group.
              # limit: Limit to n eligible paths.
              # disabled: Disable sending any paths.
              send: <str; "any" | "backup" | "ecmp" | "limit" | "disabled">

              # Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`.
              send_limit: <int; 2-64>
            next_hop:
              address_family_ipv6:
                enabled: <bool; required>
                originate: <bool>
        neighbors:
          - ip_address: <str; required; unique>
            activate: <bool>

            # Inbound route-map name.
            route_map_in: <str>

            # Outbound route-map name.
            route_map_out: <str>

            # Inbound RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            rcf_in: <str>

            # Outbound RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            rcf_out: <str>

            # Inbound prefix-list name.
            prefix_list_in: <str>

            # Prefix-list name.
            prefix_list_out: <str>
            default_originate:
              always: <bool>
              route_map: <str>
            additional_paths:

              # Apply the configurations only to the routes matching the prefix list.
              prefix_list: <str>

              # Enable or disable reception of additional-paths.
              receive: <bool>

              # Select an option to send multiple paths for same prefix through bgp updates.
              # any: Send any eligible path.
              # backup: Best path and installed backup path.
              # ecmp: All paths in best path ECMP group.
              # limit: Limit to n eligible paths.
              # disabled: Disable sending any paths.
              send: <str; "any" | "backup" | "ecmp" | "limit" | "disabled">

              # Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`.
              send_limit: <int; 2-64>

        # Redistribute routes in to BGP.
        redistribute:
          attached_host:
            enabled: <bool; required>
            route_map: <str>
          bgp:
            enabled: <bool; required>
            route_map: <str>
          connected:
            enabled: <bool; required>
            route_map: <str>

            # RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
            rcf: <str>

            # Include following routes while redistributing.
            include_leaked: <bool>
          dynamic:
            enabled: <bool; required>
            route_map: <str>

            # RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
            rcf: <str>
          isis:
            enabled: <bool; required>

            # Redistribute IS-IS route level.
            isis_level: <str; "level-1" | "level-2" | "level-1-2">
            route_map: <str>

            # RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
            rcf: <str>

            # Include following routes while redistributing.
            include_leaked: <bool>
          ospf:

            # Redistribute OSPF routes.
            enabled: <bool>

            # Redistribute OSPF routes learned from external sources.
            match_external:
              enabled: <bool; required>
              route_map: <str>

              # Include following routes while redistributing.
              include_leaked: <bool>

            # Redistribute OSPF routes learned from internal sources.
            match_internal:
              enabled: <bool; required>
              route_map: <str>

              # Include following routes while redistributing.
              include_leaked: <bool>

            # Redistribute OSPF routes learned from external NSSA sources.
            match_nssa_external:
              enabled: <bool; required>

              # NSSA External Type Number.
              nssa_type: <int; 1 | 2>
              route_map: <str>

              # Include following routes while redistributing.
              include_leaked: <bool>
            route_map: <str>

            # Include following routes while redistributing.
            include_leaked: <bool>
          ospfv3:

            # Redistribute OSPFv3 routes.
            enabled: <bool>

            # Redistribute OSPFv3 routes learned from external sources.
            match_external:
              enabled: <bool; required>
              route_map: <str>

              # Include following routes while redistributing.
              include_leaked: <bool>

            # Redistribute OSPFv3 routes learned from internal sources.
            match_internal:
              enabled: <bool; required>
              route_map: <str>

              # Include following routes while redistributing.
              include_leaked: <bool>

            # Redistribute OSPFv3 routes learned from external NSSA sources.
            match_nssa_external:
              enabled: <bool; required>

              # NSSA External Type Number.
              nssa_type: <int; 1 | 2>
              route_map: <str>

              # Include following routes while redistributing.
              include_leaked: <bool>
            route_map: <str>

            # Include following routes while redistributing.
            include_leaked: <bool>
          rip:
            enabled: <bool; required>
            route_map: <str>
          static:
            enabled: <bool; required>
            route_map: <str>

            # RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
            rcf: <str>

            # Include following routes while redistributing.
            include_leaked: <bool>
          user:
            enabled: <bool; required>

            # RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
            rcf: <str>
        # This key is deprecated.
        # Support will be removed in AVD version 6.0.0.
        # Use <samp>redistribute</samp> instead.
        redistribute_routes:
          - source_protocol: <str; "attached-host" | "bgp" | "connected" | "dynamic" | "isis" | "ospf" | "ospfv3" | "rip" | "static" | "user"; required>
            route_map: <str>

            # Only applicable if `source_protocol` is one of `connected`, `static`, `isis`, `ospf`, `ospfv3`.
            include_leaked: <bool>

            # RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
            # Only applicable if `source_protocol` is one of `connected`, `static`, `isis`, `user`, `dynamic`.
            rcf: <str>

            # Routes learned by the OSPF protocol.
            # The `ospf_route_type` is valid for source_protocols 'ospf' and 'ospfv3'.
            ospf_route_type: <str; "external" | "internal" | "nssa-external" | "nssa-external 1" | "nssa-external 2">
      address_family_ipv4_labeled_unicast:
        aigp_session:
          confederation: <bool>
          ebgp: <bool>
          ibgp: <bool>
        bgp:
          additional_paths:

            # Enable or disable reception of additional-paths.
            receive: <bool>

            # Select an option to send multiple paths for same prefix through bgp updates.
            # any: Send any eligible path.
            # backup: Best path and installed backup path.
            # ecmp: All paths in best path ECMP group.
            # limit: Limit to n eligible paths.
            # disabled: Disable sending any paths.
            send: <str; "any" | "backup" | "ecmp" | "limit" | "disabled">

            # Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`.
            send_limit: <int; 2-64>

          # Missing policy configuration for all address-families.
          missing_policy:

            # Missing policy inbound direction.
            direction_in:

              # Missing policy action.
              action: <str; "deny" | "permit" | "deny-in-out"; required>

              # Include community-list references in missing policy decision.
              include_community_list: <bool>

              # Include prefix-list references in missing policy decision.
              include_prefix_list: <bool>

              # Include sub-route-map references in missing policy decision.
              include_sub_route_map: <bool>

            # Missing policy outbound direction.
            direction_out:

              # Missing policy action.
              action: <str; "deny" | "permit" | "deny-in-out"; required>

              # Include community-list references in missing policy decision.
              include_community_list: <bool>

              # Include prefix-list references in missing policy decision.
              include_prefix_list: <bool>

              # Include sub-route-map references in missing policy decision.
              include_sub_route_map: <bool>
          next_hop_unchanged: <bool>
        graceful_restart: <bool>
        label_local_termination: <str; "explicit-null" | "implicit-null">

        # Skip LFIB entry installation and next hop self route advertisements.
        lfib_entry_installation_skipped: <bool>
        neighbor_default:
          next_hop_self: <bool>
        peer_groups:

            # Peer-group name.
          - name: <str; required; unique>
            activate: <bool>
            additional_paths:

              # Enable or disable reception of additional-paths.
              receive: <bool>

              # Select an option to send multiple paths for same prefix through bgp updates.
              # any: Send any eligible path.
              # backup: Best path and installed backup path.
              # ecmp: All paths in best path ECMP group.
              # limit: Limit to n eligible paths.
              # disabled: Disable sending any paths.
              send: <str; "any" | "backup" | "ecmp" | "limit" | "disabled">

              # Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`.
              send_limit: <int; 2-64>
            aigp_session: <bool>
            graceful_restart: <bool>
            graceful_restart_helper:
              stale_route_map: <str>

            # Maximum number of routes (0 means unlimited).
            maximum_advertised_routes: <int; 0-4294967294>

            # Maximum number of routes after which a warning is issued (0 means never warn) or
            # Percentage of maximum number of routes at which to warn ("<1-100> percent").
            maximum_advertised_routes_warning_limit: <str>

            # Missing policy configuration for BGP Labeled-Unicast neighbor.
            missing_policy:

              # Missing policy inbound direction.
              direction_in:

                # Missing policy action.
                action: <str; "deny" | "permit" | "deny-in-out"; required>

                # Include community-list references in missing policy decision.
                include_community_list: <bool>

                # Include prefix-list references in missing policy decision.
                include_prefix_list: <bool>

                # Include sub-route-map references in missing policy decision.
                include_sub_route_map: <bool>

              # Missing policy outbound direction.
              direction_out:

                # Missing policy action.
                action: <str; "deny" | "permit" | "deny-in-out"; required>

                # Include community-list references in missing policy decision.
                include_community_list: <bool>

                # Include prefix-list references in missing policy decision.
                include_prefix_list: <bool>

                # Include sub-route-map references in missing policy decision.
                include_sub_route_map: <bool>
            multi_path: <bool>
            next_hop_self: <bool>

            # Source interface name.
            next_hop_self_source_interface: <str>

            # v4-mapped-v6 source interface name. Takes precedence over the next_hop_self_source_interface.
            next_hop_self_v4_mapped_v6_source_interface: <str>
            next_hop_unchanged: <bool>

            # Inbound RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            rcf_in: <str>

            # Outbound RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            rcf_out: <str>

            # Inbound route-map name.
            route_map_in: <str>

            # Outbound route-map name.
            route_map_out: <str>
        neighbors:
          - ip_address: <str; required; unique>
            activate: <bool>
            additional_paths:

              # Enable or disable reception of additional-paths.
              receive: <bool>

              # Select an option to send multiple paths for same prefix through bgp updates.
              # any: Send any eligible path.
              # backup: Best path and installed backup path.
              # ecmp: All paths in best path ECMP group.
              # limit: Limit to n eligible paths.
              # disabled: Disable sending any paths.
              send: <str; "any" | "backup" | "ecmp" | "limit" | "disabled">

              # Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`.
              send_limit: <int; 2-64>
            aigp_session: <bool>
            graceful_restart: <bool>
            graceful_restart_helper:
              stale_route_map: <str>

            # Maximum number of routes (0 means unlimited).
            maximum_advertised_routes: <int; 0-4294967294>

            # Maximum number of routes after which a warning is issued (0 means never warn) or
            # Percentage of maximum number of routes at which to warn ("<1-100> percent").
            maximum_advertised_routes_warning_limit: <str>

            # Missing policy configuration for BGP Labeled-Unicast neighbor.
            missing_policy:

              # Missing policy inbound direction.
              direction_in:

                # Missing policy action.
                action: <str; "deny" | "permit" | "deny-in-out"; required>

                # Include community-list references in missing policy decision.
                include_community_list: <bool>

                # Include prefix-list references in missing policy decision.
                include_prefix_list: <bool>

                # Include sub-route-map references in missing policy decision.
                include_sub_route_map: <bool>

              # Missing policy outbound direction.
              direction_out:

                # Missing policy action.
                action: <str; "deny" | "permit" | "deny-in-out"; required>

                # Include community-list references in missing policy decision.
                include_community_list: <bool>

                # Include prefix-list references in missing policy decision.
                include_prefix_list: <bool>

                # Include sub-route-map references in missing policy decision.
                include_sub_route_map: <bool>
            multi_path: <bool>
            next_hop_self: <bool>

            # Source interface name.
            next_hop_self_source_interface: <str>

            # v4-mapped-v6 source interface name. Takes precedence over the next_hop_self_source_interface.
            next_hop_self_v4_mapped_v6_source_interface: <str>
            next_hop_unchanged: <bool>

            # Inbound RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            rcf_in: <str>

            # Outbound RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            rcf_out: <str>

            # Inbound route-map name.
            route_map_in: <str>

            # Outbound route-map name.
            route_map_out: <str>
        networks: # >=1 items

            # IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I".
          - prefix: <str; required; unique>

            # Route-map name.
            route_map: <str>
        next_hops: # >=1 items
          - ip_address: <str; required; unique>
            lfib_backup_ip_forwarding: <bool>

        # Specify the RIBs used to resolve next-hops. The order of this list determines the order of RIB lookups.
        next_hop_resolution_ribs: # 1-3 items

            # Type of RIB. For 'tunnel-rib', use 'rib_name' to specify the name of the Tunnel-RIB to use.
          - rib_type: <str; "system-connected" | "tunnel-rib-colored" | "tunnel-rib"; required>

            # The name of the tunnel-rib to use when using 'tunnel-rib' type.
            rib_name: <str>
        tunnel_source_protocols: # 1-2 items
          - protocol: <str; "isis segment-routing" | "ldp"; required; unique>

            # Optional RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            rcf: <str>

        # Wait for BGP to converge before sending out any route updates.
        update_wait_for_convergence: <bool>
      address_family_ipv4_multicast:
        bgp:
          additional_paths:
            receive: <bool>
        peer_groups:

            # Peer-group name.
          - name: <str; required; unique>
            activate: <bool>

            # Inbound route-map name.
            route_map_in: <str>

            # Outbound route-map name.
            route_map_out: <str>
            additional_paths:
              receive: <bool>
        neighbors:
          - ip_address: <str; required; unique>
            activate: <bool>

            # Inbound route-map name.
            route_map_in: <str>

            # Outbound route-map name.
            route_map_out: <str>
            additional_paths:
              receive: <bool>

        # Redistribute routes in to BGP.
        redistribute:
          attached_host:
            enabled: <bool; required>
            route_map: <str>
          connected:
            enabled: <bool; required>
            route_map: <str>
          isis:
            enabled: <bool; required>

            # Redistribute IS-IS route level.
            isis_level: <str; "level-1" | "level-2" | "level-1-2">
            route_map: <str>

            # RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
            rcf: <str>

            # Include following routes while redistributing.
            include_leaked: <bool>
          ospf:

            # Redistribute OSPF routes.
            enabled: <bool>

            # Redistribute OSPF routes learned from external sources.
            match_external:
              enabled: <bool; required>
              route_map: <str>

            # Redistribute OSPF routes learned from internal sources.
            match_internal:
              enabled: <bool; required>
              route_map: <str>

            # Redistribute OSPF routes learned from external NSSA sources.
            match_nssa_external:
              enabled: <bool; required>

              # NSSA External Type Number.
              nssa_type: <int; 1 | 2>
              route_map: <str>
            route_map: <str>
          ospfv3:

            # Redistribute OSPFv3 routes.
            enabled: <bool>

            # Redistribute OSPFv3 routes learned from external sources.
            match_external:
              enabled: <bool; required>
              route_map: <str>

            # Redistribute OSPFv3 routes learned from internal sources.
            match_internal:
              enabled: <bool; required>
              route_map: <str>

            # Redistribute OSPFv3 routes learned from external NSSA sources.
            match_nssa_external:
              enabled: <bool; required>

              # NSSA External Type Number.
              nssa_type: <int; 1 | 2>
              route_map: <str>
            route_map: <str>
          static:
            enabled: <bool; required>
            route_map: <str>
        # This key is deprecated.
        # Support will be removed in AVD version 6.0.0.
        # Use <samp>redistribute</samp> instead.
        redistribute_routes:
          - source_protocol: <str; required>
            route_map: <str>

            # Only applicable if `source_protocol` is `isis`.
            include_leaked: <bool>

            # RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
            # Only applicable if `source_protocol` is `isis`.
            rcf: <str>

            # Routes learned by the OSPF protocol.
            # The `ospf_route_type` is valid for source_protocols 'ospf' and 'ospfv3'.
            ospf_route_type: <str; "external" | "internal" | "nssa-external" | "nssa-external 1" | "nssa-external 2">
      address_family_ipv4_sr_te:
        neighbors:
          - ip_address: <str; required; unique>
            activate: <bool>

            # Inbound route-map name.
            route_map_in: <str>

            # Outbound route-map name.
            route_map_out: <str>
        peer_groups:

            # Peer-group name.
          - name: <str; required; unique>
            activate: <bool>

            # Inbound route-map name.
            route_map_in: <str>

            # Outbound route-map name.
            route_map_out: <str>
      address_family_ipv6:
        networks:

            # IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I".
          - prefix: <str; required; unique>

            # Route-map name.
            route_map: <str>
        bgp:

          # Allow redistribution of iBGP routes into an Interior Gateway Protocol (IGP). EOS default is true.
          redistribute_internal: <bool>
          additional_paths:

            # Install BGP backup path.
            install: <bool>

            # Allow additional path with ECMP primary path.
            install_ecmp_primary: <bool>

            # Enable or disable reception of additional-paths.
            receive: <bool>

            # Select an option to send multiple paths for same prefix through bgp updates.
            # any: Send any eligible path.
            # backup: Best path and installed backup path.
            # ecmp: All paths in best path ECMP group.
            # limit: Limit to n eligible paths.
            # disabled: Disable sending any paths.
            send: <str; "any" | "backup" | "ecmp" | "limit" | "disabled">

            # Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`.
            send_limit: <int; 2-64>
        peer_groups:

            # Peer-group name.
          - name: <str; required; unique>
            activate: <bool>

            # Inbound route-map name.
            route_map_in: <str>

            # Outbound route-map name.
            route_map_out: <str>

            # Inbound RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            rcf_in: <str>

            # Outbound RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            rcf_out: <str>

            # Inbound prefix-list name.
            prefix_list_in: <str>

            # Outbound prefix-list name.
            prefix_list_out: <str>
            additional_paths:

              # Apply the configurations only to the routes matching the prefix list.
              prefix_list: <str>

              # Enable or disable reception of additional-paths.
              receive: <bool>

              # Select an option to send multiple paths for same prefix through bgp updates.
              # any: Send any eligible path.
              # backup: Best path and installed backup path.
              # ecmp: All paths in best path ECMP group.
              # limit: Limit to n eligible paths.
              # disabled: Disable sending any paths.
              send: <str; "any" | "backup" | "ecmp" | "limit" | "disabled">

              # Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`.
              send_limit: <int; 2-64>
        neighbors:
          - ip_address: <str; required; unique>
            activate: <bool>

            # Inbound route-map name.
            route_map_in: <str>

            # Outbound route-map name.
            route_map_out: <str>

            # Inbound RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            rcf_in: <str>

            # Outbound RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            rcf_out: <str>

            # Inbound prefix-list name.
            prefix_list_in: <str>

            # Outbound prefix-list name.
            prefix_list_out: <str>
            additional_paths:

              # Apply the configurations only to the routes matching the prefix list.
              prefix_list: <str>

              # Enable or disable reception of additional-paths.
              receive: <bool>

              # Select an option to send multiple paths for same prefix through bgp updates.
              # any: Send any eligible path.
              # backup: Best path and installed backup path.
              # ecmp: All paths in best path ECMP group.
              # limit: Limit to n eligible paths.
              # disabled: Disable sending any paths.
              send: <str; "any" | "backup" | "ecmp" | "limit" | "disabled">

              # Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`.
              send_limit: <int; 2-64>

        # Redistribute routes in to BGP.
        redistribute:
          attached_host:
            enabled: <bool; required>
            route_map: <str>
          bgp:
            enabled: <bool; required>
            route_map: <str>
          connected:
            enabled: <bool; required>
            route_map: <str>

            # RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
            rcf: <str>

            # Include following routes while redistributing.
            include_leaked: <bool>
          dhcp:
            enabled: <bool; required>
            route_map: <str>
          dynamic:
            enabled: <bool; required>
            route_map: <str>

            # RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
            rcf: <str>
          isis:
            enabled: <bool; required>

            # Redistribute IS-IS route level.
            isis_level: <str; "level-1" | "level-2" | "level-1-2">
            route_map: <str>

            # RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
            rcf: <str>

            # Include following routes while redistributing.
            include_leaked: <bool>
          ospfv3:

            # Redistribute OSPFv3 routes.
            enabled: <bool>

            # Redistribute OSPFv3 routes learned from external sources.
            match_external:
              enabled: <bool; required>
              route_map: <str>

              # Include following routes while redistributing.
              include_leaked: <bool>

            # Redistribute OSPFv3 routes learned from internal sources.
            match_internal:
              enabled: <bool; required>
              route_map: <str>

              # Include following routes while redistributing.
              include_leaked: <bool>

            # Redistribute OSPFv3 routes learned from external NSSA sources.
            match_nssa_external:
              enabled: <bool; required>

              # NSSA External Type Number.
              nssa_type: <int; 1 | 2>
              route_map: <str>

              # Include following routes while redistributing.
              include_leaked: <bool>
            route_map: <str>

            # Include following routes while redistributing.
            include_leaked: <bool>
          static:
            enabled: <bool; required>
            route_map: <str>

            # RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
            rcf: <str>

            # Include following routes while redistributing.
            include_leaked: <bool>
          user:
            enabled: <bool; required>

            # RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
            rcf: <str>
        # This key is deprecated.
        # Support will be removed in AVD version 6.0.0.
        # Use <samp>redistribute</samp> instead.
        redistribute_routes:
          - source_protocol: <str; required>
            route_map: <str>
            include_leaked: <bool>

            # RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
            # Only used if `source_protocol` is one of `connected`, `static`, `isis`, `user`, `dynamic`.
            rcf: <str>

            # Routes learned by the OSPF protocol.
            # The `ospf_route_type` is valid for source_protocols 'ospfv3'.
            ospf_route_type: <str; "external" | "internal" | "nssa-external" | "nssa-external 1" | "nssa-external 2">
      address_family_ipv6_multicast:
        bgp:
          missing_policy:
            direction_in_action: <str; "deny" | "deny-in-out" | "permit">
            direction_out_action: <str; "deny" | "deny-in-out" | "permit">
          additional_paths:
            receive: <bool>
        neighbors:
          - ip_address: <str; required; unique>
            activate: <bool>

            # Inbound route-map name.
            route_map_in: <str>

            # Outbound route-map name.
            route_map_out: <str>
            additional_paths:
              receive: <bool>
        peer_groups:

            # Peer-group name.
          - name: <str; required; unique>
            activate: <bool>
            additional_paths:
              receive: <bool>
        networks:

            # IPv6 prefix "A:B:C:D:E:F:G:H/I".
          - prefix: <str; required; unique>
            route_map: <str>

        # Redistribute routes in to BGP.
        redistribute:
          connected:
            enabled: <bool; required>
            route_map: <str>
          isis:
            enabled: <bool; required>

            # Redistribute IS-IS route level.
            isis_level: <str; "level-1" | "level-2" | "level-1-2">
            route_map: <str>

            # RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
            rcf: <str>

            # Include following routes while redistributing.
            include_leaked: <bool>
          ospf:

            # Redistribute OSPF routes.
            enabled: <bool>

            # Redistribute OSPF routes learned from external sources.
            match_external:
              enabled: <bool; required>
              route_map: <str>

            # Redistribute OSPF routes learned from internal sources.
            match_internal:
              enabled: <bool; required>
              route_map: <str>

            # Redistribute OSPF routes learned from external NSSA sources.
            match_nssa_external:
              enabled: <bool; required>

              # NSSA External Type Number.
              nssa_type: <int; 1 | 2>
              route_map: <str>
            route_map: <str>
          ospfv3:

            # Redistribute OSPFv3 routes.
            enabled: <bool>

            # Redistribute OSPFv3 routes learned from external sources.
            match_external:
              enabled: <bool; required>
              route_map: <str>

            # Redistribute OSPFv3 routes learned from internal sources.
            match_internal:
              enabled: <bool; required>
              route_map: <str>

            # Redistribute OSPFv3 routes learned from external NSSA sources.
            match_nssa_external:
              enabled: <bool; required>

              # NSSA External Type Number.
              nssa_type: <int; 1 | 2>
              route_map: <str>
            route_map: <str>
          static:
            enabled: <bool; required>
            route_map: <str>
        # This key is deprecated.
        # Support will be removed in AVD version 6.0.0.
        # Use <samp>redistribute</samp> instead.
        redistribute_routes:
          - source_protocol: <str; "connected" | "isis" | "ospf" | "ospfv3" | "static"; required>

            # Only applicable if `source_protocol` is `isis`.
            include_leaked: <bool>
            route_map: <str>

            # RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
            # Only applicable if `source_protocol` is `isis`.
            rcf: <str>

            # Routes learned by the OSPF protocol.
            # The `ospf_route_type` is valid for source_protocols 'ospf' and 'ospfv3'.
            ospf_route_type: <str; "external" | "internal" | "nssa-external" | "nssa-external 1" | "nssa-external 2">
      address_family_ipv6_sr_te:
        neighbors:
          - ip_address: <str; required; unique>
            activate: <bool>

            # Inbound route-map name.
            route_map_in: <str>

            # Outbound route-map name.
            route_map_out: <str>
        peer_groups:

            # Peer-group name.
          - name: <str; required; unique>
            activate: <bool>

            # Inbound route-map name.
            route_map_in: <str>

            # Outbound route-map name.
            route_map_out: <str>
      address_family_link_state:
        bgp:
          missing_policy:
            direction_in_action: <str; "deny" | "deny-in-out" | "permit">
            direction_out_action: <str; "deny" | "deny-in-out" | "permit">
        peer_groups:

            # Peer-group name.
          - name: <str; required; unique>
            activate: <bool>
            missing_policy:
              direction_in_action: <str; "deny" | "deny-in-out" | "permit">
              direction_out_action: <str; "deny" | "deny-in-out" | "permit">
        neighbors:
          - ip_address: <str; required; unique>
            activate: <bool>
            missing_policy:
              direction_in_action: <str; "deny" | "deny-in-out" | "permit">
              direction_out_action: <str; "deny" | "deny-in-out" | "permit">
        path_selection:
          roles:
            producer: <bool>
            consumer: <bool>
            propagator: <bool>
      address_family_flow_spec_ipv4:
        bgp:
          missing_policy:
            direction_in_action: <str; "deny" | "deny-in-out" | "permit">
            direction_out_action: <str; "deny" | "deny-in-out" | "permit">
        neighbors:
          - ip_address: <str; required; unique>
            activate: <bool>
        peer_groups:

            # Peer-group name.
          - name: <str; required; unique>
            activate: <bool>
      address_family_flow_spec_ipv6:
        bgp:
          missing_policy:
            direction_in_action: <str; "deny" | "deny-in-out" | "permit">
            direction_out_action: <str; "deny" | "deny-in-out" | "permit">
        neighbors:
          - ip_address: <str; required; unique>
            activate: <bool>
        peer_groups:

            # Peer-group name.
          - name: <str; required; unique>
            activate: <bool>
      address_family_path_selection:
        bgp:
          additional_paths:

            # Enable or disable reception of additional-paths.
            receive: <bool>

            # Select an option to send multiple paths for same prefix through bgp updates.
            # any: Send any eligible path.
            # backup: Best path and installed backup path.
            # ecmp: All paths in best path ECMP group.
            # limit: Limit to n eligible paths.
            # disabled: Disable sending any paths.
            send: <str; "any" | "backup" | "ecmp" | "limit" | "disabled">

            # Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`.
            send_limit: <int; 2-64>
        neighbors:
          - ip_address: <str; required; unique>
            activate: <bool>
            additional_paths:

              # Enable or disable reception of additional-paths.
              receive: <bool>

              # Select an option to send multiple paths for same prefix through bgp updates.
              # any: Send any eligible path.
              # backup: Best path and installed backup path.
              # ecmp: All paths in best path ECMP group.
              # limit: Limit to n eligible paths.
              # disabled: Disable sending any paths.
              send: <str; "any" | "backup" | "ecmp" | "limit" | "disabled">

              # Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`.
              send_limit: <int; 2-64>
        peer_groups:

            # Peer-group name.
          - name: <str; required; unique>
            activate: <bool>
            additional_paths:

              # Enable or disable reception of additional-paths.
              receive: <bool>

              # Select an option to send multiple paths for same prefix through bgp updates.
              # any: Send any eligible path.
              # backup: Best path and installed backup path.
              # ecmp: All paths in best path ECMP group.
              # limit: Limit to n eligible paths.
              # disabled: Disable sending any paths.
              send: <str; "any" | "backup" | "ecmp" | "limit" | "disabled">

              # Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`.
              send_limit: <int; 2-64>
      address_family_vpn_ipv4:
        domain_identifier: <str>
        peer_groups:

            # Peer-group name.
          - name: <str; required; unique>
            activate: <bool>

            # Inbound route-map name.
            route_map_in: <str>

            # Outbound route-map name.
            route_map_out: <str>

            # Inbound RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            rcf_in: <str>

            # Outbound RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            rcf_out: <str>
            default_route:
              enabled: <bool>

              # RCF function name with parenthesis.
              # Example: MyFunction(myarg).
              rcf: <str>
              route_map: <str>
        route:
          import_match_failure_action: <str; "discard">
        neighbors:
          - ip_address: <str; required; unique>
            activate: <bool>

            # Inbound route-map name.
            route_map_in: <str>

            # Outbound route-map name.
            route_map_out: <str>

            # Inbound RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            rcf_in: <str>

            # Outbound RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            rcf_out: <str>
            default_route:
              enabled: <bool>

              # RCF function name with parenthesis.
              # Example: MyFunction(myarg).
              rcf: <str>
              route_map: <str>
        neighbor_default_encapsulation_mpls_next_hop_self:
          source_interface: <str>
      address_family_vpn_ipv6:
        domain_identifier: <str>
        peer_groups:

            # Peer-group name.
          - name: <str; required; unique>
            activate: <bool>

            # Inbound route-map name.
            route_map_in: <str>

            # Outbound route-map name.
            route_map_out: <str>

            # Inbound RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            rcf_in: <str>

            # Outbound RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            rcf_out: <str>
            default_route:
              enabled: <bool>

              # RCF function name with parenthesis.
              # Example: MyFunction(myarg).
              rcf: <str>
              route_map: <str>
        route:
          import_match_failure_action: <str; "discard">
        neighbors:
          - ip_address: <str; required; unique>
            activate: <bool>

            # Inbound route-map name.
            route_map_in: <str>

            # Outbound route-map name.
            route_map_out: <str>

            # Inbound RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            rcf_in: <str>

            # Outbound RCF function name with parenthesis.
            # Example: MyFunction(myarg).
            rcf_out: <str>
            default_route:
              enabled: <bool>

              # RCF function name with parenthesis.
              # Example: MyFunction(myarg).
              rcf: <str>
              route_map: <str>
        neighbor_default_encapsulation_mpls_next_hop_self:
          source_interface: <str>
      vrfs:

          # VRF name.
        - name: <str; required; unique>
          bgp:

            # Allow redistribution of iBGP routes into an Interior Gateway Protocol (IGP). EOS default is true.
            redistribute_internal: <bool>
            additional_paths:

              # Install BGP backup path.
              install: <bool>

              # Allow additional path with ECMP primary path.
              install_ecmp_primary: <bool>

              # Enable or disable reception of additional-paths.
              receive: <bool>

              # Select an option to send multiple paths for same prefix through bgp updates.
              # any: Send any eligible path.
              # backup: Best path and installed backup path.
              # ecmp: All paths in best path ECMP group.
              # limit: Limit to n eligible paths.
              # disabled: Disable sending any paths.
              send: <str; "any" | "backup" | "ecmp" | "limit" | "disabled">

              # Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`.
              send_limit: <int; 2-64>

          # Route distinguisher.
          rd: <str>
          evpn_multicast: <bool>

          # Enable per-AF EVPN multicast settings.
          evpn_multicast_address_family:
            ipv4:

              # Enable EVPN multicast transit mode.
              transit: <bool>
          evpn_multicast_gateway_dr_election:

            # DR election algorithms:
            #   hrw: Default selection based on highest random weight.
            #   modulus: Selection based on VLAN ID modulo number of candidates.
            #   preference: Selection based on a configured preference value.
            algorithm: <str; "hrw" | "modulus" | "preference"; required>

            # Required when `algorithm` is `preference`.
            preference_value: <int; 0-65535>

          # Enable default-originate per VRF/address-family.
          default_route_exports:
            - address_family: <str; "evpn" | "vpn-ipv4" | "vpn-ipv6"; required; unique>
              always: <bool>
              route_map: <str>

              # RCF function name with parenthesis.
              # Example: MyFunction(myarg).
              rcf: <str>
          route_targets:
            import:
              - address_family: <str; required; unique>
                route_targets:
                  - <str>

                # Only applicable if `address_family` is one of `evpn`, `vpn-ipv4` or `vpn-ipv6`.
                route_map: <str>

                # RCF function name with parenthesis.
                # Example: MyFunction(myarg).
                # Only applicable if `address_family` is one of `evpn`, `vpn-ipv4` or `vpn-ipv6`.
                rcf: <str>

                # RCF function name with parenthesis for filtering VPN routes. Also requires `rcf` to be set.
                # Example: MyFunction(myarg).
                # Only applicable if `address_family` is one of `vpn-ipv4` or `vpn-ipv6`.
                vpn_route_filter_rcf: <str>
            export:
              - address_family: <str; required; unique>
                route_targets:
                  - <str>

                # Only applicable if `address_family` is one of `evpn`, `vpn-ipv4` or `vpn-ipv6`.
                route_map: <str>

                # RCF function name with parenthesis.
                # Example: MyFunction(myarg).
                # Only applicable if `address_family` is one of `evpn`, `vpn-ipv4` or `vpn-ipv6`.
                rcf: <str>

                # RCF function name with parenthesis for filtering VPN routes. Also requires `rcf` to be set.
                # Example: MyFunction(myarg).
                # Only applicable if `address_family` is one of `vpn-ipv4` or `vpn-ipv6`.
                vpn_route_filter_rcf: <str>

          # in IP address format A.B.C.D.
          router_id: <str>

          # BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>".
          timers: <str>
          networks:

              # IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I".
            - prefix: <str; required; unique>
              route_map: <str>
          maximum_paths:
            paths: <int; 1-600; required>
            ecmp: <int; 1-600>
          updates:

            # Disables FIB updates and route advertisement when the BGP instance is initiated until the BGP convergence state is reached.
            wait_for_convergence: <bool>

            # Do not advertise reachability to a prefix until that prefix has been installed in hardware.
            # This will eliminate any temporary black holes due to a BGP speaker advertising reachability to a prefix that may not yet be installed into the forwarding plane.
            wait_install: <bool>

          # Improved "listen_ranges" data model to support multiple listen ranges and additional filter capabilities.
          listen_ranges:

              # IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I".
            - prefix: <str>

              # Include router ID as part of peer filter.
              peer_id_include_router_id: <bool>

              # Peer-group name.
              peer_group: <str>

              # Peer-filter name.
              # note: `peer_filter`` or `remote_as` is required but mutually exclusive.
              # If both are defined, peer_filter takes precedence.
              peer_filter: <str>

              # BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
              # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
              remote_as: <str>
          neighbors:
            - ip_address: <str; required; unique>

              # Peer-group name.
              peer_group: <str>

              # BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
              # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
              remote_as: <str>
              password: <str>
              passive: <bool>

              # Remove private AS numbers in outbound AS path.
              remove_private_as:
                enabled: <bool>
                all: <bool>
                replace_as: <bool>
              remove_private_as_ingress:
                enabled: <bool>
                replace_as: <bool>
              weight: <int; 0-65535>

              # BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
              # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
              local_as: <str>

              # BGP AS-PATH options.
              as_path:

                # Replace AS number with local AS number.
                remote_as_replace_out: <bool>

                # Disable prepending own AS number to AS path.
                prepend_own_disabled: <bool>
              description: <str>
              route_reflector_client: <bool>

              # Time-to-live in range of hops.
              ebgp_multihop: <int; 1-255>
              next_hop_self: <bool>
              shutdown: <bool>

              # Enable BFD.
              bfd: <bool>

              # Override default BFD timers. BFD must be enabled with `bfd: true`.
              bfd_timers:

                # Interval in milliseconds.
                interval: <int; 50-60000; required>

                # Rate in milliseconds.
                min_rx: <int; 50-60000; required>
                multiplier: <int; 3-50; required>

              # BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>".
              timers: <str>
              rib_in_pre_policy_retain:
                enabled: <bool>
                all: <bool>

              # 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)'.
              send_community: <str>
              maximum_routes: <int>

              # Maximum number of routes after which a warning is issued (0 means never warn) or
              # Percentage of maximum number of routes at which to warn ("<1-100> percent").
              maximum_routes_warning_limit: <str>
              maximum_routes_warning_only: <bool>
              allowas_in:
                enabled: <bool>

                # Number of local ASNs allowed in a BGP update.
                times: <int; 1-10>
              default_originate:
                enabled: <bool>
                always: <bool>
                route_map: <str>
              update_source: <str>

              # Inbound route-map name.
              route_map_in: <str>

              # Outbound route-map name.
              route_map_out: <str>
              additional_paths:

                # Enable or disable reception of additional-paths.
                receive: <bool>

                # Select an option to send multiple paths for same prefix through bgp updates.
                # any: Send any eligible path.
                # backup: Best path and installed backup path.
                # ecmp: All paths in best path ECMP group.
                # limit: Limit to n eligible paths.
                # disabled: Disable sending any paths.
                send: <str; "any" | "backup" | "ecmp" | "limit" | "disabled">

                # Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`.
                send_limit: <int; 2-64>
          neighbor_interfaces:

              # Interface name.
            - name: <str; required; unique>

              # BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
              # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
              remote_as: <str>

              # Peer-group name.
              peer_group: <str>

              # Peer-filter name.
              peer_filter: <str>
              description: <str>

          # Redistribute routes in to BGP.
          redistribute:
            attached_host:
              enabled: <bool; required>
              route_map: <str>
            bgp:
              enabled: <bool; required>
              route_map: <str>
            connected:
              enabled: <bool; required>
              route_map: <str>

              # RCF function name with parenthesis.
              # Example: MyFunction(myarg).
              # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
              rcf: <str>

              # Include following routes while redistributing.
              include_leaked: <bool>
            dynamic:
              enabled: <bool; required>
              route_map: <str>

              # RCF function name with parenthesis.
              # Example: MyFunction(myarg).
              # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
              rcf: <str>
            isis:
              enabled: <bool; required>

              # Redistribute IS-IS route level.
              isis_level: <str; "level-1" | "level-2" | "level-1-2">
              route_map: <str>

              # RCF function name with parenthesis.
              # Example: MyFunction(myarg).
              # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
              rcf: <str>

              # Include following routes while redistributing.
              include_leaked: <bool>
            ospf:

              # Redistribute OSPF routes.
              enabled: <bool>

              # Redistribute OSPF routes learned from external sources.
              match_external:
                enabled: <bool; required>
                route_map: <str>

                # Include following routes while redistributing.
                include_leaked: <bool>

              # Redistribute OSPF routes learned from internal sources.
              match_internal:
                enabled: <bool; required>
                route_map: <str>

                # Include following routes while redistributing.
                include_leaked: <bool>

              # Redistribute OSPF routes learned from external NSSA sources.
              match_nssa_external:
                enabled: <bool; required>

                # NSSA External Type Number.
                nssa_type: <int; 1 | 2>
                route_map: <str>

                # Include following routes while redistributing.
                include_leaked: <bool>
              route_map: <str>

              # Include following routes while redistributing.
              include_leaked: <bool>
            ospfv3:

              # Redistribute OSPFv3 routes.
              enabled: <bool>

              # Redistribute OSPFv3 routes learned from external sources.
              match_external:
                enabled: <bool; required>
                route_map: <str>

                # Include following routes while redistributing.
                include_leaked: <bool>

              # Redistribute OSPFv3 routes learned from internal sources.
              match_internal:
                enabled: <bool; required>
                route_map: <str>

                # Include following routes while redistributing.
                include_leaked: <bool>

              # Redistribute OSPFv3 routes learned from external NSSA sources.
              match_nssa_external:
                enabled: <bool; required>

                # NSSA External Type Number.
                nssa_type: <int; 1 | 2>
                route_map: <str>

                # Include following routes while redistributing.
                include_leaked: <bool>
              route_map: <str>

              # Include following routes while redistributing.
              include_leaked: <bool>
            rip:
              enabled: <bool; required>
              route_map: <str>
            static:
              enabled: <bool; required>
              route_map: <str>

              # RCF function name with parenthesis.
              # Example: MyFunction(myarg).
              # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
              rcf: <str>

              # Include following routes while redistributing.
              include_leaked: <bool>
            user:
              enabled: <bool; required>

              # RCF function name with parenthesis.
              # Example: MyFunction(myarg).
              # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
              rcf: <str>
          # This key is deprecated.
          # Support will be removed in AVD version 6.0.0.
          # Use <samp>redistribute</samp> instead.
          redistribute_routes:
            - source_protocol: <str; required>
              route_map: <str>
              include_leaked: <bool>

              # RCF function name with parenthesis.
              # Example: MyFunction(myarg).
              # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
              # Only applicable if `source_protocol` is one of `connected`, `dynamic`, `isis`, `static` and `user`.
              rcf: <str>

              # Routes learned by the OSPF protocol.
              # The `ospf_route_type` is valid for source_protocols 'ospf' and 'ospfv3'.
              ospf_route_type: <str; "external" | "internal" | "nssa-external" | "nssa-external 1" | "nssa-external 2">
          aggregate_addresses:

              # IPv4 prefix "A.B.C.D/E" or IPv6 prefix "A:B:C:D:E:F:G:H/I".
            - prefix: <str; required; unique>
              advertise_only: <bool>
              as_set: <bool>
              summary_only: <bool>
              attribute_map: <str>
              match_map: <str>
          address_family_ipv4:
            bgp:
              missing_policy:
                direction_in_action: <str; "deny" | "deny-in-out" | "permit">
                direction_out_action: <str; "deny" | "deny-in-out" | "permit">
              additional_paths:

                # Install BGP backup path.
                install: <bool>

                # Allow additional path with ECMP primary path.
                install_ecmp_primary: <bool>

                # Enable or disable reception of additional-paths.
                receive: <bool>

                # Select an option to send multiple paths for same prefix through bgp updates.
                # any: Send any eligible path.
                # backup: Best path and installed backup path.
                # ecmp: All paths in best path ECMP group.
                # limit: Limit to n eligible paths.
                # disabled: Disable sending any paths.
                send: <str; "any" | "backup" | "ecmp" | "limit" | "disabled">

                # Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`.
                send_limit: <int; 2-64>

              # Allow redistribution of iBGP routes into an Interior Gateway Protocol (IGP). EOS default is true.
              redistribute_internal: <bool>
            neighbors:
              - ip_address: <str; required; unique>
                activate: <bool>

                # Inbound route-map name.
                route_map_in: <str>

                # Outbound route-map name.
                route_map_out: <str>

                # Inbound RCF function name with parenthesis.
                # Example: MyFunction(myarg).
                rcf_in: <str>

                # Outbound RCF function name with parenthesis.
                # Example: MyFunction(myarg).
                rcf_out: <str>

                # Inbound prefix-list name.
                prefix_list_in: <str>

                # Outbound prefix-list name.
                prefix_list_out: <str>
                next_hop:
                  address_family_ipv6:
                    enabled: <bool; required>
                    originate: <bool>
                additional_paths:

                  # Enable or disable reception of additional-paths.
                  receive: <bool>

                  # Select an option to send multiple paths for same prefix through bgp updates.
                  # any: Send any eligible path.
                  # backup: Best path and installed backup path.
                  # ecmp: All paths in best path ECMP group.
                  # limit: Limit to n eligible paths.
                  # disabled: Disable sending any paths.
                  send: <str; "any" | "backup" | "ecmp" | "limit" | "disabled">

                  # Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`.
                  send_limit: <int; 2-64>
            networks:

                # IPv4 prefix "A.B.C.D/E".
              - prefix: <str; required; unique>
                route_map: <str>

            # Redistribute routes in to BGP.
            redistribute:
              attached_host:
                enabled: <bool; required>
                route_map: <str>
              bgp:
                enabled: <bool; required>
                route_map: <str>
              connected:
                enabled: <bool; required>
                route_map: <str>

                # RCF function name with parenthesis.
                # Example: MyFunction(myarg).
                # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
                rcf: <str>

                # Include following routes while redistributing.
                include_leaked: <bool>
              dynamic:
                enabled: <bool; required>
                route_map: <str>

                # RCF function name with parenthesis.
                # Example: MyFunction(myarg).
                # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
                rcf: <str>
              isis:
                enabled: <bool; required>

                # Redistribute IS-IS route level.
                isis_level: <str; "level-1" | "level-2" | "level-1-2">
                route_map: <str>

                # RCF function name with parenthesis.
                # Example: MyFunction(myarg).
                # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
                rcf: <str>

                # Include following routes while redistributing.
                include_leaked: <bool>
              ospf:

                # Redistribute OSPF routes.
                enabled: <bool>

                # Redistribute OSPF routes learned from external sources.
                match_external:
                  enabled: <bool; required>
                  route_map: <str>

                  # Include following routes while redistributing.
                  include_leaked: <bool>

                # Redistribute OSPF routes learned from internal sources.
                match_internal:
                  enabled: <bool; required>
                  route_map: <str>

                  # Include following routes while redistributing.
                  include_leaked: <bool>

                # Redistribute OSPF routes learned from external NSSA sources.
                match_nssa_external:
                  enabled: <bool; required>

                  # NSSA External Type Number.
                  nssa_type: <int; 1 | 2>
                  route_map: <str>

                  # Include following routes while redistributing.
                  include_leaked: <bool>
                route_map: <str>

                # Include following routes while redistributing.
                include_leaked: <bool>
              ospfv3:

                # Redistribute OSPFv3 routes.
                enabled: <bool>

                # Redistribute OSPFv3 routes learned from external sources.
                match_external:
                  enabled: <bool; required>
                  route_map: <str>

                  # Include following routes while redistributing.
                  include_leaked: <bool>

                # Redistribute OSPFv3 routes learned from internal sources.
                match_internal:
                  enabled: <bool; required>
                  route_map: <str>

                  # Include following routes while redistributing.
                  include_leaked: <bool>

                # Redistribute OSPFv3 routes learned from external NSSA sources.
                match_nssa_external:
                  enabled: <bool; required>

                  # NSSA External Type Number.
                  nssa_type: <int; 1 | 2>
                  route_map: <str>

                  # Include following routes while redistributing.
                  include_leaked: <bool>
                route_map: <str>

                # Include following routes while redistributing.
                include_leaked: <bool>
              rip:
                enabled: <bool; required>
                route_map: <str>
              static:
                enabled: <bool; required>
                route_map: <str>

                # RCF function name with parenthesis.
                # Example: MyFunction(myarg).
                # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
                rcf: <str>

                # Include following routes while redistributing.
                include_leaked: <bool>
              user:
                enabled: <bool; required>

                # RCF function name with parenthesis.
                # Example: MyFunction(myarg).
                # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
                rcf: <str>
            # This key is deprecated.
            # Support will be removed in AVD version 6.0.0.
            # Use <samp>redistribute</samp> instead.
            redistribute_routes:
              - source_protocol: <str; "attached-host" | "bgp" | "connected" | "dynamic" | "isis" | "ospf" | "ospfv3" | "rip" | "static" | "user"; required>
                route_map: <str>
                include_leaked: <bool>

                # RCF function name with parenthesis.
                # Example: MyFunction(myarg).
                # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
                # Only applicable if `source_protocol` is one of `connected`, `dynamic`, `isis`, `static` and `user`.
                rcf: <str>

                # Routes learned by the OSPF protocol.
                # The `ospf_route_type` is valid for source_protocols 'ospf' and 'ospfv3'.
                ospf_route_type: <str; "external" | "internal" | "nssa-external" | "nssa-external 1" | "nssa-external 2">
          address_family_ipv6:
            bgp:
              missing_policy:
                direction_in_action: <str; "deny" | "deny-in-out" | "permit">
                direction_out_action: <str; "deny" | "deny-in-out" | "permit">
              additional_paths:

                # Install BGP backup path.
                install: <bool>

                # Allow additional path with ECMP primary path.
                install_ecmp_primary: <bool>

                # Enable or disable reception of additional-paths.
                receive: <bool>

                # Select an option to send multiple paths for same prefix through bgp updates.
                # any: Send any eligible path.
                # backup: Best path and installed backup path.
                # ecmp: All paths in best path ECMP group.
                # limit: Limit to n eligible paths.
                # disabled: Disable sending any paths.
                send: <str; "any" | "backup" | "ecmp" | "limit" | "disabled">

                # Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`.
                send_limit: <int; 2-64>

              # Allow redistribution of iBGP routes into an Interior Gateway Protocol (IGP). EOS default is true.
              redistribute_internal: <bool>
            neighbors:
              - ip_address: <str; required; unique>
                activate: <bool>

                # Inbound route-map name.
                route_map_in: <str>

                # Outbound route-map name.
                route_map_out: <str>

                # Inbound RCF function name with parenthesis.
                # Example: MyFunction(myarg).
                rcf_in: <str>

                # Outbound RCF function name with parenthesis.
                # Example: MyFunction(myarg).
                rcf_out: <str>

                # Inbound prefix-list name.
                prefix_list_in: <str>

                # Outbound prefix-list name.
                prefix_list_out: <str>
                additional_paths:

                  # Enable or disable reception of additional-paths.
                  receive: <bool>

                  # Select an option to send multiple paths for same prefix through bgp updates.
                  # any: Send any eligible path.
                  # backup: Best path and installed backup path.
                  # ecmp: All paths in best path ECMP group.
                  # limit: Limit to n eligible paths.
                  # disabled: Disable sending any paths.
                  send: <str; "any" | "backup" | "ecmp" | "limit" | "disabled">

                  # Number of paths to send through bgp updates. For this setting, `send` must be set to `limit` or `ecmp`.
                  send_limit: <int; 2-64>
            networks:

                # IPv6 prefix "A:B:C:D:E:F:G:H/I".
              - prefix: <str; required; unique>
                route_map: <str>

            # Redistribute routes in to BGP.
            redistribute:
              attached_host:
                enabled: <bool; required>
                route_map: <str>
              bgp:
                enabled: <bool; required>
                route_map: <str>
              connected:
                enabled: <bool; required>
                route_map: <str>

                # RCF function name with parenthesis.
                # Example: MyFunction(myarg).
                # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
                rcf: <str>

                # Include following routes while redistributing.
                include_leaked: <bool>
              dhcp:
                enabled: <bool; required>
                route_map: <str>
              dynamic:
                enabled: <bool; required>
                route_map: <str>

                # RCF function name with parenthesis.
                # Example: MyFunction(myarg).
                # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
                rcf: <str>
              isis:
                enabled: <bool; required>

                # Redistribute IS-IS route level.
                isis_level: <str; "level-1" | "level-2" | "level-1-2">
                route_map: <str>

                # RCF function name with parenthesis.
                # Example: MyFunction(myarg).
                # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
                rcf: <str>

                # Include following routes while redistributing.
                include_leaked: <bool>
              ospfv3:

                # Redistribute OSPFv3 routes.
                enabled: <bool>

                # Redistribute OSPFv3 routes learned from external sources.
                match_external:
                  enabled: <bool; required>
                  route_map: <str>

                  # Include following routes while redistributing.
                  include_leaked: <bool>

                # Redistribute OSPFv3 routes learned from internal sources.
                match_internal:
                  enabled: <bool; required>
                  route_map: <str>

                  # Include following routes while redistributing.
                  include_leaked: <bool>

                # Redistribute OSPFv3 routes learned from external NSSA sources.
                match_nssa_external:
                  enabled: <bool; required>

                  # NSSA External Type Number.
                  nssa_type: <int; 1 | 2>
                  route_map: <str>

                  # Include following routes while redistributing.
                  include_leaked: <bool>
                route_map: <str>

                # Include following routes while redistributing.
                include_leaked: <bool>
              static:
                enabled: <bool; required>
                route_map: <str>

                # RCF function name with parenthesis.
                # Example: MyFunction(myarg).
                # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
                rcf: <str>

                # Include following routes while redistributing.
                include_leaked: <bool>
              user:
                enabled: <bool; required>

                # RCF function name with parenthesis.
                # Example: MyFunction(myarg).
                # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
                rcf: <str>
            # This key is deprecated.
            # Support will be removed in AVD version 6.0.0.
            # Use <samp>redistribute</samp> instead.
            redistribute_routes:
              - source_protocol: <str; "attached-host" | "bgp" | "connected" | "dhcp" | "dynamic" | "isis" | "ospfv3" | "static" | "user"; required>
                route_map: <str>
                include_leaked: <bool>

                # RCF function name with parenthesis.
                # Example: MyFunction(myarg).
                # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
                # Only applicable if `source_protocol` is one of `connected`, `dynamic`, `isis`, `static` and `user`.
                rcf: <str>

                # Routes learned by the OSPF protocol.
                # The `ospf_route_type` is valid for source_protocols 'ospfv3'.
                ospf_route_type: <str; "external" | "internal" | "nssa-external" | "nssa-external 1" | "nssa-external 2">
          address_family_ipv4_multicast:
            bgp:
              missing_policy:
                direction_in_action: <str; "deny" | "deny-in-out" | "permit">
                direction_out_action: <str; "deny" | "deny-in-out" | "permit">
              additional_paths:
                receive: <bool>
            neighbors:
              - ip_address: <str; required; unique>
                activate: <bool>

                # Inbound route-map name.
                route_map_in: <str>

                # Outbound route-map name.
                route_map_out: <str>
                additional_paths:
                  receive: <bool>
            networks:

                # IPv6 prefix "A.B.C.D/E".
              - prefix: <str; required; unique>
                route_map: <str>

            # Redistribute routes in to BGP.
            redistribute:
              attached_host:
                enabled: <bool; required>
                route_map: <str>
              connected:
                enabled: <bool; required>
                route_map: <str>
              isis:
                enabled: <bool; required>

                # Redistribute IS-IS route level.
                isis_level: <str; "level-1" | "level-2" | "level-1-2">
                route_map: <str>

                # RCF function name with parenthesis.
                # Example: MyFunction(myarg).
                # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
                rcf: <str>

                # Include following routes while redistributing.
                include_leaked: <bool>
              ospf:

                # Redistribute OSPF routes.
                enabled: <bool>

                # Redistribute OSPF routes learned from external sources.
                match_external:
                  enabled: <bool; required>
                  route_map: <str>

                # Redistribute OSPF routes learned from internal sources.
                match_internal:
                  enabled: <bool; required>
                  route_map: <str>

                # Redistribute OSPF routes learned from external NSSA sources.
                match_nssa_external:
                  enabled: <bool; required>

                  # NSSA External Type Number.
                  nssa_type: <int; 1 | 2>
                  route_map: <str>
                route_map: <str>
              ospfv3:

                # Redistribute OSPFv3 routes.
                enabled: <bool>

                # Redistribute OSPFv3 routes learned from external sources.
                match_external:
                  enabled: <bool; required>
                  route_map: <str>

                  # Include following routes while redistributing.
                  include_leaked: <bool>

                # Redistribute OSPFv3 routes learned from internal sources.
                match_internal:
                  enabled: <bool; required>
                  route_map: <str>

                  # Include following routes while redistributing.
                  include_leaked: <bool>

                # Redistribute OSPFv3 routes learned from external NSSA sources.
                match_nssa_external:
                  enabled: <bool; required>

                  # NSSA External Type Number.
                  nssa_type: <int; 1 | 2>
                  route_map: <str>

                  # Include following routes while redistributing.
                  include_leaked: <bool>
                route_map: <str>

                # Include following routes while redistributing.
                include_leaked: <bool>
              static:
                enabled: <bool; required>
                route_map: <str>
            # This key is deprecated.
            # Support will be removed in AVD version 6.0.0.
            # Use <samp>redistribute</samp> instead.
            redistribute_routes:
              - source_protocol: <str; "attached-host" | "connected" | "isis" | "ospf" | "ospfv3" | "static"; required>
                route_map: <str>

                # Only applicable if `source_protocol` is `isis`.
                include_leaked: <bool>

                # RCF function name with parenthesis.
                # Example: MyFunction(myarg).
                # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
                # Only applicable if `source_protocol` is `isis`.
                rcf: <str>

                # Routes learned by the OSPF protocol.
                # The `ospf_route_type` is valid for source_protocols 'ospf' and 'ospfv3'.
                ospf_route_type: <str; "external" | "internal" | "nssa-external" | "nssa-external 1" | "nssa-external 2">
          address_family_ipv6_multicast:
            bgp:
              missing_policy:
                direction_in_action: <str; "deny" | "deny-in-out" | "permit">
                direction_out_action: <str; "deny" | "deny-in-out" | "permit">
              additional_paths:
                receive: <bool>
            neighbors:
              - ip_address: <str; required; unique>
                activate: <bool>

                # Inbound route-map name.
                route_map_in: <str>

                # Outbound route-map name.
                route_map_out: <str>
                additional_paths:
                  receive: <bool>
            networks:

                # IPv6 prefix "A:B:C:D:E:F:G:H/I".
              - prefix: <str; required; unique>
                route_map: <str>

            # Redistribute routes in to BGP.
            redistribute:
              connected:
                enabled: <bool; required>
                route_map: <str>
              isis:
                enabled: <bool; required>

                # Redistribute IS-IS route level.
                isis_level: <str; "level-1" | "level-2" | "level-1-2">
                route_map: <str>

                # RCF function name with parenthesis.
                # Example: MyFunction(myarg).
                # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
                rcf: <str>

                # Include following routes while redistributing.
                include_leaked: <bool>
              ospf:

                # Redistribute OSPF routes.
                enabled: <bool>

                # Redistribute OSPF routes learned from external sources.
                match_external:
                  enabled: <bool; required>
                  route_map: <str>

                # Redistribute OSPF routes learned from internal sources.
                match_internal:
                  enabled: <bool; required>
                  route_map: <str>

                # Redistribute OSPF routes learned from external NSSA sources.
                match_nssa_external:
                  enabled: <bool; required>

                  # NSSA External Type Number.
                  nssa_type: <int; 1 | 2>
                  route_map: <str>
                route_map: <str>
              ospfv3:

                # Redistribute OSPFv3 routes.
                enabled: <bool>

                # Redistribute OSPFv3 routes learned from external sources.
                match_external:
                  enabled: <bool; required>
                  route_map: <str>

                # Redistribute OSPFv3 routes learned from internal sources.
                match_internal:
                  enabled: <bool; required>
                  route_map: <str>

                # Redistribute OSPFv3 routes learned from external NSSA sources.
                match_nssa_external:
                  enabled: <bool; required>

                  # NSSA External Type Number.
                  nssa_type: <int; 1 | 2>
                  route_map: <str>
                route_map: <str>
              static:
                enabled: <bool; required>
                route_map: <str>
            # This key is deprecated.
            # Support will be removed in AVD version 6.0.0.
            # Use <samp>redistribute</samp> instead.
            redistribute_routes:
              - source_protocol: <str; "connected" | "isis" | "ospf" | "ospfv3" | "static"; required>
                route_map: <str>

                # Only applicable if `source_protocol` is `isis`.
                include_leaked: <bool>

                # RCF function name with parenthesis.
                # Example: MyFunction(myarg).
                # `route_map` and `rcf` are mutually exclusive. `route_map` takes precedence.
                # Only applicable if `source_protocol` is `isis`.
                rcf: <str>

                # Routes learned by the OSPF protocol.
                # The `ospf_route_type` is valid for source_protocols 'ospf' and 'ospfv3'.
                ospf_route_type: <str; "external" | "internal" | "nssa-external" | "nssa-external 1" | "nssa-external 2">
          address_family_flow_spec_ipv4:
            bgp:
              missing_policy:
                direction_in_action: <str; "deny" | "deny-in-out" | "permit">
                direction_out_action: <str; "deny" | "deny-in-out" | "permit">
            neighbors:
              - ip_address: <str; required; unique>
                activate: <bool>
          address_family_flow_spec_ipv6:
            bgp:
              missing_policy:
                direction_in_action: <str; "deny" | "deny-in-out" | "permit">
                direction_out_action: <str; "deny" | "deny-in-out" | "permit">
            neighbors:
              - ip_address: <str; required; unique>
                activate: <bool>

          # Multiline EOS CLI rendered directly on the Router BGP, VRF definition in the final EOS configuration.
          eos_cli: <str>
      session_trackers:

          # Name of session tracker.
        - name: <str; required; unique>

          # Recovery delay in seconds.
          recovery_delay: <int; 1-3600>

      # Multiline EOS CLI rendered directly on the Router BGP in the final EOS configuration.
      eos_cli: <str>
    ```
