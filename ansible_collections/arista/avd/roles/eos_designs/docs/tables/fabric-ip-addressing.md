<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>fabric_ip_addressing</samp>](## "fabric_ip_addressing") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;mlag</samp>](## "fabric_ip_addressing.mlag") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "fabric_ip_addressing.mlag.algorithm") | String |  | `first_id` | Valid Values:<br>- <code>first_id</code><br>- <code>odd_id</code><br>- <code>same_subnet</code> | This variable defines the Multi-chassis Link Aggregation (MLAG) algorithm used.<br>Each MLAG link will have a /31¹ subnet with each subnet allocated from the relevant MLAG pool via a calculated offset.<br>The offset is calculated using one of the following algorithms:<br>  - first_id: `(mlag_primary_id - 1) * 2` where `mlag_primary_id` is the ID of the first node defined under the node_group.<br>    This allocation method will skip every other /31¹ subnet making it less space efficient than `odd_id`.<br>  - odd_id: `(odd_id - 1) / 2`. Requires the node_group to have a node with an odd ID and a node with an even ID.<br>  - same_subnet: the offset will always be zero.<br>    This allocation method will cause every MLAG link to be addressed with the same /31¹ subnet.<br>¹ The prefix length is configurable with a default of /31. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4_prefix_length</samp>](## "fabric_ip_addressing.mlag.ipv4_prefix_length") | Integer |  | `31` | Min: 1<br>Max: 31 | IPv4 prefix length used for MLAG peer-vlan and L3 point-to-point SVIs over the MLAG peer-link. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_prefix_length</samp>](## "fabric_ip_addressing.mlag.ipv6_prefix_length") | Integer |  | `64` | Min: 1<br>Max: 127 | IPv6 prefix length used for MLAG peer-vlan and L3 point-to-point SVIs over the MLAG peer-link. |
    | [<samp>&nbsp;&nbsp;p2p_uplinks</samp>](## "fabric_ip_addressing.p2p_uplinks") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4_prefix_length</samp>](## "fabric_ip_addressing.p2p_uplinks.ipv4_prefix_length") | Integer |  | `31` | Min: 1<br>Max: 31 | IPv4 prefix length used for L3 point-to-point uplinks. |
    | [<samp>&nbsp;&nbsp;wan_ha</samp>](## "fabric_ip_addressing.wan_ha") | Dictionary |  |  |  | Allow to manipulate the IP addressing scheme for WAN HA direct subnets. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4_prefix_length</samp>](## "fabric_ip_addressing.wan_ha.ipv4_prefix_length") | Integer |  | `31` | Min: 1<br>Max: 31 | IPv4 prefix length used for point-to-point interface for direct WAN HA link. |

=== "YAML"

    ```yaml
    fabric_ip_addressing:
      mlag:

        # This variable defines the Multi-chassis Link Aggregation (MLAG) algorithm used.
        # Each MLAG link will have a /31¹ subnet with each subnet allocated from the relevant MLAG pool via a calculated offset.
        # The offset is calculated using one of the following algorithms:
        #   - first_id: `(mlag_primary_id - 1) * 2` where `mlag_primary_id` is the ID of the first node defined under the node_group.
        #     This allocation method will skip every other /31¹ subnet making it less space efficient than `odd_id`.
        #   - odd_id: `(odd_id - 1) / 2`. Requires the node_group to have a node with an odd ID and a node with an even ID.
        #   - same_subnet: the offset will always be zero.
        #     This allocation method will cause every MLAG link to be addressed with the same /31¹ subnet.
        # ¹ The prefix length is configurable with a default of /31.
        algorithm: <str; "first_id" | "odd_id" | "same_subnet"; default="first_id">

        # IPv4 prefix length used for MLAG peer-vlan and L3 point-to-point SVIs over the MLAG peer-link.
        ipv4_prefix_length: <int; 1-31; default=31>

        # IPv6 prefix length used for MLAG peer-vlan and L3 point-to-point SVIs over the MLAG peer-link.
        ipv6_prefix_length: <int; 1-127; default=64>
      p2p_uplinks:

        # IPv4 prefix length used for L3 point-to-point uplinks.
        ipv4_prefix_length: <int; 1-31; default=31>

      # Allow to manipulate the IP addressing scheme for WAN HA direct subnets.
      wan_ha:

        # IPv4 prefix length used for point-to-point interface for direct WAN HA link.
        ipv4_prefix_length: <int; 1-31; default=31>
    ```
