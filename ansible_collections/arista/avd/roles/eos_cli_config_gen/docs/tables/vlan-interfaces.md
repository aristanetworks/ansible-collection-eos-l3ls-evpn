<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>vlan_interfaces</samp>](## "vlan_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "vlan_interfaces.[].name") | String | Required, Unique |  |  | VLAN interface name like "Vlan123". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "vlan_interfaces.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "vlan_interfaces.[].logging") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;event</samp>](## "vlan_interfaces.[].logging.event") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_status</samp>](## "vlan_interfaces.[].logging.event.link_status") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "vlan_interfaces.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "vlan_interfaces.[].vrf") | String |  |  |  | VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;arp_aging_timeout</samp>](## "vlan_interfaces.[].arp_aging_timeout") | Integer |  |  | Min: 1<br>Max: 65535 | In seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;arp_cache_dynamic_capacity</samp>](## "vlan_interfaces.[].arp_cache_dynamic_capacity") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;arp_gratuitous_accept</samp>](## "vlan_interfaces.[].arp_gratuitous_accept") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;arp_monitor_mac_address</samp>](## "vlan_interfaces.[].arp_monitor_mac_address") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_proxy_arp</samp>](## "vlan_interfaces.[].ip_proxy_arp") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_directed_broadcast</samp>](## "vlan_interfaces.[].ip_directed_broadcast") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "vlan_interfaces.[].ip_address") | String |  |  |  | IPv4_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address_secondaries</samp>](## "vlan_interfaces.[].ip_address_secondaries") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "vlan_interfaces.[].ip_address_secondaries.[]") | String |  |  |  | IPv4_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_virtual_router_addresses</samp>](## "vlan_interfaces.[].ip_virtual_router_addresses") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "vlan_interfaces.[].ip_virtual_router_addresses.[]") | String |  |  |  | IPv4 address or IPv4_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual</samp>](## "vlan_interfaces.[].ip_address_virtual") | String |  |  |  | IPv4_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual_secondaries</samp>](## "vlan_interfaces.[].ip_address_virtual_secondaries") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "vlan_interfaces.[].ip_address_virtual_secondaries.[]") | String |  |  |  | IPv4_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_verify_unicast_source_reachable_via</samp>](## "vlan_interfaces.[].ip_verify_unicast_source_reachable_via") | String |  |  | Valid Values:<br>- <code>any</code><br>- <code>rx</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_igmp</samp>](## "vlan_interfaces.[].ip_igmp") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_igmp_version</samp>](## "vlan_interfaces.[].ip_igmp_version") | Integer |  |  | Min: 1<br>Max: 3 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_igmp_host_proxy</samp>](## "vlan_interfaces.[].ip_igmp_host_proxy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "vlan_interfaces.[].ip_igmp_host_proxy.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "vlan_interfaces.[].ip_igmp_host_proxy.groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "vlan_interfaces.[].ip_igmp_host_proxy.groups.[].group") | String | Required, Unique |  |  | Multicast Address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exclude</samp>](## "vlan_interfaces.[].ip_igmp_host_proxy.groups.[].exclude") | List, items: Dictionary |  |  |  | The same source must not be present both in `exclude` and `include` list. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;source</samp>](## "vlan_interfaces.[].ip_igmp_host_proxy.groups.[].exclude.[].source") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;include</samp>](## "vlan_interfaces.[].ip_igmp_host_proxy.groups.[].include") | List, items: Dictionary |  |  |  | The same source must not be present both in `exclude` and `include` list. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;source</samp>](## "vlan_interfaces.[].ip_igmp_host_proxy.groups.[].include.[].source") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;report_interval</samp>](## "vlan_interfaces.[].ip_igmp_host_proxy.report_interval") | Integer |  |  | Min: 1<br>Max: 31744 | Time interval between unsolicited reports. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_lists</samp>](## "vlan_interfaces.[].ip_igmp_host_proxy.access_lists") | List, items: Dictionary |  |  |  | Non-standard Access List name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "vlan_interfaces.[].ip_igmp_host_proxy.access_lists.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "vlan_interfaces.[].ip_igmp_host_proxy.version") | Integer |  |  | Min: 1<br>Max: 3 | IGMP version on IGMP host-proxy interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "vlan_interfaces.[].ip_helpers") | List, items: Dictionary |  |  |  | List of DHCP servers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_helper</samp>](## "vlan_interfaces.[].ip_helpers.[].ip_helper") | String | Required, Unique |  |  | IP address or hostname of DHCP server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "vlan_interfaces.[].ip_helpers.[].source_interface") | String |  |  |  | Interface used as source for forwarded DHCP packets. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "vlan_interfaces.[].ip_helpers.[].vrf") | String |  |  |  | VRF where DHCP server can be reached. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_dhcp_relay_all_subnets</samp>](## "vlan_interfaces.[].ip_dhcp_relay_all_subnets") | Boolean |  |  |  | Allow forwarding requests with secondary IP addresses in the gateway address "giaddr" field. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_nat</samp>](## "vlan_interfaces.[].ip_nat") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "vlan_interfaces.[].ip_nat.destination") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic</samp>](## "vlan_interfaces.[].ip_nat.destination.dynamic") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;access_list</samp>](## "vlan_interfaces.[].ip_nat.destination.dynamic.[].access_list") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "vlan_interfaces.[].ip_nat.destination.dynamic.[].comment") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pool_name</samp>](## "vlan_interfaces.[].ip_nat.destination.dynamic.[].pool_name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "vlan_interfaces.[].ip_nat.destination.dynamic.[].priority") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "vlan_interfaces.[].ip_nat.destination.static") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;access_list</samp>](## "vlan_interfaces.[].ip_nat.destination.static.[].access_list") | String |  |  |  | 'access_list' and 'group' are mutual exclusive. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "vlan_interfaces.[].ip_nat.destination.static.[].comment") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "vlan_interfaces.[].ip_nat.destination.static.[].direction") | String |  |  | Valid Values:<br>- <code>egress</code><br>- <code>ingress</code> | Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.<br>EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "vlan_interfaces.[].ip_nat.destination.static.[].group") | Integer |  |  | Min: 1<br>Max: 65535 | 'access_list' and 'group' are mutual exclusive. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;original_ip</samp>](## "vlan_interfaces.[].ip_nat.destination.static.[].original_ip") | String |  |  |  | IPv4 address. The combination of `original_ip` and `original_port` must be unique. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;original_port</samp>](## "vlan_interfaces.[].ip_nat.destination.static.[].original_port") | Integer |  |  | Min: 1<br>Max: 65535 | TCP/UDP port. The combination of `original_ip` and `original_port` must be unique. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "vlan_interfaces.[].ip_nat.destination.static.[].priority") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "vlan_interfaces.[].ip_nat.destination.static.[].protocol") | String |  |  | Valid Values:<br>- <code>udp</code><br>- <code>tcp</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;translated_ip</samp>](## "vlan_interfaces.[].ip_nat.destination.static.[].translated_ip") | String | Required |  |  | IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;translated_port</samp>](## "vlan_interfaces.[].ip_nat.destination.static.[].translated_port") | Integer |  |  | Min: 1<br>Max: 65535 | requires 'original_port'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "vlan_interfaces.[].ip_nat.source") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic</samp>](## "vlan_interfaces.[].ip_nat.source.dynamic") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;access_list</samp>](## "vlan_interfaces.[].ip_nat.source.dynamic.[].access_list") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "vlan_interfaces.[].ip_nat.source.dynamic.[].comment") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nat_type</samp>](## "vlan_interfaces.[].ip_nat.source.dynamic.[].nat_type") | String | Required |  | Valid Values:<br>- <code>overload</code><br>- <code>pool</code><br>- <code>pool-address-only</code><br>- <code>pool-full-cone</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pool_name</samp>](## "vlan_interfaces.[].ip_nat.source.dynamic.[].pool_name") | String |  |  |  | required if 'nat_type' is pool, pool-address-only or pool-full-cone.<br>ignored if 'nat_type' is overload.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "vlan_interfaces.[].ip_nat.source.dynamic.[].priority") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "vlan_interfaces.[].ip_nat.source.static") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;access_list</samp>](## "vlan_interfaces.[].ip_nat.source.static.[].access_list") | String |  |  |  | 'access_list' and 'group' are mutual exclusive. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;comment</samp>](## "vlan_interfaces.[].ip_nat.source.static.[].comment") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "vlan_interfaces.[].ip_nat.source.static.[].direction") | String |  |  | Valid Values:<br>- <code>egress</code><br>- <code>ingress</code> | Egress or ingress can be the default. This depends on source/destination, EOS version, and hardware platform.<br>EOS might remove this keyword in the configuration. So, check the configuration on targeted HW/SW.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "vlan_interfaces.[].ip_nat.source.static.[].group") | Integer |  |  | Min: 1<br>Max: 65535 | 'access_list' and 'group' are mutual exclusive. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;original_ip</samp>](## "vlan_interfaces.[].ip_nat.source.static.[].original_ip") | String |  |  |  | IPv4 address. The combination of `original_ip` and `original_port` must be unique. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;original_port</samp>](## "vlan_interfaces.[].ip_nat.source.static.[].original_port") | Integer |  |  | Min: 1<br>Max: 65535 | TCP/UDP port. The combination of `original_ip` and `original_port` must be unique. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "vlan_interfaces.[].ip_nat.source.static.[].priority") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "vlan_interfaces.[].ip_nat.source.static.[].protocol") | String |  |  | Valid Values:<br>- <code>udp</code><br>- <code>tcp</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;translated_ip</samp>](## "vlan_interfaces.[].ip_nat.source.static.[].translated_ip") | String | Required |  |  | IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;translated_port</samp>](## "vlan_interfaces.[].ip_nat.source.static.[].translated_port") | Integer |  |  | Min: 1<br>Max: 65535 | requires 'original_port'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "vlan_interfaces.[].ipv6_enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "vlan_interfaces.[].ipv6_address") | String |  |  |  | IPv6_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtuals</samp>](## "vlan_interfaces.[].ipv6_address_virtuals") | List, items: String |  |  |  | The new "ipv6_address_virtuals" key support multiple virtual ipv6 addresses. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "vlan_interfaces.[].ipv6_address_virtuals.[]") | String |  |  |  | IPv6_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_link_local</samp>](## "vlan_interfaces.[].ipv6_address_link_local") | String |  |  |  | IPv6_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_virtual_router_addresses</samp>](## "vlan_interfaces.[].ipv6_virtual_router_addresses") | List, items: String |  |  |  | Improved "VARPv6" data model to support multiple VARPv6 addresses. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "vlan_interfaces.[].ipv6_virtual_router_addresses.[]") | String |  |  |  | IPv6 address or IPv6_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_ra_disabled</samp>](## "vlan_interfaces.[].ipv6_nd_ra_disabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_managed_config_flag</samp>](## "vlan_interfaces.[].ipv6_nd_managed_config_flag") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_other_config_flag</samp>](## "vlan_interfaces.[].ipv6_nd_other_config_flag") | Boolean |  |  |  | Set the "other stateful configuration" flag in IPv6 router advertisements. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_cache</samp>](## "vlan_interfaces.[].ipv6_nd_cache") | Dictionary |  |  |  | IPv6 neighbor cache options. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dynamic_capacity</samp>](## "vlan_interfaces.[].ipv6_nd_cache.dynamic_capacity") | Integer |  |  | Min: 0<br>Max: 4294967295 | Capacity of dynamic cache entries. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;expire</samp>](## "vlan_interfaces.[].ipv6_nd_cache.expire") | Integer |  |  | Min: 1<br>Max: 65535 | Cache entries expirery in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;refresh_always</samp>](## "vlan_interfaces.[].ipv6_nd_cache.refresh_always") | Boolean |  |  |  | Force refresh on cache expiry. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_nd_prefixes</samp>](## "vlan_interfaces.[].ipv6_nd_prefixes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ipv6_prefix</samp>](## "vlan_interfaces.[].ipv6_nd_prefixes.[].ipv6_prefix") | String | Required, Unique |  |  | IPv6_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;valid_lifetime</samp>](## "vlan_interfaces.[].ipv6_nd_prefixes.[].valid_lifetime") | String |  |  |  | In seconds <0-4294967295> or infinite. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preferred_lifetime</samp>](## "vlan_interfaces.[].ipv6_nd_prefixes.[].preferred_lifetime") | String |  |  |  | In seconds <0-4294967295> or infinite. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;no_autoconfig_flag</samp>](## "vlan_interfaces.[].ipv6_nd_prefixes.[].no_autoconfig_flag") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_dhcp_relay_destinations</samp>](## "vlan_interfaces.[].ipv6_dhcp_relay_destinations") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;address</samp>](## "vlan_interfaces.[].ipv6_dhcp_relay_destinations.[].address") | String | Required, Unique |  |  | DHCP server's IPv6 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "vlan_interfaces.[].ipv6_dhcp_relay_destinations.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "vlan_interfaces.[].ipv6_dhcp_relay_destinations.[].local_interface") | String |  |  |  | Local interface to communicate with DHCP server - mutually exclusive to source_address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_address</samp>](## "vlan_interfaces.[].ipv6_dhcp_relay_destinations.[].source_address") | String |  |  |  | Source IPv6 address to communicate with DHCP server - mutually exclusive to local_interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;link_address</samp>](## "vlan_interfaces.[].ipv6_dhcp_relay_destinations.[].link_address") | String |  |  |  | Override the default link address specified in the relayed DHCP packet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_dhcp_relay_all_subnets</samp>](## "vlan_interfaces.[].ipv6_dhcp_relay_all_subnets") | Boolean |  |  |  | Allow forwarding requests with additional IPv6 addresses in the gateway address "giaddr" field. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_in</samp>](## "vlan_interfaces.[].access_group_in") | String |  |  |  | IPv4 access-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_out</samp>](## "vlan_interfaces.[].access_group_out") | String |  |  |  | IPv4 access-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_in</samp>](## "vlan_interfaces.[].ipv6_access_group_in") | String |  |  |  | IPv6 access-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_out</samp>](## "vlan_interfaces.[].ipv6_access_group_out") | String |  |  |  | IPv6 access-list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;multicast</samp>](## "vlan_interfaces.[].multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "vlan_interfaces.[].multicast.ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;boundaries</samp>](## "vlan_interfaces.[].multicast.ipv4.boundaries") | List, items: Dictionary |  |  |  | Boundaries can be either 1 ACL or a list of multicast IP address_range(s)/prefix but not combination of both. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;boundary</samp>](## "vlan_interfaces.[].multicast.ipv4.boundaries.[].boundary") | String | Required, Unique |  |  | IPv4 access-list name or IPv4 multicast group prefix with mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;out</samp>](## "vlan_interfaces.[].multicast.ipv4.boundaries.[].out") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_route_export</samp>](## "vlan_interfaces.[].multicast.ipv4.source_route_export") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "vlan_interfaces.[].multicast.ipv4.source_route_export.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;administrative_distance</samp>](## "vlan_interfaces.[].multicast.ipv4.source_route_export.administrative_distance") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "vlan_interfaces.[].multicast.ipv4.static") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "vlan_interfaces.[].multicast.ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;boundaries</samp>](## "vlan_interfaces.[].multicast.ipv6.boundaries") | List, items: Dictionary |  |  |  | Boundaries can be either 1 ACL or a list of multicast IP address_range(s)/prefix but not combination of both. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;boundary</samp>](## "vlan_interfaces.[].multicast.ipv6.boundaries.[].boundary") | String | Required, Unique |  |  | IPv6 access-list name or IPv6 multicast group prefix with mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_route_export</samp>](## "vlan_interfaces.[].multicast.ipv6.source_route_export") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "vlan_interfaces.[].multicast.ipv6.source_route_export.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;administrative_distance</samp>](## "vlan_interfaces.[].multicast.ipv6.source_route_export.administrative_distance") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static</samp>](## "vlan_interfaces.[].multicast.ipv6.static") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_network_point_to_point</samp>](## "vlan_interfaces.[].ospf_network_point_to_point") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_area</samp>](## "vlan_interfaces.[].ospf_area") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_cost</samp>](## "vlan_interfaces.[].ospf_cost") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_authentication</samp>](## "vlan_interfaces.[].ospf_authentication") | String |  |  | Valid Values:<br>- <code>none</code><br>- <code>simple</code><br>- <code>message-digest</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_authentication_key</samp>](## "vlan_interfaces.[].ospf_authentication_key") | String |  |  |  | Encrypted password used for simple authentication. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ospf_message_digest_keys</samp>](## "vlan_interfaces.[].ospf_message_digest_keys") | List, items: Dictionary |  |  |  | Keys used for message-digest authentication. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "vlan_interfaces.[].ospf_message_digest_keys.[].id") | Integer | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "vlan_interfaces.[].ospf_message_digest_keys.[].hash_algorithm") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>sha1</code><br>- <code>sha256</code><br>- <code>sha384</code><br>- <code>sha512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "vlan_interfaces.[].ospf_message_digest_keys.[].key") | String |  |  |  | Encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pim</samp>](## "vlan_interfaces.[].pim") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "vlan_interfaces.[].pim.ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;border_router</samp>](## "vlan_interfaces.[].pim.ipv4.border_router") | Boolean |  |  |  | Configure PIM border router. EOS default is false. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dr_priority</samp>](## "vlan_interfaces.[].pim.ipv4.dr_priority") | Integer |  |  | Min: 0<br>Max: 429467295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sparse_mode</samp>](## "vlan_interfaces.[].pim.ipv4.sparse_mode") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "vlan_interfaces.[].pim.ipv4.local_interface") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "vlan_interfaces.[].pim.ipv4.bfd") | Boolean |  |  |  | Set the default for whether Bidirectional Forwarding Detection is enabled for PIM. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bidirectional</samp>](## "vlan_interfaces.[].pim.ipv4.bidirectional") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hello</samp>](## "vlan_interfaces.[].pim.ipv4.hello") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;count</samp>](## "vlan_interfaces.[].pim.ipv4.hello.count") | String |  |  |  | Number of missed hellos after which the neighbor expires. Range <1.5-65535>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "vlan_interfaces.[].pim.ipv4.hello.interval") | Integer |  |  | Min: 1<br>Max: 65535 | PIM hello interval in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_enable</samp>](## "vlan_interfaces.[].isis_enable") | String |  |  |  | ISIS instance name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_bfd</samp>](## "vlan_interfaces.[].isis_bfd") | Boolean |  |  |  | Enable BFD for ISIS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_passive</samp>](## "vlan_interfaces.[].isis_passive") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_metric</samp>](## "vlan_interfaces.[].isis_metric") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_network_point_to_point</samp>](## "vlan_interfaces.[].isis_network_point_to_point") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;isis_authentication</samp>](## "vlan_interfaces.[].isis_authentication") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;both</samp>](## "vlan_interfaces.[].isis_authentication.both") | Dictionary |  |  |  | Authentication settings for level-1 and level-2. 'both' takes precedence over 'level_1' and 'level_2' settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "vlan_interfaces.[].isis_authentication.both.key_type") | String |  |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Configure authentication key type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "vlan_interfaces.[].isis_authentication.both.key") | String |  |  |  | Password string. `key_type` is required for this setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_ids</samp>](## "vlan_interfaces.[].isis_authentication.both.key_ids") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "vlan_interfaces.[].isis_authentication.both.key_ids.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 65535 | Configure authentication key-id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "vlan_interfaces.[].isis_authentication.both.key_ids.[].algorithm") | String | Required |  | Valid Values:<br>- <code>sha-1</code><br>- <code>sha-224</code><br>- <code>sha-256</code><br>- <code>sha-384</code><br>- <code>sha-512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "vlan_interfaces.[].isis_authentication.both.key_ids.[].key_type") | String | Required |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Configure authentication key type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "vlan_interfaces.[].isis_authentication.both.key_ids.[].key") | String | Required |  |  | Password string. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rfc_5310</samp>](## "vlan_interfaces.[].isis_authentication.both.key_ids.[].rfc_5310") | Boolean |  |  |  | SHA digest computation according to rfc5310. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "vlan_interfaces.[].isis_authentication.both.mode") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>sha</code><br>- <code>text</code><br>- <code>shared-secret</code> | Authentication mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sha</samp>](## "vlan_interfaces.[].isis_authentication.both.sha") | Dictionary |  |  |  | Required settings for authentication mode 'sha'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_id</samp>](## "vlan_interfaces.[].isis_authentication.both.sha.key_id") | Integer | Required |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shared_secret</samp>](## "vlan_interfaces.[].isis_authentication.both.shared_secret") | Dictionary |  |  |  | Required settings for authentication mode 'shared_secret'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "vlan_interfaces.[].isis_authentication.both.shared_secret.profile") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "vlan_interfaces.[].isis_authentication.both.shared_secret.algorithm") | String | Required |  | Valid Values:<br>- <code>md5</code><br>- <code>sha-1</code><br>- <code>sha-224</code><br>- <code>sha-256</code><br>- <code>sha-384</code><br>- <code>sha-512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rx_disabled</samp>](## "vlan_interfaces.[].isis_authentication.both.rx_disabled") | Boolean |  |  |  | Disable authentication check on the receive side. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level_1</samp>](## "vlan_interfaces.[].isis_authentication.level_1") | Dictionary |  |  |  | Authentication settings for level-1. 'both' takes precedence over 'level_1' and 'level_2' settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "vlan_interfaces.[].isis_authentication.level_1.key_type") | String |  |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Configure authentication key type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "vlan_interfaces.[].isis_authentication.level_1.key") | String |  |  |  | Password string. `key_type` is required for this setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_ids</samp>](## "vlan_interfaces.[].isis_authentication.level_1.key_ids") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "vlan_interfaces.[].isis_authentication.level_1.key_ids.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 65535 | Configure authentication key-id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "vlan_interfaces.[].isis_authentication.level_1.key_ids.[].algorithm") | String | Required |  | Valid Values:<br>- <code>sha-1</code><br>- <code>sha-224</code><br>- <code>sha-256</code><br>- <code>sha-384</code><br>- <code>sha-512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "vlan_interfaces.[].isis_authentication.level_1.key_ids.[].key_type") | String | Required |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Configure authentication key type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "vlan_interfaces.[].isis_authentication.level_1.key_ids.[].key") | String | Required |  |  | Password string. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rfc_5310</samp>](## "vlan_interfaces.[].isis_authentication.level_1.key_ids.[].rfc_5310") | Boolean |  |  |  | SHA digest computation according to rfc5310. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "vlan_interfaces.[].isis_authentication.level_1.mode") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>sha</code><br>- <code>text</code><br>- <code>shared-secret</code> | Authentication mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sha</samp>](## "vlan_interfaces.[].isis_authentication.level_1.sha") | Dictionary |  |  |  | Required settings for authentication mode 'sha'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_id</samp>](## "vlan_interfaces.[].isis_authentication.level_1.sha.key_id") | Integer | Required |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shared_secret</samp>](## "vlan_interfaces.[].isis_authentication.level_1.shared_secret") | Dictionary |  |  |  | Required settings for authentication mode 'shared_secret'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "vlan_interfaces.[].isis_authentication.level_1.shared_secret.profile") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "vlan_interfaces.[].isis_authentication.level_1.shared_secret.algorithm") | String | Required |  | Valid Values:<br>- <code>md5</code><br>- <code>sha-1</code><br>- <code>sha-224</code><br>- <code>sha-256</code><br>- <code>sha-384</code><br>- <code>sha-512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rx_disabled</samp>](## "vlan_interfaces.[].isis_authentication.level_1.rx_disabled") | Boolean |  |  |  | Disable authentication check on the receive side. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;level_2</samp>](## "vlan_interfaces.[].isis_authentication.level_2") | Dictionary |  |  |  | Authentication settings for level-2. 'both' takes precedence over 'level_1' and 'level_2' settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "vlan_interfaces.[].isis_authentication.level_2.key_type") | String |  |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Configure authentication key type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "vlan_interfaces.[].isis_authentication.level_2.key") | String |  |  |  | Password string. `key_type` is required for this setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_ids</samp>](## "vlan_interfaces.[].isis_authentication.level_2.key_ids") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "vlan_interfaces.[].isis_authentication.level_2.key_ids.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 65535 | Configure authentication key-id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "vlan_interfaces.[].isis_authentication.level_2.key_ids.[].algorithm") | String | Required |  | Valid Values:<br>- <code>sha-1</code><br>- <code>sha-224</code><br>- <code>sha-256</code><br>- <code>sha-384</code><br>- <code>sha-512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "vlan_interfaces.[].isis_authentication.level_2.key_ids.[].key_type") | String | Required |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> | Configure authentication key type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "vlan_interfaces.[].isis_authentication.level_2.key_ids.[].key") | String | Required |  |  | Password string. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rfc_5310</samp>](## "vlan_interfaces.[].isis_authentication.level_2.key_ids.[].rfc_5310") | Boolean |  |  |  | SHA digest computation according to rfc5310. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "vlan_interfaces.[].isis_authentication.level_2.mode") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>sha</code><br>- <code>text</code><br>- <code>shared-secret</code> | Authentication mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sha</samp>](## "vlan_interfaces.[].isis_authentication.level_2.sha") | Dictionary |  |  |  | Required settings for authentication mode 'sha'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_id</samp>](## "vlan_interfaces.[].isis_authentication.level_2.sha.key_id") | Integer | Required |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shared_secret</samp>](## "vlan_interfaces.[].isis_authentication.level_2.shared_secret") | Dictionary |  |  |  | Required settings for authentication mode 'shared_secret'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "vlan_interfaces.[].isis_authentication.level_2.shared_secret.profile") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "vlan_interfaces.[].isis_authentication.level_2.shared_secret.algorithm") | String | Required |  | Valid Values:<br>- <code>md5</code><br>- <code>sha-1</code><br>- <code>sha-224</code><br>- <code>sha-256</code><br>- <code>sha-384</code><br>- <code>sha-512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rx_disabled</samp>](## "vlan_interfaces.[].isis_authentication.level_2.rx_disabled") | Boolean |  |  |  | Disable authentication check on the receive side. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "vlan_interfaces.[].mtu") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;no_autostate</samp>](## "vlan_interfaces.[].no_autostate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrrp_ids</samp>](## "vlan_interfaces.[].vrrp_ids") | List, items: Dictionary |  |  |  | Improved "vrrp" data model to support multiple VRRP IDs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "vlan_interfaces.[].vrrp_ids.[].id") | Integer | Required, Unique |  |  | VRID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority_level</samp>](## "vlan_interfaces.[].vrrp_ids.[].priority_level") | Integer |  |  | Min: 1<br>Max: 254 | Instance priority. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;advertisement</samp>](## "vlan_interfaces.[].vrrp_ids.[].advertisement") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "vlan_interfaces.[].vrrp_ids.[].advertisement.interval") | Integer |  |  | Min: 1<br>Max: 255 | Interval in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preempt</samp>](## "vlan_interfaces.[].vrrp_ids.[].preempt") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "vlan_interfaces.[].vrrp_ids.[].preempt.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "vlan_interfaces.[].vrrp_ids.[].preempt.delay") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minimum</samp>](## "vlan_interfaces.[].vrrp_ids.[].preempt.delay.minimum") | Integer |  |  | Min: 0<br>Max: 3600 | Minimum preempt delay in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reload</samp>](## "vlan_interfaces.[].vrrp_ids.[].preempt.delay.reload") | Integer |  |  | Min: 0<br>Max: 3600 | Reload preempt delay in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;timers</samp>](## "vlan_interfaces.[].vrrp_ids.[].timers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;delay</samp>](## "vlan_interfaces.[].vrrp_ids.[].timers.delay") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reload</samp>](## "vlan_interfaces.[].vrrp_ids.[].timers.delay.reload") | Integer |  |  | Min: 0<br>Max: 3600 | Delay after reload in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tracked_object</samp>](## "vlan_interfaces.[].vrrp_ids.[].tracked_object") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "vlan_interfaces.[].vrrp_ids.[].tracked_object.[].name") | String | Required, Unique |  |  | Tracked object name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;decrement</samp>](## "vlan_interfaces.[].vrrp_ids.[].tracked_object.[].decrement") | Integer |  |  | Min: 1<br>Max: 254 | Decrement VRRP priority by 1-254. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "vlan_interfaces.[].vrrp_ids.[].tracked_object.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "vlan_interfaces.[].vrrp_ids.[].ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address</samp>](## "vlan_interfaces.[].vrrp_ids.[].ipv4.address") | String | Required |  |  | Virtual IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "vlan_interfaces.[].vrrp_ids.[].ipv4.version") | Integer |  |  | Valid Values:<br>- <code>2</code><br>- <code>3</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "vlan_interfaces.[].vrrp_ids.[].ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address</samp>](## "vlan_interfaces.[].vrrp_ids.[].ipv6.address") | String | Required |  |  | Virtual IPv6 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_attached_host_route_export</samp>](## "vlan_interfaces.[].ip_attached_host_route_export") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "vlan_interfaces.[].ip_attached_host_route_export.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "vlan_interfaces.[].ip_attached_host_route_export.distance") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_attached_host_route_export</samp>](## "vlan_interfaces.[].ipv6_attached_host_route_export") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "vlan_interfaces.[].ipv6_attached_host_route_export.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "vlan_interfaces.[].ipv6_attached_host_route_export.distance") | Integer |  |  | Min: 1<br>Max: 255 | Administrative distance for generated routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_length</samp>](## "vlan_interfaces.[].ipv6_attached_host_route_export.prefix_length") | Integer |  |  | Min: 0<br>Max: 128 | Prefix length for generated routes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "vlan_interfaces.[].bfd") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;echo</samp>](## "vlan_interfaces.[].bfd.echo") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "vlan_interfaces.[].bfd.interval") | Integer |  |  |  | Rate in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp>](## "vlan_interfaces.[].bfd.min_rx") | Integer |  |  |  | Minimum RX hold time in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "vlan_interfaces.[].bfd.multiplier") | Integer |  |  | Min: 3<br>Max: 50 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;service_policy</samp>](## "vlan_interfaces.[].service_policy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pbr</samp>](## "vlan_interfaces.[].service_policy.pbr") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;input</samp>](## "vlan_interfaces.[].service_policy.pbr.input") | String |  |  |  | Name of policy-map used for policy based routing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pvlan_mapping</samp>](## "vlan_interfaces.[].pvlan_mapping") | String |  |  |  | List of VLANs as string. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tenant</samp>](## "vlan_interfaces.[].tenant") | String |  |  |  | Key only used for documentation or validation purposes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "vlan_interfaces.[].tags") | List, items: String |  |  |  | Key only used for documentation or validation purposes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "vlan_interfaces.[].tags.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "vlan_interfaces.[].type") | String |  |  |  | Key only used for documentation or validation purposes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "vlan_interfaces.[].eos_cli") | String |  |  |  | Multiline EOS CLI rendered directly on the VLAN interface in the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtual</samp>](## "vlan_interfaces.[].ipv6_address_virtual") <span style="color:red">removed</span> | String |  |  |  | IPv6_address/Mask.<br><span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>ipv6_address_virtuals</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_virtual_router_address</samp>](## "vlan_interfaces.[].ipv6_virtual_router_address") <span style="color:red">removed</span> | String |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>ipv6_virtual_router_addresses</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrrp</samp>](## "vlan_interfaces.[].vrrp") <span style="color:red">removed</span> | Dictionary |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>vrrp_ids</samp> instead.</span> |

=== "YAML"

    ```yaml
    vlan_interfaces:

        # VLAN interface name like "Vlan123".
      - name: <str; required; unique>
        description: <str>
        logging:
          event:
            link_status: <bool>
        shutdown: <bool>

        # VRF name.
        vrf: <str>

        # In seconds.
        arp_aging_timeout: <int; 1-65535>
        arp_cache_dynamic_capacity: <int; 0-4294967295>
        arp_gratuitous_accept: <bool>
        arp_monitor_mac_address: <bool>
        ip_proxy_arp: <bool>
        ip_directed_broadcast: <bool>

        # IPv4_address/Mask.
        ip_address: <str>
        ip_address_secondaries:

            # IPv4_address/Mask.
          - <str>
        ip_virtual_router_addresses:

            # IPv4 address or IPv4_address/Mask.
          - <str>

        # IPv4_address/Mask.
        ip_address_virtual: <str>
        ip_address_virtual_secondaries:

            # IPv4_address/Mask.
          - <str>
        ip_verify_unicast_source_reachable_via: <str; "any" | "rx">
        ip_igmp: <bool>
        ip_igmp_version: <int; 1-3>
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

        # List of DHCP servers.
        ip_helpers:

            # IP address or hostname of DHCP server.
          - ip_helper: <str; required; unique>

            # Interface used as source for forwarded DHCP packets.
            source_interface: <str>

            # VRF where DHCP server can be reached.
            vrf: <str>

        # Allow forwarding requests with secondary IP addresses in the gateway address "giaddr" field.
        ip_dhcp_relay_all_subnets: <bool>
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

        # IPv6_address/Mask.
        ipv6_address: <str>

        # The new "ipv6_address_virtuals" key support multiple virtual ipv6 addresses.
        ipv6_address_virtuals:

            # IPv6_address/Mask.
          - <str>

        # IPv6_address/Mask.
        ipv6_address_link_local: <str>

        # Improved "VARPv6" data model to support multiple VARPv6 addresses.
        ipv6_virtual_router_addresses:

            # IPv6 address or IPv6_address/Mask.
          - <str>
        ipv6_nd_ra_disabled: <bool>
        ipv6_nd_managed_config_flag: <bool>

        # Set the "other stateful configuration" flag in IPv6 router advertisements.
        ipv6_nd_other_config_flag: <bool>

        # IPv6 neighbor cache options.
        ipv6_nd_cache:

          # Capacity of dynamic cache entries.
          dynamic_capacity: <int; 0-4294967295>

          # Cache entries expirery in seconds.
          expire: <int; 1-65535>

          # Force refresh on cache expiry.
          refresh_always: <bool>
        ipv6_nd_prefixes:

            # IPv6_address/Mask.
          - ipv6_prefix: <str; required; unique>

            # In seconds <0-4294967295> or infinite.
            valid_lifetime: <str>

            # In seconds <0-4294967295> or infinite.
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

        # Allow forwarding requests with additional IPv6 addresses in the gateway address "giaddr" field.
        ipv6_dhcp_relay_all_subnets: <bool>

        # IPv4 access-list name.
        access_group_in: <str>

        # IPv4 access-list name.
        access_group_out: <str>

        # IPv6 access-list name.
        ipv6_access_group_in: <str>

        # IPv6 access-list name.
        ipv6_access_group_out: <str>
        multicast:
          ipv4:

            # Boundaries can be either 1 ACL or a list of multicast IP address_range(s)/prefix but not combination of both.
            boundaries:

                # IPv4 access-list name or IPv4 multicast group prefix with mask.
              - boundary: <str; required; unique>
                out: <bool>
            source_route_export:
              enabled: <bool; required>
              administrative_distance: <int; 1-255>
            static: <bool>
          ipv6:

            # Boundaries can be either 1 ACL or a list of multicast IP address_range(s)/prefix but not combination of both.
            boundaries:

                # IPv6 access-list name or IPv6 multicast group prefix with mask.
              - boundary: <str; required; unique>
            source_route_export:
              enabled: <bool; required>
              administrative_distance: <int; 1-255>
            static: <bool>
        ospf_network_point_to_point: <bool>
        ospf_area: <str>
        ospf_cost: <int>
        ospf_authentication: <str; "none" | "simple" | "message-digest">

        # Encrypted password used for simple authentication.
        ospf_authentication_key: <str>

        # Keys used for message-digest authentication.
        ospf_message_digest_keys:
          - id: <int; required; unique>
            hash_algorithm: <str; "md5" | "sha1" | "sha256" | "sha384" | "sha512">

            # Encrypted password.
            key: <str>
        pim:
          ipv4:

            # Configure PIM border router. EOS default is false.
            border_router: <bool>
            dr_priority: <int; 0-429467295>
            sparse_mode: <bool>
            local_interface: <str>

            # Set the default for whether Bidirectional Forwarding Detection is enabled for PIM.
            bfd: <bool>
            bidirectional: <bool>
            hello:

              # Number of missed hellos after which the neighbor expires. Range <1.5-65535>.
              count: <str>

              # PIM hello interval in seconds.
              interval: <int; 1-65535>

        # ISIS instance name.
        isis_enable: <str>

        # Enable BFD for ISIS.
        isis_bfd: <bool>
        isis_passive: <bool>
        isis_metric: <int>
        isis_network_point_to_point: <bool>
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
        mtu: <int>
        no_autostate: <bool>

        # Improved "vrrp" data model to support multiple VRRP IDs.
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
        ip_attached_host_route_export:
          enabled: <bool; required>
          distance: <int; 1-255>
        ipv6_attached_host_route_export:
          enabled: <bool; required>

          # Administrative distance for generated routes.
          distance: <int; 1-255>

          # Prefix length for generated routes.
          prefix_length: <int; 0-128>
        bfd:
          echo: <bool>

          # Rate in milliseconds.
          interval: <int>

          # Minimum RX hold time in milliseconds.
          min_rx: <int>
          multiplier: <int; 3-50>
        service_policy:
          pbr:

            # Name of policy-map used for policy based routing.
            input: <str>

        # List of VLANs as string.
        pvlan_mapping: <str>

        # Key only used for documentation or validation purposes.
        tenant: <str>

        # Key only used for documentation or validation purposes.
        tags:
          - <str>

        # Key only used for documentation or validation purposes.
        type: <str>

        # Multiline EOS CLI rendered directly on the VLAN interface in the final EOS configuration.
        eos_cli: <str>
    ```
