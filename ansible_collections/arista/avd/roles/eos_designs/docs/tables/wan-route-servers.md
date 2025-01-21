<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>wan_route_servers</samp>](## "wan_route_servers") | List, items: Dictionary |  |  |  | List of the AutoVPN RRs when using `wan_mode: autovpn`, or the Pathfinders<br>when using `wan_mode: cv-pathfinder`, to which the device should connect to.<br>This is also used to establish iBGP sessions between WAN route servers.<br><br>When the route server is part of the same inventory as the WAN routers,<br>only the name is required. |
    | [<samp>&nbsp;&nbsp;-&nbsp;hostname</samp>](## "wan_route_servers.[].hostname") | String | Required, Unique |  |  | Route-Reflector hostname. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vtep_ip</samp>](## "wan_route_servers.[].vtep_ip") | String |  |  |  | Route-Reflector VTEP IP Address. This is usually the IP address under `interface Dps1`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;path_groups</samp>](## "wan_route_servers.[].path_groups") | List, items: Dictionary |  |  |  | Path-groups through which the Route Reflector/Pathfinder is reached. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "wan_route_servers.[].path_groups.[].name") | String | Required, Unique |  |  | Path-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "wan_route_servers.[].path_groups.[].interfaces") | List, items: Dictionary | Required |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "wan_route_servers.[].path_groups.[].interfaces.[].name") | String | Required, Unique |  |  | Interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;public_ip</samp>](## "wan_route_servers.[].path_groups.[].interfaces.[].public_ip") | String |  |  |  | The public IPv4 address (without mask) of the Route Reflector for this path-group. |

=== "YAML"

    ```yaml
    # List of the AutoVPN RRs when using `wan_mode: autovpn`, or the Pathfinders
    # when using `wan_mode: cv-pathfinder`, to which the device should connect to.
    # This is also used to establish iBGP sessions between WAN route servers.
    #
    # When the route server is part of the same inventory as the WAN routers,
    # only the name is required.
    wan_route_servers:

        # Route-Reflector hostname.
      - hostname: <str; required; unique>

        # Route-Reflector VTEP IP Address. This is usually the IP address under `interface Dps1`.
        vtep_ip: <str>

        # Path-groups through which the Route Reflector/Pathfinder is reached.
        path_groups:

            # Path-group name.
          - name: <str; required; unique>
            interfaces: # >=1 items; required

                # Interface name.
              - name: <str; required; unique>

                # The public IPv4 address (without mask) of the Route Reflector for this path-group.
                public_ip: <str>
    ```
