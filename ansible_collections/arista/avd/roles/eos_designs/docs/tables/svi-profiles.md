<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>svi_profiles</samp>](## "svi_profiles") | List, items: Dictionary |  |  |  | Profiles to share common settings for SVIs under `<network_services_key>.[].vrfs.svis`.<br>Keys are the same used under SVIs. Keys defined under SVIs take precedence.<br>Note: structured configuration is not merged recursively and will be taken directly from the most specific level in the following order:<br>1. svi.nodes[inventory_hostname].structured_config<br>2. svi_profile.nodes[inventory_hostname].structured_config<br>3. svi_parent_profile.nodes[inventory_hostname].structured_config<br>4. svi.structured_config<br>5. svi_profile.structured_config<br>6. svi_parent_profile.structured_config<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;profile</samp>](## "svi_profiles.[].profile") | String | Required, Unique |  |  | Profile name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;parent_profile</samp>](## "svi_profiles.[].parent_profile") | String |  |  |  | Parent SVI profile name to apply.<br>svi_profiles can refer to another svi_profile to inherit settings in up to two levels (svi -> svi_profile -> svi_parent_profile).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "svi_profiles.[].nodes") | List, items: Dictionary |  |  |  | Define node specific configuration, such as unique IP addresses.<br>Any keys set here will be merged onto the SVI config, except `structured_config` keys which will replace the `structured_config` set on SVI level.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;node</samp>](## "svi_profiles.[].nodes.[].node") | String | Required, Unique |  |  | Node inventory hostname. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "svi_profiles.[].nodes.[].name") | String |  |  |  | VLAN name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].nodes.[].enabled") | Boolean |  |  |  | Enable or disable interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "svi_profiles.[].nodes.[].description") | String |  |  |  | SVI description. By default set to VLAN name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "svi_profiles.[].nodes.[].ip_address") | String |  |  |  | IPv4_address/Mask. Usually set under "nodes" to have unique IPv4 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "svi_profiles.[].nodes.[].ipv6_address") | String |  |  |  | IPv6_address/Mask. Usually set under "nodes" to have unique IPv6 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "svi_profiles.[].nodes.[].ipv6_enable") | Boolean |  |  |  | Explicitly enable/disable link-local IPv6 addressing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual</samp>](## "svi_profiles.[].nodes.[].ip_address_virtual") | String |  |  |  | IPv4_address/Mask.<br>IPv4 VXLAN Anycast IP address.<br>Conserves IP addresses in VXLAN deployments as it doesn't require unique IP addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtuals</samp>](## "svi_profiles.[].nodes.[].ipv6_address_virtuals") | List, items: String |  |  |  | IPv6 VXLAN Anycast IP addresses.<br>Conserves IPv6 addresses in VXLAN deployments as it doesn't require unique IPv6 addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "svi_profiles.[].nodes.[].ipv6_address_virtuals.[]") | String |  |  |  | IPv6_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual_secondaries</samp>](## "svi_profiles.[].nodes.[].ip_address_virtual_secondaries") | List, items: String |  |  |  | Secondary IPv4 VXLAN Anycast IP addresses. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "svi_profiles.[].nodes.[].ip_address_virtual_secondaries.[]") | String |  |  |  | IPv4_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_virtual_router_addresses</samp>](## "svi_profiles.[].nodes.[].ip_virtual_router_addresses") | List, items: String |  |  |  | IPv4 VARP addresses.<br>Requires an IP address to be configured on the SVI.<br>If ip_address_virtual is also set, ip_virtual_router_addresses will take precedence<br>_if_ there is an ip_address configured for the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "svi_profiles.[].nodes.[].ip_virtual_router_addresses.[]") | String |  |  |  | IPv4_address/Mask or IPv4_address.<br>IPv4_address/Mask will also configure a static route to the SVI per best practice.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_virtual_router_addresses</samp>](## "svi_profiles.[].nodes.[].ipv6_virtual_router_addresses") | List, items: String |  |  |  | IPv6 VARP addresses.<br>Requires an IPv6 address to be configured on the SVI.<br>If ipv6_address_virtuals is also set, ipv6_virtual_router_addresses will take precedence<br>_if_ there is an ipv6_address configured for the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "svi_profiles.[].nodes.[].ipv6_virtual_router_addresses.[]") | String |  |  |  | IPv6_address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_in</samp>](## "svi_profiles.[].nodes.[].ipv4_acl_in") | String |  |  |  | Name of the IPv4 access-list to be assigned in the ingress direction.<br>The access-list must be defined under `ipv4_acls` and supports substitution of the field "interface_ip". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_out</samp>](## "svi_profiles.[].nodes.[].ipv4_acl_out") | String |  |  |  | Name of the IPv4 Access-list to be assigned in the egress direction.<br>The access-list must be defined under `ipv4_acls` and supports substitution of the field "interface_ip". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "svi_profiles.[].nodes.[].ip_helpers") | List, items: Dictionary |  |  |  | IP helper for DHCP relay. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_helper</samp>](## "svi_profiles.[].nodes.[].ip_helpers.[].ip_helper") | String | Required, Unique |  |  | IPv4 DHCP server IP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "svi_profiles.[].nodes.[].ip_helpers.[].source_interface") | String |  |  |  | Interface name to originate DHCP relay packets to DHCP server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_vrf</samp>](## "svi_profiles.[].nodes.[].ip_helpers.[].source_vrf") | String |  |  |  | VRF to originate DHCP relay packets to DHCP server. If not set, EOS uses the VRF on the SVI. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni_override</samp>](## "svi_profiles.[].nodes.[].vni_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the VNI will be derived from "mac_vrf_vni_base".<br>The vni_override allows us to override this value and statically define it (optional).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rt_override</samp>](## "svi_profiles.[].nodes.[].rt_override") | String |  |  |  | By default the MAC VRF RT will be derived from mac_vrf_id_base + vlan_id.<br>The rt_override allows us to override this value and statically define it.<br>rt_override will default to vni_override if set.<br><br>rt_override supports two formats:<br>  - A single number which will be used in the RT fields instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rt_type' for details).<br>  - A full RT string with colon separator which will override the full RT.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd_override</samp>](## "svi_profiles.[].nodes.[].rd_override") | String |  |  |  | By default the MAC VRF RD will be derived from mac_vrf_id_base + vlan_id.<br>The rt_override allows us to override this value and statically define it.<br>rd_override will default to rt_override or vni_override if set.<br><br>rd_override supports two formats:<br>  - A single number which will be used in the RD assigned number field instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rd_type' for details).<br>  - A full RD string with colon separator which will override the full RD.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "svi_profiles.[].nodes.[].trunk_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "svi_profiles.[].nodes.[].trunk_groups.[]") | String |  |  |  | Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group.<br>Requires "enable_trunk_groups: true".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "svi_profiles.[].nodes.[].vxlan") | Boolean |  | `True` |  | Extend this SVI over VXLAN. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_priority</samp>](## "svi_profiles.[].nodes.[].spanning_tree_priority") | Integer |  |  |  | Setting spanning-tree priority per VLAN is only supported with `spanning_tree_mode: rapid-pvst` under node type settings.<br>The default priority for rapid-PVST is set under the node type settings with `spanning_tree_priority` (default=32768). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "svi_profiles.[].nodes.[].mtu") | Integer |  |  |  | Interface MTU. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "svi_profiles.[].nodes.[].bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "svi_profiles.[].nodes.[].bgp.structured_config") | Dictionary |  |  |  | Structured configuration and EOS CLI commands rendered on router_bgp.vlans.[id=<vlan>].<br>This configuration will not be applied to vlan aware bundles.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "svi_profiles.[].nodes.[].bgp.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the Router BGP, VLAN definition in the final EOS configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "svi_profiles.[].nodes.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "svi_profiles.[].nodes.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtual</samp>](## "svi_profiles.[].nodes.[].ipv6_address_virtual") <span style="color:red">removed</span> | String |  |  |  | IPv6_address/Mask.<br>ipv6 address virtuals to configure VXLAN Anycast IP address (Optional).<br><span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>ipv6_address_virtuals</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multi_domain</samp>](## "svi_profiles.[].nodes.[].evpn_l2_multi_domain") | Boolean |  |  |  | Explicitly extend SVI to remote EVPN domains.<br>Overrides `<network_services_key>[].evpn_l2_multi_domain` and `<network_services_key>[].vrfs[].evpn_l2_multi_domain`.<br>Not supported in conjunction with EVPN vlan aware bundles. i.e. `evpn_vlan_aware_bundles: true` or `<network_services_key>[].evpn_vlan_bundle` or `<network_services_key>[].vrfs[].svis[].evpn_vlan_bundle`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "svi_profiles.[].name") | String |  |  |  | VLAN name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "svi_profiles.[].enabled") | Boolean |  |  |  | Enable or disable interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "svi_profiles.[].description") | String |  |  |  | SVI description. By default set to VLAN name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "svi_profiles.[].ip_address") | String |  |  |  | IPv4_address/Mask. Usually set under "nodes" to have unique IPv4 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "svi_profiles.[].ipv6_address") | String |  |  |  | IPv6_address/Mask. Usually set under "nodes" to have unique IPv6 addresses per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "svi_profiles.[].ipv6_enable") | Boolean |  |  |  | Explicitly enable/disable link-local IPv6 addressing. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual</samp>](## "svi_profiles.[].ip_address_virtual") | String |  |  |  | IPv4_address/Mask.<br>IPv4 VXLAN Anycast IP address.<br>Conserves IP addresses in VXLAN deployments as it doesn't require unique IP addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtuals</samp>](## "svi_profiles.[].ipv6_address_virtuals") | List, items: String |  |  |  | IPv6 VXLAN Anycast IP addresses.<br>Conserves IPv6 addresses in VXLAN deployments as it doesn't require unique IPv6 addresses on each node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "svi_profiles.[].ipv6_address_virtuals.[]") | String |  |  |  | IPv6_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address_virtual_secondaries</samp>](## "svi_profiles.[].ip_address_virtual_secondaries") | List, items: String |  |  |  | Secondary IPv4 VXLAN Anycast IP addresses. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "svi_profiles.[].ip_address_virtual_secondaries.[]") | String |  |  |  | IPv4_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_virtual_router_addresses</samp>](## "svi_profiles.[].ip_virtual_router_addresses") | List, items: String |  |  |  | IPv4 VARP addresses.<br>Requires an IP address to be configured on the SVI.<br>If ip_address_virtual is also set, ip_virtual_router_addresses will take precedence<br>_if_ there is an ip_address configured for the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "svi_profiles.[].ip_virtual_router_addresses.[]") | String |  |  |  | IPv4_address/Mask or IPv4_address.<br>IPv4_address/Mask will also configure a static route to the SVI per best practice.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_virtual_router_addresses</samp>](## "svi_profiles.[].ipv6_virtual_router_addresses") | List, items: String |  |  |  | IPv6 VARP addresses.<br>Requires an IPv6 address to be configured on the SVI.<br>If ipv6_address_virtuals is also set, ipv6_virtual_router_addresses will take precedence<br>_if_ there is an ipv6_address configured for the node.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "svi_profiles.[].ipv6_virtual_router_addresses.[]") | String |  |  |  | IPv6_address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_in</samp>](## "svi_profiles.[].ipv4_acl_in") | String |  |  |  | Name of the IPv4 access-list to be assigned in the ingress direction.<br>The access-list must be defined under `ipv4_acls` and supports substitution of the field "interface_ip". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_out</samp>](## "svi_profiles.[].ipv4_acl_out") | String |  |  |  | Name of the IPv4 Access-list to be assigned in the egress direction.<br>The access-list must be defined under `ipv4_acls` and supports substitution of the field "interface_ip". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "svi_profiles.[].ip_helpers") | List, items: Dictionary |  |  |  | IP helper for DHCP relay. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_helper</samp>](## "svi_profiles.[].ip_helpers.[].ip_helper") | String | Required, Unique |  |  | IPv4 DHCP server IP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "svi_profiles.[].ip_helpers.[].source_interface") | String |  |  |  | Interface name to originate DHCP relay packets to DHCP server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_vrf</samp>](## "svi_profiles.[].ip_helpers.[].source_vrf") | String |  |  |  | VRF to originate DHCP relay packets to DHCP server. If not set, EOS uses the VRF on the SVI. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vni_override</samp>](## "svi_profiles.[].vni_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the VNI will be derived from "mac_vrf_vni_base".<br>The vni_override allows us to override this value and statically define it (optional).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rt_override</samp>](## "svi_profiles.[].rt_override") | String |  |  |  | By default the MAC VRF RT will be derived from mac_vrf_id_base + vlan_id.<br>The rt_override allows us to override this value and statically define it.<br>rt_override will default to vni_override if set.<br><br>rt_override supports two formats:<br>  - A single number which will be used in the RT fields instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rt_type' for details).<br>  - A full RT string with colon separator which will override the full RT.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rd_override</samp>](## "svi_profiles.[].rd_override") | String |  |  |  | By default the MAC VRF RD will be derived from mac_vrf_id_base + vlan_id.<br>The rt_override allows us to override this value and statically define it.<br>rd_override will default to rt_override or vni_override if set.<br><br>rd_override supports two formats:<br>  - A single number which will be used in the RD assigned number field instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rd_type' for details).<br>  - A full RD string with colon separator which will override the full RD.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "svi_profiles.[].trunk_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "svi_profiles.[].trunk_groups.[]") | String |  |  |  | Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group.<br>Requires "enable_trunk_groups: true".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "svi_profiles.[].vxlan") | Boolean |  | `True` |  | Extend this SVI over VXLAN. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_priority</samp>](## "svi_profiles.[].spanning_tree_priority") | Integer |  |  |  | Setting spanning-tree priority per VLAN is only supported with `spanning_tree_mode: rapid-pvst` under node type settings.<br>The default priority for rapid-PVST is set under the node type settings with `spanning_tree_priority` (default=32768). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "svi_profiles.[].mtu") | Integer |  |  |  | Interface MTU. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "svi_profiles.[].bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "svi_profiles.[].bgp.structured_config") | Dictionary |  |  |  | Structured configuration and EOS CLI commands rendered on router_bgp.vlans.[id=<vlan>].<br>This configuration will not be applied to vlan aware bundles.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "svi_profiles.[].bgp.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the Router BGP, VLAN definition in the final EOS configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "svi_profiles.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the VLAN interface in the final EOS configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "svi_profiles.[].structured_config") | Dictionary |  |  |  | Custom structured config added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address_virtual</samp>](## "svi_profiles.[].ipv6_address_virtual") <span style="color:red">removed</span> | String |  |  |  | IPv6_address/Mask.<br>ipv6 address virtuals to configure VXLAN Anycast IP address (Optional).<br><span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>ipv6_address_virtuals</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multi_domain</samp>](## "svi_profiles.[].evpn_l2_multi_domain") | Boolean |  |  |  | Explicitly extend SVI to remote EVPN domains.<br>Overrides `<network_services_key>[].evpn_l2_multi_domain` and `<network_services_key>[].vrfs[].evpn_l2_multi_domain`.<br>Not supported in conjunction with EVPN vlan aware bundles. i.e. `evpn_vlan_aware_bundles: true` or `<network_services_key>[].evpn_vlan_bundle` or `<network_services_key>[].vrfs[].svis[].evpn_vlan_bundle`.<br> |

=== "YAML"

    ```yaml
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

        # Parent SVI profile name to apply.
        # svi_profiles can refer to another svi_profile to inherit settings in up to two levels (svi -> svi_profile -> svi_parent_profile).
        parent_profile: <str>

        # Define node specific configuration, such as unique IP addresses.
        # Any keys set here will be merged onto the SVI config, except `structured_config` keys which will replace the `structured_config` set on SVI level.
        nodes:

            # Node inventory hostname.
          - node: <str; required; unique>

            # VLAN name.
            name: <str>

            # Enable or disable interface.
            enabled: <bool>

            # SVI description. By default set to VLAN name.
            description: <str>

            # IPv4_address/Mask. Usually set under "nodes" to have unique IPv4 addresses per node.
            ip_address: <str>

            # IPv6_address/Mask. Usually set under "nodes" to have unique IPv6 addresses per node.
            ipv6_address: <str>

            # Explicitly enable/disable link-local IPv6 addressing.
            ipv6_enable: <bool>

            # IPv4_address/Mask.
            # IPv4 VXLAN Anycast IP address.
            # Conserves IP addresses in VXLAN deployments as it doesn't require unique IP addresses on each node.
            ip_address_virtual: <str>

            # IPv6 VXLAN Anycast IP addresses.
            # Conserves IPv6 addresses in VXLAN deployments as it doesn't require unique IPv6 addresses on each node.
            ipv6_address_virtuals:

                # IPv6_address/Mask.
              - <str>

            # Secondary IPv4 VXLAN Anycast IP addresses.
            ip_address_virtual_secondaries:

                # IPv4_address/Mask.
              - <str>

            # IPv4 VARP addresses.
            # Requires an IP address to be configured on the SVI.
            # If ip_address_virtual is also set, ip_virtual_router_addresses will take precedence
            # _if_ there is an ip_address configured for the node.
            ip_virtual_router_addresses:

                # IPv4_address/Mask or IPv4_address.
                # IPv4_address/Mask will also configure a static route to the SVI per best practice.
              - <str>

            # IPv6 VARP addresses.
            # Requires an IPv6 address to be configured on the SVI.
            # If ipv6_address_virtuals is also set, ipv6_virtual_router_addresses will take precedence
            # _if_ there is an ipv6_address configured for the node.
            ipv6_virtual_router_addresses:

                # IPv6_address.
              - <str>

            # Name of the IPv4 access-list to be assigned in the ingress direction.
            # The access-list must be defined under `ipv4_acls` and supports substitution of the field "interface_ip".
            ipv4_acl_in: <str>

            # Name of the IPv4 Access-list to be assigned in the egress direction.
            # The access-list must be defined under `ipv4_acls` and supports substitution of the field "interface_ip".
            ipv4_acl_out: <str>

            # IP helper for DHCP relay.
            ip_helpers:

                # IPv4 DHCP server IP.
              - ip_helper: <str; required; unique>

                # Interface name to originate DHCP relay packets to DHCP server.
                source_interface: <str>

                # VRF to originate DHCP relay packets to DHCP server. If not set, EOS uses the VRF on the SVI.
                source_vrf: <str>

            # By default the VNI will be derived from "mac_vrf_vni_base".
            # The vni_override allows us to override this value and statically define it (optional).
            vni_override: <int; 1-16777215>

            # By default the MAC VRF RT will be derived from mac_vrf_id_base + vlan_id.
            # The rt_override allows us to override this value and statically define it.
            # rt_override will default to vni_override if set.
            #
            # rt_override supports two formats:
            #   - A single number which will be used in the RT fields instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rt_type' for details).
            #   - A full RT string with colon separator which will override the full RT.
            rt_override: <str>

            # By default the MAC VRF RD will be derived from mac_vrf_id_base + vlan_id.
            # The rt_override allows us to override this value and statically define it.
            # rd_override will default to rt_override or vni_override if set.
            #
            # rd_override supports two formats:
            #   - A single number which will be used in the RD assigned number field instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rd_type' for details).
            #   - A full RD string with colon separator which will override the full RD.
            rd_override: <str>
            trunk_groups:

                # Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group.
                # Requires "enable_trunk_groups: true".
              - <str>

            # Extend this SVI over VXLAN.
            vxlan: <bool; default=True>

            # Setting spanning-tree priority per VLAN is only supported with `spanning_tree_mode: rapid-pvst` under node type settings.
            # The default priority for rapid-PVST is set under the node type settings with `spanning_tree_priority` (default=32768).
            spanning_tree_priority: <int>

            # Interface MTU.
            mtu: <int>
            bgp:

              # Structured configuration and EOS CLI commands rendered on router_bgp.vlans.[id=<vlan>].
              # This configuration will not be applied to vlan aware bundles.
              structured_config: <dict>

              # EOS CLI rendered directly on the Router BGP, VLAN definition in the final EOS configuration.
              raw_eos_cli: <str>

            # EOS CLI rendered directly on the VLAN interface in the final EOS configuration.
            raw_eos_cli: <str>

            # Custom structured config added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.
            structured_config: <dict>

            # Explicitly extend SVI to remote EVPN domains.
            # Overrides `<network_services_key>[].evpn_l2_multi_domain` and `<network_services_key>[].vrfs[].evpn_l2_multi_domain`.
            # Not supported in conjunction with EVPN vlan aware bundles. i.e. `evpn_vlan_aware_bundles: true` or `<network_services_key>[].evpn_vlan_bundle` or `<network_services_key>[].vrfs[].svis[].evpn_vlan_bundle`.
            evpn_l2_multi_domain: <bool>

        # VLAN name.
        name: <str>

        # Enable or disable interface.
        enabled: <bool>

        # SVI description. By default set to VLAN name.
        description: <str>

        # IPv4_address/Mask. Usually set under "nodes" to have unique IPv4 addresses per node.
        ip_address: <str>

        # IPv6_address/Mask. Usually set under "nodes" to have unique IPv6 addresses per node.
        ipv6_address: <str>

        # Explicitly enable/disable link-local IPv6 addressing.
        ipv6_enable: <bool>

        # IPv4_address/Mask.
        # IPv4 VXLAN Anycast IP address.
        # Conserves IP addresses in VXLAN deployments as it doesn't require unique IP addresses on each node.
        ip_address_virtual: <str>

        # IPv6 VXLAN Anycast IP addresses.
        # Conserves IPv6 addresses in VXLAN deployments as it doesn't require unique IPv6 addresses on each node.
        ipv6_address_virtuals:

            # IPv6_address/Mask.
          - <str>

        # Secondary IPv4 VXLAN Anycast IP addresses.
        ip_address_virtual_secondaries:

            # IPv4_address/Mask.
          - <str>

        # IPv4 VARP addresses.
        # Requires an IP address to be configured on the SVI.
        # If ip_address_virtual is also set, ip_virtual_router_addresses will take precedence
        # _if_ there is an ip_address configured for the node.
        ip_virtual_router_addresses:

            # IPv4_address/Mask or IPv4_address.
            # IPv4_address/Mask will also configure a static route to the SVI per best practice.
          - <str>

        # IPv6 VARP addresses.
        # Requires an IPv6 address to be configured on the SVI.
        # If ipv6_address_virtuals is also set, ipv6_virtual_router_addresses will take precedence
        # _if_ there is an ipv6_address configured for the node.
        ipv6_virtual_router_addresses:

            # IPv6_address.
          - <str>

        # Name of the IPv4 access-list to be assigned in the ingress direction.
        # The access-list must be defined under `ipv4_acls` and supports substitution of the field "interface_ip".
        ipv4_acl_in: <str>

        # Name of the IPv4 Access-list to be assigned in the egress direction.
        # The access-list must be defined under `ipv4_acls` and supports substitution of the field "interface_ip".
        ipv4_acl_out: <str>

        # IP helper for DHCP relay.
        ip_helpers:

            # IPv4 DHCP server IP.
          - ip_helper: <str; required; unique>

            # Interface name to originate DHCP relay packets to DHCP server.
            source_interface: <str>

            # VRF to originate DHCP relay packets to DHCP server. If not set, EOS uses the VRF on the SVI.
            source_vrf: <str>

        # By default the VNI will be derived from "mac_vrf_vni_base".
        # The vni_override allows us to override this value and statically define it (optional).
        vni_override: <int; 1-16777215>

        # By default the MAC VRF RT will be derived from mac_vrf_id_base + vlan_id.
        # The rt_override allows us to override this value and statically define it.
        # rt_override will default to vni_override if set.
        #
        # rt_override supports two formats:
        #   - A single number which will be used in the RT fields instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rt_type' for details).
        #   - A full RT string with colon separator which will override the full RT.
        rt_override: <str>

        # By default the MAC VRF RD will be derived from mac_vrf_id_base + vlan_id.
        # The rt_override allows us to override this value and statically define it.
        # rd_override will default to rt_override or vni_override if set.
        #
        # rd_override supports two formats:
        #   - A single number which will be used in the RD assigned number field instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rd_type' for details).
        #   - A full RD string with colon separator which will override the full RD.
        rd_override: <str>
        trunk_groups:

            # Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group.
            # Requires "enable_trunk_groups: true".
          - <str>

        # Extend this SVI over VXLAN.
        vxlan: <bool; default=True>

        # Setting spanning-tree priority per VLAN is only supported with `spanning_tree_mode: rapid-pvst` under node type settings.
        # The default priority for rapid-PVST is set under the node type settings with `spanning_tree_priority` (default=32768).
        spanning_tree_priority: <int>

        # Interface MTU.
        mtu: <int>
        bgp:

          # Structured configuration and EOS CLI commands rendered on router_bgp.vlans.[id=<vlan>].
          # This configuration will not be applied to vlan aware bundles.
          structured_config: <dict>

          # EOS CLI rendered directly on the Router BGP, VLAN definition in the final EOS configuration.
          raw_eos_cli: <str>

        # EOS CLI rendered directly on the VLAN interface in the final EOS configuration.
        raw_eos_cli: <str>

        # Custom structured config added under vlan_interfaces.[name=<interface>] for eos_cli_config_gen.
        structured_config: <dict>

        # Explicitly extend SVI to remote EVPN domains.
        # Overrides `<network_services_key>[].evpn_l2_multi_domain` and `<network_services_key>[].vrfs[].evpn_l2_multi_domain`.
        # Not supported in conjunction with EVPN vlan aware bundles. i.e. `evpn_vlan_aware_bundles: true` or `<network_services_key>[].evpn_vlan_bundle` or `<network_services_key>[].vrfs[].svis[].evpn_vlan_bundle`.
        evpn_l2_multi_domain: <bool>
    ```
