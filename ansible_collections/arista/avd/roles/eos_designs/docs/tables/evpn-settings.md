<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_ebgp_gateway_inter_domain</samp>](## "evpn_ebgp_gateway_inter_domain") | Boolean |  |  |  |  |
    | [<samp>evpn_ebgp_gateway_multihop</samp>](## "evpn_ebgp_gateway_multihop") | Integer |  | `15` |  | Default of 15, considering a large value to avoid BGP reachability issues in very complex DCI networks.<br>Adapt the value for your specific topology.<br> |
    | [<samp>evpn_ebgp_multihop</samp>](## "evpn_ebgp_multihop") | Integer |  | `3` |  | Default of 3, the recommended value for a 3 stage spine and leaf topology.<br>Set to a higher value to allow for very large and complex topologies.<br> |
    | [<samp>evpn_hostflap_detection</samp>](## "evpn_hostflap_detection") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "evpn_hostflap_detection.enabled") | Boolean |  | `True` |  | If set to false it will disable EVPN host-flap detection. |
    | [<samp>&nbsp;&nbsp;threshold</samp>](## "evpn_hostflap_detection.threshold") | Integer |  | `5` |  | Minimum number of MAC moves that indicate a MAC duplication issue. |
    | [<samp>&nbsp;&nbsp;window</samp>](## "evpn_hostflap_detection.window") | Integer |  | `180` |  | Time (in seconds) to detect a MAC duplication issue. |
    | [<samp>&nbsp;&nbsp;expiry_timeout</samp>](## "evpn_hostflap_detection.expiry_timeout") | Integer |  |  |  | Time (in seconds) to purge a MAC duplication issue. |
    | [<samp>evpn_import_pruning</samp>](## "evpn_import_pruning") | Boolean |  | `False` |  | Enable VPN import pruning (Min. EOS 4.24.2F).<br>The Route Target extended communities carried by incoming VPN paths will be examined.<br>If none of those Route Targets have been configured for import, the path will be immediately discarded.<br> |
    | [<samp>evpn_multicast</samp>](## "evpn_multicast") | Boolean |  | `False` |  | General Configuration required for EVPN Multicast. "evpn_l2_multicast" or "evpn_l3_multicast" must also be configured under the Network Services (tenants).<br>Requires "underlay_multicast: true" and IGMP snooping enabled globally (default).<br>For MLAG devices Route Distinguisher must be unique since this feature will create multi-vtep configuration.<br>Warning !!! For Trident3 based platforms i.e 7050X3, 7300X3, 720XP.<br>  The Following default platform setting will be configured on 7050X3 and 7300X3: "platform trident forwarding-table partition flexible exact-match 16384 l2-shared 98304 l3-shared 131072"<br>  The Following default platform setting will be configured on 720XP: "flexible exact-match 16000 l2-shared 18000 l3-shared 22000"<br>  All forwarding agents will be restarted when this configuration is applied.<br>  You can tune the settings by overriding the default variable: "platform_settings[platforms].trident_forwarding_table_partition:"<br>  Please contact an Arista representative for help with determining the appropriate values for your environment.<br> |
    | [<samp>evpn_overlay_bgp_rtc</samp>](## "evpn_overlay_bgp_rtc") | Boolean |  | `False` |  | Enable Route Target Membership Constraint Address Family on EVPN overlay BGP peerings (Min. EOS 4.25.1F).<br>Requires use eBGP as overlay protocol.<br> |
    | [<samp>evpn_prevent_readvertise_to_server</samp>](## "evpn_prevent_readvertise_to_server") | Boolean |  | `False` |  | Configure route-map on eBGP sessions towards route-servers, where prefixes with the peer's ASN in the AS Path are filtered away.<br>This is very useful in large-scale networks, where convergence will be quicker by not returning all updates received<br>from Route-server-1 to Router-server-2 just for Route-server-2 to throw them away because of AS Path loop detection.<br> |
    | [<samp>evpn_short_esi_prefix</samp>](## "evpn_short_esi_prefix") | String |  | `0000:0000:` |  | Configure prefix for "short_esi" values. |
    | [<samp>evpn_vlan_aware_bundles</samp>](## "evpn_vlan_aware_bundles") | Boolean |  | `False` |  | Enable VLAN aware bundles for every EVPN MAC-VRF.<br>If set to `true` all SVIs in a VRF are configured in a vlan-aware-bundle using the VRF name as the bundle name. `l2vlans` are bundled in vlan-aware-bundles using the VLAN name as the bundle name.<br><br>The `evpn_vlan_bundle` option under `svis` and `l2vlans` takes precedence and overrides this behavior. Per svi/l2vlan `evpn_vlan_bundle` also works when this setting is disabled which allow mixing vlan-aware-bundles with regular MAC-VRFs. |
    | [<samp>fabric_evpn_encapsulation</samp>](## "fabric_evpn_encapsulation") | String |  |  | Valid Values:<br>- <code>vxlan</code><br>- <code>mpls</code> | Should be set to mpls for evpn-mpls scenario. This overrides the evpn_encapsulation setting under node_type_keys. |

=== "YAML"

    ```yaml
    evpn_ebgp_gateway_inter_domain: <bool>

    # Default of 15, considering a large value to avoid BGP reachability issues in very complex DCI networks.
    # Adapt the value for your specific topology.
    evpn_ebgp_gateway_multihop: <int; default=15>

    # Default of 3, the recommended value for a 3 stage spine and leaf topology.
    # Set to a higher value to allow for very large and complex topologies.
    evpn_ebgp_multihop: <int; default=3>
    evpn_hostflap_detection:

      # If set to false it will disable EVPN host-flap detection.
      enabled: <bool; default=True>

      # Minimum number of MAC moves that indicate a MAC duplication issue.
      threshold: <int; default=5>

      # Time (in seconds) to detect a MAC duplication issue.
      window: <int; default=180>

      # Time (in seconds) to purge a MAC duplication issue.
      expiry_timeout: <int>

    # Enable VPN import pruning (Min. EOS 4.24.2F).
    # The Route Target extended communities carried by incoming VPN paths will be examined.
    # If none of those Route Targets have been configured for import, the path will be immediately discarded.
    evpn_import_pruning: <bool; default=False>

    # General Configuration required for EVPN Multicast. "evpn_l2_multicast" or "evpn_l3_multicast" must also be configured under the Network Services (tenants).
    # Requires "underlay_multicast: true" and IGMP snooping enabled globally (default).
    # For MLAG devices Route Distinguisher must be unique since this feature will create multi-vtep configuration.
    # Warning !!! For Trident3 based platforms i.e 7050X3, 7300X3, 720XP.
    #   The Following default platform setting will be configured on 7050X3 and 7300X3: "platform trident forwarding-table partition flexible exact-match 16384 l2-shared 98304 l3-shared 131072"
    #   The Following default platform setting will be configured on 720XP: "flexible exact-match 16000 l2-shared 18000 l3-shared 22000"
    #   All forwarding agents will be restarted when this configuration is applied.
    #   You can tune the settings by overriding the default variable: "platform_settings[platforms].trident_forwarding_table_partition:"
    #   Please contact an Arista representative for help with determining the appropriate values for your environment.
    evpn_multicast: <bool; default=False>

    # Enable Route Target Membership Constraint Address Family on EVPN overlay BGP peerings (Min. EOS 4.25.1F).
    # Requires use eBGP as overlay protocol.
    evpn_overlay_bgp_rtc: <bool; default=False>

    # Configure route-map on eBGP sessions towards route-servers, where prefixes with the peer's ASN in the AS Path are filtered away.
    # This is very useful in large-scale networks, where convergence will be quicker by not returning all updates received
    # from Route-server-1 to Router-server-2 just for Route-server-2 to throw them away because of AS Path loop detection.
    evpn_prevent_readvertise_to_server: <bool; default=False>

    # Configure prefix for "short_esi" values.
    evpn_short_esi_prefix: <str; default="0000:0000:">

    # Enable VLAN aware bundles for every EVPN MAC-VRF.
    # If set to `true` all SVIs in a VRF are configured in a vlan-aware-bundle using the VRF name as the bundle name. `l2vlans` are bundled in vlan-aware-bundles using the VLAN name as the bundle name.
    #
    # The `evpn_vlan_bundle` option under `svis` and `l2vlans` takes precedence and overrides this behavior. Per svi/l2vlan `evpn_vlan_bundle` also works when this setting is disabled which allow mixing vlan-aware-bundles with regular MAC-VRFs.
    evpn_vlan_aware_bundles: <bool; default=False>

    # Should be set to mpls for evpn-mpls scenario. This overrides the evpn_encapsulation setting under node_type_keys.
    fabric_evpn_encapsulation: <str; "vxlan" | "mpls">
    ```
