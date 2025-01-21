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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "<network_services_keys.name>.[].evpn_l2_multicast") | Dictionary |  |  |  | Enable EVPN L2 Multicast for all SVIs and l2vlans within Tenant.<br>- Multicast group binding is created only for Multicast traffic. BULL traffic will use ingress-replication.<br>- Configures binding between VXLAN, VLAN, and multicast group IPv4 address using the following formula:<br>  < evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool > + < vlan_id - 1 > + < evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool_offset >.<br>- The recommendation is to assign a /20 block within the 232.0.0.0/8 Source-Specific Multicast range.<br>- Enables `redistribute igmp` on the router bgp MAC VRF.<br>- When evpn_l2_multicast.enabled is true for a VLAN or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled - overriding those individual settings.<br>- Requires `evpn_multicast` to also be set to `true`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_l2_multicast_group_ipv4_pool</samp>](## "<network_services_keys.name>.[].evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool") | String |  |  |  | IPv4_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;underlay_l2_multicast_group_ipv4_pool_offset</samp>](## "<network_services_keys.name>.[].evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool_offset") | Integer |  | `0` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fast_leave</samp>](## "<network_services_keys.name>.[].evpn_l2_multicast.fast_leave") | Boolean |  |  |  | Enable IGMP snooping fast-leave feature for all SVIs and l2vlans within the Tenant. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_redistribute_igmp</samp>](## "<network_services_keys.name>.[].evpn_l2_multicast.always_redistribute_igmp") | Boolean |  |  |  | Always configure `redistribute igmp` under BGP for all SVIs within the Tenant if `evpn_l2_multicast` is True.<br>By default `redistribute igmp` is only configured when `evpn_l2_multicast` is True and `evpn_l3_multicast` for the VRF is False.<br>Configuring `redistribute igmp` when both L2 and L3 EVPN Multicast is enabled will take up additional control-plane and data-plane resources,<br>but it is required to support forwarding of TTL=1 multicast traffic within the VLAN.<br>This can be overridden per SVI. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "<network_services_keys.name>.[].evpn_l3_multicast") | Dictionary |  |  |  | Enable L3 Multicast for all SVIs and l3vlans within Tenant.<br>- In the evpn-l3ls design type, this enables L3 EVPN Multicast (aka OISM)'.<br>- Multicast group binding for VRF is created only for Multicast traffic. BULL traffic will use ingress-replication.<br>- Configures binding between VXLAN, VLAN, and multicast group IPv4 address using the following formula:<br>  < l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool > + < vrf_id - 1 > + < l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool_offset >.<br>- The recommendation is to assign a /20 block within the 232.0.0.0/8 Source-Specific Multicast range.<br>- If enabled on an SVI using the anycast default gateway feature, a diagnostic loopback (see below) MUST be configured to source IGMP traffic.<br>- Enables `evpn multicast` on the router bgp VRF.<br>- When enabled on an SVI:<br>     - If switch is part of an MLAG pair, enables "pim ipv4 sparse-mode" on the SVI.<br>     - If switch is standalone or A-A MH, enables "ip igmp" on the SVI.<br>     - If "ip address virtual" is configured, enables "pim ipv4 local-interface" and uses the diagnostic Loopback defined in the VRF<br>- Requires `evpn_multicast` to also be set to `true`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_underlay_l3_multicast_group_ipv4_pool</samp>](## "<network_services_keys.name>.[].evpn_l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool") | String | Required |  |  | IPv4_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_underlay_l3_multicast_group_ipv4_pool_offset</samp>](## "<network_services_keys.name>.[].evpn_l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool_offset") | Integer |  | `0` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_peg</samp>](## "<network_services_keys.name>.[].evpn_l3_multicast.evpn_peg") | List, items: Dictionary |  |  |  | For each group of nodes, allow configuration of EVPN PEG options.<br>The first group of settings where the device's hostname is present in the 'nodes' list will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;nodes</samp>](## "<network_services_keys.name>.[].evpn_l3_multicast.evpn_peg.[].nodes") | List, items: String |  |  |  | A description will be applied to all nodes with RP addresses configured if not set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].evpn_l3_multicast.evpn_peg.[].nodes.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transit</samp>](## "<network_services_keys.name>.[].evpn_l3_multicast.evpn_peg.[].transit") | Boolean |  |  |  | Enable EVPN PEG transit mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pim_rp_addresses</samp>](## "<network_services_keys.name>.[].pim_rp_addresses") | List, items: Dictionary |  |  |  | For each group of nodes, allow configuration of RP Addresses & associated groups.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;rps</samp>](## "<network_services_keys.name>.[].pim_rp_addresses.[].rps") | List, items: String |  |  | Min Length: 1 | List of Rendevouz Points. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].pim_rp_addresses.[].rps.[]") | String |  |  |  | RP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<network_services_keys.name>.[].pim_rp_addresses.[].nodes") | List, items: String |  |  |  | Restrict configuration to specific nodes.<br>Configuration Will be applied to all nodes if not set.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].pim_rp_addresses.[].nodes.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "<network_services_keys.name>.[].pim_rp_addresses.[].groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].pim_rp_addresses.[].groups.[]") | String |  |  |  | Group_prefix/mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_list_name</samp>](## "<network_services_keys.name>.[].pim_rp_addresses.[].access_list_name") | String |  |  |  | List of groups to associate with the RP address set in 'rp'.<br>If access_list_name is set, a standard access-list will be configured matching these groups.<br>Otherwise the groups are configured directly on the RP command.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "<network_services_keys.name>.[].igmp_snooping_querier") | Dictionary |  |  |  | Enable IGMP snooping querier for each SVI/l2vlan within tenant, by default using IP address of Loopback 0.<br>When enabled, IGMP snooping querier will only be configured on L3 devices, i.e., uplink_type: p2p.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if "evpn_l2_multicast" is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "<network_services_keys.name>.[].igmp_snooping_querier.source_address") | String |  |  | Format: ipv4 | Default IP address of Loopback0. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "<network_services_keys.name>.[].igmp_snooping_querier.version") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code><br>- <code>3</code> | IGMP Version (By default EOS uses IGMP version 2 for IGMP querier). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "<network_services_keys.name>.[].vrfs") | List, items: Dictionary |  |  |  | VRFs will only be configured on a node if any of the underlying objects like `svis` or `l3_interfaces` apply to the node.<br><br>It is recommended to only define a VRF in one Tenant. If the same VRF name is used across multiple tenants and those tenants<br>are accepted by `filter.tenants` on the node, any object set under the duplicate VRFs must either be unique or be an exact match.<br><br>VRF "default" is partially supported under network-services. Currently the supported options for "default" vrf are route-target,<br>route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.<br>Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<network_services_keys.name>.[].vrfs.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "<network_services_keys.name>.[].vrfs.[].evpn_l3_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l3_multicast to override setting of `<network_services_key>.[].evpn_l3_multicast.enabled`.<br>Allow override of `<network_services_key>.[].evpn_l3_multicast` node_settings.<br>Requires `evpn_multicast` to also be set to `true`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_underlay_l3_multicast_group</samp>](## "<network_services_keys.name>.[].vrfs.[].evpn_l3_multicast.evpn_underlay_l3_multicast_group") | String |  |  |  | IPv4 address of evpn underlay l3 multicast group.<br>To override multicast range set using the formula < l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool > + < vrf_id - 1 > + < l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool_offset >. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_peg</samp>](## "<network_services_keys.name>.[].vrfs.[].evpn_l3_multicast.evpn_peg") | List, items: Dictionary |  |  |  | For each group of nodes, allow configuration of EVPN PEG features. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;nodes</samp>](## "<network_services_keys.name>.[].vrfs.[].evpn_l3_multicast.evpn_peg.[].nodes") | List, items: String |  |  |  | Restrict configuration to specific nodes.<br>Will apply to all nodes with RP addresses configured if not set.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].evpn_l3_multicast.evpn_peg.[].nodes.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transit</samp>](## "<network_services_keys.name>.[].vrfs.[].evpn_l3_multicast.evpn_peg.[].transit") | Boolean |  | `False` |  | Enable EVPN PEG transit mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pim_rp_addresses</samp>](## "<network_services_keys.name>.[].vrfs.[].pim_rp_addresses") | List, items: Dictionary |  |  |  | For each group of nodes, allow configuration of RP Addresses & associated groups.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;rps</samp>](## "<network_services_keys.name>.[].vrfs.[].pim_rp_addresses.[].rps") | List, items: String |  |  |  | A minimum of one RP must be specified. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].pim_rp_addresses.[].rps.[]") | String |  |  |  | RP address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<network_services_keys.name>.[].vrfs.[].pim_rp_addresses.[].nodes") | List, items: String |  |  |  | Restrict configuration to specific nodes.<br>Configuration Will be applied to all nodes if not set.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].pim_rp_addresses.[].nodes.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "<network_services_keys.name>.[].vrfs.[].pim_rp_addresses.[].groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].pim_rp_addresses.[].groups.[]") | String |  |  |  | Group_prefix/mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_list_name</samp>](## "<network_services_keys.name>.[].vrfs.[].pim_rp_addresses.[].access_list_name") | String |  |  |  | List of groups to associate with the RP addresses set in 'rps'.<br>If access_list_name is set, a standard access-list will be configured matching these groups.<br>Otherwise the groups are configured directly on the RP command.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;svis</samp>](## "<network_services_keys.name>.[].vrfs.[].svis") | List, items: Dictionary |  |  |  | List of SVIs.<br>This will create both the L3 SVI and L2 VLAN based on filters applied to the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].id") | Integer | Required |  | Min: 1<br>Max: 4096 | SVI interface id and VLAN id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes") | List, items: Dictionary |  |  |  | Define node specific configuration, such as unique IP addresses.<br>Any keys set here will be merged onto the SVI config, except `structured_config` keys which will replace the `structured_config` set on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;node</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].node") | String | Required, Unique |  |  | Node inventory hostname. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].evpn_l2_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l2_multicast to override setting of `<network_services_key>.[].evpn_l2_multicast.enabled`.<br>When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled, overriding those individual settings.<br>Requires `evpn_multicast` to also be set to `true`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_redistribute_igmp</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].evpn_l2_multicast.always_redistribute_igmp") | Boolean |  |  |  | Always configure `redistribute igmp` under BGP for the VLAN. Overrides the setting of `<network_services_key>.[].evpn_l2_multicast.always_redistribute_igmp`.<br>By default `redistribute igmp` is only configured when `evpn_l2_multicast` is True and `evpn_l3_multicast` for the VRF is False.<br>Configuring `redistribute igmp` when both L2 and L3 EVPN Multicast is enabled will take up additional control-plane and data-plane resources,<br>but it is required to support forwarding of TTL=1 multicast traffic within the VLAN. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].evpn_l3_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l3_multicast to override setting of `<network_services_key>.[].evpn_l3_multicast.enabled` and `<network_services_key>.[].vrfs.[].evpn_l3_multicast.enabled`.<br>Requires `evpn_multicast` to also be set to `true`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].igmp_snooping_enabled") | Boolean |  |  |  | Enable or disable IGMP snooping (Enabled by default on EOS). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].igmp_snooping_querier") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if evpn_l2_multicast is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].igmp_snooping_querier.source_address") | String |  |  |  | IPv4_address<br>If not set, IP address of "Loopback0" will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].igmp_snooping_querier.version") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code><br>- <code>3</code> | IGMP Version (By default EOS uses IGMP version 2 for IGMP querier). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fast_leave</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].nodes.[].igmp_snooping_querier.fast_leave") | Boolean |  |  |  | Enable IGMP snooping fast-leave feature. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].evpn_l2_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l2_multicast to override setting of `<network_services_key>.[].evpn_l2_multicast.enabled`.<br>When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled, overriding those individual settings.<br>Requires `evpn_multicast` to also be set to `true`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_redistribute_igmp</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].evpn_l2_multicast.always_redistribute_igmp") | Boolean |  |  |  | Always configure `redistribute igmp` under BGP for the VLAN. Overrides the setting of `<network_services_key>.[].evpn_l2_multicast.always_redistribute_igmp`.<br>By default `redistribute igmp` is only configured when `evpn_l2_multicast` is True and `evpn_l3_multicast` for the VRF is False.<br>Configuring `redistribute igmp` when both L2 and L3 EVPN Multicast is enabled will take up additional control-plane and data-plane resources,<br>but it is required to support forwarding of TTL=1 multicast traffic within the VLAN. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].evpn_l3_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l3_multicast to override setting of `<network_services_key>.[].evpn_l3_multicast.enabled` and `<network_services_key>.[].vrfs.[].evpn_l3_multicast.enabled`.<br>Requires `evpn_multicast` to also be set to `true`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].igmp_snooping_enabled") | Boolean |  |  |  | Enable or disable IGMP snooping (Enabled by default on EOS). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].igmp_snooping_querier") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if evpn_l2_multicast is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].igmp_snooping_querier.source_address") | String |  |  |  | IPv4_address<br>If not set, IP address of "Loopback0" will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].igmp_snooping_querier.version") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code><br>- <code>3</code> | IGMP Version (By default EOS uses IGMP version 2 for IGMP querier). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fast_leave</samp>](## "<network_services_keys.name>.[].vrfs.[].svis.[].igmp_snooping_querier.fast_leave") | Boolean |  |  |  | Enable IGMP snooping fast-leave feature. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2vlans</samp>](## "<network_services_keys.name>.[].l2vlans") | List, items: Dictionary |  |  |  | Define L2 network services organized by vlan id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "<network_services_keys.name>.[].l2vlans.[].id") | Integer | Required |  | Min: 1<br>Max: 4094 | VLAN ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "<network_services_keys.name>.[].l2vlans.[].evpn_l2_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l2_multicast to override setting of `<network_services_key>.[].evpn_l2_multicast.enabled`.<br>When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, igmp snooping and igmp snooping querier will always be enabled, overriding those individual settings.<br>Requires `evpn_multicast` to also be set to `true`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].l2vlans.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "<network_services_keys.name>.[].l2vlans.[].igmp_snooping_enabled") | Boolean |  |  |  | Enable or disable IGMP snooping (Enabled by default on EOS). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "<network_services_keys.name>.[].l2vlans.[].igmp_snooping_querier") | Dictionary |  |  |  | Enable igmp snooping querier, by default using IP address of Loopback 0.<br>When enabled, igmp snooping querier will only be configured on l3 devices, i.e., uplink_type: p2p.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].l2vlans.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if evpn_l2_multicast is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "<network_services_keys.name>.[].l2vlans.[].igmp_snooping_querier.source_address") | String |  |  |  | IPv4_address<br>If not set, IP address of "Loopback0" will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "<network_services_keys.name>.[].l2vlans.[].igmp_snooping_querier.version") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code><br>- <code>3</code> | IGMP Version (By default EOS uses IGMP version 2 for IGMP querier). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fast_leave</samp>](## "<network_services_keys.name>.[].l2vlans.[].igmp_snooping_querier.fast_leave") | Boolean |  |  |  | Enable IGMP snooping fast-leave feature. |
    | [<samp>svi_profiles</samp>](## "svi_profiles") | List, items: Dictionary |  |  |  | Profiles to share common settings for SVIs under `<network_services_key>.[].vrfs.svis`.<br>Keys are the same used under SVIs. Keys defined under SVIs take precedence.<br>Note: structured configuration is not merged recursively and will be taken directly from the most specific level in the following order:<br>1. svi.nodes[inventory_hostname].structured_config<br>2. svi_profile.nodes[inventory_hostname].structured_config<br>3. svi_parent_profile.nodes[inventory_hostname].structured_config<br>4. svi.structured_config<br>5. svi_profile.structured_config<br>6. svi_parent_profile.structured_config<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;profile</samp>](## "svi_profiles.[].profile") | String | Required, Unique |  |  | Profile name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "svi_profiles.[].nodes") | List, items: Dictionary |  |  |  | Define node specific configuration, such as unique IP addresses.<br>Any keys set here will be merged onto the SVI config, except `structured_config` keys which will replace the `structured_config` set on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;node</samp>](## "svi_profiles.[].nodes.[].node") | String | Required, Unique |  |  | Node inventory hostname. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "svi_profiles.[].nodes.[].evpn_l2_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l2_multicast to override setting of `<network_services_key>.[].evpn_l2_multicast.enabled`.<br>When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled, overriding those individual settings.<br>Requires `evpn_multicast` to also be set to `true`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].nodes.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_redistribute_igmp</samp>](## "svi_profiles.[].nodes.[].evpn_l2_multicast.always_redistribute_igmp") | Boolean |  |  |  | Always configure `redistribute igmp` under BGP for the VLAN. Overrides the setting of `<network_services_key>.[].evpn_l2_multicast.always_redistribute_igmp`.<br>By default `redistribute igmp` is only configured when `evpn_l2_multicast` is True and `evpn_l3_multicast` for the VRF is False.<br>Configuring `redistribute igmp` when both L2 and L3 EVPN Multicast is enabled will take up additional control-plane and data-plane resources,<br>but it is required to support forwarding of TTL=1 multicast traffic within the VLAN. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "svi_profiles.[].nodes.[].evpn_l3_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l3_multicast to override setting of `<network_services_key>.[].evpn_l3_multicast.enabled` and `<network_services_key>.[].vrfs.[].evpn_l3_multicast.enabled`.<br>Requires `evpn_multicast` to also be set to `true`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].nodes.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "svi_profiles.[].nodes.[].igmp_snooping_enabled") | Boolean |  |  |  | Enable or disable IGMP snooping (Enabled by default on EOS). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "svi_profiles.[].nodes.[].igmp_snooping_querier") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].nodes.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if evpn_l2_multicast is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "svi_profiles.[].nodes.[].igmp_snooping_querier.source_address") | String |  |  |  | IPv4_address<br>If not set, IP address of "Loopback0" will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "svi_profiles.[].nodes.[].igmp_snooping_querier.version") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code><br>- <code>3</code> | IGMP Version (By default EOS uses IGMP version 2 for IGMP querier). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fast_leave</samp>](## "svi_profiles.[].nodes.[].igmp_snooping_querier.fast_leave") | Boolean |  |  |  | Enable IGMP snooping fast-leave feature. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multicast</samp>](## "svi_profiles.[].evpn_l2_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l2_multicast to override setting of `<network_services_key>.[].evpn_l2_multicast.enabled`.<br>When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled, overriding those individual settings.<br>Requires `evpn_multicast` to also be set to `true`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].evpn_l2_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_redistribute_igmp</samp>](## "svi_profiles.[].evpn_l2_multicast.always_redistribute_igmp") | Boolean |  |  |  | Always configure `redistribute igmp` under BGP for the VLAN. Overrides the setting of `<network_services_key>.[].evpn_l2_multicast.always_redistribute_igmp`.<br>By default `redistribute igmp` is only configured when `evpn_l2_multicast` is True and `evpn_l3_multicast` for the VRF is False.<br>Configuring `redistribute igmp` when both L2 and L3 EVPN Multicast is enabled will take up additional control-plane and data-plane resources,<br>but it is required to support forwarding of TTL=1 multicast traffic within the VLAN. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_l3_multicast</samp>](## "svi_profiles.[].evpn_l3_multicast") | Dictionary |  |  |  | Explicitly enable or disable evpn_l3_multicast to override setting of `<network_services_key>.[].evpn_l3_multicast.enabled` and `<network_services_key>.[].vrfs.[].evpn_l3_multicast.enabled`.<br>Requires `evpn_multicast` to also be set to `true`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].evpn_l3_multicast.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "svi_profiles.[].igmp_snooping_enabled") | Boolean |  |  |  | Enable or disable IGMP snooping (Enabled by default on EOS). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_querier</samp>](## "svi_profiles.[].igmp_snooping_querier") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].igmp_snooping_querier.enabled") | Boolean |  |  |  | Will be enabled automatically if evpn_l2_multicast is enabled. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "svi_profiles.[].igmp_snooping_querier.source_address") | String |  |  |  | IPv4_address<br>If not set, IP address of "Loopback0" will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "svi_profiles.[].igmp_snooping_querier.version") | Integer |  |  | Valid Values:<br>- <code>1</code><br>- <code>2</code><br>- <code>3</code> | IGMP Version (By default EOS uses IGMP version 2 for IGMP querier). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fast_leave</samp>](## "svi_profiles.[].igmp_snooping_querier.fast_leave") | Boolean |  |  |  | Enable IGMP snooping fast-leave feature. |

=== "YAML"

    ```yaml
    <network_services_keys.name>:

        # Specify a tenant name.
        # Tenant provide a construct to group L3 VRFs and L2 VLANs.
        # Networks services can be filtered by tenant name.
      - name: <str; required; unique>

        # Enable EVPN L2 Multicast for all SVIs and l2vlans within Tenant.
        # - Multicast group binding is created only for Multicast traffic. BULL traffic will use ingress-replication.
        # - Configures binding between VXLAN, VLAN, and multicast group IPv4 address using the following formula:
        #   < evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool > + < vlan_id - 1 > + < evpn_l2_multicast.underlay_l2_multicast_group_ipv4_pool_offset >.
        # - The recommendation is to assign a /20 block within the 232.0.0.0/8 Source-Specific Multicast range.
        # - Enables `redistribute igmp` on the router bgp MAC VRF.
        # - When evpn_l2_multicast.enabled is true for a VLAN or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled - overriding those individual settings.
        # - Requires `evpn_multicast` to also be set to `true`.
        evpn_l2_multicast:
          enabled: <bool>

          # IPv4_address/Mask.
          underlay_l2_multicast_group_ipv4_pool: <str>
          underlay_l2_multicast_group_ipv4_pool_offset: <int; default=0>

          # Enable IGMP snooping fast-leave feature for all SVIs and l2vlans within the Tenant.
          fast_leave: <bool>

          # Always configure `redistribute igmp` under BGP for all SVIs within the Tenant if `evpn_l2_multicast` is True.
          # By default `redistribute igmp` is only configured when `evpn_l2_multicast` is True and `evpn_l3_multicast` for the VRF is False.
          # Configuring `redistribute igmp` when both L2 and L3 EVPN Multicast is enabled will take up additional control-plane and data-plane resources,
          # but it is required to support forwarding of TTL=1 multicast traffic within the VLAN.
          # This can be overridden per SVI.
          always_redistribute_igmp: <bool>

        # Enable L3 Multicast for all SVIs and l3vlans within Tenant.
        # - In the evpn-l3ls design type, this enables L3 EVPN Multicast (aka OISM)'.
        # - Multicast group binding for VRF is created only for Multicast traffic. BULL traffic will use ingress-replication.
        # - Configures binding between VXLAN, VLAN, and multicast group IPv4 address using the following formula:
        #   < l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool > + < vrf_id - 1 > + < l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool_offset >.
        # - The recommendation is to assign a /20 block within the 232.0.0.0/8 Source-Specific Multicast range.
        # - If enabled on an SVI using the anycast default gateway feature, a diagnostic loopback (see below) MUST be configured to source IGMP traffic.
        # - Enables `evpn multicast` on the router bgp VRF.
        # - When enabled on an SVI:
        #      - If switch is part of an MLAG pair, enables "pim ipv4 sparse-mode" on the SVI.
        #      - If switch is standalone or A-A MH, enables "ip igmp" on the SVI.
        #      - If "ip address virtual" is configured, enables "pim ipv4 local-interface" and uses the diagnostic Loopback defined in the VRF
        # - Requires `evpn_multicast` to also be set to `true`.
        evpn_l3_multicast:
          enabled: <bool>

          # IPv4_address/Mask.
          evpn_underlay_l3_multicast_group_ipv4_pool: <str; required>
          evpn_underlay_l3_multicast_group_ipv4_pool_offset: <int; default=0>

          # For each group of nodes, allow configuration of EVPN PEG options.
          # The first group of settings where the device's hostname is present in the 'nodes' list will be used.
          evpn_peg:

              # A description will be applied to all nodes with RP addresses configured if not set.
            - nodes:
                - <str>

              # Enable EVPN PEG transit mode.
              transit: <bool>

        # For each group of nodes, allow configuration of RP Addresses & associated groups.
        pim_rp_addresses:

            # List of Rendevouz Points.
          - rps: # >=1 items

                # RP address.
              - <str>

            # Restrict configuration to specific nodes.
            # Configuration Will be applied to all nodes if not set.
            nodes:
              - <str>
            groups:

                # Group_prefix/mask.
              - <str>

            # List of groups to associate with the RP address set in 'rp'.
            # If access_list_name is set, a standard access-list will be configured matching these groups.
            # Otherwise the groups are configured directly on the RP command.
            access_list_name: <str>

        # Enable IGMP snooping querier for each SVI/l2vlan within tenant, by default using IP address of Loopback 0.
        # When enabled, IGMP snooping querier will only be configured on L3 devices, i.e., uplink_type: p2p.
        igmp_snooping_querier:

          # Will be enabled automatically if "evpn_l2_multicast" is enabled.
          enabled: <bool>

          # Default IP address of Loopback0.
          source_address: <str>

          # IGMP Version (By default EOS uses IGMP version 2 for IGMP querier).
          version: <int; 1 | 2 | 3>

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

            # Explicitly enable or disable evpn_l3_multicast to override setting of `<network_services_key>.[].evpn_l3_multicast.enabled`.
            # Allow override of `<network_services_key>.[].evpn_l3_multicast` node_settings.
            # Requires `evpn_multicast` to also be set to `true`.
            evpn_l3_multicast:
              enabled: <bool>

              # IPv4 address of evpn underlay l3 multicast group.
              # To override multicast range set using the formula < l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool > + < vrf_id - 1 > + < l3_multicast.evpn_underlay_l3_multicast_group_ipv4_pool_offset >.
              evpn_underlay_l3_multicast_group: <str>

              # For each group of nodes, allow configuration of EVPN PEG features.
              evpn_peg:

                  # Restrict configuration to specific nodes.
                  # Will apply to all nodes with RP addresses configured if not set.
                - nodes:
                    - <str>

                  # Enable EVPN PEG transit mode.
                  transit: <bool; default=False>

            # For each group of nodes, allow configuration of RP Addresses & associated groups.
            pim_rp_addresses:

                # A minimum of one RP must be specified.
              - rps:

                    # RP address.
                  - <str>

                # Restrict configuration to specific nodes.
                # Configuration Will be applied to all nodes if not set.
                nodes:
                  - <str>
                groups:

                    # Group_prefix/mask.
                  - <str>

                # List of groups to associate with the RP addresses set in 'rps'.
                # If access_list_name is set, a standard access-list will be configured matching these groups.
                # Otherwise the groups are configured directly on the RP command.
                access_list_name: <str>

            # List of SVIs.
            # This will create both the L3 SVI and L2 VLAN based on filters applied to the node.
            svis:

                # SVI interface id and VLAN id.
              - id: <int; 1-4096; required>

                # Define node specific configuration, such as unique IP addresses.
                # Any keys set here will be merged onto the SVI config, except `structured_config` keys which will replace the `structured_config` set on SVI level.
                nodes:

                    # Node inventory hostname.
                  - node: <str; required; unique>

                    # Explicitly enable or disable evpn_l2_multicast to override setting of `<network_services_key>.[].evpn_l2_multicast.enabled`.
                    # When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled, overriding those individual settings.
                    # Requires `evpn_multicast` to also be set to `true`.
                    evpn_l2_multicast:
                      enabled: <bool>

                      # Always configure `redistribute igmp` under BGP for the VLAN. Overrides the setting of `<network_services_key>.[].evpn_l2_multicast.always_redistribute_igmp`.
                      # By default `redistribute igmp` is only configured when `evpn_l2_multicast` is True and `evpn_l3_multicast` for the VRF is False.
                      # Configuring `redistribute igmp` when both L2 and L3 EVPN Multicast is enabled will take up additional control-plane and data-plane resources,
                      # but it is required to support forwarding of TTL=1 multicast traffic within the VLAN.
                      always_redistribute_igmp: <bool>

                    # Explicitly enable or disable evpn_l3_multicast to override setting of `<network_services_key>.[].evpn_l3_multicast.enabled` and `<network_services_key>.[].vrfs.[].evpn_l3_multicast.enabled`.
                    # Requires `evpn_multicast` to also be set to `true`.
                    evpn_l3_multicast:
                      enabled: <bool>

                    # Enable or disable IGMP snooping (Enabled by default on EOS).
                    igmp_snooping_enabled: <bool>
                    igmp_snooping_querier:

                      # Will be enabled automatically if evpn_l2_multicast is enabled.
                      enabled: <bool>

                      # IPv4_address
                      # If not set, IP address of "Loopback0" will be used.
                      source_address: <str>

                      # IGMP Version (By default EOS uses IGMP version 2 for IGMP querier).
                      version: <int; 1 | 2 | 3>

                      # Enable IGMP snooping fast-leave feature.
                      fast_leave: <bool>

                # Explicitly enable or disable evpn_l2_multicast to override setting of `<network_services_key>.[].evpn_l2_multicast.enabled`.
                # When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled, overriding those individual settings.
                # Requires `evpn_multicast` to also be set to `true`.
                evpn_l2_multicast:
                  enabled: <bool>

                  # Always configure `redistribute igmp` under BGP for the VLAN. Overrides the setting of `<network_services_key>.[].evpn_l2_multicast.always_redistribute_igmp`.
                  # By default `redistribute igmp` is only configured when `evpn_l2_multicast` is True and `evpn_l3_multicast` for the VRF is False.
                  # Configuring `redistribute igmp` when both L2 and L3 EVPN Multicast is enabled will take up additional control-plane and data-plane resources,
                  # but it is required to support forwarding of TTL=1 multicast traffic within the VLAN.
                  always_redistribute_igmp: <bool>

                # Explicitly enable or disable evpn_l3_multicast to override setting of `<network_services_key>.[].evpn_l3_multicast.enabled` and `<network_services_key>.[].vrfs.[].evpn_l3_multicast.enabled`.
                # Requires `evpn_multicast` to also be set to `true`.
                evpn_l3_multicast:
                  enabled: <bool>

                # Enable or disable IGMP snooping (Enabled by default on EOS).
                igmp_snooping_enabled: <bool>
                igmp_snooping_querier:

                  # Will be enabled automatically if evpn_l2_multicast is enabled.
                  enabled: <bool>

                  # IPv4_address
                  # If not set, IP address of "Loopback0" will be used.
                  source_address: <str>

                  # IGMP Version (By default EOS uses IGMP version 2 for IGMP querier).
                  version: <int; 1 | 2 | 3>

                  # Enable IGMP snooping fast-leave feature.
                  fast_leave: <bool>

        # Define L2 network services organized by vlan id.
        l2vlans:

            # VLAN ID.
          - id: <int; 1-4094; required>

            # Explicitly enable or disable evpn_l2_multicast to override setting of `<network_services_key>.[].evpn_l2_multicast.enabled`.
            # When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, igmp snooping and igmp snooping querier will always be enabled, overriding those individual settings.
            # Requires `evpn_multicast` to also be set to `true`.
            evpn_l2_multicast:
              enabled: <bool>

            # Enable or disable IGMP snooping (Enabled by default on EOS).
            igmp_snooping_enabled: <bool>

            # Enable igmp snooping querier, by default using IP address of Loopback 0.
            # When enabled, igmp snooping querier will only be configured on l3 devices, i.e., uplink_type: p2p.
            igmp_snooping_querier:

              # Will be enabled automatically if evpn_l2_multicast is enabled.
              enabled: <bool>

              # IPv4_address
              # If not set, IP address of "Loopback0" will be used.
              source_address: <str>

              # IGMP Version (By default EOS uses IGMP version 2 for IGMP querier).
              version: <int; 1 | 2 | 3>

              # Enable IGMP snooping fast-leave feature.
              fast_leave: <bool>

    # Profiles to share common settings for SVIs under `<network_services_key>.[].vrfs.svis`.
    # Keys are the same used under SVIs. Keys defined under SVIs take precedence.
    # Note: structured configuration is not merged recursively and will be taken directly from the most specific level in the following order:
    # 1. svi.nodes[inventory_hostname].structured_config
    # 2. svi_profile.nodes[inventory_hostname].structured_config
    # 3. svi_parent_profile.nodes[inventory_hostname].structured_config
    # 4. svi.structured_config
    # 5. svi_profile.structured_config
    # 6. svi_parent_profile.structured_config
    svi_profiles:

        # Profile name.
      - profile: <str; required; unique>

        # Define node specific configuration, such as unique IP addresses.
        # Any keys set here will be merged onto the SVI config, except `structured_config` keys which will replace the `structured_config` set on SVI level.
        nodes:

            # Node inventory hostname.
          - node: <str; required; unique>

            # Explicitly enable or disable evpn_l2_multicast to override setting of `<network_services_key>.[].evpn_l2_multicast.enabled`.
            # When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled, overriding those individual settings.
            # Requires `evpn_multicast` to also be set to `true`.
            evpn_l2_multicast:
              enabled: <bool>

              # Always configure `redistribute igmp` under BGP for the VLAN. Overrides the setting of `<network_services_key>.[].evpn_l2_multicast.always_redistribute_igmp`.
              # By default `redistribute igmp` is only configured when `evpn_l2_multicast` is True and `evpn_l3_multicast` for the VRF is False.
              # Configuring `redistribute igmp` when both L2 and L3 EVPN Multicast is enabled will take up additional control-plane and data-plane resources,
              # but it is required to support forwarding of TTL=1 multicast traffic within the VLAN.
              always_redistribute_igmp: <bool>

            # Explicitly enable or disable evpn_l3_multicast to override setting of `<network_services_key>.[].evpn_l3_multicast.enabled` and `<network_services_key>.[].vrfs.[].evpn_l3_multicast.enabled`.
            # Requires `evpn_multicast` to also be set to `true`.
            evpn_l3_multicast:
              enabled: <bool>

            # Enable or disable IGMP snooping (Enabled by default on EOS).
            igmp_snooping_enabled: <bool>
            igmp_snooping_querier:

              # Will be enabled automatically if evpn_l2_multicast is enabled.
              enabled: <bool>

              # IPv4_address
              # If not set, IP address of "Loopback0" will be used.
              source_address: <str>

              # IGMP Version (By default EOS uses IGMP version 2 for IGMP querier).
              version: <int; 1 | 2 | 3>

              # Enable IGMP snooping fast-leave feature.
              fast_leave: <bool>

        # Explicitly enable or disable evpn_l2_multicast to override setting of `<network_services_key>.[].evpn_l2_multicast.enabled`.
        # When evpn_l2_multicast.enabled is set to true for a vlan or a tenant, "igmp snooping" and "igmp snooping querier" will always be enabled, overriding those individual settings.
        # Requires `evpn_multicast` to also be set to `true`.
        evpn_l2_multicast:
          enabled: <bool>

          # Always configure `redistribute igmp` under BGP for the VLAN. Overrides the setting of `<network_services_key>.[].evpn_l2_multicast.always_redistribute_igmp`.
          # By default `redistribute igmp` is only configured when `evpn_l2_multicast` is True and `evpn_l3_multicast` for the VRF is False.
          # Configuring `redistribute igmp` when both L2 and L3 EVPN Multicast is enabled will take up additional control-plane and data-plane resources,
          # but it is required to support forwarding of TTL=1 multicast traffic within the VLAN.
          always_redistribute_igmp: <bool>

        # Explicitly enable or disable evpn_l3_multicast to override setting of `<network_services_key>.[].evpn_l3_multicast.enabled` and `<network_services_key>.[].vrfs.[].evpn_l3_multicast.enabled`.
        # Requires `evpn_multicast` to also be set to `true`.
        evpn_l3_multicast:
          enabled: <bool>

        # Enable or disable IGMP snooping (Enabled by default on EOS).
        igmp_snooping_enabled: <bool>
        igmp_snooping_querier:

          # Will be enabled automatically if evpn_l2_multicast is enabled.
          enabled: <bool>

          # IPv4_address
          # If not set, IP address of "Loopback0" will be used.
          source_address: <str>

          # IGMP Version (By default EOS uses IGMP version 2 for IGMP querier).
          version: <int; 1 | 2 | 3>

          # Enable IGMP snooping fast-leave feature.
          fast_leave: <bool>
    ```
