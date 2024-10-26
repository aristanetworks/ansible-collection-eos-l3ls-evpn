<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_adaptive_virtual_topology</samp>](## "router_adaptive_virtual_topology") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;topology_role</samp>](## "router_adaptive_virtual_topology.topology_role") | String |  |  | Valid Values:<br>- <code>edge</code><br>- <code>pathfinder</code><br>- <code>transit region</code><br>- <code>transit zone</code> | Role name. |
    | [<samp>&nbsp;&nbsp;gateway_vxlan</samp>](## "router_adaptive_virtual_topology.gateway_vxlan") | Boolean |  |  |  | Enables VXLAN gateway router profile.<br>Only applicable for `topology_role: edge`, `topology_role: transit region` or `topology_role: transit zone`. |
    | [<samp>&nbsp;&nbsp;region</samp>](## "router_adaptive_virtual_topology.region") | Dictionary |  |  |  | Region name and ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "router_adaptive_virtual_topology.region.name") | String | Required |  | Pattern: `^[A-Za-z0-9_.:{}\[\]-]+$` |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "router_adaptive_virtual_topology.region.id") | Integer | Required |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;zone</samp>](## "router_adaptive_virtual_topology.zone") | Dictionary |  |  |  | Zone name and ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "router_adaptive_virtual_topology.zone.name") | String | Required |  | Pattern: `^[A-Za-z0-9_.:{}\[\]-]+$` |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "router_adaptive_virtual_topology.zone.id") | Integer | Required |  | Min: 1<br>Max: 10000 |  |
    | [<samp>&nbsp;&nbsp;site</samp>](## "router_adaptive_virtual_topology.site") | Dictionary |  |  |  | Site name and ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "router_adaptive_virtual_topology.site.name") | String | Required |  | Pattern: `^[A-Za-z0-9_.:{}\[\]-]+$` |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "router_adaptive_virtual_topology.site.id") | Integer | Required |  | Min: 1<br>Max: 10000 |  |
    | [<samp>&nbsp;&nbsp;profiles</samp>](## "router_adaptive_virtual_topology.profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_adaptive_virtual_topology.profiles.[].name") | String | Required, Unique |  |  | AVT Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;load_balance_policy</samp>](## "router_adaptive_virtual_topology.profiles.[].load_balance_policy") | String |  |  |  | Name of the load-balance policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;internet_exit_policy</samp>](## "router_adaptive_virtual_topology.profiles.[].internet_exit_policy") | String |  |  |  | Name of the internet exit policy. |
    | [<samp>&nbsp;&nbsp;policies</samp>](## "router_adaptive_virtual_topology.policies") | List, items: Dictionary |  |  |  | A sequence of application profiles mapped to some virtual topologies. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_adaptive_virtual_topology.policies.[].name") | String | Required, Unique |  |  | Policy name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;matches</samp>](## "router_adaptive_virtual_topology.policies.[].matches") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;application_profile</samp>](## "router_adaptive_virtual_topology.policies.[].matches.[].application_profile") | String |  |  |  | Application profile name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;avt_profile</samp>](## "router_adaptive_virtual_topology.policies.[].matches.[].avt_profile") | String |  |  |  | AVT Profile name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "router_adaptive_virtual_topology.policies.[].matches.[].dscp") | Integer |  |  | Min: 0<br>Max: 63 | Set DSCP for matched traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp>](## "router_adaptive_virtual_topology.policies.[].matches.[].traffic_class") | Integer |  |  | Min: 0<br>Max: 7 | Set traffic-class for matched traffic. |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "router_adaptive_virtual_topology.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_adaptive_virtual_topology.vrfs.[].name") | String | Required, Unique |  |  | VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;policy</samp>](## "router_adaptive_virtual_topology.vrfs.[].policy") | String |  |  |  | AVT Policy name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profiles</samp>](## "router_adaptive_virtual_topology.vrfs.[].profiles") | List, items: Dictionary |  |  |  | AVT profiles in this VRF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_adaptive_virtual_topology.vrfs.[].profiles.[].name") | String |  |  |  | AVT profile name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "router_adaptive_virtual_topology.vrfs.[].profiles.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 254 | Unique ID for this AVT (per VRF). |

=== "YAML"

    ```yaml
    router_adaptive_virtual_topology:

      # Role name.
      topology_role: <str; "edge" | "pathfinder" | "transit region" | "transit zone">

      # Enables VXLAN gateway router profile.
      # Only applicable for `topology_role: edge`, `topology_role: transit region` or `topology_role: transit zone`.
      gateway_vxlan: <bool>

      # Region name and ID.
      region:
        name: <str; required>
        id: <int; 1-255; required>

      # Zone name and ID.
      zone:
        name: <str; required>
        id: <int; 1-10000; required>

      # Site name and ID.
      site:
        name: <str; required>
        id: <int; 1-10000; required>
      profiles:

          # AVT Name.
        - name: <str; required; unique>

          # Name of the load-balance policy.
          load_balance_policy: <str>

          # Name of the internet exit policy.
          internet_exit_policy: <str>

      # A sequence of application profiles mapped to some virtual topologies.
      policies:

          # Policy name.
        - name: <str; required; unique>
          matches:

              # Application profile name.
            - application_profile: <str>

              # AVT Profile name.
              avt_profile: <str>

              # Set DSCP for matched traffic.
              dscp: <int; 0-63>

              # Set traffic-class for matched traffic.
              traffic_class: <int; 0-7>
      vrfs:

          # VRF name.
        - name: <str; required; unique>

          # AVT Policy name.
          policy: <str>

          # AVT profiles in this VRF.
          profiles:

              # AVT profile name.
            - name: <str>

              # Unique ID for this AVT (per VRF).
              id: <int; 1-254; required; unique>
    ```
