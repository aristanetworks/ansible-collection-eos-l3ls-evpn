<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;network_services_keys.name&gt;</samp>](## "<network_services_keys.name>") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "<network_services_keys.name>.[].name") | String | Required, Unique |  |  | Specify a tenant name.<br>Tenant provide a construct to group L3 VRFs and L2 VLANs.<br>Networks services can be filtered by tenant name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enable_mlag_ibgp_peering_vrfs</samp>](## "<network_services_keys.name>.[].enable_mlag_ibgp_peering_vrfs") | Boolean |  |  |  | MLAG iBGP peering per VRF.<br>By default an iBGP peering is configured per VRF between MLAG peers on separate VLANs.<br>Setting `enable_mlag_ibgp_peering_vrfs` false under a tenant will change this default to prevent configuration of these peerings and VLANs for all VRFs in the tenant.<br>This setting can be overridden per VRF.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;redistribute_mlag_ibgp_peering_vrfs</samp>](## "<network_services_keys.name>.[].redistribute_mlag_ibgp_peering_vrfs") | Boolean |  | `False` |  | Redistribute the connected subnet for the MLAG iBGP peering per VRF into overlay BGP.<br>By default the iBGP peering subnet is not redistributed into the overlay routing protocol per VRF.<br>Setting `redistribute_mlag_ibgp_peering_vrfs: true` under a tenant will change this default to redistribution of these subnets for all VRFs in the tenant.<br>This setting can be overridden per VRF.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "<network_services_keys.name>.[].vrfs") | List, items: Dictionary |  |  |  | VRFs will only be configured on a node if any of the underlying objects like `svis` or `l3_interfaces` apply to the node.<br><br>It is recommended to only define a VRF in one Tenant. If the same VRF name is used across multiple tenants and those tenants<br>are accepted by `filter.tenants` on the node, any object set under the duplicate VRFs must either be unique or be an exact match.<br><br>VRF "default" is partially supported under network-services. Currently the supported options for "default" vrf are route-target,<br>route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.<br>Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<network_services_keys.name>.[].vrfs.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_families</samp>](## "<network_services_keys.name>.[].vrfs.[].address_families") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].address_families.[]") | String |  |  | Valid Values:<br>- <code>evpn</code><br>- <code>vpn-ipv4</code><br>- <code>vpn-ipv6</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "<network_services_keys.name>.[].vrfs.[].description") | String |  |  |  | VRF description. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf_vni</samp>](## "<network_services_keys.name>.[].vrfs.[].vrf_vni") | Integer |  |  | Min: 1<br>Max: 16777215 | Required if "vrf_id" is not set.<br>The VRF VNI range is not limited, but if vrf_id is not set, "vrf_vni" is used for calculating MLAG iBGP peering vlan id.<br>"vrf_vni" may also be used for VRF RD/RT ID. See "overlay_rd_type" and "overlay_rt_type" for details.<br>See "mlag_ibgp_peering_vrfs.base_vlan" for details.<br>If vrf_vni > 10000 make sure to adjust "mac_vrf_vni_base" accordingly to avoid overlap.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf_id</samp>](## "<network_services_keys.name>.[].vrfs.[].vrf_id") | Integer |  |  |  | Required if "vrf_vni" is not set.<br>"vrf_id" is used as default value for "vrf_vni" and "ospf.process_id" unless those are set.<br>"vrf_id" may also be used for VRF RD/RT ID. See "overlay_rd_type" and "overlay_rt_type" for details.<br>"vrf_id" is preferred over "vrf_vni" for MLAG iBGP peering vlan, see "mlag_ibgp_peering_vrfs.base_vlan" for details.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd_override</samp>](## "<network_services_keys.name>.[].vrfs.[].rd_override") | String |  |  |  | By default, the VRF RD will be derived from the pattern defined in `overlay_rd_type`.<br>The rd_override allows us to override this value and statically define it.<br><br>rd_override supports two formats:<br>  - A single number will be used in the RD assigned number subfield (second part of the RD).<br>  - A full RD string with colon separator which will override the full RD.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rt_override</samp>](## "<network_services_keys.name>.[].vrfs.[].rt_override") | String |  |  |  | By default, the VRF RT will be derived from the pattern defined in `overlay_rt_type`.<br>The rt_override allows us to override this value and statically define it.<br><br>rt_override supports two formats:<br>  - A single number will be used in the RT assigned number subfield (second part of the RT).<br>  - A full RT string with colon separator which will override the full RT.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_peering_ipv4_pool</samp>](## "<network_services_keys.name>.[].vrfs.[].mlag_ibgp_peering_ipv4_pool") | String |  |  |  | IPv4_address/Mask<br>The subnet used for iBGP peering in the VRF.<br>Each MLAG pair will be assigned a subnet based on the ID of the primary MLAG switch.<br>If not set, "mlag_peer_l3_ipv4_pool" or "mlag_peer_ipv4_pool" will be used.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_helpers</samp>](## "<network_services_keys.name>.[].vrfs.[].ip_helpers") | List, items: Dictionary |  |  |  | IP helper for DHCP relay. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;ip_helper</samp>](## "<network_services_keys.name>.[].vrfs.[].ip_helpers.[].ip_helper") | String | Required, Unique |  |  | IPv4 DHCP server IP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "<network_services_keys.name>.[].vrfs.[].ip_helpers.[].source_interface") | String |  |  |  | Interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_vrf</samp>](## "<network_services_keys.name>.[].vrfs.[].ip_helpers.[].source_vrf") | String |  |  |  | VRF to originate DHCP relay packets to DHCP server. If not set, uses current VRF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_mlag_ibgp_peering_vrfs</samp>](## "<network_services_keys.name>.[].vrfs.[].enable_mlag_ibgp_peering_vrfs") | Boolean |  |  |  | MLAG iBGP peering per VRF.<br>By default an iBGP peering is configured per VRF between MLAG peers on separate VLANs.<br>Setting `enable_mlag_ibgp_peering_vrfs: false` under a VRF will change this default and/or override the tenant-wide setting.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_mlag_ibgp_peering_vrfs</samp>](## "<network_services_keys.name>.[].vrfs.[].redistribute_mlag_ibgp_peering_vrfs") | Boolean |  | `False` |  | Redistribute the connected subnet for the MLAG iBGP peering per VRF into overlay BGP.<br>By default the iBGP peering subnet is not redistributed into the overlay routing protocol per VRF.<br>Setting `redistribute_mlag_ibgp_peering_vrfs: true` under a VRF will change this default and/or override the tenant-wide setting.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_ibgp_peering_vlan</samp>](## "<network_services_keys.name>.[].vrfs.[].mlag_ibgp_peering_vlan") | Integer |  |  | Min: 1<br>Max: 4096 | Manually define the VLAN used on the MLAG pair for the iBGP session.<br>By default this parameter is calculated using the following formula: `<mlag_ibgp_peering_vrfs.base_vlan>` + `<vrf_id>` - 1.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_diagnostic</samp>](## "<network_services_keys.name>.[].vrfs.[].vtep_diagnostic") | Dictionary |  |  |  | Enable VTEP Network diagnostics.<br>This will create a loopback with virtual source-nat enable to perform diagnostics from the switch.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback</samp>](## "<network_services_keys.name>.[].vrfs.[].vtep_diagnostic.loopback") | Integer |  |  | Min: 2<br>Max: 2100 | Loopback interface number, required when vtep_diagnotics defined.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_description</samp>](## "<network_services_keys.name>.[].vrfs.[].vtep_diagnostic.loopback_description") | String |  |  |  | Provide a custom description or description template to be used on the VRF diagnostic loopback interface.<br>This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.<br>The available template fields are:<br>  - `interface`: The Loopback interface name.<br>  - `vrf`: The VRF name.<br>  - `tenant`: The tenant name.<br><br>The default description is set by `default_vrf_diag_loopback_description`.<br>By default the description is templated from the VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ip_range</samp>](## "<network_services_keys.name>.[].vrfs.[].vtep_diagnostic.loopback_ip_range") | String |  |  |  | IPv4_address/Mask.<br>Loopback ip range, a unique ip is derived from this ranged and assignedto each l3 leaf based on it's unique id.<br>Loopback is not created unless loopback_ip_range or loopback_ip_pools are set.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_ip_pools</samp>](## "<network_services_keys.name>.[].vrfs.[].vtep_diagnostic.loopback_ip_pools") | List, items: Dictionary |  |  |  | For inventories with multiple PODs a loopback range can be set per POD to avoid overlaps.<br>This only takes effect when loopback_ip_range is not defined, ptional (loopback is not created unless loopback_ip_range or loopback_ip_pools are set).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;pod</samp>](## "<network_services_keys.name>.[].vrfs.[].vtep_diagnostic.loopback_ip_pools.[].pod") | String |  |  |  | POD name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_pool</samp>](## "<network_services_keys.name>.[].vrfs.[].vtep_diagnostic.loopback_ip_pools.[].ipv4_pool") | String |  |  |  | IPv4_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;static_routes</samp>](## "<network_services_keys.name>.[].vrfs.[].static_routes") | List, items: Dictionary |  |  |  | List of static routes for v4 and/or v6.<br>This will create static routes inside the tenant VRF.<br>If nodes are not specified, all l3leafs that carry the VRF will also be applied the static routes.<br>If a node has a static route in the VRF, redistribute static will be automatically enabled in that VRF.<br>This automatic behavior can be overridden non-selectively with the redistribute_static knob for the VRF.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;destination_address_prefix</samp>](## "<network_services_keys.name>.[].vrfs.[].static_routes.[].destination_address_prefix") | String |  |  |  | IPv4_address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gateway</samp>](## "<network_services_keys.name>.[].vrfs.[].static_routes.[].gateway") | String |  |  |  | IPv4_address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;track_bfd</samp>](## "<network_services_keys.name>.[].vrfs.[].static_routes.[].track_bfd") | Boolean |  |  |  | Track next-hop using BFD. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "<network_services_keys.name>.[].vrfs.[].static_routes.[].distance") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tag</samp>](## "<network_services_keys.name>.[].vrfs.[].static_routes.[].tag") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<network_services_keys.name>.[].vrfs.[].static_routes.[].name") | String |  |  |  | description. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metric</samp>](## "<network_services_keys.name>.[].vrfs.[].static_routes.[].metric") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "<network_services_keys.name>.[].vrfs.[].static_routes.[].interface") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<network_services_keys.name>.[].vrfs.[].static_routes.[].nodes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].static_routes.[].nodes.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_static_routes</samp>](## "<network_services_keys.name>.[].vrfs.[].ipv6_static_routes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;destination_address_prefix</samp>](## "<network_services_keys.name>.[].vrfs.[].ipv6_static_routes.[].destination_address_prefix") | String |  |  |  | IPv6_address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;gateway</samp>](## "<network_services_keys.name>.[].vrfs.[].ipv6_static_routes.[].gateway") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;track_bfd</samp>](## "<network_services_keys.name>.[].vrfs.[].ipv6_static_routes.[].track_bfd") | Boolean |  |  |  | Track next-hop using BFD. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "<network_services_keys.name>.[].vrfs.[].ipv6_static_routes.[].distance") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tag</samp>](## "<network_services_keys.name>.[].vrfs.[].ipv6_static_routes.[].tag") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<network_services_keys.name>.[].vrfs.[].ipv6_static_routes.[].name") | String |  |  |  | description. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;metric</samp>](## "<network_services_keys.name>.[].vrfs.[].ipv6_static_routes.[].metric") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "<network_services_keys.name>.[].vrfs.[].ipv6_static_routes.[].interface") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<network_services_keys.name>.[].vrfs.[].ipv6_static_routes.[].nodes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].ipv6_static_routes.[].nodes.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_static</samp>](## "<network_services_keys.name>.[].vrfs.[].redistribute_static") | Boolean |  |  |  | Enable or disable the redistribution of all static routes to BGP in the VRF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redistribute_connected</samp>](## "<network_services_keys.name>.[].vrfs.[].redistribute_connected") | Boolean |  | `True` |  | Enable or disable the redistribution of all connected routes to BGP in the VRF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp.enabled") | Boolean |  |  |  | Force (no) configuration of BGP for the VRF.<br>If not set, BGP will be configured when needed according to the following rules:<br>- If the VRF is part of an overlay (`evpn` or `mpls`), BGP will be configured for it.<br>- If any BGP peers are configured under the VRF, BGP will be configured for it. This is useful for L2LS designs with VRFs.<br>- If uplink type is `p2p-vrfs` *and* the vrf is included in the uplink VRFs, BGP will be configured for it. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the Router BGP, VRF definition in the final EOS configuration.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<network_services_keys.name>.[].vrfs.[].bgp.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.vrfs.[name=<vrf>] for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;additional_route_targets</samp>](## "<network_services_keys.name>.[].vrfs.[].additional_route_targets") | List, items: Dictionary |  |  |  | Configuration of extra route-targets for this VRF. Useful for route-leaking or gateway between address families. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;type</samp>](## "<network_services_keys.name>.[].vrfs.[].additional_route_targets.[].type") | String |  |  | Valid Values:<br>- <code>import</code><br>- <code>export</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_family</samp>](## "<network_services_keys.name>.[].vrfs.[].additional_route_targets.[].address_family") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_target</samp>](## "<network_services_keys.name>.[].vrfs.[].additional_route_targets.[].route_target") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<network_services_keys.name>.[].vrfs.[].additional_route_targets.[].nodes") | List, items: String |  |  |  | Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].additional_route_targets.[].nodes.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "<network_services_keys.name>.[].vrfs.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the root level of the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<network_services_keys.name>.[].vrfs.[].structured_config") | Dictionary |  |  |  | Custom structured config for eos_cli_config_gen. |
    | [<samp>mlag_ibgp_peering_vrfs</samp>](## "mlag_ibgp_peering_vrfs") | Dictionary |  |  |  | On mlag leafs, an SVI interface is defined per vrf, to establish iBGP peering (required when there are MLAG leafs in topology).<br>The SVI id will be derived from the base vlan defined: mlag_ibgp_peering_vrfs.base_vlan + (vrf_id or vrf_vni) - 1.<br>Depending on the values of vrf_id / vrf_vni it may be required to adjust the base_vlan to avoid overlaps or invalid vlan ids.<br>The SVI ip address derived from mlag_l3_peer_ipv4_pool is re-used across all iBGP peerings.<br> |
    | [<samp>&nbsp;&nbsp;base_vlan</samp>](## "mlag_ibgp_peering_vrfs.base_vlan") | Integer |  | `3000` | Min: 1<br>Max: 4093 |  |

=== "YAML"

    ```yaml
    <network_services_keys.name>:

        # Specify a tenant name.
        # Tenant provide a construct to group L3 VRFs and L2 VLANs.
        # Networks services can be filtered by tenant name.
      - name: <str; required; unique>

        # MLAG iBGP peering per VRF.
        # By default an iBGP peering is configured per VRF between MLAG peers on separate VLANs.
        # Setting `enable_mlag_ibgp_peering_vrfs` false under a tenant will change this default to prevent configuration of these peerings and VLANs for all VRFs in the tenant.
        # This setting can be overridden per VRF.
        enable_mlag_ibgp_peering_vrfs: <bool>

        # Redistribute the connected subnet for the MLAG iBGP peering per VRF into overlay BGP.
        # By default the iBGP peering subnet is not redistributed into the overlay routing protocol per VRF.
        # Setting `redistribute_mlag_ibgp_peering_vrfs: true` under a tenant will change this default to redistribution of these subnets for all VRFs in the tenant.
        # This setting can be overridden per VRF.
        redistribute_mlag_ibgp_peering_vrfs: <bool; default=False>

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
            address_families:
              - <str; "evpn" | "vpn-ipv4" | "vpn-ipv6">

            # VRF description.
            description: <str>

            # Required if "vrf_id" is not set.
            # The VRF VNI range is not limited, but if vrf_id is not set, "vrf_vni" is used for calculating MLAG iBGP peering vlan id.
            # "vrf_vni" may also be used for VRF RD/RT ID. See "overlay_rd_type" and "overlay_rt_type" for details.
            # See "mlag_ibgp_peering_vrfs.base_vlan" for details.
            # If vrf_vni > 10000 make sure to adjust "mac_vrf_vni_base" accordingly to avoid overlap.
            vrf_vni: <int; 1-16777215>

            # Required if "vrf_vni" is not set.
            # "vrf_id" is used as default value for "vrf_vni" and "ospf.process_id" unless those are set.
            # "vrf_id" may also be used for VRF RD/RT ID. See "overlay_rd_type" and "overlay_rt_type" for details.
            # "vrf_id" is preferred over "vrf_vni" for MLAG iBGP peering vlan, see "mlag_ibgp_peering_vrfs.base_vlan" for details.
            vrf_id: <int>

            # By default, the VRF RD will be derived from the pattern defined in `overlay_rd_type`.
            # The rd_override allows us to override this value and statically define it.
            #
            # rd_override supports two formats:
            #   - A single number will be used in the RD assigned number subfield (second part of the RD).
            #   - A full RD string with colon separator which will override the full RD.
            rd_override: <str>

            # By default, the VRF RT will be derived from the pattern defined in `overlay_rt_type`.
            # The rt_override allows us to override this value and statically define it.
            #
            # rt_override supports two formats:
            #   - A single number will be used in the RT assigned number subfield (second part of the RT).
            #   - A full RT string with colon separator which will override the full RT.
            rt_override: <str>

            # IPv4_address/Mask
            # The subnet used for iBGP peering in the VRF.
            # Each MLAG pair will be assigned a subnet based on the ID of the primary MLAG switch.
            # If not set, "mlag_peer_l3_ipv4_pool" or "mlag_peer_ipv4_pool" will be used.
            mlag_ibgp_peering_ipv4_pool: <str>

            # IP helper for DHCP relay.
            ip_helpers:

                # IPv4 DHCP server IP.
              - ip_helper: <str; required; unique>

                # Interface name.
                source_interface: <str>

                # VRF to originate DHCP relay packets to DHCP server. If not set, uses current VRF.
                source_vrf: <str>

            # MLAG iBGP peering per VRF.
            # By default an iBGP peering is configured per VRF between MLAG peers on separate VLANs.
            # Setting `enable_mlag_ibgp_peering_vrfs: false` under a VRF will change this default and/or override the tenant-wide setting.
            enable_mlag_ibgp_peering_vrfs: <bool>

            # Redistribute the connected subnet for the MLAG iBGP peering per VRF into overlay BGP.
            # By default the iBGP peering subnet is not redistributed into the overlay routing protocol per VRF.
            # Setting `redistribute_mlag_ibgp_peering_vrfs: true` under a VRF will change this default and/or override the tenant-wide setting.
            redistribute_mlag_ibgp_peering_vrfs: <bool; default=False>

            # Manually define the VLAN used on the MLAG pair for the iBGP session.
            # By default this parameter is calculated using the following formula: `<mlag_ibgp_peering_vrfs.base_vlan>` + `<vrf_id>` - 1.
            mlag_ibgp_peering_vlan: <int; 1-4096>

            # Enable VTEP Network diagnostics.
            # This will create a loopback with virtual source-nat enable to perform diagnostics from the switch.
            vtep_diagnostic:

              # Loopback interface number, required when vtep_diagnotics defined.
              loopback: <int; 2-2100>

              # Provide a custom description or description template to be used on the VRF diagnostic loopback interface.
              # This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
              # The available template fields are:
              #   - `interface`: The Loopback interface name.
              #   - `vrf`: The VRF name.
              #   - `tenant`: The tenant name.
              #
              # The default description is set by `default_vrf_diag_loopback_description`.
              # By default the description is templated from the VRF name.
              loopback_description: <str>

              # IPv4_address/Mask.
              # Loopback ip range, a unique ip is derived from this ranged and assignedto each l3 leaf based on it's unique id.
              # Loopback is not created unless loopback_ip_range or loopback_ip_pools are set.
              loopback_ip_range: <str>

              # For inventories with multiple PODs a loopback range can be set per POD to avoid overlaps.
              # This only takes effect when loopback_ip_range is not defined, ptional (loopback is not created unless loopback_ip_range or loopback_ip_pools are set).
              loopback_ip_pools:

                  # POD name.
                - pod: <str>

                  # IPv4_address/Mask.
                  ipv4_pool: <str>

            # List of static routes for v4 and/or v6.
            # This will create static routes inside the tenant VRF.
            # If nodes are not specified, all l3leafs that carry the VRF will also be applied the static routes.
            # If a node has a static route in the VRF, redistribute static will be automatically enabled in that VRF.
            # This automatic behavior can be overridden non-selectively with the redistribute_static knob for the VRF.
            static_routes:

                # IPv4_address.
              - destination_address_prefix: <str>

                # IPv4_address.
                gateway: <str>

                # Track next-hop using BFD.
                track_bfd: <bool>
                distance: <int; 1-255>
                tag: <int; 0-4294967295>

                # description.
                name: <str>
                metric: <int; 0-4294967295>
                interface: <str>
                nodes:
                  - <str>
            ipv6_static_routes:

                # IPv6_address.
              - destination_address_prefix: <str>
                gateway: <str>

                # Track next-hop using BFD.
                track_bfd: <bool>
                distance: <int; 1-255>
                tag: <int; 0-4294967295>

                # description.
                name: <str>
                metric: <int; 0-4294967295>
                interface: <str>
                nodes:
                  - <str>

            # Enable or disable the redistribution of all static routes to BGP in the VRF.
            redistribute_static: <bool>

            # Enable or disable the redistribution of all connected routes to BGP in the VRF.
            redistribute_connected: <bool; default=True>
            bgp:

              # Force (no) configuration of BGP for the VRF.
              # If not set, BGP will be configured when needed according to the following rules:
              # - If the VRF is part of an overlay (`evpn` or `mpls`), BGP will be configured for it.
              # - If any BGP peers are configured under the VRF, BGP will be configured for it. This is useful for L2LS designs with VRFs.
              # - If uplink type is `p2p-vrfs` *and* the vrf is included in the uplink VRFs, BGP will be configured for it.
              enabled: <bool>

              # EOS CLI rendered directly on the Router BGP, VRF definition in the final EOS configuration.
              raw_eos_cli: <str>

              # Custom structured config added under router_bgp.vrfs.[name=<vrf>] for eos_cli_config_gen.
              structured_config: <dict>

            # Configuration of extra route-targets for this VRF. Useful for route-leaking or gateway between address families.
            additional_route_targets:
              - type: <str; "import" | "export">
                address_family: <str>
                route_target: <str>

                # Nodes is required to restrict configuration of BGP neighbors to certain nodes in the network.
                nodes:
                  - <str>

            # EOS CLI rendered directly on the root level of the final EOS configuration.
            raw_eos_cli: <str>

            # Custom structured config for eos_cli_config_gen.
            structured_config: <dict>

    # On mlag leafs, an SVI interface is defined per vrf, to establish iBGP peering (required when there are MLAG leafs in topology).
    # The SVI id will be derived from the base vlan defined: mlag_ibgp_peering_vrfs.base_vlan + (vrf_id or vrf_vni) - 1.
    # Depending on the values of vrf_id / vrf_vni it may be required to adjust the base_vlan to avoid overlaps or invalid vlan ids.
    # The SVI ip address derived from mlag_l3_peer_ipv4_pool is re-used across all iBGP peerings.
    mlag_ibgp_peering_vrfs:
      base_vlan: <int; 1-4093; default=3000>
    ```
