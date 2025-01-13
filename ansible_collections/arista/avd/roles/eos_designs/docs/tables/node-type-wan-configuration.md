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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;wan_role</samp>](## "<node_type_keys.key>.defaults.wan_role") | String |  |  | Valid Values:<br>- <code>client</code><br>- <code>server</code> | Override the default WAN role.<br><br>This is used both for AutoVPN and Pathfinder designs.<br>That means if `wan_mode` root key is set to `autovpn` or `cv-pathfinder`.<br>`server` indicates that the router is a route-reflector.<br><br>Only supported if `overlay_routing_protocol` is set to `ibgp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_transit_mode</samp>](## "<node_type_keys.key>.defaults.cv_pathfinder_transit_mode") | String |  |  | Valid Values:<br>- <code>region</code><br>- <code>zone</code> | Configure the transit mode for a WAN client for CV Pathfinder designs<br>only when the `wan_mode` root key is set to `cv_pathfinder`.<br><br>'zone' is currently not supported. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_region</samp>](## "<node_type_keys.key>.defaults.cv_pathfinder_region") | String |  |  |  | The CV Pathfinder region name.<br>This key is required for WAN routers but optional for pathfinders.<br>The region name must be defined under 'cv_pathfinder_regions'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_site</samp>](## "<node_type_keys.key>.defaults.cv_pathfinder_site") | String |  |  |  | The CV Pathfinder site name.<br>This key is required for WAN routers but optional for pathfinders.<br>For WAN routers and pathfinders with `cv_pathfinder_region`, the site name must be defined for the relevant region under 'cv_pathfinder_regions'.<br>For pathfinders without `cv_pathfinder_region` set, the site must be defined under `cv_pathfinder_global_sites`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;wan_ha</samp>](## "<node_type_keys.key>.defaults.wan_ha") | Dictionary |  |  |  | PREVIEW: This key is currently not supported<br><br>The key is supported only if `wan_mode` == `cv-pathfinder`.<br>AutoVPN support is still to be determined.<br><br>Maximum 2 devices supported by group for HA. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.defaults.wan_ha.enabled") | Boolean |  |  |  | Enable / Disable auto CV-Pathfinder HA, when two nodes are defined in the same node_group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipsec</samp>](## "<node_type_keys.key>.defaults.wan_ha.ipsec") | Boolean |  | `True` |  | Enable / Disable IPsec over HA path-group when HA is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "<node_type_keys.key>.defaults.wan_ha.mtu") | Integer |  | `9194` | Min: 68<br>Max: 65535 | Set MTU on WAN HA interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ha_interfaces</samp>](## "<node_type_keys.key>.defaults.wan_ha.ha_interfaces") | List, items: String |  |  |  | Local WAN HA interfaces<br>Overwrite the default behavior which is to pick all the `uplink_interfaces`.<br>Can be used to filter uplink interfaces when there are multiple uplinks.<br>Limitations:<br>  Either all interfaces must be uplinks or all interfaces must not be uplinks.<br>  Only one interface is supported for non uplinks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.defaults.wan_ha.ha_interfaces.[]") | String |  |  | Pattern: `Ethernet[\d/]+` |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ha_ipv4_pool</samp>](## "<node_type_keys.key>.defaults.wan_ha.ha_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for WAN HA connectivity.<br>IP is derived from the node ID.<br>Not used for uplink interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_ha_interfaces</samp>](## "<node_type_keys.key>.defaults.wan_ha.max_ha_interfaces") | Integer |  |  |  | Number of parallel links towards HA switches.<br>Can be used to reserve IP addresses for future parallel HA links. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_channel_id</samp>](## "<node_type_keys.key>.defaults.wan_ha.port_channel_id") | Integer |  |  |  | Port-channel ID to use for direct HA. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use_port_channel_for_direct_ha</samp>](## "<node_type_keys.key>.defaults.wan_ha.use_port_channel_for_direct_ha") | Boolean |  | `True` |  | Enable or disable using a port-channel interface for direct HA when there is only one interface.<br>This feature was introduced in EOS 4.33.0F. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flow_tracking</samp>](## "<node_type_keys.key>.defaults.wan_ha.flow_tracking") | Dictionary |  |  |  | Configures flow-tracking on the HA interfaces. Overrides `fabric_flow_tracking.wan_ha_links` setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.defaults.wan_ha.flow_tracking.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<node_type_keys.key>.defaults.wan_ha.flow_tracking.name") | String |  |  |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dps_mss_ipv4</samp>](## "<node_type_keys.key>.defaults.dps_mss_ipv4") | String |  | `auto` |  | IPv4 MSS value configured under "router path-selection" on WAN Devices. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_role</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].wan_role") | String |  |  | Valid Values:<br>- <code>client</code><br>- <code>server</code> | Override the default WAN role.<br><br>This is used both for AutoVPN and Pathfinder designs.<br>That means if `wan_mode` root key is set to `autovpn` or `cv-pathfinder`.<br>`server` indicates that the router is a route-reflector.<br><br>Only supported if `overlay_routing_protocol` is set to `ibgp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_transit_mode</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].cv_pathfinder_transit_mode") | String |  |  | Valid Values:<br>- <code>region</code><br>- <code>zone</code> | Configure the transit mode for a WAN client for CV Pathfinder designs<br>only when the `wan_mode` root key is set to `cv_pathfinder`.<br><br>'zone' is currently not supported. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_region</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].cv_pathfinder_region") | String |  |  |  | The CV Pathfinder region name.<br>This key is required for WAN routers but optional for pathfinders.<br>The region name must be defined under 'cv_pathfinder_regions'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_site</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].cv_pathfinder_site") | String |  |  |  | The CV Pathfinder site name.<br>This key is required for WAN routers but optional for pathfinders.<br>For WAN routers and pathfinders with `cv_pathfinder_region`, the site name must be defined for the relevant region under 'cv_pathfinder_regions'.<br>For pathfinders without `cv_pathfinder_region` set, the site must be defined under `cv_pathfinder_global_sites`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_ha</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].wan_ha") | Dictionary |  |  |  | PREVIEW: This key is currently not supported<br><br>The key is supported only if `wan_mode` == `cv-pathfinder`.<br>AutoVPN support is still to be determined.<br><br>Maximum 2 devices supported by group for HA. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].wan_ha.enabled") | Boolean |  |  |  | Enable / Disable auto CV-Pathfinder HA, when two nodes are defined in the same node_group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipsec</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].wan_ha.ipsec") | Boolean |  | `True` |  | Enable / Disable IPsec over HA path-group when HA is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].wan_ha.mtu") | Integer |  | `9194` | Min: 68<br>Max: 65535 | Set MTU on WAN HA interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ha_interfaces</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].wan_ha.ha_interfaces") | List, items: String |  |  |  | Local WAN HA interfaces<br>Overwrite the default behavior which is to pick all the `uplink_interfaces`.<br>Can be used to filter uplink interfaces when there are multiple uplinks.<br>Limitations:<br>  Either all interfaces must be uplinks or all interfaces must not be uplinks.<br>  Only one interface is supported for non uplinks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].wan_ha.ha_interfaces.[]") | String |  |  | Pattern: `Ethernet[\d/]+` |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ha_ipv4_pool</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].wan_ha.ha_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for WAN HA connectivity.<br>IP is derived from the node ID.<br>Not used for uplink interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_ha_interfaces</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].wan_ha.max_ha_interfaces") | Integer |  |  |  | Number of parallel links towards HA switches.<br>Can be used to reserve IP addresses for future parallel HA links. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_channel_id</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].wan_ha.port_channel_id") | Integer |  |  |  | Port-channel ID to use for direct HA. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use_port_channel_for_direct_ha</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].wan_ha.use_port_channel_for_direct_ha") | Boolean |  | `True` |  | Enable or disable using a port-channel interface for direct HA when there is only one interface.<br>This feature was introduced in EOS 4.33.0F. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flow_tracking</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].wan_ha.flow_tracking") | Dictionary |  |  |  | Configures flow-tracking on the HA interfaces. Overrides `fabric_flow_tracking.wan_ha_links` setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].wan_ha.flow_tracking.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].wan_ha.flow_tracking.name") | String |  |  |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dps_mss_ipv4</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].dps_mss_ipv4") | String |  | `auto` |  | IPv4 MSS value configured under "router path-selection" on WAN Devices. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_role</samp>](## "<node_type_keys.key>.node_groups.[].wan_role") | String |  |  | Valid Values:<br>- <code>client</code><br>- <code>server</code> | Override the default WAN role.<br><br>This is used both for AutoVPN and Pathfinder designs.<br>That means if `wan_mode` root key is set to `autovpn` or `cv-pathfinder`.<br>`server` indicates that the router is a route-reflector.<br><br>Only supported if `overlay_routing_protocol` is set to `ibgp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_transit_mode</samp>](## "<node_type_keys.key>.node_groups.[].cv_pathfinder_transit_mode") | String |  |  | Valid Values:<br>- <code>region</code><br>- <code>zone</code> | Configure the transit mode for a WAN client for CV Pathfinder designs<br>only when the `wan_mode` root key is set to `cv_pathfinder`.<br><br>'zone' is currently not supported. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_region</samp>](## "<node_type_keys.key>.node_groups.[].cv_pathfinder_region") | String |  |  |  | The CV Pathfinder region name.<br>This key is required for WAN routers but optional for pathfinders.<br>The region name must be defined under 'cv_pathfinder_regions'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_site</samp>](## "<node_type_keys.key>.node_groups.[].cv_pathfinder_site") | String |  |  |  | The CV Pathfinder site name.<br>This key is required for WAN routers but optional for pathfinders.<br>For WAN routers and pathfinders with `cv_pathfinder_region`, the site name must be defined for the relevant region under 'cv_pathfinder_regions'.<br>For pathfinders without `cv_pathfinder_region` set, the site must be defined under `cv_pathfinder_global_sites`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_ha</samp>](## "<node_type_keys.key>.node_groups.[].wan_ha") | Dictionary |  |  |  | PREVIEW: This key is currently not supported<br><br>The key is supported only if `wan_mode` == `cv-pathfinder`.<br>AutoVPN support is still to be determined.<br><br>Maximum 2 devices supported by group for HA. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].wan_ha.enabled") | Boolean |  |  |  | Enable / Disable auto CV-Pathfinder HA, when two nodes are defined in the same node_group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipsec</samp>](## "<node_type_keys.key>.node_groups.[].wan_ha.ipsec") | Boolean |  | `True` |  | Enable / Disable IPsec over HA path-group when HA is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "<node_type_keys.key>.node_groups.[].wan_ha.mtu") | Integer |  | `9194` | Min: 68<br>Max: 65535 | Set MTU on WAN HA interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ha_interfaces</samp>](## "<node_type_keys.key>.node_groups.[].wan_ha.ha_interfaces") | List, items: String |  |  |  | Local WAN HA interfaces<br>Overwrite the default behavior which is to pick all the `uplink_interfaces`.<br>Can be used to filter uplink interfaces when there are multiple uplinks.<br>Limitations:<br>  Either all interfaces must be uplinks or all interfaces must not be uplinks.<br>  Only one interface is supported for non uplinks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].wan_ha.ha_interfaces.[]") | String |  |  | Pattern: `Ethernet[\d/]+` |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ha_ipv4_pool</samp>](## "<node_type_keys.key>.node_groups.[].wan_ha.ha_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for WAN HA connectivity.<br>IP is derived from the node ID.<br>Not used for uplink interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_ha_interfaces</samp>](## "<node_type_keys.key>.node_groups.[].wan_ha.max_ha_interfaces") | Integer |  |  |  | Number of parallel links towards HA switches.<br>Can be used to reserve IP addresses for future parallel HA links. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_channel_id</samp>](## "<node_type_keys.key>.node_groups.[].wan_ha.port_channel_id") | Integer |  |  |  | Port-channel ID to use for direct HA. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use_port_channel_for_direct_ha</samp>](## "<node_type_keys.key>.node_groups.[].wan_ha.use_port_channel_for_direct_ha") | Boolean |  | `True` |  | Enable or disable using a port-channel interface for direct HA when there is only one interface.<br>This feature was introduced in EOS 4.33.0F. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flow_tracking</samp>](## "<node_type_keys.key>.node_groups.[].wan_ha.flow_tracking") | Dictionary |  |  |  | Configures flow-tracking on the HA interfaces. Overrides `fabric_flow_tracking.wan_ha_links` setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].wan_ha.flow_tracking.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].wan_ha.flow_tracking.name") | String |  |  |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dps_mss_ipv4</samp>](## "<node_type_keys.key>.node_groups.[].dps_mss_ipv4") | String |  | `auto` |  | IPv4 MSS value configured under "router path-selection" on WAN Devices. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_role</samp>](## "<node_type_keys.key>.nodes.[].wan_role") | String |  |  | Valid Values:<br>- <code>client</code><br>- <code>server</code> | Override the default WAN role.<br><br>This is used both for AutoVPN and Pathfinder designs.<br>That means if `wan_mode` root key is set to `autovpn` or `cv-pathfinder`.<br>`server` indicates that the router is a route-reflector.<br><br>Only supported if `overlay_routing_protocol` is set to `ibgp`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_transit_mode</samp>](## "<node_type_keys.key>.nodes.[].cv_pathfinder_transit_mode") | String |  |  | Valid Values:<br>- <code>region</code><br>- <code>zone</code> | Configure the transit mode for a WAN client for CV Pathfinder designs<br>only when the `wan_mode` root key is set to `cv_pathfinder`.<br><br>'zone' is currently not supported. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_region</samp>](## "<node_type_keys.key>.nodes.[].cv_pathfinder_region") | String |  |  |  | The CV Pathfinder region name.<br>This key is required for WAN routers but optional for pathfinders.<br>The region name must be defined under 'cv_pathfinder_regions'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cv_pathfinder_site</samp>](## "<node_type_keys.key>.nodes.[].cv_pathfinder_site") | String |  |  |  | The CV Pathfinder site name.<br>This key is required for WAN routers but optional for pathfinders.<br>For WAN routers and pathfinders with `cv_pathfinder_region`, the site name must be defined for the relevant region under 'cv_pathfinder_regions'.<br>For pathfinders without `cv_pathfinder_region` set, the site must be defined under `cv_pathfinder_global_sites`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_ha</samp>](## "<node_type_keys.key>.nodes.[].wan_ha") | Dictionary |  |  |  | PREVIEW: This key is currently not supported<br><br>The key is supported only if `wan_mode` == `cv-pathfinder`.<br>AutoVPN support is still to be determined.<br><br>Maximum 2 devices supported by group for HA. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.nodes.[].wan_ha.enabled") | Boolean |  |  |  | Enable / Disable auto CV-Pathfinder HA, when two nodes are defined in the same node_group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipsec</samp>](## "<node_type_keys.key>.nodes.[].wan_ha.ipsec") | Boolean |  | `True` |  | Enable / Disable IPsec over HA path-group when HA is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "<node_type_keys.key>.nodes.[].wan_ha.mtu") | Integer |  | `9194` | Min: 68<br>Max: 65535 | Set MTU on WAN HA interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ha_interfaces</samp>](## "<node_type_keys.key>.nodes.[].wan_ha.ha_interfaces") | List, items: String |  |  |  | Local WAN HA interfaces<br>Overwrite the default behavior which is to pick all the `uplink_interfaces`.<br>Can be used to filter uplink interfaces when there are multiple uplinks.<br>Limitations:<br>  Either all interfaces must be uplinks or all interfaces must not be uplinks.<br>  Only one interface is supported for non uplinks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.nodes.[].wan_ha.ha_interfaces.[]") | String |  |  | Pattern: `Ethernet[\d/]+` |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ha_ipv4_pool</samp>](## "<node_type_keys.key>.nodes.[].wan_ha.ha_ipv4_pool") | String |  |  | Format: ipv4_cidr | IP address pool used for WAN HA connectivity.<br>IP is derived from the node ID.<br>Not used for uplink interfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_ha_interfaces</samp>](## "<node_type_keys.key>.nodes.[].wan_ha.max_ha_interfaces") | Integer |  |  |  | Number of parallel links towards HA switches.<br>Can be used to reserve IP addresses for future parallel HA links. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_channel_id</samp>](## "<node_type_keys.key>.nodes.[].wan_ha.port_channel_id") | Integer |  |  |  | Port-channel ID to use for direct HA. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use_port_channel_for_direct_ha</samp>](## "<node_type_keys.key>.nodes.[].wan_ha.use_port_channel_for_direct_ha") | Boolean |  | `True` |  | Enable or disable using a port-channel interface for direct HA when there is only one interface.<br>This feature was introduced in EOS 4.33.0F. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flow_tracking</samp>](## "<node_type_keys.key>.nodes.[].wan_ha.flow_tracking") | Dictionary |  |  |  | Configures flow-tracking on the HA interfaces. Overrides `fabric_flow_tracking.wan_ha_links` setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.nodes.[].wan_ha.flow_tracking.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].wan_ha.flow_tracking.name") | String |  |  |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dps_mss_ipv4</samp>](## "<node_type_keys.key>.nodes.[].dps_mss_ipv4") | String |  | `auto` |  | IPv4 MSS value configured under "router path-selection" on WAN Devices. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:

        # Override the default WAN role.
        #
        # This is used both for AutoVPN and Pathfinder designs.
        # That means if `wan_mode` root key is set to `autovpn` or `cv-pathfinder`.
        # `server` indicates that the router is a route-reflector.
        #
        # Only supported if `overlay_routing_protocol` is set to `ibgp`.
        wan_role: <str; "client" | "server">

        # Configure the transit mode for a WAN client for CV Pathfinder designs
        # only when the `wan_mode` root key is set to `cv_pathfinder`.
        #
        # 'zone' is currently not supported.
        cv_pathfinder_transit_mode: <str; "region" | "zone">

        # The CV Pathfinder region name.
        # This key is required for WAN routers but optional for pathfinders.
        # The region name must be defined under 'cv_pathfinder_regions'.
        cv_pathfinder_region: <str>

        # The CV Pathfinder site name.
        # This key is required for WAN routers but optional for pathfinders.
        # For WAN routers and pathfinders with `cv_pathfinder_region`, the site name must be defined for the relevant region under 'cv_pathfinder_regions'.
        # For pathfinders without `cv_pathfinder_region` set, the site must be defined under `cv_pathfinder_global_sites`.
        cv_pathfinder_site: <str>

        # PREVIEW: This key is currently not supported
        #
        # The key is supported only if `wan_mode` == `cv-pathfinder`.
        # AutoVPN support is still to be determined.
        #
        # Maximum 2 devices supported by group for HA.
        wan_ha:

          # Enable / Disable auto CV-Pathfinder HA, when two nodes are defined in the same node_group.
          enabled: <bool>

          # Enable / Disable IPsec over HA path-group when HA is enabled.
          ipsec: <bool; default=True>

          # Set MTU on WAN HA interfaces.
          mtu: <int; 68-65535; default=9194>

          # Local WAN HA interfaces
          # Overwrite the default behavior which is to pick all the `uplink_interfaces`.
          # Can be used to filter uplink interfaces when there are multiple uplinks.
          # Limitations:
          #   Either all interfaces must be uplinks or all interfaces must not be uplinks.
          #   Only one interface is supported for non uplinks.
          ha_interfaces:
            - <str>

          # IP address pool used for WAN HA connectivity.
          # IP is derived from the node ID.
          # Not used for uplink interfaces.
          ha_ipv4_pool: <str>

          # Number of parallel links towards HA switches.
          # Can be used to reserve IP addresses for future parallel HA links.
          max_ha_interfaces: <int>

          # Port-channel ID to use for direct HA.
          port_channel_id: <int>

          # Enable or disable using a port-channel interface for direct HA when there is only one interface.
          # This feature was introduced in EOS 4.33.0F.
          use_port_channel_for_direct_ha: <bool; default=True>

          # Configures flow-tracking on the HA interfaces. Overrides `fabric_flow_tracking.wan_ha_links` setting.
          flow_tracking:
            enabled: <bool>

            # Flow tracker name as defined in flow_tracking_settings.
            name: <str>

        # IPv4 MSS value configured under "router path-selection" on WAN Devices.
        dps_mss_ipv4: <str; default="auto">

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>

              # Override the default WAN role.
              #
              # This is used both for AutoVPN and Pathfinder designs.
              # That means if `wan_mode` root key is set to `autovpn` or `cv-pathfinder`.
              # `server` indicates that the router is a route-reflector.
              #
              # Only supported if `overlay_routing_protocol` is set to `ibgp`.
              wan_role: <str; "client" | "server">

              # Configure the transit mode for a WAN client for CV Pathfinder designs
              # only when the `wan_mode` root key is set to `cv_pathfinder`.
              #
              # 'zone' is currently not supported.
              cv_pathfinder_transit_mode: <str; "region" | "zone">

              # The CV Pathfinder region name.
              # This key is required for WAN routers but optional for pathfinders.
              # The region name must be defined under 'cv_pathfinder_regions'.
              cv_pathfinder_region: <str>

              # The CV Pathfinder site name.
              # This key is required for WAN routers but optional for pathfinders.
              # For WAN routers and pathfinders with `cv_pathfinder_region`, the site name must be defined for the relevant region under 'cv_pathfinder_regions'.
              # For pathfinders without `cv_pathfinder_region` set, the site must be defined under `cv_pathfinder_global_sites`.
              cv_pathfinder_site: <str>

              # PREVIEW: This key is currently not supported
              #
              # The key is supported only if `wan_mode` == `cv-pathfinder`.
              # AutoVPN support is still to be determined.
              #
              # Maximum 2 devices supported by group for HA.
              wan_ha:

                # Enable / Disable auto CV-Pathfinder HA, when two nodes are defined in the same node_group.
                enabled: <bool>

                # Enable / Disable IPsec over HA path-group when HA is enabled.
                ipsec: <bool; default=True>

                # Set MTU on WAN HA interfaces.
                mtu: <int; 68-65535; default=9194>

                # Local WAN HA interfaces
                # Overwrite the default behavior which is to pick all the `uplink_interfaces`.
                # Can be used to filter uplink interfaces when there are multiple uplinks.
                # Limitations:
                #   Either all interfaces must be uplinks or all interfaces must not be uplinks.
                #   Only one interface is supported for non uplinks.
                ha_interfaces:
                  - <str>

                # IP address pool used for WAN HA connectivity.
                # IP is derived from the node ID.
                # Not used for uplink interfaces.
                ha_ipv4_pool: <str>

                # Number of parallel links towards HA switches.
                # Can be used to reserve IP addresses for future parallel HA links.
                max_ha_interfaces: <int>

                # Port-channel ID to use for direct HA.
                port_channel_id: <int>

                # Enable or disable using a port-channel interface for direct HA when there is only one interface.
                # This feature was introduced in EOS 4.33.0F.
                use_port_channel_for_direct_ha: <bool; default=True>

                # Configures flow-tracking on the HA interfaces. Overrides `fabric_flow_tracking.wan_ha_links` setting.
                flow_tracking:
                  enabled: <bool>

                  # Flow tracker name as defined in flow_tracking_settings.
                  name: <str>

              # IPv4 MSS value configured under "router path-selection" on WAN Devices.
              dps_mss_ipv4: <str; default="auto">

          # Override the default WAN role.
          #
          # This is used both for AutoVPN and Pathfinder designs.
          # That means if `wan_mode` root key is set to `autovpn` or `cv-pathfinder`.
          # `server` indicates that the router is a route-reflector.
          #
          # Only supported if `overlay_routing_protocol` is set to `ibgp`.
          wan_role: <str; "client" | "server">

          # Configure the transit mode for a WAN client for CV Pathfinder designs
          # only when the `wan_mode` root key is set to `cv_pathfinder`.
          #
          # 'zone' is currently not supported.
          cv_pathfinder_transit_mode: <str; "region" | "zone">

          # The CV Pathfinder region name.
          # This key is required for WAN routers but optional for pathfinders.
          # The region name must be defined under 'cv_pathfinder_regions'.
          cv_pathfinder_region: <str>

          # The CV Pathfinder site name.
          # This key is required for WAN routers but optional for pathfinders.
          # For WAN routers and pathfinders with `cv_pathfinder_region`, the site name must be defined for the relevant region under 'cv_pathfinder_regions'.
          # For pathfinders without `cv_pathfinder_region` set, the site must be defined under `cv_pathfinder_global_sites`.
          cv_pathfinder_site: <str>

          # PREVIEW: This key is currently not supported
          #
          # The key is supported only if `wan_mode` == `cv-pathfinder`.
          # AutoVPN support is still to be determined.
          #
          # Maximum 2 devices supported by group for HA.
          wan_ha:

            # Enable / Disable auto CV-Pathfinder HA, when two nodes are defined in the same node_group.
            enabled: <bool>

            # Enable / Disable IPsec over HA path-group when HA is enabled.
            ipsec: <bool; default=True>

            # Set MTU on WAN HA interfaces.
            mtu: <int; 68-65535; default=9194>

            # Local WAN HA interfaces
            # Overwrite the default behavior which is to pick all the `uplink_interfaces`.
            # Can be used to filter uplink interfaces when there are multiple uplinks.
            # Limitations:
            #   Either all interfaces must be uplinks or all interfaces must not be uplinks.
            #   Only one interface is supported for non uplinks.
            ha_interfaces:
              - <str>

            # IP address pool used for WAN HA connectivity.
            # IP is derived from the node ID.
            # Not used for uplink interfaces.
            ha_ipv4_pool: <str>

            # Number of parallel links towards HA switches.
            # Can be used to reserve IP addresses for future parallel HA links.
            max_ha_interfaces: <int>

            # Port-channel ID to use for direct HA.
            port_channel_id: <int>

            # Enable or disable using a port-channel interface for direct HA when there is only one interface.
            # This feature was introduced in EOS 4.33.0F.
            use_port_channel_for_direct_ha: <bool; default=True>

            # Configures flow-tracking on the HA interfaces. Overrides `fabric_flow_tracking.wan_ha_links` setting.
            flow_tracking:
              enabled: <bool>

              # Flow tracker name as defined in flow_tracking_settings.
              name: <str>

          # IPv4 MSS value configured under "router path-selection" on WAN Devices.
          dps_mss_ipv4: <str; default="auto">

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>

          # Override the default WAN role.
          #
          # This is used both for AutoVPN and Pathfinder designs.
          # That means if `wan_mode` root key is set to `autovpn` or `cv-pathfinder`.
          # `server` indicates that the router is a route-reflector.
          #
          # Only supported if `overlay_routing_protocol` is set to `ibgp`.
          wan_role: <str; "client" | "server">

          # Configure the transit mode for a WAN client for CV Pathfinder designs
          # only when the `wan_mode` root key is set to `cv_pathfinder`.
          #
          # 'zone' is currently not supported.
          cv_pathfinder_transit_mode: <str; "region" | "zone">

          # The CV Pathfinder region name.
          # This key is required for WAN routers but optional for pathfinders.
          # The region name must be defined under 'cv_pathfinder_regions'.
          cv_pathfinder_region: <str>

          # The CV Pathfinder site name.
          # This key is required for WAN routers but optional for pathfinders.
          # For WAN routers and pathfinders with `cv_pathfinder_region`, the site name must be defined for the relevant region under 'cv_pathfinder_regions'.
          # For pathfinders without `cv_pathfinder_region` set, the site must be defined under `cv_pathfinder_global_sites`.
          cv_pathfinder_site: <str>

          # PREVIEW: This key is currently not supported
          #
          # The key is supported only if `wan_mode` == `cv-pathfinder`.
          # AutoVPN support is still to be determined.
          #
          # Maximum 2 devices supported by group for HA.
          wan_ha:

            # Enable / Disable auto CV-Pathfinder HA, when two nodes are defined in the same node_group.
            enabled: <bool>

            # Enable / Disable IPsec over HA path-group when HA is enabled.
            ipsec: <bool; default=True>

            # Set MTU on WAN HA interfaces.
            mtu: <int; 68-65535; default=9194>

            # Local WAN HA interfaces
            # Overwrite the default behavior which is to pick all the `uplink_interfaces`.
            # Can be used to filter uplink interfaces when there are multiple uplinks.
            # Limitations:
            #   Either all interfaces must be uplinks or all interfaces must not be uplinks.
            #   Only one interface is supported for non uplinks.
            ha_interfaces:
              - <str>

            # IP address pool used for WAN HA connectivity.
            # IP is derived from the node ID.
            # Not used for uplink interfaces.
            ha_ipv4_pool: <str>

            # Number of parallel links towards HA switches.
            # Can be used to reserve IP addresses for future parallel HA links.
            max_ha_interfaces: <int>

            # Port-channel ID to use for direct HA.
            port_channel_id: <int>

            # Enable or disable using a port-channel interface for direct HA when there is only one interface.
            # This feature was introduced in EOS 4.33.0F.
            use_port_channel_for_direct_ha: <bool; default=True>

            # Configures flow-tracking on the HA interfaces. Overrides `fabric_flow_tracking.wan_ha_links` setting.
            flow_tracking:
              enabled: <bool>

              # Flow tracker name as defined in flow_tracking_settings.
              name: <str>

          # IPv4 MSS value configured under "router path-selection" on WAN Devices.
          dps_mss_ipv4: <str; default="auto">
    ```
