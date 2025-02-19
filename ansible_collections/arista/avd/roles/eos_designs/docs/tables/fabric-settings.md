<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>default_underlay_p2p_ethernet_description</samp>](## "default_underlay_p2p_ethernet_description") | String |  | `P2P_{peer}_{peer_interface}{vrf?<_VRF_}` |  | The default description or description template to be used on L3 point-to-point ethernet interfaces.<br>The interfaces using this are the routed uplinks and `p2p_links` defined under `l3_edge` or `core_interfaces`.<br>This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.<br>The available template fields are:<br>  - `peer`: The name of the peer.<br>  - `interface`: The local interface name.<br>  - `peer_interface`: The interface on the peer.<br>  - `vrf`: The name of the VRF if set (Only applicable for `uplink_type: p2p-vrfs`).<br><br>By default the description is templated from the name and interface of the peer. |
    | [<samp>default_underlay_p2p_port_channel_description</samp>](## "default_underlay_p2p_port_channel_description") | String |  | `P2P_{peer}_{peer_interface}` |  | The default description or description template to be used on L3 point-to-point port-channel interfaces.<br>The port-channels using this are `p2p_links` defined under `l3_edge` or `core_interfaces`.<br>This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.<br>The available template fields are:<br>  - `peer`: The name of the peer.<br>  - `interface`: The local interface name.<br>  - `peer_interface`: The interface on the peer.<br>  - `port_channel_id`: The local port-channel ID.<br>  - `peer_port_channel_id`: The ID of the port-channel on the peer.<br><br>By default the description is templated from the name and interface of the peer. |
    | [<samp>default_vrf_diag_loopback_description</samp>](## "default_vrf_diag_loopback_description") | String |  | `DIAG_VRF_{vrf}` |  | The default description or description template to be used on VRF diagnostic loopback interfaces.<br>This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.<br>The available template fields are:<br>  - `interface`: The Loopback interface name.<br>  - `vrf`: The VRF name.<br>  - `tenant`: The tenant name.<br><br>By default the description is templated from the VRF name. |
    | [<samp>enable_trunk_groups</samp>](## "enable_trunk_groups") | Boolean |  | `False` |  | Enable Trunk Group support across eos_designs.<br>Warning: Because of the nature of the EOS Trunk Group feature, enabling this is "all or nothing".<br>*All* vlans and *all* trunks towards connected endpoints must be using trunk groups as well.<br>If trunk groups are not assigned to a trunk, no vlans will be enabled on that trunk.<br>See "Details on enable_trunk_groups" below before enabling this feature.<br> |
    | [<samp>mlag_bgp_peer_description</samp>](## "mlag_bgp_peer_description") | String |  | `{mlag_peer}_{peer_interface}` |  | Description or description template to be used on the MLAG BGP peers including those in VRFs.<br>This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.<br>The available template fields are:<br>  - `mlag_peer`: The name of the MLAG peer.<br>  - `interface`: The local MLAG L3 VLAN interface.<br>  - `peer_interface`: The MLAG L3 VLAN interface on the MLAG peer.<br>  - `vrf`: The name of the VRF. Not available for the underlay peering.<br><br>The default description is built from the name and interface of the MLAG peer and optionally the VRF. |
    | [<samp>mlag_bgp_peer_group_description</samp>](## "mlag_bgp_peer_group_description") | String |  | `{mlag_peer}` |  | Description or description template to be used on the MLAG BGP peer-group.<br>This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.<br>The available template fields are:<br>  - `mlag_peer`: The name of the MLAG peer.<br><br>The default description is the name of the MLAG peers. |
    | [<samp>mlag_member_description</samp>](## "mlag_member_description") | String |  | `MLAG_{mlag_peer}_{peer_interface}` |  | Description or description template to be used on MLAG peer-link ethernet interfaces.<br>This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.<br>The available template fields are:<br>  - `mlag_peer`: The name of the MLAG peer.<br>  - `interface`: The local MLAG port-channel interface.<br>  - `peer_interface`: The port-channel interface on the MLAG peer.<br>  - `mlag_port_channel_id`: The local MLAG port-channel ID.<br>  - `mlag_peer_port_channel_id`: The port-channel ID on the MLAG peer.<br><br>By default the description is templated from the name and interface of the MLAG peer. |
    | [<samp>mlag_on_orphan_port_channel_downlink</samp>](## "mlag_on_orphan_port_channel_downlink") | Boolean |  | `False` |  | If `true` an MLAG ID will always be configured on a Port-Channel downlink even if the downlink is only on one node in the MLAG pair.<br>If `false` (default) an MLAG ID will only be configured on Port-Channel downlinks dual-homed to two MLAG switches. |
    | [<samp>mlag_peer_l3_svi_description</samp>](## "mlag_peer_l3_svi_description") | String |  | `MLAG_L3` |  | Description or description template to be used on MLAG L3 peering SVI (Interface Vlan4093 by default).<br>This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.<br>The available template fields are:<br>  - `mlag_peer`: The name of the MLAG peer.<br>  - `interface`: The MLAG L3 peering SVI name.<br>  - `mlag_peer_l3_vlan`: The MLAG L3 peering VLAN ID. |
    | [<samp>mlag_peer_l3_vlan_name</samp>](## "mlag_peer_l3_vlan_name") | String |  | `MLAG_L3` |  | Name or name template to be used on MLAG L3 VLAN (VLAN 4093 by default).<br>This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.<br>The available template fields are:<br>  - `mlag_peer`: The name of the MLAG peer.<br>  - `mlag_peer_l3_vlan`: The MLAG L3 peering VLAN ID. |
    | [<samp>mlag_peer_l3_vrf_svi_description</samp>](## "mlag_peer_l3_vrf_svi_description") | String |  | `MLAG_L3_VRF_{vrf}` |  | Description or description template to be used on MLAG L3 peering SVI for VRFs.<br>This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.<br>The available template fields are:<br>  - `mlag_peer`: The name of the MLAG peer.<br>  - `interface`: The MLAG L3 VRF peering SVI name.<br>  - `vlan`: The MLAG L3 VRF peering VLAN ID.<br>  - `vrf`: The VRF name. |
    | [<samp>mlag_peer_l3_vrf_vlan_name</samp>](## "mlag_peer_l3_vrf_vlan_name") | String |  | `MLAG_L3_VRF_{vrf}` |  | Name or name template to be used on MLAG L3 peering VLAN for VRFs.<br>This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.<br>The available template fields are:<br>  - `mlag_peer`: The name of the MLAG peer.<br>  - `vlan`: The MLAG L3 VRF peering VLAN ID.<br>  - `vrf`: The VRF name. |
    | [<samp>mlag_peer_svi_description</samp>](## "mlag_peer_svi_description") | String |  | `MLAG` |  | Description or description template to be used on MLAG peering SVI (Interface Vlan4094 by default).<br>This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.<br>The available template fields are:<br>  - `mlag_peer`: The name of the MLAG peer.<br>  - `interface`: The MLAG peering SVI name.<br>  - `mlag_peer_vlan`: The MLAG peering VLAN ID. |
    | [<samp>mlag_peer_vlan_name</samp>](## "mlag_peer_vlan_name") | String |  | `MLAG` |  | Name or name template to be used on MLAG peering VLAN (VLAN 4094 by default).<br>This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.<br>The available template fields are:<br>  - `mlag_peer`: The name of the MLAG peer.<br>  - `mlag_peer_vlan`: The MLAG peering VLAN ID. |
    | [<samp>mlag_port_channel_description</samp>](## "mlag_port_channel_description") | String |  | `MLAG_{mlag_peer}_{peer_interface}` |  | Description or description template to be used on MLAG peer-link port-channel interfaces.<br>This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.<br>The available template fields are:<br>  - `mlag_peer`: The name of the MLAG peer.<br>  - `interface`: The local MLAG port-channel interface.<br>  - `peer_interface`: The port-channel interface on the MLAG peer.<br>  - `mlag_port_channel_id`: The local MLAG port-channel ID.<br>  - `mlag_peer_port_channel_id`: The port-channel ID on the MLAG peer.<br><br>By default the description is templated from the name and port-channel interface of the MLAG peer. |
    | [<samp>only_local_vlan_trunk_groups</samp>](## "only_local_vlan_trunk_groups") | Boolean |  | `False` |  | A vlan can have many trunk_groups assigned.<br>To avoid unneeded configuration changes on all leaf switches when a new trunk group is added,<br>this feature will only configure the vlan trunk groups matched with local connected_endpoints.<br>See "Details on only_local_vlan_trunk_groups" below.<br>Requires "enable_trunk_groups: true".<br> |
    | [<samp>p2p_uplinks_mtu</samp>](## "p2p_uplinks_mtu") | Integer |  | `9214` | Min: 68<br>Max: 65535 | Point to Point Links MTU.<br>Precedence: <node_type>.uplink_mtu -> platform_settings.p2p_uplinks_mtu -> p2p_uplinks_mtu -> 9214 |
    | [<samp>p2p_uplinks_qos_profile</samp>](## "p2p_uplinks_qos_profile") | String |  |  |  | QOS Profile assigned on all infrastructure links. |
    | [<samp>shutdown_bgp_towards_undeployed_peers</samp>](## "shutdown_bgp_towards_undeployed_peers") | Boolean |  | `True` |  | When a device is set undeployed using `is_deployed: false` and `shutdown_bgp_towards_undeployed_peers` key is set to true, the BGP neighborship is shutdown on the peer. |
    | [<samp>shutdown_interfaces_towards_undeployed_peers</samp>](## "shutdown_interfaces_towards_undeployed_peers") | Boolean |  | `True` |  | - It is possible to provision configurations for a complete topology but flag devices as undeployed using the host level variable `is_deployed: false`.<br><br>```yaml<br># Use at the host level<br>is_deployed: < true or false or default -> true ><br>```<br><br>- By default, this will have no impact within the `eos_designs` role. Configs will still be generated by the `eos_cli_config_gen` role and will still be pushed by the `eos_config_deploy_eapi` directly to devices if used.<br>- However, if the `eos_config_deploy_cvp` role is used to push configurations, CloudVision will ignore the devices flagged  as `is_deployed: false` and not attempt to configure them.<br>- If the device is not present in the network due to CloudVision not configuring the device, `eos_validate_state` role will fail tests on peers of the undeployed device trying to verify that interfaces are up.<br>- To overcome this and shutdown interfaces towards undeployed peers, the variable `shutdown_interfaces_towards_undeployed_peers` can be used, satisfying the `eos_validate_state` role interface tests.<br>- Again, this is only an issue if `eos_config_deploy_cvp` is used and the devices are not present in the network.<br> |
    | [<samp>trunk_groups</samp>](## "trunk_groups") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;mlag</samp>](## "trunk_groups.mlag") | Dictionary |  |  |  | Trunk Group used for MLAG VLAN (Typically VLAN 4094).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "trunk_groups.mlag.name") | String |  | `MLAG` |  |  |
    | [<samp>&nbsp;&nbsp;mlag_l3</samp>](## "trunk_groups.mlag_l3") | Dictionary |  |  |  | Trunk Group used for MLAG L3 peering VLAN and for VRF L3 peering VLANs (Typically VLAN 4093).<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "trunk_groups.mlag_l3.name") | String |  | `MLAG` |  |  |
    | [<samp>&nbsp;&nbsp;uplink</samp>](## "trunk_groups.uplink") | Dictionary |  |  |  | Trunk Group used on L2 Leaf switches when "enable_trunk_groups" is set.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "trunk_groups.uplink.name") | String |  | `UPLINK` |  |  |
    | [<samp>underlay_filter_peer_as</samp>](## "underlay_filter_peer_as") | Boolean |  | `False` |  | Configure route-map on eBGP sessions towards underlay peers, where prefixes with the peer's ASN in the AS Path are filtered away.<br>This is very useful in very large scale networks not using EVPN overlays, where convergence will be quicker by not having to return<br>all updates received from Spine-1 to Spine-2 just for Spine-2 to throw them away because of AS Path loop detection.<br>Note that this setting cannot be used while there are EVPN services present in the default VRF.<br> |
    | [<samp>underlay_filter_redistribute_connected</samp>](## "underlay_filter_redistribute_connected") | Boolean |  | `True` |  | Filter redistribution of connected into the underlay routing protocol.<br>Only applicable when overlay_routing_protocol != 'none' and underlay_routing_protocol == BGP.<br>Creates a route-map and prefix-list assigned to redistribute connected permitting only loopbacks and inband management subnets.<br> |
    | [<samp>underlay_ipv6</samp>](## "underlay_ipv6") | Boolean |  | `False` |  | This feature allows IPv6 underlay routing protocol with RFC5549 addresses to be used along with IPv4 advertisements as VXLAN tunnel endpoints.<br>Requires "underlay_rfc5549: true" and "loopback_ipv6_pool" under the node type settings.<br> |
    | [<samp>underlay_l2_ethernet_description</samp>](## "underlay_l2_ethernet_description") | String |  | `L2_{peer}_{peer_interface}` |  | The description or description template to be used on L2 ethernet interfaces.<br>The interfaces using this are the member interfaces of port-channel uplinks.<br>This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.<br>The available template fields are:<br>  - `peer`: The name of the peer.<br>  - `interface`: The local interface name.<br>  - `peer_interface`: The interface on the peer.<br><br>By default the description is templated from the hostname and interface of the peer. |
    | [<samp>underlay_l2_port_channel_description</samp>](## "underlay_l2_port_channel_description") | String |  | `L2_{peer_node_group_or_peer}_{peer_interface}` |  | The description or description template to be used on L2 port-channel interfaces.<br>The interfaces using this are port-channel uplinks.<br>This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.<br>The available template fields are:<br>  - `peer`: The name of the peer.<br>  - `interface`: The local interface name.<br>  - `peer_interface`: The interface on the peer.<br>  - `port_channel_id`: The local port-channel ID.<br>  - `peer_port_channel_id`: The ID of the port-channel on the peer.<br>  - `peer_node_group`: The node group of the peer if the peer is an MLAG member or running EVPN A/A.<br>  - `peer_node_group_or_peer`: Helper alias of the peer_node_group or peer.<br>  - `peer_node_group_or_uppercase_peer`: Helper alias of the peer_node_group or peer hostname in uppercase.<br><br>By default the description is templated from the peer's node group (for MLAG or EVPN A/A) or hostname and port-channel interface of the peer. |
    | [<samp>underlay_multicast</samp>](## "underlay_multicast") | Boolean |  | `False` |  | Enable Multicast in the underlay on all p2p uplink interfaces and mlag l3 peer interface.<br>Specifically PIM Sparse-Mode will be configured on all routed underlay interfaces.<br>No other configuration is added, so the underlay will only support Source-Specific Multicast (SSM).<br>The configuration is intended to be used as multicast underlay for EVPN OISM overlay.<br> |
    | [<samp>underlay_multicast_anycast_rp</samp>](## "underlay_multicast_anycast_rp") | Dictionary |  |  |  | If multiple nodes are configured under 'underlay_multicast_rps.[].nodes' for the same RP address, they will be configured<br>with one of the following methods:<br>- Anycast RP using PIM (RFC4610).<br>- Anycast RP using MSDP (RFC4611).<br><br>NOTE: When using MSDP, all nodes across all MSDP enabled RPs will be added to a single MSDP mesh group named "ANYCAST-RP".<br> |
    | [<samp>&nbsp;&nbsp;mode</samp>](## "underlay_multicast_anycast_rp.mode") | String |  | `pim` | Valid Values:<br>- <code>pim</code><br>- <code>msdp</code> |  |
    | [<samp>underlay_multicast_rps</samp>](## "underlay_multicast_rps") | List, items: Dictionary |  |  |  | List of PIM Sparse-Mode Rendevouz Points configured for underlay multicast on all devices.<br>The device(s) listed under 'nodes', will be configured as the Rendevouz point router(s).<br>If multiple nodes are configured under 'nodes' for the same RP address, they will be configured<br>according to the 'underlay_multicast_anycast_rp.mode' setting.<br><br>Requires 'underlay_multicast: true'.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;rp</samp>](## "underlay_multicast_rps.[].rp") | String | Required, Unique |  |  | RP IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "underlay_multicast_rps.[].nodes") | List, items: Dictionary |  |  |  | List of nodes where a Loopback interface with the RP address will be configured.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "underlay_multicast_rps.[].nodes.[].name") | String | Required, Unique |  |  | Hostname. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loopback_number</samp>](## "underlay_multicast_rps.[].nodes.[].loopback_number") | Integer | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "underlay_multicast_rps.[].nodes.[].description") | String |  | `PIM RP` |  | Interface description. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "underlay_multicast_rps.[].groups") | List, items: String |  |  |  | List of groups to associate with the RP address set in 'rp'.<br>If access_list_name is set, a standard access-list will be configured matching these groups.<br>Otherwise the groups are configured directly on the RP command.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "underlay_multicast_rps.[].groups.[]") | String |  |  |  | Multicast Group IPv4 prefix/mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_list_name</samp>](## "underlay_multicast_rps.[].access_list_name") | String |  |  |  | Name of standard Access-List.<br> |
    | [<samp>underlay_rfc5549</samp>](## "underlay_rfc5549") | Boolean |  | `False` |  | Point to Point Underlay with RFC 5549(eBGP), i.e. IPv6 Unnumbered.<br>Requires "underlay_routing_protocol: ebgp".<br> |
    | [<samp>underlay_routing_protocol</samp>](## "underlay_routing_protocol") | String |  |  | Value is converted to lower case.<br>Valid Values:<br>- <code>ebgp</code><br>- <code>ospf</code><br>- <code>ospf-ldp</code><br>- <code>isis</code><br>- <code>isis-sr</code><br>- <code>isis-ldp</code><br>- <code>isis-sr-ldp</code><br>- <code>none</code> | - The following underlay routing protocols are supported:<br>  - EBGP (default for l3ls-evpn)<br>  - OSPF.<br>  - OSPF-LDP*.<br>  - ISIS.<br>  - ISIS-SR*.<br>  - ISIS-LDP*.<br>  - ISIS-SR-LDP*.<br>  - No underlay routing protocol (none)<br>- The variables should be applied to all devices in the fabric.<br>*Only supported with core_interfaces data model.<br> |
    | [<samp>uplink_ptp</samp>](## "uplink_ptp") | Dictionary |  |  |  | Enable PTP on all infrastructure links. |
    | [<samp>&nbsp;&nbsp;enable</samp>](## "uplink_ptp.enable") | Boolean |  | `False` |  |  |
    | [<samp>use_router_general_for_router_id</samp>](## "use_router_general_for_router_id") | Boolean |  | `False` |  | Use `router general` to set router ID for all routing protocols and VRFs. |

=== "YAML"

    ```yaml
    # The default description or description template to be used on L3 point-to-point ethernet interfaces.
    # The interfaces using this are the routed uplinks and `p2p_links` defined under `l3_edge` or `core_interfaces`.
    # This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
    # The available template fields are:
    #   - `peer`: The name of the peer.
    #   - `interface`: The local interface name.
    #   - `peer_interface`: The interface on the peer.
    #   - `vrf`: The name of the VRF if set (Only applicable for `uplink_type: p2p-vrfs`).
    #
    # By default the description is templated from the name and interface of the peer.
    default_underlay_p2p_ethernet_description: <str; default="P2P_{peer}_{peer_interface}{vrf?<_VRF_}">

    # The default description or description template to be used on L3 point-to-point port-channel interfaces.
    # The port-channels using this are `p2p_links` defined under `l3_edge` or `core_interfaces`.
    # This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
    # The available template fields are:
    #   - `peer`: The name of the peer.
    #   - `interface`: The local interface name.
    #   - `peer_interface`: The interface on the peer.
    #   - `port_channel_id`: The local port-channel ID.
    #   - `peer_port_channel_id`: The ID of the port-channel on the peer.
    #
    # By default the description is templated from the name and interface of the peer.
    default_underlay_p2p_port_channel_description: <str; default="P2P_{peer}_{peer_interface}">

    # The default description or description template to be used on VRF diagnostic loopback interfaces.
    # This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
    # The available template fields are:
    #   - `interface`: The Loopback interface name.
    #   - `vrf`: The VRF name.
    #   - `tenant`: The tenant name.
    #
    # By default the description is templated from the VRF name.
    default_vrf_diag_loopback_description: <str; default="DIAG_VRF_{vrf}">

    # Enable Trunk Group support across eos_designs.
    # Warning: Because of the nature of the EOS Trunk Group feature, enabling this is "all or nothing".
    # *All* vlans and *all* trunks towards connected endpoints must be using trunk groups as well.
    # If trunk groups are not assigned to a trunk, no vlans will be enabled on that trunk.
    # See "Details on enable_trunk_groups" below before enabling this feature.
    enable_trunk_groups: <bool; default=False>

    # Description or description template to be used on the MLAG BGP peers including those in VRFs.
    # This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
    # The available template fields are:
    #   - `mlag_peer`: The name of the MLAG peer.
    #   - `interface`: The local MLAG L3 VLAN interface.
    #   - `peer_interface`: The MLAG L3 VLAN interface on the MLAG peer.
    #   - `vrf`: The name of the VRF. Not available for the underlay peering.
    #
    # The default description is built from the name and interface of the MLAG peer and optionally the VRF.
    mlag_bgp_peer_description: <str; default="{mlag_peer}_{peer_interface}">

    # Description or description template to be used on the MLAG BGP peer-group.
    # This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
    # The available template fields are:
    #   - `mlag_peer`: The name of the MLAG peer.
    #
    # The default description is the name of the MLAG peers.
    mlag_bgp_peer_group_description: <str; default="{mlag_peer}">

    # Description or description template to be used on MLAG peer-link ethernet interfaces.
    # This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
    # The available template fields are:
    #   - `mlag_peer`: The name of the MLAG peer.
    #   - `interface`: The local MLAG port-channel interface.
    #   - `peer_interface`: The port-channel interface on the MLAG peer.
    #   - `mlag_port_channel_id`: The local MLAG port-channel ID.
    #   - `mlag_peer_port_channel_id`: The port-channel ID on the MLAG peer.
    #
    # By default the description is templated from the name and interface of the MLAG peer.
    mlag_member_description: <str; default="MLAG_{mlag_peer}_{peer_interface}">

    # If `true` an MLAG ID will always be configured on a Port-Channel downlink even if the downlink is only on one node in the MLAG pair.
    # If `false` (default) an MLAG ID will only be configured on Port-Channel downlinks dual-homed to two MLAG switches.
    mlag_on_orphan_port_channel_downlink: <bool; default=False>

    # Description or description template to be used on MLAG L3 peering SVI (Interface Vlan4093 by default).
    # This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
    # The available template fields are:
    #   - `mlag_peer`: The name of the MLAG peer.
    #   - `interface`: The MLAG L3 peering SVI name.
    #   - `mlag_peer_l3_vlan`: The MLAG L3 peering VLAN ID.
    mlag_peer_l3_svi_description: <str; default="MLAG_L3">

    # Name or name template to be used on MLAG L3 VLAN (VLAN 4093 by default).
    # This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
    # The available template fields are:
    #   - `mlag_peer`: The name of the MLAG peer.
    #   - `mlag_peer_l3_vlan`: The MLAG L3 peering VLAN ID.
    mlag_peer_l3_vlan_name: <str; default="MLAG_L3">

    # Description or description template to be used on MLAG L3 peering SVI for VRFs.
    # This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
    # The available template fields are:
    #   - `mlag_peer`: The name of the MLAG peer.
    #   - `interface`: The MLAG L3 VRF peering SVI name.
    #   - `vlan`: The MLAG L3 VRF peering VLAN ID.
    #   - `vrf`: The VRF name.
    mlag_peer_l3_vrf_svi_description: <str; default="MLAG_L3_VRF_{vrf}">

    # Name or name template to be used on MLAG L3 peering VLAN for VRFs.
    # This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
    # The available template fields are:
    #   - `mlag_peer`: The name of the MLAG peer.
    #   - `vlan`: The MLAG L3 VRF peering VLAN ID.
    #   - `vrf`: The VRF name.
    mlag_peer_l3_vrf_vlan_name: <str; default="MLAG_L3_VRF_{vrf}">

    # Description or description template to be used on MLAG peering SVI (Interface Vlan4094 by default).
    # This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
    # The available template fields are:
    #   - `mlag_peer`: The name of the MLAG peer.
    #   - `interface`: The MLAG peering SVI name.
    #   - `mlag_peer_vlan`: The MLAG peering VLAN ID.
    mlag_peer_svi_description: <str; default="MLAG">

    # Name or name template to be used on MLAG peering VLAN (VLAN 4094 by default).
    # This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
    # The available template fields are:
    #   - `mlag_peer`: The name of the MLAG peer.
    #   - `mlag_peer_vlan`: The MLAG peering VLAN ID.
    mlag_peer_vlan_name: <str; default="MLAG">

    # Description or description template to be used on MLAG peer-link port-channel interfaces.
    # This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
    # The available template fields are:
    #   - `mlag_peer`: The name of the MLAG peer.
    #   - `interface`: The local MLAG port-channel interface.
    #   - `peer_interface`: The port-channel interface on the MLAG peer.
    #   - `mlag_port_channel_id`: The local MLAG port-channel ID.
    #   - `mlag_peer_port_channel_id`: The port-channel ID on the MLAG peer.
    #
    # By default the description is templated from the name and port-channel interface of the MLAG peer.
    mlag_port_channel_description: <str; default="MLAG_{mlag_peer}_{peer_interface}">

    # A vlan can have many trunk_groups assigned.
    # To avoid unneeded configuration changes on all leaf switches when a new trunk group is added,
    # this feature will only configure the vlan trunk groups matched with local connected_endpoints.
    # See "Details on only_local_vlan_trunk_groups" below.
    # Requires "enable_trunk_groups: true".
    only_local_vlan_trunk_groups: <bool; default=False>

    # Point to Point Links MTU.
    # Precedence: <node_type>.uplink_mtu -> platform_settings.p2p_uplinks_mtu -> p2p_uplinks_mtu -> 9214
    p2p_uplinks_mtu: <int; 68-65535; default=9214>

    # QOS Profile assigned on all infrastructure links.
    p2p_uplinks_qos_profile: <str>

    # When a device is set undeployed using `is_deployed: false` and `shutdown_bgp_towards_undeployed_peers` key is set to true, the BGP neighborship is shutdown on the peer.
    shutdown_bgp_towards_undeployed_peers: <bool; default=True>

    # - It is possible to provision configurations for a complete topology but flag devices as undeployed using the host level variable `is_deployed: false`.
    #
    # ```yaml
    # # Use at the host level
    # is_deployed: < true or false or default -> true >
    # ```
    #
    # - By default, this will have no impact within the `eos_designs` role. Configs will still be generated by the `eos_cli_config_gen` role and will still be pushed by the `eos_config_deploy_eapi` directly to devices if used.
    # - However, if the `eos_config_deploy_cvp` role is used to push configurations, CloudVision will ignore the devices flagged  as `is_deployed: false` and not attempt to configure them.
    # - If the device is not present in the network due to CloudVision not configuring the device, `eos_validate_state` role will fail tests on peers of the undeployed device trying to verify that interfaces are up.
    # - To overcome this and shutdown interfaces towards undeployed peers, the variable `shutdown_interfaces_towards_undeployed_peers` can be used, satisfying the `eos_validate_state` role interface tests.
    # - Again, this is only an issue if `eos_config_deploy_cvp` is used and the devices are not present in the network.
    shutdown_interfaces_towards_undeployed_peers: <bool; default=True>
    trunk_groups:

      # Trunk Group used for MLAG VLAN (Typically VLAN 4094).
      mlag:
        name: <str; default="MLAG">

      # Trunk Group used for MLAG L3 peering VLAN and for VRF L3 peering VLANs (Typically VLAN 4093).
      mlag_l3:
        name: <str; default="MLAG">

      # Trunk Group used on L2 Leaf switches when "enable_trunk_groups" is set.
      uplink:
        name: <str; default="UPLINK">

    # Configure route-map on eBGP sessions towards underlay peers, where prefixes with the peer's ASN in the AS Path are filtered away.
    # This is very useful in very large scale networks not using EVPN overlays, where convergence will be quicker by not having to return
    # all updates received from Spine-1 to Spine-2 just for Spine-2 to throw them away because of AS Path loop detection.
    # Note that this setting cannot be used while there are EVPN services present in the default VRF.
    underlay_filter_peer_as: <bool; default=False>

    # Filter redistribution of connected into the underlay routing protocol.
    # Only applicable when overlay_routing_protocol != 'none' and underlay_routing_protocol == BGP.
    # Creates a route-map and prefix-list assigned to redistribute connected permitting only loopbacks and inband management subnets.
    underlay_filter_redistribute_connected: <bool; default=True>

    # This feature allows IPv6 underlay routing protocol with RFC5549 addresses to be used along with IPv4 advertisements as VXLAN tunnel endpoints.
    # Requires "underlay_rfc5549: true" and "loopback_ipv6_pool" under the node type settings.
    underlay_ipv6: <bool; default=False>

    # The description or description template to be used on L2 ethernet interfaces.
    # The interfaces using this are the member interfaces of port-channel uplinks.
    # This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
    # The available template fields are:
    #   - `peer`: The name of the peer.
    #   - `interface`: The local interface name.
    #   - `peer_interface`: The interface on the peer.
    #
    # By default the description is templated from the hostname and interface of the peer.
    underlay_l2_ethernet_description: <str; default="L2_{peer}_{peer_interface}">

    # The description or description template to be used on L2 port-channel interfaces.
    # The interfaces using this are port-channel uplinks.
    # This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
    # The available template fields are:
    #   - `peer`: The name of the peer.
    #   - `interface`: The local interface name.
    #   - `peer_interface`: The interface on the peer.
    #   - `port_channel_id`: The local port-channel ID.
    #   - `peer_port_channel_id`: The ID of the port-channel on the peer.
    #   - `peer_node_group`: The node group of the peer if the peer is an MLAG member or running EVPN A/A.
    #   - `peer_node_group_or_peer`: Helper alias of the peer_node_group or peer.
    #   - `peer_node_group_or_uppercase_peer`: Helper alias of the peer_node_group or peer hostname in uppercase.
    #
    # By default the description is templated from the peer's node group (for MLAG or EVPN A/A) or hostname and port-channel interface of the peer.
    underlay_l2_port_channel_description: <str; default="L2_{peer_node_group_or_peer}_{peer_interface}">

    # Enable Multicast in the underlay on all p2p uplink interfaces and mlag l3 peer interface.
    # Specifically PIM Sparse-Mode will be configured on all routed underlay interfaces.
    # No other configuration is added, so the underlay will only support Source-Specific Multicast (SSM).
    # The configuration is intended to be used as multicast underlay for EVPN OISM overlay.
    underlay_multicast: <bool; default=False>

    # If multiple nodes are configured under 'underlay_multicast_rps.[].nodes' for the same RP address, they will be configured
    # with one of the following methods:
    # - Anycast RP using PIM (RFC4610).
    # - Anycast RP using MSDP (RFC4611).
    #
    # NOTE: When using MSDP, all nodes across all MSDP enabled RPs will be added to a single MSDP mesh group named "ANYCAST-RP".
    underlay_multicast_anycast_rp:
      mode: <str; "pim" | "msdp"; default="pim">

    # List of PIM Sparse-Mode Rendevouz Points configured for underlay multicast on all devices.
    # The device(s) listed under 'nodes', will be configured as the Rendevouz point router(s).
    # If multiple nodes are configured under 'nodes' for the same RP address, they will be configured
    # according to the 'underlay_multicast_anycast_rp.mode' setting.
    #
    # Requires 'underlay_multicast: true'.
    underlay_multicast_rps:

        # RP IPv4 address.
      - rp: <str; required; unique>

        # List of nodes where a Loopback interface with the RP address will be configured.
        nodes:

            # Hostname.
          - name: <str; required; unique>
            loopback_number: <int; required>

            # Interface description.
            description: <str; default="PIM RP">

        # List of groups to associate with the RP address set in 'rp'.
        # If access_list_name is set, a standard access-list will be configured matching these groups.
        # Otherwise the groups are configured directly on the RP command.
        groups:

            # Multicast Group IPv4 prefix/mask.
          - <str>

        # Name of standard Access-List.
        access_list_name: <str>

    # Point to Point Underlay with RFC 5549(eBGP), i.e. IPv6 Unnumbered.
    # Requires "underlay_routing_protocol: ebgp".
    underlay_rfc5549: <bool; default=False>

    # - The following underlay routing protocols are supported:
    #   - EBGP (default for l3ls-evpn)
    #   - OSPF.
    #   - OSPF-LDP*.
    #   - ISIS.
    #   - ISIS-SR*.
    #   - ISIS-LDP*.
    #   - ISIS-SR-LDP*.
    #   - No underlay routing protocol (none)
    # - The variables should be applied to all devices in the fabric.
    # *Only supported with core_interfaces data model.
    underlay_routing_protocol: <str; "ebgp" | "ospf" | "ospf-ldp" | "isis" | "isis-sr" | "isis-ldp" | "isis-sr-ldp" | "none">

    # Enable PTP on all infrastructure links.
    uplink_ptp:
      enable: <bool; default=False>

    # Use `router general` to set router ID for all routing protocols and VRFs.
    use_router_general_for_router_id: <bool; default=False>
    ```
