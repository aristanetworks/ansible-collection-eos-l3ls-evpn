<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>maintenance</samp>](## "maintenance") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;default_interface_profile</samp>](## "maintenance.default_interface_profile") | String |  |  |  | Name of default Interface Profile.<br> |
    | [<samp>&nbsp;&nbsp;default_bgp_profile</samp>](## "maintenance.default_bgp_profile") | String |  |  |  | Name of default BGP Profile.<br> |
    | [<samp>&nbsp;&nbsp;default_unit_profile</samp>](## "maintenance.default_unit_profile") | String |  |  |  | Name of default Unit Profile.<br> |
    | [<samp>&nbsp;&nbsp;interface_profiles</samp>](## "maintenance.interface_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "maintenance.interface_profiles.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_monitoring</samp>](## "maintenance.interface_profiles.[].rate_monitoring") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;load_interval</samp>](## "maintenance.interface_profiles.[].rate_monitoring.load_interval") | Integer |  |  |  | Load Interval in Seconds.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;threshold</samp>](## "maintenance.interface_profiles.[].rate_monitoring.threshold") | Integer |  |  |  | Threshold in kbps.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "maintenance.interface_profiles.[].shutdown") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max_delay</samp>](## "maintenance.interface_profiles.[].shutdown.max_delay") | Integer |  |  |  | Max delay in seconds.<br> |
    | [<samp>&nbsp;&nbsp;bgp_profiles</samp>](## "maintenance.bgp_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "maintenance.bgp_profiles.[].name") | String | Required, Unique |  |  | BGP Profile Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;initiator</samp>](## "maintenance.bgp_profiles.[].initiator") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;route_map_inout</samp>](## "maintenance.bgp_profiles.[].initiator.route_map_inout") | String |  |  |  | Route Map. |
    | [<samp>&nbsp;&nbsp;unit_profiles</samp>](## "maintenance.unit_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "maintenance.unit_profiles.[].name") | String | Required, Unique |  |  | Unit Profile Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;on_boot</samp>](## "maintenance.unit_profiles.[].on_boot") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;duration</samp>](## "maintenance.unit_profiles.[].on_boot.duration") | Integer |  |  | Min: 300<br>Max: 3600 | On-boot in seconds.<br> |
    | [<samp>&nbsp;&nbsp;units</samp>](## "maintenance.units") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "maintenance.units.[].name") | String | Required, Unique |  |  | Unit Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;quiesce</samp>](## "maintenance.units.[].quiesce") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "maintenance.units.[].profile") | String |  |  |  | Name of Unit Profile.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "maintenance.units.[].groups") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_groups</samp>](## "maintenance.units.[].groups.bgp_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "maintenance.units.[].groups.bgp_groups.[]") | String |  |  |  | Name of BGP Group.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface_groups</samp>](## "maintenance.units.[].groups.interface_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "maintenance.units.[].groups.interface_groups.[]") | String |  |  |  | Name of Interface Group.<br> |

=== "YAML"

    ```yaml
    maintenance:

      # Name of default Interface Profile.
      default_interface_profile: <str>

      # Name of default BGP Profile.
      default_bgp_profile: <str>

      # Name of default Unit Profile.
      default_unit_profile: <str>
      interface_profiles:
        - name: <str; required; unique>
          rate_monitoring:

            # Load Interval in Seconds.
            load_interval: <int>

            # Threshold in kbps.
            threshold: <int>
          shutdown:

            # Max delay in seconds.
            max_delay: <int>
      bgp_profiles:

          # BGP Profile Name.
        - name: <str; required; unique>
          initiator:

            # Route Map.
            route_map_inout: <str>
      unit_profiles:

          # Unit Profile Name.
        - name: <str; required; unique>
          on_boot:

            # On-boot in seconds.
            duration: <int; 300-3600>
      units:

          # Unit Name.
        - name: <str; required; unique>
          quiesce: <bool>

          # Name of Unit Profile.
          profile: <str>
          groups:
            bgp_groups:

                # Name of BGP Group.
              - <str>
            interface_groups:

                # Name of Interface Group.
              - <str>
    ```
