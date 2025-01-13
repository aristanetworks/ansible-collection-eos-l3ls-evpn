<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>tunnel_interfaces</samp>](## "tunnel_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "tunnel_interfaces.[].name") | String | Required, Unique |  |  | Tunnel Interface Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "tunnel_interfaces.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "tunnel_interfaces.[].shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "tunnel_interfaces.[].mtu") | Integer |  |  | Min: 68<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "tunnel_interfaces.[].vrf") | String |  |  |  | VRF Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;underlay_vrf</samp>](## "tunnel_interfaces.[].underlay_vrf") | String |  |  |  | Underlay VRF Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "tunnel_interfaces.[].ip_address") | String |  |  | Format: ipv4_cidr | IPv4_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_enable</samp>](## "tunnel_interfaces.[].ipv6_enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "tunnel_interfaces.[].ipv6_address") | String |  |  | Format: ipv6_cidr | IPv6_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_in</samp>](## "tunnel_interfaces.[].access_group_in") | String |  |  |  | IPv4 ACL Name for ingress. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_group_out</samp>](## "tunnel_interfaces.[].access_group_out") | String |  |  |  | IPv4 ACL Name for egress. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_in</samp>](## "tunnel_interfaces.[].ipv6_access_group_in") | String |  |  |  | IPv6 ACL Name for ingress. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group_out</samp>](## "tunnel_interfaces.[].ipv6_access_group_out") | String |  |  |  | IPv6 ACL Name for egress. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tcp_mss_ceiling</samp>](## "tunnel_interfaces.[].tcp_mss_ceiling") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "tunnel_interfaces.[].tcp_mss_ceiling.ipv4") | Integer |  |  | Min: 64<br>Max: 65495 | Segment Size for IPv4. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "tunnel_interfaces.[].tcp_mss_ceiling.ipv6") | Integer |  |  | Min: 64<br>Max: 65475 | Segment Size for IPv6. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "tunnel_interfaces.[].tcp_mss_ceiling.direction") | String |  |  | Valid Values:<br>- <code>ingress</code><br>- <code>egress</code> | Optional direction ('ingress', 'egress')  for tcp mss ceiling.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tunnel_mode</samp>](## "tunnel_interfaces.[].tunnel_mode") | String |  |  | Valid Values:<br>- <code>gre</code><br>- <code>ipsec</code> | Tunnel encapsulation method.<br>`gre`: Generic route encapsulation protocol,<br>`ipsec`: IPsec-over-IP encapsulation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "tunnel_interfaces.[].source_interface") | String |  |  |  | Tunnel Source Interface Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "tunnel_interfaces.[].destination") | String |  |  |  | IPv4 or IPv6 Address Tunnel Destination. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;path_mtu_discovery</samp>](## "tunnel_interfaces.[].path_mtu_discovery") | Boolean |  |  |  | Enable Path MTU Discovery On Tunnel. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipsec_profile</samp>](## "tunnel_interfaces.[].ipsec_profile") | String |  |  |  | Used only when `tunnel_mode` is set to `ipsec`.<br>It must target a defined IPsec profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;nat_profile</samp>](## "tunnel_interfaces.[].nat_profile") | String |  |  |  | NAT interface profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "tunnel_interfaces.[].eos_cli") | String |  |  |  | Multiline String with EOS CLI rendered directly on the Tunnel interface in the final EOS configuration.<br> |

=== "YAML"

    ```yaml
    tunnel_interfaces:

        # Tunnel Interface Name.
      - name: <str; required; unique>
        description: <str>
        shutdown: <bool>
        mtu: <int; 68-65535>

        # VRF Name.
        vrf: <str>

        # Underlay VRF Name.
        underlay_vrf: <str>

        # IPv4_address/Mask.
        ip_address: <str>
        ipv6_enable: <bool>

        # IPv6_address/Mask.
        ipv6_address: <str>

        # IPv4 ACL Name for ingress.
        access_group_in: <str>

        # IPv4 ACL Name for egress.
        access_group_out: <str>

        # IPv6 ACL Name for ingress.
        ipv6_access_group_in: <str>

        # IPv6 ACL Name for egress.
        ipv6_access_group_out: <str>
        tcp_mss_ceiling:

          # Segment Size for IPv4.
          ipv4: <int; 64-65495>

          # Segment Size for IPv6.
          ipv6: <int; 64-65475>

          # Optional direction ('ingress', 'egress')  for tcp mss ceiling.
          direction: <str; "ingress" | "egress">

        # Tunnel encapsulation method.
        # `gre`: Generic route encapsulation protocol,
        # `ipsec`: IPsec-over-IP encapsulation.
        tunnel_mode: <str; "gre" | "ipsec">

        # Tunnel Source Interface Name.
        source_interface: <str>

        # IPv4 or IPv6 Address Tunnel Destination.
        destination: <str>

        # Enable Path MTU Discovery On Tunnel.
        path_mtu_discovery: <bool>

        # Used only when `tunnel_mode` is set to `ipsec`.
        # It must target a defined IPsec profile.
        ipsec_profile: <str>

        # NAT interface profile.
        nat_profile: <str>

        # Multiline String with EOS CLI rendered directly on the Tunnel interface in the final EOS configuration.
        eos_cli: <str>
    ```
