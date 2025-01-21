---
# This title is used for search results
title: Custom descriptions and names
---
<!--
  ~ Copyright (c) 2023-2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Custom descriptions and names

The `eos_designs` role provides the capability to customize various field descriptions and names leveraging the following methods:

- [AVD string formatter syntax](#avd-string-formatter-syntax) (Recommended).
- [Node type customization](../input-variables.md#node-type-customization) with custom Jinja2 template or Python class.

## AVD string formatter syntax

The AVD string formatter is based on Python's [custom string formatter class](https://docs.python.org/3/library/string.html#custom-string-formatting) syntax.
It provides extra protection from malicious format strings and adds support for prefixes and suffixes per field.

The following syntax is supported: `"{" [field_name] ["?"] ["<" prefix] [">" suffix] ["!" conversion] [":" format_spec] "}"`:

- `[field_name]`: Template field or variable, as per `eos_designs` input variables documentation.
- `["?"]`: The literal `?` signals that the field is optional and will not be printed if the value is missing or None.
- `["<" prefix]`: Prefix string including spaces which will be inserted before the field value. Most useful in combination with `?`. Prefix should not contain `"<"`, `">"`, `"!"` or `":"`.
- `[">" suffix]`: The suffix string including spaces which will be inserted after the field value. Most useful in combination with `?`. The suffix should not contain `"<"`, `">"`, `"!"` or `":"`.
- `["!" conversion]`: Convert string to supported methods. Note the regular Python conversions "!r", "!s", "!a" have been removed.
  - `"!u"`: convert all characters to upper case. Symbols and numbers are ignored.
- `[":" format_spec]`: Format specifications are used within replacement fields contained within a format string to define how individual values are presented. Please consult [Format Specification Mini-Language](https://docs.python.org/3/library/string.html#grammar-token-format-spec-format_spec) for usage details.

Example:

Given the following syntax: `"{endpoint_type!u}_{endpoint}{endpoint_port_channel?<_}"`

**Server with port-channel:**

Template fields:

- endpoint_type: servers
- endpoint: server1
- endpoint_port_channel: Po1

results in: `SERVERS_server1_Po1`

**Server without port-channel:**

Template fields:

- endpoint_type: servers
- endpoint: server2
- endpoint_port_channel: none

results in: `SERVERS_server2`

## Default description or name values

Below is a complete list of input variables and default values to facilitate customizing the description and names of values.
Please consult the `eos_designs` input variables documentation to obtain the available template field(s) (`[field_name]`).

```yaml
# Loopback interfaces description
router_id_loopback_description: "ROUTER_ID"
vtep_loopback_description: "VXLAN_TUNNEL_SOURCE"
default_vrf_diag_loopback_description: "DIAG_VRF_{vrf}"

# Underlay point-to-point interfaces description
default_underlay_p2p_ethernet_description: "P2P_{peer}_{peer_interface}{vrf?<_VRF_}"
default_underlay_p2p_port_channel_description: "P2P_{peer}_{peer_interface}"

# Underlay l2 interfaces description
underlay_l2_ethernet_description: "L2_{peer}_{peer_interface}"
underlay_l2_port_channel_description: "L2_{peer_node_group_or_peer}_{peer_interface}"

# Management interface description
mgmt_interface_description: "OOB_MANAGEMENT"

# Endpoint description
default_connected_endpoints_description: "{endpoint_type!u}_{endpoint}{endpoint_port?<_}"
default_connected_endpoints_port_channel_description: "{endpoint_type!u}_{endpoint}{endpoint_port_channel?<_}"
default_network_ports_description: "{endpoint?}"
default_network_ports_port_channel_description: " {endpoint?}{endpoint_port_channel?<_}"

# MLAG interfaces description
mlag_member_description: "MLAG_{mlag_peer}_{peer_interface}"
mlag_port_channel_description: "MLAG_{mlag_peer}_{peer_interface}"
mlag_peer_svi_description: "MLAG"
mlag_peer_l3_svi_description: "MLAG_L3"
mlag_peer_l3_vrf_svi_description: "MLAG_L3_VRF_{vrf}"

# MLAG interfaces name
mlag_peer_vlan_name: "MLAG"
mlag_peer_l3_vlan_name: "MLAG_L3_VRF_{vrf}"
mlag_peer_l3_vrf_vlan_name: "MLAG_L3_VRF_{vrf}"

# MLAG BGP peer description
mlag_bgp_peer_description: "{mlag_peer}_{peer_interface}"

# Overlay BGP peer description
overlay_bgp_peer_description: "{peer}{peer_interface?<_}"
```
