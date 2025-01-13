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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l3_interfaces</samp>](## "<node_type_keys.key>.defaults.l3_interfaces") | List, items: Dictionary |  |  |  | L3 Interfaces to configure on the node.<br>Used to define the node for WAN interfaces when `wan_carrier` is set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;profile</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].profile") | String |  |  |  | L3 interface profile name. Profile defined under `l3_interface_profiles`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].name") | String | Required, Unique |  | Pattern: `Ethernet[\d/]+(.[\d]+)?` | Ethernet interface name like 'Ethernet2' or subinterface name like 'Ethernet2.42'.<br>For a subinterface, the parent physical interface is automatically created. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].description") | String |  |  |  | Interface description.<br>If not set a default description will be configured with '[<peer>[ <peer_interface>]]'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].ip_address") | String |  |  |  | Node IPv4 address/Mask or 'dhcp'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dhcp_ip</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].dhcp_ip") | String |  |  |  | When the `ip_address` is `dhcp`, this optional field allows to indicate the expected<br>IPv4 address (without mask) to be allocated on the interface if known.<br>This is not rendered in the configuration but can be used for substitution of 'interface_ip' in the Access-list<br>set under `ipv4_acl_in` and `ipv4_acl_out`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;public_ip</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].public_ip") | String |  |  |  | Node IPv4 address (no mask).<br><br>This is used to get the public IP (if known) when the device is behind NAT.<br>This is only used for `wan_rr` routers (AutoVPN RRs and Pathfinders) to determine the Public IP<br>with the following preference:<br>  `wan_route_servers.path_groups.interfaces.ip_address`<br>      -> `l3_interfaces.public_ip`<br>          -> `l3_interfaces.ip_address`<br><br>The determined Public IP is used by WAN routers when peering with this interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].encapsulation_dot1q_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dhcp_accept_default_route</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].dhcp_accept_default_route") | Boolean |  | `True` |  | Accept a default route from DHCP if `ip_address` is set to `dhcp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].enabled") | Boolean |  | `True` |  | Enable or Shutdown the interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].speed") | String |  |  |  | Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].peer") | String |  |  |  | The peer device name. Used for description and documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_interface</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].peer_interface") | String |  |  |  | The peer device interface. Used for description and documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_ip</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].peer_ip") | String |  |  |  | The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].bgp") | Dictionary |  |  |  | Enforce IPv4 BGP peering for the peer |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_as</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].bgp.peer_as") | String | Required |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_prefix_list_in</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].bgp.ipv4_prefix_list_in") | String |  |  |  | Prefix List Name. Accept routes for only these prefixes from the peer.<br>Required for wan interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_prefix_list_out</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].bgp.ipv4_prefix_list_out") | String |  |  |  | Prefix List Name. Advertise routes for only these prefixes.<br>If not specified, nothing would be advertised. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_in</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].ipv4_acl_in") | String |  |  |  | Name of the IPv4 access-list to be assigned in the ingress direction.<br>The access-list must be defined under `ipv4_acls` and supports field substitution for "interface_ip" and "peer_ip".<br>Required for all WAN interfaces (`wan_carrier` is set) unless the carrier is marked as 'trusted' under `wan_carriers`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_out</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].ipv4_acl_out") | String |  |  |  | Name of the IPv4 Access-list to be assigned in the egress direction.<br>The access-list must be defined under `ipv4_acls` and supports field substitution for "interface_ip" and "peer_ip". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static_routes</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].static_routes") | List, items: Dictionary |  |  | Min Length: 1 | Configure IPv4 static routes pointing to `peer_ip`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].static_routes.[].prefix") | String | Required |  |  | IPv4_network/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].qos_profile") | String |  |  |  | QOS service profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_carrier</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].wan_carrier") | String |  |  |  | The WAN carrier this interface is connected to.<br>This is used to infer the path-groups in which this interface should be configured.<br>Unless the carrier is marked as 'trusted' under `wan_carriers`, `ipv4_acl_in` is also required on all WAN interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_circuit_id</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].wan_circuit_id") | String |  |  |  | The WAN circuit ID for this interface.<br>This is not rendered in the configuration but used for WAN designs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected_to_pathfinder</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].connected_to_pathfinder") | Boolean |  | `True` |  | For a WAN interface (`wan_carrier` is set), allow to disable the static tunnel towards Pathfinders. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_internet_exit</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].cv_pathfinder_internet_exit") | Dictionary |  |  |  | PREVIEW: This key is in preview mode |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;policies</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].cv_pathfinder_internet_exit.policies") | List, items: Dictionary |  |  |  | List of Internet-exit policies using this interface as exit. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].cv_pathfinder_internet_exit.policies.[].name") | String | Required, Unique |  |  | Internet-exit policy name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tunnel_interface_numbers</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].cv_pathfinder_internet_exit.policies.[].tunnel_interface_numbers") | String |  |  |  | Number range to use for Tunnel interfaces to an internet-exit service provider using this local interface.<br>Examples: '1-3' or '100,200,300' |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flow_tracking</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].flow_tracking") | Dictionary |  |  |  | Configures flow-tracking on the interface. Overrides `fabric_flow_tracking.l3_interfaces` setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].flow_tracking.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].flow_tracking.name") | String |  |  |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<node_type_keys.key>.defaults.l3_interfaces.[].structured_config") | Dictionary |  |  |  | Custom structured config for the Ethernet interface. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l3_interfaces</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces") | List, items: Dictionary |  |  |  | L3 Interfaces to configure on the node.<br>Used to define the node for WAN interfaces when `wan_carrier` is set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;profile</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].profile") | String |  |  |  | L3 interface profile name. Profile defined under `l3_interface_profiles`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].name") | String | Required, Unique |  | Pattern: `Ethernet[\d/]+(.[\d]+)?` | Ethernet interface name like 'Ethernet2' or subinterface name like 'Ethernet2.42'.<br>For a subinterface, the parent physical interface is automatically created. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].description") | String |  |  |  | Interface description.<br>If not set a default description will be configured with '[<peer>[ <peer_interface>]]'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].ip_address") | String |  |  |  | Node IPv4 address/Mask or 'dhcp'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dhcp_ip</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].dhcp_ip") | String |  |  |  | When the `ip_address` is `dhcp`, this optional field allows to indicate the expected<br>IPv4 address (without mask) to be allocated on the interface if known.<br>This is not rendered in the configuration but can be used for substitution of 'interface_ip' in the Access-list<br>set under `ipv4_acl_in` and `ipv4_acl_out`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;public_ip</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].public_ip") | String |  |  |  | Node IPv4 address (no mask).<br><br>This is used to get the public IP (if known) when the device is behind NAT.<br>This is only used for `wan_rr` routers (AutoVPN RRs and Pathfinders) to determine the Public IP<br>with the following preference:<br>  `wan_route_servers.path_groups.interfaces.ip_address`<br>      -> `l3_interfaces.public_ip`<br>          -> `l3_interfaces.ip_address`<br><br>The determined Public IP is used by WAN routers when peering with this interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].encapsulation_dot1q_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dhcp_accept_default_route</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].dhcp_accept_default_route") | Boolean |  | `True` |  | Accept a default route from DHCP if `ip_address` is set to `dhcp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].enabled") | Boolean |  | `True` |  | Enable or Shutdown the interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].speed") | String |  |  |  | Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].peer") | String |  |  |  | The peer device name. Used for description and documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_interface</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].peer_interface") | String |  |  |  | The peer device interface. Used for description and documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_ip</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].peer_ip") | String |  |  |  | The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].bgp") | Dictionary |  |  |  | Enforce IPv4 BGP peering for the peer |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_as</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].bgp.peer_as") | String | Required |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_prefix_list_in</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].bgp.ipv4_prefix_list_in") | String |  |  |  | Prefix List Name. Accept routes for only these prefixes from the peer.<br>Required for wan interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_prefix_list_out</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].bgp.ipv4_prefix_list_out") | String |  |  |  | Prefix List Name. Advertise routes for only these prefixes.<br>If not specified, nothing would be advertised. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_in</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].ipv4_acl_in") | String |  |  |  | Name of the IPv4 access-list to be assigned in the ingress direction.<br>The access-list must be defined under `ipv4_acls` and supports field substitution for "interface_ip" and "peer_ip".<br>Required for all WAN interfaces (`wan_carrier` is set) unless the carrier is marked as 'trusted' under `wan_carriers`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_out</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].ipv4_acl_out") | String |  |  |  | Name of the IPv4 Access-list to be assigned in the egress direction.<br>The access-list must be defined under `ipv4_acls` and supports field substitution for "interface_ip" and "peer_ip". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static_routes</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].static_routes") | List, items: Dictionary |  |  | Min Length: 1 | Configure IPv4 static routes pointing to `peer_ip`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].static_routes.[].prefix") | String | Required |  |  | IPv4_network/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].qos_profile") | String |  |  |  | QOS service profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_carrier</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].wan_carrier") | String |  |  |  | The WAN carrier this interface is connected to.<br>This is used to infer the path-groups in which this interface should be configured.<br>Unless the carrier is marked as 'trusted' under `wan_carriers`, `ipv4_acl_in` is also required on all WAN interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_circuit_id</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].wan_circuit_id") | String |  |  |  | The WAN circuit ID for this interface.<br>This is not rendered in the configuration but used for WAN designs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected_to_pathfinder</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].connected_to_pathfinder") | Boolean |  | `True` |  | For a WAN interface (`wan_carrier` is set), allow to disable the static tunnel towards Pathfinders. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_internet_exit</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].cv_pathfinder_internet_exit") | Dictionary |  |  |  | PREVIEW: This key is in preview mode |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;policies</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].cv_pathfinder_internet_exit.policies") | List, items: Dictionary |  |  |  | List of Internet-exit policies using this interface as exit. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].cv_pathfinder_internet_exit.policies.[].name") | String | Required, Unique |  |  | Internet-exit policy name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tunnel_interface_numbers</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].cv_pathfinder_internet_exit.policies.[].tunnel_interface_numbers") | String |  |  |  | Number range to use for Tunnel interfaces to an internet-exit service provider using this local interface.<br>Examples: '1-3' or '100,200,300' |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flow_tracking</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].flow_tracking") | Dictionary |  |  |  | Configures flow-tracking on the interface. Overrides `fabric_flow_tracking.l3_interfaces` setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].flow_tracking.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].flow_tracking.name") | String |  |  |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].l3_interfaces.[].structured_config") | Dictionary |  |  |  | Custom structured config for the Ethernet interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l3_interfaces</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces") | List, items: Dictionary |  |  |  | L3 Interfaces to configure on the node.<br>Used to define the node for WAN interfaces when `wan_carrier` is set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;profile</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].profile") | String |  |  |  | L3 interface profile name. Profile defined under `l3_interface_profiles`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].name") | String | Required, Unique |  | Pattern: `Ethernet[\d/]+(.[\d]+)?` | Ethernet interface name like 'Ethernet2' or subinterface name like 'Ethernet2.42'.<br>For a subinterface, the parent physical interface is automatically created. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].description") | String |  |  |  | Interface description.<br>If not set a default description will be configured with '[<peer>[ <peer_interface>]]'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].ip_address") | String |  |  |  | Node IPv4 address/Mask or 'dhcp'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dhcp_ip</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].dhcp_ip") | String |  |  |  | When the `ip_address` is `dhcp`, this optional field allows to indicate the expected<br>IPv4 address (without mask) to be allocated on the interface if known.<br>This is not rendered in the configuration but can be used for substitution of 'interface_ip' in the Access-list<br>set under `ipv4_acl_in` and `ipv4_acl_out`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;public_ip</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].public_ip") | String |  |  |  | Node IPv4 address (no mask).<br><br>This is used to get the public IP (if known) when the device is behind NAT.<br>This is only used for `wan_rr` routers (AutoVPN RRs and Pathfinders) to determine the Public IP<br>with the following preference:<br>  `wan_route_servers.path_groups.interfaces.ip_address`<br>      -> `l3_interfaces.public_ip`<br>          -> `l3_interfaces.ip_address`<br><br>The determined Public IP is used by WAN routers when peering with this interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].encapsulation_dot1q_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dhcp_accept_default_route</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].dhcp_accept_default_route") | Boolean |  | `True` |  | Accept a default route from DHCP if `ip_address` is set to `dhcp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].enabled") | Boolean |  | `True` |  | Enable or Shutdown the interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].speed") | String |  |  |  | Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].peer") | String |  |  |  | The peer device name. Used for description and documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_interface</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].peer_interface") | String |  |  |  | The peer device interface. Used for description and documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_ip</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].peer_ip") | String |  |  |  | The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].bgp") | Dictionary |  |  |  | Enforce IPv4 BGP peering for the peer |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_as</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].bgp.peer_as") | String | Required |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_prefix_list_in</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].bgp.ipv4_prefix_list_in") | String |  |  |  | Prefix List Name. Accept routes for only these prefixes from the peer.<br>Required for wan interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_prefix_list_out</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].bgp.ipv4_prefix_list_out") | String |  |  |  | Prefix List Name. Advertise routes for only these prefixes.<br>If not specified, nothing would be advertised. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_in</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].ipv4_acl_in") | String |  |  |  | Name of the IPv4 access-list to be assigned in the ingress direction.<br>The access-list must be defined under `ipv4_acls` and supports field substitution for "interface_ip" and "peer_ip".<br>Required for all WAN interfaces (`wan_carrier` is set) unless the carrier is marked as 'trusted' under `wan_carriers`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_out</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].ipv4_acl_out") | String |  |  |  | Name of the IPv4 Access-list to be assigned in the egress direction.<br>The access-list must be defined under `ipv4_acls` and supports field substitution for "interface_ip" and "peer_ip". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static_routes</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].static_routes") | List, items: Dictionary |  |  | Min Length: 1 | Configure IPv4 static routes pointing to `peer_ip`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].static_routes.[].prefix") | String | Required |  |  | IPv4_network/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].qos_profile") | String |  |  |  | QOS service profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_carrier</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].wan_carrier") | String |  |  |  | The WAN carrier this interface is connected to.<br>This is used to infer the path-groups in which this interface should be configured.<br>Unless the carrier is marked as 'trusted' under `wan_carriers`, `ipv4_acl_in` is also required on all WAN interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_circuit_id</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].wan_circuit_id") | String |  |  |  | The WAN circuit ID for this interface.<br>This is not rendered in the configuration but used for WAN designs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected_to_pathfinder</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].connected_to_pathfinder") | Boolean |  | `True` |  | For a WAN interface (`wan_carrier` is set), allow to disable the static tunnel towards Pathfinders. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_internet_exit</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].cv_pathfinder_internet_exit") | Dictionary |  |  |  | PREVIEW: This key is in preview mode |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;policies</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].cv_pathfinder_internet_exit.policies") | List, items: Dictionary |  |  |  | List of Internet-exit policies using this interface as exit. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].cv_pathfinder_internet_exit.policies.[].name") | String | Required, Unique |  |  | Internet-exit policy name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tunnel_interface_numbers</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].cv_pathfinder_internet_exit.policies.[].tunnel_interface_numbers") | String |  |  |  | Number range to use for Tunnel interfaces to an internet-exit service provider using this local interface.<br>Examples: '1-3' or '100,200,300' |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flow_tracking</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].flow_tracking") | Dictionary |  |  |  | Configures flow-tracking on the interface. Overrides `fabric_flow_tracking.l3_interfaces` setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].flow_tracking.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].flow_tracking.name") | String |  |  |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<node_type_keys.key>.node_groups.[].l3_interfaces.[].structured_config") | Dictionary |  |  |  | Custom structured config for the Ethernet interface. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l3_interfaces</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces") | List, items: Dictionary |  |  |  | L3 Interfaces to configure on the node.<br>Used to define the node for WAN interfaces when `wan_carrier` is set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;profile</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].profile") | String |  |  |  | L3 interface profile name. Profile defined under `l3_interface_profiles`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].name") | String | Required, Unique |  | Pattern: `Ethernet[\d/]+(.[\d]+)?` | Ethernet interface name like 'Ethernet2' or subinterface name like 'Ethernet2.42'.<br>For a subinterface, the parent physical interface is automatically created. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].description") | String |  |  |  | Interface description.<br>If not set a default description will be configured with '[<peer>[ <peer_interface>]]'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].ip_address") | String |  |  |  | Node IPv4 address/Mask or 'dhcp'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dhcp_ip</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].dhcp_ip") | String |  |  |  | When the `ip_address` is `dhcp`, this optional field allows to indicate the expected<br>IPv4 address (without mask) to be allocated on the interface if known.<br>This is not rendered in the configuration but can be used for substitution of 'interface_ip' in the Access-list<br>set under `ipv4_acl_in` and `ipv4_acl_out`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;public_ip</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].public_ip") | String |  |  |  | Node IPv4 address (no mask).<br><br>This is used to get the public IP (if known) when the device is behind NAT.<br>This is only used for `wan_rr` routers (AutoVPN RRs and Pathfinders) to determine the Public IP<br>with the following preference:<br>  `wan_route_servers.path_groups.interfaces.ip_address`<br>      -> `l3_interfaces.public_ip`<br>          -> `l3_interfaces.ip_address`<br><br>The determined Public IP is used by WAN routers when peering with this interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].encapsulation_dot1q_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dhcp_accept_default_route</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].dhcp_accept_default_route") | Boolean |  | `True` |  | Accept a default route from DHCP if `ip_address` is set to `dhcp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].enabled") | Boolean |  | `True` |  | Enable or Shutdown the interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].speed") | String |  |  |  | Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].peer") | String |  |  |  | The peer device name. Used for description and documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_interface</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].peer_interface") | String |  |  |  | The peer device interface. Used for description and documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_ip</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].peer_ip") | String |  |  |  | The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].bgp") | Dictionary |  |  |  | Enforce IPv4 BGP peering for the peer |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_as</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].bgp.peer_as") | String | Required |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_prefix_list_in</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].bgp.ipv4_prefix_list_in") | String |  |  |  | Prefix List Name. Accept routes for only these prefixes from the peer.<br>Required for wan interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_prefix_list_out</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].bgp.ipv4_prefix_list_out") | String |  |  |  | Prefix List Name. Advertise routes for only these prefixes.<br>If not specified, nothing would be advertised. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_in</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].ipv4_acl_in") | String |  |  |  | Name of the IPv4 access-list to be assigned in the ingress direction.<br>The access-list must be defined under `ipv4_acls` and supports field substitution for "interface_ip" and "peer_ip".<br>Required for all WAN interfaces (`wan_carrier` is set) unless the carrier is marked as 'trusted' under `wan_carriers`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_out</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].ipv4_acl_out") | String |  |  |  | Name of the IPv4 Access-list to be assigned in the egress direction.<br>The access-list must be defined under `ipv4_acls` and supports field substitution for "interface_ip" and "peer_ip". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static_routes</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].static_routes") | List, items: Dictionary |  |  | Min Length: 1 | Configure IPv4 static routes pointing to `peer_ip`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].static_routes.[].prefix") | String | Required |  |  | IPv4_network/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].qos_profile") | String |  |  |  | QOS service profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_carrier</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].wan_carrier") | String |  |  |  | The WAN carrier this interface is connected to.<br>This is used to infer the path-groups in which this interface should be configured.<br>Unless the carrier is marked as 'trusted' under `wan_carriers`, `ipv4_acl_in` is also required on all WAN interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_circuit_id</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].wan_circuit_id") | String |  |  |  | The WAN circuit ID for this interface.<br>This is not rendered in the configuration but used for WAN designs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connected_to_pathfinder</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].connected_to_pathfinder") | Boolean |  | `True` |  | For a WAN interface (`wan_carrier` is set), allow to disable the static tunnel towards Pathfinders. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_internet_exit</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].cv_pathfinder_internet_exit") | Dictionary |  |  |  | PREVIEW: This key is in preview mode |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;policies</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].cv_pathfinder_internet_exit.policies") | List, items: Dictionary |  |  |  | List of Internet-exit policies using this interface as exit. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].cv_pathfinder_internet_exit.policies.[].name") | String | Required, Unique |  |  | Internet-exit policy name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tunnel_interface_numbers</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].cv_pathfinder_internet_exit.policies.[].tunnel_interface_numbers") | String |  |  |  | Number range to use for Tunnel interfaces to an internet-exit service provider using this local interface.<br>Examples: '1-3' or '100,200,300' |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flow_tracking</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].flow_tracking") | Dictionary |  |  |  | Configures flow-tracking on the interface. Overrides `fabric_flow_tracking.l3_interfaces` setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].flow_tracking.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].flow_tracking.name") | String |  |  |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<node_type_keys.key>.nodes.[].l3_interfaces.[].structured_config") | Dictionary |  |  |  | Custom structured config for the Ethernet interface. |
    | [<samp>l3_interface_profiles</samp>](## "l3_interface_profiles") | List, items: Dictionary |  |  |  | Profiles to inherit common settings for l3_interfaces defined under the node type key.<br>These profiles will *not* work for `l3_interfaces` defined under `vrfs`. |
    | [<samp>&nbsp;&nbsp;-&nbsp;profile</samp>](## "l3_interface_profiles.[].profile") | String | Required, Unique |  |  | L3 interface profile name. Any variable supported under `l3_interfaces` can be inherited from a profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "l3_interface_profiles.[].name") | String |  |  | Pattern: `Ethernet[\d/]+(.[\d]+)?` | Ethernet interface name like 'Ethernet2' or subinterface name like 'Ethernet2.42'.<br>For a subinterface, the parent physical interface is automatically created. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "l3_interface_profiles.[].description") | String |  |  |  | Interface description.<br>If not set a default description will be configured with '[<peer>[ <peer_interface>]]'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "l3_interface_profiles.[].ip_address") | String |  |  |  | Node IPv4 address/Mask or 'dhcp'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dhcp_ip</samp>](## "l3_interface_profiles.[].dhcp_ip") | String |  |  |  | When the `ip_address` is `dhcp`, this optional field allows to indicate the expected<br>IPv4 address (without mask) to be allocated on the interface if known.<br>This is not rendered in the configuration but can be used for substitution of 'interface_ip' in the Access-list<br>set under `ipv4_acl_in` and `ipv4_acl_out`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;public_ip</samp>](## "l3_interface_profiles.[].public_ip") | String |  |  |  | Node IPv4 address (no mask).<br><br>This is used to get the public IP (if known) when the device is behind NAT.<br>This is only used for `wan_rr` routers (AutoVPN RRs and Pathfinders) to determine the Public IP<br>with the following preference:<br>  `wan_route_servers.path_groups.interfaces.ip_address`<br>      -> `l3_interfaces.public_ip`<br>          -> `l3_interfaces.ip_address`<br><br>The determined Public IP is used by WAN routers when peering with this interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "l3_interface_profiles.[].encapsulation_dot1q_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dhcp_accept_default_route</samp>](## "l3_interface_profiles.[].dhcp_accept_default_route") | Boolean |  | `True` |  | Accept a default route from DHCP if `ip_address` is set to `dhcp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "l3_interface_profiles.[].enabled") | Boolean |  | `True` |  | Enable or Shutdown the interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "l3_interface_profiles.[].speed") | String |  |  |  | Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "l3_interface_profiles.[].peer") | String |  |  |  | The peer device name. Used for description and documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_interface</samp>](## "l3_interface_profiles.[].peer_interface") | String |  |  |  | The peer device interface. Used for description and documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;peer_ip</samp>](## "l3_interface_profiles.[].peer_ip") | String |  |  |  | The peer device IPv4 address (no mask). Used as default route gateway if `set_default_route` is true and `ip` is an IP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "l3_interface_profiles.[].bgp") | Dictionary |  |  |  | Enforce IPv4 BGP peering for the peer |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_as</samp>](## "l3_interface_profiles.[].bgp.peer_as") | String | Required |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_prefix_list_in</samp>](## "l3_interface_profiles.[].bgp.ipv4_prefix_list_in") | String |  |  |  | Prefix List Name. Accept routes for only these prefixes from the peer.<br>Required for wan interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_prefix_list_out</samp>](## "l3_interface_profiles.[].bgp.ipv4_prefix_list_out") | String |  |  |  | Prefix List Name. Advertise routes for only these prefixes.<br>If not specified, nothing would be advertised. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_in</samp>](## "l3_interface_profiles.[].ipv4_acl_in") | String |  |  |  | Name of the IPv4 access-list to be assigned in the ingress direction.<br>The access-list must be defined under `ipv4_acls` and supports field substitution for "interface_ip" and "peer_ip".<br>Required for all WAN interfaces (`wan_carrier` is set) unless the carrier is marked as 'trusted' under `wan_carriers`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_out</samp>](## "l3_interface_profiles.[].ipv4_acl_out") | String |  |  |  | Name of the IPv4 Access-list to be assigned in the egress direction.<br>The access-list must be defined under `ipv4_acls` and supports field substitution for "interface_ip" and "peer_ip". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;static_routes</samp>](## "l3_interface_profiles.[].static_routes") | List, items: Dictionary |  |  | Min Length: 1 | Configure IPv4 static routes pointing to `peer_ip`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;prefix</samp>](## "l3_interface_profiles.[].static_routes.[].prefix") | String | Required |  |  | IPv4_network/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;qos_profile</samp>](## "l3_interface_profiles.[].qos_profile") | String |  |  |  | QOS service profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;wan_carrier</samp>](## "l3_interface_profiles.[].wan_carrier") | String |  |  |  | The WAN carrier this interface is connected to.<br>This is used to infer the path-groups in which this interface should be configured.<br>Unless the carrier is marked as 'trusted' under `wan_carriers`, `ipv4_acl_in` is also required on all WAN interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;wan_circuit_id</samp>](## "l3_interface_profiles.[].wan_circuit_id") | String |  |  |  | The WAN circuit ID for this interface.<br>This is not rendered in the configuration but used for WAN designs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;connected_to_pathfinder</samp>](## "l3_interface_profiles.[].connected_to_pathfinder") | Boolean |  | `True` |  | For a WAN interface (`wan_carrier` is set), allow to disable the static tunnel towards Pathfinders. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_internet_exit</samp>](## "l3_interface_profiles.[].cv_pathfinder_internet_exit") | Dictionary |  |  |  | PREVIEW: This key is in preview mode |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;policies</samp>](## "l3_interface_profiles.[].cv_pathfinder_internet_exit.policies") | List, items: Dictionary |  |  |  | List of Internet-exit policies using this interface as exit. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "l3_interface_profiles.[].cv_pathfinder_internet_exit.policies.[].name") | String | Required, Unique |  |  | Internet-exit policy name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tunnel_interface_numbers</samp>](## "l3_interface_profiles.[].cv_pathfinder_internet_exit.policies.[].tunnel_interface_numbers") | String |  |  |  | Number range to use for Tunnel interfaces to an internet-exit service provider using this local interface.<br>Examples: '1-3' or '100,200,300' |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "l3_interface_profiles.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;flow_tracking</samp>](## "l3_interface_profiles.[].flow_tracking") | Dictionary |  |  |  | Configures flow-tracking on the interface. Overrides `fabric_flow_tracking.l3_interfaces` setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "l3_interface_profiles.[].flow_tracking.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "l3_interface_profiles.[].flow_tracking.name") | String |  |  |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "l3_interface_profiles.[].structured_config") | Dictionary |  |  |  | Custom structured config for the Ethernet interface. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:

        # L3 Interfaces to configure on the node.
        # Used to define the node for WAN interfaces when `wan_carrier` is set.
        l3_interfaces:

            # L3 interface profile name. Profile defined under `l3_interface_profiles`.
          - profile: <str>

            # Ethernet interface name like 'Ethernet2' or subinterface name like 'Ethernet2.42'.
            # For a subinterface, the parent physical interface is automatically created.
            name: <str; required; unique>

            # Interface description.
            # If not set a default description will be configured with '[<peer>[ <peer_interface>]]'.
            description: <str>

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
            #       -> `l3_interfaces.public_ip`
            #           -> `l3_interfaces.ip_address`
            #
            # The determined Public IP is used by WAN routers when peering with this interface.
            public_ip: <str>

            # For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified.
            encapsulation_dot1q_vlan: <int; 1-4094>

            # Accept a default route from DHCP if `ip_address` is set to `dhcp`.
            dhcp_accept_default_route: <bool; default=True>

            # Enable or Shutdown the interface.
            enabled: <bool; default=True>

            # Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
            speed: <str>

            # The peer device name. Used for description and documentation.
            peer: <str>

            # The peer device interface. Used for description and documentation.
            peer_interface: <str>

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
              - prefix: <str; required>

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

            # PREVIEW: This key is in preview mode
            cv_pathfinder_internet_exit:

              # List of Internet-exit policies using this interface as exit.
              policies:

                  # Internet-exit policy name.
                - name: <str; required; unique>

                  # Number range to use for Tunnel interfaces to an internet-exit service provider using this local interface.
                  # Examples: '1-3' or '100,200,300'
                  tunnel_interface_numbers: <str>

            # EOS CLI rendered directly on the interface in the final EOS configuration.
            raw_eos_cli: <str>

            # Configures flow-tracking on the interface. Overrides `fabric_flow_tracking.l3_interfaces` setting.
            flow_tracking:
              enabled: <bool>

              # Flow tracker name as defined in flow_tracking_settings.
              name: <str>

            # Custom structured config for the Ethernet interface.
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

              # L3 Interfaces to configure on the node.
              # Used to define the node for WAN interfaces when `wan_carrier` is set.
              l3_interfaces:

                  # L3 interface profile name. Profile defined under `l3_interface_profiles`.
                - profile: <str>

                  # Ethernet interface name like 'Ethernet2' or subinterface name like 'Ethernet2.42'.
                  # For a subinterface, the parent physical interface is automatically created.
                  name: <str; required; unique>

                  # Interface description.
                  # If not set a default description will be configured with '[<peer>[ <peer_interface>]]'.
                  description: <str>

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
                  #       -> `l3_interfaces.public_ip`
                  #           -> `l3_interfaces.ip_address`
                  #
                  # The determined Public IP is used by WAN routers when peering with this interface.
                  public_ip: <str>

                  # For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified.
                  encapsulation_dot1q_vlan: <int; 1-4094>

                  # Accept a default route from DHCP if `ip_address` is set to `dhcp`.
                  dhcp_accept_default_route: <bool; default=True>

                  # Enable or Shutdown the interface.
                  enabled: <bool; default=True>

                  # Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
                  speed: <str>

                  # The peer device name. Used for description and documentation.
                  peer: <str>

                  # The peer device interface. Used for description and documentation.
                  peer_interface: <str>

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
                    - prefix: <str; required>

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

                  # PREVIEW: This key is in preview mode
                  cv_pathfinder_internet_exit:

                    # List of Internet-exit policies using this interface as exit.
                    policies:

                        # Internet-exit policy name.
                      - name: <str; required; unique>

                        # Number range to use for Tunnel interfaces to an internet-exit service provider using this local interface.
                        # Examples: '1-3' or '100,200,300'
                        tunnel_interface_numbers: <str>

                  # EOS CLI rendered directly on the interface in the final EOS configuration.
                  raw_eos_cli: <str>

                  # Configures flow-tracking on the interface. Overrides `fabric_flow_tracking.l3_interfaces` setting.
                  flow_tracking:
                    enabled: <bool>

                    # Flow tracker name as defined in flow_tracking_settings.
                    name: <str>

                  # Custom structured config for the Ethernet interface.
                  structured_config: <dict>

          # L3 Interfaces to configure on the node.
          # Used to define the node for WAN interfaces when `wan_carrier` is set.
          l3_interfaces:

              # L3 interface profile name. Profile defined under `l3_interface_profiles`.
            - profile: <str>

              # Ethernet interface name like 'Ethernet2' or subinterface name like 'Ethernet2.42'.
              # For a subinterface, the parent physical interface is automatically created.
              name: <str; required; unique>

              # Interface description.
              # If not set a default description will be configured with '[<peer>[ <peer_interface>]]'.
              description: <str>

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
              #       -> `l3_interfaces.public_ip`
              #           -> `l3_interfaces.ip_address`
              #
              # The determined Public IP is used by WAN routers when peering with this interface.
              public_ip: <str>

              # For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified.
              encapsulation_dot1q_vlan: <int; 1-4094>

              # Accept a default route from DHCP if `ip_address` is set to `dhcp`.
              dhcp_accept_default_route: <bool; default=True>

              # Enable or Shutdown the interface.
              enabled: <bool; default=True>

              # Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
              speed: <str>

              # The peer device name. Used for description and documentation.
              peer: <str>

              # The peer device interface. Used for description and documentation.
              peer_interface: <str>

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
                - prefix: <str; required>

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

              # PREVIEW: This key is in preview mode
              cv_pathfinder_internet_exit:

                # List of Internet-exit policies using this interface as exit.
                policies:

                    # Internet-exit policy name.
                  - name: <str; required; unique>

                    # Number range to use for Tunnel interfaces to an internet-exit service provider using this local interface.
                    # Examples: '1-3' or '100,200,300'
                    tunnel_interface_numbers: <str>

              # EOS CLI rendered directly on the interface in the final EOS configuration.
              raw_eos_cli: <str>

              # Configures flow-tracking on the interface. Overrides `fabric_flow_tracking.l3_interfaces` setting.
              flow_tracking:
                enabled: <bool>

                # Flow tracker name as defined in flow_tracking_settings.
                name: <str>

              # Custom structured config for the Ethernet interface.
              structured_config: <dict>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>

          # L3 Interfaces to configure on the node.
          # Used to define the node for WAN interfaces when `wan_carrier` is set.
          l3_interfaces:

              # L3 interface profile name. Profile defined under `l3_interface_profiles`.
            - profile: <str>

              # Ethernet interface name like 'Ethernet2' or subinterface name like 'Ethernet2.42'.
              # For a subinterface, the parent physical interface is automatically created.
              name: <str; required; unique>

              # Interface description.
              # If not set a default description will be configured with '[<peer>[ <peer_interface>]]'.
              description: <str>

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
              #       -> `l3_interfaces.public_ip`
              #           -> `l3_interfaces.ip_address`
              #
              # The determined Public IP is used by WAN routers when peering with this interface.
              public_ip: <str>

              # For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified.
              encapsulation_dot1q_vlan: <int; 1-4094>

              # Accept a default route from DHCP if `ip_address` is set to `dhcp`.
              dhcp_accept_default_route: <bool; default=True>

              # Enable or Shutdown the interface.
              enabled: <bool; default=True>

              # Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
              speed: <str>

              # The peer device name. Used for description and documentation.
              peer: <str>

              # The peer device interface. Used for description and documentation.
              peer_interface: <str>

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
                - prefix: <str; required>

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

              # PREVIEW: This key is in preview mode
              cv_pathfinder_internet_exit:

                # List of Internet-exit policies using this interface as exit.
                policies:

                    # Internet-exit policy name.
                  - name: <str; required; unique>

                    # Number range to use for Tunnel interfaces to an internet-exit service provider using this local interface.
                    # Examples: '1-3' or '100,200,300'
                    tunnel_interface_numbers: <str>

              # EOS CLI rendered directly on the interface in the final EOS configuration.
              raw_eos_cli: <str>

              # Configures flow-tracking on the interface. Overrides `fabric_flow_tracking.l3_interfaces` setting.
              flow_tracking:
                enabled: <bool>

                # Flow tracker name as defined in flow_tracking_settings.
                name: <str>

              # Custom structured config for the Ethernet interface.
              structured_config: <dict>

    # Profiles to inherit common settings for l3_interfaces defined under the node type key.
    # These profiles will *not* work for `l3_interfaces` defined under `vrfs`.
    l3_interface_profiles:

        # L3 interface profile name. Any variable supported under `l3_interfaces` can be inherited from a profile.
      - profile: <str; required; unique>

        # Ethernet interface name like 'Ethernet2' or subinterface name like 'Ethernet2.42'.
        # For a subinterface, the parent physical interface is automatically created.
        name: <str>

        # Interface description.
        # If not set a default description will be configured with '[<peer>[ <peer_interface>]]'.
        description: <str>

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
        #       -> `l3_interfaces.public_ip`
        #           -> `l3_interfaces.ip_address`
        #
        # The determined Public IP is used by WAN routers when peering with this interface.
        public_ip: <str>

        # For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified.
        encapsulation_dot1q_vlan: <int; 1-4094>

        # Accept a default route from DHCP if `ip_address` is set to `dhcp`.
        dhcp_accept_default_route: <bool; default=True>

        # Enable or Shutdown the interface.
        enabled: <bool; default=True>

        # Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
        speed: <str>

        # The peer device name. Used for description and documentation.
        peer: <str>

        # The peer device interface. Used for description and documentation.
        peer_interface: <str>

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
          - prefix: <str; required>

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

        # PREVIEW: This key is in preview mode
        cv_pathfinder_internet_exit:

          # List of Internet-exit policies using this interface as exit.
          policies:

              # Internet-exit policy name.
            - name: <str; required; unique>

              # Number range to use for Tunnel interfaces to an internet-exit service provider using this local interface.
              # Examples: '1-3' or '100,200,300'
              tunnel_interface_numbers: <str>

        # EOS CLI rendered directly on the interface in the final EOS configuration.
        raw_eos_cli: <str>

        # Configures flow-tracking on the interface. Overrides `fabric_flow_tracking.l3_interfaces` setting.
        flow_tracking:
          enabled: <bool>

          # Flow tracker name as defined in flow_tracking_settings.
          name: <str>

        # Custom structured config for the Ethernet interface.
        structured_config: <dict>
    ```
