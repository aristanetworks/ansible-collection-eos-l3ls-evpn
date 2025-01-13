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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_gateway</samp>](## "<node_type_keys.key>.defaults.ipvpn_gateway") | Dictionary |  |  |  | Node is acting as IP-VPN Gateway for EVPN to MPLS-IP-VPN Interworking. The BGP peer group used for this is "bgp_peer_groups.ipvpn_gateway_peers".<br>L3 Reachability is required for this to work, the preferred method to establish underlay connectivity is to use core_interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.defaults.ipvpn_gateway.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id</samp>](## "<node_type_keys.key>.defaults.ipvpn_gateway.evpn_domain_id") | String |  | `65535:1` |  | Domain ID to assign to EVPN address family for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_domain_id</samp>](## "<node_type_keys.key>.defaults.ipvpn_gateway.ipvpn_domain_id") | String |  | `65535:2` |  | Domain ID to assign to IPVPN address families for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_d_path</samp>](## "<node_type_keys.key>.defaults.ipvpn_gateway.enable_d_path") | Boolean |  | `True` |  | Enable D-path for use with BGP bestpath selection algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "<node_type_keys.key>.defaults.ipvpn_gateway.maximum_routes") | Integer |  | `0` |  | Maximum routes to accept from IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "<node_type_keys.key>.defaults.ipvpn_gateway.local_as") | String |  |  |  | Local BGP AS applied to peering with IPVPN remote peers.<br>BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_families</samp>](## "<node_type_keys.key>.defaults.ipvpn_gateway.address_families") | List, items: String |  | `['vpn-ipv4']` |  | IPVPN address families to enable for remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.defaults.ipvpn_gateway.address_families.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "<node_type_keys.key>.defaults.ipvpn_gateway.remote_peers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;hostname</samp>](## "<node_type_keys.key>.defaults.ipvpn_gateway.remote_peers.[].hostname") | String | Required, Unique |  |  | Hostname of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "<node_type_keys.key>.defaults.ipvpn_gateway.remote_peers.[].ip_address") | String | Required |  | Format: ipv4 | Peering IP of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "<node_type_keys.key>.defaults.ipvpn_gateway.remote_peers.[].bgp_as") | String | Required |  |  | Remote IPVPN Peer's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_gateway</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ipvpn_gateway") | Dictionary |  |  |  | Node is acting as IP-VPN Gateway for EVPN to MPLS-IP-VPN Interworking. The BGP peer group used for this is "bgp_peer_groups.ipvpn_gateway_peers".<br>L3 Reachability is required for this to work, the preferred method to establish underlay connectivity is to use core_interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ipvpn_gateway.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ipvpn_gateway.evpn_domain_id") | String |  | `65535:1` |  | Domain ID to assign to EVPN address family for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_domain_id</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ipvpn_gateway.ipvpn_domain_id") | String |  | `65535:2` |  | Domain ID to assign to IPVPN address families for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_d_path</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ipvpn_gateway.enable_d_path") | Boolean |  | `True` |  | Enable D-path for use with BGP bestpath selection algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ipvpn_gateway.maximum_routes") | Integer |  | `0` |  | Maximum routes to accept from IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ipvpn_gateway.local_as") | String |  |  |  | Local BGP AS applied to peering with IPVPN remote peers.<br>BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_families</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ipvpn_gateway.address_families") | List, items: String |  | `['vpn-ipv4']` |  | IPVPN address families to enable for remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ipvpn_gateway.address_families.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ipvpn_gateway.remote_peers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;hostname</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ipvpn_gateway.remote_peers.[].hostname") | String | Required, Unique |  |  | Hostname of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ipvpn_gateway.remote_peers.[].ip_address") | String | Required |  | Format: ipv4 | Peering IP of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ipvpn_gateway.remote_peers.[].bgp_as") | String | Required |  |  | Remote IPVPN Peer's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_gateway</samp>](## "<node_type_keys.key>.node_groups.[].ipvpn_gateway") | Dictionary |  |  |  | Node is acting as IP-VPN Gateway for EVPN to MPLS-IP-VPN Interworking. The BGP peer group used for this is "bgp_peer_groups.ipvpn_gateway_peers".<br>L3 Reachability is required for this to work, the preferred method to establish underlay connectivity is to use core_interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].ipvpn_gateway.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id</samp>](## "<node_type_keys.key>.node_groups.[].ipvpn_gateway.evpn_domain_id") | String |  | `65535:1` |  | Domain ID to assign to EVPN address family for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_domain_id</samp>](## "<node_type_keys.key>.node_groups.[].ipvpn_gateway.ipvpn_domain_id") | String |  | `65535:2` |  | Domain ID to assign to IPVPN address families for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_d_path</samp>](## "<node_type_keys.key>.node_groups.[].ipvpn_gateway.enable_d_path") | Boolean |  | `True` |  | Enable D-path for use with BGP bestpath selection algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "<node_type_keys.key>.node_groups.[].ipvpn_gateway.maximum_routes") | Integer |  | `0` |  | Maximum routes to accept from IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "<node_type_keys.key>.node_groups.[].ipvpn_gateway.local_as") | String |  |  |  | Local BGP AS applied to peering with IPVPN remote peers.<br>BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_families</samp>](## "<node_type_keys.key>.node_groups.[].ipvpn_gateway.address_families") | List, items: String |  | `['vpn-ipv4']` |  | IPVPN address families to enable for remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].ipvpn_gateway.address_families.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "<node_type_keys.key>.node_groups.[].ipvpn_gateway.remote_peers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;hostname</samp>](## "<node_type_keys.key>.node_groups.[].ipvpn_gateway.remote_peers.[].hostname") | String | Required, Unique |  |  | Hostname of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "<node_type_keys.key>.node_groups.[].ipvpn_gateway.remote_peers.[].ip_address") | String | Required |  | Format: ipv4 | Peering IP of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "<node_type_keys.key>.node_groups.[].ipvpn_gateway.remote_peers.[].bgp_as") | String | Required |  |  | Remote IPVPN Peer's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_gateway</samp>](## "<node_type_keys.key>.nodes.[].ipvpn_gateway") | Dictionary |  |  |  | Node is acting as IP-VPN Gateway for EVPN to MPLS-IP-VPN Interworking. The BGP peer group used for this is "bgp_peer_groups.ipvpn_gateway_peers".<br>L3 Reachability is required for this to work, the preferred method to establish underlay connectivity is to use core_interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.nodes.[].ipvpn_gateway.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_domain_id</samp>](## "<node_type_keys.key>.nodes.[].ipvpn_gateway.evpn_domain_id") | String |  | `65535:1` |  | Domain ID to assign to EVPN address family for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipvpn_domain_id</samp>](## "<node_type_keys.key>.nodes.[].ipvpn_gateway.ipvpn_domain_id") | String |  | `65535:2` |  | Domain ID to assign to IPVPN address families for use with D-path. Format <nn>:<nn>. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable_d_path</samp>](## "<node_type_keys.key>.nodes.[].ipvpn_gateway.enable_d_path") | Boolean |  | `True` |  | Enable D-path for use with BGP bestpath selection algorithm. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maximum_routes</samp>](## "<node_type_keys.key>.nodes.[].ipvpn_gateway.maximum_routes") | Integer |  | `0` |  | Maximum routes to accept from IPVPN remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_as</samp>](## "<node_type_keys.key>.nodes.[].ipvpn_gateway.local_as") | String |  |  |  | Local BGP AS applied to peering with IPVPN remote peers.<br>BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_families</samp>](## "<node_type_keys.key>.nodes.[].ipvpn_gateway.address_families") | List, items: String |  | `['vpn-ipv4']` |  | IPVPN address families to enable for remote peers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.nodes.[].ipvpn_gateway.address_families.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_peers</samp>](## "<node_type_keys.key>.nodes.[].ipvpn_gateway.remote_peers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;hostname</samp>](## "<node_type_keys.key>.nodes.[].ipvpn_gateway.remote_peers.[].hostname") | String | Required, Unique |  |  | Hostname of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "<node_type_keys.key>.nodes.[].ipvpn_gateway.remote_peers.[].ip_address") | String | Required |  | Format: ipv4 | Peering IP of remote IPVPN Peer. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "<node_type_keys.key>.nodes.[].ipvpn_gateway.remote_peers.[].bgp_as") | String | Required |  |  | Remote IPVPN Peer's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:

        # Node is acting as IP-VPN Gateway for EVPN to MPLS-IP-VPN Interworking. The BGP peer group used for this is "bgp_peer_groups.ipvpn_gateway_peers".
        # L3 Reachability is required for this to work, the preferred method to establish underlay connectivity is to use core_interfaces.
        ipvpn_gateway:
          enabled: <bool; required>

          # Domain ID to assign to EVPN address family for use with D-path. Format <nn>:<nn>.
          evpn_domain_id: <str; default="65535:1">

          # Domain ID to assign to IPVPN address families for use with D-path. Format <nn>:<nn>.
          ipvpn_domain_id: <str; default="65535:2">

          # Enable D-path for use with BGP bestpath selection algorithm.
          enable_d_path: <bool; default=True>

          # Maximum routes to accept from IPVPN remote peers.
          maximum_routes: <int; default=0>

          # Local BGP AS applied to peering with IPVPN remote peers.
          # BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
          # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
          local_as: <str>

          # IPVPN address families to enable for remote peers.
          address_families: # default=['vpn-ipv4']
            - <str>
          remote_peers:

              # Hostname of remote IPVPN Peer.
            - hostname: <str; required; unique>

              # Peering IP of remote IPVPN Peer.
              ip_address: <str; required>

              # Remote IPVPN Peer's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
              # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
              bgp_as: <str; required>

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>

              # Node is acting as IP-VPN Gateway for EVPN to MPLS-IP-VPN Interworking. The BGP peer group used for this is "bgp_peer_groups.ipvpn_gateway_peers".
              # L3 Reachability is required for this to work, the preferred method to establish underlay connectivity is to use core_interfaces.
              ipvpn_gateway:
                enabled: <bool; required>

                # Domain ID to assign to EVPN address family for use with D-path. Format <nn>:<nn>.
                evpn_domain_id: <str; default="65535:1">

                # Domain ID to assign to IPVPN address families for use with D-path. Format <nn>:<nn>.
                ipvpn_domain_id: <str; default="65535:2">

                # Enable D-path for use with BGP bestpath selection algorithm.
                enable_d_path: <bool; default=True>

                # Maximum routes to accept from IPVPN remote peers.
                maximum_routes: <int; default=0>

                # Local BGP AS applied to peering with IPVPN remote peers.
                # BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
                local_as: <str>

                # IPVPN address families to enable for remote peers.
                address_families: # default=['vpn-ipv4']
                  - <str>
                remote_peers:

                    # Hostname of remote IPVPN Peer.
                  - hostname: <str; required; unique>

                    # Peering IP of remote IPVPN Peer.
                    ip_address: <str; required>

                    # Remote IPVPN Peer's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                    # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
                    bgp_as: <str; required>

          # Node is acting as IP-VPN Gateway for EVPN to MPLS-IP-VPN Interworking. The BGP peer group used for this is "bgp_peer_groups.ipvpn_gateway_peers".
          # L3 Reachability is required for this to work, the preferred method to establish underlay connectivity is to use core_interfaces.
          ipvpn_gateway:
            enabled: <bool; required>

            # Domain ID to assign to EVPN address family for use with D-path. Format <nn>:<nn>.
            evpn_domain_id: <str; default="65535:1">

            # Domain ID to assign to IPVPN address families for use with D-path. Format <nn>:<nn>.
            ipvpn_domain_id: <str; default="65535:2">

            # Enable D-path for use with BGP bestpath selection algorithm.
            enable_d_path: <bool; default=True>

            # Maximum routes to accept from IPVPN remote peers.
            maximum_routes: <int; default=0>

            # Local BGP AS applied to peering with IPVPN remote peers.
            # BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
            # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
            local_as: <str>

            # IPVPN address families to enable for remote peers.
            address_families: # default=['vpn-ipv4']
              - <str>
            remote_peers:

                # Hostname of remote IPVPN Peer.
              - hostname: <str; required; unique>

                # Peering IP of remote IPVPN Peer.
                ip_address: <str; required>

                # Remote IPVPN Peer's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
                bgp_as: <str; required>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>

          # Node is acting as IP-VPN Gateway for EVPN to MPLS-IP-VPN Interworking. The BGP peer group used for this is "bgp_peer_groups.ipvpn_gateway_peers".
          # L3 Reachability is required for this to work, the preferred method to establish underlay connectivity is to use core_interfaces.
          ipvpn_gateway:
            enabled: <bool; required>

            # Domain ID to assign to EVPN address family for use with D-path. Format <nn>:<nn>.
            evpn_domain_id: <str; default="65535:1">

            # Domain ID to assign to IPVPN address families for use with D-path. Format <nn>:<nn>.
            ipvpn_domain_id: <str; default="65535:2">

            # Enable D-path for use with BGP bestpath selection algorithm.
            enable_d_path: <bool; default=True>

            # Maximum routes to accept from IPVPN remote peers.
            maximum_routes: <int; default=0>

            # Local BGP AS applied to peering with IPVPN remote peers.
            # BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
            # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
            local_as: <str>

            # IPVPN address families to enable for remote peers.
            address_families: # default=['vpn-ipv4']
              - <str>
            remote_peers:

                # Hostname of remote IPVPN Peer.
              - hostname: <str; required; unique>

                # Peering IP of remote IPVPN Peer.
                ip_address: <str; required>

                # Remote IPVPN Peer's BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
                # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
                bgp_as: <str; required>
    ```
