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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "<node_type_keys.key>.defaults.bgp_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.<br>Required with eBGP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_defaults</samp>](## "<node_type_keys.key>.defaults.bgp_defaults") | List, items: String |  |  |  | List of EOS commands to apply to BGP daemon. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.defaults.bgp_defaults.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_role</samp>](## "<node_type_keys.key>.defaults.evpn_role") | String |  |  | Valid Values:<br>- <code>client</code><br>- <code>server</code><br>- <code>none</code> | Acting role in EVPN control plane.<br>Default is set in node_type definition from node_type_keys.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_route_servers</samp>](## "<node_type_keys.key>.defaults.evpn_route_servers") | List, items: String |  |  |  | List of nodes acting as EVPN Route-Servers / Route-Reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.defaults.evpn_route_servers.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].bgp_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.<br>Required with eBGP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_defaults</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].bgp_defaults") | List, items: String |  |  |  | List of EOS commands to apply to BGP daemon. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].bgp_defaults.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_role</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].evpn_role") | String |  |  | Valid Values:<br>- <code>client</code><br>- <code>server</code><br>- <code>none</code> | Acting role in EVPN control plane.<br>Default is set in node_type definition from node_type_keys.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_route_servers</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].evpn_route_servers") | List, items: String |  |  |  | List of nodes acting as EVPN Route-Servers / Route-Reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].evpn_route_servers.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "<node_type_keys.key>.node_groups.[].bgp_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.<br>Required with eBGP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_defaults</samp>](## "<node_type_keys.key>.node_groups.[].bgp_defaults") | List, items: String |  |  |  | List of EOS commands to apply to BGP daemon. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].bgp_defaults.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_role</samp>](## "<node_type_keys.key>.node_groups.[].evpn_role") | String |  |  | Valid Values:<br>- <code>client</code><br>- <code>server</code><br>- <code>none</code> | Acting role in EVPN control plane.<br>Default is set in node_type definition from node_type_keys.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_route_servers</samp>](## "<node_type_keys.key>.node_groups.[].evpn_route_servers") | List, items: String |  |  |  | List of nodes acting as EVPN Route-Servers / Route-Reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].evpn_route_servers.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_as</samp>](## "<node_type_keys.key>.nodes.[].bgp_as") | String |  |  |  | BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".<br>For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.<br>Required with eBGP. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_defaults</samp>](## "<node_type_keys.key>.nodes.[].bgp_defaults") | List, items: String |  |  |  | List of EOS commands to apply to BGP daemon. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.nodes.[].bgp_defaults.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_role</samp>](## "<node_type_keys.key>.nodes.[].evpn_role") | String |  |  | Valid Values:<br>- <code>client</code><br>- <code>server</code><br>- <code>none</code> | Acting role in EVPN control plane.<br>Default is set in node_type definition from node_type_keys.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_route_servers</samp>](## "<node_type_keys.key>.nodes.[].evpn_route_servers") | List, items: String |  |  |  | List of nodes acting as EVPN Route-Servers / Route-Reflectors. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.nodes.[].evpn_route_servers.[]") | String |  |  |  |  |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:

        # BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
        # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
        # Required with eBGP.
        bgp_as: <str>

        # List of EOS commands to apply to BGP daemon.
        bgp_defaults:
          - <str>

        # Acting role in EVPN control plane.
        # Default is set in node_type definition from node_type_keys.
        evpn_role: <str; "client" | "server" | "none">

        # List of nodes acting as EVPN Route-Servers / Route-Reflectors.
        evpn_route_servers:
          - <str>

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>

              # BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
              # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
              # Required with eBGP.
              bgp_as: <str>

              # List of EOS commands to apply to BGP daemon.
              bgp_defaults:
                - <str>

              # Acting role in EVPN control plane.
              # Default is set in node_type definition from node_type_keys.
              evpn_role: <str; "client" | "server" | "none">

              # List of nodes acting as EVPN Route-Servers / Route-Reflectors.
              evpn_route_servers:
                - <str>

          # BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
          # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
          # Required with eBGP.
          bgp_as: <str>

          # List of EOS commands to apply to BGP daemon.
          bgp_defaults:
            - <str>

          # Acting role in EVPN control plane.
          # Default is set in node_type definition from node_type_keys.
          evpn_role: <str; "client" | "server" | "none">

          # List of nodes acting as EVPN Route-Servers / Route-Reflectors.
          evpn_route_servers:
            - <str>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>

          # BGP AS <1-4294967295> or AS number in asdot notation "<1-65535>.<0-65535>".
          # For asdot notation in YAML inputs, the value must be put in quotes, to prevent it from being interpreted as a float number.
          # Required with eBGP.
          bgp_as: <str>

          # List of EOS commands to apply to BGP daemon.
          bgp_defaults:
            - <str>

          # Acting role in EVPN control plane.
          # Default is set in node_type definition from node_type_keys.
          evpn_role: <str; "client" | "server" | "none">

          # List of nodes acting as EVPN Route-Servers / Route-Reflectors.
          evpn_route_servers:
            - <str>
    ```
