<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_internet_exit</samp>](## "router_internet_exit") | Dictionary |  |  |  | Internet-exit feature to configure internet bound service for virtual topologies. |
    | [<samp>&nbsp;&nbsp;policies</samp>](## "router_internet_exit.policies") | List, items: Dictionary |  |  |  | Internet-exit policy represent a policy which can be attached to a virtual topology profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_internet_exit.policies.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;exit_groups</samp>](## "router_internet_exit.policies.[].exit_groups") | List, items: Dictionary |  |  |  | The exit groups that are configured under a policy are strictly ordered, meaning an exit group appearing first has more priority than the exit group that follows it. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_internet_exit.policies.[].exit_groups.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;exit_groups</samp>](## "router_internet_exit.exit_groups") | List, items: Dictionary |  |  |  | Exit groups represent a group of exit options (connections).<br>Traffic flows are load balanced in a round robin fashion across all the members (exits) of the exit-group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_internet_exit.exit_groups.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fib_default</samp>](## "router_internet_exit.exit_groups.[].fib_default") | Boolean |  |  |  | Fib default exit indicates that the flows that select this exit will follow the default route available in the VRF of the flow. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_connections</samp>](## "router_internet_exit.exit_groups.[].local_connections") | List, items: Dictionary |  |  |  | Local connections refer to connections configured under the `router_service_insertion`.<br>The service-insertion module reports the health of the connection and the exit will qualify for use only when it is healthy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_internet_exit.exit_groups.[].local_connections.[].name") | String |  |  |  |  |

=== "YAML"

    ```yaml
    # Internet-exit feature to configure internet bound service for virtual topologies.
    router_internet_exit:

      # Internet-exit policy represent a policy which can be attached to a virtual topology profile.
      policies:
        - name: <str; required; unique>

          # The exit groups that are configured under a policy are strictly ordered, meaning an exit group appearing first has more priority than the exit group that follows it.
          exit_groups:
            - name: <str>

      # Exit groups represent a group of exit options (connections).
      # Traffic flows are load balanced in a round robin fashion across all the members (exits) of the exit-group.
      exit_groups:
        - name: <str; required; unique>

          # Fib default exit indicates that the flows that select this exit will follow the default route available in the VRF of the flow.
          fib_default: <bool>

          # Local connections refer to connections configured under the `router_service_insertion`.
          # The service-insertion module reports the health of the connection and the exit will qualify for use only when it is healthy.
          local_connections:
            - name: <str>
    ```
