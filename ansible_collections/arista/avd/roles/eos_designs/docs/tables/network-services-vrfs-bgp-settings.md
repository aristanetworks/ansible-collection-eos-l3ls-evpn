<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;network_services_keys.name&gt;</samp>](## "<network_services_keys.name>") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "<network_services_keys.name>.[].name") | String | Required, Unique |  |  | Specify a tenant name.<br>Tenant provide a construct to group L3 VRFs and L2 VLANs.<br>Networks services can be filtered by tenant name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_peer_groups</samp>](## "<network_services_keys.name>.[].bgp_peer_groups") | List, items: Dictionary |  |  |  | List of BGP peer groups definitions.<br>This will configure BGP peer groups to be used inside the tenant VRF for peering with external devices.<br>Since BGP peer groups are configured at higher BGP level, shared between VRFs,<br>peer_group names should not overlap between VRFs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].name") | String | Required, Unique |  |  | BGP peer group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].nodes") | List, items: String |  |  |  | Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network.<br>If not set the peer-group is created on devices which have a bgp_peer mapped to the corresponding peer_group.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].nodes.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv4</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].address_family_ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].address_family_ipv4.activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].address_family_ipv4.route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].address_family_ipv4.route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_in</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].address_family_ipv4.rcf_in") | String |  |  |  | Inbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_out</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].address_family_ipv4.rcf_out") | String |  |  |  | Outbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].address_family_ipv4.default_originate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].address_family_ipv4.default_originate.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].address_family_ipv4.default_originate.route_map") | String |  |  |  | Route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].address_family_ipv4.next_hop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv6</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].address_family_ipv4.next_hop.address_family_ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].address_family_ipv4.next_hop.address_family_ipv6.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;originate</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].address_family_ipv4.next_hop.address_family_ipv6.originate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv6_originate</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].address_family_ipv4.next_hop.address_family_ipv6_originate") <span style="color:red">removed</span> | Boolean |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>address_family_ipv6</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].address_family_ipv4.prefix_list_in") | String |  |  |  | Inbound prefix-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].address_family_ipv4.prefix_list_out") | String |  |  |  | Outbound prefix-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv6</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].address_family_ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].address_family_ipv6.activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].address_family_ipv6.route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].address_family_ipv6.route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_in</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].address_family_ipv6.rcf_in") | String |  |  |  | Inbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_out</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].address_family_ipv6.rcf_out") | String |  |  |  | Outbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].address_family_ipv6.prefix_list_in") | String |  |  |  | Inbound prefix-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].address_family_ipv6.prefix_list_out") | String |  |  |  | Outbound prefix-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].type") | String |  |  |  | Key only used for documentation or validation purposes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].remote_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].local_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as_path</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].as_path") | Dictionary |  |  |  | BGP AS-PATH options. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as_replace_out</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].as_path.remote_as_replace_out") | Boolean |  |  |  | Replace AS number with local AS number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prepend_own_disabled</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].as_path.prepend_own_disabled") | Boolean |  |  |  | Disable prepending own AS number to AS path. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].remove_private_as") | Dictionary |  |  |  | Remove private AS numbers in outbound AS path. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].remove_private_as.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].remove_private_as.all") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].remove_private_as.replace_as") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as_ingress</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].remove_private_as_ingress") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].remove_private_as_ingress.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].remove_private_as_ingress.replace_as") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_unchanged</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].next_hop_unchanged") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_source</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].update_source") | String |  |  |  | IP address or interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_reflector_client</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].route_reflector_client") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].bfd") | Boolean |  |  |  | Enable BFD. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd_timers</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].bfd_timers") | Dictionary |  |  |  | Override default BFD timers. BFD must be enabled with `bfd: true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].bfd_timers.interval") | Integer | Required |  | Min: 50<br>Max: 60000 | Interval in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].bfd_timers.min_rx") | Integer | Required |  | Min: 50<br>Max: 60000 | Rate in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].bfd_timers.multiplier") | Integer | Required |  | Min: 3<br>Max: 50 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp_multihop</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].ebgp_multihop") | Integer |  |  | Min: 1<br>Max: 255 | Time-to-live in range of hops. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].next_hop_self") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].password") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;passive</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].passive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].default_originate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].default_originate.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].default_originate.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].default_originate.route_map") | String |  |  |  | Route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_community</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].send_community") | String |  |  |  | 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].maximum_routes") | Integer |  |  | Min: 0<br>Max: 4294967294 | Maximum number of routes (0 means unlimited). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_limit</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].maximum_routes_warning_limit") | String |  |  |  | Maximum number of routes after which a warning is issued (0 means never warn) or<br>Percentage of maximum number of routes at which to warn ("<1-100> percent").<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_only</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].maximum_routes_warning_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].missing_policy") | Dictionary |  |  |  | Missing policy configuration for all address-families. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].missing_policy.direction_in") | Dictionary |  |  |  | Missing policy inbound direction. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].missing_policy.direction_in.action") | String | Required |  | Valid Values:<br>- <code>deny</code><br>- <code>permit</code><br>- <code>deny-in-out</code> | Missing policy action. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_community_list</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].missing_policy.direction_in.include_community_list") | Boolean |  |  |  | Include community-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_prefix_list</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].missing_policy.direction_in.include_prefix_list") | Boolean |  |  |  | Include prefix-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_sub_route_map</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].missing_policy.direction_in.include_sub_route_map") | Boolean |  |  |  | Include sub-route-map references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].missing_policy.direction_out") | Dictionary |  |  |  | Missing policy outbound direction. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].missing_policy.direction_out.action") | String | Required |  | Valid Values:<br>- <code>deny</code><br>- <code>permit</code><br>- <code>deny-in-out</code> | Missing policy action. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_community_list</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].missing_policy.direction_out.include_community_list") | Boolean |  |  |  | Include community-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_prefix_list</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].missing_policy.direction_out.include_prefix_list") | Boolean |  |  |  | Include prefix-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_sub_route_map</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].missing_policy.direction_out.include_sub_route_map") | Boolean |  |  |  | Include sub-route-map references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_bandwidth</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].link_bandwidth") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].link_bandwidth.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].link_bandwidth.default") | String |  |  |  | nn.nn(K|M|G) link speed in bits/second. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allowas_in</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].allowas_in") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].allowas_in.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;times</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].allowas_in.times") | Integer |  |  | Min: 1<br>Max: 10 | Number of local ASNs allowed in a BGP update. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].weight") | Integer |  |  | Min: 0<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].timers") | String |  |  |  | BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rib_in_pre_policy_retain</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].rib_in_pre_policy_retain") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].rib_in_pre_policy_retain.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].rib_in_pre_policy_retain.all") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session_tracker</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].session_tracker") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shared_secret</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].shared_secret") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].shared_secret.profile") | String | Required |  |  | Name of profile defined under `management_security`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].shared_secret.hash_algorithm") | String | Required |  | Valid Values:<br>- <code>aes-128-cmac-96</code><br>- <code>hmac-sha-256</code><br>- <code>hmac-sha1-96</code> | Note: Algorithm hmac-sha-256 requires EOS version 4.31.1F and above. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl_maximum_hops</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].ttl_maximum_hops") | Integer |  |  | Min: 0<br>Max: 254 | Maximum number of hops. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_filter</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].peer_filter") <span style="color:red">removed</span> | String |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>router_bgp.listen_ranges[].peer_filter</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_listen_range_prefix</samp>](## "<network_services_keys.name>.[].bgp_peer_groups.[].bgp_listen_range_prefix") <span style="color:red">removed</span> | String |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>router_bgp.listen_ranges[].bgp_listen_range_prefix</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "<network_services_keys.name>.[].vrfs") | List, items: Dictionary |  |  |  | VRFs will only be configured on a node if any of the underlying objects like `svis` or `l3_interfaces` apply to the node.<br><br>It is recommended to only define a VRF in one Tenant. If the same VRF name is used across multiple tenants and those tenants<br>are accepted by `filter.tenants` on the node, any object set under the duplicate VRFs must either be unique or be an exact match.<br><br>VRF "default" is partially supported under network-services. Currently the supported options for "default" vrf are route-target,<br>route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.<br>Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<network_services_keys.name>.[].vrfs.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_peers</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peers") | List, items: Dictionary |  |  |  | List of BGP peer definitions.<br>This will configure BGP neighbors inside the tenant VRF for peering with external devices.<br>The configured peer will automatically be activated for ipv4 or ipv6 address family based on the ip address.<br>Note, only ipv4 and ipv6 address families are currently supported in eos_designs.<br>For other address families, use custom_structured configuration with eos_cli_config_gen.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_address</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peers.[].ip_address") | String | Required |  |  | IPv4_address or IPv6_address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_group</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peers.[].peer_group") | String |  |  |  | Peer group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peers.[].remote_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peers.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peers.[].password") | String |  |  |  | Encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_community</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peers.[].send_community") | String |  |  |  | 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)'.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peers.[].next_hop_self") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peers.[].timers") | String |  |  |  | BGP Keepalive and Hold Timer values in seconds as string <0-3600> <0-3600>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peers.[].maximum_routes") | Integer |  |  | Min: 0<br>Max: 4294967294 | Maximum number of routes (0 means unlimited). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_only</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peers.[].maximum_routes_warning_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peers.[].default_originate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peers.[].default_originate.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_source</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peers.[].update_source") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp_multihop</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peers.[].ebgp_multihop") | Integer |  |  | Min: 1<br>Max: 255 | Time-to-live in range of hops. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peers.[].nodes") | List, items: String |  |  |  | Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peers.[].nodes.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set_ipv4_next_hop</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peers.[].set_ipv4_next_hop") | String |  |  |  | IPv4_address<br>Next hop settings can be either ipv4 or ipv6 for one neighbor, this will be applied by a uniquely generated route-map per neighbor.<br>Next hop takes precedence over route_map_out.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set_ipv6_next_hop</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peers.[].set_ipv6_next_hop") | String |  |  |  | IPv6_address<br>Next hop settings can be either ipv4 or ipv6 for one neighbor, this will be applied by a uniquely generated route-map per neighbor.<br>Next hop takes precedence over route_map_out.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peers.[].route_map_out") | String |  |  |  | Route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peers.[].route_map_in") | String |  |  |  | Route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peers.[].prefix_list_in") | String |  |  |  | Inbound prefix list name.<br>The prefix-list will be associated under the IPv4 or IPv6 address family based on the IP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peers.[].prefix_list_out") | String |  |  |  | Outbound prefix list name.<br>The prefix-list will be associated under the IPv4 or IPv6 address family based on the IP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peers.[].local_as") | String |  |  |  | Local BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peers.[].weight") | Integer |  |  | Min: 0<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peers.[].bfd") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peers.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_peer_groups</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups") | List, items: Dictionary |  |  |  | List of BGP peer groups definitions.<br>This will configure BGP peer groups to be used inside the tenant VRF for peering with external devices.<br>Since BGP peer groups are configured at higher BGP level, shared between VRFs,<br>peer_group names should not overlap between VRFs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].name") | String |  |  |  | BGP peer group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].nodes") | List, items: String |  |  |  | Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network.<br>If not set the peer-group is created on devices which have a bgp_peer mapped to the corresponding peer_group.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].nodes.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv4</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].address_family_ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].address_family_ipv4.activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].address_family_ipv4.route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].address_family_ipv4.route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_in</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].address_family_ipv4.rcf_in") | String |  |  |  | Inbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_out</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].address_family_ipv4.rcf_out") | String |  |  |  | Outbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].address_family_ipv4.default_originate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].address_family_ipv4.default_originate.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].address_family_ipv4.default_originate.route_map") | String |  |  |  | Route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].address_family_ipv4.next_hop") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv6</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].address_family_ipv4.next_hop.address_family_ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].address_family_ipv4.next_hop.address_family_ipv6.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;originate</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].address_family_ipv4.next_hop.address_family_ipv6.originate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv6_originate</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].address_family_ipv4.next_hop.address_family_ipv6_originate") <span style="color:red">removed</span> | Boolean |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>address_family_ipv6</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].address_family_ipv4.prefix_list_in") | String |  |  |  | Inbound prefix-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].address_family_ipv4.prefix_list_out") | String |  |  |  | Outbound prefix-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family_ipv6</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].address_family_ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;activate</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].address_family_ipv6.activate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].address_family_ipv6.route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].address_family_ipv6.route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_in</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].address_family_ipv6.rcf_in") | String |  |  |  | Inbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rcf_out</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].address_family_ipv6.rcf_out") | String |  |  |  | Outbound RCF function name with parenthesis.<br>Example: MyFunction(myarg). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_in</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].address_family_ipv6.prefix_list_in") | String |  |  |  | Inbound prefix-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list_out</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].address_family_ipv6.prefix_list_out") | String |  |  |  | Outbound prefix-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].type") | String |  |  |  | Key only used for documentation or validation purposes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].remote_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].local_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as_path</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].as_path") | Dictionary |  |  |  | BGP AS-PATH options. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_as_replace_out</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].as_path.remote_as_replace_out") | Boolean |  |  |  | Replace AS number with local AS number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prepend_own_disabled</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].as_path.prepend_own_disabled") | Boolean |  |  |  | Disable prepending own AS number to AS path. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].remove_private_as") | Dictionary |  |  |  | Remove private AS numbers in outbound AS path. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].remove_private_as.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].remove_private_as.all") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].remove_private_as.replace_as") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remove_private_as_ingress</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].remove_private_as_ingress") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].remove_private_as_ingress.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;replace_as</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].remove_private_as_ingress.replace_as") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_unchanged</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].next_hop_unchanged") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;update_source</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].update_source") | String |  |  |  | IP address or interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_reflector_client</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].route_reflector_client") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].bfd") | Boolean |  |  |  | Enable BFD. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd_timers</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].bfd_timers") | Dictionary |  |  |  | Override default BFD timers. BFD must be enabled with `bfd: true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].bfd_timers.interval") | Integer | Required |  | Min: 50<br>Max: 60000 | Interval in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].bfd_timers.min_rx") | Integer | Required |  | Min: 50<br>Max: 60000 | Rate in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].bfd_timers.multiplier") | Integer | Required |  | Min: 3<br>Max: 50 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ebgp_multihop</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].ebgp_multihop") | Integer |  |  | Min: 1<br>Max: 255 | Time-to-live in range of hops. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;next_hop_self</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].next_hop_self") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].password") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;passive</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].passive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_originate</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].default_originate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].default_originate.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].default_originate.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].default_originate.route_map") | String |  |  |  | Route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;send_community</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].send_community") | String |  |  |  | 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].maximum_routes") | Integer |  |  | Min: 0<br>Max: 4294967294 | Maximum number of routes (0 means unlimited). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_limit</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].maximum_routes_warning_limit") | String |  |  |  | Maximum number of routes after which a warning is issued (0 means never warn) or<br>Percentage of maximum number of routes at which to warn ("<1-100> percent").<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes_warning_only</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].maximum_routes_warning_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;missing_policy</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].missing_policy") | Dictionary |  |  |  | Missing policy configuration for all address-families. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].missing_policy.direction_in") | Dictionary |  |  |  | Missing policy inbound direction. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].missing_policy.direction_in.action") | String | Required |  | Valid Values:<br>- <code>deny</code><br>- <code>permit</code><br>- <code>deny-in-out</code> | Missing policy action. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_community_list</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].missing_policy.direction_in.include_community_list") | Boolean |  |  |  | Include community-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_prefix_list</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].missing_policy.direction_in.include_prefix_list") | Boolean |  |  |  | Include prefix-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_sub_route_map</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].missing_policy.direction_in.include_sub_route_map") | Boolean |  |  |  | Include sub-route-map references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].missing_policy.direction_out") | Dictionary |  |  |  | Missing policy outbound direction. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].missing_policy.direction_out.action") | String | Required |  | Valid Values:<br>- <code>deny</code><br>- <code>permit</code><br>- <code>deny-in-out</code> | Missing policy action. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_community_list</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].missing_policy.direction_out.include_community_list") | Boolean |  |  |  | Include community-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_prefix_list</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].missing_policy.direction_out.include_prefix_list") | Boolean |  |  |  | Include prefix-list references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_sub_route_map</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].missing_policy.direction_out.include_sub_route_map") | Boolean |  |  |  | Include sub-route-map references in missing policy decision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_bandwidth</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].link_bandwidth") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].link_bandwidth.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].link_bandwidth.default") | String |  |  |  | nn.nn(K|M|G) link speed in bits/second. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allowas_in</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].allowas_in") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].allowas_in.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;times</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].allowas_in.times") | Integer |  |  | Min: 1<br>Max: 10 | Number of local ASNs allowed in a BGP update. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].weight") | Integer |  |  | Min: 0<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].timers") | String |  |  |  | BGP Keepalive and Hold Timer values in seconds as string "<0-3600> <0-3600>". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rib_in_pre_policy_retain</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].rib_in_pre_policy_retain") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].rib_in_pre_policy_retain.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].rib_in_pre_policy_retain.all") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_in</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].route_map_in") | String |  |  |  | Inbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_out</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].route_map_out") | String |  |  |  | Outbound route-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session_tracker</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].session_tracker") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shared_secret</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].shared_secret") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].shared_secret.profile") | String | Required |  |  | Name of profile defined under `management_security`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].shared_secret.hash_algorithm") | String | Required |  | Valid Values:<br>- <code>aes-128-cmac-96</code><br>- <code>hmac-sha-256</code><br>- <code>hmac-sha1-96</code> | Note: Algorithm hmac-sha-256 requires EOS version 4.31.1F and above. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl_maximum_hops</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].ttl_maximum_hops") | Integer |  |  | Min: 0<br>Max: 254 | Maximum number of hops. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_filter</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].peer_filter") <span style="color:red">removed</span> | String |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>router_bgp.listen_ranges[].peer_filter</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_listen_range_prefix</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp_peer_groups.[].bgp_listen_range_prefix") <span style="color:red">removed</span> | String |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>router_bgp.listen_ranges[].bgp_listen_range_prefix</samp> instead.</span> |

=== "YAML"

    ```yaml
    <network_services_keys.name>:

        # Specify a tenant name.
        # Tenant provide a construct to group L3 VRFs and L2 VLANs.
        # Networks services can be filtered by tenant name.
      - name: <str; required; unique>

        # List of BGP peer groups definitions.
        # This will configure BGP peer groups to be used inside the tenant VRF for peering with external devices.
        # Since BGP peer groups are configured at higher BGP level, shared between VRFs,
        # peer_group names should not overlap between VRFs.
        bgp_peer_groups:

            # BGP peer group name.
          - name: <str; required; unique>

            # Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network.
            # If not set the peer-group is created on devices which have a bgp_peer mapped to the corresponding peer_group.
            nodes:
              - <str>
            address_family_ipv4:
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
              next_hop:
                address_family_ipv6:
                  enabled: <bool; required>
                  originate: <bool>

              # Inbound prefix-list name.
              prefix_list_in: <str>

              # Outbound prefix-list name.
              prefix_list_out: <str>
            address_family_ipv6:
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

        # VRFs will only be configured on a node if any of the underlying objects like `svis` or `l3_interfaces` apply to the node.
        #
        # It is recommended to only define a VRF in one Tenant. If the same VRF name is used across multiple tenants and those tenants
        # are accepted by `filter.tenants` on the node, any object set under the duplicate VRFs must either be unique or be an exact match.
        #
        # VRF "default" is partially supported under network-services. Currently the supported options for "default" vrf are route-target,
        # route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.
        # Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.
        vrfs:
          - name: <str; required; unique>

            # List of BGP peer definitions.
            # This will configure BGP neighbors inside the tenant VRF for peering with external devices.
            # The configured peer will automatically be activated for ipv4 or ipv6 address family based on the ip address.
            # Note, only ipv4 and ipv6 address families are currently supported in eos_designs.
            # For other address families, use custom_structured configuration with eos_cli_config_gen.
            bgp_peers:

                # IPv4_address or IPv6_address.
              - ip_address: <str; required>

                # Peer group name.
                peer_group: <str>

                # BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
                remote_as: <str>
                description: <str>

                # Encrypted password.
                password: <str>

                # 'all' or a combination of 'standard', 'extended', 'large' and 'link-bandwidth (w/options)'.
                send_community: <str>
                next_hop_self: <bool>

                # BGP Keepalive and Hold Timer values in seconds as string <0-3600> <0-3600>.
                timers: <str>

                # Maximum number of routes (0 means unlimited).
                maximum_routes: <int; 0-4294967294>
                maximum_routes_warning_only: <bool>
                default_originate:
                  always: <bool>
                update_source: <str>

                # Time-to-live in range of hops.
                ebgp_multihop: <int; 1-255>

                # Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network.
                nodes:
                  - <str>

                # IPv4_address
                # Next hop settings can be either ipv4 or ipv6 for one neighbor, this will be applied by a uniquely generated route-map per neighbor.
                # Next hop takes precedence over route_map_out.
                set_ipv4_next_hop: <str>

                # IPv6_address
                # Next hop settings can be either ipv4 or ipv6 for one neighbor, this will be applied by a uniquely generated route-map per neighbor.
                # Next hop takes precedence over route_map_out.
                set_ipv6_next_hop: <str>

                # Route-map name.
                route_map_out: <str>

                # Route-map name.
                route_map_in: <str>

                # Inbound prefix list name.
                # The prefix-list will be associated under the IPv4 or IPv6 address family based on the IP address.
                prefix_list_in: <str>

                # Outbound prefix list name.
                # The prefix-list will be associated under the IPv4 or IPv6 address family based on the IP address.
                prefix_list_out: <str>

                # Local BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
                local_as: <str>
                weight: <int; 0-65535>
                bfd: <bool>
                shutdown: <bool>

            # List of BGP peer groups definitions.
            # This will configure BGP peer groups to be used inside the tenant VRF for peering with external devices.
            # Since BGP peer groups are configured at higher BGP level, shared between VRFs,
            # peer_group names should not overlap between VRFs.
            bgp_peer_groups:

                # BGP peer group name.
              - name: <str>

                # Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network.
                # If not set the peer-group is created on devices which have a bgp_peer mapped to the corresponding peer_group.
                nodes:
                  - <str>
                address_family_ipv4:
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
                  next_hop:
                    address_family_ipv6:
                      enabled: <bool; required>
                      originate: <bool>

                  # Inbound prefix-list name.
                  prefix_list_in: <str>

                  # Outbound prefix-list name.
                  prefix_list_out: <str>
                address_family_ipv6:
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
    ```
