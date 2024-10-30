<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ethernet_interfaces</samp>](## "ethernet_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "ethernet_interfaces.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "ethernet_interfaces.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "ethernet_interfaces.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;load_interval</samp>](## "ethernet_interfaces.[].load_interval") | Integer |  |  | Min: 0<br>Max: 600 | Interval in seconds for updating interface counters. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "ethernet_interfaces.[].speed") | String |  |  |  | Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "ethernet_interfaces.[].mtu") | Integer |  |  | Min: 68<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2_mtu</samp>](## "ethernet_interfaces.[].l2_mtu") | Integer |  |  | Min: 68<br>Max: 65535 | "l2_mtu" should only be defined for platforms supporting the "l2 mtu" CLI.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2_mru</samp>](## "ethernet_interfaces.[].l2_mru") | Integer |  |  | Min: 68<br>Max: 65535 | "l2_mru" should only be defined for platforms supporting the "l2 mru" CLI.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlans</samp>](## "ethernet_interfaces.[].vlans") <span style="color:red">deprecated</span> | String |  |  |  | List of switchport vlans as string.<br>For a trunk port this would be a range like "1-200,300".<br>For an access port this would be a single vlan "123".<br><span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>switchport.access_vlan or switchport.trunk.allowed_vlan</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;native_vlan</samp>](## "ethernet_interfaces.[].native_vlan") <span style="color:red">deprecated</span> | Integer |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>switchport.trunk.native_vlan</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;native_vlan_tag</samp>](## "ethernet_interfaces.[].native_vlan_tag") <span style="color:red">deprecated</span> | Boolean |  |  |  | If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>switchport.trunk.native_vlan_tag</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "ethernet_interfaces.[].mode") <span style="color:red">deprecated</span> | String |  |  | Valid Values:<br>- <code>access</code><br>- <code>dot1q-tunnel</code><br>- <code>trunk</code><br>- <code>trunk phone</code> | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>switchport.mode</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;phone</samp>](## "ethernet_interfaces.[].phone") <span style="color:red">deprecated</span> | Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>switchport.phone</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk</samp>](## "ethernet_interfaces.[].phone.trunk") | String |  |  | Valid Values:<br>- <code>tagged</code><br>- <code>tagged phone</code><br>- <code>untagged</code><br>- <code>untagged phone</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "ethernet_interfaces.[].phone.vlan") | Integer |  |  | Min: 1<br>Max: 4094 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2_protocol</samp>](## "ethernet_interfaces.[].l2_protocol") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "ethernet_interfaces.[].l2_protocol.encapsulation_dot1q_vlan") | Integer |  |  |  | Vlan tag to configure on sub-interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forwarding_profile</samp>](## "ethernet_interfaces.[].l2_protocol.forwarding_profile") | String |  |  |  | L2 protocol forwarding profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "ethernet_interfaces.[].trunk_groups") <span style="color:red">deprecated</span> | List, items: String |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>switchport.trunk.groups</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "ethernet_interfaces.[].trunk_groups.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "ethernet_interfaces.[].type") <span style="color:red">deprecated</span> | String |  |  | Valid Values:<br>- <code>routed</code><br>- <code>switched</code><br>- <code>l3dot1q</code><br>- <code>l2dot1q</code><br>- <code>port-channel-member</code> | l3dot1q and l2dot1q are used for sub-interfaces. The parent interface should be defined as routed.<br>The `type = switched/routed` should not be combined with `switchport`.<br><span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. See [here](https://avd.arista.com/stable/docs/release-notes/5.x.x.html#removal-of-type-key-dependency-for-rendering-ethernetport-channel-interfaces-configuration-and-documentation) for details.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;snmp_trap_link_change</samp>](## "ethernet_interfaces.[].snmp_trap_link_change") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;address_locking</samp>](## "ethernet_interfaces.[].address_locking") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "ethernet_interfaces.[].address_locking.ipv4") | Boolean |  |  |  | Enable address locking for IPv4. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "ethernet_interfaces.[].address_locking.ipv6") | Boolean |  |  |  | Enable address locking for IPv6. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;flowcontrol</samp>](## "ethernet_interfaces.[].flowcontrol") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;received</samp>](## "ethernet_interfaces.[].flowcontrol.received") | String |  |  | Valid Values:<br>- <code>desired</code><br>- <code>on</code><br>- <code>off</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ethernet_interfaces.[].vrf") | String |  |  |  | VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;flow_tracker</samp>](## "ethernet_interfaces.[].flow_tracker") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sampled</samp>](## "ethernet_interfaces.[].flow_tracker.sampled") | String |  |  |  | Sampled flow tracker name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware</samp>](## "ethernet_interfaces.[].flow_tracker.hardware") | String |  |  |  | Hardware flow tracker name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;error_correction_encoding</samp>](## "ethernet_interfaces.[].error_correction_encoding") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ethernet_interfaces.[].error_correction_encoding.enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fire_code</samp>](## "ethernet_interfaces.[].error_correction_encoding.fire_code") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reed_solomon</samp>](## "ethernet_interfaces.[].error_correction_encoding.reed_solomon") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;link_tracking_groups</samp>](## "ethernet_interfaces.[].link_tracking_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "ethernet_interfaces.[].link_tracking_groups.[].name") | String | Required, Unique |  |  | Group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "ethernet_interfaces.[].link_tracking_groups.[].direction") | String |  |  | Valid Values:<br>- <code>upstream</code><br>- <code>downstream</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_ethernet_segment</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.identifier") | String |  |  |  | EVPN Ethernet Segment Identifier (Type 1 format). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redundancy</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.redundancy") | String |  |  | Valid Values:<br>- <code>all-active</code><br>- <code>single-active</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;designated_forwarder_election</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.designated_forwarder_election") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.algorithm") | String |  |  | Valid Values:<br>- <code>modulus</code><br>- <code>preference</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preference_value</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.preference_value") | Integer |  |  | Min: 0<br>Max: 65535 | Preference_value is only used when "algorithm" is "preference". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dont_preempt</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.dont_preempt") | Boolean |  |  |  | Dont_preempt is only used when "algorithm" is "preference". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hold_time</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.hold_time") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subsequent_hold_time</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.subsequent_hold_time") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;candidate_reachability_required</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.candidate_reachability_required") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.mpls") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shared_index</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.mpls.shared_index") | Integer |  |  | Min: 1<br>Max: 1024 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tunnel_flood_filter_time</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.mpls.tunnel_flood_filter_time") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "ethernet_interfaces.[].evpn_ethernet_segment.route_target") | String |  |  |  | EVPN Route Target for ESI with format xx:xx:xx:xx:xx:xx. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "ethernet_interfaces.[].encapsulation_dot1q_vlan") <span style="color:red">deprecated</span> | Integer |  |  |  | VLAN tag to configure on sub-interface.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>encapsulation_dot1q.vlan</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q</samp>](## "ethernet_interfaces.[].encapsulation_dot1q") | Dictionary |  |  |  | Warning: `encapsulation_dot1q` should not be combined with `ethernet_interfaces[].type: l3dot1q` or `ethernet_interfaces[].type: l2dot1q`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "ethernet_interfaces.[].encapsulation_dot1q.vlan") | Integer | Required |  | Min: 1<br>Max: 4094 | VLAD ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner_vlan</samp>](## "ethernet_interfaces.[].encapsulation_dot1q.inner_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Inner VLAN ID. This setting can only be applied to sub-interfaces on EOS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_vlan</samp>](## "ethernet_interfaces.[].encapsulation_vlan") | Dictionary |  |  |  | This setting can only be applied to sub-interfaces on EOS.<br>Warning: `encapsulation_vlan` should not be combined with `ethernet_interfaces[].type: l3dot1q` or `ethernet_interfaces[].type: l2dot1q`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;client</samp>](## "ethernet_interfaces.[].encapsulation_vlan.client") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1q</samp>](## "ethernet_interfaces.[].encapsulation_vlan.client.dot1q") <span style="color:red">deprecated</span> | Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "ethernet_interfaces.[].encapsulation_vlan.client.dot1q.vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Client VLAN ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;outer</samp>](## "ethernet_interfaces.[].encapsulation_vlan.client.dot1q.outer") | Integer |  |  | Min: 1<br>Max: 4094 | Client Outer VLAN ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner</samp>](## "ethernet_interfaces.[].encapsulation_vlan.client.dot1q.inner") | Integer |  |  |  | Client Inner VLAN ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unmatched</samp>](## "ethernet_interfaces.[].encapsulation_vlan.client.unmatched") <span style="color:red">deprecated</span> | Boolean |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation</samp>](## "ethernet_interfaces.[].encapsulation_vlan.client.encapsulation") | String |  |  | Valid Values:<br>- <code>dot1q</code><br>- <code>dot1ad</code><br>- <code>unmatched</code><br>- <code>untagged</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "ethernet_interfaces.[].encapsulation_vlan.client.vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Client VLAN ID. Not applicable for `encapsulation: untagged` or `encapsulation: unmatched`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;outer_vlan</samp>](## "ethernet_interfaces.[].encapsulation_vlan.client.outer_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Client Outer VLAN ID. Not applicable for `encapsulation: untagged` or `encapsulation: unmatched`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner_vlan</samp>](## "ethernet_interfaces.[].encapsulation_vlan.client.inner_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Client Inner VLAN ID. Not applicable for `encapsulation: untagged` or `encapsulation: unmatched`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner_encapsulation</samp>](## "ethernet_interfaces.[].encapsulation_vlan.client.inner_encapsulation") | String |  |  | Valid Values:<br>- <code>dot1q</code><br>- <code>dot1ad</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;network</samp>](## "ethernet_interfaces.[].encapsulation_vlan.network") | Dictionary |  |  |  | Network encapsulations are all optional and skipped if using client unmatched. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1q</samp>](## "ethernet_interfaces.[].encapsulation_vlan.network.dot1q") <span style="color:red">deprecated</span> | Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "ethernet_interfaces.[].encapsulation_vlan.network.dot1q.vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Network VLAN ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;outer</samp>](## "ethernet_interfaces.[].encapsulation_vlan.network.dot1q.outer") | Integer |  |  | Min: 1<br>Max: 4094 | Network outer VLAN ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner</samp>](## "ethernet_interfaces.[].encapsulation_vlan.network.dot1q.inner") | Integer |  |  | Min: 1<br>Max: 4094 | Network inner VLAN ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;client</samp>](## "ethernet_interfaces.[].encapsulation_vlan.network.client") <span style="color:red">deprecated</span> | Boolean |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation</samp>](## "ethernet_interfaces.[].encapsulation_vlan.network.encapsulation") | String |  |  | Valid Values:<br>- <code>dot1q</code><br>- <code>dot1ad</code><br>- <code>client</code><br>- <code>client inner</code><br>- <code>untagged</code> | `untagged` (no encapsulation) is applicable for `untagged` client only.<br>`client` and `client inner` (retain client encapsulation) is not applicable for `untagged` client. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "ethernet_interfaces.[].encapsulation_vlan.network.vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Network VLAN ID. Not applicable for `encapsulation: untagged` or `encapsulation: client`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;outer_vlan</samp>](## "ethernet_interfaces.[].encapsulation_vlan.network.outer_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Network outer VLAN ID. Not applicable for `encapsulation: untagged` or `encapsulation: client`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner_vlan</samp>](## "ethernet_interfaces.[].encapsulation_vlan.network.inner_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Network inner VLAN ID.  Not applicable for `encapsulation: untagged` or `encapsulation: client`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner_encapsulation</samp>](## "ethernet_interfaces.[].encapsulation_vlan.network.inner_encapsulation") | String |  |  | Valid Values:<br>- <code>dot1q</code><br>- <code>dot1ad</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlan_id</samp>](## "ethernet_interfaces.[].vlan_id") | Integer |  |  | Min: 1<br>Max: 4094 | This setting can only be applied to sub-interfaces on EOS.<br>Warning: `vlan_id` should not be combined with `ethernet_interfaces[].type == l2dot1q`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "ethernet_interfaces.[].ip_address") | String |  |  |  | IPv4 address/mask or "dhcp". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address_secondaries</samp>](## "ethernet_interfaces.[].ip_address_secondaries") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "ethernet_interfaces.[].ip_address_secondaries.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_verify_unicast_source_reachable_via</samp>](## "ethernet_interfaces.[].ip_verify_unicast_source_reachable_via") | String |  |  | Valid Values:<br>- <code>any</code><br>- <code>rx</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dhcp_client_accept_default_route</samp>](## "ethernet_interfaces.[].dhcp_client_accept_default_route") | Boolean |  |  |  | Install default-route obtained via DHCP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dhcp_server_ipv4</samp>](## "ethernet_interfaces.[].dhcp_server_ipv4") | Boolean |  |  |  | Enable IPv4 DHCP server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dhcp_server_ipv6</samp>](## "ethernet_interfaces.[].dhcp_server_ipv6") | Boolean |  |  |  | Enable IPv6 DHCP server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "ethernet_interfaces.[].ip_helpers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_helper</samp>](## "ethernet_interfaces.[].ip_helpers.[].ip_helper") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "ethernet_interfaces.[].ip_helpers.[].source_interface") | String |  |  |  | Source interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ethernet_interfaces.[].ip_helpers.[].vrf") | String |  |  |  | VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_nat</samp>](## "ethernet_interfaces.[].ip_nat") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;service_profile</samp>](## "ethernet_interfaces.[].ip_nat.service_profile") | String |  |  |  | NAT interface profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "ethernet_interfaces.[].ip_nat.destination") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic</samp>](## "ethernet_interfaces.[].ip_nat.destination.dynamic") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;access_list</samp>](## "ethernet_interfaces.[].ip_nat.destination.dynamic.[].access_list") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "ethernet_interfaces.[].ip_nat.destination.dynamic.[].comment") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pool_name</samp>](## "ethernet_interfaces.[].ip_nat.destination.dynamic.[].pool_name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "ethernet_interfaces.[].ip_nat.destination.dynamic.[].priority") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "ethernet_interfaces.[].ip_nat.destination.static") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;access_list</samp>](## "ethernet_interfaces.[].ip_nat.destination.static.[].access_list") | String |  |  |  | 'access_list' and 'group' are mutual exclusive. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "ethernet_interfaces.[].ip_nat.destination.static.[].comment") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "ethernet_interfaces.[].ip_nat.destination.static.[].direction") | String |  |  | Valid Values:<br>- <code>egress</code><br>- <code>ingress</code> | Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.<br>EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "ethernet_interfaces.[].ip_nat.destination.static.[].group") | Integer |  |  | Min: 1<br>Max: 65535 | 'access_list' and 'group' are mutual exclusive. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;original_ip</samp>](## "ethernet_interfaces.[].ip_nat.destination.static.[].original_ip") | String |  |  |  | IPv4 address. The combination of `original_ip` and `original_port` must be unique. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;original_port</samp>](## "ethernet_interfaces.[].ip_nat.destination.static.[].original_port") | Integer |  |  | Min: 1<br>Max: 65535 | TCP/UDP port. The combination of `original_ip` and `original_port` must be unique. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "ethernet_interfaces.[].ip_nat.destination.static.[].priority") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "ethernet_interfaces.[].ip_nat.destination.static.[].protocol") | String |  |  | Valid Values:<br>- <code>udp</code><br>- <code>tcp</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;translated_ip</samp>](## "ethernet_interfaces.[].ip_nat.destination.static.[].translated_ip") | String | Required |  |  | IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;translated_port</samp>](## "ethernet_interfaces.[].ip_nat.destination.static.[].translated_port") | Integer |  |  | Min: 1<br>Max: 65535 | requires 'original_port'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "ethernet_interfaces.[].ip_nat.source") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic</samp>](## "ethernet_interfaces.[].ip_nat.source.dynamic") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;access_list</samp>](## "ethernet_interfaces.[].ip_nat.source.dynamic.[].access_list") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "ethernet_interfaces.[].ip_nat.source.dynamic.[].comment") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nat_type</samp>](## "ethernet_interfaces.[].ip_nat.source.dynamic.[].nat_type") | String | Required |  | Valid Values:<br>- <code>overload</code><br>- <code>pool</code><br>- <code>pool-address-only</code><br>- <code>pool-full-cone</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pool_name</samp>](## "ethernet_interfaces.[].ip_nat.source.dynamic.[].pool_name") | String |  |  |  | required if 'nat_type' is pool, pool-address-only or pool-full-cone.<br>ignored if 'nat_type' is overload.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "ethernet_interfaces.[].ip_nat.source.dynamic.[].priority") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "ethernet_interfaces.[].ip_nat.source.static") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;access_list</samp>](## "ethernet_interfaces.[].ip_nat.source.static.[].access_list") | String |  |  |  | 'access_list' and 'group' are mutual exclusive. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "ethernet_interfaces.[].ip_nat.source.static.[].comment") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "ethernet_interfaces.[].ip_nat.source.static.[].direction") | String |  |  | Valid Values:<br>- <code>egress</code><br>- <code>ingress</code> | Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.<br>EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "ethernet_interfaces.[].ip_nat.source.static.[].group") | Integer |  |  | Min: 1<br>Max: 65535 | 'access_list' and 'group' are mutual exclusive. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;original_ip</samp>](## "ethernet_interfaces.[].ip_nat.source.static.[].original_ip") | String |  |  |  | IPv4 address. The combination of `original_ip` and `original_port` must be unique. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;original_port</samp>](## "ethernet_interfaces.[].ip_nat.source.static.[].original_port") | Integer |  |  | Min: 1<br>Max: 65535 | TCP/UDP port. The combination of `original_ip` and `original_port` must be unique. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "ethernet_interfaces.[].ip_nat.source.static.[].priority") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "ethernet_interfaces.[].ip_nat.source.static.[].protocol") | String |  |  | Valid Values:<br>- <code>udp</code><br>- <code>tcp</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;translated_ip</samp>](## "ethernet_interfaces.[].ip_nat.source.static.[].translated_ip") | String | Required |  |  | IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;translated_port</samp>](## "ethernet_interfaces.[].ip_nat.source.static.[].translated_port") | Integer |  |  | Min: 1<br>Max: 65535 | requires 'original_port'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "ethernet_interfaces.[].ipv6_enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "ethernet_interfaces.[].ipv6_address") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_link_local</samp>](## "ethernet_interfaces.[].ipv6_address_link_local") | String |  |  |  | Link local IPv6 address/mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_ra_disabled</samp>](## "ethernet_interfaces.[].ipv6_nd_ra_disabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_managed_config_flag</samp>](## "ethernet_interfaces.[].ipv6_nd_managed_config_flag") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_prefixes</samp>](## "ethernet_interfaces.[].ipv6_nd_prefixes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ipv6_prefix</samp>](## "ethernet_interfaces.[].ipv6_nd_prefixes.[].ipv6_prefix") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;valid_lifetime</samp>](## "ethernet_interfaces.[].ipv6_nd_prefixes.[].valid_lifetime") | String |  |  |  | Infinite or lifetime in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preferred_lifetime</samp>](## "ethernet_interfaces.[].ipv6_nd_prefixes.[].preferred_lifetime") | String |  |  |  | Infinite or lifetime in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_autoconfig_flag</samp>](## "ethernet_interfaces.[].ipv6_nd_prefixes.[].no_autoconfig_flag") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_dhcp_relay_destinations</samp>](## "ethernet_interfaces.[].ipv6_dhcp_relay_destinations") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;address</samp>](## "ethernet_interfaces.[].ipv6_dhcp_relay_destinations.[].address") | String | Required, Unique |  |  | DHCP server's IPv6 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ethernet_interfaces.[].ipv6_dhcp_relay_destinations.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "ethernet_interfaces.[].ipv6_dhcp_relay_destinations.[].local_interface") | String |  |  |  | Local interface to communicate with DHCP server - mutually exclusive to source_address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "ethernet_interfaces.[].ipv6_dhcp_relay_destinations.[].source_address") | String |  |  |  | Source IPv6 address to communicate with DHCP server - mutually exclusive to local_interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_address</samp>](## "ethernet_interfaces.[].ipv6_dhcp_relay_destinations.[].link_address") | String |  |  |  | Override the default link address specified in the relayed DHCP packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_in</samp>](## "ethernet_interfaces.[].access_group_in") | String |  |  |  | Access list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_out</samp>](## "ethernet_interfaces.[].access_group_out") | String |  |  |  | Access list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_in</samp>](## "ethernet_interfaces.[].ipv6_access_group_in") | String |  |  |  | IPv6 access list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_out</samp>](## "ethernet_interfaces.[].ipv6_access_group_out") | String |  |  |  | IPv6 access list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_access_group_in</samp>](## "ethernet_interfaces.[].mac_access_group_in") | String |  |  |  | MAC access list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_access_group_out</samp>](## "ethernet_interfaces.[].mac_access_group_out") | String |  |  |  | MAC access list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp>](## "ethernet_interfaces.[].multicast") | Dictionary |  |  |  | Boundaries can be either 1 ACL or a list of multicast IP address_range(s)/prefix but not combination of both. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "ethernet_interfaces.[].multicast.ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;boundaries</samp>](## "ethernet_interfaces.[].multicast.ipv4.boundaries") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;boundary</samp>](## "ethernet_interfaces.[].multicast.ipv4.boundaries.[].boundary") | String |  |  |  | ACL name or multicast IP subnet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;out</samp>](## "ethernet_interfaces.[].multicast.ipv4.boundaries.[].out") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "ethernet_interfaces.[].multicast.ipv4.static") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "ethernet_interfaces.[].multicast.ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;boundaries</samp>](## "ethernet_interfaces.[].multicast.ipv6.boundaries") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;boundary</samp>](## "ethernet_interfaces.[].multicast.ipv6.boundaries.[].boundary") | String |  |  |  | ACL name or multicast IP subnet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "ethernet_interfaces.[].multicast.ipv6.static") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_network_point_to_point</samp>](## "ethernet_interfaces.[].ospf_network_point_to_point") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_area</samp>](## "ethernet_interfaces.[].ospf_area") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_cost</samp>](## "ethernet_interfaces.[].ospf_cost") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_authentication</samp>](## "ethernet_interfaces.[].ospf_authentication") | String |  |  | Valid Values:<br>- <code>none</code><br>- <code>simple</code><br>- <code>message-digest</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_authentication_key</samp>](## "ethernet_interfaces.[].ospf_authentication_key") | String |  |  |  | Encrypted password - only type 7 supported. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_message_digest_keys</samp>](## "ethernet_interfaces.[].ospf_message_digest_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "ethernet_interfaces.[].ospf_message_digest_keys.[].id") | Integer | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "ethernet_interfaces.[].ospf_message_digest_keys.[].hash_algorithm") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>sha1</code><br>- <code>sha256</code><br>- <code>sha384</code><br>- <code>sha512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "ethernet_interfaces.[].ospf_message_digest_keys.[].key") | String |  |  |  | Encrypted password - only type 7 supported. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pim</samp>](## "ethernet_interfaces.[].pim") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "ethernet_interfaces.[].pim.ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;border_router</samp>](## "ethernet_interfaces.[].pim.ipv4.border_router") | Boolean |  |  |  | Configure PIM border router. EOS default is false. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dr_priority</samp>](## "ethernet_interfaces.[].pim.ipv4.dr_priority") | Integer |  |  | Min: 0<br>Max: 429467295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sparse_mode</samp>](## "ethernet_interfaces.[].pim.ipv4.sparse_mode") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "ethernet_interfaces.[].pim.ipv4.bfd") | Boolean |  |  |  | Set the default for whether Bidirectional Forwarding Detection is enabled for PIM. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bidirectional</samp>](## "ethernet_interfaces.[].pim.ipv4.bidirectional") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hello</samp>](## "ethernet_interfaces.[].pim.ipv4.hello") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;count</samp>](## "ethernet_interfaces.[].pim.ipv4.hello.count") | String |  |  |  | Number of missed hellos after which the neighbor expires. Range <1.5-65535>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "ethernet_interfaces.[].pim.ipv4.hello.interval") | Integer |  |  | Min: 1<br>Max: 65535 | PIM hello interval in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_security</samp>](## "ethernet_interfaces.[].mac_security") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "ethernet_interfaces.[].mac_security.profile") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tcp_mss_ceiling</samp>](## "ethernet_interfaces.[].tcp_mss_ceiling") | Dictionary |  |  |  | The TCP MSS clamping feature involves clamping the maximum segment size (MSS) in the TCP header<br>of TCP SYN packets if it exceeds the configured MSS ceiling limit for the interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_segment_size</samp>](## "ethernet_interfaces.[].tcp_mss_ceiling.ipv4_segment_size") | Integer |  |  | Min: 64<br>Max: 65475 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_segment_size</samp>](## "ethernet_interfaces.[].tcp_mss_ceiling.ipv6_segment_size") | Integer |  |  | Min: 64<br>Max: 65475 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "ethernet_interfaces.[].tcp_mss_ceiling.direction") | String |  |  | Valid Values:<br>- <code>egress</code><br>- <code>ingress</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;channel_group</samp>](## "ethernet_interfaces.[].channel_group") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "ethernet_interfaces.[].channel_group.id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "ethernet_interfaces.[].channel_group.mode") | String |  |  | Valid Values:<br>- <code>on</code><br>- <code>active</code><br>- <code>passive</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_enable</samp>](## "ethernet_interfaces.[].isis_enable") | String |  |  |  | ISIS instance. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_bfd</samp>](## "ethernet_interfaces.[].isis_bfd") | Boolean |  |  |  | Enable BFD for ISIS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_passive</samp>](## "ethernet_interfaces.[].isis_passive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp>](## "ethernet_interfaces.[].isis_metric") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_network_point_to_point</samp>](## "ethernet_interfaces.[].isis_network_point_to_point") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_circuit_type</samp>](## "ethernet_interfaces.[].isis_circuit_type") | String |  |  | Valid Values:<br>- <code>level-1-2</code><br>- <code>level-1</code><br>- <code>level-2</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_hello_padding</samp>](## "ethernet_interfaces.[].isis_hello_padding") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_mode</samp>](## "ethernet_interfaces.[].isis_authentication_mode") | String |  |  | Valid Values:<br>- <code>text</code><br>- <code>md5</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_key</samp>](## "ethernet_interfaces.[].isis_authentication_key") | String |  |  |  | Type-7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;poe</samp>](## "ethernet_interfaces.[].poe") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "ethernet_interfaces.[].poe.disabled") | Boolean |  | `False` |  | Disable PoE on a POE capable port. PoE is enabled on all ports that support it by default in EOS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "ethernet_interfaces.[].poe.priority") | String |  |  | Valid Values:<br>- <code>critical</code><br>- <code>high</code><br>- <code>medium</code><br>- <code>low</code> | Prioritize a port's power in the event that one of the switch's power supplies loses power. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reboot</samp>](## "ethernet_interfaces.[].poe.reboot") | Dictionary |  |  |  | Set the PoE power behavior for a PoE port when the system is rebooted. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ethernet_interfaces.[].poe.reboot.action") | String |  |  | Valid Values:<br>- <code>maintain</code><br>- <code>power-off</code> | PoE action for interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_down</samp>](## "ethernet_interfaces.[].poe.link_down") | Dictionary |  |  |  | Set the PoE power behavior for a PoE port when the port goes down. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ethernet_interfaces.[].poe.link_down.action") | String |  |  | Valid Values:<br>- <code>maintain</code><br>- <code>power-off</code> | PoE action for interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;power_off_delay</samp>](## "ethernet_interfaces.[].poe.link_down.power_off_delay") | Integer |  |  | Min: 1<br>Max: 86400 | Number of seconds to delay shutting the power off after a link down event occurs. Default value is 5 seconds in EOS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "ethernet_interfaces.[].poe.shutdown") | Dictionary |  |  |  | Set the PoE power behavior for a PoE port when the port is admin down. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ethernet_interfaces.[].poe.shutdown.action") | String |  |  | Valid Values:<br>- <code>maintain</code><br>- <code>power-off</code> | PoE action for interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;limit</samp>](## "ethernet_interfaces.[].poe.limit") | Dictionary |  |  |  | Override the hardware-negotiated power limit using either wattage or a power class. Note that if using a power class, AVD will automatically convert the class value to the wattage value corresponding to that power class. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;class</samp>](## "ethernet_interfaces.[].poe.limit.class") | Integer |  |  | Min: 0<br>Max: 8 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;watts</samp>](## "ethernet_interfaces.[].poe.limit.watts") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fixed</samp>](## "ethernet_interfaces.[].poe.limit.fixed") | Boolean |  |  |  | Set to ignore hardware classification. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;negotiation_lldp</samp>](## "ethernet_interfaces.[].poe.negotiation_lldp") | Boolean |  |  |  | Disable to prevent port from negotiating power with powered devices over LLDP. Enabled by default in EOS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;legacy_detect</samp>](## "ethernet_interfaces.[].poe.legacy_detect") | Boolean |  |  |  | Allow a subset of legacy devices to work with the PoE switch. Disabled by default in EOS because it can cause false positive detections. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "ethernet_interfaces.[].ptp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "ethernet_interfaces.[].ptp.enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "ethernet_interfaces.[].ptp.announce") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "ethernet_interfaces.[].ptp.announce.interval") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "ethernet_interfaces.[].ptp.announce.timeout") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_req</samp>](## "ethernet_interfaces.[].ptp.delay_req") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_mechanism</samp>](## "ethernet_interfaces.[].ptp.delay_mechanism") | String |  |  | Valid Values:<br>- <code>e2e</code><br>- <code>p2p</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "ethernet_interfaces.[].ptp.profile") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;g8275_1</samp>](## "ethernet_interfaces.[].ptp.profile.g8275_1") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_mac_address</samp>](## "ethernet_interfaces.[].ptp.profile.g8275_1.destination_mac_address") | String |  |  | Valid Values:<br>- <code>forwardable</code><br>- <code>non-forwardable</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync_message</samp>](## "ethernet_interfaces.[].ptp.sync_message") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "ethernet_interfaces.[].ptp.sync_message.interval") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "ethernet_interfaces.[].ptp.role") | String |  |  | Valid Values:<br>- <code>master</code><br>- <code>dynamic</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "ethernet_interfaces.[].ptp.vlan") | String |  |  |  | VLAN can be 'all' or list of vlans as string. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transport</samp>](## "ethernet_interfaces.[].ptp.transport") | String |  |  | Valid Values:<br>- <code>ipv4</code><br>- <code>ipv6</code><br>- <code>layer2</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "ethernet_interfaces.[].profile") | String |  |  |  | Interface profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;storm_control</samp>](## "ethernet_interfaces.[].storm_control") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "ethernet_interfaces.[].storm_control.all") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "ethernet_interfaces.[].storm_control.all.level") | String |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "ethernet_interfaces.[].storm_control.all.unit") | String |  | `percent` | Valid Values:<br>- <code>percent</code><br>- <code>pps</code> | Optional field and is hardware dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;broadcast</samp>](## "ethernet_interfaces.[].storm_control.broadcast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "ethernet_interfaces.[].storm_control.broadcast.level") | String |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "ethernet_interfaces.[].storm_control.broadcast.unit") | String |  | `percent` | Valid Values:<br>- <code>percent</code><br>- <code>pps</code> | Optional field and is hardware dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp>](## "ethernet_interfaces.[].storm_control.multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "ethernet_interfaces.[].storm_control.multicast.level") | String |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "ethernet_interfaces.[].storm_control.multicast.unit") | String |  | `percent` | Valid Values:<br>- <code>percent</code><br>- <code>pps</code> | Optional field and is hardware dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unknown_unicast</samp>](## "ethernet_interfaces.[].storm_control.unknown_unicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "ethernet_interfaces.[].storm_control.unknown_unicast.level") | String |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "ethernet_interfaces.[].storm_control.unknown_unicast.unit") | String |  | `percent` | Valid Values:<br>- <code>percent</code><br>- <code>pps</code> | Optional field and is hardware dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "ethernet_interfaces.[].logging") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;event</samp>](## "ethernet_interfaces.[].logging.event") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_status</samp>](## "ethernet_interfaces.[].logging.event.link_status") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;congestion_drops</samp>](## "ethernet_interfaces.[].logging.event.congestion_drops") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree</samp>](## "ethernet_interfaces.[].logging.event.spanning_tree") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;storm_control_discards</samp>](## "ethernet_interfaces.[].logging.event.storm_control_discards") | Boolean |  |  |  | Discards due to storm-control.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lldp</samp>](## "ethernet_interfaces.[].lldp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transmit</samp>](## "ethernet_interfaces.[].lldp.transmit") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;receive</samp>](## "ethernet_interfaces.[].lldp.receive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ztp_vlan</samp>](## "ethernet_interfaces.[].lldp.ztp_vlan") | Integer |  |  |  | ZTP vlan number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_private_vlan_secondary</samp>](## "ethernet_interfaces.[].trunk_private_vlan_secondary") <span style="color:red">deprecated</span> | Boolean |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>switchport.trunk.private_vlan_secondary</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pvlan_mapping</samp>](## "ethernet_interfaces.[].pvlan_mapping") <span style="color:red">deprecated</span> | String |  |  |  | List of vlans as string.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>switchport.pvlan_mapping</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlan_translations</samp>](## "ethernet_interfaces.[].vlan_translations") <span style="color:red">deprecated</span> | List, items: Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>switchport.vlan_translations</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;from</samp>](## "ethernet_interfaces.[].vlan_translations.[].from") | String |  |  |  | List of vlans as string (only one vlan if direction is "both"). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to</samp>](## "ethernet_interfaces.[].vlan_translations.[].to") | Integer |  |  |  | VLAN ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "ethernet_interfaces.[].vlan_translations.[].direction") | String |  | `both` | Valid Values:<br>- <code>in</code><br>- <code>out</code><br>- <code>both</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dot1x</samp>](## "ethernet_interfaces.[].dot1x") | Dictionary |  |  |  | 802.1x |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_control</samp>](## "ethernet_interfaces.[].dot1x.port_control") | String |  |  | Valid Values:<br>- <code>auto</code><br>- <code>force-authorized</code><br>- <code>force-unauthorized</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_control_force_authorized_phone</samp>](## "ethernet_interfaces.[].dot1x.port_control_force_authorized_phone") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauthentication</samp>](## "ethernet_interfaces.[].dot1x.reauthentication") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pae</samp>](## "ethernet_interfaces.[].dot1x.pae") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "ethernet_interfaces.[].dot1x.pae.mode") | String |  |  | Valid Values:<br>- <code>authenticator</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication_failure</samp>](## "ethernet_interfaces.[].dot1x.authentication_failure") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ethernet_interfaces.[].dot1x.authentication_failure.action") | String |  |  | Valid Values:<br>- <code>allow</code><br>- <code>drop</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allow_vlan</samp>](## "ethernet_interfaces.[].dot1x.authentication_failure.allow_vlan") | Integer |  |  | Min: 1<br>Max: 4094 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_mode</samp>](## "ethernet_interfaces.[].dot1x.host_mode") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "ethernet_interfaces.[].dot1x.host_mode.mode") | String |  |  | Valid Values:<br>- <code>multi-host</code><br>- <code>single-host</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multi_host_authenticated</samp>](## "ethernet_interfaces.[].dot1x.host_mode.multi_host_authenticated") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_based_authentication</samp>](## "ethernet_interfaces.[].dot1x.mac_based_authentication") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ethernet_interfaces.[].dot1x.mac_based_authentication.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always</samp>](## "ethernet_interfaces.[].dot1x.mac_based_authentication.always") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_mode_common</samp>](## "ethernet_interfaces.[].dot1x.mac_based_authentication.host_mode_common") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_based_access_list</samp>](## "ethernet_interfaces.[].dot1x.mac_based_access_list") | Boolean |  |  |  | Operate interface in per-mac access-list mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "ethernet_interfaces.[].dot1x.timeout") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;idle_host</samp>](## "ethernet_interfaces.[].dot1x.timeout.idle_host") | Integer |  |  | Min: 10<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;quiet_period</samp>](## "ethernet_interfaces.[].dot1x.timeout.quiet_period") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauth_period</samp>](## "ethernet_interfaces.[].dot1x.timeout.reauth_period") | String |  |  |  | Value can be 60-4294967295 or 'server'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauth_timeout_ignore</samp>](## "ethernet_interfaces.[].dot1x.timeout.reauth_timeout_ignore") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tx_period</samp>](## "ethernet_interfaces.[].dot1x.timeout.tx_period") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reauthorization_request_limit</samp>](## "ethernet_interfaces.[].dot1x.reauthorization_request_limit") | Integer |  |  | Min: 1<br>Max: 10 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unauthorized</samp>](## "ethernet_interfaces.[].dot1x.unauthorized") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_vlan_membership_egress</samp>](## "ethernet_interfaces.[].dot1x.unauthorized.access_vlan_membership_egress") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;native_vlan_membership_egress</samp>](## "ethernet_interfaces.[].dot1x.unauthorized.native_vlan_membership_egress") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eapol</samp>](## "ethernet_interfaces.[].dot1x.eapol") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "ethernet_interfaces.[].dot1x.eapol.disabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication_failure_fallback_mba</samp>](## "ethernet_interfaces.[].dot1x.eapol.authentication_failure_fallback_mba") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ethernet_interfaces.[].dot1x.eapol.authentication_failure_fallback_mba.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "ethernet_interfaces.[].dot1x.eapol.authentication_failure_fallback_mba.timeout") | Integer |  |  | Min: 0<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;aaa</samp>](## "ethernet_interfaces.[].dot1x.aaa") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unresponsive</samp>](## "ethernet_interfaces.[].dot1x.aaa.unresponsive") | Dictionary |  |  |  | Configure AAA timeout options. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;eap_response</samp>](## "ethernet_interfaces.[].dot1x.aaa.unresponsive.eap_response") | String |  |  | Valid Values:<br>- <code>success</code><br>- <code>disabled</code> | EAP response to send. EOS default is `success`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ethernet_interfaces.[].dot1x.aaa.unresponsive.action") | Dictionary |  |  |  | Set action for supplicant when AAA times out. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_allow_access_list</samp>](## "ethernet_interfaces.[].dot1x.aaa.unresponsive.action.traffic_allow_access_list") | String |  |  |  | Name of standard access-list to apply when AAA times out. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;apply_cached_results</samp>](## "ethernet_interfaces.[].dot1x.aaa.unresponsive.action.apply_cached_results") | Boolean |  |  |  | Use results from a previous AAA response. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cached_results_timeout</samp>](## "ethernet_interfaces.[].dot1x.aaa.unresponsive.action.cached_results_timeout") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time_duration</samp>](## "ethernet_interfaces.[].dot1x.aaa.unresponsive.action.cached_results_timeout.time_duration") | Integer |  |  | Min: 1 | Enable caching for a specific duration -<br><1-10000>      duration in days<br><1-14400000>   duration in minutes<br><1-240000>     duration in hours<br><1-864000000>  duration in seconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time_duration_unit</samp>](## "ethernet_interfaces.[].dot1x.aaa.unresponsive.action.cached_results_timeout.time_duration_unit") | String | Required |  | Valid Values:<br>- <code>days</code><br>- <code>hours</code><br>- <code>minutes</code><br>- <code>seconds</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;apply_alternate</samp>](## "ethernet_interfaces.[].dot1x.aaa.unresponsive.action.apply_alternate") | Boolean |  |  |  | Apply alternate action if primary action fails.<br>eg. aaa unresponsive action apply cached-results else traffic allow |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_allow</samp>](## "ethernet_interfaces.[].dot1x.aaa.unresponsive.action.traffic_allow") | Boolean |  |  |  | Set action for supplicant traffic when AAA times out. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_allow_vlan</samp>](## "ethernet_interfaces.[].dot1x.aaa.unresponsive.action.traffic_allow_vlan") | Integer |  |  | Min: 1<br>Max: 4094 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;phone_action</samp>](## "ethernet_interfaces.[].dot1x.aaa.unresponsive.phone_action") | Dictionary |  |  |  | Set action for supplicant when AAA times out. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;apply_cached_results</samp>](## "ethernet_interfaces.[].dot1x.aaa.unresponsive.phone_action.apply_cached_results") | Boolean |  |  |  | Use results from a previous AAA response. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cached_results_timeout</samp>](## "ethernet_interfaces.[].dot1x.aaa.unresponsive.phone_action.cached_results_timeout") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time_duration</samp>](## "ethernet_interfaces.[].dot1x.aaa.unresponsive.phone_action.cached_results_timeout.time_duration") | Integer |  |  | Min: 1 | Enable caching for a specific duration -<br><1-10000>      duration in days<br><1-14400000>   duration in minutes<br><1-240000>     duration in hours<br><1-864000000>  duration in seconds |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;time_duration_unit</samp>](## "ethernet_interfaces.[].dot1x.aaa.unresponsive.phone_action.cached_results_timeout.time_duration_unit") | String | Required |  | Valid Values:<br>- <code>days</code><br>- <code>hours</code><br>- <code>minutes</code><br>- <code>seconds</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;apply_alternate</samp>](## "ethernet_interfaces.[].dot1x.aaa.unresponsive.phone_action.apply_alternate") | Boolean |  |  |  | Apply alternate action if primary action fails.<br>eg. aaa unresponsive phone action apply cached-results else traffic allow |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_allow</samp>](## "ethernet_interfaces.[].dot1x.aaa.unresponsive.phone_action.traffic_allow") | Boolean |  |  |  | Set action for supplicant traffic when AAA times out. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;service_profile</samp>](## "ethernet_interfaces.[].service_profile") | String |  |  |  | QOS profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shape</samp>](## "ethernet_interfaces.[].shape") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "ethernet_interfaces.[].shape.rate") | String |  |  |  | Rate in kbps, pps or percent.<br>Supported options are platform dependent.<br>Examples:<br>- "5000 kbps"<br>- "1000 pps"<br>- "20 percent"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;qos</samp>](## "ethernet_interfaces.[].qos") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trust</samp>](## "ethernet_interfaces.[].qos.trust") | String |  |  | Valid Values:<br>- <code>dscp</code><br>- <code>cos</code><br>- <code>disabled</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "ethernet_interfaces.[].qos.dscp") | Integer |  |  |  | DSCP value. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "ethernet_interfaces.[].qos.cos") | Integer |  |  |  | COS value. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpdufilter</samp>](## "ethernet_interfaces.[].spanning_tree_bpdufilter") | String |  |  | Valid Values:<br>- <code>enabled</code><br>- <code>disabled</code><br>- <code>True</code><br>- <code>False</code><br>- <code>true</code><br>- <code>false</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpduguard</samp>](## "ethernet_interfaces.[].spanning_tree_bpduguard") | String |  |  | Valid Values:<br>- <code>enabled</code><br>- <code>disabled</code><br>- <code>True</code><br>- <code>False</code><br>- <code>true</code><br>- <code>false</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_guard</samp>](## "ethernet_interfaces.[].spanning_tree_guard") | String |  |  | Valid Values:<br>- <code>loop</code><br>- <code>root</code><br>- <code>disabled</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_portfast</samp>](## "ethernet_interfaces.[].spanning_tree_portfast") | String |  |  | Valid Values:<br>- <code>edge</code><br>- <code>network</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vmtracer</samp>](## "ethernet_interfaces.[].vmtracer") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;priority_flow_control</samp>](## "ethernet_interfaces.[].priority_flow_control") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ethernet_interfaces.[].priority_flow_control.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priorities</samp>](## "ethernet_interfaces.[].priority_flow_control.priorities") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;priority</samp>](## "ethernet_interfaces.[].priority_flow_control.priorities.[].priority") | Integer | Required, Unique |  | Min: 0<br>Max: 7 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_drop</samp>](## "ethernet_interfaces.[].priority_flow_control.priorities.[].no_drop") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "ethernet_interfaces.[].bfd") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;echo</samp>](## "ethernet_interfaces.[].bfd.echo") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "ethernet_interfaces.[].bfd.interval") | Integer |  |  |  | Interval in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp>](## "ethernet_interfaces.[].bfd.min_rx") | Integer |  |  |  | Rate in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "ethernet_interfaces.[].bfd.multiplier") | Integer |  |  | Min: 3<br>Max: 50 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;service_policy</samp>](## "ethernet_interfaces.[].service_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pbr</samp>](## "ethernet_interfaces.[].service_policy.pbr") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input</samp>](## "ethernet_interfaces.[].service_policy.pbr.input") | String |  |  |  | Policy Based Routing Policy-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos</samp>](## "ethernet_interfaces.[].service_policy.qos") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input</samp>](## "ethernet_interfaces.[].service_policy.qos.input") | String | Required |  |  | Quality of Service Policy-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp>](## "ethernet_interfaces.[].mpls") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "ethernet_interfaces.[].mpls.ip") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ldp</samp>](## "ethernet_interfaces.[].mpls.ldp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "ethernet_interfaces.[].mpls.ldp.interface") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igp_sync</samp>](## "ethernet_interfaces.[].mpls.ldp.igp_sync") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lacp_timer</samp>](## "ethernet_interfaces.[].lacp_timer") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "ethernet_interfaces.[].lacp_timer.mode") | String |  |  | Valid Values:<br>- <code>fast</code><br>- <code>normal</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "ethernet_interfaces.[].lacp_timer.multiplier") | Integer |  |  | Min: 3<br>Max: 3000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lacp_port_priority</samp>](## "ethernet_interfaces.[].lacp_port_priority") | Integer |  |  | Min: 0<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;transceiver</samp>](## "ethernet_interfaces.[].transceiver") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;frequency</samp>](## "ethernet_interfaces.[].transceiver.frequency") | String |  |  |  | Transceiver Laser Frequency in GHz (min 190000, max 200000). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;frequency_unit</samp>](## "ethernet_interfaces.[].transceiver.frequency_unit") | String |  |  | Valid Values:<br>- <code>ghz</code> | Unit of Transceiver Laser Frequency. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;media</samp>](## "ethernet_interfaces.[].transceiver.media") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;override</samp>](## "ethernet_interfaces.[].transceiver.media.override") | String |  |  |  | Transceiver type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_proxy_arp</samp>](## "ethernet_interfaces.[].ip_proxy_arp") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;traffic_policy</samp>](## "ethernet_interfaces.[].traffic_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input</samp>](## "ethernet_interfaces.[].traffic_policy.input") | String |  |  |  | Ingress traffic policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;output</samp>](## "ethernet_interfaces.[].traffic_policy.output") | String |  |  |  | Egress traffic policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "ethernet_interfaces.[].bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session_tracker</samp>](## "ethernet_interfaces.[].bgp.session_tracker") | String |  |  |  | Name of session tracker. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_igmp_host_proxy</samp>](## "ethernet_interfaces.[].ip_igmp_host_proxy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ethernet_interfaces.[].ip_igmp_host_proxy.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "ethernet_interfaces.[].ip_igmp_host_proxy.groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "ethernet_interfaces.[].ip_igmp_host_proxy.groups.[].group") | String | Required, Unique |  |  | Multicast Address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exclude</samp>](## "ethernet_interfaces.[].ip_igmp_host_proxy.groups.[].exclude") | List, items: Dictionary |  |  |  | The same source must not be present both in `exclude` and `include` list. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;source</samp>](## "ethernet_interfaces.[].ip_igmp_host_proxy.groups.[].exclude.[].source") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include</samp>](## "ethernet_interfaces.[].ip_igmp_host_proxy.groups.[].include") | List, items: Dictionary |  |  |  | The same source must not be present both in `exclude` and `include` list. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;source</samp>](## "ethernet_interfaces.[].ip_igmp_host_proxy.groups.[].include.[].source") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;report_interval</samp>](## "ethernet_interfaces.[].ip_igmp_host_proxy.report_interval") | Integer |  |  | Min: 1<br>Max: 31744 | Time interval between unsolicited reports. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_lists</samp>](## "ethernet_interfaces.[].ip_igmp_host_proxy.access_lists") | List, items: Dictionary |  |  |  | Non-standard Access List name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "ethernet_interfaces.[].ip_igmp_host_proxy.access_lists.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "ethernet_interfaces.[].ip_igmp_host_proxy.version") | Integer |  |  | Min: 1<br>Max: 3 | IGMP version on IGMP host-proxy interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "ethernet_interfaces.[].peer") | String |  |  |  | Key only used for documentation or validation purposes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_interface</samp>](## "ethernet_interfaces.[].peer_interface") | String |  |  |  | Key only used for documentation or validation purposes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_type</samp>](## "ethernet_interfaces.[].peer_type") | String |  |  |  | Key only used for documentation or validation purposes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sflow</samp>](## "ethernet_interfaces.[].sflow") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "ethernet_interfaces.[].sflow.enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;egress</samp>](## "ethernet_interfaces.[].sflow.egress") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "ethernet_interfaces.[].sflow.egress.enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unmodified_enable</samp>](## "ethernet_interfaces.[].sflow.egress.unmodified_enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sync_e</samp>](## "ethernet_interfaces.[].sync_e") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "ethernet_interfaces.[].sync_e.enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "ethernet_interfaces.[].sync_e.priority") | String |  |  |  | The priority is used to influence the reference clock selection. The EOS default priority is 127. The priority can be configured to any integer between 1-255, or set to `disabled`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;port_profile</samp>](## "ethernet_interfaces.[].port_profile") | String |  |  |  | Key only used for documentation or validation purposes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uc_tx_queues</samp>](## "ethernet_interfaces.[].uc_tx_queues") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "ethernet_interfaces.[].uc_tx_queues.[].id") | Integer | Required, Unique |  |  | TX-Queue ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;random_detect</samp>](## "ethernet_interfaces.[].uc_tx_queues.[].random_detect") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ecn</samp>](## "ethernet_interfaces.[].uc_tx_queues.[].random_detect.ecn") | Dictionary |  |  |  | Explicit Congestion Notification. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;count</samp>](## "ethernet_interfaces.[].uc_tx_queues.[].random_detect.ecn.count") | Boolean |  |  |  | Enable counter for random-detect ECNs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "ethernet_interfaces.[].uc_tx_queues.[].random_detect.ecn.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;units</samp>](## "ethernet_interfaces.[].uc_tx_queues.[].random_detect.ecn.threshold.units") | String | Required |  | Valid Values:<br>- <code>segments</code><br>- <code>bytes</code><br>- <code>kbytes</code><br>- <code>mbytes</code><br>- <code>milliseconds</code> | Indicate the units to be used for the threshold values. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min</samp>](## "ethernet_interfaces.[].uc_tx_queues.[].random_detect.ecn.threshold.min") | Integer | Required |  | Min: 1<br>Max: 256000000 | Set the random-detect ECN minimum-threshold. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max</samp>](## "ethernet_interfaces.[].uc_tx_queues.[].random_detect.ecn.threshold.max") | Integer | Required |  | Min: 1<br>Max: 256000000 | Set the random-detect ECN maximum-threshold. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_probability</samp>](## "ethernet_interfaces.[].uc_tx_queues.[].random_detect.ecn.threshold.max_probability") | Integer |  |  | Min: 1<br>Max: 100 | Set the random-detect ECN max-mark-probability. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "ethernet_interfaces.[].uc_tx_queues.[].random_detect.ecn.threshold.weight") | Integer |  |  | Min: 0<br>Max: 15 | Set the random-detect ECN weight. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tx_queues</samp>](## "ethernet_interfaces.[].tx_queues") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "ethernet_interfaces.[].tx_queues.[].id") | Integer | Required, Unique |  |  | TX-Queue ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;random_detect</samp>](## "ethernet_interfaces.[].tx_queues.[].random_detect") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ecn</samp>](## "ethernet_interfaces.[].tx_queues.[].random_detect.ecn") | Dictionary |  |  |  | Explicit Congestion Notification. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;count</samp>](## "ethernet_interfaces.[].tx_queues.[].random_detect.ecn.count") | Boolean |  |  |  | Enable counter for random-detect ECNs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "ethernet_interfaces.[].tx_queues.[].random_detect.ecn.threshold") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;units</samp>](## "ethernet_interfaces.[].tx_queues.[].random_detect.ecn.threshold.units") | String | Required |  | Valid Values:<br>- <code>segments</code><br>- <code>bytes</code><br>- <code>kbytes</code><br>- <code>mbytes</code><br>- <code>milliseconds</code> | Indicate the units to be used for the threshold values. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min</samp>](## "ethernet_interfaces.[].tx_queues.[].random_detect.ecn.threshold.min") | Integer |  |  | Min: 1<br>Max: 256000000 | Set the random-detect ECN minimum-threshold. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max</samp>](## "ethernet_interfaces.[].tx_queues.[].random_detect.ecn.threshold.max") | Integer | Required |  | Min: 1<br>Max: 256000000 | Set the random-detect ECN maximum-threshold. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_probability</samp>](## "ethernet_interfaces.[].tx_queues.[].random_detect.ecn.threshold.max_probability") | Integer | Required |  | Min: 1<br>Max: 100 | Set the random-detect ECN max-mark-probability. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;weight</samp>](## "ethernet_interfaces.[].tx_queues.[].random_detect.ecn.threshold.weight") | Integer |  |  | Min: 0<br>Max: 15 | Set the random-detect ECN weight. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrrp_ids</samp>](## "ethernet_interfaces.[].vrrp_ids") | List, items: Dictionary |  |  |  | VRRP model. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "ethernet_interfaces.[].vrrp_ids.[].id") | Integer | Required, Unique |  |  | VRID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority_level</samp>](## "ethernet_interfaces.[].vrrp_ids.[].priority_level") | Integer |  |  | Min: 1<br>Max: 254 | Instance priority. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;advertisement</samp>](## "ethernet_interfaces.[].vrrp_ids.[].advertisement") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "ethernet_interfaces.[].vrrp_ids.[].advertisement.interval") | Integer |  |  | Min: 1<br>Max: 255 | Interval in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preempt</samp>](## "ethernet_interfaces.[].vrrp_ids.[].preempt") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ethernet_interfaces.[].vrrp_ids.[].preempt.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "ethernet_interfaces.[].vrrp_ids.[].preempt.delay") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minimum</samp>](## "ethernet_interfaces.[].vrrp_ids.[].preempt.delay.minimum") | Integer |  |  | Min: 0<br>Max: 3600 | Minimum preempt delay in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reload</samp>](## "ethernet_interfaces.[].vrrp_ids.[].preempt.delay.reload") | Integer |  |  | Min: 0<br>Max: 3600 | Reload preempt delay in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "ethernet_interfaces.[].vrrp_ids.[].timers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "ethernet_interfaces.[].vrrp_ids.[].timers.delay") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reload</samp>](## "ethernet_interfaces.[].vrrp_ids.[].timers.delay.reload") | Integer |  |  | Min: 0<br>Max: 3600 | Delay after reload in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tracked_object</samp>](## "ethernet_interfaces.[].vrrp_ids.[].tracked_object") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "ethernet_interfaces.[].vrrp_ids.[].tracked_object.[].name") | String | Required, Unique |  |  | Tracked object name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decrement</samp>](## "ethernet_interfaces.[].vrrp_ids.[].tracked_object.[].decrement") | Integer |  |  | Min: 1<br>Max: 254 | Decrement VRRP priority by 1-254. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "ethernet_interfaces.[].vrrp_ids.[].tracked_object.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "ethernet_interfaces.[].vrrp_ids.[].ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address</samp>](## "ethernet_interfaces.[].vrrp_ids.[].ipv4.address") | String | Required |  |  | Virtual IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "ethernet_interfaces.[].vrrp_ids.[].ipv4.version") | Integer |  |  | Valid Values:<br>- <code>2</code><br>- <code>3</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "ethernet_interfaces.[].vrrp_ids.[].ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address</samp>](## "ethernet_interfaces.[].vrrp_ids.[].ipv6.address") | String | Required |  |  | Virtual IPv6 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;validate_state</samp>](## "ethernet_interfaces.[].validate_state") | Boolean |  |  |  | Set to false to disable interface validation by the `eos_validate_state` role. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;switchport</samp>](## "ethernet_interfaces.[].switchport") | Dictionary |  |  |  | This should not be combined with `ethernet_interfaces[].type = switched/routed`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ethernet_interfaces.[].switchport.enabled") | Boolean |  |  |  | Warning: This should not be combined with `ethernet_interfaces[].type = routed`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "ethernet_interfaces.[].switchport.mode") | String |  |  | Valid Values:<br>- <code>access</code><br>- <code>dot1q-tunnel</code><br>- <code>trunk</code><br>- <code>trunk phone</code> | Warning: This should not be combined with `ethernet_interfaces[].mode`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_vlan</samp>](## "ethernet_interfaces.[].switchport.access_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Set VLAN when interface is in access mode.<br>Warning: This should not be combined with `ethernet_interfaces[].mode = access/dot1q-tunnel` and `ethernet_interface[].vlans`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk</samp>](## "ethernet_interfaces.[].switchport.trunk") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allowed_vlan</samp>](## "ethernet_interfaces.[].switchport.trunk.allowed_vlan") | String |  |  |  | VLAN ID or range(s) of VLAN IDs.<br>Warning: This should not be combined with `ethernet_interfaces[].mode = trunk` and `ethernet_interface[].vlans`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;native_vlan</samp>](## "ethernet_interfaces.[].switchport.trunk.native_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Set native VLAN when interface is in trunking mode.<br>Warning: This should not be combined with `ethernet_interfaces[].native_vlan`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;native_vlan_tag</samp>](## "ethernet_interfaces.[].switchport.trunk.native_vlan_tag") | Boolean |  |  |  | If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence.<br>Warning: This should not be combined with `ethernet_interfaces[].native_vlan_tag`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;private_vlan_secondary</samp>](## "ethernet_interfaces.[].switchport.trunk.private_vlan_secondary") | Boolean |  |  |  | Enable secondary VLAN mapping for a private vlan.<br>Warning: This should not be combined with `ethernet_ineterfaces[].trunk_private_vlan_secondary`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "ethernet_interfaces.[].switchport.trunk.groups") | List, items: String |  |  |  | Warning: This should not be combined with `ethernet_ineterfaces[].trunk_groups`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "ethernet_interfaces.[].switchport.trunk.groups.[]") | String |  |  |  | Trunk group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;phone</samp>](## "ethernet_interfaces.[].switchport.phone") | Dictionary |  |  |  | Warning: This should not be combined with `ethernet_interfaces[].phone`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "ethernet_interfaces.[].switchport.phone.vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Warning: This should not be combined with `ethernet_interfaces[].phone.vlan`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk</samp>](## "ethernet_interfaces.[].switchport.phone.trunk") | String |  |  | Valid Values:<br>- <code>tagged</code><br>- <code>tagged phone</code><br>- <code>untagged</code><br>- <code>untagged phone</code> | Warning: This should not be combined with `ethernet_interfaces[].phone.trunk`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pvlan_mapping</samp>](## "ethernet_interfaces.[].switchport.pvlan_mapping") | String |  |  |  | Secondary VLAN IDs of the private VLAN mapping.<br>Warning: This should not be combined with `ethernet_interfaces[].pvlan_mapping`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1q</samp>](## "ethernet_interfaces.[].switchport.dot1q") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ethertype</samp>](## "ethernet_interfaces.[].switchport.dot1q.ethertype") | Integer |  |  | Min: 1536<br>Max: 65535 | Ethertype/TPID (Tag Protocol IDentifier) for VLAN tagged frames. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_tag</samp>](## "ethernet_interfaces.[].switchport.dot1q.vlan_tag") | String |  |  | Valid Values:<br>- <code>disallowed</code><br>- <code>required</code> | Allow/disallow VLAN tagged frames. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "ethernet_interfaces.[].switchport.source_interface") | String |  |  | Valid Values:<br>- <code>tx</code><br>- <code>tx multicast</code> | tx: Allow bridged traffic to go out of the source interface.<br>tx multicast: Allow multicast traffic only to go out of the source interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_translations</samp>](## "ethernet_interfaces.[].switchport.vlan_translations") | Dictionary |  |  |  | VLAN Translation mappings.<br>Warning: This should not be combined with `ethernet_interfaces[].vlan_translations`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;in_required</samp>](## "ethernet_interfaces.[].switchport.vlan_translations.in_required") | Boolean |  |  |  | Drop the ingress traffic that do not match any VLAN mapping. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;out_required</samp>](## "ethernet_interfaces.[].switchport.vlan_translations.out_required") | Boolean |  |  |  | Drop the egress traffic that do not match any VLAN mapping. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in</samp>](## "ethernet_interfaces.[].switchport.vlan_translations.direction_in") | List, items: Dictionary |  |  |  | Map ingress traffic only. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;from</samp>](## "ethernet_interfaces.[].switchport.vlan_translations.direction_in.[].from") | String | Required |  |  | VLAN ID or range of VLAN IDs to map from. Range 1-4094. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to</samp>](## "ethernet_interfaces.[].switchport.vlan_translations.direction_in.[].to") | Integer | Required |  | Min: 1<br>Max: 4094 | VLAN ID to map to. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1q_tunnel</samp>](## "ethernet_interfaces.[].switchport.vlan_translations.direction_in.[].dot1q_tunnel") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner_vlan_from</samp>](## "ethernet_interfaces.[].switchport.vlan_translations.direction_in.[].inner_vlan_from") | Integer |  |  | Min: 1<br>Max: 4094 | Inner VLAN ID to map from. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out</samp>](## "ethernet_interfaces.[].switchport.vlan_translations.direction_out") | List, items: Dictionary |  |  |  | Map egress traffic only. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;from</samp>](## "ethernet_interfaces.[].switchport.vlan_translations.direction_out.[].from") | String | Required |  |  | VLAN ID or range of VLAN IDs to map from. Range 1-4094. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to</samp>](## "ethernet_interfaces.[].switchport.vlan_translations.direction_out.[].to") | Integer |  |  | Min: 1<br>Max: 4094 | VLAN ID to map to. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1q_tunnel_to</samp>](## "ethernet_interfaces.[].switchport.vlan_translations.direction_out.[].dot1q_tunnel_to") | String |  |  |  | VLAN ID or range of VLAN IDs or "all". Range 1-4094.<br>This takes precedence over `to` and `inner_vlan_to`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner_vlan_to</samp>](## "ethernet_interfaces.[].switchport.vlan_translations.direction_out.[].inner_vlan_to") | Integer |  |  | Min: 1<br>Max: 4094 | Inner VLAN ID to map to. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_both</samp>](## "ethernet_interfaces.[].switchport.vlan_translations.direction_both") | List, items: Dictionary |  |  |  | Map both egress and ingress traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;from</samp>](## "ethernet_interfaces.[].switchport.vlan_translations.direction_both.[].from") | String | Required |  |  | VLAN ID or range of VLAN IDs to map from. Range 1-4094. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to</samp>](## "ethernet_interfaces.[].switchport.vlan_translations.direction_both.[].to") | Integer | Required |  | Min: 1<br>Max: 4094 | VLAN ID to map to. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1q_tunnel</samp>](## "ethernet_interfaces.[].switchport.vlan_translations.direction_both.[].dot1q_tunnel") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner_vlan_from</samp>](## "ethernet_interfaces.[].switchport.vlan_translations.direction_both.[].inner_vlan_from") | Integer |  |  | Min: 1<br>Max: 4094 | Inner VLAN ID to map from. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;network</samp>](## "ethernet_interfaces.[].switchport.vlan_translations.direction_both.[].network") | Boolean |  |  |  | Enable use of network-side VLAN ID.<br>This setting can only be enabled when `inner_vlan_from` is defined. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_forwarding_accept_all</samp>](## "ethernet_interfaces.[].switchport.vlan_forwarding_accept_all") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;backup_link</samp>](## "ethernet_interfaces.[].switchport.backup_link") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "ethernet_interfaces.[].switchport.backup_link.interface") | String |  |  |  | Backup interface. Example - Ethernet4, Vlan10 etc. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefer_vlan</samp>](## "ethernet_interfaces.[].switchport.backup_link.prefer_vlan") | String |  |  |  | VLANs to carry on the backup interface (1-4094). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;backup</samp>](## "ethernet_interfaces.[].switchport.backup") | Dictionary |  |  |  | The `backup_link` is required for this setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dest_macaddr</samp>](## "ethernet_interfaces.[].switchport.backup.dest_macaddr") | String |  |  | Format: mac | Destination MAC address for MAC move updates.<br>The mac address should be multicast or broadcast.<br>Example: 01:00:00:00:00:00 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;initial_mac_move_delay</samp>](## "ethernet_interfaces.[].switchport.backup.initial_mac_move_delay") | Integer |  |  | Min: 0<br>Max: 65535 | Initial MAC move delay in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_move_burst</samp>](## "ethernet_interfaces.[].switchport.backup.mac_move_burst") | Integer |  |  | Min: 0<br>Max: 65535 | Size of MAC move bursts. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_move_burst_interval</samp>](## "ethernet_interfaces.[].switchport.backup.mac_move_burst_interval") | Integer |  |  | Min: 0<br>Max: 65535 | MAC move burst interval in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preemption_delay</samp>](## "ethernet_interfaces.[].switchport.backup.preemption_delay") | Integer |  |  | Min: 0<br>Max: 65535 | Preemption delay in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_security</samp>](## "ethernet_interfaces.[].switchport.port_security") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "ethernet_interfaces.[].switchport.port_security.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_address_maximum</samp>](## "ethernet_interfaces.[].switchport.port_security.mac_address_maximum") | Dictionary |  |  |  | Maximum number of MAC addresses allowed on the interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "ethernet_interfaces.[].switchport.port_security.mac_address_maximum.disabled") | Boolean |  |  |  | Disable port level check for port security (only in violation 'shutdown' mode). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;limit</samp>](## "ethernet_interfaces.[].switchport.port_security.mac_address_maximum.limit") | Integer |  |  | Min: 1<br>Max: 1000 | MAC address limit. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;violation</samp>](## "ethernet_interfaces.[].switchport.port_security.violation") | Dictionary |  |  |  | Configure violation mode (shutdown or protect), EOS default is 'shutdown'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "ethernet_interfaces.[].switchport.port_security.violation.mode") | String |  |  | Valid Values:<br>- <code>shutdown</code><br>- <code>protect</code> | Configure port security mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protect_log</samp>](## "ethernet_interfaces.[].switchport.port_security.violation.protect_log") | Boolean |  |  |  | Log new addresses seen after limit is reached in protect mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_default_mac_address_maximum</samp>](## "ethernet_interfaces.[].switchport.port_security.vlan_default_mac_address_maximum") | Integer |  |  | Min: 0<br>Max: 1000 | Default maximum MAC addresses for all VLANs on this interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlans</samp>](## "ethernet_interfaces.[].switchport.port_security.vlans") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;range</samp>](## "ethernet_interfaces.[].switchport.port_security.vlans.[].range") | String | Required, Unique |  |  | VLAN ID or range(s) of VLAN IDs, <1-4094>.<br>Example:<br>  - 3<br>  - 1,3<br>  - 1-10<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_address_maximum</samp>](## "ethernet_interfaces.[].switchport.port_security.vlans.[].mac_address_maximum") | Integer | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "ethernet_interfaces.[].eos_cli") | String |  |  |  | Multiline EOS CLI rendered directly on the ethernet interface in the final EOS configuration. |

=== "YAML"

    ```yaml
    ethernet_interfaces:
      - name: <str; required; unique>
        description: <str>
        shutdown: <bool>

        # Interval in seconds for updating interface counters.
        load_interval: <int; 0-600>

        # Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
        speed: <str>
        mtu: <int; 68-65535>

        # "l2_mtu" should only be defined for platforms supporting the "l2 mtu" CLI.
        l2_mtu: <int; 68-65535>

        # "l2_mru" should only be defined for platforms supporting the "l2 mru" CLI.
        l2_mru: <int; 68-65535>

        # List of switchport vlans as string.
        # For a trunk port this would be a range like "1-200,300".
        # For an access port this would be a single vlan "123".
        # This key is deprecated.
        # Support will be removed in AVD version 6.0.0.
        # Use <samp>switchport.access_vlan or switchport.trunk.allowed_vlan</samp> instead.
        vlans: <str>
        # This key is deprecated.
        # Support will be removed in AVD version 6.0.0.
        # Use <samp>switchport.trunk.native_vlan</samp> instead.
        native_vlan: <int>

        # If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence.
        # This key is deprecated.
        # Support will be removed in AVD version 6.0.0.
        # Use <samp>switchport.trunk.native_vlan_tag</samp> instead.
        native_vlan_tag: <bool>
        # This key is deprecated.
        # Support will be removed in AVD version 6.0.0.
        # Use <samp>switchport.mode</samp> instead.
        mode: <str; "access" | "dot1q-tunnel" | "trunk" | "trunk phone">
        # This key is deprecated.
        # Support will be removed in AVD version 6.0.0.
        # Use <samp>switchport.phone</samp> instead.
        phone:
          trunk: <str; "tagged" | "tagged phone" | "untagged" | "untagged phone">
          vlan: <int; 1-4094>
        l2_protocol:

          # Vlan tag to configure on sub-interface.
          encapsulation_dot1q_vlan: <int>

          # L2 protocol forwarding profile.
          forwarding_profile: <str>
        # This key is deprecated.
        # Support will be removed in AVD version 6.0.0.
        # Use <samp>switchport.trunk.groups</samp> instead.
        trunk_groups:
          - <str>

        # l3dot1q and l2dot1q are used for sub-interfaces. The parent interface should be defined as routed.
        # The `type = switched/routed` should not be combined with `switchport`.
        # This key is deprecated.
        # Support will be removed in AVD version 6.0.0.
        # See [here](https://avd.arista.com/stable/docs/release-notes/5.x.x.html#removal-of-type-key-dependency-for-rendering-ethernetport-channel-interfaces-configuration-and-documentation) for details.
        type: <str; "routed" | "switched" | "l3dot1q" | "l2dot1q" | "port-channel-member">
        snmp_trap_link_change: <bool>
        address_locking:

          # Enable address locking for IPv4.
          ipv4: <bool>

          # Enable address locking for IPv6.
          ipv6: <bool>
        flowcontrol:
          received: <str; "desired" | "on" | "off">

        # VRF name.
        vrf: <str>
        flow_tracker:

          # Sampled flow tracker name.
          sampled: <str>

          # Hardware flow tracker name.
          hardware: <str>
        error_correction_encoding:
          enabled: <bool; default=True>
          fire_code: <bool>
          reed_solomon: <bool>
        link_tracking_groups:

            # Group name.
          - name: <str; required; unique>
            direction: <str; "upstream" | "downstream">
        evpn_ethernet_segment:

          # EVPN Ethernet Segment Identifier (Type 1 format).
          identifier: <str>
          redundancy: <str; "all-active" | "single-active">
          designated_forwarder_election:
            algorithm: <str; "modulus" | "preference">

            # Preference_value is only used when "algorithm" is "preference".
            preference_value: <int; 0-65535>

            # Dont_preempt is only used when "algorithm" is "preference".
            dont_preempt: <bool>
            hold_time: <int>
            subsequent_hold_time: <int>
            candidate_reachability_required: <bool>
          mpls:
            shared_index: <int; 1-1024>
            tunnel_flood_filter_time: <int>

          # EVPN Route Target for ESI with format xx:xx:xx:xx:xx:xx.
          route_target: <str>

        # VLAN tag to configure on sub-interface.
        # This key is deprecated.
        # Support will be removed in AVD version 6.0.0.
        # Use <samp>encapsulation_dot1q.vlan</samp> instead.
        encapsulation_dot1q_vlan: <int>

        # Warning: `encapsulation_dot1q` should not be combined with `ethernet_interfaces[].type: l3dot1q` or `ethernet_interfaces[].type: l2dot1q`.
        encapsulation_dot1q:

          # VLAD ID.
          vlan: <int; 1-4094; required>

          # Inner VLAN ID. This setting can only be applied to sub-interfaces on EOS.
          inner_vlan: <int; 1-4094>

        # This setting can only be applied to sub-interfaces on EOS.
        # Warning: `encapsulation_vlan` should not be combined with `ethernet_interfaces[].type: l3dot1q` or `ethernet_interfaces[].type: l2dot1q`.
        encapsulation_vlan:
          client:
            # This key is deprecated.
            # Support will be removed in AVD version 6.0.0.
            dot1q:

              # Client VLAN ID.
              vlan: <int; 1-4094>

              # Client Outer VLAN ID.
              outer: <int; 1-4094>

              # Client Inner VLAN ID.
              inner: <int>
            # This key is deprecated.
            # Support will be removed in AVD version 6.0.0.
            unmatched: <bool>
            encapsulation: <str; "dot1q" | "dot1ad" | "unmatched" | "untagged">

            # Client VLAN ID. Not applicable for `encapsulation: untagged` or `encapsulation: unmatched`.
            vlan: <int; 1-4094>

            # Client Outer VLAN ID. Not applicable for `encapsulation: untagged` or `encapsulation: unmatched`.
            outer_vlan: <int; 1-4094>

            # Client Inner VLAN ID. Not applicable for `encapsulation: untagged` or `encapsulation: unmatched`.
            inner_vlan: <int; 1-4094>
            inner_encapsulation: <str; "dot1q" | "dot1ad">

          # Network encapsulations are all optional and skipped if using client unmatched.
          network:
            # This key is deprecated.
            # Support will be removed in AVD version 6.0.0.
            dot1q:

              # Network VLAN ID.
              vlan: <int; 1-4094>

              # Network outer VLAN ID.
              outer: <int; 1-4094>

              # Network inner VLAN ID.
              inner: <int; 1-4094>
            # This key is deprecated.
            # Support will be removed in AVD version 6.0.0.
            client: <bool>

            # `untagged` (no encapsulation) is applicable for `untagged` client only.
            # `client` and `client inner` (retain client encapsulation) is not applicable for `untagged` client.
            encapsulation: <str; "dot1q" | "dot1ad" | "client" | "client inner" | "untagged">

            # Network VLAN ID. Not applicable for `encapsulation: untagged` or `encapsulation: client`.
            vlan: <int; 1-4094>

            # Network outer VLAN ID. Not applicable for `encapsulation: untagged` or `encapsulation: client`.
            outer_vlan: <int; 1-4094>

            # Network inner VLAN ID.  Not applicable for `encapsulation: untagged` or `encapsulation: client`.
            inner_vlan: <int; 1-4094>
            inner_encapsulation: <str; "dot1q" | "dot1ad">

        # This setting can only be applied to sub-interfaces on EOS.
        # Warning: `vlan_id` should not be combined with `ethernet_interfaces[].type == l2dot1q`.
        vlan_id: <int; 1-4094>

        # IPv4 address/mask or "dhcp".
        ip_address: <str>
        ip_address_secondaries:
          - <str>
        ip_verify_unicast_source_reachable_via: <str; "any" | "rx">

        # Install default-route obtained via DHCP.
        dhcp_client_accept_default_route: <bool>

        # Enable IPv4 DHCP server.
        dhcp_server_ipv4: <bool>

        # Enable IPv6 DHCP server.
        dhcp_server_ipv6: <bool>
        ip_helpers:
          - ip_helper: <str; required; unique>

            # Source interface name.
            source_interface: <str>

            # VRF name.
            vrf: <str>
        ip_nat:

          # NAT interface profile.
          service_profile: <str>
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
        ipv6_enable: <bool>
        ipv6_address: <str>

        # Link local IPv6 address/mask.
        ipv6_address_link_local: <str>
        ipv6_nd_ra_disabled: <bool>
        ipv6_nd_managed_config_flag: <bool>
        ipv6_nd_prefixes:
          - ipv6_prefix: <str; required; unique>

            # Infinite or lifetime in seconds.
            valid_lifetime: <str>

            # Infinite or lifetime in seconds.
            preferred_lifetime: <str>
            no_autoconfig_flag: <bool>
        ipv6_dhcp_relay_destinations:

            # DHCP server's IPv6 address.
          - address: <str; required; unique>
            vrf: <str>

            # Local interface to communicate with DHCP server - mutually exclusive to source_address.
            local_interface: <str>

            # Source IPv6 address to communicate with DHCP server - mutually exclusive to local_interface.
            source_address: <str>

            # Override the default link address specified in the relayed DHCP packet.
            link_address: <str>

        # Access list name.
        access_group_in: <str>

        # Access list name.
        access_group_out: <str>

        # IPv6 access list name.
        ipv6_access_group_in: <str>

        # IPv6 access list name.
        ipv6_access_group_out: <str>

        # MAC access list name.
        mac_access_group_in: <str>

        # MAC access list name.
        mac_access_group_out: <str>

        # Boundaries can be either 1 ACL or a list of multicast IP address_range(s)/prefix but not combination of both.
        multicast:
          ipv4:
            boundaries:

                # ACL name or multicast IP subnet.
              - boundary: <str>
                out: <bool>
            static: <bool>
          ipv6:
            boundaries:

                # ACL name or multicast IP subnet.
              - boundary: <str>
            static: <bool>
        ospf_network_point_to_point: <bool>
        ospf_area: <str>
        ospf_cost: <int>
        ospf_authentication: <str; "none" | "simple" | "message-digest">

        # Encrypted password - only type 7 supported.
        ospf_authentication_key: <str>
        ospf_message_digest_keys:
          - id: <int; required; unique>
            hash_algorithm: <str; "md5" | "sha1" | "sha256" | "sha384" | "sha512">

            # Encrypted password - only type 7 supported.
            key: <str>
        pim:
          ipv4:

            # Configure PIM border router. EOS default is false.
            border_router: <bool>
            dr_priority: <int; 0-429467295>
            sparse_mode: <bool>

            # Set the default for whether Bidirectional Forwarding Detection is enabled for PIM.
            bfd: <bool>
            bidirectional: <bool>
            hello:

              # Number of missed hellos after which the neighbor expires. Range <1.5-65535>.
              count: <str>

              # PIM hello interval in seconds.
              interval: <int; 1-65535>
        mac_security:
          profile: <str>

        # The TCP MSS clamping feature involves clamping the maximum segment size (MSS) in the TCP header
        # of TCP SYN packets if it exceeds the configured MSS ceiling limit for the interface.
        tcp_mss_ceiling:
          ipv4_segment_size: <int; 64-65475>
          ipv6_segment_size: <int; 64-65475>
          direction: <str; "egress" | "ingress">
        channel_group:
          id: <int>
          mode: <str; "on" | "active" | "passive">

        # ISIS instance.
        isis_enable: <str>

        # Enable BFD for ISIS.
        isis_bfd: <bool>
        isis_passive: <bool>
        isis_metric: <int>
        isis_network_point_to_point: <bool>
        isis_circuit_type: <str; "level-1-2" | "level-1" | "level-2">
        isis_hello_padding: <bool>
        isis_authentication_mode: <str; "text" | "md5">

        # Type-7 encrypted password.
        isis_authentication_key: <str>
        poe:

          # Disable PoE on a POE capable port. PoE is enabled on all ports that support it by default in EOS.
          disabled: <bool; default=False>

          # Prioritize a port's power in the event that one of the switch's power supplies loses power.
          priority: <str; "critical" | "high" | "medium" | "low">

          # Set the PoE power behavior for a PoE port when the system is rebooted.
          reboot:

            # PoE action for interface.
            action: <str; "maintain" | "power-off">

          # Set the PoE power behavior for a PoE port when the port goes down.
          link_down:

            # PoE action for interface.
            action: <str; "maintain" | "power-off">

            # Number of seconds to delay shutting the power off after a link down event occurs. Default value is 5 seconds in EOS.
            power_off_delay: <int; 1-86400>

          # Set the PoE power behavior for a PoE port when the port is admin down.
          shutdown:

            # PoE action for interface.
            action: <str; "maintain" | "power-off">

          # Override the hardware-negotiated power limit using either wattage or a power class. Note that if using a power class, AVD will automatically convert the class value to the wattage value corresponding to that power class.
          limit:
            class: <int; 0-8>
            watts: <str>

            # Set to ignore hardware classification.
            fixed: <bool>

          # Disable to prevent port from negotiating power with powered devices over LLDP. Enabled by default in EOS.
          negotiation_lldp: <bool>

          # Allow a subset of legacy devices to work with the PoE switch. Disabled by default in EOS because it can cause false positive detections.
          legacy_detect: <bool>
        ptp:
          enable: <bool>
          announce:
            interval: <int>
            timeout: <int>
          delay_req: <int>
          delay_mechanism: <str; "e2e" | "p2p">
          profile:
            g8275_1:
              destination_mac_address: <str; "forwardable" | "non-forwardable">
          sync_message:
            interval: <int>
          role: <str; "master" | "dynamic">

          # VLAN can be 'all' or list of vlans as string.
          vlan: <str>
          transport: <str; "ipv4" | "ipv6" | "layer2">

        # Interface profile.
        profile: <str>
        storm_control:
          all:

            # Configure maximum storm-control level.
            level: <str>

            # Optional field and is hardware dependent.
            unit: <str; "percent" | "pps"; default="percent">
          broadcast:

            # Configure maximum storm-control level.
            level: <str>

            # Optional field and is hardware dependent.
            unit: <str; "percent" | "pps"; default="percent">
          multicast:

            # Configure maximum storm-control level.
            level: <str>

            # Optional field and is hardware dependent.
            unit: <str; "percent" | "pps"; default="percent">
          unknown_unicast:

            # Configure maximum storm-control level.
            level: <str>

            # Optional field and is hardware dependent.
            unit: <str; "percent" | "pps"; default="percent">
        logging:
          event:
            link_status: <bool>
            congestion_drops: <bool>
            spanning_tree: <bool>

            # Discards due to storm-control.
            storm_control_discards: <bool>
        lldp:
          transmit: <bool>
          receive: <bool>

          # ZTP vlan number.
          ztp_vlan: <int>
        # This key is deprecated.
        # Support will be removed in AVD version 6.0.0.
        # Use <samp>switchport.trunk.private_vlan_secondary</samp> instead.
        trunk_private_vlan_secondary: <bool>

        # List of vlans as string.
        # This key is deprecated.
        # Support will be removed in AVD version 6.0.0.
        # Use <samp>switchport.pvlan_mapping</samp> instead.
        pvlan_mapping: <str>
        # This key is deprecated.
        # Support will be removed in AVD version 6.0.0.
        # Use <samp>switchport.vlan_translations</samp> instead.
        vlan_translations:

            # List of vlans as string (only one vlan if direction is "both").
          - from: <str>

            # VLAN ID.
            to: <int>
            direction: <str; "in" | "out" | "both"; default="both">

        # 802.1x
        dot1x:
          port_control: <str; "auto" | "force-authorized" | "force-unauthorized">
          port_control_force_authorized_phone: <bool>
          reauthentication: <bool>
          pae:
            mode: <str; "authenticator">
          authentication_failure:
            action: <str; "allow" | "drop">
            allow_vlan: <int; 1-4094>
          host_mode:
            mode: <str; "multi-host" | "single-host">
            multi_host_authenticated: <bool>
          mac_based_authentication:
            enabled: <bool>
            always: <bool>
            host_mode_common: <bool>

          # Operate interface in per-mac access-list mode.
          mac_based_access_list: <bool>
          timeout:
            idle_host: <int; 10-65535>
            quiet_period: <int; 1-65535>

            # Value can be 60-4294967295 or 'server'.
            reauth_period: <str>
            reauth_timeout_ignore: <bool>
            tx_period: <int; 1-65535>
          reauthorization_request_limit: <int; 1-10>
          unauthorized:
            access_vlan_membership_egress: <bool>
            native_vlan_membership_egress: <bool>
          eapol:
            disabled: <bool>
            authentication_failure_fallback_mba:
              enabled: <bool>
              timeout: <int; 0-65535>
          aaa:

            # Configure AAA timeout options.
            unresponsive:

              # EAP response to send. EOS default is `success`.
              eap_response: <str; "success" | "disabled">

              # Set action for supplicant when AAA times out.
              action:

                # Name of standard access-list to apply when AAA times out.
                traffic_allow_access_list: <str>

                # Use results from a previous AAA response.
                apply_cached_results: <bool>
                cached_results_timeout:

                  # Enable caching for a specific duration -
                  # <1-10000>      duration in days
                  # <1-14400000>   duration in minutes
                  # <1-240000>     duration in hours
                  # <1-864000000>  duration in seconds
                  time_duration: <int; >=1>
                  time_duration_unit: <str; "days" | "hours" | "minutes" | "seconds"; required>

                # Apply alternate action if primary action fails.
                # eg. aaa unresponsive action apply cached-results else traffic allow
                apply_alternate: <bool>

                # Set action for supplicant traffic when AAA times out.
                traffic_allow: <bool>
                traffic_allow_vlan: <int; 1-4094>

              # Set action for supplicant when AAA times out.
              phone_action:

                # Use results from a previous AAA response.
                apply_cached_results: <bool>
                cached_results_timeout:

                  # Enable caching for a specific duration -
                  # <1-10000>      duration in days
                  # <1-14400000>   duration in minutes
                  # <1-240000>     duration in hours
                  # <1-864000000>  duration in seconds
                  time_duration: <int; >=1>
                  time_duration_unit: <str; "days" | "hours" | "minutes" | "seconds"; required>

                # Apply alternate action if primary action fails.
                # eg. aaa unresponsive phone action apply cached-results else traffic allow
                apply_alternate: <bool>

                # Set action for supplicant traffic when AAA times out.
                traffic_allow: <bool>

        # QOS profile.
        service_profile: <str>
        shape:

          # Rate in kbps, pps or percent.
          # Supported options are platform dependent.
          # Examples:
          # - "5000 kbps"
          # - "1000 pps"
          # - "20 percent"
          rate: <str>
        qos:
          trust: <str; "dscp" | "cos" | "disabled">

          # DSCP value.
          dscp: <int>

          # COS value.
          cos: <int>
        spanning_tree_bpdufilter: <str; "enabled" | "disabled" | "True" | "False" | "true" | "false">
        spanning_tree_bpduguard: <str; "enabled" | "disabled" | "True" | "False" | "true" | "false">
        spanning_tree_guard: <str; "loop" | "root" | "disabled">
        spanning_tree_portfast: <str; "edge" | "network">
        vmtracer: <bool>
        priority_flow_control:
          enabled: <bool>
          priorities:
            - priority: <int; 0-7; required; unique>
              no_drop: <bool>
        bfd:
          echo: <bool>

          # Interval in milliseconds.
          interval: <int>

          # Rate in milliseconds.
          min_rx: <int>
          multiplier: <int; 3-50>
        service_policy:
          pbr:

            # Policy Based Routing Policy-map name.
            input: <str>
          qos:

            # Quality of Service Policy-map name.
            input: <str; required>
        mpls:
          ip: <bool>
          ldp:
            interface: <bool>
            igp_sync: <bool>
        lacp_timer:
          mode: <str; "fast" | "normal">
          multiplier: <int; 3-3000>
        lacp_port_priority: <int; 0-65535>
        transceiver:

          # Transceiver Laser Frequency in GHz (min 190000, max 200000).
          frequency: <str>

          # Unit of Transceiver Laser Frequency.
          frequency_unit: <str; "ghz">
          media:

            # Transceiver type.
            override: <str>
        ip_proxy_arp: <bool>
        traffic_policy:

          # Ingress traffic policy.
          input: <str>

          # Egress traffic policy.
          output: <str>
        bgp:

          # Name of session tracker.
          session_tracker: <str>
        ip_igmp_host_proxy:
          enabled: <bool>
          groups:

              # Multicast Address.
            - group: <str; required; unique>

              # The same source must not be present both in `exclude` and `include` list.
              exclude:
                - source: <str; required; unique>

              # The same source must not be present both in `exclude` and `include` list.
              include:
                - source: <str; required; unique>

          # Time interval between unsolicited reports.
          report_interval: <int; 1-31744>

          # Non-standard Access List name.
          access_lists:
            - name: <str; required; unique>

          # IGMP version on IGMP host-proxy interface.
          version: <int; 1-3>

        # Key only used for documentation or validation purposes.
        peer: <str>

        # Key only used for documentation or validation purposes.
        peer_interface: <str>

        # Key only used for documentation or validation purposes.
        peer_type: <str>
        sflow:
          enable: <bool>
          egress:
            enable: <bool>
            unmodified_enable: <bool>
        sync_e:
          enable: <bool>

          # The priority is used to influence the reference clock selection. The EOS default priority is 127. The priority can be configured to any integer between 1-255, or set to `disabled`.
          priority: <str>

        # Key only used for documentation or validation purposes.
        port_profile: <str>
        uc_tx_queues:

            # TX-Queue ID.
          - id: <int; required; unique>
            random_detect:

              # Explicit Congestion Notification.
              ecn:

                # Enable counter for random-detect ECNs.
                count: <bool>
                threshold:

                  # Indicate the units to be used for the threshold values.
                  units: <str; "segments" | "bytes" | "kbytes" | "mbytes" | "milliseconds"; required>

                  # Set the random-detect ECN minimum-threshold.
                  min: <int; 1-256000000; required>

                  # Set the random-detect ECN maximum-threshold.
                  max: <int; 1-256000000; required>

                  # Set the random-detect ECN max-mark-probability.
                  max_probability: <int; 1-100>

                  # Set the random-detect ECN weight.
                  weight: <int; 0-15>
        tx_queues:

            # TX-Queue ID.
          - id: <int; required; unique>
            random_detect:

              # Explicit Congestion Notification.
              ecn:

                # Enable counter for random-detect ECNs.
                count: <bool>
                threshold:

                  # Indicate the units to be used for the threshold values.
                  units: <str; "segments" | "bytes" | "kbytes" | "mbytes" | "milliseconds"; required>

                  # Set the random-detect ECN minimum-threshold.
                  min: <int; 1-256000000>

                  # Set the random-detect ECN maximum-threshold.
                  max: <int; 1-256000000; required>

                  # Set the random-detect ECN max-mark-probability.
                  max_probability: <int; 1-100; required>

                  # Set the random-detect ECN weight.
                  weight: <int; 0-15>

        # VRRP model.
        vrrp_ids:

            # VRID.
          - id: <int; required; unique>

            # Instance priority.
            priority_level: <int; 1-254>
            advertisement:

              # Interval in seconds.
              interval: <int; 1-255>
            preempt:
              enabled: <bool; required>
              delay:

                # Minimum preempt delay in seconds.
                minimum: <int; 0-3600>

                # Reload preempt delay in seconds.
                reload: <int; 0-3600>
            timers:
              delay:

                # Delay after reload in seconds.
                reload: <int; 0-3600>
            tracked_object:

                # Tracked object name.
              - name: <str; required; unique>

                # Decrement VRRP priority by 1-254.
                decrement: <int; 1-254>
                shutdown: <bool>
            ipv4:

              # Virtual IPv4 address.
              address: <str; required>
              version: <int; 2 | 3>
            ipv6:

              # Virtual IPv6 address.
              address: <str; required>

        # Set to false to disable interface validation by the `eos_validate_state` role.
        validate_state: <bool>

        # This should not be combined with `ethernet_interfaces[].type = switched/routed`.
        switchport:

          # Warning: This should not be combined with `ethernet_interfaces[].type = routed`.
          enabled: <bool>

          # Warning: This should not be combined with `ethernet_interfaces[].mode`.
          mode: <str; "access" | "dot1q-tunnel" | "trunk" | "trunk phone">

          # Set VLAN when interface is in access mode.
          # Warning: This should not be combined with `ethernet_interfaces[].mode = access/dot1q-tunnel` and `ethernet_interface[].vlans`.
          access_vlan: <int; 1-4094>
          trunk:

            # VLAN ID or range(s) of VLAN IDs.
            # Warning: This should not be combined with `ethernet_interfaces[].mode = trunk` and `ethernet_interface[].vlans`.
            allowed_vlan: <str>

            # Set native VLAN when interface is in trunking mode.
            # Warning: This should not be combined with `ethernet_interfaces[].native_vlan`.
            native_vlan: <int; 1-4094>

            # If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence.
            # Warning: This should not be combined with `ethernet_interfaces[].native_vlan_tag`.
            native_vlan_tag: <bool>

            # Enable secondary VLAN mapping for a private vlan.
            # Warning: This should not be combined with `ethernet_ineterfaces[].trunk_private_vlan_secondary`.
            private_vlan_secondary: <bool>

            # Warning: This should not be combined with `ethernet_ineterfaces[].trunk_groups`.
            groups:

                # Trunk group name.
              - <str>

          # Warning: This should not be combined with `ethernet_interfaces[].phone`.
          phone:

            # Warning: This should not be combined with `ethernet_interfaces[].phone.vlan`.
            vlan: <int; 1-4094>

            # Warning: This should not be combined with `ethernet_interfaces[].phone.trunk`.
            trunk: <str; "tagged" | "tagged phone" | "untagged" | "untagged phone">

          # Secondary VLAN IDs of the private VLAN mapping.
          # Warning: This should not be combined with `ethernet_interfaces[].pvlan_mapping`.
          pvlan_mapping: <str>
          dot1q:

            # Ethertype/TPID (Tag Protocol IDentifier) for VLAN tagged frames.
            ethertype: <int; 1536-65535>

            # Allow/disallow VLAN tagged frames.
            vlan_tag: <str; "disallowed" | "required">

          # tx: Allow bridged traffic to go out of the source interface.
          # tx multicast: Allow multicast traffic only to go out of the source interface.
          source_interface: <str; "tx" | "tx multicast">

          # VLAN Translation mappings.
          # Warning: This should not be combined with `ethernet_interfaces[].vlan_translations`.
          vlan_translations:

            # Drop the ingress traffic that do not match any VLAN mapping.
            in_required: <bool>

            # Drop the egress traffic that do not match any VLAN mapping.
            out_required: <bool>

            # Map ingress traffic only.
            direction_in:

                # VLAN ID or range of VLAN IDs to map from. Range 1-4094.
              - from: <str; required>

                # VLAN ID to map to.
                to: <int; 1-4094; required>
                dot1q_tunnel: <bool>

                # Inner VLAN ID to map from.
                inner_vlan_from: <int; 1-4094>

            # Map egress traffic only.
            direction_out:

                # VLAN ID or range of VLAN IDs to map from. Range 1-4094.
              - from: <str; required>

                # VLAN ID to map to.
                to: <int; 1-4094>

                # VLAN ID or range of VLAN IDs or "all". Range 1-4094.
                # This takes precedence over `to` and `inner_vlan_to`.
                dot1q_tunnel_to: <str>

                # Inner VLAN ID to map to.
                inner_vlan_to: <int; 1-4094>

            # Map both egress and ingress traffic.
            direction_both:

                # VLAN ID or range of VLAN IDs to map from. Range 1-4094.
              - from: <str; required>

                # VLAN ID to map to.
                to: <int; 1-4094; required>
                dot1q_tunnel: <bool>

                # Inner VLAN ID to map from.
                inner_vlan_from: <int; 1-4094>

                # Enable use of network-side VLAN ID.
                # This setting can only be enabled when `inner_vlan_from` is defined.
                network: <bool>
          vlan_forwarding_accept_all: <bool>
          backup_link:

            # Backup interface. Example - Ethernet4, Vlan10 etc.
            interface: <str>

            # VLANs to carry on the backup interface (1-4094).
            prefer_vlan: <str>

          # The `backup_link` is required for this setting.
          backup:

            # Destination MAC address for MAC move updates.
            # The mac address should be multicast or broadcast.
            # Example: 01:00:00:00:00:00
            dest_macaddr: <str>

            # Initial MAC move delay in milliseconds.
            initial_mac_move_delay: <int; 0-65535>

            # Size of MAC move bursts.
            mac_move_burst: <int; 0-65535>

            # MAC move burst interval in milliseconds.
            mac_move_burst_interval: <int; 0-65535>

            # Preemption delay in milliseconds.
            preemption_delay: <int; 0-65535>
          port_security:
            enabled: <bool>

            # Maximum number of MAC addresses allowed on the interface.
            mac_address_maximum:

              # Disable port level check for port security (only in violation 'shutdown' mode).
              disabled: <bool>

              # MAC address limit.
              limit: <int; 1-1000>

            # Configure violation mode (shutdown or protect), EOS default is 'shutdown'.
            violation:

              # Configure port security mode.
              mode: <str; "shutdown" | "protect">

              # Log new addresses seen after limit is reached in protect mode.
              protect_log: <bool>

            # Default maximum MAC addresses for all VLANs on this interface.
            vlan_default_mac_address_maximum: <int; 0-1000>
            vlans:

                # VLAN ID or range(s) of VLAN IDs, <1-4094>.
                # Example:
                #   - 3
                #   - 1,3
                #   - 1-10
              - range: <str; required; unique>
                mac_address_maximum: <int; required>

        # Multiline EOS CLI rendered directly on the ethernet interface in the final EOS configuration.
        eos_cli: <str>
    ```
