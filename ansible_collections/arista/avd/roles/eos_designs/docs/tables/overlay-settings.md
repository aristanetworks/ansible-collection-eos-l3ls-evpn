<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bgp_mesh_pes</samp>](## "bgp_mesh_pes") | Boolean |  | `False` |  | Configure an iBGP full mesh between PEs, either because there is no RR used or other reasons.<br>Only supported in combination with MPLS overlay.<br> |
    | [<samp>overlay_bgp_peer_description</samp>](## "overlay_bgp_peer_description") | String |  | `{peer}{peer_interface?<_}` |  | Description or description template to be used on the overlay BGP peers.<br>This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.<br>The available template fields are:<br>  - `peer`: The name of the BGP peer.<br>  - `peer_interface`: The interface on the BGP peer if available.<br><br>The default description is built from the name and interface of the BGP peer. |
    | [<samp>overlay_cvx_servers</samp>](## "overlay_cvx_servers") | List, items: String |  |  |  | List of CVX vxlan overlay controllers.<br>Required if overlay_routing_protocol == CVX.<br>CVX servers (VMs) are peering using their management interface, so mgmt_ip must be set for all CVX servers.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "overlay_cvx_servers.[]") | String |  |  |  | 'inventory_hostname' of CVX server.<br> |
    | [<samp>overlay_her_flood_list_per_vni</samp>](## "overlay_her_flood_list_per_vni") | Boolean |  | `False` |  | When using Head-End Replication, configure flood-lists per VNI.<br>By default HER will be configured with a common flood-list containing all VTEPs.<br>This behavior can be changed to per-VNI flood-lists by setting `overlay_her_flood_list_per_vni: true`.<br>This will make `eos_designs` consider configured VLANs per VTEP, and only include the relevant VTEPs to each VNI's flood-list.<br> |
    | [<samp>overlay_her_flood_list_scope</samp>](## "overlay_her_flood_list_scope") | String |  | `fabric` | Valid Values:<br>- <code>fabric</code><br>- <code>dc</code> | When using Head-End Replication, set the scope of flood-lists to Fabric or DC.<br>By default all VTEPs in the Fabric (part of the inventory group referenced by "fabric_name") are added to the flood-lists.<br>This can be changed to all VTEPs in the DC (sharing the same "dc_name" value).<br>This is useful if Border Leaf switches are dividing the VXLAN overlay into separate domains.<br> |
    | [<samp>overlay_loopback_description</samp>](## "overlay_loopback_description") <span style="color:red">deprecated</span> | String |  |  |  | Customize the description on overlay interface Loopback0.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>router_id_loopback_description</samp> instead.</span> |
    | [<samp>overlay_mlag_rfc5549</samp>](## "overlay_mlag_rfc5549") | Boolean |  | `False` |  | IPv6 Unnumbered for MLAG iBGP connections.<br>Requires "underlay_rfc5549: true".<br> |
    | [<samp>overlay_rd_type</samp>](## "overlay_rd_type") | Dictionary |  |  |  | Configuration options for the Administrator subfield (first part of RD) and the Assigned Number subfield (second part of RD).<br><br>By default Route Distinguishers (RD) are set to:<br>- `<overlay_loopback>:<mac_vrf_id_base + vlan_id or mac_vrf_vni_base + vlan_id>` for VLANs and VLAN-Aware Bundles with L2 vlans.<br>- `<overlay_loopback>:<vlan_aware_bundle_number_base + vrf_id>` for VLAN-Aware Bundles with SVIs.<br>- `<overlay_loopback>:<vlan_aware_bundle_number_base + id>` for VLAN-Aware Bundles defined under 'evpn_vlan_bundles'.<br>- `<overlay_loopback>:<vrf_id>` for VRFs.<br><br>Note:<br>RD is a 48-bit value which is split into <16-bit>:<32-bit> or <32-bit>:<16-bit>.<br>When using loopback or 32-bit ASN/number the assigned number can only be a 16-bit number. This may be a problem with large VNIs.<br>For 16-bit ASN/number the assigned number can be a 32-bit number.<br> |
    | [<samp>&nbsp;&nbsp;admin_subfield</samp>](## "overlay_rd_type.admin_subfield") | String |  | `router_id` |  | The method for deriving RD Administrator subfield (first part of RD):<br>- 'router_id' means the IP address of Loopback0.<br>- 'vtep_loopback' means the IP address of the VTEP loopback interface.<br>- 'bgp_as' means the AS number of the device.<br>- 'switch_id' means the 'id' value of the device.<br>- Any <IPv4 Address> without mask.<br>- Integer between <0-65535>.<br>- Integer between <0-4294967295>.<br>- 'overlay_loopback_ip' means the IP address of Loopback0. (deprecated - use 'router_id' instead)<br> |
    | [<samp>&nbsp;&nbsp;admin_subfield_offset</samp>](## "overlay_rd_type.admin_subfield_offset") | Integer |  | `0` |  | Offset can only be used if admin_subfield is an integer between <0-4294967295> or 'switch_id'.<br>Total value of admin_subfield + admin_subfield_offset must be <= 4294967295.<br> |
    | [<samp>&nbsp;&nbsp;vrf_admin_subfield</samp>](## "overlay_rd_type.vrf_admin_subfield") | String |  |  |  | The method for deriving RD Administrator subfield (first part of RD) for VRF services:<br>- 'router_id' means the IP address of Loopback0.<br>- 'vtep_loopback' means the IP address of the VTEP loopback interface.<br>- 'bgp_as' means the AS number of the device.<br>- 'switch_id' means the 'id' value of the device.<br>- Any <IPv4 Address> without mask.<br>- Integer between <0-65535>.<br>- Integer between <0-4294967295>.<br>- 'overlay_loopback_ip' means the IP address of Loopback0. (deprecated - use 'router_id' instead)<br><br>'vrf_admin_subfield' takes precedence for VRF RDs if set. Otherwise the 'admin_subfield' value will be used.<br> |
    | [<samp>&nbsp;&nbsp;vrf_admin_subfield_offset</samp>](## "overlay_rd_type.vrf_admin_subfield_offset") | Integer |  |  |  | Offset can only be used if 'vrf_admin_subfield' is an integer between <0-4294967295> or 'switch_id'.<br>Total value of 'vrf_admin_subfield' + 'vrf_admin_subfield_offset' must be <= 4294967295.<br><br>'vrf_admin_subfield_offset' takes precedence for VRF RDs if set. Otherwise the 'admin_subfield_offset' value will be used.<br> |
    | [<samp>&nbsp;&nbsp;vlan_assigned_number_subfield</samp>](## "overlay_rd_type.vlan_assigned_number_subfield") | String |  | `mac_vrf_id` | Valid Values:<br>- <code>mac_vrf_id</code><br>- <code>mac_vrf_vni</code><br>- <code>vlan_id</code> | The method for deriving RD Assigned Number subfield for VLAN services (second part of RD):<br>- 'mac_vrf_id' means `(mac_vrf_id_base or mac_vrf_vni_base) + vlan_id`.<br>- 'mac_vrf_vni' means `(mac_vrf_vni_base or mac_vrf_id_base) + vlan_id`.<br>- 'vlan_id' will only use the 'vlan_id' and ignores all base values.<br><br>These methods can be overridden per VLAN if either 'rd_override', 'rt_override' or 'vni_override' is set (preferred in this order).<br> |
    | [<samp>overlay_routing_protocol</samp>](## "overlay_routing_protocol") | String |  |  | Value is converted to lower case.<br>Valid Values:<br>- <code>ebgp</code><br>- <code>ibgp</code><br>- <code>cvx</code><br>- <code>her</code><br>- <code>none</code> | - The following overlay routing protocols are supported:<br>  - ebgp: Configures fabric with eBGP, default for l3ls-evpn design.<br>  - ibgp: Configured fabric with iBGP, only supported with OSPF or ISIS variants in underlay, default for mpls design.<br>  - cvx: Configures fabric to leverage CloudVision eXchange as the overlay controller.<br>  - her: Configures fabric with Head-End Replication, configures static VXLAN flood-lists instead of using a dynamic overlay protocol.<br>  - none: No overlay configuration will be generated, default for l2ls design.<br><br>  If not set, the default_overlay_routing_protocol defined under the node_type_keys will be used (default is "ebgp").<br> |
    | [<samp>overlay_routing_protocol_address_family</samp>](## "overlay_routing_protocol_address_family") | String |  | `ipv4` | Valid Values:<br>- <code>ipv4</code><br>- <code>ipv6</code> | When set to `ipv6`, enable overlay EVPN peering with IPv6 addresses.<br>This feature depends on underlay_ipv6 variable. As of today, only RFC5549 is capable to transport IPv6 in the underlay.<br> |
    | [<samp>overlay_rt_type</samp>](## "overlay_rt_type") | Dictionary |  |  |  | Configuration options for the Administrator subfield (first part of RT) and the Assigned Number subfield (second part of RT).<br><br>By default Route Targets (RT) are set to:<br>- `<(mac_vrf_id_base or mac_vrf_vni_base) + vlan_id>:<(mac_vrf_id_base or mac_vrf_vni_base) + vlan_id>` for VLANs and VLAN-Aware Bundles with L2 vlans.<br>- `<vlan_aware_bundle_number_base + vrf_id>:<vlan_aware_bundle_number_base + vrf_id>` for VLAN-Aware Bundles with SVIs.<br>- `<vlan_aware_bundle_number_base + id>:<vlan_aware_bundle_number_base + id>` for VLAN-Aware Bundles defined under 'evpn_vlan_bundles'.<br>- `<vrf_id>:<vrf_id>` for VRFs.<br><br>Notes:<br>RT is a 48-bit value which is split into <16-bit>:<32-bit> or <32-bit>:<16-bit>.<br>When using 32-bit ASN/number the VNI can only be a 16-bit number. Alternatively use vlan_id/vrf_id as assigned number.<br>For 16-bit ASN/number the assigned number can be a 32-bit number.<br> |
    | [<samp>&nbsp;&nbsp;admin_subfield</samp>](## "overlay_rt_type.admin_subfield") | String |  | `vrf_id` |  | The method for deriving RT Administrator subfield (first part of RT):<br>- 'vrf_id' means `(mac_vrf_id_base or mac_vrf_vni_base) + vlan_id` for VLANs, `(vrf_id or vrf_vni)` for VRFs and `id` for bundles defined under 'evpn_vlan_bundles'.<br>- 'vrf_vni' means `(mac_vrf_vni_base or mac_vrf_id_base) + vlan_id` for VLANs, `(vrf_vni or vrf_id)` for VRFs and `id` for bundles defined under 'evpn_vlan_bundles'.<br>- 'id' means `vlan_id` for VLANs, `(vrf_id or vrf_vni)` for VRFs and `id` for bundles defined under 'evpn_vlan_bundles'.<br>- 'bgp_as' means the AS number of the device.<br>- Integer between <0-65535>.<br>- Integer between <0-4294967295>.<br><br>The 'vrf_id' and 'vrf_vni' methods can be overridden per VLAN if either 'rt_override' or 'vni_override' is set (preferred in this order).<br>The 'vrf_id', 'vrf_vni' and 'id' methods can be overridden per bundle defined under `evpn_vlan_bundles` using 'rt_override'.<br> |
    | [<samp>&nbsp;&nbsp;vrf_admin_subfield</samp>](## "overlay_rt_type.vrf_admin_subfield") | String |  |  |  | The method for deriving RT Administrator subfield (first part of RT) for VRF services:<br>- 'id' means `(vrf_id or vrf_vni)`.<br>- 'vrf_id' means `(vrf_id or vrf_vni)`.<br>- 'vrf_vni' means `(vrf_vni or vrf_id)`.<br>- 'bgp_as' means the AS number of the device.<br>- Integer between <0-65535>.<br>- Integer between <0-4294967295>.<br><br>'vrf_admin_subfield' takes precedence for VRF RDs if set. Otherwise the 'admin_subfield' value will be used.<br> |
    | [<samp>&nbsp;&nbsp;vlan_assigned_number_subfield</samp>](## "overlay_rt_type.vlan_assigned_number_subfield") | String |  | `mac_vrf_id` | Valid Values:<br>- <code>mac_vrf_id</code><br>- <code>mac_vrf_vni</code><br>- <code>vlan_id</code> | The method for deriving RT Assigned Number subfield for VLAN services (second part of RT):<br>- 'mac_vrf_id' means `(mac_vrf_id_base or mac_vrf_vni_base) + vlan_id`.<br>- 'mac_vrf_vni' means `(mac_vrf_vni_base or mac_vrf_id_base) + vlan_id`.<br>- 'vlan_id' will only use the 'vlan_id' and ignores all base values.<br><br>These methods can be overridden per VLAN if either 'rt_override' or 'vni_override' is set (preferred in this order).<br> |
    | [<samp>router_id_loopback_description</samp>](## "router_id_loopback_description") | String |  | `ROUTER_ID` |  | Customize the description on Router ID interface Loopback0. |
    | [<samp>vtep_loopback_description</samp>](## "vtep_loopback_description") | String |  | `VXLAN_TUNNEL_SOURCE` |  | Customize the description on the VTEP interface, typically Loopback1. |
    | [<samp>vtep_vvtep_ip</samp>](## "vtep_vvtep_ip") | String |  |  |  | IP Address used as Virtual VTEP. Will be configured as secondary IP on Loopback1.<br>This is only needed for centralized routing designs.<br> |

=== "YAML"

    ```yaml
    # Configure an iBGP full mesh between PEs, either because there is no RR used or other reasons.
    # Only supported in combination with MPLS overlay.
    bgp_mesh_pes: <bool; default=False>

    # Description or description template to be used on the overlay BGP peers.
    # This can be a template using the AVD string formatter syntax: https://avd.arista.com/devel/roles/eos_designs/docs/how-to/custom-descriptions-names.html#avd-string-formatter-syntax.
    # The available template fields are:
    #   - `peer`: The name of the BGP peer.
    #   - `peer_interface`: The interface on the BGP peer if available.
    #
    # The default description is built from the name and interface of the BGP peer.
    overlay_bgp_peer_description: <str; default="{peer}{peer_interface?<_}">

    # List of CVX vxlan overlay controllers.
    # Required if overlay_routing_protocol == CVX.
    # CVX servers (VMs) are peering using their management interface, so mgmt_ip must be set for all CVX servers.
    overlay_cvx_servers:

        # 'inventory_hostname' of CVX server.
      - <str>

    # When using Head-End Replication, configure flood-lists per VNI.
    # By default HER will be configured with a common flood-list containing all VTEPs.
    # This behavior can be changed to per-VNI flood-lists by setting `overlay_her_flood_list_per_vni: true`.
    # This will make `eos_designs` consider configured VLANs per VTEP, and only include the relevant VTEPs to each VNI's flood-list.
    overlay_her_flood_list_per_vni: <bool; default=False>

    # When using Head-End Replication, set the scope of flood-lists to Fabric or DC.
    # By default all VTEPs in the Fabric (part of the inventory group referenced by "fabric_name") are added to the flood-lists.
    # This can be changed to all VTEPs in the DC (sharing the same "dc_name" value).
    # This is useful if Border Leaf switches are dividing the VXLAN overlay into separate domains.
    overlay_her_flood_list_scope: <str; "fabric" | "dc"; default="fabric">

    # Customize the description on overlay interface Loopback0.
    # This key is deprecated.
    # Support will be removed in AVD version 6.0.0.
    # Use <samp>router_id_loopback_description</samp> instead.
    overlay_loopback_description: <str>

    # IPv6 Unnumbered for MLAG iBGP connections.
    # Requires "underlay_rfc5549: true".
    overlay_mlag_rfc5549: <bool; default=False>

    # Configuration options for the Administrator subfield (first part of RD) and the Assigned Number subfield (second part of RD).
    #
    # By default Route Distinguishers (RD) are set to:
    # - `<overlay_loopback>:<mac_vrf_id_base + vlan_id or mac_vrf_vni_base + vlan_id>` for VLANs and VLAN-Aware Bundles with L2 vlans.
    # - `<overlay_loopback>:<vlan_aware_bundle_number_base + vrf_id>` for VLAN-Aware Bundles with SVIs.
    # - `<overlay_loopback>:<vlan_aware_bundle_number_base + id>` for VLAN-Aware Bundles defined under 'evpn_vlan_bundles'.
    # - `<overlay_loopback>:<vrf_id>` for VRFs.
    #
    # Note:
    # RD is a 48-bit value which is split into <16-bit>:<32-bit> or <32-bit>:<16-bit>.
    # When using loopback or 32-bit ASN/number the assigned number can only be a 16-bit number. This may be a problem with large VNIs.
    # For 16-bit ASN/number the assigned number can be a 32-bit number.
    overlay_rd_type:

      # The method for deriving RD Administrator subfield (first part of RD):
      # - 'router_id' means the IP address of Loopback0.
      # - 'vtep_loopback' means the IP address of the VTEP loopback interface.
      # - 'bgp_as' means the AS number of the device.
      # - 'switch_id' means the 'id' value of the device.
      # - Any <IPv4 Address> without mask.
      # - Integer between <0-65535>.
      # - Integer between <0-4294967295>.
      # - 'overlay_loopback_ip' means the IP address of Loopback0. (deprecated - use 'router_id' instead)
      admin_subfield: <str; default="router_id">

      # Offset can only be used if admin_subfield is an integer between <0-4294967295> or 'switch_id'.
      # Total value of admin_subfield + admin_subfield_offset must be <= 4294967295.
      admin_subfield_offset: <int; default=0>

      # The method for deriving RD Administrator subfield (first part of RD) for VRF services:
      # - 'router_id' means the IP address of Loopback0.
      # - 'vtep_loopback' means the IP address of the VTEP loopback interface.
      # - 'bgp_as' means the AS number of the device.
      # - 'switch_id' means the 'id' value of the device.
      # - Any <IPv4 Address> without mask.
      # - Integer between <0-65535>.
      # - Integer between <0-4294967295>.
      # - 'overlay_loopback_ip' means the IP address of Loopback0. (deprecated - use 'router_id' instead)
      #
      # 'vrf_admin_subfield' takes precedence for VRF RDs if set. Otherwise the 'admin_subfield' value will be used.
      vrf_admin_subfield: <str>

      # Offset can only be used if 'vrf_admin_subfield' is an integer between <0-4294967295> or 'switch_id'.
      # Total value of 'vrf_admin_subfield' + 'vrf_admin_subfield_offset' must be <= 4294967295.
      #
      # 'vrf_admin_subfield_offset' takes precedence for VRF RDs if set. Otherwise the 'admin_subfield_offset' value will be used.
      vrf_admin_subfield_offset: <int>

      # The method for deriving RD Assigned Number subfield for VLAN services (second part of RD):
      # - 'mac_vrf_id' means `(mac_vrf_id_base or mac_vrf_vni_base) + vlan_id`.
      # - 'mac_vrf_vni' means `(mac_vrf_vni_base or mac_vrf_id_base) + vlan_id`.
      # - 'vlan_id' will only use the 'vlan_id' and ignores all base values.
      #
      # These methods can be overridden per VLAN if either 'rd_override', 'rt_override' or 'vni_override' is set (preferred in this order).
      vlan_assigned_number_subfield: <str; "mac_vrf_id" | "mac_vrf_vni" | "vlan_id"; default="mac_vrf_id">

    # - The following overlay routing protocols are supported:
    #   - ebgp: Configures fabric with eBGP, default for l3ls-evpn design.
    #   - ibgp: Configured fabric with iBGP, only supported with OSPF or ISIS variants in underlay, default for mpls design.
    #   - cvx: Configures fabric to leverage CloudVision eXchange as the overlay controller.
    #   - her: Configures fabric with Head-End Replication, configures static VXLAN flood-lists instead of using a dynamic overlay protocol.
    #   - none: No overlay configuration will be generated, default for l2ls design.
    #
    #   If not set, the default_overlay_routing_protocol defined under the node_type_keys will be used (default is "ebgp").
    overlay_routing_protocol: <str; "ebgp" | "ibgp" | "cvx" | "her" | "none">

    # When set to `ipv6`, enable overlay EVPN peering with IPv6 addresses.
    # This feature depends on underlay_ipv6 variable. As of today, only RFC5549 is capable to transport IPv6 in the underlay.
    overlay_routing_protocol_address_family: <str; "ipv4" | "ipv6"; default="ipv4">

    # Configuration options for the Administrator subfield (first part of RT) and the Assigned Number subfield (second part of RT).
    #
    # By default Route Targets (RT) are set to:
    # - `<(mac_vrf_id_base or mac_vrf_vni_base) + vlan_id>:<(mac_vrf_id_base or mac_vrf_vni_base) + vlan_id>` for VLANs and VLAN-Aware Bundles with L2 vlans.
    # - `<vlan_aware_bundle_number_base + vrf_id>:<vlan_aware_bundle_number_base + vrf_id>` for VLAN-Aware Bundles with SVIs.
    # - `<vlan_aware_bundle_number_base + id>:<vlan_aware_bundle_number_base + id>` for VLAN-Aware Bundles defined under 'evpn_vlan_bundles'.
    # - `<vrf_id>:<vrf_id>` for VRFs.
    #
    # Notes:
    # RT is a 48-bit value which is split into <16-bit>:<32-bit> or <32-bit>:<16-bit>.
    # When using 32-bit ASN/number the VNI can only be a 16-bit number. Alternatively use vlan_id/vrf_id as assigned number.
    # For 16-bit ASN/number the assigned number can be a 32-bit number.
    overlay_rt_type:

      # The method for deriving RT Administrator subfield (first part of RT):
      # - 'vrf_id' means `(mac_vrf_id_base or mac_vrf_vni_base) + vlan_id` for VLANs, `(vrf_id or vrf_vni)` for VRFs and `id` for bundles defined under 'evpn_vlan_bundles'.
      # - 'vrf_vni' means `(mac_vrf_vni_base or mac_vrf_id_base) + vlan_id` for VLANs, `(vrf_vni or vrf_id)` for VRFs and `id` for bundles defined under 'evpn_vlan_bundles'.
      # - 'id' means `vlan_id` for VLANs, `(vrf_id or vrf_vni)` for VRFs and `id` for bundles defined under 'evpn_vlan_bundles'.
      # - 'bgp_as' means the AS number of the device.
      # - Integer between <0-65535>.
      # - Integer between <0-4294967295>.
      #
      # The 'vrf_id' and 'vrf_vni' methods can be overridden per VLAN if either 'rt_override' or 'vni_override' is set (preferred in this order).
      # The 'vrf_id', 'vrf_vni' and 'id' methods can be overridden per bundle defined under `evpn_vlan_bundles` using 'rt_override'.
      admin_subfield: <str; default="vrf_id">

      # The method for deriving RT Administrator subfield (first part of RT) for VRF services:
      # - 'id' means `(vrf_id or vrf_vni)`.
      # - 'vrf_id' means `(vrf_id or vrf_vni)`.
      # - 'vrf_vni' means `(vrf_vni or vrf_id)`.
      # - 'bgp_as' means the AS number of the device.
      # - Integer between <0-65535>.
      # - Integer between <0-4294967295>.
      #
      # 'vrf_admin_subfield' takes precedence for VRF RDs if set. Otherwise the 'admin_subfield' value will be used.
      vrf_admin_subfield: <str>

      # The method for deriving RT Assigned Number subfield for VLAN services (second part of RT):
      # - 'mac_vrf_id' means `(mac_vrf_id_base or mac_vrf_vni_base) + vlan_id`.
      # - 'mac_vrf_vni' means `(mac_vrf_vni_base or mac_vrf_id_base) + vlan_id`.
      # - 'vlan_id' will only use the 'vlan_id' and ignores all base values.
      #
      # These methods can be overridden per VLAN if either 'rt_override' or 'vni_override' is set (preferred in this order).
      vlan_assigned_number_subfield: <str; "mac_vrf_id" | "mac_vrf_vni" | "vlan_id"; default="mac_vrf_id">

    # Customize the description on Router ID interface Loopback0.
    router_id_loopback_description: <str; default="ROUTER_ID">

    # Customize the description on the VTEP interface, typically Loopback1.
    vtep_loopback_description: <str; default="VXLAN_TUNNEL_SOURCE">

    # IP Address used as Virtual VTEP. Will be configured as secondary IP on Loopback1.
    # This is only needed for centralized routing designs.
    vtep_vvtep_ip: <str>
    ```
