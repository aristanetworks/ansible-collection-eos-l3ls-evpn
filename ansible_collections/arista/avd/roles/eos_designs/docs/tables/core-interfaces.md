<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>core_interfaces</samp>](## "core_interfaces") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;p2p_links_ip_pools</samp>](## "core_interfaces.p2p_links_ip_pools") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "core_interfaces.p2p_links_ip_pools.[].name") | String | Required, Unique |  |  | P2P pool name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_pool</samp>](## "core_interfaces.p2p_links_ip_pools.[].ipv4_pool") | String |  |  |  | IPv4 address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_size</samp>](## "core_interfaces.p2p_links_ip_pools.[].prefix_size") | Integer |  | `31` | Min: 8<br>Max: 31 | Subnet mask size. |
    | [<samp>&nbsp;&nbsp;p2p_links_profiles</samp>](## "core_interfaces.p2p_links_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "core_interfaces.p2p_links_profiles.[].name") | String | Required, Unique |  |  | P2P profile name. Any variable supported under `p2p_links` can be inherited from a profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "core_interfaces.p2p_links_profiles.[].id") | Integer |  |  |  | Unique id per subnet_summary. Used to calculate ip addresses.<br>Required with ip_pool. ID starting from 1.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "core_interfaces.p2p_links_profiles.[].speed") | String |  |  |  | Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_pool</samp>](## "core_interfaces.p2p_links_profiles.[].ip_pool") | String |  |  |  | P2P pool name. IP Pool defined under p2p_links_ip_pools. A /31 will be taken from the pool per P2P link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subnet</samp>](## "core_interfaces.p2p_links_profiles.[].subnet") | String |  |  |  | IPv4 address/Mask. Subnet used on this P2P link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "core_interfaces.p2p_links_profiles.[].ip") | List, items: String |  |  |  | Specific IP addresses used on this P2P link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "core_interfaces.p2p_links_profiles.[].ip.[]") | String |  |  |  | Node IPv4 address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "core_interfaces.p2p_links_profiles.[].ipv6_enable") | Boolean |  | `False` |  | Allows turning on ipv6 for the link or profile (also autodetected based on underlay_rfc5549 and include_in_underlay_protocol). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "core_interfaces.p2p_links_profiles.[].nodes") | List, items: String |  |  |  | Nodes where this link should be configured. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "core_interfaces.p2p_links_profiles.[].nodes.[]") | String |  |  |  | The values can be < node_a >, < node_b >.<br>ex.- [ core-1-isis-sr-ldp, core-2-ospf-ldp ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "core_interfaces.p2p_links_profiles.[].interfaces") | List, items: String |  |  |  | Interfaces where this link should be configured and Required unless using port-channels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "core_interfaces.p2p_links_profiles.[].interfaces.[]") | String |  |  |  | The value can be like < node_a_interface >, < node_b_interface >.<br>ex. - [ Ethernet2, Ethernet2 ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as</samp>](## "core_interfaces.p2p_links_profiles.[].as") | List, items: String |  |  |  | AS numbers for BGP.<br>Required with bgp peering.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "core_interfaces.p2p_links_profiles.[].as.[]") | String |  |  |  | The values can be like ["node_a_as", "node_b_as"]. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;descriptions</samp>](## "core_interfaces.p2p_links_profiles.[].descriptions") | List, items: String |  |  |  | Interface descriptions. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "core_interfaces.p2p_links_profiles.[].descriptions.[]") | String |  |  |  | Description or description template to be used on the ethernet interface.<br>This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.<br>The available template fields are:<br>  - `peer`: The name of the peer.<br>  - `interface`: The local interface name.<br>  - `peer_interface`: The interface on the peer.<br><br>The default description is set by `default_underlay_p2p_ethernet_description`.<br>By default the description is templated from the name and interface of the peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_in_underlay_protocol</samp>](## "core_interfaces.p2p_links_profiles.[].include_in_underlay_protocol") | Boolean |  | `True` |  | Add this interface to underlay routing protocol. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_hello_padding</samp>](## "core_interfaces.p2p_links_profiles.[].isis_hello_padding") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp>](## "core_interfaces.p2p_links_profiles.[].isis_metric") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_circuit_type</samp>](## "core_interfaces.p2p_links_profiles.[].isis_circuit_type") | String |  |  | Valid Values:<br>- <code>level-1</code><br>- <code>level-2</code><br>- <code>level-1-2</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_mode</samp>](## "core_interfaces.p2p_links_profiles.[].isis_authentication_mode") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>text</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_key</samp>](## "core_interfaces.p2p_links_profiles.[].isis_authentication_key") | String |  |  |  | Type-7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_network_type</samp>](## "core_interfaces.p2p_links_profiles.[].isis_network_type") | String |  | `point-to-point` | Valid Values:<br>- <code>point-to-point</code><br>- <code>broadcast</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ip</samp>](## "core_interfaces.p2p_links_profiles.[].mpls_ip") | Boolean |  |  |  | MPLS parameters. Default value is true if switch.mpls_lsr is true. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ldp</samp>](## "core_interfaces.p2p_links_profiles.[].mpls_ldp") | Boolean |  |  |  | MPLS parameters. Default value is true for ldp underlay variants, otherwise false. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "core_interfaces.p2p_links_profiles.[].mtu") | Integer |  |  |  | MTU for this P2P link. Default value same as p2p_uplinks_mtu. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "core_interfaces.p2p_links_profiles.[].bfd") | Boolean |  |  |  | Enable BFD (only considered for BGP). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "core_interfaces.p2p_links_profiles.[].ptp") | Dictionary |  |  |  | PTP parameters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "core_interfaces.p2p_links_profiles.[].ptp.enabled") | Boolean |  | `False` |  | Enable PTP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;roles</samp>](## "core_interfaces.p2p_links_profiles.[].ptp.roles") | List, items: String |  |  |  | Role in boundary clock mode for each node. Default is `dynamic`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "core_interfaces.p2p_links_profiles.[].ptp.roles.[]") | String |  | `dynamic` | Valid Values:<br>- <code>dynamic</code><br>- <code>master</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "core_interfaces.p2p_links_profiles.[].ptp.profile") | String |  | `aes67-r16-2016` |  | Default available profiles are:<br>  - "aes67"<br>  - "aes67-r16-2016"<br>  - "smpte2059-2" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sflow</samp>](## "core_interfaces.p2p_links_profiles.[].sflow") | Boolean |  |  |  | Enable sFlow. Overrides `fabric_sflow` setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_multicast</samp>](## "core_interfaces.p2p_links_profiles.[].underlay_multicast") | Boolean |  | `False` |  | Enable PIM sparse mode. Requires `include_in_underlay_protocol` and the global `underlay_multicast` to be `true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flow_tracking</samp>](## "core_interfaces.p2p_links_profiles.[].flow_tracking") | Dictionary |  |  |  | Enable flow-tracking. Overrides `fabric_flow_tracking` setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "core_interfaces.p2p_links_profiles.[].flow_tracking.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "core_interfaces.p2p_links_profiles.[].flow_tracking.name") | String |  |  |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "core_interfaces.p2p_links_profiles.[].qos_profile") | String |  |  |  | QOS service profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;macsec_profile</samp>](## "core_interfaces.p2p_links_profiles.[].macsec_profile") | String |  |  |  | MAC security profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_channel</samp>](## "core_interfaces.p2p_links_profiles.[].port_channel") | Dictionary |  |  |  | Port-channel parameters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "core_interfaces.p2p_links_profiles.[].port_channel.description") | String |  |  |  | Description or description template to be used on the port-channel interface.<br>This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.<br>The available template fields are:<br>  - `peer`: The name of the peer.<br>  - `interface`: The local port-channel interface name.<br>  - `peer_interface`: The port-channel interface on the peer.<br>  - `port_channel_id`: The local port-channel ID.<br>  - `peer_port_channel_id`: The ID of the port-channel on the peer.<br><br>Falls back to the description on the `p2p_link` if set. Otherwise default description is set by `default_underlay_p2p_port_channel_description`.<br>By default the description is templated from the name and port_channel interface of the peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "core_interfaces.p2p_links_profiles.[].port_channel.mode") | String |  | `active` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes_child_interfaces</samp>](## "core_interfaces.p2p_links_profiles.[].port_channel.nodes_child_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;node</samp>](## "core_interfaces.p2p_links_profiles.[].port_channel.nodes_child_interfaces.[].node") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "core_interfaces.p2p_links_profiles.[].port_channel.nodes_child_interfaces.[].interfaces") | List, items: String |  |  |  | List of node interfaces. Ex.- [ 'node1 interface1', 'node1 interface2' ]. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "core_interfaces.p2p_links_profiles.[].port_channel.nodes_child_interfaces.[].interfaces.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;channel_id</samp>](## "core_interfaces.p2p_links_profiles.[].port_channel.nodes_child_interfaces.[].channel_id") | Integer |  |  |  | Port-Channel ID. If no channel_id is specified, an id is generated from the first switch port in the port channel. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "core_interfaces.p2p_links_profiles.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the point-to-point interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;routing_protocol</samp>](## "core_interfaces.p2p_links_profiles.[].routing_protocol") | String |  |  | Valid Values:<br>- <code>ebgp</code> | Enables deviation of the routing protocol used on this link from the fabric underlay default.<br>- ebgp: Enforce plain IPv4 BGP peering |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "core_interfaces.p2p_links_profiles.[].structured_config") | Dictionary |  |  |  | Custom structured config for interfaces.<br>Note! The content of this dictionary is _not_ validated by the schema, since it can be either ethernet_interfaces or port_channel_interfaces. |
    | [<samp>&nbsp;&nbsp;p2p_links</samp>](## "core_interfaces.p2p_links") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;nodes</samp>](## "core_interfaces.p2p_links.[].nodes") | List, items: String | Required |  |  | Nodes where this link should be configured. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].nodes.[]") | String |  |  |  | The values can be < node_a >, < node_b >.<br>ex.- [ core-1-isis-sr-ldp, core-2-ospf-ldp ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "core_interfaces.p2p_links.[].profile") | String |  |  |  | P2P profile name. Profile defined under p2p_profiles. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "core_interfaces.p2p_links.[].id") | Integer |  |  |  | Unique id per subnet_summary. Used to calculate ip addresses.<br>Required with ip_pool. ID starting from 1.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "core_interfaces.p2p_links.[].speed") | String |  |  |  | Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_pool</samp>](## "core_interfaces.p2p_links.[].ip_pool") | String |  |  |  | P2P pool name. IP Pool defined under p2p_links_ip_pools. A /31 will be taken from the pool per P2P link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subnet</samp>](## "core_interfaces.p2p_links.[].subnet") | String |  |  |  | IPv4 address/Mask. Subnet used on this P2P link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "core_interfaces.p2p_links.[].ip") | List, items: String |  |  |  | Specific IP addresses used on this P2P link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].ip.[]") | String |  |  |  | Node IPv4 address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "core_interfaces.p2p_links.[].ipv6_enable") | Boolean |  | `False` |  | Allows turning on ipv6 for the link or profile (also autodetected based on underlay_rfc5549 and include_in_underlay_protocol). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "core_interfaces.p2p_links.[].interfaces") | List, items: String |  |  |  | Interfaces where this link should be configured and Required unless using port-channels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].interfaces.[]") | String |  |  |  | The value can be like < node_a_interface >, < node_b_interface >.<br>ex. - [ Ethernet2, Ethernet2 ].<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;as</samp>](## "core_interfaces.p2p_links.[].as") | List, items: String |  |  |  | AS numbers for BGP.<br>Required with bgp peering.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].as.[]") | String |  |  |  | The values can be like ["node_a_as", "node_b_as"]. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;descriptions</samp>](## "core_interfaces.p2p_links.[].descriptions") | List, items: String |  |  |  | Interface descriptions. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].descriptions.[]") | String |  |  |  | Description or description template to be used on the ethernet interface.<br>This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.<br>The available template fields are:<br>  - `peer`: The name of the peer.<br>  - `interface`: The local interface name.<br>  - `peer_interface`: The interface on the peer.<br><br>The default description is set by `default_underlay_p2p_ethernet_description`.<br>By default the description is templated from the name and interface of the peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include_in_underlay_protocol</samp>](## "core_interfaces.p2p_links.[].include_in_underlay_protocol") | Boolean |  | `True` |  | Add this interface to underlay routing protocol. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_hello_padding</samp>](## "core_interfaces.p2p_links.[].isis_hello_padding") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp>](## "core_interfaces.p2p_links.[].isis_metric") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_circuit_type</samp>](## "core_interfaces.p2p_links.[].isis_circuit_type") | String |  |  | Valid Values:<br>- <code>level-1</code><br>- <code>level-2</code><br>- <code>level-1-2</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_mode</samp>](## "core_interfaces.p2p_links.[].isis_authentication_mode") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>text</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_key</samp>](## "core_interfaces.p2p_links.[].isis_authentication_key") | String |  |  |  | Type-7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;isis_network_type</samp>](## "core_interfaces.p2p_links.[].isis_network_type") | String |  | `point-to-point` | Valid Values:<br>- <code>point-to-point</code><br>- <code>broadcast</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ip</samp>](## "core_interfaces.p2p_links.[].mpls_ip") | Boolean |  |  |  | MPLS parameters. Default value is true if switch.mpls_lsr is true. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_ldp</samp>](## "core_interfaces.p2p_links.[].mpls_ldp") | Boolean |  |  |  | MPLS parameters. Default value is true for ldp underlay variants, otherwise false. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "core_interfaces.p2p_links.[].mtu") | Integer |  |  |  | MTU for this P2P link. Default value same as p2p_uplinks_mtu. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "core_interfaces.p2p_links.[].bfd") | Boolean |  |  |  | Enable BFD (only considered for BGP). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "core_interfaces.p2p_links.[].ptp") | Dictionary |  |  |  | PTP parameters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "core_interfaces.p2p_links.[].ptp.enabled") | Boolean |  | `False` |  | Enable PTP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;roles</samp>](## "core_interfaces.p2p_links.[].ptp.roles") | List, items: String |  |  |  | Role in boundary clock mode for each node. Default is `dynamic`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].ptp.roles.[]") | String |  | `dynamic` | Valid Values:<br>- <code>dynamic</code><br>- <code>master</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "core_interfaces.p2p_links.[].ptp.profile") | String |  | `aes67-r16-2016` |  | Default available profiles are:<br>  - "aes67"<br>  - "aes67-r16-2016"<br>  - "smpte2059-2" |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sflow</samp>](## "core_interfaces.p2p_links.[].sflow") | Boolean |  |  |  | Enable sFlow. Overrides `fabric_sflow` setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_multicast</samp>](## "core_interfaces.p2p_links.[].underlay_multicast") | Boolean |  | `False` |  | Enable PIM sparse mode. Requires `include_in_underlay_protocol` and the global `underlay_multicast` to be `true`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flow_tracking</samp>](## "core_interfaces.p2p_links.[].flow_tracking") | Dictionary |  |  |  | Enable flow-tracking. Overrides `fabric_flow_tracking` setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "core_interfaces.p2p_links.[].flow_tracking.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "core_interfaces.p2p_links.[].flow_tracking.name") | String |  |  |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "core_interfaces.p2p_links.[].qos_profile") | String |  |  |  | QOS service profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;macsec_profile</samp>](## "core_interfaces.p2p_links.[].macsec_profile") | String |  |  |  | MAC security profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_channel</samp>](## "core_interfaces.p2p_links.[].port_channel") | Dictionary |  |  |  | Port-channel parameters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "core_interfaces.p2p_links.[].port_channel.description") | String |  |  |  | Description or description template to be used on the port-channel interface.<br>This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.<br>The available template fields are:<br>  - `peer`: The name of the peer.<br>  - `interface`: The local port-channel interface name.<br>  - `peer_interface`: The port-channel interface on the peer.<br>  - `port_channel_id`: The local port-channel ID.<br>  - `peer_port_channel_id`: The ID of the port-channel on the peer.<br><br>Falls back to the description on the `p2p_link` if set. Otherwise default description is set by `default_underlay_p2p_port_channel_description`.<br>By default the description is templated from the name and port_channel interface of the peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "core_interfaces.p2p_links.[].port_channel.mode") | String |  | `active` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes_child_interfaces</samp>](## "core_interfaces.p2p_links.[].port_channel.nodes_child_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;node</samp>](## "core_interfaces.p2p_links.[].port_channel.nodes_child_interfaces.[].node") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "core_interfaces.p2p_links.[].port_channel.nodes_child_interfaces.[].interfaces") | List, items: String |  |  |  | List of node interfaces. Ex.- [ 'node1 interface1', 'node1 interface2' ]. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "core_interfaces.p2p_links.[].port_channel.nodes_child_interfaces.[].interfaces.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;channel_id</samp>](## "core_interfaces.p2p_links.[].port_channel.nodes_child_interfaces.[].channel_id") | Integer |  |  |  | Port-Channel ID. If no channel_id is specified, an id is generated from the first switch port in the port channel. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "core_interfaces.p2p_links.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the point-to-point interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;routing_protocol</samp>](## "core_interfaces.p2p_links.[].routing_protocol") | String |  |  | Valid Values:<br>- <code>ebgp</code> | Enables deviation of the routing protocol used on this link from the fabric underlay default.<br>- ebgp: Enforce plain IPv4 BGP peering |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "core_interfaces.p2p_links.[].structured_config") | Dictionary |  |  |  | Custom structured config for interfaces.<br>Note! The content of this dictionary is _not_ validated by the schema, since it can be either ethernet_interfaces or port_channel_interfaces. |

=== "YAML"

    ```yaml
    core_interfaces:
      p2p_links_ip_pools:

          # P2P pool name.
        - name: <str; required; unique>

          # IPv4 address/Mask.
          ipv4_pool: <str>

          # Subnet mask size.
          prefix_size: <int; 8-31; default=31>
      p2p_links_profiles:

          # P2P profile name. Any variable supported under `p2p_links` can be inherited from a profile.
        - name: <str; required; unique>

          # Unique id per subnet_summary. Used to calculate ip addresses.
          # Required with ip_pool. ID starting from 1.
          id: <int>

          # Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
          speed: <str>

          # P2P pool name. IP Pool defined under p2p_links_ip_pools. A /31 will be taken from the pool per P2P link.
          ip_pool: <str>

          # IPv4 address/Mask. Subnet used on this P2P link.
          subnet: <str>

          # Specific IP addresses used on this P2P link.
          ip:

              # Node IPv4 address/Mask.
            - <str>

          # Allows turning on ipv6 for the link or profile (also autodetected based on underlay_rfc5549 and include_in_underlay_protocol).
          ipv6_enable: <bool; default=False>

          # Nodes where this link should be configured.
          nodes:

              # The values can be < node_a >, < node_b >.
              # ex.- [ core-1-isis-sr-ldp, core-2-ospf-ldp ].
            - <str>

          # Interfaces where this link should be configured and Required unless using port-channels.
          interfaces:

              # The value can be like < node_a_interface >, < node_b_interface >.
              # ex. - [ Ethernet2, Ethernet2 ].
            - <str>

          # AS numbers for BGP.
          # Required with bgp peering.
          as:

              # The values can be like ["node_a_as", "node_b_as"].
            - <str>

          # Interface descriptions.
          descriptions:

              # Description or description template to be used on the ethernet interface.
              # This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
              # The available template fields are:
              #   - `peer`: The name of the peer.
              #   - `interface`: The local interface name.
              #   - `peer_interface`: The interface on the peer.
              #
              # The default description is set by `default_underlay_p2p_ethernet_description`.
              # By default the description is templated from the name and interface of the peer.
            - <str>

          # Add this interface to underlay routing protocol.
          include_in_underlay_protocol: <bool; default=True>
          isis_hello_padding: <bool; default=True>
          isis_metric: <int>
          isis_circuit_type: <str; "level-1" | "level-2" | "level-1-2">
          isis_authentication_mode: <str; "md5" | "text">

          # Type-7 encrypted password.
          isis_authentication_key: <str>
          isis_network_type: <str; "point-to-point" | "broadcast"; default="point-to-point">

          # MPLS parameters. Default value is true if switch.mpls_lsr is true.
          mpls_ip: <bool>

          # MPLS parameters. Default value is true for ldp underlay variants, otherwise false.
          mpls_ldp: <bool>

          # MTU for this P2P link. Default value same as p2p_uplinks_mtu.
          mtu: <int>

          # Enable BFD (only considered for BGP).
          bfd: <bool>

          # PTP parameters.
          ptp:

            # Enable PTP.
            enabled: <bool; default=False>

            # Role in boundary clock mode for each node. Default is `dynamic`.
            roles:
              - <str; "dynamic" | "master"; default="dynamic">

            # Default available profiles are:
            #   - "aes67"
            #   - "aes67-r16-2016"
            #   - "smpte2059-2"
            profile: <str; default="aes67-r16-2016">

          # Enable sFlow. Overrides `fabric_sflow` setting.
          sflow: <bool>

          # Enable PIM sparse mode. Requires `include_in_underlay_protocol` and the global `underlay_multicast` to be `true`.
          underlay_multicast: <bool; default=False>

          # Enable flow-tracking. Overrides `fabric_flow_tracking` setting.
          flow_tracking:
            enabled: <bool>

            # Flow tracker name as defined in flow_tracking_settings.
            name: <str>

          # QOS service profile.
          qos_profile: <str>

          # MAC security profile.
          macsec_profile: <str>

          # Port-channel parameters.
          port_channel:

            # Description or description template to be used on the port-channel interface.
            # This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
            # The available template fields are:
            #   - `peer`: The name of the peer.
            #   - `interface`: The local port-channel interface name.
            #   - `peer_interface`: The port-channel interface on the peer.
            #   - `port_channel_id`: The local port-channel ID.
            #   - `peer_port_channel_id`: The ID of the port-channel on the peer.
            #
            # Falls back to the description on the `p2p_link` if set. Otherwise default description is set by `default_underlay_p2p_port_channel_description`.
            # By default the description is templated from the name and port_channel interface of the peer.
            description: <str>
            mode: <str; default="active">
            nodes_child_interfaces:
              - node: <str; required; unique>

                # List of node interfaces. Ex.- [ 'node1 interface1', 'node1 interface2' ].
                interfaces:
                  - <str>

                # Port-Channel ID. If no channel_id is specified, an id is generated from the first switch port in the port channel.
                channel_id: <int>

          # EOS CLI rendered directly on the point-to-point interface in the final EOS configuration.
          raw_eos_cli: <str>

          # Enables deviation of the routing protocol used on this link from the fabric underlay default.
          # - ebgp: Enforce plain IPv4 BGP peering
          routing_protocol: <str; "ebgp">

          # Custom structured config for interfaces.
          # Note! The content of this dictionary is _not_ validated by the schema, since it can be either ethernet_interfaces or port_channel_interfaces.
          structured_config: <dict>
      p2p_links:

          # Nodes where this link should be configured.
        - nodes: # required

              # The values can be < node_a >, < node_b >.
              # ex.- [ core-1-isis-sr-ldp, core-2-ospf-ldp ].
            - <str>

          # P2P profile name. Profile defined under p2p_profiles.
          profile: <str>

          # Unique id per subnet_summary. Used to calculate ip addresses.
          # Required with ip_pool. ID starting from 1.
          id: <int>

          # Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
          speed: <str>

          # P2P pool name. IP Pool defined under p2p_links_ip_pools. A /31 will be taken from the pool per P2P link.
          ip_pool: <str>

          # IPv4 address/Mask. Subnet used on this P2P link.
          subnet: <str>

          # Specific IP addresses used on this P2P link.
          ip:

              # Node IPv4 address/Mask.
            - <str>

          # Allows turning on ipv6 for the link or profile (also autodetected based on underlay_rfc5549 and include_in_underlay_protocol).
          ipv6_enable: <bool; default=False>

          # Interfaces where this link should be configured and Required unless using port-channels.
          interfaces:

              # The value can be like < node_a_interface >, < node_b_interface >.
              # ex. - [ Ethernet2, Ethernet2 ].
            - <str>

          # AS numbers for BGP.
          # Required with bgp peering.
          as:

              # The values can be like ["node_a_as", "node_b_as"].
            - <str>

          # Interface descriptions.
          descriptions:

              # Description or description template to be used on the ethernet interface.
              # This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
              # The available template fields are:
              #   - `peer`: The name of the peer.
              #   - `interface`: The local interface name.
              #   - `peer_interface`: The interface on the peer.
              #
              # The default description is set by `default_underlay_p2p_ethernet_description`.
              # By default the description is templated from the name and interface of the peer.
            - <str>

          # Add this interface to underlay routing protocol.
          include_in_underlay_protocol: <bool; default=True>
          isis_hello_padding: <bool; default=True>
          isis_metric: <int>
          isis_circuit_type: <str; "level-1" | "level-2" | "level-1-2">
          isis_authentication_mode: <str; "md5" | "text">

          # Type-7 encrypted password.
          isis_authentication_key: <str>
          isis_network_type: <str; "point-to-point" | "broadcast"; default="point-to-point">

          # MPLS parameters. Default value is true if switch.mpls_lsr is true.
          mpls_ip: <bool>

          # MPLS parameters. Default value is true for ldp underlay variants, otherwise false.
          mpls_ldp: <bool>

          # MTU for this P2P link. Default value same as p2p_uplinks_mtu.
          mtu: <int>

          # Enable BFD (only considered for BGP).
          bfd: <bool>

          # PTP parameters.
          ptp:

            # Enable PTP.
            enabled: <bool; default=False>

            # Role in boundary clock mode for each node. Default is `dynamic`.
            roles:
              - <str; "dynamic" | "master"; default="dynamic">

            # Default available profiles are:
            #   - "aes67"
            #   - "aes67-r16-2016"
            #   - "smpte2059-2"
            profile: <str; default="aes67-r16-2016">

          # Enable sFlow. Overrides `fabric_sflow` setting.
          sflow: <bool>

          # Enable PIM sparse mode. Requires `include_in_underlay_protocol` and the global `underlay_multicast` to be `true`.
          underlay_multicast: <bool; default=False>

          # Enable flow-tracking. Overrides `fabric_flow_tracking` setting.
          flow_tracking:
            enabled: <bool>

            # Flow tracker name as defined in flow_tracking_settings.
            name: <str>

          # QOS service profile.
          qos_profile: <str>

          # MAC security profile.
          macsec_profile: <str>

          # Port-channel parameters.
          port_channel:

            # Description or description template to be used on the port-channel interface.
            # This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
            # The available template fields are:
            #   - `peer`: The name of the peer.
            #   - `interface`: The local port-channel interface name.
            #   - `peer_interface`: The port-channel interface on the peer.
            #   - `port_channel_id`: The local port-channel ID.
            #   - `peer_port_channel_id`: The ID of the port-channel on the peer.
            #
            # Falls back to the description on the `p2p_link` if set. Otherwise default description is set by `default_underlay_p2p_port_channel_description`.
            # By default the description is templated from the name and port_channel interface of the peer.
            description: <str>
            mode: <str; default="active">
            nodes_child_interfaces:
              - node: <str; required; unique>

                # List of node interfaces. Ex.- [ 'node1 interface1', 'node1 interface2' ].
                interfaces:
                  - <str>

                # Port-Channel ID. If no channel_id is specified, an id is generated from the first switch port in the port channel.
                channel_id: <int>

          # EOS CLI rendered directly on the point-to-point interface in the final EOS configuration.
          raw_eos_cli: <str>

          # Enables deviation of the routing protocol used on this link from the fabric underlay default.
          # - ebgp: Enforce plain IPv4 BGP peering
          routing_protocol: <str; "ebgp">

          # Custom structured config for interfaces.
          # Note! The content of this dictionary is _not_ validated by the schema, since it can be either ethernet_interfaces or port_channel_interfaces.
          structured_config: <dict>
    ```
