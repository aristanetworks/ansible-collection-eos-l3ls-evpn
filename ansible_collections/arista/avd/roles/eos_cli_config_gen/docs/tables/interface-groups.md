<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>interface_groups</samp>](## "interface_groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "interface_groups.[].name") | String | Required, Unique |  |  | Interface-Group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "interface_groups.[].interfaces") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "interface_groups.[].interfaces.[]") | String |  |  |  | Interface Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp_maintenance_profiles</samp>](## "interface_groups.[].bgp_maintenance_profiles") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "interface_groups.[].bgp_maintenance_profiles.[]") | String |  |  |  | Name of BGP Maintenance Profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface_maintenance_profiles</samp>](## "interface_groups.[].interface_maintenance_profiles") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "interface_groups.[].interface_maintenance_profiles.[]") | String |  |  |  | Name of Interface Maintenance Profile. |

=== "YAML"

    ```yaml
    interface_groups:

        # Interface-Group name.
      - name: <str; required; unique>
        interfaces:

            # Interface Name.
          - <str>
        bgp_maintenance_profiles:

            # Name of BGP Maintenance Profile.
          - <str>
        interface_maintenance_profiles:

            # Name of Interface Maintenance Profile.
          - <str>
    ```
