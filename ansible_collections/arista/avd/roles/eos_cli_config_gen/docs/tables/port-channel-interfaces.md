<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>port_channel_interfaces</samp>](## "port_channel_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "port_channel_interfaces.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "port_channel_interfaces.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "port_channel_interfaces.[].profile") | String |  |  |  | Interface profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "port_channel_interfaces.[].logging") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;event</samp>](## "port_channel_interfaces.[].logging.event") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_status</samp>](## "port_channel_interfaces.[].logging.event.link_status") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;storm_control_discards</samp>](## "port_channel_interfaces.[].logging.event.storm_control_discards") | Boolean |  |  |  | Discards due to storm-control.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "port_channel_interfaces.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2_mtu</samp>](## "port_channel_interfaces.[].l2_mtu") | Integer |  |  | Min: 68<br>Max: 65535 | "l2_mtu" should only be defined for platforms supporting the "l2 mtu" CLI.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2_mru</samp>](## "port_channel_interfaces.[].l2_mru") | Integer |  |  | Min: 68<br>Max: 65535 | "l2_mru" should only be defined for platforms supporting the "l2 mru" CLI.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlans</samp>](## "port_channel_interfaces.[].vlans") <span style="color:red">deprecated</span> | String |  |  |  | List of switchport vlans as string.<br>For a trunk port this would be a range like "1-200,300".<br>For an access port this would be a single vlan "123".<br><span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>switchport.access_vlan or switchport.trunk.allowed_vlan</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;snmp_trap_link_change</samp>](## "port_channel_interfaces.[].snmp_trap_link_change") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "port_channel_interfaces.[].type") <span style="color:red">deprecated</span> | String |  |  | Valid Values:<br>- <code>routed</code><br>- <code>switched</code><br>- <code>l3dot1q</code><br>- <code>l2dot1q</code> | l3dot1q and l2dot1q are used for sub-interfaces. The parent interface should be defined as routed.<br>Interface will not be listed in device documentation, unless "type" is set.<br><span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. See [here](https://avd.arista.com/5.x/docs/porting-guides/5.x.x.html#removal-of-type-key-dependency-for-rendering-ethernetport-channel-interfaces-configuration-and-documentation) for details.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "port_channel_interfaces.[].encapsulation_dot1q_vlan") <span style="color:red">deprecated</span> | Integer |  |  |  | VLAN tag to configure on sub-interface.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>encapsulation_dot1q.vlan</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q</samp>](## "port_channel_interfaces.[].encapsulation_dot1q") | Dictionary |  |  |  | Warning: `encapsulation_dot1q` should not be combined with `ethernet_interfaces[].type: l3dot1q` or `ethernet_interfaces[].type: l2dot1q`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "port_channel_interfaces.[].encapsulation_dot1q.vlan") | Integer | Required |  | Min: 1<br>Max: 4094 | VLAD ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner_vlan</samp>](## "port_channel_interfaces.[].encapsulation_dot1q.inner_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Inner VLAN ID. This setting can only be applied to sub-interfaces on EOS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "port_channel_interfaces.[].vrf") | String |  |  |  | VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_vlan</samp>](## "port_channel_interfaces.[].encapsulation_vlan") | Dictionary |  |  |  | This setting can only be applied to sub-interfaces on EOS.<br>Warning: `encapsulation_vlan` should not be combined with `ethernet_interfaces[].type: l3dot1q` or `ethernet_interfaces[].type: l2dot1q`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;client</samp>](## "port_channel_interfaces.[].encapsulation_vlan.client") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1q</samp>](## "port_channel_interfaces.[].encapsulation_vlan.client.dot1q") <span style="color:red">deprecated</span> | Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "port_channel_interfaces.[].encapsulation_vlan.client.dot1q.vlan") | Integer |  |  |  | Client VLAN ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;outer</samp>](## "port_channel_interfaces.[].encapsulation_vlan.client.dot1q.outer") | Integer |  |  | Min: 1<br>Max: 4094 | Client Outer VLAN ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner</samp>](## "port_channel_interfaces.[].encapsulation_vlan.client.dot1q.inner") | Integer |  |  | Min: 1<br>Max: 4094 | Client Inner VLAN ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unmatched</samp>](## "port_channel_interfaces.[].encapsulation_vlan.client.unmatched") <span style="color:red">deprecated</span> | Boolean |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation</samp>](## "port_channel_interfaces.[].encapsulation_vlan.client.encapsulation") | String |  |  | Valid Values:<br>- <code>dot1q</code><br>- <code>dot1ad</code><br>- <code>unmatched</code><br>- <code>untagged</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "port_channel_interfaces.[].encapsulation_vlan.client.vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Client VLAN ID. Not applicable for `encapsulation: untagged` or `encapsulation: unmatched`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;outer_vlan</samp>](## "port_channel_interfaces.[].encapsulation_vlan.client.outer_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Client Outer VLAN ID. Not applicable for `encapsulation: untagged` or `encapsulation: unmatched`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner_vlan</samp>](## "port_channel_interfaces.[].encapsulation_vlan.client.inner_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Client Inner VLAN ID. Not applicable for `encapsulation: untagged` or `encapsulation: unmatched`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner_encapsulation</samp>](## "port_channel_interfaces.[].encapsulation_vlan.client.inner_encapsulation") | String |  |  | Valid Values:<br>- <code>dot1q</code><br>- <code>dot1ad</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;network</samp>](## "port_channel_interfaces.[].encapsulation_vlan.network") | Dictionary |  |  |  | Network encapsulation are all optional, and skipped if using client unmatched. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1q</samp>](## "port_channel_interfaces.[].encapsulation_vlan.network.dot1q") <span style="color:red">deprecated</span> | Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "port_channel_interfaces.[].encapsulation_vlan.network.dot1q.vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Network VLAN ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;outer</samp>](## "port_channel_interfaces.[].encapsulation_vlan.network.dot1q.outer") | Integer |  |  | Min: 1<br>Max: 4094 | Network Outer VLAN ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner</samp>](## "port_channel_interfaces.[].encapsulation_vlan.network.dot1q.inner") | Integer |  |  | Min: 1<br>Max: 4094 | Network Inner VLAN ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;client</samp>](## "port_channel_interfaces.[].encapsulation_vlan.network.client") <span style="color:red">deprecated</span> | Boolean |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation</samp>](## "port_channel_interfaces.[].encapsulation_vlan.network.encapsulation") | String |  |  | Valid Values:<br>- <code>dot1q</code><br>- <code>dot1ad</code><br>- <code>client</code><br>- <code>client inner</code><br>- <code>untagged</code> | `untagged` (no encapsulation) is applicable for `untagged` client only.<br>`client` and `client inner` (retain client encapsulation) is not applicable for `untagged` client. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "port_channel_interfaces.[].encapsulation_vlan.network.vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Network VLAN ID. Not applicable for `encapsulation: untagged` or `encapsulation: client`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;outer_vlan</samp>](## "port_channel_interfaces.[].encapsulation_vlan.network.outer_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Network outer VLAN ID. Not applicable for `encapsulation: untagged` or `encapsulation: client`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner_vlan</samp>](## "port_channel_interfaces.[].encapsulation_vlan.network.inner_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Network inner VLAN ID. Not applicable for `encapsulation: untagged` or `encapsulation: client`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner_encapsulation</samp>](## "port_channel_interfaces.[].encapsulation_vlan.network.inner_encapsulation") | String |  |  | Valid Values:<br>- <code>dot1q</code><br>- <code>dot1ad</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlan_id</samp>](## "port_channel_interfaces.[].vlan_id") | Integer |  |  | Min: 1<br>Max: 4094 | This setting can only be applied to sub-interfaces on EOS.<br>Warning: `vlan_id` should not be combined with `ethernet_interfaces[].type == l2dot1q`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "port_channel_interfaces.[].mode") <span style="color:red">deprecated</span> | String |  |  | Valid Values:<br>- <code>access</code><br>- <code>dot1q-tunnel</code><br>- <code>trunk</code><br>- <code>trunk phone</code> | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>switchport.mode</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;native_vlan</samp>](## "port_channel_interfaces.[].native_vlan") <span style="color:red">deprecated</span> | Integer |  |  |  | If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>switchport.trunk.native_vlan</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;native_vlan_tag</samp>](## "port_channel_interfaces.[].native_vlan_tag") <span style="color:red">deprecated</span> | Boolean |  |  |  | If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>switchport.trunk.native_vlan_tag</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;link_tracking_groups</samp>](## "port_channel_interfaces.[].link_tracking_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "port_channel_interfaces.[].link_tracking_groups.[].name") | String | Required, Unique |  |  | Group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "port_channel_interfaces.[].link_tracking_groups.[].direction") | String |  |  | Valid Values:<br>- <code>upstream</code><br>- <code>downstream</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;link_tracking</samp>](## "port_channel_interfaces.[].link_tracking") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "port_channel_interfaces.[].link_tracking.direction") | String |  |  | Valid Values:<br>- <code>upstream</code><br>- <code>downstream</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "port_channel_interfaces.[].link_tracking.groups") | List, items: String |  |  |  | Link state group(s) an interface belongs to. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "port_channel_interfaces.[].link_tracking.groups.[]") | String |  |  |  | Group names. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;phone</samp>](## "port_channel_interfaces.[].phone") <span style="color:red">deprecated</span> | Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>switchport.phone</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk</samp>](## "port_channel_interfaces.[].phone.trunk") | String |  |  | Valid Values:<br>- <code>tagged</code><br>- <code>untagged</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "port_channel_interfaces.[].phone.vlan") | Integer |  |  | Min: 1<br>Max: 4094 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2_protocol</samp>](## "port_channel_interfaces.[].l2_protocol") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "port_channel_interfaces.[].l2_protocol.encapsulation_dot1q_vlan") | Integer |  |  |  | Vlan tag to configure on sub-interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forwarding_profile</samp>](## "port_channel_interfaces.[].l2_protocol.forwarding_profile") | String |  |  |  | L2 protocol forwarding profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "port_channel_interfaces.[].mtu") | Integer |  |  | Min: 68<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag</samp>](## "port_channel_interfaces.[].mlag") | Integer |  |  | Min: 1<br>Max: 2000 | MLAG ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "port_channel_interfaces.[].trunk_groups") <span style="color:red">deprecated</span> | List, items: String |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>switchport.trunk.groups</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "port_channel_interfaces.[].trunk_groups.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lacp_fallback_timeout</samp>](## "port_channel_interfaces.[].lacp_fallback_timeout") | Integer |  |  | Min: 0<br>Max: 300 | Timeout in seconds. EOS default is 90 seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;min_links</samp>](## "port_channel_interfaces.[].min_links") | Integer |  |  | Min: 0<br>Max: 120 | Minimum number of ports required up before bringing up a port-channel.<br>Maximum in `min_links` is hardware dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lacp_fallback_mode</samp>](## "port_channel_interfaces.[].lacp_fallback_mode") | String |  |  | Valid Values:<br>- <code>individual</code><br>- <code>static</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;qos</samp>](## "port_channel_interfaces.[].qos") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trust</samp>](## "port_channel_interfaces.[].qos.trust") | String |  |  | Valid Values:<br>- <code>dscp</code><br>- <code>cos</code><br>- <code>disabled</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "port_channel_interfaces.[].qos.dscp") | Integer |  |  |  | DSCP value. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cos</samp>](## "port_channel_interfaces.[].qos.cos") | Integer |  |  |  | COS value. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "port_channel_interfaces.[].bfd") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;echo</samp>](## "port_channel_interfaces.[].bfd.echo") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "port_channel_interfaces.[].bfd.interval") | Integer |  |  |  | Interval in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp>](## "port_channel_interfaces.[].bfd.min_rx") | Integer |  |  |  | Rate in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "port_channel_interfaces.[].bfd.multiplier") | Integer |  |  | Min: 3<br>Max: 50 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;neighbor</samp>](## "port_channel_interfaces.[].bfd.neighbor") | String |  |  |  | IPv4 or IPv6 address. When the Port-channel is a L2 interface, a local L3 BFD address (router_bfd.local_address) has to be defined globally on the switch. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;per_link</samp>](## "port_channel_interfaces.[].bfd.per_link") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "port_channel_interfaces.[].bfd.per_link.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rfc_7130</samp>](## "port_channel_interfaces.[].bfd.per_link.rfc_7130") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;service_policy</samp>](## "port_channel_interfaces.[].service_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pbr</samp>](## "port_channel_interfaces.[].service_policy.pbr") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input</samp>](## "port_channel_interfaces.[].service_policy.pbr.input") | String |  |  |  | Policy Based Routing Policy-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos</samp>](## "port_channel_interfaces.[].service_policy.qos") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input</samp>](## "port_channel_interfaces.[].service_policy.qos.input") | String | Required |  |  | Quality of Service Policy-map name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp>](## "port_channel_interfaces.[].mpls") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "port_channel_interfaces.[].mpls.ip") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ldp</samp>](## "port_channel_interfaces.[].mpls.ldp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "port_channel_interfaces.[].mpls.ldp.interface") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igp_sync</samp>](## "port_channel_interfaces.[].mpls.ldp.igp_sync") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_private_vlan_secondary</samp>](## "port_channel_interfaces.[].trunk_private_vlan_secondary") <span style="color:red">deprecated</span> | Boolean |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>switchport.trunk.private_vlan_secondary</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pvlan_mapping</samp>](## "port_channel_interfaces.[].pvlan_mapping") <span style="color:red">deprecated</span> | String |  |  |  | List of vlans as string.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>switchport.pvlan_mapping</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlan_translations</samp>](## "port_channel_interfaces.[].vlan_translations") <span style="color:red">deprecated</span> | List, items: Dictionary |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>switchport.vlan_translations</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;from</samp>](## "port_channel_interfaces.[].vlan_translations.[].from") | String |  |  |  | List of vlans as string (only one vlan if direction is "both"). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to</samp>](## "port_channel_interfaces.[].vlan_translations.[].to") | Integer |  |  |  | VLAN ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "port_channel_interfaces.[].vlan_translations.[].direction") | String |  | `both` | Valid Values:<br>- <code>in</code><br>- <code>out</code><br>- <code>both</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shape</samp>](## "port_channel_interfaces.[].shape") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate</samp>](## "port_channel_interfaces.[].shape.rate") | String |  |  |  | Rate in kbps, pps or percent.<br>Supported options are platform dependent.<br>Examples:<br>- "5000 kbps"<br>- "1000 pps"<br>- "20 percent"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;storm_control</samp>](## "port_channel_interfaces.[].storm_control") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;all</samp>](## "port_channel_interfaces.[].storm_control.all") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "port_channel_interfaces.[].storm_control.all.level") | String |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "port_channel_interfaces.[].storm_control.all.unit") | String |  | `percent` | Valid Values:<br>- <code>percent</code><br>- <code>pps</code> | Optional field and is hardware dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;broadcast</samp>](## "port_channel_interfaces.[].storm_control.broadcast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "port_channel_interfaces.[].storm_control.broadcast.level") | String |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "port_channel_interfaces.[].storm_control.broadcast.unit") | String |  | `percent` | Valid Values:<br>- <code>percent</code><br>- <code>pps</code> | Optional field and is hardware dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp>](## "port_channel_interfaces.[].storm_control.multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "port_channel_interfaces.[].storm_control.multicast.level") | String |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "port_channel_interfaces.[].storm_control.multicast.unit") | String |  | `percent` | Valid Values:<br>- <code>percent</code><br>- <code>pps</code> | Optional field and is hardware dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unknown_unicast</samp>](## "port_channel_interfaces.[].storm_control.unknown_unicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level</samp>](## "port_channel_interfaces.[].storm_control.unknown_unicast.level") | String |  |  |  | Configure maximum storm-control level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unit</samp>](## "port_channel_interfaces.[].storm_control.unknown_unicast.unit") | String |  | `percent` | Valid Values:<br>- <code>percent</code><br>- <code>pps</code> | Optional field and is hardware dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_proxy_arp</samp>](## "port_channel_interfaces.[].ip_proxy_arp") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_enable</samp>](## "port_channel_interfaces.[].isis_enable") | String |  |  |  | ISIS instance. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_bfd</samp>](## "port_channel_interfaces.[].isis_bfd") | Boolean |  |  |  | Enable BFD for ISIS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_passive</samp>](## "port_channel_interfaces.[].isis_passive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp>](## "port_channel_interfaces.[].isis_metric") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_network_point_to_point</samp>](## "port_channel_interfaces.[].isis_network_point_to_point") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_circuit_type</samp>](## "port_channel_interfaces.[].isis_circuit_type") | String |  |  | Valid Values:<br>- <code>level-1-2</code><br>- <code>level-1</code><br>- <code>level-2</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_hello_padding</samp>](## "port_channel_interfaces.[].isis_hello_padding") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_mode</samp>](## "port_channel_interfaces.[].isis_authentication_mode") <span style="color:red">deprecated</span> | String |  |  | Valid Values:<br>- <code>text</code><br>- <code>md5</code> | <span style="color:red">This key is deprecated. Support will be removed in AVD version v6.0.0. Use <samp>port_channel_interfaces[].isis_authentication.both.mode or port_channel_interfaces[].isis_authentication.level_1.mode or port_channel_interfaces[].isis_authentication.level_2.mode</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication_key</samp>](## "port_channel_interfaces.[].isis_authentication_key") <span style="color:red">deprecated</span> | String |  |  |  | Type-7 encrypted password.<span style="color:red">This key is deprecated. Support will be removed in AVD version v6.0.0. Use <samp>port_channel_interfaces[].isis_authentication.both.key or port_channel_interfaces[].isis_authentication.level_1.key or port_channel_interfaces[].isis_authentication.level_2.key</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication</samp>](## "port_channel_interfaces.[].isis_authentication") | Dictionary |  |  |  | This key should not be mixed with port_channel_interfaces[].isis_authentication_mode or ethernet_interfaces[].isis_authentication_key. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;both</samp>](## "port_channel_interfaces.[].isis_authentication.both") | Dictionary |  |  |  | Authentication settings for level-1 and level-2. 'both' takes precedence over 'level_1' and 'level_2' settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "port_channel_interfaces.[].isis_authentication.both.key_type") | String |  |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Configure authentication key type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "port_channel_interfaces.[].isis_authentication.both.key") | String |  |  |  | Password string. `key_type` is required for this setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_ids</samp>](## "port_channel_interfaces.[].isis_authentication.both.key_ids") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "port_channel_interfaces.[].isis_authentication.both.key_ids.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 65535 | Configure authentication key-id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "port_channel_interfaces.[].isis_authentication.both.key_ids.[].algorithm") | String | Required |  | Valid Values:<br>- <code>sha-1</code><br>- <code>sha-224</code><br>- <code>sha-256</code><br>- <code>sha-384</code><br>- <code>sha-512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "port_channel_interfaces.[].isis_authentication.both.key_ids.[].key_type") | String | Required |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Configure authentication key type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "port_channel_interfaces.[].isis_authentication.both.key_ids.[].key") | String | Required |  |  | Password string. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rfc_5310</samp>](## "port_channel_interfaces.[].isis_authentication.both.key_ids.[].rfc_5310") | Boolean |  |  |  | SHA digest computation according to rfc5310. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "port_channel_interfaces.[].isis_authentication.both.mode") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>sha</code><br>- <code>text</code><br>- <code>shared-secret</code> | Authentication mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sha</samp>](## "port_channel_interfaces.[].isis_authentication.both.sha") | Dictionary |  |  |  | Required settings for authentication mode 'sha'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_id</samp>](## "port_channel_interfaces.[].isis_authentication.both.sha.key_id") | Integer | Required |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shared_secret</samp>](## "port_channel_interfaces.[].isis_authentication.both.shared_secret") | Dictionary |  |  |  | Required settings for authentication mode 'shared_secret'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "port_channel_interfaces.[].isis_authentication.both.shared_secret.profile") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "port_channel_interfaces.[].isis_authentication.both.shared_secret.algorithm") | String | Required |  | Valid Values:<br>- <code>md5</code><br>- <code>sha-1</code><br>- <code>sha-224</code><br>- <code>sha-256</code><br>- <code>sha-384</code><br>- <code>sha-512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rx_disabled</samp>](## "port_channel_interfaces.[].isis_authentication.both.rx_disabled") | Boolean |  |  |  | Disable authentication check on the receive side. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level_1</samp>](## "port_channel_interfaces.[].isis_authentication.level_1") | Dictionary |  |  |  | Authentication settings for level-1. 'both' takes precedence over 'level_1' and 'level_2' settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "port_channel_interfaces.[].isis_authentication.level_1.key_type") | String |  |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Configure authentication key type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "port_channel_interfaces.[].isis_authentication.level_1.key") | String |  |  |  | Password string. `key_type` is required for this setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_ids</samp>](## "port_channel_interfaces.[].isis_authentication.level_1.key_ids") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "port_channel_interfaces.[].isis_authentication.level_1.key_ids.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 65535 | Configure authentication key-id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "port_channel_interfaces.[].isis_authentication.level_1.key_ids.[].algorithm") | String | Required |  | Valid Values:<br>- <code>sha-1</code><br>- <code>sha-224</code><br>- <code>sha-256</code><br>- <code>sha-384</code><br>- <code>sha-512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "port_channel_interfaces.[].isis_authentication.level_1.key_ids.[].key_type") | String | Required |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Configure authentication key type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "port_channel_interfaces.[].isis_authentication.level_1.key_ids.[].key") | String | Required |  |  | Password string. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rfc_5310</samp>](## "port_channel_interfaces.[].isis_authentication.level_1.key_ids.[].rfc_5310") | Boolean |  |  |  | SHA digest computation according to rfc5310. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "port_channel_interfaces.[].isis_authentication.level_1.mode") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>sha</code><br>- <code>text</code><br>- <code>shared-secret</code> | Authentication mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sha</samp>](## "port_channel_interfaces.[].isis_authentication.level_1.sha") | Dictionary |  |  |  | Required settings for authentication mode 'sha'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_id</samp>](## "port_channel_interfaces.[].isis_authentication.level_1.sha.key_id") | Integer | Required |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shared_secret</samp>](## "port_channel_interfaces.[].isis_authentication.level_1.shared_secret") | Dictionary |  |  |  | Required settings for authentication mode 'shared_secret'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "port_channel_interfaces.[].isis_authentication.level_1.shared_secret.profile") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "port_channel_interfaces.[].isis_authentication.level_1.shared_secret.algorithm") | String | Required |  | Valid Values:<br>- <code>md5</code><br>- <code>sha-1</code><br>- <code>sha-224</code><br>- <code>sha-256</code><br>- <code>sha-384</code><br>- <code>sha-512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rx_disabled</samp>](## "port_channel_interfaces.[].isis_authentication.level_1.rx_disabled") | Boolean |  |  |  | Disable authentication check on the receive side. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level_2</samp>](## "port_channel_interfaces.[].isis_authentication.level_2") | Dictionary |  |  |  | Authentication settings for level-2. 'both' takes precedence over 'level_1' and 'level_2' settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "port_channel_interfaces.[].isis_authentication.level_2.key_type") | String |  |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Configure authentication key type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "port_channel_interfaces.[].isis_authentication.level_2.key") | String |  |  |  | Password string. `key_type` is required for this setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_ids</samp>](## "port_channel_interfaces.[].isis_authentication.level_2.key_ids") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "port_channel_interfaces.[].isis_authentication.level_2.key_ids.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 65535 | Configure authentication key-id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "port_channel_interfaces.[].isis_authentication.level_2.key_ids.[].algorithm") | String | Required |  | Valid Values:<br>- <code>sha-1</code><br>- <code>sha-224</code><br>- <code>sha-256</code><br>- <code>sha-384</code><br>- <code>sha-512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "port_channel_interfaces.[].isis_authentication.level_2.key_ids.[].key_type") | String | Required |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Configure authentication key type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "port_channel_interfaces.[].isis_authentication.level_2.key_ids.[].key") | String | Required |  |  | Password string. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rfc_5310</samp>](## "port_channel_interfaces.[].isis_authentication.level_2.key_ids.[].rfc_5310") | Boolean |  |  |  | SHA digest computation according to rfc5310. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "port_channel_interfaces.[].isis_authentication.level_2.mode") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>sha</code><br>- <code>text</code><br>- <code>shared-secret</code> | Authentication mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sha</samp>](## "port_channel_interfaces.[].isis_authentication.level_2.sha") | Dictionary |  |  |  | Required settings for authentication mode 'sha'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_id</samp>](## "port_channel_interfaces.[].isis_authentication.level_2.sha.key_id") | Integer | Required |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shared_secret</samp>](## "port_channel_interfaces.[].isis_authentication.level_2.shared_secret") | Dictionary |  |  |  | Required settings for authentication mode 'shared_secret'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "port_channel_interfaces.[].isis_authentication.level_2.shared_secret.profile") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "port_channel_interfaces.[].isis_authentication.level_2.shared_secret.algorithm") | String | Required |  | Valid Values:<br>- <code>md5</code><br>- <code>sha-1</code><br>- <code>sha-224</code><br>- <code>sha-256</code><br>- <code>sha-384</code><br>- <code>sha-512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rx_disabled</samp>](## "port_channel_interfaces.[].isis_authentication.level_2.rx_disabled") | Boolean |  |  |  | Disable authentication check on the receive side. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;traffic_policy</samp>](## "port_channel_interfaces.[].traffic_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input</samp>](## "port_channel_interfaces.[].traffic_policy.input") | String |  |  |  | Ingress traffic policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;output</samp>](## "port_channel_interfaces.[].traffic_policy.output") | String |  |  |  | Egress traffic policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_ethernet_segment</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identifier</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.identifier") | String |  |  |  | EVPN Ethernet Segment Identifier (Type 1 format). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redundancy</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.redundancy") | String |  |  | Valid Values:<br>- <code>all-active</code><br>- <code>single-active</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;designated_forwarder_election</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.designated_forwarder_election") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.algorithm") | String |  |  | Valid Values:<br>- <code>modulus</code><br>- <code>preference</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preference_value</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.preference_value") | Integer |  |  | Min: 0<br>Max: 65535 | Preference_value is only used when "algorithm" is "preference". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dont_preempt</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.dont_preempt") | Boolean |  | `False` |  | Dont_preempt is only used when "algorithm" is "preference". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hold_time</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.hold_time") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;subsequent_hold_time</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.subsequent_hold_time") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;candidate_reachability_required</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.designated_forwarder_election.candidate_reachability_required") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.mpls") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shared_index</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.mpls.shared_index") | Integer |  |  | Min: 1<br>Max: 1024 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tunnel_flood_filter_time</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.mpls.tunnel_flood_filter_time") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "port_channel_interfaces.[].evpn_ethernet_segment.route_target") | String |  |  |  | EVPN Route Target for ESI with format xx:xx:xx:xx:xx:xx. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lacp_id</samp>](## "port_channel_interfaces.[].lacp_id") | String |  |  |  | LACP ID with format xxxx.xxxx.xxxx. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpdufilter</samp>](## "port_channel_interfaces.[].spanning_tree_bpdufilter") | String |  |  | Valid Values:<br>- <code>enabled</code><br>- <code>disabled</code><br>- <code>True</code><br>- <code>False</code><br>- <code>true</code><br>- <code>false</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_bpduguard</samp>](## "port_channel_interfaces.[].spanning_tree_bpduguard") | String |  |  | Valid Values:<br>- <code>enabled</code><br>- <code>disabled</code><br>- <code>True</code><br>- <code>False</code><br>- <code>true</code><br>- <code>false</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_guard</samp>](## "port_channel_interfaces.[].spanning_tree_guard") | String |  |  | Valid Values:<br>- <code>loop</code><br>- <code>root</code><br>- <code>disabled</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_portfast</samp>](## "port_channel_interfaces.[].spanning_tree_portfast") | String |  |  | Valid Values:<br>- <code>edge</code><br>- <code>network</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vmtracer</samp>](## "port_channel_interfaces.[].vmtracer") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ptp</samp>](## "port_channel_interfaces.[].ptp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "port_channel_interfaces.[].ptp.enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;announce</samp>](## "port_channel_interfaces.[].ptp.announce") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "port_channel_interfaces.[].ptp.announce.interval") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timeout</samp>](## "port_channel_interfaces.[].ptp.announce.timeout") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_req</samp>](## "port_channel_interfaces.[].ptp.delay_req") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay_mechanism</samp>](## "port_channel_interfaces.[].ptp.delay_mechanism") | String |  |  | Valid Values:<br>- <code>e2e</code><br>- <code>p2p</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "port_channel_interfaces.[].ptp.profile") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;g8275_1</samp>](## "port_channel_interfaces.[].ptp.profile.g8275_1") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_mac_address</samp>](## "port_channel_interfaces.[].ptp.profile.g8275_1.destination_mac_address") | String |  |  | Valid Values:<br>- <code>forwardable</code><br>- <code>non-forwardable</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sync_message</samp>](## "port_channel_interfaces.[].ptp.sync_message") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "port_channel_interfaces.[].ptp.sync_message.interval") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "port_channel_interfaces.[].ptp.role") | String |  |  | Valid Values:<br>- <code>master</code><br>- <code>dynamic</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "port_channel_interfaces.[].ptp.vlan") | String |  |  |  | VLAN can be 'all' or list of vlans as string. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transport</samp>](## "port_channel_interfaces.[].ptp.transport") | String |  |  | Valid Values:<br>- <code>ipv4</code><br>- <code>ipv6</code><br>- <code>layer2</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpass</samp>](## "port_channel_interfaces.[].ptp.mpass") | Boolean |  |  |  | When MPASS is enabled on an MLAG port-channel, MLAG peers coordinate to function as a single PTP logical device.<br>Arista PTP enabled devices always place PTP messages on the same physical link within the port-channel.<br>Hence, MPASS is needed only on MLAG port-channels connected to non-Arista devices. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "port_channel_interfaces.[].ip_address") | String |  |  |  | IPv4 address/mask or "dhcp". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dhcp_client_accept_default_route</samp>](## "port_channel_interfaces.[].dhcp_client_accept_default_route") | Boolean |  |  |  | Install default-route obtained via DHCP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_verify_unicast_source_reachable_via</samp>](## "port_channel_interfaces.[].ip_verify_unicast_source_reachable_via") | String |  |  | Valid Values:<br>- <code>any</code><br>- <code>rx</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_nat</samp>](## "port_channel_interfaces.[].ip_nat") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "port_channel_interfaces.[].ip_nat.destination") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic</samp>](## "port_channel_interfaces.[].ip_nat.destination.dynamic") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;access_list</samp>](## "port_channel_interfaces.[].ip_nat.destination.dynamic.[].access_list") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "port_channel_interfaces.[].ip_nat.destination.dynamic.[].comment") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pool_name</samp>](## "port_channel_interfaces.[].ip_nat.destination.dynamic.[].pool_name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "port_channel_interfaces.[].ip_nat.destination.dynamic.[].priority") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "port_channel_interfaces.[].ip_nat.destination.static") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;access_list</samp>](## "port_channel_interfaces.[].ip_nat.destination.static.[].access_list") | String |  |  |  | 'access_list' and 'group' are mutual exclusive. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "port_channel_interfaces.[].ip_nat.destination.static.[].comment") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "port_channel_interfaces.[].ip_nat.destination.static.[].direction") | String |  |  | Valid Values:<br>- <code>egress</code><br>- <code>ingress</code> | Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.<br>EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "port_channel_interfaces.[].ip_nat.destination.static.[].group") | Integer |  |  | Min: 1<br>Max: 65535 | 'access_list' and 'group' are mutual exclusive. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;original_ip</samp>](## "port_channel_interfaces.[].ip_nat.destination.static.[].original_ip") | String |  |  |  | IPv4 address. The combination of `original_ip` and `original_port` must be unique. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;original_port</samp>](## "port_channel_interfaces.[].ip_nat.destination.static.[].original_port") | Integer |  |  | Min: 1<br>Max: 65535 | TCP/UDP port. The combination of `original_ip` and `original_port` must be unique. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "port_channel_interfaces.[].ip_nat.destination.static.[].priority") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "port_channel_interfaces.[].ip_nat.destination.static.[].protocol") | String |  |  | Valid Values:<br>- <code>udp</code><br>- <code>tcp</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;translated_ip</samp>](## "port_channel_interfaces.[].ip_nat.destination.static.[].translated_ip") | String | Required |  |  | IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;translated_port</samp>](## "port_channel_interfaces.[].ip_nat.destination.static.[].translated_port") | Integer |  |  | Min: 1<br>Max: 65535 | requires 'original_port'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "port_channel_interfaces.[].ip_nat.source") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic</samp>](## "port_channel_interfaces.[].ip_nat.source.dynamic") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;access_list</samp>](## "port_channel_interfaces.[].ip_nat.source.dynamic.[].access_list") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "port_channel_interfaces.[].ip_nat.source.dynamic.[].comment") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nat_type</samp>](## "port_channel_interfaces.[].ip_nat.source.dynamic.[].nat_type") | String | Required |  | Valid Values:<br>- <code>overload</code><br>- <code>pool</code><br>- <code>pool-address-only</code><br>- <code>pool-full-cone</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pool_name</samp>](## "port_channel_interfaces.[].ip_nat.source.dynamic.[].pool_name") | String |  |  |  | required if 'nat_type' is pool, pool-address-only or pool-full-cone.<br>ignored if 'nat_type' is overload.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "port_channel_interfaces.[].ip_nat.source.dynamic.[].priority") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "port_channel_interfaces.[].ip_nat.source.static") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;access_list</samp>](## "port_channel_interfaces.[].ip_nat.source.static.[].access_list") | String |  |  |  | 'access_list' and 'group' are mutual exclusive. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "port_channel_interfaces.[].ip_nat.source.static.[].comment") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "port_channel_interfaces.[].ip_nat.source.static.[].direction") | String |  |  | Valid Values:<br>- <code>egress</code><br>- <code>ingress</code> | Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.<br>EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "port_channel_interfaces.[].ip_nat.source.static.[].group") | Integer |  |  | Min: 1<br>Max: 65535 | 'access_list' and 'group' are mutual exclusive. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;original_ip</samp>](## "port_channel_interfaces.[].ip_nat.source.static.[].original_ip") | String |  |  |  | IPv4 address. The combination of `original_ip` and `original_port` must be unique. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;original_port</samp>](## "port_channel_interfaces.[].ip_nat.source.static.[].original_port") | Integer |  |  | Min: 1<br>Max: 65535 | TCP/UDP port. The combination of `original_ip` and `original_port` must be unique. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "port_channel_interfaces.[].ip_nat.source.static.[].priority") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "port_channel_interfaces.[].ip_nat.source.static.[].protocol") | String |  |  | Valid Values:<br>- <code>udp</code><br>- <code>tcp</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;translated_ip</samp>](## "port_channel_interfaces.[].ip_nat.source.static.[].translated_ip") | String | Required |  |  | IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;translated_port</samp>](## "port_channel_interfaces.[].ip_nat.source.static.[].translated_port") | Integer |  |  | Min: 1<br>Max: 65535 | requires 'original_port'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "port_channel_interfaces.[].ipv6_enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "port_channel_interfaces.[].ipv6_address") | String |  |  |  | IPv6 address/mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_link_local</samp>](## "port_channel_interfaces.[].ipv6_address_link_local") | String |  |  |  | Link local IPv6 address/mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_ra_disabled</samp>](## "port_channel_interfaces.[].ipv6_nd_ra_disabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_managed_config_flag</samp>](## "port_channel_interfaces.[].ipv6_nd_managed_config_flag") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_prefixes</samp>](## "port_channel_interfaces.[].ipv6_nd_prefixes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ipv6_prefix</samp>](## "port_channel_interfaces.[].ipv6_nd_prefixes.[].ipv6_prefix") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;valid_lifetime</samp>](## "port_channel_interfaces.[].ipv6_nd_prefixes.[].valid_lifetime") | String |  |  |  | Infinite or lifetime in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preferred_lifetime</samp>](## "port_channel_interfaces.[].ipv6_nd_prefixes.[].preferred_lifetime") | String |  |  |  | Infinite or lifetime in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_autoconfig_flag</samp>](## "port_channel_interfaces.[].ipv6_nd_prefixes.[].no_autoconfig_flag") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_in</samp>](## "port_channel_interfaces.[].access_group_in") | String |  |  |  | Access list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_out</samp>](## "port_channel_interfaces.[].access_group_out") | String |  |  |  | Access list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_in</samp>](## "port_channel_interfaces.[].ipv6_access_group_in") | String |  |  |  | IPv6 access list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_out</samp>](## "port_channel_interfaces.[].ipv6_access_group_out") | String |  |  |  | IPv6 access list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_access_group_in</samp>](## "port_channel_interfaces.[].mac_access_group_in") | String |  |  |  | MAC access list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_access_group_out</samp>](## "port_channel_interfaces.[].mac_access_group_out") | String |  |  |  | MAC access list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pim</samp>](## "port_channel_interfaces.[].pim") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "port_channel_interfaces.[].pim.ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;border_router</samp>](## "port_channel_interfaces.[].pim.ipv4.border_router") | Boolean |  |  |  | Configure PIM border router. EOS default is false. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dr_priority</samp>](## "port_channel_interfaces.[].pim.ipv4.dr_priority") | Integer |  |  | Min: 0<br>Max: 429467295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sparse_mode</samp>](## "port_channel_interfaces.[].pim.ipv4.sparse_mode") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "port_channel_interfaces.[].pim.ipv4.bfd") | Boolean |  |  |  | Set the default for whether Bidirectional Forwarding Detection is enabled for PIM. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bidirectional</samp>](## "port_channel_interfaces.[].pim.ipv4.bidirectional") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hello</samp>](## "port_channel_interfaces.[].pim.ipv4.hello") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;count</samp>](## "port_channel_interfaces.[].pim.ipv4.hello.count") | String |  |  |  | Number of missed hellos after which the neighbor expires. Range <1.5-65535>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "port_channel_interfaces.[].pim.ipv4.hello.interval") | Integer |  |  | Min: 1<br>Max: 65535 | PIM hello interval in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;service_profile</samp>](## "port_channel_interfaces.[].service_profile") | String |  |  |  | QOS profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_network_point_to_point</samp>](## "port_channel_interfaces.[].ospf_network_point_to_point") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_area</samp>](## "port_channel_interfaces.[].ospf_area") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_cost</samp>](## "port_channel_interfaces.[].ospf_cost") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_authentication</samp>](## "port_channel_interfaces.[].ospf_authentication") | String |  |  | Valid Values:<br>- <code>none</code><br>- <code>simple</code><br>- <code>message-digest</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_authentication_key</samp>](## "port_channel_interfaces.[].ospf_authentication_key") | String |  |  |  | Encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_message_digest_keys</samp>](## "port_channel_interfaces.[].ospf_message_digest_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "port_channel_interfaces.[].ospf_message_digest_keys.[].id") | Integer | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "port_channel_interfaces.[].ospf_message_digest_keys.[].hash_algorithm") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>sha1</code><br>- <code>sha256</code><br>- <code>sha384</code><br>- <code>sha512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "port_channel_interfaces.[].ospf_message_digest_keys.[].key") | String |  |  |  | Encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;flow_tracker</samp>](## "port_channel_interfaces.[].flow_tracker") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sampled</samp>](## "port_channel_interfaces.[].flow_tracker.sampled") | String |  |  |  | Sampled flow tracker name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hardware</samp>](## "port_channel_interfaces.[].flow_tracker.hardware") | String |  |  |  | Hardware flow tracker name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "port_channel_interfaces.[].bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session_tracker</samp>](## "port_channel_interfaces.[].bgp.session_tracker") | String |  |  |  | Name of session tracker. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_igmp_host_proxy</samp>](## "port_channel_interfaces.[].ip_igmp_host_proxy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "port_channel_interfaces.[].ip_igmp_host_proxy.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "port_channel_interfaces.[].ip_igmp_host_proxy.groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "port_channel_interfaces.[].ip_igmp_host_proxy.groups.[].group") | String | Required, Unique |  |  | Multicast Address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exclude</samp>](## "port_channel_interfaces.[].ip_igmp_host_proxy.groups.[].exclude") | List, items: Dictionary |  |  |  | The same source must not be present both in `exclude` and `include` list. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;source</samp>](## "port_channel_interfaces.[].ip_igmp_host_proxy.groups.[].exclude.[].source") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include</samp>](## "port_channel_interfaces.[].ip_igmp_host_proxy.groups.[].include") | List, items: Dictionary |  |  |  | The same source must not be present both in `exclude` and `include` list. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;source</samp>](## "port_channel_interfaces.[].ip_igmp_host_proxy.groups.[].include.[].source") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;report_interval</samp>](## "port_channel_interfaces.[].ip_igmp_host_proxy.report_interval") | Integer |  |  | Min: 1<br>Max: 31744 | Time interval between unsolicited reports. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_lists</samp>](## "port_channel_interfaces.[].ip_igmp_host_proxy.access_lists") | List, items: Dictionary |  |  |  | Non-standard Access List name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "port_channel_interfaces.[].ip_igmp_host_proxy.access_lists.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "port_channel_interfaces.[].ip_igmp_host_proxy.version") | Integer |  |  | Min: 1<br>Max: 3 | IGMP version on IGMP host-proxy interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "port_channel_interfaces.[].peer") | String |  |  |  | Key only used for documentation or validation purposes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_interface</samp>](## "port_channel_interfaces.[].peer_interface") | String |  |  |  | Key only used for documentation or validation purposes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_type</samp>](## "port_channel_interfaces.[].peer_type") | String |  |  |  | Key only used for documentation or validation purposes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sflow</samp>](## "port_channel_interfaces.[].sflow") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "port_channel_interfaces.[].sflow.enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;egress</samp>](## "port_channel_interfaces.[].sflow.egress") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "port_channel_interfaces.[].sflow.egress.enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;unmodified_enable</samp>](## "port_channel_interfaces.[].sflow.egress.unmodified_enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;switchport</samp>](## "port_channel_interfaces.[].switchport") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "port_channel_interfaces.[].switchport.enabled") | Boolean |  |  |  | Warning: This should not be combined with `port_channel_interfaces[].type = routed`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "port_channel_interfaces.[].switchport.mode") | String |  |  | Valid Values:<br>- <code>access</code><br>- <code>dot1q-tunnel</code><br>- <code>trunk</code><br>- <code>trunk phone</code> | Warning: This should not be combined with `port_channel_interfaces[].mode` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_vlan</samp>](## "port_channel_interfaces.[].switchport.access_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Set VLAN when interface is in access mode.<br>Warning: This should not be combined with `port_channel_interfaces[].mode = access/dot1q-tunnel` and `port_channel_interface.vlans`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk</samp>](## "port_channel_interfaces.[].switchport.trunk") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allowed_vlan</samp>](## "port_channel_interfaces.[].switchport.trunk.allowed_vlan") | String |  |  |  | VLAN ID or range(s) of VLAN IDs (1-4094).<br>Warning: This should not be combined with `port_channel_interfaces[].mode = trunk` and `port_channel_interfaces[].vlans`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;native_vlan</samp>](## "port_channel_interfaces.[].switchport.trunk.native_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Set native VLAN when interface is in trunking mode.<br>Warning: This should not be combined with `port_channel_interfaces[].native_vlan`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;native_vlan_tag</samp>](## "port_channel_interfaces.[].switchport.trunk.native_vlan_tag") | Boolean |  |  |  | If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence.<br>Warning: This should not be combined with `port_channel_interfaces[].native_vlan_tag`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;private_vlan_secondary</samp>](## "port_channel_interfaces.[].switchport.trunk.private_vlan_secondary") | Boolean |  |  |  | Enable secondary VLAN mapping for a private vlan.<br>Warning: This should not be combined with `port_channel_interfaces[].trunk_private_vlan_secondary`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "port_channel_interfaces.[].switchport.trunk.groups") | List, items: String |  |  |  | Warning: This should not be combined with `port_channel_interfaces[].trunk_groups`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "port_channel_interfaces.[].switchport.trunk.groups.[]") | String |  |  |  | Trunk group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;phone</samp>](## "port_channel_interfaces.[].switchport.phone") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan</samp>](## "port_channel_interfaces.[].switchport.phone.vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Warning: This should not be combined with `port_channel_interfaces[].phone.vlan`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk</samp>](## "port_channel_interfaces.[].switchport.phone.trunk") | String |  |  | Valid Values:<br>- <code>tagged</code><br>- <code>tagged phone</code><br>- <code>untagged</code><br>- <code>untagged phone</code> | Warning: This should not be combined with `port_channel_interfaces[].phone.trunk` |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pvlan_mapping</samp>](## "port_channel_interfaces.[].switchport.pvlan_mapping") | String |  |  |  | Secondary VLAN IDs of the private VLAN mapping.<br>Warning: This should not be combined with `port_channel_interfaces[].pvlan_mapping`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1q</samp>](## "port_channel_interfaces.[].switchport.dot1q") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ethertype</samp>](## "port_channel_interfaces.[].switchport.dot1q.ethertype") | Integer |  |  | Min: 1536<br>Max: 65535 | Ethertype/TPID (Tag Protocol IDentifier) for VLAN tagged frames. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_tag</samp>](## "port_channel_interfaces.[].switchport.dot1q.vlan_tag") | String |  |  | Valid Values:<br>- <code>disallowed</code><br>- <code>required</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "port_channel_interfaces.[].switchport.source_interface") | String |  |  | Valid Values:<br>- <code>tx</code><br>- <code>tx multicast</code> | tx: Allow bridged traffic to go out of the source interface.<br>tx multicast: Allow multicast traffic only to go out of the source interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_translations</samp>](## "port_channel_interfaces.[].switchport.vlan_translations") | Dictionary |  |  |  | VLAN Translation mappings.<br>Warning: This should not be combined with `port_channel_interfaces[].vlan_translations`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;in_required</samp>](## "port_channel_interfaces.[].switchport.vlan_translations.in_required") | Boolean |  |  |  | Drop the ingress traffic that do not match any VLAN mapping. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;out_required</samp>](## "port_channel_interfaces.[].switchport.vlan_translations.out_required") | Boolean |  |  |  | Drop the egress traffic that do not match any VLAN mapping. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_in</samp>](## "port_channel_interfaces.[].switchport.vlan_translations.direction_in") | List, items: Dictionary |  |  |  | Map ingress traffic only. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;from</samp>](## "port_channel_interfaces.[].switchport.vlan_translations.direction_in.[].from") | String |  |  |  | VLAN ID or range of VLAN IDs to map from. Range 1-4094. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to</samp>](## "port_channel_interfaces.[].switchport.vlan_translations.direction_in.[].to") | Integer |  |  | Min: 1<br>Max: 4094 | VLAN ID to map to. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1q_tunnel</samp>](## "port_channel_interfaces.[].switchport.vlan_translations.direction_in.[].dot1q_tunnel") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner_vlan_from</samp>](## "port_channel_interfaces.[].switchport.vlan_translations.direction_in.[].inner_vlan_from") | Integer |  |  | Min: 1<br>Max: 4094 | Inner VLAN ID to map from. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_out</samp>](## "port_channel_interfaces.[].switchport.vlan_translations.direction_out") | List, items: Dictionary |  |  |  | Map egress traffic only. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;from</samp>](## "port_channel_interfaces.[].switchport.vlan_translations.direction_out.[].from") | String | Required |  |  | VLAN ID or range of VLAN IDs to map from. Range 1-4094. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to</samp>](## "port_channel_interfaces.[].switchport.vlan_translations.direction_out.[].to") | Integer |  |  | Min: 1<br>Max: 4094 | VLAN ID to map to. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1q_tunnel_to</samp>](## "port_channel_interfaces.[].switchport.vlan_translations.direction_out.[].dot1q_tunnel_to") | String |  |  |  | VLAN ID or range of VLAN IDs or "all". Range 1-4094.<br>This takes precedence over `to` and `inner_vlan_to`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner_vlan_to</samp>](## "port_channel_interfaces.[].switchport.vlan_translations.direction_out.[].inner_vlan_to") | Integer |  |  | Min: 1<br>Max: 4094 | Inner VLAN ID to map to. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction_both</samp>](## "port_channel_interfaces.[].switchport.vlan_translations.direction_both") | List, items: Dictionary |  |  |  | Map both egress and ingress traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;from</samp>](## "port_channel_interfaces.[].switchport.vlan_translations.direction_both.[].from") | String | Required |  |  | VLAN ID or range of VLAN IDs to map from. Range 1-4094. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;to</samp>](## "port_channel_interfaces.[].switchport.vlan_translations.direction_both.[].to") | Integer | Required |  | Min: 1<br>Max: 4094 | VLAN ID to map to. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1q_tunnel</samp>](## "port_channel_interfaces.[].switchport.vlan_translations.direction_both.[].dot1q_tunnel") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner_vlan_from</samp>](## "port_channel_interfaces.[].switchport.vlan_translations.direction_both.[].inner_vlan_from") | Integer |  |  | Min: 1<br>Max: 4094 | Inner VLAN ID to map from. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;network</samp>](## "port_channel_interfaces.[].switchport.vlan_translations.direction_both.[].network") | Boolean |  |  |  | Enable use of network-side VLAN ID.<br>This setting can only be enabled when `inner_vlan_from` is defined. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_forwarding_accept_all</samp>](## "port_channel_interfaces.[].switchport.vlan_forwarding_accept_all") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;backup_link</samp>](## "port_channel_interfaces.[].switchport.backup_link") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "port_channel_interfaces.[].switchport.backup_link.interface") | String | Required |  |  | Backup interface. Example - Ethernet4, Vlan10 etc. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefer_vlan</samp>](## "port_channel_interfaces.[].switchport.backup_link.prefer_vlan") | String |  |  |  | VLANs to carry on the backup interface (1-4094). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;backup</samp>](## "port_channel_interfaces.[].switchport.backup") | Dictionary |  |  |  | The `backup_link` is required for this setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dest_macaddr</samp>](## "port_channel_interfaces.[].switchport.backup.dest_macaddr") | String |  |  | Format: mac | Destination MAC address for MAC move updates.<br>The mac address should be multicast or broadcast.<br>Example: 01:00:00:00:00:00 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;initial_mac_move_delay</samp>](## "port_channel_interfaces.[].switchport.backup.initial_mac_move_delay") | Integer |  |  | Min: 0<br>Max: 65535 | Initial MAC move delay in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_move_burst</samp>](## "port_channel_interfaces.[].switchport.backup.mac_move_burst") | Integer |  |  | Min: 0<br>Max: 65535 | Size of MAC move bursts. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_move_burst_interval</samp>](## "port_channel_interfaces.[].switchport.backup.mac_move_burst_interval") | Integer |  |  | Min: 0<br>Max: 65535 | MAC move burst interval in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preemption_delay</samp>](## "port_channel_interfaces.[].switchport.backup.preemption_delay") | Integer |  |  | Min: 0<br>Max: 65535 | Preemption delay in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_security</samp>](## "port_channel_interfaces.[].switchport.port_security") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "port_channel_interfaces.[].switchport.port_security.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_address_maximum</samp>](## "port_channel_interfaces.[].switchport.port_security.mac_address_maximum") | Dictionary |  |  |  | Maximum number of MAC addresses allowed on the interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;disabled</samp>](## "port_channel_interfaces.[].switchport.port_security.mac_address_maximum.disabled") | Boolean |  |  |  | Disable port level check for port security (only in violation 'shutdown' mode). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;limit</samp>](## "port_channel_interfaces.[].switchport.port_security.mac_address_maximum.limit") | Integer |  |  | Min: 1<br>Max: 1000 | MAC address limit. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;violation</samp>](## "port_channel_interfaces.[].switchport.port_security.violation") | Dictionary |  |  |  | Configure violation mode (shutdown or protect), EOS default is 'shutdown'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "port_channel_interfaces.[].switchport.port_security.violation.mode") | String |  |  | Valid Values:<br>- <code>shutdown</code><br>- <code>protect</code> | Configure port security mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protect_log</samp>](## "port_channel_interfaces.[].switchport.port_security.violation.protect_log") | Boolean |  |  |  | Log new addresses seen after limit is reached in protect mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_default_mac_address_maximum</samp>](## "port_channel_interfaces.[].switchport.port_security.vlan_default_mac_address_maximum") | Integer |  |  | Min: 0<br>Max: 1000 | Default maximum MAC addresses for all VLANs on this interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlans</samp>](## "port_channel_interfaces.[].switchport.port_security.vlans") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;range</samp>](## "port_channel_interfaces.[].switchport.port_security.vlans.[].range") | String | Required, Unique |  |  | VLAN ID or range(s) of VLAN IDs, <1-4094>.<br>Example:<br>  - 3<br>  - 1,3<br>  - 1-10<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_address_maximum</samp>](## "port_channel_interfaces.[].switchport.port_security.vlans.[].mac_address_maximum") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tap</samp>](## "port_channel_interfaces.[].switchport.tap") | Dictionary |  |  |  | In tap mode, the interface operates as a tap port.<br>Tap ports receive traffic for replication on one or more tool ports.<br>This setting applies only to parent interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allowed_vlan</samp>](## "port_channel_interfaces.[].switchport.tap.allowed_vlan") | String |  |  |  | VLAN ID or range(s) of VLAN IDs within range 1-4094. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "port_channel_interfaces.[].switchport.tap.default") | Dictionary |  |  |  | Default tap destination config. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "port_channel_interfaces.[].switchport.tap.default.groups") | List, items: String |  |  |  | Tap group names for the interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "port_channel_interfaces.[].switchport.tap.default.groups.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "port_channel_interfaces.[].switchport.tap.default.interfaces") | List, items: String |  |  |  | Interfaces like -  Ethernet1, InternalRecirc1, Port-Channel1, Recirc-Channel1. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "port_channel_interfaces.[].switchport.tap.default.interfaces.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nexthop_groups</samp>](## "port_channel_interfaces.[].switchport.tap.default.nexthop_groups") | List, items: String |  |  |  | Default nexthop-group names. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "port_channel_interfaces.[].switchport.tap.default.nexthop_groups.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identity</samp>](## "port_channel_interfaces.[].switchport.tap.identity") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "port_channel_interfaces.[].switchport.tap.identity.id") | Integer |  |  | Min: 1<br>Max: 65535 | Tap port VLAN ID (1-4094) or DzGRE extended ID (1-65535). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inner_vlan</samp>](## "port_channel_interfaces.[].switchport.tap.identity.inner_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Tap port inner VLAN ID. Only applicable if `id` is a VLAN ID (1-4094). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_pop_all</samp>](## "port_channel_interfaces.[].switchport.tap.mpls_pop_all") | Boolean |  |  |  | Pop all MPLS labels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;native_vlan</samp>](## "port_channel_interfaces.[].switchport.tap.native_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | Native VLAN ID when interface is in tap mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;truncation</samp>](## "port_channel_interfaces.[].switchport.tap.truncation") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "port_channel_interfaces.[].switchport.tap.truncation.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "port_channel_interfaces.[].switchport.tap.truncation.size") | Integer |  |  | Min: 100<br>Max: 9236 | Ingress packet truncation size in bytes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_address</samp>](## "port_channel_interfaces.[].switchport.tap.mac_address") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "port_channel_interfaces.[].switchport.tap.mac_address.source") | String |  |  | Pattern: `^([0-9a-f]{2}:){5}[0-9a-f]{2}$` | MAC address for the source. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "port_channel_interfaces.[].switchport.tap.mac_address.destination") | String |  |  | Pattern: `^([0-9a-f]{2}:){5}[0-9a-f]{2}$` | MAC address for the destination. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation</samp>](## "port_channel_interfaces.[].switchport.tap.encapsulation") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vxlan_strip</samp>](## "port_channel_interfaces.[].switchport.tap.encapsulation.vxlan_strip") | Boolean |  |  |  | Strip VXLAN encapsulation header.<br>`encapsulation.vxlan_strip` and `mpls_pop_all` are mutually exclusive.<br>`mpls_pop_all` takes precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gre</samp>](## "port_channel_interfaces.[].switchport.tap.encapsulation.gre") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;strip</samp>](## "port_channel_interfaces.[].switchport.tap.encapsulation.gre.strip") | Boolean |  |  |  | Strip GRE encapsulation header for all GRE tunnels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocols</samp>](## "port_channel_interfaces.[].switchport.tap.encapsulation.gre.protocols") | List, items: Dictionary |  |  |  | Protocols for all destinations; destination-specific protocols should be set under the `destinations[].protocols` key. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;protocol</samp>](## "port_channel_interfaces.[].switchport.tap.encapsulation.gre.protocols.[].protocol") | String | Required, Unique |  |  | Protocol type in GRE header.<br>Valid range: 0x0-0xFFFF. The value must be enclosed in quotes, e.g., "0x0". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;strip</samp>](## "port_channel_interfaces.[].switchport.tap.encapsulation.gre.protocols.[].strip") | Boolean |  |  |  | This is a required key to strip GRE encapsulation header with protocols. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;feature_header_length</samp>](## "port_channel_interfaces.[].switchport.tap.encapsulation.gre.protocols.[].feature_header_length") | Integer |  |  | Min: 1<br>Max: 16 | Feature header length in bytes.<br>Note: This setting does not appear in the EOS running-config for protocol 0x0. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;re_encapsulation_ethernet_header</samp>](## "port_channel_interfaces.[].switchport.tap.encapsulation.gre.protocols.[].re_encapsulation_ethernet_header") | Boolean |  |  |  | Extra ethernet header to prepend to the terminated packet.<br>Note: This setting does not appear in the EOS running-config for protocol 0x0. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destinations</samp>](## "port_channel_interfaces.[].switchport.tap.encapsulation.gre.destinations") | List, items: Dictionary |  |  |  | In EOS, `gre.strip` and `destinations.destination/source.strip` (without defining protocols) are mutually exclusive. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;destination</samp>](## "port_channel_interfaces.[].switchport.tap.encapsulation.gre.destinations.[].destination") | String | Required, Unique |  |  | Destination IP address of tunnel packets. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "port_channel_interfaces.[].switchport.tap.encapsulation.gre.destinations.[].source") | String |  |  |  | Source IP address of tunnel packets. Applied only when destination is defined. When not defined; any GRE packet that matches the `destination` is terminated. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;strip</samp>](## "port_channel_interfaces.[].switchport.tap.encapsulation.gre.destinations.[].strip") | Boolean |  |  |  | Strip GRE encapsulation header for specific destination. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocols</samp>](## "port_channel_interfaces.[].switchport.tap.encapsulation.gre.destinations.[].protocols") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;protocol</samp>](## "port_channel_interfaces.[].switchport.tap.encapsulation.gre.destinations.[].protocols.[].protocol") | String | Required, Unique |  |  | Protocol type in GRE header.<br>Valid range: 0x0-0xFFFF. The value must be enclosed in quotes, e.g., "0x0". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;strip</samp>](## "port_channel_interfaces.[].switchport.tap.encapsulation.gre.destinations.[].protocols.[].strip") | Boolean |  |  |  | This is a required key to strip GRE encapsulation header for specific destination with protocols. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;feature_header_length</samp>](## "port_channel_interfaces.[].switchport.tap.encapsulation.gre.destinations.[].protocols.[].feature_header_length") | Integer |  |  | Min: 1<br>Max: 16 | Feature header length in bytes.<br>Note: This setting does not appear in the EOS running-config for protocol 0x0. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;re_encapsulation_ethernet_header</samp>](## "port_channel_interfaces.[].switchport.tap.encapsulation.gre.destinations.[].protocols.[].re_encapsulation_ethernet_header") | Boolean |  |  |  | Extra ethernet header to prepend to the terminated packet.<br>Note: This setting does not appear in the EOS running-config for protocol 0x0. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tool</samp>](## "port_channel_interfaces.[].switchport.tool") | Dictionary |  |  |  | In tool mode, the interface operates as a tool port.<br>Tool ports replicate traffic received by tap ports.<br>This setting applies only to parent interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mpls_pop_all</samp>](## "port_channel_interfaces.[].switchport.tool.mpls_pop_all") | Boolean |  |  |  | Pop all MPLS labels. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation</samp>](## "port_channel_interfaces.[].switchport.tool.encapsulation") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1br_strip</samp>](## "port_channel_interfaces.[].switchport.tool.encapsulation.dot1br_strip") | Boolean |  |  |  | Remove a 802.1 BR tag in packet header. 'mpls_pop_all' takes precedence over 'dot1br_strip' in EOS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vn_tag_strip</samp>](## "port_channel_interfaces.[].switchport.tool.encapsulation.vn_tag_strip") | Boolean |  |  |  | Remove a VN-tag in packet header. 'mpls_pop_all' takes precedence over 'vn_tag_strip' in EOS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allowed_vlan</samp>](## "port_channel_interfaces.[].switchport.tool.allowed_vlan") | String |  |  |  | VLAN ID or range of VLAN IDs within range 1-4094. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;identity</samp>](## "port_channel_interfaces.[].switchport.tool.identity") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tag</samp>](## "port_channel_interfaces.[].switchport.tool.identity.tag") | String |  |  | Valid Values:<br>- <code>dot1q</code><br>- <code>qinq</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1q_dzgre_source</samp>](## "port_channel_interfaces.[].switchport.tool.identity.dot1q_dzgre_source") | String |  |  | Valid Values:<br>- <code>policy</code><br>- <code>port</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qinq_dzgre_source</samp>](## "port_channel_interfaces.[].switchport.tool.identity.qinq_dzgre_source") | String |  |  | Valid Values:<br>- <code>policy inner port</code><br>- <code>port inner policy</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "port_channel_interfaces.[].switchport.tool.groups") | List, items: String |  |  |  | Tool groups for the interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "port_channel_interfaces.[].switchport.tool.groups.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dot1q_remove_outer_vlan_tag</samp>](## "port_channel_interfaces.[].switchport.tool.dot1q_remove_outer_vlan_tag") | String |  |  |  | Indices of vlan tags to be removed.<br>Range: 1-2 |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;traffic_engineering</samp>](## "port_channel_interfaces.[].traffic_engineering") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "port_channel_interfaces.[].traffic_engineering.enabled") | Boolean |  |  |  | Whether to enable traffic-engineering on this interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;administrative_groups</samp>](## "port_channel_interfaces.[].traffic_engineering.administrative_groups") | List, items: String |  |  |  | List of traffic-engineering administrative groups, valid values are names, ranges 0-127, or single integers 0-127. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "port_channel_interfaces.[].traffic_engineering.administrative_groups.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;validate_state</samp>](## "port_channel_interfaces.[].validate_state") | Boolean |  |  |  | Set to false to disable interface state and LLDP topology validation performed by the `eos_validate_state` role. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;validate_lldp</samp>](## "port_channel_interfaces.[].validate_lldp") | Boolean |  |  |  | Set to false to disable the LLDP topology validation performed by the `eos_validate_state` role. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "port_channel_interfaces.[].eos_cli") | String |  |  |  | Multiline EOS CLI rendered directly on the port-channel interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;esi</samp>](## "port_channel_interfaces.[].esi") <span style="color:red">removed</span> | String |  |  |  | EVPN Ethernet Segment Identifier (Type 1 format).<br><span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>evpn_ethernet_segment.identifier</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rt</samp>](## "port_channel_interfaces.[].rt") <span style="color:red">removed</span> | String |  |  |  | EVPN Route Target for ESI with format xx:xx:xx:xx:xx:xx.<br><span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>evpn_ethernet_segment.route_target</samp> instead.</span> |

=== "YAML"

    ```yaml
    port_channel_interfaces:
      - name: <str; required; unique>
        description: <str>

        # Interface profile.
        profile: <str>
        logging:
          event:
            link_status: <bool>

            # Discards due to storm-control.
            storm_control_discards: <bool>
        shutdown: <bool>

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
        snmp_trap_link_change: <bool>

        # l3dot1q and l2dot1q are used for sub-interfaces. The parent interface should be defined as routed.
        # Interface will not be listed in device documentation, unless "type" is set.
        # This key is deprecated.
        # Support will be removed in AVD version 6.0.0.
        # See [here](https://avd.arista.com/5.x/docs/porting-guides/5.x.x.html#removal-of-type-key-dependency-for-rendering-ethernetport-channel-interfaces-configuration-and-documentation) for details.
        type: <str; "routed" | "switched" | "l3dot1q" | "l2dot1q">

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

        # VRF name.
        vrf: <str>

        # This setting can only be applied to sub-interfaces on EOS.
        # Warning: `encapsulation_vlan` should not be combined with `ethernet_interfaces[].type: l3dot1q` or `ethernet_interfaces[].type: l2dot1q`.
        encapsulation_vlan:
          client:
            # This key is deprecated.
            # Support will be removed in AVD version 6.0.0.
            dot1q:

              # Client VLAN ID.
              vlan: <int>

              # Client Outer VLAN ID.
              outer: <int; 1-4094>

              # Client Inner VLAN ID.
              inner: <int; 1-4094>
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

          # Network encapsulation are all optional, and skipped if using client unmatched.
          network:
            # This key is deprecated.
            # Support will be removed in AVD version 6.0.0.
            dot1q:

              # Network VLAN ID.
              vlan: <int; 1-4094>

              # Network Outer VLAN ID.
              outer: <int; 1-4094>

              # Network Inner VLAN ID.
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

            # Network inner VLAN ID. Not applicable for `encapsulation: untagged` or `encapsulation: client`.
            inner_vlan: <int; 1-4094>
            inner_encapsulation: <str; "dot1q" | "dot1ad">

        # This setting can only be applied to sub-interfaces on EOS.
        # Warning: `vlan_id` should not be combined with `ethernet_interfaces[].type == l2dot1q`.
        vlan_id: <int; 1-4094>
        # This key is deprecated.
        # Support will be removed in AVD version 6.0.0.
        # Use <samp>switchport.mode</samp> instead.
        mode: <str; "access" | "dot1q-tunnel" | "trunk" | "trunk phone">

        # If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence.
        # This key is deprecated.
        # Support will be removed in AVD version 6.0.0.
        # Use <samp>switchport.trunk.native_vlan</samp> instead.
        native_vlan: <int>

        # If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence.
        # This key is deprecated.
        # Support will be removed in AVD version 6.0.0.
        # Use <samp>switchport.trunk.native_vlan_tag</samp> instead.
        native_vlan_tag: <bool>
        link_tracking_groups:

            # Group name.
          - name: <str; required; unique>
            direction: <str; "upstream" | "downstream">
        link_tracking:
          direction: <str; "upstream" | "downstream">

          # Link state group(s) an interface belongs to.
          groups:

              # Group names.
            - <str>
        # This key is deprecated.
        # Support will be removed in AVD version 6.0.0.
        # Use <samp>switchport.phone</samp> instead.
        phone:
          trunk: <str; "tagged" | "untagged">
          vlan: <int; 1-4094>
        l2_protocol:

          # Vlan tag to configure on sub-interface.
          encapsulation_dot1q_vlan: <int>

          # L2 protocol forwarding profile.
          forwarding_profile: <str>
        mtu: <int; 68-65535>

        # MLAG ID.
        mlag: <int; 1-2000>
        # This key is deprecated.
        # Support will be removed in AVD version 6.0.0.
        # Use <samp>switchport.trunk.groups</samp> instead.
        trunk_groups:
          - <str>

        # Timeout in seconds. EOS default is 90 seconds.
        lacp_fallback_timeout: <int; 0-300>

        # Minimum number of ports required up before bringing up a port-channel.
        # Maximum in `min_links` is hardware dependent.
        min_links: <int; 0-120>
        lacp_fallback_mode: <str; "individual" | "static">
        qos:
          trust: <str; "dscp" | "cos" | "disabled">

          # DSCP value.
          dscp: <int>

          # COS value.
          cos: <int>
        bfd:
          echo: <bool>

          # Interval in milliseconds.
          interval: <int>

          # Rate in milliseconds.
          min_rx: <int>
          multiplier: <int; 3-50>

          # IPv4 or IPv6 address. When the Port-channel is a L2 interface, a local L3 BFD address (router_bfd.local_address) has to be defined globally on the switch.
          neighbor: <str>
          per_link:
            enabled: <bool>
            rfc_7130: <bool>
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
        shape:

          # Rate in kbps, pps or percent.
          # Supported options are platform dependent.
          # Examples:
          # - "5000 kbps"
          # - "1000 pps"
          # - "20 percent"
          rate: <str>
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
        ip_proxy_arp: <bool>

        # ISIS instance.
        isis_enable: <str>

        # Enable BFD for ISIS.
        isis_bfd: <bool>
        isis_passive: <bool>
        isis_metric: <int>
        isis_network_point_to_point: <bool>
        isis_circuit_type: <str; "level-1-2" | "level-1" | "level-2">
        isis_hello_padding: <bool>
        # This key is deprecated.
        # Support will be removed in AVD version v6.0.0.
        # Use <samp>port_channel_interfaces[].isis_authentication.both.mode or port_channel_interfaces[].isis_authentication.level_1.mode or port_channel_interfaces[].isis_authentication.level_2.mode</samp> instead.
        isis_authentication_mode: <str; "text" | "md5">

        # Type-7 encrypted password.
        # This key is deprecated.
        # Support will be removed in AVD version v6.0.0.
        # Use <samp>port_channel_interfaces[].isis_authentication.both.key or port_channel_interfaces[].isis_authentication.level_1.key or port_channel_interfaces[].isis_authentication.level_2.key</samp> instead.
        isis_authentication_key: <str>

        # This key should not be mixed with port_channel_interfaces[].isis_authentication_mode or ethernet_interfaces[].isis_authentication_key.
        isis_authentication:

          # Authentication settings for level-1 and level-2. 'both' takes precedence over 'level_1' and 'level_2' settings.
          both:

            # Configure authentication key type.
            key_type: <str; "0" | "7" | "8a">

            # Password string. `key_type` is required for this setting.
            key: <str>
            key_ids:

                # Configure authentication key-id.
              - id: <int; 1-65535; required; unique>
                algorithm: <str; "sha-1" | "sha-224" | "sha-256" | "sha-384" | "sha-512"; required>

                # Configure authentication key type.
                key_type: <str; "0" | "7" | "8a"; required>

                # Password string.
                key: <str; required>

                # SHA digest computation according to rfc5310.
                rfc_5310: <bool>

            # Authentication mode.
            mode: <str; "md5" | "sha" | "text" | "shared-secret">

            # Required settings for authentication mode 'sha'.
            sha:
              key_id: <int; 1-65535; required>

            # Required settings for authentication mode 'shared_secret'.
            shared_secret:
              profile: <str; required>
              algorithm: <str; "md5" | "sha-1" | "sha-224" | "sha-256" | "sha-384" | "sha-512"; required>

            # Disable authentication check on the receive side.
            rx_disabled: <bool>

          # Authentication settings for level-1. 'both' takes precedence over 'level_1' and 'level_2' settings.
          level_1:

            # Configure authentication key type.
            key_type: <str; "0" | "7" | "8a">

            # Password string. `key_type` is required for this setting.
            key: <str>
            key_ids:

                # Configure authentication key-id.
              - id: <int; 1-65535; required; unique>
                algorithm: <str; "sha-1" | "sha-224" | "sha-256" | "sha-384" | "sha-512"; required>

                # Configure authentication key type.
                key_type: <str; "0" | "7" | "8a"; required>

                # Password string.
                key: <str; required>

                # SHA digest computation according to rfc5310.
                rfc_5310: <bool>

            # Authentication mode.
            mode: <str; "md5" | "sha" | "text" | "shared-secret">

            # Required settings for authentication mode 'sha'.
            sha:
              key_id: <int; 1-65535; required>

            # Required settings for authentication mode 'shared_secret'.
            shared_secret:
              profile: <str; required>
              algorithm: <str; "md5" | "sha-1" | "sha-224" | "sha-256" | "sha-384" | "sha-512"; required>

            # Disable authentication check on the receive side.
            rx_disabled: <bool>

          # Authentication settings for level-2. 'both' takes precedence over 'level_1' and 'level_2' settings.
          level_2:

            # Configure authentication key type.
            key_type: <str; "0" | "7" | "8a">

            # Password string. `key_type` is required for this setting.
            key: <str>
            key_ids:

                # Configure authentication key-id.
              - id: <int; 1-65535; required; unique>
                algorithm: <str; "sha-1" | "sha-224" | "sha-256" | "sha-384" | "sha-512"; required>

                # Configure authentication key type.
                key_type: <str; "0" | "7" | "8a"; required>

                # Password string.
                key: <str; required>

                # SHA digest computation according to rfc5310.
                rfc_5310: <bool>

            # Authentication mode.
            mode: <str; "md5" | "sha" | "text" | "shared-secret">

            # Required settings for authentication mode 'sha'.
            sha:
              key_id: <int; 1-65535; required>

            # Required settings for authentication mode 'shared_secret'.
            shared_secret:
              profile: <str; required>
              algorithm: <str; "md5" | "sha-1" | "sha-224" | "sha-256" | "sha-384" | "sha-512"; required>

            # Disable authentication check on the receive side.
            rx_disabled: <bool>
        traffic_policy:

          # Ingress traffic policy.
          input: <str>

          # Egress traffic policy.
          output: <str>
        evpn_ethernet_segment:

          # EVPN Ethernet Segment Identifier (Type 1 format).
          identifier: <str>
          redundancy: <str; "all-active" | "single-active">
          designated_forwarder_election:
            algorithm: <str; "modulus" | "preference">

            # Preference_value is only used when "algorithm" is "preference".
            preference_value: <int; 0-65535>

            # Dont_preempt is only used when "algorithm" is "preference".
            dont_preempt: <bool; default=False>
            hold_time: <int>
            subsequent_hold_time: <int>
            candidate_reachability_required: <bool>
          mpls:
            shared_index: <int; 1-1024>
            tunnel_flood_filter_time: <int>

          # EVPN Route Target for ESI with format xx:xx:xx:xx:xx:xx.
          route_target: <str>

        # LACP ID with format xxxx.xxxx.xxxx.
        lacp_id: <str>
        spanning_tree_bpdufilter: <str; "enabled" | "disabled" | "True" | "False" | "true" | "false">
        spanning_tree_bpduguard: <str; "enabled" | "disabled" | "True" | "False" | "true" | "false">
        spanning_tree_guard: <str; "loop" | "root" | "disabled">
        spanning_tree_portfast: <str; "edge" | "network">
        vmtracer: <bool>
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

          # When MPASS is enabled on an MLAG port-channel, MLAG peers coordinate to function as a single PTP logical device.
          # Arista PTP enabled devices always place PTP messages on the same physical link within the port-channel.
          # Hence, MPASS is needed only on MLAG port-channels connected to non-Arista devices.
          mpass: <bool>

        # IPv4 address/mask or "dhcp".
        ip_address: <str>

        # Install default-route obtained via DHCP.
        dhcp_client_accept_default_route: <bool>
        ip_verify_unicast_source_reachable_via: <str; "any" | "rx">
        ip_nat:
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

        # IPv6 address/mask.
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

        # QOS profile.
        service_profile: <str>
        ospf_network_point_to_point: <bool>
        ospf_area: <str>
        ospf_cost: <int>
        ospf_authentication: <str; "none" | "simple" | "message-digest">

        # Encrypted password.
        ospf_authentication_key: <str>
        ospf_message_digest_keys:
          - id: <int; required; unique>
            hash_algorithm: <str; "md5" | "sha1" | "sha256" | "sha384" | "sha512">

            # Encrypted password.
            key: <str>
        flow_tracker:

          # Sampled flow tracker name.
          sampled: <str>

          # Hardware flow tracker name.
          hardware: <str>
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
        switchport:

          # Warning: This should not be combined with `port_channel_interfaces[].type = routed`.
          enabled: <bool>

          # Warning: This should not be combined with `port_channel_interfaces[].mode`
          mode: <str; "access" | "dot1q-tunnel" | "trunk" | "trunk phone">

          # Set VLAN when interface is in access mode.
          # Warning: This should not be combined with `port_channel_interfaces[].mode = access/dot1q-tunnel` and `port_channel_interface.vlans`.
          access_vlan: <int; 1-4094>
          trunk:

            # VLAN ID or range(s) of VLAN IDs (1-4094).
            # Warning: This should not be combined with `port_channel_interfaces[].mode = trunk` and `port_channel_interfaces[].vlans`.
            allowed_vlan: <str>

            # Set native VLAN when interface is in trunking mode.
            # Warning: This should not be combined with `port_channel_interfaces[].native_vlan`.
            native_vlan: <int; 1-4094>

            # If setting both native_vlan and native_vlan_tag, native_vlan_tag takes precedence.
            # Warning: This should not be combined with `port_channel_interfaces[].native_vlan_tag`.
            native_vlan_tag: <bool>

            # Enable secondary VLAN mapping for a private vlan.
            # Warning: This should not be combined with `port_channel_interfaces[].trunk_private_vlan_secondary`.
            private_vlan_secondary: <bool>

            # Warning: This should not be combined with `port_channel_interfaces[].trunk_groups`.
            groups:

                # Trunk group name.
              - <str>
          phone:

            # Warning: This should not be combined with `port_channel_interfaces[].phone.vlan`.
            vlan: <int; 1-4094>

            # Warning: This should not be combined with `port_channel_interfaces[].phone.trunk`
            trunk: <str; "tagged" | "tagged phone" | "untagged" | "untagged phone">

          # Secondary VLAN IDs of the private VLAN mapping.
          # Warning: This should not be combined with `port_channel_interfaces[].pvlan_mapping`.
          pvlan_mapping: <str>
          dot1q:

            # Ethertype/TPID (Tag Protocol IDentifier) for VLAN tagged frames.
            ethertype: <int; 1536-65535>
            vlan_tag: <str; "disallowed" | "required">

          # tx: Allow bridged traffic to go out of the source interface.
          # tx multicast: Allow multicast traffic only to go out of the source interface.
          source_interface: <str; "tx" | "tx multicast">

          # VLAN Translation mappings.
          # Warning: This should not be combined with `port_channel_interfaces[].vlan_translations`.
          vlan_translations:

            # Drop the ingress traffic that do not match any VLAN mapping.
            in_required: <bool>

            # Drop the egress traffic that do not match any VLAN mapping.
            out_required: <bool>

            # Map ingress traffic only.
            direction_in:

                # VLAN ID or range of VLAN IDs to map from. Range 1-4094.
              - from: <str>

                # VLAN ID to map to.
                to: <int; 1-4094>
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
            interface: <str; required>

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
                mac_address_maximum: <int>

          # In tap mode, the interface operates as a tap port.
          # Tap ports receive traffic for replication on one or more tool ports.
          # This setting applies only to parent interfaces.
          tap:

            # VLAN ID or range(s) of VLAN IDs within range 1-4094.
            allowed_vlan: <str>

            # Default tap destination config.
            default:

              # Tap group names for the interface.
              groups:
                - <str>

              # Interfaces like -  Ethernet1, InternalRecirc1, Port-Channel1, Recirc-Channel1.
              interfaces:
                - <str>

              # Default nexthop-group names.
              nexthop_groups:
                - <str>
            identity:

              # Tap port VLAN ID (1-4094) or DzGRE extended ID (1-65535).
              id: <int; 1-65535>

              # Tap port inner VLAN ID. Only applicable if `id` is a VLAN ID (1-4094).
              inner_vlan: <int; 1-4094>

            # Pop all MPLS labels.
            mpls_pop_all: <bool>

            # Native VLAN ID when interface is in tap mode.
            native_vlan: <int; 1-4094>
            truncation:
              enabled: <bool>

              # Ingress packet truncation size in bytes.
              size: <int; 100-9236>
            mac_address:

              # MAC address for the source.
              source: <str>

              # MAC address for the destination.
              destination: <str>
            encapsulation:

              # Strip VXLAN encapsulation header.
              # `encapsulation.vxlan_strip` and `mpls_pop_all` are mutually exclusive.
              # `mpls_pop_all` takes precedence.
              vxlan_strip: <bool>
              gre:

                # Strip GRE encapsulation header for all GRE tunnels.
                strip: <bool>

                # Protocols for all destinations; destination-specific protocols should be set under the `destinations[].protocols` key.
                protocols:

                    # Protocol type in GRE header.
                    # Valid range: 0x0-0xFFFF. The value must be enclosed in quotes, e.g., "0x0".
                  - protocol: <str; required; unique>

                    # This is a required key to strip GRE encapsulation header with protocols.
                    strip: <bool>

                    # Feature header length in bytes.
                    # Note: This setting does not appear in the EOS running-config for protocol 0x0.
                    feature_header_length: <int; 1-16>

                    # Extra ethernet header to prepend to the terminated packet.
                    # Note: This setting does not appear in the EOS running-config for protocol 0x0.
                    re_encapsulation_ethernet_header: <bool>

                # In EOS, `gre.strip` and `destinations.destination/source.strip` (without defining protocols) are mutually exclusive.
                destinations:

                    # Destination IP address of tunnel packets.
                  - destination: <str; required; unique>

                    # Source IP address of tunnel packets. Applied only when destination is defined. When not defined; any GRE packet that matches the `destination` is terminated.
                    source: <str>

                    # Strip GRE encapsulation header for specific destination.
                    strip: <bool>
                    protocols:

                        # Protocol type in GRE header.
                        # Valid range: 0x0-0xFFFF. The value must be enclosed in quotes, e.g., "0x0".
                      - protocol: <str; required; unique>

                        # This is a required key to strip GRE encapsulation header for specific destination with protocols.
                        strip: <bool>

                        # Feature header length in bytes.
                        # Note: This setting does not appear in the EOS running-config for protocol 0x0.
                        feature_header_length: <int; 1-16>

                        # Extra ethernet header to prepend to the terminated packet.
                        # Note: This setting does not appear in the EOS running-config for protocol 0x0.
                        re_encapsulation_ethernet_header: <bool>

          # In tool mode, the interface operates as a tool port.
          # Tool ports replicate traffic received by tap ports.
          # This setting applies only to parent interfaces.
          tool:

            # Pop all MPLS labels.
            mpls_pop_all: <bool>
            encapsulation:

              # Remove a 802.1 BR tag in packet header. 'mpls_pop_all' takes precedence over 'dot1br_strip' in EOS.
              dot1br_strip: <bool>

              # Remove a VN-tag in packet header. 'mpls_pop_all' takes precedence over 'vn_tag_strip' in EOS.
              vn_tag_strip: <bool>

            # VLAN ID or range of VLAN IDs within range 1-4094.
            allowed_vlan: <str>
            identity:
              tag: <str; "dot1q" | "qinq">
              dot1q_dzgre_source: <str; "policy" | "port">
              qinq_dzgre_source: <str; "policy inner port" | "port inner policy">

            # Tool groups for the interface.
            groups:
              - <str>

            # Indices of vlan tags to be removed.
            # Range: 1-2
            dot1q_remove_outer_vlan_tag: <str>
        traffic_engineering:

          # Whether to enable traffic-engineering on this interface.
          enabled: <bool>

          # List of traffic-engineering administrative groups, valid values are names, ranges 0-127, or single integers 0-127.
          administrative_groups:
            - <str>

        # Set to false to disable interface state and LLDP topology validation performed by the `eos_validate_state` role.
        validate_state: <bool>

        # Set to false to disable the LLDP topology validation performed by the `eos_validate_state` role.
        validate_lldp: <bool>

        # Multiline EOS CLI rendered directly on the port-channel interface in the final EOS configuration.
        eos_cli: <str>
    ```
