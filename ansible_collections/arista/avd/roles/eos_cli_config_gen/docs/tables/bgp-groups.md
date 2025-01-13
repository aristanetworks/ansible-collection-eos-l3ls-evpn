<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bgp_groups</samp>](## "bgp_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "bgp_groups.[].name") | String | Required, Unique |  |  | Group Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "bgp_groups.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;neighbors</samp>](## "bgp_groups.[].neighbors") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "bgp_groups.[].neighbors.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_maintenance_profiles</samp>](## "bgp_groups.[].bgp_maintenance_profiles") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "bgp_groups.[].bgp_maintenance_profiles.[]") | String |  |  |  | Profile Name. |

=== "YAML"

    ```yaml
    bgp_groups:

        # Group Name.
      - name: <str; required; unique>
        vrf: <str>
        neighbors:
          - <str>
        bgp_maintenance_profiles:

            # Profile Name.
          - <str>
    ```
