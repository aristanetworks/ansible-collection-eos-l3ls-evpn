<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>wan_virtual_topologies</samp>](## "wan_virtual_topologies") | Dictionary |  |  |  | Configure Virtual Topologies for CV Pathfinder and AutoVPN.<br>Auto create a control plane profile/policy/application and enforce it being first in the default VRF. |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "wan_virtual_topologies.vrfs") | List, items: Dictionary |  |  |  | Map a VRF that exists in network_services to an AVT policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "wan_virtual_topologies.vrfs.[].name") | String | Required, Unique |  |  | VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;policy</samp>](## "wan_virtual_topologies.vrfs.[].policy") | String |  | `DEFAULT-POLICY` |  | Name of the policy to apply to this VRF.<br>AVD will auto generate a default policy DEFAULT-POLICY and apply it to the VRF(s)<br>where the `policy` key is not set.<br>It is possible to overwrite the default policy for all VRFs using it<br>by redefining it in the `wan_virtual_topologies.policies` list using the<br>default name `DEFAULT-POLICY`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;wan_vni</samp>](## "wan_virtual_topologies.vrfs.[].wan_vni") | Integer | Required |  | Min: 1<br>Max: 255 | Required for VRFs carried over AutoVPN or CV Pathfinder WAN.<br><br>A VRF can have different VNIs between the Datacenters and the WAN.<br>Note that if no VRF default is configured for WAN, AVD will automatically inject the VRF default with<br>`wan_vni` set to `1`.<br>In addition either `vrf_id` or `vrf_vni` must be set to enforce consistent route-targets across domains. |
    | [<samp>&nbsp;&nbsp;control_plane_virtual_topology</samp>](## "wan_virtual_topologies.control_plane_virtual_topology") | Dictionary |  |  |  | Always injected into the default VRF policy as the first entry.<br><br>By default, if no path-groups are specified, all locally available path-groups<br>are used in the generated load-balance policy.<br>ID is hardcoded to 254 for the AVT profile in CV Pathfinder mode. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "wan_virtual_topologies.control_plane_virtual_topology.name") | String |  |  |  | Optional name, if not set `CONTROL-PLANE-PROFILE` is used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;application_profile</samp>](## "wan_virtual_topologies.control_plane_virtual_topology.application_profile") | String |  | `APP-PROFILE-CONTROL-PLANE` |  | The application profile to use for control plane traffic.<br><br>The application profile should be defined under `application_classification.application_profiles`.<br>If not defined AVD will auto generate an application profile using the provided name or the default value.<br><br>If not overwritten elsewhere, the application profile is generated matching one application matching the control plane traffic either sourced from or destined to the WAN route servers. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp>](## "wan_virtual_topologies.control_plane_virtual_topology.traffic_class") | Integer |  |  | Min: 0<br>Max: 7 | Set traffic-class for matched traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "wan_virtual_topologies.control_plane_virtual_topology.dscp") | Integer |  |  | Min: 0<br>Max: 63 | Set DSCP for matched traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lowest_hop_count</samp>](## "wan_virtual_topologies.control_plane_virtual_topology.lowest_hop_count") | Boolean |  | `False` |  | Prefer paths with lowest hop-count.<br>Only applicable for `wan_mode: "cv-pathfinder"`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;constraints</samp>](## "wan_virtual_topologies.control_plane_virtual_topology.constraints") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;jitter</samp>](## "wan_virtual_topologies.control_plane_virtual_topology.constraints.jitter") | Integer |  |  | Min: 0<br>Max: 10000 | Jitter requirement for this load balance policy in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;latency</samp>](## "wan_virtual_topologies.control_plane_virtual_topology.constraints.latency") | Integer |  |  | Min: 0<br>Max: 10000 | One way delay requirement for this load balance policy in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loss_rate</samp>](## "wan_virtual_topologies.control_plane_virtual_topology.constraints.loss_rate") | String |  |  | Pattern: `^\d+(\.\d{1,2})?$` | Loss Rate requirement in percentage for this load balance policy.<br>Value between 0.00 and 100.00. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;path_groups</samp>](## "wan_virtual_topologies.control_plane_virtual_topology.path_groups") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;names</samp>](## "wan_virtual_topologies.control_plane_virtual_topology.path_groups.[].names") | List, items: String | Required |  | Min Length: 1 | List of path-group names. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "wan_virtual_topologies.control_plane_virtual_topology.path_groups.[].names.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preference</samp>](## "wan_virtual_topologies.control_plane_virtual_topology.path_groups.[].preference") | String |  |  |  | Valid values are 1-65535 | "preferred" | "alternate".<br><br>"preferred" is converted to priority 1.<br>"alternate" is converted to priority 2.<br><br>If not set, each path-group in `names` will be attributed its `default_preference`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;internet_exit</samp>](## "wan_virtual_topologies.control_plane_virtual_topology.internet_exit") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;policy</samp>](## "wan_virtual_topologies.control_plane_virtual_topology.internet_exit.policy") | String |  |  |  | PREVIEW: This key is in preview mode.<br><br>Internet-exit policy name associated with this virtual_topology.<br>The policy must be defined under `cv_pathfinder_internet_exit_policies`. |
    | [<samp>&nbsp;&nbsp;policies</samp>](## "wan_virtual_topologies.policies") | List, items: Dictionary |  |  |  | List of virtual toplogies policies.<br><br>For AutoVPN, each item in the list creates:<br>  * one policy with:<br>      * one `match` entry per `application_virtual_topologies` item<br>        they are indexed using `10 * <list_index>` where `list_index` starts at `1`.<br>      * one `default-match`<br>  * one load-balance policy per `application_virtual_topologies` and one for the `default_virtual_topology`.<br>  * if the policy is associated with the default VRF, a special control-plane rule is injected<br>    in the policy with index `1` referring to a control-plane load-balance policy as defined under<br>    `control_plane_virtual_topology` or if not set, the default one.<br><br>For CV Pathfinder, each item in the list creates:<br>  * one policy with:<br>      * one `match` entry per `application_virtual_topologies` item ordered as in the data.<br>      * one last match entry for the `default` application-profile using `default_virtual_topology` information.<br>  * one profile per `application_virtual_topologies` item.<br>  * one profile for the `default_virtual_topology`.<br>  * one load-balance policy per `application_virtual_topologies`.<br>  * one load_balance policy for the `default_virtual_topology`.<br>  * if the policy is associated with the default VRF, a special control-plane profile is configured<br>    and injected first in the policy assigned to the `default` VRF. This profile points to a<br>    control-plane load-balance policy as defined under `control_plane_virtual_topology` or if not set, the default one. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "wan_virtual_topologies.policies.[].name") | String | Required, Unique |  |  | Name of the AVT policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;application_virtual_topologies</samp>](## "wan_virtual_topologies.policies.[].application_virtual_topologies") | List, items: Dictionary |  |  |  | List of application specific virtual topologies. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;application_profile</samp>](## "wan_virtual_topologies.policies.[].application_virtual_topologies.[].application_profile") | String | Required, Unique |  |  | The application profile to use for this virtual topology. It must be a defined `application_classification.application_profile`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "wan_virtual_topologies.policies.[].application_virtual_topologies.[].name") | String |  |  |  | Optional name, if not set `<policy_name>-<application_profile>` is used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "wan_virtual_topologies.policies.[].application_virtual_topologies.[].id") | Integer |  |  | Min: 2<br>Max: 253 | ID of the AVT in each VRFs. ID must be unique across all virtual topologies in a policy.<br>ID 1 is reserved for the default_virtual_toplogy.<br>ID 254 is reserved for the control_plane_virtual_topology.<br><br>`id` is required when `wan_mode` is 'cv-pathfinder'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp>](## "wan_virtual_topologies.policies.[].application_virtual_topologies.[].traffic_class") | Integer |  |  | Min: 0<br>Max: 7 | Set traffic-class for matched traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "wan_virtual_topologies.policies.[].application_virtual_topologies.[].dscp") | Integer |  |  | Min: 0<br>Max: 63 | Set DSCP for matched traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lowest_hop_count</samp>](## "wan_virtual_topologies.policies.[].application_virtual_topologies.[].lowest_hop_count") | Boolean |  | `False` |  | Prefer paths with lowest hop-count.<br>Only applicable for `wan_mode: "cv-pathfinder"`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;constraints</samp>](## "wan_virtual_topologies.policies.[].application_virtual_topologies.[].constraints") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;jitter</samp>](## "wan_virtual_topologies.policies.[].application_virtual_topologies.[].constraints.jitter") | Integer |  |  | Min: 0<br>Max: 10000 | Jitter requirement for this load balance policy in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;latency</samp>](## "wan_virtual_topologies.policies.[].application_virtual_topologies.[].constraints.latency") | Integer |  |  | Min: 0<br>Max: 10000 | One way delay requirement for this load balance policy in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loss_rate</samp>](## "wan_virtual_topologies.policies.[].application_virtual_topologies.[].constraints.loss_rate") | String |  |  | Pattern: `^\d+(\.\d{1,2})?$` | Loss Rate requirement in percentage for this load balance policy.<br>Value between 0.00 and 100.00. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;path_groups</samp>](## "wan_virtual_topologies.policies.[].application_virtual_topologies.[].path_groups") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;names</samp>](## "wan_virtual_topologies.policies.[].application_virtual_topologies.[].path_groups.[].names") | List, items: String | Required |  | Min Length: 1 | List of path-group names. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "wan_virtual_topologies.policies.[].application_virtual_topologies.[].path_groups.[].names.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preference</samp>](## "wan_virtual_topologies.policies.[].application_virtual_topologies.[].path_groups.[].preference") | String |  |  |  | Valid values are 1-65535 | "preferred" | "alternate".<br><br>"preferred" is converted to priority 1.<br>"alternate" is converted to priority 2.<br><br>If not set, each path-group in `names` will be attributed its `default_preference`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;internet_exit</samp>](## "wan_virtual_topologies.policies.[].application_virtual_topologies.[].internet_exit") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;policy</samp>](## "wan_virtual_topologies.policies.[].application_virtual_topologies.[].internet_exit.policy") | String |  |  |  | PREVIEW: This key is in preview mode.<br><br>Internet-exit policy name associated with this virtual_topology.<br>The policy must be defined under `cv_pathfinder_internet_exit_policies`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_virtual_topology</samp>](## "wan_virtual_topologies.policies.[].default_virtual_topology") | Dictionary | Required |  |  | Default match for the policy.<br>If no default match should be configured, set `drop_unmatched` to `true`.<br>Otherwise, in CV Pathfinder mode, a default AVT profile will be configured with ID 1. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "wan_virtual_topologies.policies.[].default_virtual_topology.name") | String |  |  |  | Optional name, if not set `<policy_name>-DEFAULT` is used. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop_unmatched</samp>](## "wan_virtual_topologies.policies.[].default_virtual_topology.drop_unmatched") | Boolean |  | `False` |  | When set, no `catch-all` match is configured for the policy and unmatched traffic is dropped. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp>](## "wan_virtual_topologies.policies.[].default_virtual_topology.traffic_class") | Integer |  |  | Min: 0<br>Max: 7 | Set traffic-class for matched traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "wan_virtual_topologies.policies.[].default_virtual_topology.dscp") | Integer |  |  | Min: 0<br>Max: 63 | Set DSCP for matched traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lowest_hop_count</samp>](## "wan_virtual_topologies.policies.[].default_virtual_topology.lowest_hop_count") | Boolean |  | `False` |  | Prefer paths with lowest hop-count.<br>Only applicable for `wan_mode: "cv-pathfinder"`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;constraints</samp>](## "wan_virtual_topologies.policies.[].default_virtual_topology.constraints") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;jitter</samp>](## "wan_virtual_topologies.policies.[].default_virtual_topology.constraints.jitter") | Integer |  |  | Min: 0<br>Max: 10000 | Jitter requirement for this load balance policy in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;latency</samp>](## "wan_virtual_topologies.policies.[].default_virtual_topology.constraints.latency") | Integer |  |  | Min: 0<br>Max: 10000 | One way delay requirement for this load balance policy in milliseconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;loss_rate</samp>](## "wan_virtual_topologies.policies.[].default_virtual_topology.constraints.loss_rate") | String |  |  | Pattern: `^\d+(\.\d{1,2})?$` | Loss Rate requirement in percentage for this load balance policy.<br>Value between 0.00 and 100.00. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;path_groups</samp>](## "wan_virtual_topologies.policies.[].default_virtual_topology.path_groups") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;names</samp>](## "wan_virtual_topologies.policies.[].default_virtual_topology.path_groups.[].names") | List, items: String | Required |  | Min Length: 1 | List of path-group names. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "wan_virtual_topologies.policies.[].default_virtual_topology.path_groups.[].names.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preference</samp>](## "wan_virtual_topologies.policies.[].default_virtual_topology.path_groups.[].preference") | String |  |  |  | Valid values are 1-65535 | "preferred" | "alternate".<br><br>"preferred" is converted to priority 1.<br>"alternate" is converted to priority 2.<br><br>If not set, each path-group in `names` will be attributed its `default_preference`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;internet_exit</samp>](## "wan_virtual_topologies.policies.[].default_virtual_topology.internet_exit") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;policy</samp>](## "wan_virtual_topologies.policies.[].default_virtual_topology.internet_exit.policy") | String |  |  |  | PREVIEW: This key is in preview mode.<br><br>Internet-exit policy name associated with this virtual_topology.<br>The policy must be defined under `cv_pathfinder_internet_exit_policies`. |

=== "YAML"

    ```yaml
    # Configure Virtual Topologies for CV Pathfinder and AutoVPN.
    # Auto create a control plane profile/policy/application and enforce it being first in the default VRF.
    wan_virtual_topologies:

      # Map a VRF that exists in network_services to an AVT policy.
      vrfs:

          # VRF name.
        - name: <str; required; unique>

          # Name of the policy to apply to this VRF.
          # AVD will auto generate a default policy DEFAULT-POLICY and apply it to the VRF(s)
          # where the `policy` key is not set.
          # It is possible to overwrite the default policy for all VRFs using it
          # by redefining it in the `wan_virtual_topologies.policies` list using the
          # default name `DEFAULT-POLICY`.
          policy: <str; default="DEFAULT-POLICY">

          # Required for VRFs carried over AutoVPN or CV Pathfinder WAN.
          #
          # A VRF can have different VNIs between the Datacenters and the WAN.
          # Note that if no VRF default is configured for WAN, AVD will automatically inject the VRF default with
          # `wan_vni` set to `1`.
          # In addition either `vrf_id` or `vrf_vni` must be set to enforce consistent route-targets across domains.
          wan_vni: <int; 1-255; required>

      # Always injected into the default VRF policy as the first entry.
      #
      # By default, if no path-groups are specified, all locally available path-groups
      # are used in the generated load-balance policy.
      # ID is hardcoded to 254 for the AVT profile in CV Pathfinder mode.
      control_plane_virtual_topology:

        # Optional name, if not set `CONTROL-PLANE-PROFILE` is used.
        name: <str>

        # The application profile to use for control plane traffic.
        #
        # The application profile should be defined under `application_classification.application_profiles`.
        # If not defined AVD will auto generate an application profile using the provided name or the default value.
        #
        # If not overwritten elsewhere, the application profile is generated matching one application matching the control plane traffic either sourced from or destined to the WAN route servers.
        application_profile: <str; default="APP-PROFILE-CONTROL-PLANE">

        # Set traffic-class for matched traffic.
        traffic_class: <int; 0-7>

        # Set DSCP for matched traffic.
        dscp: <int; 0-63>

        # Prefer paths with lowest hop-count.
        # Only applicable for `wan_mode: "cv-pathfinder"`.
        lowest_hop_count: <bool; default=False>
        constraints:

          # Jitter requirement for this load balance policy in milliseconds.
          jitter: <int; 0-10000>

          # One way delay requirement for this load balance policy in milliseconds.
          latency: <int; 0-10000>

          # Loss Rate requirement in percentage for this load balance policy.
          # Value between 0.00 and 100.00.
          loss_rate: <str>
        path_groups: # >=1 items

            # List of path-group names.
          - names: # >=1 items; required
              - <str>

            # Valid values are 1-65535 | "preferred" | "alternate".
            #
            # "preferred" is converted to priority 1.
            # "alternate" is converted to priority 2.
            #
            # If not set, each path-group in `names` will be attributed its `default_preference`.
            preference: <str>
        internet_exit:

          # PREVIEW: This key is in preview mode.
          #
          # Internet-exit policy name associated with this virtual_topology.
          # The policy must be defined under `cv_pathfinder_internet_exit_policies`.
          policy: <str>

      # List of virtual toplogies policies.
      #
      # For AutoVPN, each item in the list creates:
      #   * one policy with:
      #       * one `match` entry per `application_virtual_topologies` item
      #         they are indexed using `10 * <list_index>` where `list_index` starts at `1`.
      #       * one `default-match`
      #   * one load-balance policy per `application_virtual_topologies` and one for the `default_virtual_topology`.
      #   * if the policy is associated with the default VRF, a special control-plane rule is injected
      #     in the policy with index `1` referring to a control-plane load-balance policy as defined under
      #     `control_plane_virtual_topology` or if not set, the default one.
      #
      # For CV Pathfinder, each item in the list creates:
      #   * one policy with:
      #       * one `match` entry per `application_virtual_topologies` item ordered as in the data.
      #       * one last match entry for the `default` application-profile using `default_virtual_topology` information.
      #   * one profile per `application_virtual_topologies` item.
      #   * one profile for the `default_virtual_topology`.
      #   * one load-balance policy per `application_virtual_topologies`.
      #   * one load_balance policy for the `default_virtual_topology`.
      #   * if the policy is associated with the default VRF, a special control-plane profile is configured
      #     and injected first in the policy assigned to the `default` VRF. This profile points to a
      #     control-plane load-balance policy as defined under `control_plane_virtual_topology` or if not set, the default one.
      policies:

          # Name of the AVT policy.
        - name: <str; required; unique>

          # List of application specific virtual topologies.
          application_virtual_topologies:

              # The application profile to use for this virtual topology. It must be a defined `application_classification.application_profile`.
            - application_profile: <str; required; unique>

              # Optional name, if not set `<policy_name>-<application_profile>` is used.
              name: <str>

              # ID of the AVT in each VRFs. ID must be unique across all virtual topologies in a policy.
              # ID 1 is reserved for the default_virtual_toplogy.
              # ID 254 is reserved for the control_plane_virtual_topology.
              #
              # `id` is required when `wan_mode` is 'cv-pathfinder'.
              id: <int; 2-253>

              # Set traffic-class for matched traffic.
              traffic_class: <int; 0-7>

              # Set DSCP for matched traffic.
              dscp: <int; 0-63>

              # Prefer paths with lowest hop-count.
              # Only applicable for `wan_mode: "cv-pathfinder"`.
              lowest_hop_count: <bool; default=False>
              constraints:

                # Jitter requirement for this load balance policy in milliseconds.
                jitter: <int; 0-10000>

                # One way delay requirement for this load balance policy in milliseconds.
                latency: <int; 0-10000>

                # Loss Rate requirement in percentage for this load balance policy.
                # Value between 0.00 and 100.00.
                loss_rate: <str>
              path_groups: # >=1 items

                  # List of path-group names.
                - names: # >=1 items; required
                    - <str>

                  # Valid values are 1-65535 | "preferred" | "alternate".
                  #
                  # "preferred" is converted to priority 1.
                  # "alternate" is converted to priority 2.
                  #
                  # If not set, each path-group in `names` will be attributed its `default_preference`.
                  preference: <str>
              internet_exit:

                # PREVIEW: This key is in preview mode.
                #
                # Internet-exit policy name associated with this virtual_topology.
                # The policy must be defined under `cv_pathfinder_internet_exit_policies`.
                policy: <str>

          # Default match for the policy.
          # If no default match should be configured, set `drop_unmatched` to `true`.
          # Otherwise, in CV Pathfinder mode, a default AVT profile will be configured with ID 1.
          default_virtual_topology: # required

            # Optional name, if not set `<policy_name>-DEFAULT` is used.
            name: <str>

            # When set, no `catch-all` match is configured for the policy and unmatched traffic is dropped.
            drop_unmatched: <bool; default=False>

            # Set traffic-class for matched traffic.
            traffic_class: <int; 0-7>

            # Set DSCP for matched traffic.
            dscp: <int; 0-63>

            # Prefer paths with lowest hop-count.
            # Only applicable for `wan_mode: "cv-pathfinder"`.
            lowest_hop_count: <bool; default=False>
            constraints:

              # Jitter requirement for this load balance policy in milliseconds.
              jitter: <int; 0-10000>

              # One way delay requirement for this load balance policy in milliseconds.
              latency: <int; 0-10000>

              # Loss Rate requirement in percentage for this load balance policy.
              # Value between 0.00 and 100.00.
              loss_rate: <str>
            path_groups: # >=1 items

                # List of path-group names.
              - names: # >=1 items; required
                  - <str>

                # Valid values are 1-65535 | "preferred" | "alternate".
                #
                # "preferred" is converted to priority 1.
                # "alternate" is converted to priority 2.
                #
                # If not set, each path-group in `names` will be attributed its `default_preference`.
                preference: <str>
            internet_exit:

              # PREVIEW: This key is in preview mode.
              #
              # Internet-exit policy name associated with this virtual_topology.
              # The policy must be defined under `cv_pathfinder_internet_exit_policies`.
              policy: <str>
    ```
