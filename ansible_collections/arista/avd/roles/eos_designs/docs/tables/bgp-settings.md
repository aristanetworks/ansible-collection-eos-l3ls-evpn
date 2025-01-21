<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bgp_as</samp>](## "bgp_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>" to use to configure overlay when "overlay_routing_protocol" == ibgp.<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number. |
    | [<samp>bgp_default_ipv4_unicast</samp>](## "bgp_default_ipv4_unicast") | Boolean |  | `False` |  | Default activation of IPv4 unicast address-family on all IPv4 neighbors.<br>It is best practice to disable activation.<br> |
    | [<samp>bgp_distance</samp>](## "bgp_distance") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;external_routes</samp>](## "bgp_distance.external_routes") | Integer | Required |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;internal_routes</samp>](## "bgp_distance.internal_routes") | Integer | Required |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;local_routes</samp>](## "bgp_distance.local_routes") | Integer | Required |  | Min: 1<br>Max: 255 |  |
    | [<samp>bgp_ecmp</samp>](## "bgp_ecmp") | Integer |  |  |  | Maximum ECMP for BGP multi-path.<br>The default value is 4 except for WAN Routers where the default value is unset (falls back to EOS default). |
    | [<samp>bgp_graceful_restart</samp>](## "bgp_graceful_restart") | Dictionary |  |  |  | BGP graceful-restart allows a BGP speaker with separate control plane and data plane processing to continue forwarding traffic during a BGP restart.<br>Its neighbors (receiving speakers) may retain routing information from the restarting speaker while a BGP session with it is being re-established, reducing route flapping.<br> |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "bgp_graceful_restart.enabled") | Boolean | Required | `False` |  | Enable or disable graceful-restart for all BGP peers. |
    | [<samp>&nbsp;&nbsp;restart_time</samp>](## "bgp_graceful_restart.restart_time") | Integer |  | `300` | Min: 1<br>Max: 3600 | Restart time in seconds. |
    | [<samp>bgp_maximum_paths</samp>](## "bgp_maximum_paths") | Integer |  |  | Min: 1<br>Max: 512 | Maximum Paths for BGP multi-path.<br>The default value is 4 except for WAN Routers where the default value is 16. |
    | [<samp>bgp_peer_groups</samp>](## "bgp_peer_groups") | Dictionary |  |  |  | Leverage an Arista EOS switch to generate the encrypted password using the correct peer group name.<br>Note that the name of the peer groups use '-' instead of '_' in EOS configuration.<br> |
    | [<samp>&nbsp;&nbsp;ipv4_underlay_peers</samp>](## "bgp_peer_groups.ipv4_underlay_peers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.ipv4_underlay_peers.name") | String |  | `IPv4-UNDERLAY-PEERS` |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.ipv4_underlay_peers.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "bgp_peer_groups.ipv4_underlay_peers.bfd") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.ipv4_underlay_peers.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;mlag_ipv4_underlay_peer</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer.name") | String |  | `MLAG-IPv4-UNDERLAY-PEER` |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer.bfd") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.mlag_ipv4_underlay_peer.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;evpn_overlay_peers</samp>](## "bgp_peer_groups.evpn_overlay_peers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.evpn_overlay_peers.name") | String |  | `EVPN-OVERLAY-PEERS` |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.evpn_overlay_peers.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "bgp_peer_groups.evpn_overlay_peers.bfd") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.evpn_overlay_peers.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;evpn_overlay_core</samp>](## "bgp_peer_groups.evpn_overlay_core") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.evpn_overlay_core.name") | String |  | `EVPN-OVERLAY-CORE` |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.evpn_overlay_core.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "bgp_peer_groups.evpn_overlay_core.bfd") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.evpn_overlay_core.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;mpls_overlay_peers</samp>](## "bgp_peer_groups.mpls_overlay_peers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.mpls_overlay_peers.name") | String |  | `MPLS-OVERLAY-PEERS` |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.mpls_overlay_peers.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "bgp_peer_groups.mpls_overlay_peers.bfd") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.mpls_overlay_peers.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;rr_overlay_peers</samp>](## "bgp_peer_groups.rr_overlay_peers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.rr_overlay_peers.name") | String |  | `RR-OVERLAY-PEERS` |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.rr_overlay_peers.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "bgp_peer_groups.rr_overlay_peers.bfd") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.rr_overlay_peers.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;ipvpn_gateway_peers</samp>](## "bgp_peer_groups.ipvpn_gateway_peers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.ipvpn_gateway_peers.name") | String |  | `IPVPN-GATEWAY-PEERS` |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.ipvpn_gateway_peers.password") | String |  |  |  | Type 7 encrypted password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "bgp_peer_groups.ipvpn_gateway_peers.bfd") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.ipvpn_gateway_peers.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;wan_overlay_peers</samp>](## "bgp_peer_groups.wan_overlay_peers") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.wan_overlay_peers.name") | String |  | `WAN-OVERLAY-PEERS` |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.wan_overlay_peers.password") | String |  |  |  | Type 7 encrypted password.<br>When configuring a password on the `wan_overlay_peers` BGP peer group,<br>it may also be required to set a password for the `wan_rr_overlay_peers` BGP peer group.<br>This is required in the case where one or more pathfinders use the same VTEP IP range as the edge routers.<br>If the password is not set, the static BGP peerings between Pathfinders may not come up. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "bgp_peer_groups.wan_overlay_peers.bfd") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd_timers</samp>](## "bgp_peer_groups.wan_overlay_peers.bfd_timers") | Dictionary |  |  |  | Specify the BFD timers to override the default values.<br>It is recommended to keep BFD total timeout longer than the DPS timeout.<br>The Default BFD timeout is 10 x 1 seconds and the default DPS timeout is 5 x 1 seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "bgp_peer_groups.wan_overlay_peers.bfd_timers.interval") | Integer | Required | `1000` | Min: 50<br>Max: 60000 | Interval in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp>](## "bgp_peer_groups.wan_overlay_peers.bfd_timers.min_rx") | Integer | Required | `1000` | Min: 50<br>Max: 60000 | Rate in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "bgp_peer_groups.wan_overlay_peers.bfd_timers.multiplier") | Integer | Required | `10` | Min: 3<br>Max: 50 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;listen_range_prefixes</samp>](## "bgp_peer_groups.wan_overlay_peers.listen_range_prefixes") | List, items: String |  |  |  | Only used for nodes where `wan_role` is `server` like AutoVPN RRs and Pathfinders.<br>For clients, AVD will raise an error if the Loopback0 IP is not in any listen range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "bgp_peer_groups.wan_overlay_peers.listen_range_prefixes.[]") | String |  |  |  | The prefixes to use in listen_range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ttl_maximum_hops</samp>](## "bgp_peer_groups.wan_overlay_peers.ttl_maximum_hops") | Integer |  | `1` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.wan_overlay_peers.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;wan_rr_overlay_peers</samp>](## "bgp_peer_groups.wan_rr_overlay_peers") | Dictionary |  |  |  | Configuration options for the peer-group created to peer between AutoVPN RRs or CV Pathfinders. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "bgp_peer_groups.wan_rr_overlay_peers.name") | String |  | `WAN-RR-OVERLAY-PEERS` |  | Name of peer group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "bgp_peer_groups.wan_rr_overlay_peers.password") | String |  |  |  | Type 7 encrypted password.<br>When configuring a password on the `wan_overlay_peers` BGP peer group,<br>it may also be required to set a password for the `wan_rr_overlay_peers` BGP peer group.<br>This is required in the case where one or more pathfinders use the same VTEP IP range as the edge routers.<br>If the password is not set, the static BGP peerings between Pathfinders may not come up. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "bgp_peer_groups.wan_rr_overlay_peers.bfd") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd_timers</samp>](## "bgp_peer_groups.wan_rr_overlay_peers.bfd_timers") | Dictionary |  |  |  | Specify the BFD timers to override the default values.<br>It is recommended to keep BFD total timeout longer than the DPS timeout.<br>The Default BFD timeout is 10 x 1 seconds and the default DPS timeout is 5 x 1 seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "bgp_peer_groups.wan_rr_overlay_peers.bfd_timers.interval") | Integer | Required | `1000` | Min: 50<br>Max: 60000 | Interval in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp>](## "bgp_peer_groups.wan_rr_overlay_peers.bfd_timers.min_rx") | Integer | Required | `1000` | Min: 50<br>Max: 60000 | Rate in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "bgp_peer_groups.wan_rr_overlay_peers.bfd_timers.multiplier") | Integer | Required | `10` | Min: 3<br>Max: 50 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ttl_maximum_hops</samp>](## "bgp_peer_groups.wan_rr_overlay_peers.ttl_maximum_hops") | Integer |  | `1` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "bgp_peer_groups.wan_rr_overlay_peers.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen. |
    | [<samp>bgp_update_wait_install</samp>](## "bgp_update_wait_install") | Boolean |  | `True` |  | Do not advertise reachability to a prefix until that prefix has been installed in hardware.<br>This will eliminate any temporary black holes due to a BGP speaker advertising reachability to a prefix that may not yet be installed into the forwarding plane.<br> |
    | [<samp>bgp_update_wait_for_convergence</samp>](## "bgp_update_wait_for_convergence") | Boolean |  | `False` |  | Disables FIB updates and route advertisement when the BGP instance is initiated until the BGP convergence state is reached.<br> |

=== "YAML"

    ```yaml
    # BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>" to use to configure overlay when "overlay_routing_protocol" == ibgp.
    # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
    bgp_as: <str>

    # Default activation of IPv4 unicast address-family on all IPv4 neighbors.
    # It is best practice to disable activation.
    bgp_default_ipv4_unicast: <bool; default=False>
    bgp_distance:
      external_routes: <int; 1-255; required>
      internal_routes: <int; 1-255; required>
      local_routes: <int; 1-255; required>

    # Maximum ECMP for BGP multi-path.
    # The default value is 4 except for WAN Routers where the default value is unset (falls back to EOS default).
    bgp_ecmp: <int>

    # BGP graceful-restart allows a BGP speaker with separate control plane and data plane processing to continue forwarding traffic during a BGP restart.
    # Its neighbors (receiving speakers) may retain routing information from the restarting speaker while a BGP session with it is being re-established, reducing route flapping.
    bgp_graceful_restart:

      # Enable or disable graceful-restart for all BGP peers.
      enabled: <bool; default=False; required>

      # Restart time in seconds.
      restart_time: <int; 1-3600; default=300>

    # Maximum Paths for BGP multi-path.
    # The default value is 4 except for WAN Routers where the default value is 16.
    bgp_maximum_paths: <int; 1-512>

    # Leverage an Arista EOS switch to generate the encrypted password using the correct peer group name.
    # Note that the name of the peer groups use '-' instead of '_' in EOS configuration.
    bgp_peer_groups:
      ipv4_underlay_peers:

        # Name of peer group.
        name: <str; default="IPv4-UNDERLAY-PEERS">

        # Type 7 encrypted password.
        password: <str>
        bfd: <bool; default=False>

        # Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen.
        structured_config: <dict>
      mlag_ipv4_underlay_peer:

        # Name of peer group.
        name: <str; default="MLAG-IPv4-UNDERLAY-PEER">

        # Type 7 encrypted password.
        password: <str>
        bfd: <bool; default=False>

        # Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen.
        structured_config: <dict>
      evpn_overlay_peers:

        # Name of peer group.
        name: <str; default="EVPN-OVERLAY-PEERS">

        # Type 7 encrypted password.
        password: <str>
        bfd: <bool; default=True>

        # Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen.
        structured_config: <dict>
      evpn_overlay_core:

        # Name of peer group.
        name: <str; default="EVPN-OVERLAY-CORE">

        # Type 7 encrypted password.
        password: <str>
        bfd: <bool; default=True>

        # Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen.
        structured_config: <dict>
      mpls_overlay_peers:

        # Name of peer group.
        name: <str; default="MPLS-OVERLAY-PEERS">

        # Type 7 encrypted password.
        password: <str>
        bfd: <bool; default=True>

        # Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen.
        structured_config: <dict>
      rr_overlay_peers:

        # Name of peer group.
        name: <str; default="RR-OVERLAY-PEERS">

        # Type 7 encrypted password.
        password: <str>
        bfd: <bool; default=True>

        # Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen.
        structured_config: <dict>
      ipvpn_gateway_peers:

        # Name of peer group.
        name: <str; default="IPVPN-GATEWAY-PEERS">

        # Type 7 encrypted password.
        password: <str>
        bfd: <bool; default=True>

        # Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen.
        structured_config: <dict>
      wan_overlay_peers:

        # Name of peer group.
        name: <str; default="WAN-OVERLAY-PEERS">

        # Type 7 encrypted password.
        # When configuring a password on the `wan_overlay_peers` BGP peer group,
        # it may also be required to set a password for the `wan_rr_overlay_peers` BGP peer group.
        # This is required in the case where one or more pathfinders use the same VTEP IP range as the edge routers.
        # If the password is not set, the static BGP peerings between Pathfinders may not come up.
        password: <str>
        bfd: <bool; default=True>

        # Specify the BFD timers to override the default values.
        # It is recommended to keep BFD total timeout longer than the DPS timeout.
        # The Default BFD timeout is 10 x 1 seconds and the default DPS timeout is 5 x 1 seconds.
        bfd_timers:

          # Interval in milliseconds.
          interval: <int; 50-60000; default=1000; required>

          # Rate in milliseconds.
          min_rx: <int; 50-60000; default=1000; required>
          multiplier: <int; 3-50; default=10; required>

        # Only used for nodes where `wan_role` is `server` like AutoVPN RRs and Pathfinders.
        # For clients, AVD will raise an error if the Loopback0 IP is not in any listen range.
        listen_range_prefixes:

            # The prefixes to use in listen_range.
          - <str>
        ttl_maximum_hops: <int; default=1>

        # Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen.
        structured_config: <dict>

      # Configuration options for the peer-group created to peer between AutoVPN RRs or CV Pathfinders.
      wan_rr_overlay_peers:

        # Name of peer group.
        name: <str; default="WAN-RR-OVERLAY-PEERS">

        # Type 7 encrypted password.
        # When configuring a password on the `wan_overlay_peers` BGP peer group,
        # it may also be required to set a password for the `wan_rr_overlay_peers` BGP peer group.
        # This is required in the case where one or more pathfinders use the same VTEP IP range as the edge routers.
        # If the password is not set, the static BGP peerings between Pathfinders may not come up.
        password: <str>
        bfd: <bool; default=True>

        # Specify the BFD timers to override the default values.
        # It is recommended to keep BFD total timeout longer than the DPS timeout.
        # The Default BFD timeout is 10 x 1 seconds and the default DPS timeout is 5 x 1 seconds.
        bfd_timers:

          # Interval in milliseconds.
          interval: <int; 50-60000; default=1000; required>

          # Rate in milliseconds.
          min_rx: <int; 50-60000; default=1000; required>
          multiplier: <int; 3-50; default=10; required>
        ttl_maximum_hops: <int; default=1>

        # Custom structured config added under router_bgp.peer_groups.[name=<name>] for eos_cli_config_gen.
        structured_config: <dict>

    # Do not advertise reachability to a prefix until that prefix has been installed in hardware.
    # This will eliminate any temporary black holes due to a BGP speaker advertising reachability to a prefix that may not yet be installed into the forwarding plane.
    bgp_update_wait_install: <bool; default=True>

    # Disables FIB updates and route advertisement when the BGP instance is initiated until the BGP convergence state is reached.
    bgp_update_wait_for_convergence: <bool; default=False>
    ```
