<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_l2_vpn</samp>](## "router_l2_vpn") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;arp_learning_bridged</samp>](## "router_l2_vpn.arp_learning_bridged") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;arp_proxy</samp>](## "router_l2_vpn.arp_proxy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp>](## "router_l2_vpn.arp_proxy.prefix_list") | String |  |  |  | Prefix-list name. ARP Proxying is disabled for IPv4 addresses defined in the prefix-list. |
    | [<samp>&nbsp;&nbsp;arp_selective_install</samp>](## "router_l2_vpn.arp_selective_install") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;nd_learning_bridged</samp>](## "router_l2_vpn.nd_learning_bridged") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;nd_proxy</samp>](## "router_l2_vpn.nd_proxy") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp>](## "router_l2_vpn.nd_proxy.prefix_list") | String |  |  |  | Prefix-list name. Neighbor Discovery Proxying is disabled for IPv6 addresses defined in the prefix-list. |
    | [<samp>&nbsp;&nbsp;nd_rs_flooding_disabled</samp>](## "router_l2_vpn.nd_rs_flooding_disabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;virtual_router_nd_ra_flooding_disabled</samp>](## "router_l2_vpn.virtual_router_nd_ra_flooding_disabled") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    router_l2_vpn:
      arp_learning_bridged: <bool>
      arp_proxy:

        # Prefix-list name. ARP Proxying is disabled for IPv4 addresses defined in the prefix-list.
        prefix_list: <str>
      arp_selective_install: <bool>
      nd_learning_bridged: <bool>
      nd_proxy:

        # Prefix-list name. Neighbor Discovery Proxying is disabled for IPv6 addresses defined in the prefix-list.
        prefix_list: <str>
      nd_rs_flooding_disabled: <bool>
      virtual_router_nd_ra_flooding_disabled: <bool>
    ```
