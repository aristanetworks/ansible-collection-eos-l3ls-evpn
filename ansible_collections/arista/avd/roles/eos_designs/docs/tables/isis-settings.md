<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>isis_advertise_passive_only</samp>](## "isis_advertise_passive_only") | Boolean |  | `False` |  |  |
    | [<samp>isis_area_id</samp>](## "isis_area_id") | String |  | `49.0001` |  |  |
    | [<samp>isis_default_circuit_type</samp>](## "isis_default_circuit_type") | String |  | `level-2` | Valid Values:<br>- <code>level-1-2</code><br>- <code>level-1</code><br>- <code>level-2</code> | These fabric level parameters can be used with core_interfaces running ISIS, and may be overridden on link profile or link level.<br> |
    | [<samp>isis_default_is_type</samp>](## "isis_default_is_type") | String |  | `level-2` | Valid Values:<br>- <code>level-1-2</code><br>- <code>level-1</code><br>- <code>level-2</code> |  |
    | [<samp>isis_default_metric</samp>](## "isis_default_metric") | Integer |  | `50` |  | These fabric level parameters can be used with core_interfaces running ISIS, and may be overridden at link profile or link level.<br> |
    | [<samp>isis_maximum_paths</samp>](## "isis_maximum_paths") | Integer |  | `4` |  | Number of path to configure in ECMP for ISIS. |
    | [<samp>isis_system_id_format</samp>](## "isis_system_id_format") | String |  | `underlay_loopback` | Valid Values:<br>- <code>node_id</code><br>- <code>underlay_loopback</code> | Configures source for the system-id within the ISIS net id.<br>If this key is set to `node_id`, the fields `id` and `isis_system_id_prefix` configured under the node attributes are used to generate the system-id.<br>If `underlay_loopback` is selected then all node `isis_system_id_prefix` settings will be ignored and the loopback address will be used to generate the system-id. |
    | [<samp>isis_ti_lfa</samp>](## "isis_ti_lfa") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "isis_ti_lfa.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;protection</samp>](## "isis_ti_lfa.protection") | String |  |  | Valid Values:<br>- <code>link</code><br>- <code>node</code> |  |
    | [<samp>&nbsp;&nbsp;local_convergence_delay</samp>](## "isis_ti_lfa.local_convergence_delay") | Integer |  | `10000` |  | Local convergence delay in milliseconds. |
    | [<samp>underlay_isis_authentication_key</samp>](## "underlay_isis_authentication_key") | String |  |  |  | Type-7 encrypted password. |
    | [<samp>underlay_isis_authentication_mode</samp>](## "underlay_isis_authentication_mode") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>text</code> | Underlay ISIS authentication mode. |
    | [<samp>underlay_isis_bfd</samp>](## "underlay_isis_bfd") | Boolean |  | `False` |  | Enable BFD for ISIS on all underlay links. |
    | [<samp>underlay_isis_instance_name</samp>](## "underlay_isis_instance_name") | String |  |  |  | Default -> "EVPN_UNDERLAY" for l3ls, "CORE" for mpls. |

=== "YAML"

    ```yaml
    isis_advertise_passive_only: <bool; default=False>
    isis_area_id: <str; default="49.0001">

    # These fabric level parameters can be used with core_interfaces running ISIS, and may be overridden on link profile or link level.
    isis_default_circuit_type: <str; "level-1-2" | "level-1" | "level-2"; default="level-2">
    isis_default_is_type: <str; "level-1-2" | "level-1" | "level-2"; default="level-2">

    # These fabric level parameters can be used with core_interfaces running ISIS, and may be overridden at link profile or link level.
    isis_default_metric: <int; default=50>

    # Number of path to configure in ECMP for ISIS.
    isis_maximum_paths: <int; default=4>

    # Configures source for the system-id within the ISIS net id.
    # If this key is set to `node_id`, the fields `id` and `isis_system_id_prefix` configured under the node attributes are used to generate the system-id.
    # If `underlay_loopback` is selected then all node `isis_system_id_prefix` settings will be ignored and the loopback address will be used to generate the system-id.
    isis_system_id_format: <str; "node_id" | "underlay_loopback"; default="underlay_loopback">
    isis_ti_lfa:
      enabled: <bool; default=False>
      protection: <str; "link" | "node">

      # Local convergence delay in milliseconds.
      local_convergence_delay: <int; default=10000>

    # Type-7 encrypted password.
    underlay_isis_authentication_key: <str>

    # Underlay ISIS authentication mode.
    underlay_isis_authentication_mode: <str; "md5" | "text">

    # Enable BFD for ISIS on all underlay links.
    underlay_isis_bfd: <bool; default=False>

    # Default -> "EVPN_UNDERLAY" for l3ls, "CORE" for mpls.
    underlay_isis_instance_name: <str>
    ```
