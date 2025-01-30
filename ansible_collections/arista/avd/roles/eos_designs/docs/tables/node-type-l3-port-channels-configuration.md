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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l3_port_channels</samp>](## "<node_type_keys.key>.defaults.l3_port_channels") | List, items: Dictionary |  |  |  | L3 Port-Channel interfaces to configure on the node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].name") | String | Required, Unique |  | Pattern: `Port-Channel[\d/]+(\.[\d]+)?` | Port-Channel interface name like 'Port-Channel2' or subinterface name like 'Port-Channel2.42'.<br>For a Port-Channel subinterface, the parent Port-Channel interface must be defined as well. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].description") | String |  |  |  | Interface description.<br>If not set, a default description will be configured with '[<peer>[ <peer_port_channel>]]'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].mode") | String |  | `active` | Valid Values:<br>- <code>active</code><br>- <code>passive</code><br>- <code>on</code> | Port-Channel mode.<br>Should not be set on Port-Channel subinterfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;member_interfaces</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].member_interfaces") | List, items: Dictionary |  |  |  | Port-Channel member interfaces.<br>Should not be set on Port-Channel subinterfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].member_interfaces.[].name") | String | Required, Unique |  | Pattern: `Ethernet[\d/]+` | Ethernet interface name like 'Ethernet2'.<br>Member interface cannot be subinterface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].member_interfaces.[].description") | String |  |  |  | Interface description for this member.<br>If not set, a default description will be configured with '[<peer>[ <peer_interface>]]'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].member_interfaces.[].peer") | String |  |  |  | The peer device name. Used for description and documentation.<br>If not set, this inherits the peer setting on the port-channel interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_interface</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].member_interfaces.[].peer_interface") | String |  |  |  | The peer device interface. Used for description and documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].member_interfaces.[].speed") | String |  |  |  | Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].member_interfaces.[].structured_config") | Dictionary |  |  |  | Custom structured config for the member ethernet interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].ip_address") | String |  |  |  | Node IPv4 address/Mask or 'dhcp'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dhcp_ip</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].dhcp_ip") | String |  |  |  | When the `ip_address` is `dhcp`, this optional field allows to indicate the expected<br>IPv4 address (without mask) to be allocated on the interface if known.<br>This is not rendered in the configuration but can be used for substitution of 'interface_ip' in the Access-list<br>set under `ipv4_acl_in` and `ipv4_acl_out`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;public_ip</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].public_ip") | String |  |  |  | Node IPv4 address (no mask).<br><br>This is used to get the public IP (if known) when the device is behind NAT.<br>This is only used for `wan_rr` routers (AutoVPN RRs and Pathfinders) to determine the Public IP<br>with the following preference:<br>  `wan_route_servers.path_groups.interfaces.ip_address`<br>      -> `l3_port_channels.public_ip`<br>          -> `l3_port_channels.ip_address`<br><br>The determined Public IP is used by WAN routers when peering with this interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].encapsulation_dot1q_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dhcp_accept_default_route</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].dhcp_accept_default_route") | Boolean |  | `True` |  | Accept a default route from DHCP if `ip_address` is set to `dhcp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].enabled") | Boolean |  | `True` |  | Enable or Shutdown the interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].peer") | String |  |  |  | The peer device name. Used for description and documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_port_channel</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].peer_port_channel") | String |  |  |  | The peer device port-channel interface. Used for description and documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_ip</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].peer_ip") | String |  |  |  | The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].bgp") | Dictionary |  |  |  | Enforce IPv4 BGP peering for the peer |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_as</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].bgp.peer_as") | String | Required |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_prefix_list_in</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].bgp.ipv4_prefix_list_in") | String |  |  |  | Prefix List Name. Accept routes for only these prefixes from the peer.<br>Required for wan interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_prefix_list_out</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].bgp.ipv4_prefix_list_out") | String |  |  |  | Prefix List Name. Advertise routes for only these prefixes.<br>If not specified, nothing would be advertised. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_in</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].ipv4_acl_in") | String |  |  |  | Name of the IPv4 access-list to be assigned in the ingress direction.<br>The access-list must be defined under `ipv4_acls` and supports field substitution for "interface_ip" and "peer_ip".<br>Required for all WAN interfaces (`wan_carrier` is set) unless the carrier is marked as 'trusted' under `wan_carriers`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_out</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].ipv4_acl_out") | String |  |  |  | Name of the IPv4 Access-list to be assigned in the egress direction.<br>The access-list must be defined under `ipv4_acls` and supports field substitution for "interface_ip" and "peer_ip". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static_routes</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].static_routes") | List, items: Dictionary |  |  | Min Length: 1 | Configure IPv4 static routes pointing to `peer_ip`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].static_routes.[].prefix") | String | Required, Unique |  |  | IPv4_network/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].qos_profile") | String |  |  |  | QOS service profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_carrier</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].wan_carrier") | String |  |  |  | The WAN carrier this interface is connected to.<br>This is used to infer the path-groups in which this interface should be configured.<br>Unless the carrier is marked as 'trusted' under `wan_carriers`, `ipv4_acl_in` is also required on all WAN interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_circuit_id</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].wan_circuit_id") | String |  |  |  | The WAN circuit ID for this interface.<br>This is not rendered in the configuration but used for WAN designs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected_to_pathfinder</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].connected_to_pathfinder") | Boolean |  | `True` |  | For a WAN interface (`wan_carrier` is set), allow to disable the static tunnel towards Pathfinders. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the Port-Channel interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flow_tracking</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].flow_tracking") | Dictionary |  |  |  | Configures flow-tracking on the interface. Overrides `fabric_flow_tracking.l3_port_channels` setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].flow_tracking.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].flow_tracking.name") | String |  |  |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<node_type_keys.key>.defaults.l3_port_channels.[].structured_config") | Dictionary |  |  |  | Custom structured config for the Port-Channel interface. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l3_port_channels</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels") | List, items: Dictionary |  |  |  | L3 Port-Channel interfaces to configure on the node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].name") | String | Required, Unique |  | Pattern: `Port-Channel[\d/]+(\.[\d]+)?` | Port-Channel interface name like 'Port-Channel2' or subinterface name like 'Port-Channel2.42'.<br>For a Port-Channel subinterface, the parent Port-Channel interface must be defined as well. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].description") | String |  |  |  | Interface description.<br>If not set, a default description will be configured with '[<peer>[ <peer_port_channel>]]'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].mode") | String |  | `active` | Valid Values:<br>- <code>active</code><br>- <code>passive</code><br>- <code>on</code> | Port-Channel mode.<br>Should not be set on Port-Channel subinterfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;member_interfaces</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].member_interfaces") | List, items: Dictionary |  |  |  | Port-Channel member interfaces.<br>Should not be set on Port-Channel subinterfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].member_interfaces.[].name") | String | Required, Unique |  | Pattern: `Ethernet[\d/]+` | Ethernet interface name like 'Ethernet2'.<br>Member interface cannot be subinterface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].member_interfaces.[].description") | String |  |  |  | Interface description for this member.<br>If not set, a default description will be configured with '[<peer>[ <peer_interface>]]'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].member_interfaces.[].peer") | String |  |  |  | The peer device name. Used for description and documentation.<br>If not set, this inherits the peer setting on the port-channel interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_interface</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].member_interfaces.[].peer_interface") | String |  |  |  | The peer device interface. Used for description and documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].member_interfaces.[].speed") | String |  |  |  | Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].member_interfaces.[].structured_config") | Dictionary |  |  |  | Custom structured config for the member ethernet interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].ip_address") | String |  |  |  | Node IPv4 address/Mask or 'dhcp'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dhcp_ip</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].dhcp_ip") | String |  |  |  | When the `ip_address` is `dhcp`, this optional field allows to indicate the expected<br>IPv4 address (without mask) to be allocated on the interface if known.<br>This is not rendered in the configuration but can be used for substitution of 'interface_ip' in the Access-list<br>set under `ipv4_acl_in` and `ipv4_acl_out`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;public_ip</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].public_ip") | String |  |  |  | Node IPv4 address (no mask).<br><br>This is used to get the public IP (if known) when the device is behind NAT.<br>This is only used for `wan_rr` routers (AutoVPN RRs and Pathfinders) to determine the Public IP<br>with the following preference:<br>  `wan_route_servers.path_groups.interfaces.ip_address`<br>      -> `l3_port_channels.public_ip`<br>          -> `l3_port_channels.ip_address`<br><br>The determined Public IP is used by WAN routers when peering with this interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].encapsulation_dot1q_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dhcp_accept_default_route</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].dhcp_accept_default_route") | Boolean |  | `True` |  | Accept a default route from DHCP if `ip_address` is set to `dhcp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].enabled") | Boolean |  | `True` |  | Enable or Shutdown the interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].peer") | String |  |  |  | The peer device name. Used for description and documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_port_channel</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].peer_port_channel") | String |  |  |  | The peer device port-channel interface. Used for description and documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_ip</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].peer_ip") | String |  |  |  | The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].bgp") | Dictionary |  |  |  | Enforce IPv4 BGP peering for the peer |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_as</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].bgp.peer_as") | String | Required |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_prefix_list_in</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].bgp.ipv4_prefix_list_in") | String |  |  |  | Prefix List Name. Accept routes for only these prefixes from the peer.<br>Required for wan interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_prefix_list_out</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].bgp.ipv4_prefix_list_out") | String |  |  |  | Prefix List Name. Advertise routes for only these prefixes.<br>If not specified, nothing would be advertised. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_in</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].ipv4_acl_in") | String |  |  |  | Name of the IPv4 access-list to be assigned in the ingress direction.<br>The access-list must be defined under `ipv4_acls` and supports field substitution for "interface_ip" and "peer_ip".<br>Required for all WAN interfaces (`wan_carrier` is set) unless the carrier is marked as 'trusted' under `wan_carriers`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_out</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].ipv4_acl_out") | String |  |  |  | Name of the IPv4 Access-list to be assigned in the egress direction.<br>The access-list must be defined under `ipv4_acls` and supports field substitution for "interface_ip" and "peer_ip". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static_routes</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].static_routes") | List, items: Dictionary |  |  | Min Length: 1 | Configure IPv4 static routes pointing to `peer_ip`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].static_routes.[].prefix") | String | Required, Unique |  |  | IPv4_network/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].qos_profile") | String |  |  |  | QOS service profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_carrier</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].wan_carrier") | String |  |  |  | The WAN carrier this interface is connected to.<br>This is used to infer the path-groups in which this interface should be configured.<br>Unless the carrier is marked as 'trusted' under `wan_carriers`, `ipv4_acl_in` is also required on all WAN interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_circuit_id</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].wan_circuit_id") | String |  |  |  | The WAN circuit ID for this interface.<br>This is not rendered in the configuration but used for WAN designs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected_to_pathfinder</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].connected_to_pathfinder") | Boolean |  | `True` |  | For a WAN interface (`wan_carrier` is set), allow to disable the static tunnel towards Pathfinders. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the Port-Channel interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flow_tracking</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].flow_tracking") | Dictionary |  |  |  | Configures flow-tracking on the interface. Overrides `fabric_flow_tracking.l3_port_channels` setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].flow_tracking.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].flow_tracking.name") | String |  |  |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_port_channels.[].structured_config") | Dictionary |  |  |  | Custom structured config for the Port-Channel interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l3_port_channels</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels") | List, items: Dictionary |  |  |  | L3 Port-Channel interfaces to configure on the node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].name") | String | Required, Unique |  | Pattern: `Port-Channel[\d/]+(\.[\d]+)?` | Port-Channel interface name like 'Port-Channel2' or subinterface name like 'Port-Channel2.42'.<br>For a Port-Channel subinterface, the parent Port-Channel interface must be defined as well. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].description") | String |  |  |  | Interface description.<br>If not set, a default description will be configured with '[<peer>[ <peer_port_channel>]]'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].mode") | String |  | `active` | Valid Values:<br>- <code>active</code><br>- <code>passive</code><br>- <code>on</code> | Port-Channel mode.<br>Should not be set on Port-Channel subinterfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;member_interfaces</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].member_interfaces") | List, items: Dictionary |  |  |  | Port-Channel member interfaces.<br>Should not be set on Port-Channel subinterfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].member_interfaces.[].name") | String | Required, Unique |  | Pattern: `Ethernet[\d/]+` | Ethernet interface name like 'Ethernet2'.<br>Member interface cannot be subinterface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].member_interfaces.[].description") | String |  |  |  | Interface description for this member.<br>If not set, a default description will be configured with '[<peer>[ <peer_interface>]]'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].member_interfaces.[].peer") | String |  |  |  | The peer device name. Used for description and documentation.<br>If not set, this inherits the peer setting on the port-channel interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_interface</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].member_interfaces.[].peer_interface") | String |  |  |  | The peer device interface. Used for description and documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].member_interfaces.[].speed") | String |  |  |  | Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].member_interfaces.[].structured_config") | Dictionary |  |  |  | Custom structured config for the member ethernet interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].ip_address") | String |  |  |  | Node IPv4 address/Mask or 'dhcp'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dhcp_ip</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].dhcp_ip") | String |  |  |  | When the `ip_address` is `dhcp`, this optional field allows to indicate the expected<br>IPv4 address (without mask) to be allocated on the interface if known.<br>This is not rendered in the configuration but can be used for substitution of 'interface_ip' in the Access-list<br>set under `ipv4_acl_in` and `ipv4_acl_out`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;public_ip</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].public_ip") | String |  |  |  | Node IPv4 address (no mask).<br><br>This is used to get the public IP (if known) when the device is behind NAT.<br>This is only used for `wan_rr` routers (AutoVPN RRs and Pathfinders) to determine the Public IP<br>with the following preference:<br>  `wan_route_servers.path_groups.interfaces.ip_address`<br>      -> `l3_port_channels.public_ip`<br>          -> `l3_port_channels.ip_address`<br><br>The determined Public IP is used by WAN routers when peering with this interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].encapsulation_dot1q_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dhcp_accept_default_route</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].dhcp_accept_default_route") | Boolean |  | `True` |  | Accept a default route from DHCP if `ip_address` is set to `dhcp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].enabled") | Boolean |  | `True` |  | Enable or Shutdown the interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].peer") | String |  |  |  | The peer device name. Used for description and documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_port_channel</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].peer_port_channel") | String |  |  |  | The peer device port-channel interface. Used for description and documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_ip</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].peer_ip") | String |  |  |  | The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].bgp") | Dictionary |  |  |  | Enforce IPv4 BGP peering for the peer |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_as</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].bgp.peer_as") | String | Required |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_prefix_list_in</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].bgp.ipv4_prefix_list_in") | String |  |  |  | Prefix List Name. Accept routes for only these prefixes from the peer.<br>Required for wan interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_prefix_list_out</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].bgp.ipv4_prefix_list_out") | String |  |  |  | Prefix List Name. Advertise routes for only these prefixes.<br>If not specified, nothing would be advertised. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_in</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].ipv4_acl_in") | String |  |  |  | Name of the IPv4 access-list to be assigned in the ingress direction.<br>The access-list must be defined under `ipv4_acls` and supports field substitution for "interface_ip" and "peer_ip".<br>Required for all WAN interfaces (`wan_carrier` is set) unless the carrier is marked as 'trusted' under `wan_carriers`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_out</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].ipv4_acl_out") | String |  |  |  | Name of the IPv4 Access-list to be assigned in the egress direction.<br>The access-list must be defined under `ipv4_acls` and supports field substitution for "interface_ip" and "peer_ip". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static_routes</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].static_routes") | List, items: Dictionary |  |  | Min Length: 1 | Configure IPv4 static routes pointing to `peer_ip`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].static_routes.[].prefix") | String | Required, Unique |  |  | IPv4_network/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].qos_profile") | String |  |  |  | QOS service profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_carrier</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].wan_carrier") | String |  |  |  | The WAN carrier this interface is connected to.<br>This is used to infer the path-groups in which this interface should be configured.<br>Unless the carrier is marked as 'trusted' under `wan_carriers`, `ipv4_acl_in` is also required on all WAN interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_circuit_id</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].wan_circuit_id") | String |  |  |  | The WAN circuit ID for this interface.<br>This is not rendered in the configuration but used for WAN designs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected_to_pathfinder</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].connected_to_pathfinder") | Boolean |  | `True` |  | For a WAN interface (`wan_carrier` is set), allow to disable the static tunnel towards Pathfinders. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the Port-Channel interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flow_tracking</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].flow_tracking") | Dictionary |  |  |  | Configures flow-tracking on the interface. Overrides `fabric_flow_tracking.l3_port_channels` setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].flow_tracking.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].flow_tracking.name") | String |  |  |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<node_type_keys.key>.node_groups.[].l3_port_channels.[].structured_config") | Dictionary |  |  |  | Custom structured config for the Port-Channel interface. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l3_port_channels</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels") | List, items: Dictionary |  |  |  | L3 Port-Channel interfaces to configure on the node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].name") | String | Required, Unique |  | Pattern: `Port-Channel[\d/]+(\.[\d]+)?` | Port-Channel interface name like 'Port-Channel2' or subinterface name like 'Port-Channel2.42'.<br>For a Port-Channel subinterface, the parent Port-Channel interface must be defined as well. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].description") | String |  |  |  | Interface description.<br>If not set, a default description will be configured with '[<peer>[ <peer_port_channel>]]'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].mode") | String |  | `active` | Valid Values:<br>- <code>active</code><br>- <code>passive</code><br>- <code>on</code> | Port-Channel mode.<br>Should not be set on Port-Channel subinterfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;member_interfaces</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].member_interfaces") | List, items: Dictionary |  |  |  | Port-Channel member interfaces.<br>Should not be set on Port-Channel subinterfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].member_interfaces.[].name") | String | Required, Unique |  | Pattern: `Ethernet[\d/]+` | Ethernet interface name like 'Ethernet2'.<br>Member interface cannot be subinterface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].member_interfaces.[].description") | String |  |  |  | Interface description for this member.<br>If not set, a default description will be configured with '[<peer>[ <peer_interface>]]'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].member_interfaces.[].peer") | String |  |  |  | The peer device name. Used for description and documentation.<br>If not set, this inherits the peer setting on the port-channel interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_interface</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].member_interfaces.[].peer_interface") | String |  |  |  | The peer device interface. Used for description and documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].member_interfaces.[].speed") | String |  |  |  | Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].member_interfaces.[].structured_config") | Dictionary |  |  |  | Custom structured config for the member ethernet interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].ip_address") | String |  |  |  | Node IPv4 address/Mask or 'dhcp'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dhcp_ip</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].dhcp_ip") | String |  |  |  | When the `ip_address` is `dhcp`, this optional field allows to indicate the expected<br>IPv4 address (without mask) to be allocated on the interface if known.<br>This is not rendered in the configuration but can be used for substitution of 'interface_ip' in the Access-list<br>set under `ipv4_acl_in` and `ipv4_acl_out`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;public_ip</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].public_ip") | String |  |  |  | Node IPv4 address (no mask).<br><br>This is used to get the public IP (if known) when the device is behind NAT.<br>This is only used for `wan_rr` routers (AutoVPN RRs and Pathfinders) to determine the Public IP<br>with the following preference:<br>  `wan_route_servers.path_groups.interfaces.ip_address`<br>      -> `l3_port_channels.public_ip`<br>          -> `l3_port_channels.ip_address`<br><br>The determined Public IP is used by WAN routers when peering with this interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].encapsulation_dot1q_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dhcp_accept_default_route</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].dhcp_accept_default_route") | Boolean |  | `True` |  | Accept a default route from DHCP if `ip_address` is set to `dhcp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].enabled") | Boolean |  | `True` |  | Enable or Shutdown the interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].peer") | String |  |  |  | The peer device name. Used for description and documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_port_channel</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].peer_port_channel") | String |  |  |  | The peer device port-channel interface. Used for description and documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_ip</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].peer_ip") | String |  |  |  | The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].bgp") | Dictionary |  |  |  | Enforce IPv4 BGP peering for the peer |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_as</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].bgp.peer_as") | String | Required |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_prefix_list_in</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].bgp.ipv4_prefix_list_in") | String |  |  |  | Prefix List Name. Accept routes for only these prefixes from the peer.<br>Required for wan interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_prefix_list_out</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].bgp.ipv4_prefix_list_out") | String |  |  |  | Prefix List Name. Advertise routes for only these prefixes.<br>If not specified, nothing would be advertised. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_in</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].ipv4_acl_in") | String |  |  |  | Name of the IPv4 access-list to be assigned in the ingress direction.<br>The access-list must be defined under `ipv4_acls` and supports field substitution for "interface_ip" and "peer_ip".<br>Required for all WAN interfaces (`wan_carrier` is set) unless the carrier is marked as 'trusted' under `wan_carriers`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_out</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].ipv4_acl_out") | String |  |  |  | Name of the IPv4 Access-list to be assigned in the egress direction.<br>The access-list must be defined under `ipv4_acls` and supports field substitution for "interface_ip" and "peer_ip". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static_routes</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].static_routes") | List, items: Dictionary |  |  | Min Length: 1 | Configure IPv4 static routes pointing to `peer_ip`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].static_routes.[].prefix") | String | Required, Unique |  |  | IPv4_network/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].qos_profile") | String |  |  |  | QOS service profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_carrier</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].wan_carrier") | String |  |  |  | The WAN carrier this interface is connected to.<br>This is used to infer the path-groups in which this interface should be configured.<br>Unless the carrier is marked as 'trusted' under `wan_carriers`, `ipv4_acl_in` is also required on all WAN interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_circuit_id</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].wan_circuit_id") | String |  |  |  | The WAN circuit ID for this interface.<br>This is not rendered in the configuration but used for WAN designs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected_to_pathfinder</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].connected_to_pathfinder") | Boolean |  | `True` |  | For a WAN interface (`wan_carrier` is set), allow to disable the static tunnel towards Pathfinders. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the Port-Channel interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flow_tracking</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].flow_tracking") | Dictionary |  |  |  | Configures flow-tracking on the interface. Overrides `fabric_flow_tracking.l3_port_channels` setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].flow_tracking.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].flow_tracking.name") | String |  |  |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<node_type_keys.key>.nodes.[].l3_port_channels.[].structured_config") | Dictionary |  |  |  | Custom structured config for the Port-Channel interface. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:

        # L3 Port-Channel interfaces to configure on the node.
        l3_port_channels:

            # Port-Channel interface name like 'Port-Channel2' or subinterface name like 'Port-Channel2.42'.
            # For a Port-Channel subinterface, the parent Port-Channel interface must be defined as well.
          - name: <str; required; unique>

            # Interface description.
            # If not set, a default description will be configured with '[<peer>[ <peer_port_channel>]]'.
            description: <str>

            # Port-Channel mode.
            # Should not be set on Port-Channel subinterfaces.
            mode: <str; "active" | "passive" | "on"; default="active">

            # Port-Channel member interfaces.
            # Should not be set on Port-Channel subinterfaces.
            member_interfaces:

                # Ethernet interface name like 'Ethernet2'.
                # Member interface cannot be subinterface.
              - name: <str; required; unique>

                # Interface description for this member.
                # If not set, a default description will be configured with '[<peer>[ <peer_interface>]]'.
                description: <str>

                # The peer device name. Used for description and documentation.
                # If not set, this inherits the peer setting on the port-channel interface.
                peer: <str>

                # The peer device interface. Used for description and documentation.
                peer_interface: <str>

                # Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
                speed: <str>

                # Custom structured config for the member ethernet interface.
                structured_config: <dict>

            # Node IPv4 address/Mask or 'dhcp'.
            ip_address: <str>

            # When the `ip_address` is `dhcp`, this optional field allows to indicate the expected
            # IPv4 address (without mask) to be allocated on the interface if known.
            # This is not rendered in the configuration but can be used for substitution of 'interface_ip' in the Access-list
            # set under `ipv4_acl_in` and `ipv4_acl_out`.
            dhcp_ip: <str>

            # Node IPv4 address (no mask).
            #
            # This is used to get the public IP (if known) when the device is behind NAT.
            # This is only used for `wan_rr` routers (AutoVPN RRs and Pathfinders) to determine the Public IP
            # with the following preference:
            #   `wan_route_servers.path_groups.interfaces.ip_address`
            #       -> `l3_port_channels.public_ip`
            #           -> `l3_port_channels.ip_address`
            #
            # The determined Public IP is used by WAN routers when peering with this interface.
            public_ip: <str>

            # For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified.
            encapsulation_dot1q_vlan: <int; 1-4094>

            # Accept a default route from DHCP if `ip_address` is set to `dhcp`.
            dhcp_accept_default_route: <bool; default=True>

            # Enable or Shutdown the interface.
            enabled: <bool; default=True>

            # The peer device name. Used for description and documentation.
            peer: <str>

            # The peer device port-channel interface. Used for description and documentation.
            peer_port_channel: <str>

            # The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP address.
            peer_ip: <str>

            # Enforce IPv4 BGP peering for the peer
            bgp:

              # BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
              # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
              peer_as: <str; required>

              # Prefix List Name. Accept routes for only these prefixes from the peer.
              # Required for wan interfaces.
              ipv4_prefix_list_in: <str>

              # Prefix List Name. Advertise routes for only these prefixes.
              # If not specified, nothing would be advertised.
              ipv4_prefix_list_out: <str>

            # Name of the IPv4 access-list to be assigned in the ingress direction.
            # The access-list must be defined under `ipv4_acls` and supports field substitution for "interface_ip" and "peer_ip".
            # Required for all WAN interfaces (`wan_carrier` is set) unless the carrier is marked as 'trusted' under `wan_carriers`.
            ipv4_acl_in: <str>

            # Name of the IPv4 Access-list to be assigned in the egress direction.
            # The access-list must be defined under `ipv4_acls` and supports field substitution for "interface_ip" and "peer_ip".
            ipv4_acl_out: <str>

            # Configure IPv4 static routes pointing to `peer_ip`.
            static_routes: # >=1 items

                # IPv4_network/Mask.
              - prefix: <str; required; unique>

            # QOS service profile.
            qos_profile: <str>

            # The WAN carrier this interface is connected to.
            # This is used to infer the path-groups in which this interface should be configured.
            # Unless the carrier is marked as 'trusted' under `wan_carriers`, `ipv4_acl_in` is also required on all WAN interfaces.
            wan_carrier: <str>

            # The WAN circuit ID for this interface.
            # This is not rendered in the configuration but used for WAN designs.
            wan_circuit_id: <str>

            # For a WAN interface (`wan_carrier` is set), allow to disable the static tunnel towards Pathfinders.
            connected_to_pathfinder: <bool; default=True>

            # EOS CLI rendered directly on the Port-Channel interface in the final EOS configuration.
            raw_eos_cli: <str>

            # Configures flow-tracking on the interface. Overrides `fabric_flow_tracking.l3_port_channels` setting.
            flow_tracking:
              enabled: <bool>

              # Flow tracker name as defined in flow_tracking_settings.
              name: <str>

            # Custom structured config for the Port-Channel interface.
            structured_config: <dict>

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>

              # L3 Port-Channel interfaces to configure on the node.
              l3_port_channels:

                  # Port-Channel interface name like 'Port-Channel2' or subinterface name like 'Port-Channel2.42'.
                  # For a Port-Channel subinterface, the parent Port-Channel interface must be defined as well.
                - name: <str; required; unique>

                  # Interface description.
                  # If not set, a default description will be configured with '[<peer>[ <peer_port_channel>]]'.
                  description: <str>

                  # Port-Channel mode.
                  # Should not be set on Port-Channel subinterfaces.
                  mode: <str; "active" | "passive" | "on"; default="active">

                  # Port-Channel member interfaces.
                  # Should not be set on Port-Channel subinterfaces.
                  member_interfaces:

                      # Ethernet interface name like 'Ethernet2'.
                      # Member interface cannot be subinterface.
                    - name: <str; required; unique>

                      # Interface description for this member.
                      # If not set, a default description will be configured with '[<peer>[ <peer_interface>]]'.
                      description: <str>

                      # The peer device name. Used for description and documentation.
                      # If not set, this inherits the peer setting on the port-channel interface.
                      peer: <str>

                      # The peer device interface. Used for description and documentation.
                      peer_interface: <str>

                      # Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
                      speed: <str>

                      # Custom structured config for the member ethernet interface.
                      structured_config: <dict>

                  # Node IPv4 address/Mask or 'dhcp'.
                  ip_address: <str>

                  # When the `ip_address` is `dhcp`, this optional field allows to indicate the expected
                  # IPv4 address (without mask) to be allocated on the interface if known.
                  # This is not rendered in the configuration but can be used for substitution of 'interface_ip' in the Access-list
                  # set under `ipv4_acl_in` and `ipv4_acl_out`.
                  dhcp_ip: <str>

                  # Node IPv4 address (no mask).
                  #
                  # This is used to get the public IP (if known) when the device is behind NAT.
                  # This is only used for `wan_rr` routers (AutoVPN RRs and Pathfinders) to determine the Public IP
                  # with the following preference:
                  #   `wan_route_servers.path_groups.interfaces.ip_address`
                  #       -> `l3_port_channels.public_ip`
                  #           -> `l3_port_channels.ip_address`
                  #
                  # The determined Public IP is used by WAN routers when peering with this interface.
                  public_ip: <str>

                  # For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified.
                  encapsulation_dot1q_vlan: <int; 1-4094>

                  # Accept a default route from DHCP if `ip_address` is set to `dhcp`.
                  dhcp_accept_default_route: <bool; default=True>

                  # Enable or Shutdown the interface.
                  enabled: <bool; default=True>

                  # The peer device name. Used for description and documentation.
                  peer: <str>

                  # The peer device port-channel interface. Used for description and documentation.
                  peer_port_channel: <str>

                  # The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP address.
                  peer_ip: <str>

                  # Enforce IPv4 BGP peering for the peer
                  bgp:

                    # BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                    # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
                    peer_as: <str; required>

                    # Prefix List Name. Accept routes for only these prefixes from the peer.
                    # Required for wan interfaces.
                    ipv4_prefix_list_in: <str>

                    # Prefix List Name. Advertise routes for only these prefixes.
                    # If not specified, nothing would be advertised.
                    ipv4_prefix_list_out: <str>

                  # Name of the IPv4 access-list to be assigned in the ingress direction.
                  # The access-list must be defined under `ipv4_acls` and supports field substitution for "interface_ip" and "peer_ip".
                  # Required for all WAN interfaces (`wan_carrier` is set) unless the carrier is marked as 'trusted' under `wan_carriers`.
                  ipv4_acl_in: <str>

                  # Name of the IPv4 Access-list to be assigned in the egress direction.
                  # The access-list must be defined under `ipv4_acls` and supports field substitution for "interface_ip" and "peer_ip".
                  ipv4_acl_out: <str>

                  # Configure IPv4 static routes pointing to `peer_ip`.
                  static_routes: # >=1 items

                      # IPv4_network/Mask.
                    - prefix: <str; required; unique>

                  # QOS service profile.
                  qos_profile: <str>

                  # The WAN carrier this interface is connected to.
                  # This is used to infer the path-groups in which this interface should be configured.
                  # Unless the carrier is marked as 'trusted' under `wan_carriers`, `ipv4_acl_in` is also required on all WAN interfaces.
                  wan_carrier: <str>

                  # The WAN circuit ID for this interface.
                  # This is not rendered in the configuration but used for WAN designs.
                  wan_circuit_id: <str>

                  # For a WAN interface (`wan_carrier` is set), allow to disable the static tunnel towards Pathfinders.
                  connected_to_pathfinder: <bool; default=True>

                  # EOS CLI rendered directly on the Port-Channel interface in the final EOS configuration.
                  raw_eos_cli: <str>

                  # Configures flow-tracking on the interface. Overrides `fabric_flow_tracking.l3_port_channels` setting.
                  flow_tracking:
                    enabled: <bool>

                    # Flow tracker name as defined in flow_tracking_settings.
                    name: <str>

                  # Custom structured config for the Port-Channel interface.
                  structured_config: <dict>

          # L3 Port-Channel interfaces to configure on the node.
          l3_port_channels:

              # Port-Channel interface name like 'Port-Channel2' or subinterface name like 'Port-Channel2.42'.
              # For a Port-Channel subinterface, the parent Port-Channel interface must be defined as well.
            - name: <str; required; unique>

              # Interface description.
              # If not set, a default description will be configured with '[<peer>[ <peer_port_channel>]]'.
              description: <str>

              # Port-Channel mode.
              # Should not be set on Port-Channel subinterfaces.
              mode: <str; "active" | "passive" | "on"; default="active">

              # Port-Channel member interfaces.
              # Should not be set on Port-Channel subinterfaces.
              member_interfaces:

                  # Ethernet interface name like 'Ethernet2'.
                  # Member interface cannot be subinterface.
                - name: <str; required; unique>

                  # Interface description for this member.
                  # If not set, a default description will be configured with '[<peer>[ <peer_interface>]]'.
                  description: <str>

                  # The peer device name. Used for description and documentation.
                  # If not set, this inherits the peer setting on the port-channel interface.
                  peer: <str>

                  # The peer device interface. Used for description and documentation.
                  peer_interface: <str>

                  # Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
                  speed: <str>

                  # Custom structured config for the member ethernet interface.
                  structured_config: <dict>

              # Node IPv4 address/Mask or 'dhcp'.
              ip_address: <str>

              # When the `ip_address` is `dhcp`, this optional field allows to indicate the expected
              # IPv4 address (without mask) to be allocated on the interface if known.
              # This is not rendered in the configuration but can be used for substitution of 'interface_ip' in the Access-list
              # set under `ipv4_acl_in` and `ipv4_acl_out`.
              dhcp_ip: <str>

              # Node IPv4 address (no mask).
              #
              # This is used to get the public IP (if known) when the device is behind NAT.
              # This is only used for `wan_rr` routers (AutoVPN RRs and Pathfinders) to determine the Public IP
              # with the following preference:
              #   `wan_route_servers.path_groups.interfaces.ip_address`
              #       -> `l3_port_channels.public_ip`
              #           -> `l3_port_channels.ip_address`
              #
              # The determined Public IP is used by WAN routers when peering with this interface.
              public_ip: <str>

              # For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified.
              encapsulation_dot1q_vlan: <int; 1-4094>

              # Accept a default route from DHCP if `ip_address` is set to `dhcp`.
              dhcp_accept_default_route: <bool; default=True>

              # Enable or Shutdown the interface.
              enabled: <bool; default=True>

              # The peer device name. Used for description and documentation.
              peer: <str>

              # The peer device port-channel interface. Used for description and documentation.
              peer_port_channel: <str>

              # The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP address.
              peer_ip: <str>

              # Enforce IPv4 BGP peering for the peer
              bgp:

                # BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
                peer_as: <str; required>

                # Prefix List Name. Accept routes for only these prefixes from the peer.
                # Required for wan interfaces.
                ipv4_prefix_list_in: <str>

                # Prefix List Name. Advertise routes for only these prefixes.
                # If not specified, nothing would be advertised.
                ipv4_prefix_list_out: <str>

              # Name of the IPv4 access-list to be assigned in the ingress direction.
              # The access-list must be defined under `ipv4_acls` and supports field substitution for "interface_ip" and "peer_ip".
              # Required for all WAN interfaces (`wan_carrier` is set) unless the carrier is marked as 'trusted' under `wan_carriers`.
              ipv4_acl_in: <str>

              # Name of the IPv4 Access-list to be assigned in the egress direction.
              # The access-list must be defined under `ipv4_acls` and supports field substitution for "interface_ip" and "peer_ip".
              ipv4_acl_out: <str>

              # Configure IPv4 static routes pointing to `peer_ip`.
              static_routes: # >=1 items

                  # IPv4_network/Mask.
                - prefix: <str; required; unique>

              # QOS service profile.
              qos_profile: <str>

              # The WAN carrier this interface is connected to.
              # This is used to infer the path-groups in which this interface should be configured.
              # Unless the carrier is marked as 'trusted' under `wan_carriers`, `ipv4_acl_in` is also required on all WAN interfaces.
              wan_carrier: <str>

              # The WAN circuit ID for this interface.
              # This is not rendered in the configuration but used for WAN designs.
              wan_circuit_id: <str>

              # For a WAN interface (`wan_carrier` is set), allow to disable the static tunnel towards Pathfinders.
              connected_to_pathfinder: <bool; default=True>

              # EOS CLI rendered directly on the Port-Channel interface in the final EOS configuration.
              raw_eos_cli: <str>

              # Configures flow-tracking on the interface. Overrides `fabric_flow_tracking.l3_port_channels` setting.
              flow_tracking:
                enabled: <bool>

                # Flow tracker name as defined in flow_tracking_settings.
                name: <str>

              # Custom structured config for the Port-Channel interface.
              structured_config: <dict>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>

          # L3 Port-Channel interfaces to configure on the node.
          l3_port_channels:

              # Port-Channel interface name like 'Port-Channel2' or subinterface name like 'Port-Channel2.42'.
              # For a Port-Channel subinterface, the parent Port-Channel interface must be defined as well.
            - name: <str; required; unique>

              # Interface description.
              # If not set, a default description will be configured with '[<peer>[ <peer_port_channel>]]'.
              description: <str>

              # Port-Channel mode.
              # Should not be set on Port-Channel subinterfaces.
              mode: <str; "active" | "passive" | "on"; default="active">

              # Port-Channel member interfaces.
              # Should not be set on Port-Channel subinterfaces.
              member_interfaces:

                  # Ethernet interface name like 'Ethernet2'.
                  # Member interface cannot be subinterface.
                - name: <str; required; unique>

                  # Interface description for this member.
                  # If not set, a default description will be configured with '[<peer>[ <peer_interface>]]'.
                  description: <str>

                  # The peer device name. Used for description and documentation.
                  # If not set, this inherits the peer setting on the port-channel interface.
                  peer: <str>

                  # The peer device interface. Used for description and documentation.
                  peer_interface: <str>

                  # Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
                  speed: <str>

                  # Custom structured config for the member ethernet interface.
                  structured_config: <dict>

              # Node IPv4 address/Mask or 'dhcp'.
              ip_address: <str>

              # When the `ip_address` is `dhcp`, this optional field allows to indicate the expected
              # IPv4 address (without mask) to be allocated on the interface if known.
              # This is not rendered in the configuration but can be used for substitution of 'interface_ip' in the Access-list
              # set under `ipv4_acl_in` and `ipv4_acl_out`.
              dhcp_ip: <str>

              # Node IPv4 address (no mask).
              #
              # This is used to get the public IP (if known) when the device is behind NAT.
              # This is only used for `wan_rr` routers (AutoVPN RRs and Pathfinders) to determine the Public IP
              # with the following preference:
              #   `wan_route_servers.path_groups.interfaces.ip_address`
              #       -> `l3_port_channels.public_ip`
              #           -> `l3_port_channels.ip_address`
              #
              # The determined Public IP is used by WAN routers when peering with this interface.
              public_ip: <str>

              # For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified.
              encapsulation_dot1q_vlan: <int; 1-4094>

              # Accept a default route from DHCP if `ip_address` is set to `dhcp`.
              dhcp_accept_default_route: <bool; default=True>

              # Enable or Shutdown the interface.
              enabled: <bool; default=True>

              # The peer device name. Used for description and documentation.
              peer: <str>

              # The peer device port-channel interface. Used for description and documentation.
              peer_port_channel: <str>

              # The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP address.
              peer_ip: <str>

              # Enforce IPv4 BGP peering for the peer
              bgp:

                # BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
                peer_as: <str; required>

                # Prefix List Name. Accept routes for only these prefixes from the peer.
                # Required for wan interfaces.
                ipv4_prefix_list_in: <str>

                # Prefix List Name. Advertise routes for only these prefixes.
                # If not specified, nothing would be advertised.
                ipv4_prefix_list_out: <str>

              # Name of the IPv4 access-list to be assigned in the ingress direction.
              # The access-list must be defined under `ipv4_acls` and supports field substitution for "interface_ip" and "peer_ip".
              # Required for all WAN interfaces (`wan_carrier` is set) unless the carrier is marked as 'trusted' under `wan_carriers`.
              ipv4_acl_in: <str>

              # Name of the IPv4 Access-list to be assigned in the egress direction.
              # The access-list must be defined under `ipv4_acls` and supports field substitution for "interface_ip" and "peer_ip".
              ipv4_acl_out: <str>

              # Configure IPv4 static routes pointing to `peer_ip`.
              static_routes: # >=1 items

                  # IPv4_network/Mask.
                - prefix: <str; required; unique>

              # QOS service profile.
              qos_profile: <str>

              # The WAN carrier this interface is connected to.
              # This is used to infer the path-groups in which this interface should be configured.
              # Unless the carrier is marked as 'trusted' under `wan_carriers`, `ipv4_acl_in` is also required on all WAN interfaces.
              wan_carrier: <str>

              # The WAN circuit ID for this interface.
              # This is not rendered in the configuration but used for WAN designs.
              wan_circuit_id: <str>

              # For a WAN interface (`wan_carrier` is set), allow to disable the static tunnel towards Pathfinders.
              connected_to_pathfinder: <bool; default=True>

              # EOS CLI rendered directly on the Port-Channel interface in the final EOS configuration.
              raw_eos_cli: <str>

              # Configures flow-tracking on the interface. Overrides `fabric_flow_tracking.l3_port_channels` setting.
              flow_tracking:
                enabled: <bool>

                # Flow tracker name as defined in flow_tracking_settings.
                name: <str>

              # Custom structured config for the Port-Channel interface.
              structured_config: <dict>
    ```
