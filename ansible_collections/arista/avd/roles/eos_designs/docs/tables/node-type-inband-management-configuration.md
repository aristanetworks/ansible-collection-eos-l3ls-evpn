<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "<node_type_keys.key>") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "<node_type_keys.key>.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_interface</samp>](## "<node_type_keys.key>.defaults.inband_mgmt_interface") | String |  |  |  | Pointer to interface used for inband management.<br>All configuration must be done using other data models like network services or structured_config.<br>'inband_mgmt_interface' is only used to refer to this interface as source in various management protocol settings (future feature).<br><br>On L2 switches, this defaults to Vlan<inband_mgmt_vlan> if either 'inband_mgmt_subnet' or 'inband_mgmt_ip' is set.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_vlan</samp>](## "<node_type_keys.key>.defaults.inband_mgmt_vlan") | Integer |  | `4092` |  | VLAN number used for inband management on L2 switches (switches using port-channel trunks as uplinks).<br>When using 'inband_mgmt_subnet' the VLAN and SVIs will be created automatically on this switch as well as all 'uplink_switches'.<br>When using 'inband_mgmt_ip' the VLAN and SVI will only be created on this device and added to uplink trunk. The VLAN and SVI on the parent switches must be created using network services data models. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_subnet</samp>](## "<node_type_keys.key>.defaults.inband_mgmt_subnet") | String |  |  | Format: ipv4_cidr | Optional IP subnet assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).<br>Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP.<br>This allows all l3leafs to reuse the same subnet across multiple racks without VXLAN extension.<br>SVI IP address will be assigned as follows:<br>virtual-router: <subnet> + 1<br>l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)<br>l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)<br>l2leafs       : <subnet> + 3 + <l2leaf id><br>GW on l2leafs : <subnet> + 1<br>Assign range larger than total l2leafs + 5<br><br>Setting is ignored if 'inband_mgmt_ip' is set.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_ip</samp>](## "<node_type_keys.key>.defaults.inband_mgmt_ip") | String |  |  | Format: ipv4_cidr | IP address assigned to the inband management interface set with 'inband_mgmt_vlan'.<br>This overrides 'inband_mgmt_subnet', hence all behavior of 'inband_mgmt_subnet' is removed.<br><br>If this is set the VLAN and SVI will only be created on the L2 switch and added to uplink trunk.<br>The VLAN and SVI on the parent switches must be created using network services data models.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_gateway</samp>](## "<node_type_keys.key>.defaults.inband_mgmt_gateway") | String |  |  | Format: ipv4 | Default gateway configured in the 'inband_mgmt_vrf' when using 'inband_mgmt_ip'. Otherwise gateway is derived from 'inband_mgmt_subnet' if set.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_ipv6_address</samp>](## "<node_type_keys.key>.defaults.inband_mgmt_ipv6_address") | String |  |  | Format: ipv6 | IPv6 address assigned to the inband management interface set with 'inband_mgmt_vlan'.<br>This overrides 'inband_mgmt_ipv6_subnet', hence the configuration of 'inband_mgmt_ipv6_subnet' is ignored.<br><br>If this is set the VLAN and SVI will only be created on the L2 switch and added to uplink trunk.<br>The VLAN and SVI on the parent switches must be created using network services data models.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_ipv6_subnet</samp>](## "<node_type_keys.key>.defaults.inband_mgmt_ipv6_subnet") | String |  |  | Format: ipv6_cidr | Optional IPv6 prefix assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).<br>Parent l3leafs will have SVI with "ipv6 virtual-router" and host-route injection based on ARP.<br>This allows all l3leafs to reuse the same subnet across multiple racks without VXLAN extension.<br>SVI IP address will be assigned as follows:<br>virtual-router: <subnet> + 1<br>l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)<br>l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)<br>l2leafs       : <subnet> + 3 + <l2leaf id><br>GW on l2leafs : <subnet> + 1<br>Assign range larger than total l2leafs + 5<br><br>Setting is ignored if 'inband_mgmt_ipv6_address' is set.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_ipv6_gateway</samp>](## "<node_type_keys.key>.defaults.inband_mgmt_ipv6_gateway") | String |  |  | Format: ipv6 | Default gateway configured in the 'inband_mgmt_vrf'.<br>Used when `inband_mgmt_ipv6_address` is set.<br>Ignored when 'inband_mgmt_ipv6_subnet' is set (first IP in subnet used as gateway).<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_description</samp>](## "<node_type_keys.key>.defaults.inband_mgmt_description") | String |  | `Inband Management` |  | Description configured on the Inband Management SVI.<br><br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_vlan_name</samp>](## "<node_type_keys.key>.defaults.inband_mgmt_vlan_name") | String |  | `INBAND_MGMT` |  | Name configured on the Inband Management VLAN.<br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_vrf</samp>](## "<node_type_keys.key>.defaults.inband_mgmt_vrf") | String |  | `default` |  | VRF configured on the Inband Management Interface.<br>The VRF is created if not already created by other means.<br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_mtu</samp>](## "<node_type_keys.key>.defaults.inband_mgmt_mtu") | Integer |  | `1500` |  | MTU configured on the Inband Management Interface.<br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_ztp</samp>](## "<node_type_keys.key>.defaults.inband_ztp") | Boolean |  | `False` |  | Enable to configure upstream device with proper configuration to allow downstream devices to be Zero-Touch-Provisioned over the uplink interfaces.<br>For L2 devices this setting also requires that the `inband_mgmt_vlan` is set for the node.<br><br>PREVIEW: Support for L3 devices is marked as "preview", meaning the data models or generated configuration can change at any time. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_ztp_lacp_fallback_delay</samp>](## "<node_type_keys.key>.defaults.inband_ztp_lacp_fallback_delay") | Integer |  | `30` | Min: 0<br>Max: 300 | Set the LACP fallback timeout of the upstream device's port-channel towards the downstream inband ZTP node.<br>This setting also requires that `inband_ztp` is set for the node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_management_subnet</samp>](## "<node_type_keys.key>.defaults.inband_management_subnet") <span style="color:red">removed</span> | String |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>inband_mgmt_subnet</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;inband_management_vlan</samp>](## "<node_type_keys.key>.defaults.inband_management_vlan") <span style="color:red">removed</span> | Integer |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>inband_mgmt_vlan</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_interface</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].inband_mgmt_interface") | String |  |  |  | Pointer to interface used for inband management.<br>All configuration must be done using other data models like network services or structured_config.<br>'inband_mgmt_interface' is only used to refer to this interface as source in various management protocol settings (future feature).<br><br>On L2 switches, this defaults to Vlan<inband_mgmt_vlan> if either 'inband_mgmt_subnet' or 'inband_mgmt_ip' is set.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_vlan</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].inband_mgmt_vlan") | Integer |  | `4092` |  | VLAN number used for inband management on L2 switches (switches using port-channel trunks as uplinks).<br>When using 'inband_mgmt_subnet' the VLAN and SVIs will be created automatically on this switch as well as all 'uplink_switches'.<br>When using 'inband_mgmt_ip' the VLAN and SVI will only be created on this device and added to uplink trunk. The VLAN and SVI on the parent switches must be created using network services data models. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_subnet</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].inband_mgmt_subnet") | String |  |  | Format: ipv4_cidr | Optional IP subnet assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).<br>Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP.<br>This allows all l3leafs to reuse the same subnet across multiple racks without VXLAN extension.<br>SVI IP address will be assigned as follows:<br>virtual-router: <subnet> + 1<br>l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)<br>l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)<br>l2leafs       : <subnet> + 3 + <l2leaf id><br>GW on l2leafs : <subnet> + 1<br>Assign range larger than total l2leafs + 5<br><br>Setting is ignored if 'inband_mgmt_ip' is set.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_ip</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].inband_mgmt_ip") | String |  |  | Format: ipv4_cidr | IP address assigned to the inband management interface set with 'inband_mgmt_vlan'.<br>This overrides 'inband_mgmt_subnet', hence all behavior of 'inband_mgmt_subnet' is removed.<br><br>If this is set the VLAN and SVI will only be created on the L2 switch and added to uplink trunk.<br>The VLAN and SVI on the parent switches must be created using network services data models.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_gateway</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].inband_mgmt_gateway") | String |  |  | Format: ipv4 | Default gateway configured in the 'inband_mgmt_vrf' when using 'inband_mgmt_ip'. Otherwise gateway is derived from 'inband_mgmt_subnet' if set.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_ipv6_address</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].inband_mgmt_ipv6_address") | String |  |  | Format: ipv6 | IPv6 address assigned to the inband management interface set with 'inband_mgmt_vlan'.<br>This overrides 'inband_mgmt_ipv6_subnet', hence the configuration of 'inband_mgmt_ipv6_subnet' is ignored.<br><br>If this is set the VLAN and SVI will only be created on the L2 switch and added to uplink trunk.<br>The VLAN and SVI on the parent switches must be created using network services data models.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_ipv6_subnet</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].inband_mgmt_ipv6_subnet") | String |  |  | Format: ipv6_cidr | Optional IPv6 prefix assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).<br>Parent l3leafs will have SVI with "ipv6 virtual-router" and host-route injection based on ARP.<br>This allows all l3leafs to reuse the same subnet across multiple racks without VXLAN extension.<br>SVI IP address will be assigned as follows:<br>virtual-router: <subnet> + 1<br>l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)<br>l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)<br>l2leafs       : <subnet> + 3 + <l2leaf id><br>GW on l2leafs : <subnet> + 1<br>Assign range larger than total l2leafs + 5<br><br>Setting is ignored if 'inband_mgmt_ipv6_address' is set.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_ipv6_gateway</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].inband_mgmt_ipv6_gateway") | String |  |  | Format: ipv6 | Default gateway configured in the 'inband_mgmt_vrf'.<br>Used when `inband_mgmt_ipv6_address` is set.<br>Ignored when 'inband_mgmt_ipv6_subnet' is set (first IP in subnet used as gateway).<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_description</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].inband_mgmt_description") | String |  | `Inband Management` |  | Description configured on the Inband Management SVI.<br><br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_vlan_name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].inband_mgmt_vlan_name") | String |  | `INBAND_MGMT` |  | Name configured on the Inband Management VLAN.<br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_vrf</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].inband_mgmt_vrf") | String |  | `default` |  | VRF configured on the Inband Management Interface.<br>The VRF is created if not already created by other means.<br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_mtu</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].inband_mgmt_mtu") | Integer |  | `1500` |  | MTU configured on the Inband Management Interface.<br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_ztp</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].inband_ztp") | Boolean |  | `False` |  | Enable to configure upstream device with proper configuration to allow downstream devices to be Zero-Touch-Provisioned over the uplink interfaces.<br>For L2 devices this setting also requires that the `inband_mgmt_vlan` is set for the node.<br><br>PREVIEW: Support for L3 devices is marked as "preview", meaning the data models or generated configuration can change at any time. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_ztp_lacp_fallback_delay</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].inband_ztp_lacp_fallback_delay") | Integer |  | `30` | Min: 0<br>Max: 300 | Set the LACP fallback timeout of the upstream device's port-channel towards the downstream inband ZTP node.<br>This setting also requires that `inband_ztp` is set for the node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_management_subnet</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].inband_management_subnet") <span style="color:red">removed</span> | String |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>inband_mgmt_subnet</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_management_vlan</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].inband_management_vlan") <span style="color:red">removed</span> | Integer |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>inband_mgmt_vlan</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_interface</samp>](## "<node_type_keys.key>.node_groups.[].inband_mgmt_interface") | String |  |  |  | Pointer to interface used for inband management.<br>All configuration must be done using other data models like network services or structured_config.<br>'inband_mgmt_interface' is only used to refer to this interface as source in various management protocol settings (future feature).<br><br>On L2 switches, this defaults to Vlan<inband_mgmt_vlan> if either 'inband_mgmt_subnet' or 'inband_mgmt_ip' is set.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_vlan</samp>](## "<node_type_keys.key>.node_groups.[].inband_mgmt_vlan") | Integer |  | `4092` |  | VLAN number used for inband management on L2 switches (switches using port-channel trunks as uplinks).<br>When using 'inband_mgmt_subnet' the VLAN and SVIs will be created automatically on this switch as well as all 'uplink_switches'.<br>When using 'inband_mgmt_ip' the VLAN and SVI will only be created on this device and added to uplink trunk. The VLAN and SVI on the parent switches must be created using network services data models. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_subnet</samp>](## "<node_type_keys.key>.node_groups.[].inband_mgmt_subnet") | String |  |  | Format: ipv4_cidr | Optional IP subnet assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).<br>Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP.<br>This allows all l3leafs to reuse the same subnet across multiple racks without VXLAN extension.<br>SVI IP address will be assigned as follows:<br>virtual-router: <subnet> + 1<br>l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)<br>l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)<br>l2leafs       : <subnet> + 3 + <l2leaf id><br>GW on l2leafs : <subnet> + 1<br>Assign range larger than total l2leafs + 5<br><br>Setting is ignored if 'inband_mgmt_ip' is set.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_ip</samp>](## "<node_type_keys.key>.node_groups.[].inband_mgmt_ip") | String |  |  | Format: ipv4_cidr | IP address assigned to the inband management interface set with 'inband_mgmt_vlan'.<br>This overrides 'inband_mgmt_subnet', hence all behavior of 'inband_mgmt_subnet' is removed.<br><br>If this is set the VLAN and SVI will only be created on the L2 switch and added to uplink trunk.<br>The VLAN and SVI on the parent switches must be created using network services data models.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_gateway</samp>](## "<node_type_keys.key>.node_groups.[].inband_mgmt_gateway") | String |  |  | Format: ipv4 | Default gateway configured in the 'inband_mgmt_vrf' when using 'inband_mgmt_ip'. Otherwise gateway is derived from 'inband_mgmt_subnet' if set.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_ipv6_address</samp>](## "<node_type_keys.key>.node_groups.[].inband_mgmt_ipv6_address") | String |  |  | Format: ipv6 | IPv6 address assigned to the inband management interface set with 'inband_mgmt_vlan'.<br>This overrides 'inband_mgmt_ipv6_subnet', hence the configuration of 'inband_mgmt_ipv6_subnet' is ignored.<br><br>If this is set the VLAN and SVI will only be created on the L2 switch and added to uplink trunk.<br>The VLAN and SVI on the parent switches must be created using network services data models.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_ipv6_subnet</samp>](## "<node_type_keys.key>.node_groups.[].inband_mgmt_ipv6_subnet") | String |  |  | Format: ipv6_cidr | Optional IPv6 prefix assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).<br>Parent l3leafs will have SVI with "ipv6 virtual-router" and host-route injection based on ARP.<br>This allows all l3leafs to reuse the same subnet across multiple racks without VXLAN extension.<br>SVI IP address will be assigned as follows:<br>virtual-router: <subnet> + 1<br>l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)<br>l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)<br>l2leafs       : <subnet> + 3 + <l2leaf id><br>GW on l2leafs : <subnet> + 1<br>Assign range larger than total l2leafs + 5<br><br>Setting is ignored if 'inband_mgmt_ipv6_address' is set.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_ipv6_gateway</samp>](## "<node_type_keys.key>.node_groups.[].inband_mgmt_ipv6_gateway") | String |  |  | Format: ipv6 | Default gateway configured in the 'inband_mgmt_vrf'.<br>Used when `inband_mgmt_ipv6_address` is set.<br>Ignored when 'inband_mgmt_ipv6_subnet' is set (first IP in subnet used as gateway).<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_description</samp>](## "<node_type_keys.key>.node_groups.[].inband_mgmt_description") | String |  | `Inband Management` |  | Description configured on the Inband Management SVI.<br><br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_vlan_name</samp>](## "<node_type_keys.key>.node_groups.[].inband_mgmt_vlan_name") | String |  | `INBAND_MGMT` |  | Name configured on the Inband Management VLAN.<br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_vrf</samp>](## "<node_type_keys.key>.node_groups.[].inband_mgmt_vrf") | String |  | `default` |  | VRF configured on the Inband Management Interface.<br>The VRF is created if not already created by other means.<br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_mtu</samp>](## "<node_type_keys.key>.node_groups.[].inband_mgmt_mtu") | Integer |  | `1500` |  | MTU configured on the Inband Management Interface.<br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_ztp</samp>](## "<node_type_keys.key>.node_groups.[].inband_ztp") | Boolean |  | `False` |  | Enable to configure upstream device with proper configuration to allow downstream devices to be Zero-Touch-Provisioned over the uplink interfaces.<br>For L2 devices this setting also requires that the `inband_mgmt_vlan` is set for the node.<br><br>PREVIEW: Support for L3 devices is marked as "preview", meaning the data models or generated configuration can change at any time. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_ztp_lacp_fallback_delay</samp>](## "<node_type_keys.key>.node_groups.[].inband_ztp_lacp_fallback_delay") | Integer |  | `30` | Min: 0<br>Max: 300 | Set the LACP fallback timeout of the upstream device's port-channel towards the downstream inband ZTP node.<br>This setting also requires that `inband_ztp` is set for the node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_management_subnet</samp>](## "<node_type_keys.key>.node_groups.[].inband_management_subnet") <span style="color:red">removed</span> | String |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>inband_mgmt_subnet</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_management_vlan</samp>](## "<node_type_keys.key>.node_groups.[].inband_management_vlan") <span style="color:red">removed</span> | Integer |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>inband_mgmt_vlan</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_interface</samp>](## "<node_type_keys.key>.nodes.[].inband_mgmt_interface") | String |  |  |  | Pointer to interface used for inband management.<br>All configuration must be done using other data models like network services or structured_config.<br>'inband_mgmt_interface' is only used to refer to this interface as source in various management protocol settings (future feature).<br><br>On L2 switches, this defaults to Vlan<inband_mgmt_vlan> if either 'inband_mgmt_subnet' or 'inband_mgmt_ip' is set.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_vlan</samp>](## "<node_type_keys.key>.nodes.[].inband_mgmt_vlan") | Integer |  | `4092` |  | VLAN number used for inband management on L2 switches (switches using port-channel trunks as uplinks).<br>When using 'inband_mgmt_subnet' the VLAN and SVIs will be created automatically on this switch as well as all 'uplink_switches'.<br>When using 'inband_mgmt_ip' the VLAN and SVI will only be created on this device and added to uplink trunk. The VLAN and SVI on the parent switches must be created using network services data models. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_subnet</samp>](## "<node_type_keys.key>.nodes.[].inband_mgmt_subnet") | String |  |  | Format: ipv4_cidr | Optional IP subnet assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).<br>Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP.<br>This allows all l3leafs to reuse the same subnet across multiple racks without VXLAN extension.<br>SVI IP address will be assigned as follows:<br>virtual-router: <subnet> + 1<br>l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)<br>l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)<br>l2leafs       : <subnet> + 3 + <l2leaf id><br>GW on l2leafs : <subnet> + 1<br>Assign range larger than total l2leafs + 5<br><br>Setting is ignored if 'inband_mgmt_ip' is set.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_ip</samp>](## "<node_type_keys.key>.nodes.[].inband_mgmt_ip") | String |  |  | Format: ipv4_cidr | IP address assigned to the inband management interface set with 'inband_mgmt_vlan'.<br>This overrides 'inband_mgmt_subnet', hence all behavior of 'inband_mgmt_subnet' is removed.<br><br>If this is set the VLAN and SVI will only be created on the L2 switch and added to uplink trunk.<br>The VLAN and SVI on the parent switches must be created using network services data models.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_gateway</samp>](## "<node_type_keys.key>.nodes.[].inband_mgmt_gateway") | String |  |  | Format: ipv4 | Default gateway configured in the 'inband_mgmt_vrf' when using 'inband_mgmt_ip'. Otherwise gateway is derived from 'inband_mgmt_subnet' if set.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_ipv6_address</samp>](## "<node_type_keys.key>.nodes.[].inband_mgmt_ipv6_address") | String |  |  | Format: ipv6 | IPv6 address assigned to the inband management interface set with 'inband_mgmt_vlan'.<br>This overrides 'inband_mgmt_ipv6_subnet', hence the configuration of 'inband_mgmt_ipv6_subnet' is ignored.<br><br>If this is set the VLAN and SVI will only be created on the L2 switch and added to uplink trunk.<br>The VLAN and SVI on the parent switches must be created using network services data models.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_ipv6_subnet</samp>](## "<node_type_keys.key>.nodes.[].inband_mgmt_ipv6_subnet") | String |  |  | Format: ipv6_cidr | Optional IPv6 prefix assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).<br>Parent l3leafs will have SVI with "ipv6 virtual-router" and host-route injection based on ARP.<br>This allows all l3leafs to reuse the same subnet across multiple racks without VXLAN extension.<br>SVI IP address will be assigned as follows:<br>virtual-router: <subnet> + 1<br>l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)<br>l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)<br>l2leafs       : <subnet> + 3 + <l2leaf id><br>GW on l2leafs : <subnet> + 1<br>Assign range larger than total l2leafs + 5<br><br>Setting is ignored if 'inband_mgmt_ipv6_address' is set.<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_ipv6_gateway</samp>](## "<node_type_keys.key>.nodes.[].inband_mgmt_ipv6_gateway") | String |  |  | Format: ipv6 | Default gateway configured in the 'inband_mgmt_vrf'.<br>Used when `inband_mgmt_ipv6_address` is set.<br>Ignored when 'inband_mgmt_ipv6_subnet' is set (first IP in subnet used as gateway).<br><br>This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_description</samp>](## "<node_type_keys.key>.nodes.[].inband_mgmt_description") | String |  | `Inband Management` |  | Description configured on the Inband Management SVI.<br><br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_vlan_name</samp>](## "<node_type_keys.key>.nodes.[].inband_mgmt_vlan_name") | String |  | `INBAND_MGMT` |  | Name configured on the Inband Management VLAN.<br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_vrf</samp>](## "<node_type_keys.key>.nodes.[].inband_mgmt_vrf") | String |  | `default` |  | VRF configured on the Inband Management Interface.<br>The VRF is created if not already created by other means.<br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_mgmt_mtu</samp>](## "<node_type_keys.key>.nodes.[].inband_mgmt_mtu") | Integer |  | `1500` |  | MTU configured on the Inband Management Interface.<br>This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_ztp</samp>](## "<node_type_keys.key>.nodes.[].inband_ztp") | Boolean |  | `False` |  | Enable to configure upstream device with proper configuration to allow downstream devices to be Zero-Touch-Provisioned over the uplink interfaces.<br>For L2 devices this setting also requires that the `inband_mgmt_vlan` is set for the node.<br><br>PREVIEW: Support for L3 devices is marked as "preview", meaning the data models or generated configuration can change at any time. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_ztp_lacp_fallback_delay</samp>](## "<node_type_keys.key>.nodes.[].inband_ztp_lacp_fallback_delay") | Integer |  | `30` | Min: 0<br>Max: 300 | Set the LACP fallback timeout of the upstream device's port-channel towards the downstream inband ZTP node.<br>This setting also requires that `inband_ztp` is set for the node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_management_subnet</samp>](## "<node_type_keys.key>.nodes.[].inband_management_subnet") <span style="color:red">removed</span> | String |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>inband_mgmt_subnet</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;inband_management_vlan</samp>](## "<node_type_keys.key>.nodes.[].inband_management_vlan") <span style="color:red">removed</span> | Integer |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>inband_mgmt_vlan</samp> instead.</span> |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:

        # Pointer to interface used for inband management.
        # All configuration must be done using other data models like network services or structured_config.
        # 'inband_mgmt_interface' is only used to refer to this interface as source in various management protocol settings (future feature).
        #
        # On L2 switches, this defaults to Vlan<inband_mgmt_vlan> if either 'inband_mgmt_subnet' or 'inband_mgmt_ip' is set.
        inband_mgmt_interface: <str>

        # VLAN number used for inband management on L2 switches (switches using port-channel trunks as uplinks).
        # When using 'inband_mgmt_subnet' the VLAN and SVIs will be created automatically on this switch as well as all 'uplink_switches'.
        # When using 'inband_mgmt_ip' the VLAN and SVI will only be created on this device and added to uplink trunk. The VLAN and SVI on the parent switches must be created using network services data models.
        inband_mgmt_vlan: <int; default=4092>

        # Optional IP subnet assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).
        # Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP.
        # This allows all l3leafs to reuse the same subnet across multiple racks without VXLAN extension.
        # SVI IP address will be assigned as follows:
        # virtual-router: <subnet> + 1
        # l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)
        # l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)
        # l2leafs       : <subnet> + 3 + <l2leaf id>
        # GW on l2leafs : <subnet> + 1
        # Assign range larger than total l2leafs + 5
        #
        # Setting is ignored if 'inband_mgmt_ip' is set.
        #
        # This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
        inband_mgmt_subnet: <str>

        # IP address assigned to the inband management interface set with 'inband_mgmt_vlan'.
        # This overrides 'inband_mgmt_subnet', hence all behavior of 'inband_mgmt_subnet' is removed.
        #
        # If this is set the VLAN and SVI will only be created on the L2 switch and added to uplink trunk.
        # The VLAN and SVI on the parent switches must be created using network services data models.
        #
        # This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
        inband_mgmt_ip: <str>

        # Default gateway configured in the 'inband_mgmt_vrf' when using 'inband_mgmt_ip'. Otherwise gateway is derived from 'inband_mgmt_subnet' if set.
        #
        # This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
        inband_mgmt_gateway: <str>

        # IPv6 address assigned to the inband management interface set with 'inband_mgmt_vlan'.
        # This overrides 'inband_mgmt_ipv6_subnet', hence the configuration of 'inband_mgmt_ipv6_subnet' is ignored.
        #
        # If this is set the VLAN and SVI will only be created on the L2 switch and added to uplink trunk.
        # The VLAN and SVI on the parent switches must be created using network services data models.
        #
        # This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
        inband_mgmt_ipv6_address: <str>

        # Optional IPv6 prefix assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).
        # Parent l3leafs will have SVI with "ipv6 virtual-router" and host-route injection based on ARP.
        # This allows all l3leafs to reuse the same subnet across multiple racks without VXLAN extension.
        # SVI IP address will be assigned as follows:
        # virtual-router: <subnet> + 1
        # l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)
        # l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)
        # l2leafs       : <subnet> + 3 + <l2leaf id>
        # GW on l2leafs : <subnet> + 1
        # Assign range larger than total l2leafs + 5
        #
        # Setting is ignored if 'inband_mgmt_ipv6_address' is set.
        #
        # This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
        inband_mgmt_ipv6_subnet: <str>

        # Default gateway configured in the 'inband_mgmt_vrf'.
        # Used when `inband_mgmt_ipv6_address` is set.
        # Ignored when 'inband_mgmt_ipv6_subnet' is set (first IP in subnet used as gateway).
        #
        # This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
        inband_mgmt_ipv6_gateway: <str>

        # Description configured on the Inband Management SVI.
        #
        # This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed.
        inband_mgmt_description: <str; default="Inband Management">

        # Name configured on the Inband Management VLAN.
        # This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed.
        inband_mgmt_vlan_name: <str; default="INBAND_MGMT">

        # VRF configured on the Inband Management Interface.
        # The VRF is created if not already created by other means.
        # This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed.
        inband_mgmt_vrf: <str; default="default">

        # MTU configured on the Inband Management Interface.
        # This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed.
        inband_mgmt_mtu: <int; default=1500>

        # Enable to configure upstream device with proper configuration to allow downstream devices to be Zero-Touch-Provisioned over the uplink interfaces.
        # For L2 devices this setting also requires that the `inband_mgmt_vlan` is set for the node.
        #
        # PREVIEW: Support for L3 devices is marked as "preview", meaning the data models or generated configuration can change at any time.
        inband_ztp: <bool; default=False>

        # Set the LACP fallback timeout of the upstream device's port-channel towards the downstream inband ZTP node.
        # This setting also requires that `inband_ztp` is set for the node.
        inband_ztp_lacp_fallback_delay: <int; 0-300; default=30>

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>

              # Pointer to interface used for inband management.
              # All configuration must be done using other data models like network services or structured_config.
              # 'inband_mgmt_interface' is only used to refer to this interface as source in various management protocol settings (future feature).
              #
              # On L2 switches, this defaults to Vlan<inband_mgmt_vlan> if either 'inband_mgmt_subnet' or 'inband_mgmt_ip' is set.
              inband_mgmt_interface: <str>

              # VLAN number used for inband management on L2 switches (switches using port-channel trunks as uplinks).
              # When using 'inband_mgmt_subnet' the VLAN and SVIs will be created automatically on this switch as well as all 'uplink_switches'.
              # When using 'inband_mgmt_ip' the VLAN and SVI will only be created on this device and added to uplink trunk. The VLAN and SVI on the parent switches must be created using network services data models.
              inband_mgmt_vlan: <int; default=4092>

              # Optional IP subnet assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).
              # Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP.
              # This allows all l3leafs to reuse the same subnet across multiple racks without VXLAN extension.
              # SVI IP address will be assigned as follows:
              # virtual-router: <subnet> + 1
              # l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)
              # l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)
              # l2leafs       : <subnet> + 3 + <l2leaf id>
              # GW on l2leafs : <subnet> + 1
              # Assign range larger than total l2leafs + 5
              #
              # Setting is ignored if 'inband_mgmt_ip' is set.
              #
              # This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
              inband_mgmt_subnet: <str>

              # IP address assigned to the inband management interface set with 'inband_mgmt_vlan'.
              # This overrides 'inband_mgmt_subnet', hence all behavior of 'inband_mgmt_subnet' is removed.
              #
              # If this is set the VLAN and SVI will only be created on the L2 switch and added to uplink trunk.
              # The VLAN and SVI on the parent switches must be created using network services data models.
              #
              # This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
              inband_mgmt_ip: <str>

              # Default gateway configured in the 'inband_mgmt_vrf' when using 'inband_mgmt_ip'. Otherwise gateway is derived from 'inband_mgmt_subnet' if set.
              #
              # This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
              inband_mgmt_gateway: <str>

              # IPv6 address assigned to the inband management interface set with 'inband_mgmt_vlan'.
              # This overrides 'inband_mgmt_ipv6_subnet', hence the configuration of 'inband_mgmt_ipv6_subnet' is ignored.
              #
              # If this is set the VLAN and SVI will only be created on the L2 switch and added to uplink trunk.
              # The VLAN and SVI on the parent switches must be created using network services data models.
              #
              # This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
              inband_mgmt_ipv6_address: <str>

              # Optional IPv6 prefix assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).
              # Parent l3leafs will have SVI with "ipv6 virtual-router" and host-route injection based on ARP.
              # This allows all l3leafs to reuse the same subnet across multiple racks without VXLAN extension.
              # SVI IP address will be assigned as follows:
              # virtual-router: <subnet> + 1
              # l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)
              # l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)
              # l2leafs       : <subnet> + 3 + <l2leaf id>
              # GW on l2leafs : <subnet> + 1
              # Assign range larger than total l2leafs + 5
              #
              # Setting is ignored if 'inband_mgmt_ipv6_address' is set.
              #
              # This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
              inband_mgmt_ipv6_subnet: <str>

              # Default gateway configured in the 'inband_mgmt_vrf'.
              # Used when `inband_mgmt_ipv6_address` is set.
              # Ignored when 'inband_mgmt_ipv6_subnet' is set (first IP in subnet used as gateway).
              #
              # This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
              inband_mgmt_ipv6_gateway: <str>

              # Description configured on the Inband Management SVI.
              #
              # This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed.
              inband_mgmt_description: <str; default="Inband Management">

              # Name configured on the Inband Management VLAN.
              # This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed.
              inband_mgmt_vlan_name: <str; default="INBAND_MGMT">

              # VRF configured on the Inband Management Interface.
              # The VRF is created if not already created by other means.
              # This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed.
              inband_mgmt_vrf: <str; default="default">

              # MTU configured on the Inband Management Interface.
              # This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed.
              inband_mgmt_mtu: <int; default=1500>

              # Enable to configure upstream device with proper configuration to allow downstream devices to be Zero-Touch-Provisioned over the uplink interfaces.
              # For L2 devices this setting also requires that the `inband_mgmt_vlan` is set for the node.
              #
              # PREVIEW: Support for L3 devices is marked as "preview", meaning the data models or generated configuration can change at any time.
              inband_ztp: <bool; default=False>

              # Set the LACP fallback timeout of the upstream device's port-channel towards the downstream inband ZTP node.
              # This setting also requires that `inband_ztp` is set for the node.
              inband_ztp_lacp_fallback_delay: <int; 0-300; default=30>

          # Pointer to interface used for inband management.
          # All configuration must be done using other data models like network services or structured_config.
          # 'inband_mgmt_interface' is only used to refer to this interface as source in various management protocol settings (future feature).
          #
          # On L2 switches, this defaults to Vlan<inband_mgmt_vlan> if either 'inband_mgmt_subnet' or 'inband_mgmt_ip' is set.
          inband_mgmt_interface: <str>

          # VLAN number used for inband management on L2 switches (switches using port-channel trunks as uplinks).
          # When using 'inband_mgmt_subnet' the VLAN and SVIs will be created automatically on this switch as well as all 'uplink_switches'.
          # When using 'inband_mgmt_ip' the VLAN and SVI will only be created on this device and added to uplink trunk. The VLAN and SVI on the parent switches must be created using network services data models.
          inband_mgmt_vlan: <int; default=4092>

          # Optional IP subnet assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).
          # Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP.
          # This allows all l3leafs to reuse the same subnet across multiple racks without VXLAN extension.
          # SVI IP address will be assigned as follows:
          # virtual-router: <subnet> + 1
          # l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)
          # l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)
          # l2leafs       : <subnet> + 3 + <l2leaf id>
          # GW on l2leafs : <subnet> + 1
          # Assign range larger than total l2leafs + 5
          #
          # Setting is ignored if 'inband_mgmt_ip' is set.
          #
          # This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
          inband_mgmt_subnet: <str>

          # IP address assigned to the inband management interface set with 'inband_mgmt_vlan'.
          # This overrides 'inband_mgmt_subnet', hence all behavior of 'inband_mgmt_subnet' is removed.
          #
          # If this is set the VLAN and SVI will only be created on the L2 switch and added to uplink trunk.
          # The VLAN and SVI on the parent switches must be created using network services data models.
          #
          # This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
          inband_mgmt_ip: <str>

          # Default gateway configured in the 'inband_mgmt_vrf' when using 'inband_mgmt_ip'. Otherwise gateway is derived from 'inband_mgmt_subnet' if set.
          #
          # This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
          inband_mgmt_gateway: <str>

          # IPv6 address assigned to the inband management interface set with 'inband_mgmt_vlan'.
          # This overrides 'inband_mgmt_ipv6_subnet', hence the configuration of 'inband_mgmt_ipv6_subnet' is ignored.
          #
          # If this is set the VLAN and SVI will only be created on the L2 switch and added to uplink trunk.
          # The VLAN and SVI on the parent switches must be created using network services data models.
          #
          # This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
          inband_mgmt_ipv6_address: <str>

          # Optional IPv6 prefix assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).
          # Parent l3leafs will have SVI with "ipv6 virtual-router" and host-route injection based on ARP.
          # This allows all l3leafs to reuse the same subnet across multiple racks without VXLAN extension.
          # SVI IP address will be assigned as follows:
          # virtual-router: <subnet> + 1
          # l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)
          # l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)
          # l2leafs       : <subnet> + 3 + <l2leaf id>
          # GW on l2leafs : <subnet> + 1
          # Assign range larger than total l2leafs + 5
          #
          # Setting is ignored if 'inband_mgmt_ipv6_address' is set.
          #
          # This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
          inband_mgmt_ipv6_subnet: <str>

          # Default gateway configured in the 'inband_mgmt_vrf'.
          # Used when `inband_mgmt_ipv6_address` is set.
          # Ignored when 'inband_mgmt_ipv6_subnet' is set (first IP in subnet used as gateway).
          #
          # This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
          inband_mgmt_ipv6_gateway: <str>

          # Description configured on the Inband Management SVI.
          #
          # This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed.
          inband_mgmt_description: <str; default="Inband Management">

          # Name configured on the Inband Management VLAN.
          # This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed.
          inband_mgmt_vlan_name: <str; default="INBAND_MGMT">

          # VRF configured on the Inband Management Interface.
          # The VRF is created if not already created by other means.
          # This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed.
          inband_mgmt_vrf: <str; default="default">

          # MTU configured on the Inband Management Interface.
          # This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed.
          inband_mgmt_mtu: <int; default=1500>

          # Enable to configure upstream device with proper configuration to allow downstream devices to be Zero-Touch-Provisioned over the uplink interfaces.
          # For L2 devices this setting also requires that the `inband_mgmt_vlan` is set for the node.
          #
          # PREVIEW: Support for L3 devices is marked as "preview", meaning the data models or generated configuration can change at any time.
          inband_ztp: <bool; default=False>

          # Set the LACP fallback timeout of the upstream device's port-channel towards the downstream inband ZTP node.
          # This setting also requires that `inband_ztp` is set for the node.
          inband_ztp_lacp_fallback_delay: <int; 0-300; default=30>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>

          # Pointer to interface used for inband management.
          # All configuration must be done using other data models like network services or structured_config.
          # 'inband_mgmt_interface' is only used to refer to this interface as source in various management protocol settings (future feature).
          #
          # On L2 switches, this defaults to Vlan<inband_mgmt_vlan> if either 'inband_mgmt_subnet' or 'inband_mgmt_ip' is set.
          inband_mgmt_interface: <str>

          # VLAN number used for inband management on L2 switches (switches using port-channel trunks as uplinks).
          # When using 'inband_mgmt_subnet' the VLAN and SVIs will be created automatically on this switch as well as all 'uplink_switches'.
          # When using 'inband_mgmt_ip' the VLAN and SVI will only be created on this device and added to uplink trunk. The VLAN and SVI on the parent switches must be created using network services data models.
          inband_mgmt_vlan: <int; default=4092>

          # Optional IP subnet assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).
          # Parent l3leafs will have SVI with "ip virtual-router" and host-route injection based on ARP.
          # This allows all l3leafs to reuse the same subnet across multiple racks without VXLAN extension.
          # SVI IP address will be assigned as follows:
          # virtual-router: <subnet> + 1
          # l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)
          # l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)
          # l2leafs       : <subnet> + 3 + <l2leaf id>
          # GW on l2leafs : <subnet> + 1
          # Assign range larger than total l2leafs + 5
          #
          # Setting is ignored if 'inband_mgmt_ip' is set.
          #
          # This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
          inband_mgmt_subnet: <str>

          # IP address assigned to the inband management interface set with 'inband_mgmt_vlan'.
          # This overrides 'inband_mgmt_subnet', hence all behavior of 'inband_mgmt_subnet' is removed.
          #
          # If this is set the VLAN and SVI will only be created on the L2 switch and added to uplink trunk.
          # The VLAN and SVI on the parent switches must be created using network services data models.
          #
          # This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
          inband_mgmt_ip: <str>

          # Default gateway configured in the 'inband_mgmt_vrf' when using 'inband_mgmt_ip'. Otherwise gateway is derived from 'inband_mgmt_subnet' if set.
          #
          # This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
          inband_mgmt_gateway: <str>

          # IPv6 address assigned to the inband management interface set with 'inband_mgmt_vlan'.
          # This overrides 'inband_mgmt_ipv6_subnet', hence the configuration of 'inband_mgmt_ipv6_subnet' is ignored.
          #
          # If this is set the VLAN and SVI will only be created on the L2 switch and added to uplink trunk.
          # The VLAN and SVI on the parent switches must be created using network services data models.
          #
          # This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
          inband_mgmt_ipv6_address: <str>

          # Optional IPv6 prefix assigned to inband management SVIs on L2 switches (switches using port-channels as uplinks).
          # Parent l3leafs will have SVI with "ipv6 virtual-router" and host-route injection based on ARP.
          # This allows all l3leafs to reuse the same subnet across multiple racks without VXLAN extension.
          # SVI IP address will be assigned as follows:
          # virtual-router: <subnet> + 1
          # l3leaf A      : <subnet> + 2 (same IP on all l3leaf A)
          # l3leaf B      : <subnet> + 3 (same IP on all l3leaf B)
          # l2leafs       : <subnet> + 3 + <l2leaf id>
          # GW on l2leafs : <subnet> + 1
          # Assign range larger than total l2leafs + 5
          #
          # Setting is ignored if 'inband_mgmt_ipv6_address' is set.
          #
          # This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
          inband_mgmt_ipv6_subnet: <str>

          # Default gateway configured in the 'inband_mgmt_vrf'.
          # Used when `inband_mgmt_ipv6_address` is set.
          # Ignored when 'inband_mgmt_ipv6_subnet' is set (first IP in subnet used as gateway).
          #
          # This setting is applicable to L2 switches (switches using port-channel trunks as uplinks).
          inband_mgmt_ipv6_gateway: <str>

          # Description configured on the Inband Management SVI.
          #
          # This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed.
          inband_mgmt_description: <str; default="Inband Management">

          # Name configured on the Inband Management VLAN.
          # This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed.
          inband_mgmt_vlan_name: <str; default="INBAND_MGMT">

          # VRF configured on the Inband Management Interface.
          # The VRF is created if not already created by other means.
          # This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed.
          inband_mgmt_vrf: <str; default="default">

          # MTU configured on the Inband Management Interface.
          # This setting is only applied on the devices where it is set, it does not automatically affect any parent/child devices configuration, so it must be set on each applicable node/node-group/node-type as needed.
          inband_mgmt_mtu: <int; default=1500>

          # Enable to configure upstream device with proper configuration to allow downstream devices to be Zero-Touch-Provisioned over the uplink interfaces.
          # For L2 devices this setting also requires that the `inband_mgmt_vlan` is set for the node.
          #
          # PREVIEW: Support for L3 devices is marked as "preview", meaning the data models or generated configuration can change at any time.
          inband_ztp: <bool; default=False>

          # Set the LACP fallback timeout of the upstream device's port-channel towards the downstream inband ZTP node.
          # This setting also requires that `inband_ztp` is set for the node.
          inband_ztp_lacp_fallback_delay: <int; 0-300; default=30>
    ```
