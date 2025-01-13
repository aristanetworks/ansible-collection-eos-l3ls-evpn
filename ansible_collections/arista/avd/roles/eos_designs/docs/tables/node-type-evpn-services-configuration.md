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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_services_l2_only</samp>](## "<node_type_keys.key>.defaults.evpn_services_l2_only") | Boolean |  | `False` |  | Possibility to prevent configuration of Tenant VRFs and SVIs.<br>Override node definition "network_services_l3" from node_type_keys.<br>This allows support for centralized routing.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;filter</samp>](## "<node_type_keys.key>.defaults.filter") | Dictionary |  |  |  | Filter L3 and L2 network services based on tenant and tags (and operation filter).<br>If filter is not defined it will default to all.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenants</samp>](## "<node_type_keys.key>.defaults.filter.tenants") | List, items: String |  | `['all']` |  | Limit configured Network Services to those defined under these Tenants. Set to ['all'] for all Tenants (default).<br>This list also limits Tenants included by `always_include_vrfs_in_tenants`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.defaults.filter.tenants.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "<node_type_keys.key>.defaults.filter.tags") | List, items: String |  | `['all']` |  | Limit configured VLANs to those matching the given tags. Set to ['all'] for all VLANs (default). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.defaults.filter.tags.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allow_vrfs</samp>](## "<node_type_keys.key>.defaults.filter.allow_vrfs") | List, items: String |  | `['all']` |  | Limit configured Network Services to those defined under these VRFs. Set to ['all'] for all VRFs (default).<br>This list also limits VRFs included by `always_include_vrfs_in_tenants`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.defaults.filter.allow_vrfs.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;deny_vrfs</samp>](## "<node_type_keys.key>.defaults.filter.deny_vrfs") | List, items: String |  | `['all']` |  | Prevent configuration of Network Services defined under these VRFs.<br>This list prevents the given VRFs to be included by any other filtering mechanism. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.defaults.filter.deny_vrfs.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_include_vrfs_in_tenants</samp>](## "<node_type_keys.key>.defaults.filter.always_include_vrfs_in_tenants") | List, items: String |  |  |  | List of tenants where VRFs will be configured even if VLANs are not included in tags.<br>Useful for L3 "border" leaf.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.defaults.filter.always_include_vrfs_in_tenants.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;only_vlans_in_use</samp>](## "<node_type_keys.key>.defaults.filter.only_vlans_in_use") | Boolean |  | `False` |  | Only configure VLANs, SVIs, VRFs in use by connected endpoints or downstream L2 switches.<br>Note! This feature only considers configuration managed by eos_designs.<br>This excludes structured_config, custom_structured_configuration_, raw_eos_cli, eos_cli, custom templates, configlets etc.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "<node_type_keys.key>.defaults.igmp_snooping_enabled") | Boolean |  |  |  | Activate or deactivate IGMP snooping on device level. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_services_l2_only</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].evpn_services_l2_only") | Boolean |  | `False` |  | Possibility to prevent configuration of Tenant VRFs and SVIs.<br>Override node definition "network_services_l3" from node_type_keys.<br>This allows support for centralized routing.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filter</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].filter") | Dictionary |  |  |  | Filter L3 and L2 network services based on tenant and tags (and operation filter).<br>If filter is not defined it will default to all.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenants</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].filter.tenants") | List, items: String |  | `['all']` |  | Limit configured Network Services to those defined under these Tenants. Set to ['all'] for all Tenants (default).<br>This list also limits Tenants included by `always_include_vrfs_in_tenants`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].filter.tenants.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].filter.tags") | List, items: String |  | `['all']` |  | Limit configured VLANs to those matching the given tags. Set to ['all'] for all VLANs (default). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].filter.tags.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allow_vrfs</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].filter.allow_vrfs") | List, items: String |  | `['all']` |  | Limit configured Network Services to those defined under these VRFs. Set to ['all'] for all VRFs (default).<br>This list also limits VRFs included by `always_include_vrfs_in_tenants`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].filter.allow_vrfs.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;deny_vrfs</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].filter.deny_vrfs") | List, items: String |  | `['all']` |  | Prevent configuration of Network Services defined under these VRFs.<br>This list prevents the given VRFs to be included by any other filtering mechanism. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].filter.deny_vrfs.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_include_vrfs_in_tenants</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].filter.always_include_vrfs_in_tenants") | List, items: String |  |  |  | List of tenants where VRFs will be configured even if VLANs are not included in tags.<br>Useful for L3 "border" leaf.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].filter.always_include_vrfs_in_tenants.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;only_vlans_in_use</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].filter.only_vlans_in_use") | Boolean |  | `False` |  | Only configure VLANs, SVIs, VRFs in use by connected endpoints or downstream L2 switches.<br>Note! This feature only considers configuration managed by eos_designs.<br>This excludes structured_config, custom_structured_configuration_, raw_eos_cli, eos_cli, custom templates, configlets etc.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].igmp_snooping_enabled") | Boolean |  |  |  | Activate or deactivate IGMP snooping on device level. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_services_l2_only</samp>](## "<node_type_keys.key>.node_groups.[].evpn_services_l2_only") | Boolean |  | `False` |  | Possibility to prevent configuration of Tenant VRFs and SVIs.<br>Override node definition "network_services_l3" from node_type_keys.<br>This allows support for centralized routing.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filter</samp>](## "<node_type_keys.key>.node_groups.[].filter") | Dictionary |  |  |  | Filter L3 and L2 network services based on tenant and tags (and operation filter).<br>If filter is not defined it will default to all.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenants</samp>](## "<node_type_keys.key>.node_groups.[].filter.tenants") | List, items: String |  | `['all']` |  | Limit configured Network Services to those defined under these Tenants. Set to ['all'] for all Tenants (default).<br>This list also limits Tenants included by `always_include_vrfs_in_tenants`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].filter.tenants.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "<node_type_keys.key>.node_groups.[].filter.tags") | List, items: String |  | `['all']` |  | Limit configured VLANs to those matching the given tags. Set to ['all'] for all VLANs (default). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].filter.tags.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allow_vrfs</samp>](## "<node_type_keys.key>.node_groups.[].filter.allow_vrfs") | List, items: String |  | `['all']` |  | Limit configured Network Services to those defined under these VRFs. Set to ['all'] for all VRFs (default).<br>This list also limits VRFs included by `always_include_vrfs_in_tenants`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].filter.allow_vrfs.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;deny_vrfs</samp>](## "<node_type_keys.key>.node_groups.[].filter.deny_vrfs") | List, items: String |  | `['all']` |  | Prevent configuration of Network Services defined under these VRFs.<br>This list prevents the given VRFs to be included by any other filtering mechanism. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].filter.deny_vrfs.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_include_vrfs_in_tenants</samp>](## "<node_type_keys.key>.node_groups.[].filter.always_include_vrfs_in_tenants") | List, items: String |  |  |  | List of tenants where VRFs will be configured even if VLANs are not included in tags.<br>Useful for L3 "border" leaf.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.node_groups.[].filter.always_include_vrfs_in_tenants.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;only_vlans_in_use</samp>](## "<node_type_keys.key>.node_groups.[].filter.only_vlans_in_use") | Boolean |  | `False` |  | Only configure VLANs, SVIs, VRFs in use by connected endpoints or downstream L2 switches.<br>Note! This feature only considers configuration managed by eos_designs.<br>This excludes structured_config, custom_structured_configuration_, raw_eos_cli, eos_cli, custom templates, configlets etc.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "<node_type_keys.key>.node_groups.[].igmp_snooping_enabled") | Boolean |  |  |  | Activate or deactivate IGMP snooping on device level. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_services_l2_only</samp>](## "<node_type_keys.key>.nodes.[].evpn_services_l2_only") | Boolean |  | `False` |  | Possibility to prevent configuration of Tenant VRFs and SVIs.<br>Override node definition "network_services_l3" from node_type_keys.<br>This allows support for centralized routing.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;filter</samp>](## "<node_type_keys.key>.nodes.[].filter") | Dictionary |  |  |  | Filter L3 and L2 network services based on tenant and tags (and operation filter).<br>If filter is not defined it will default to all.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tenants</samp>](## "<node_type_keys.key>.nodes.[].filter.tenants") | List, items: String |  | `['all']` |  | Limit configured Network Services to those defined under these Tenants. Set to ['all'] for all Tenants (default).<br>This list also limits Tenants included by `always_include_vrfs_in_tenants`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.nodes.[].filter.tenants.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "<node_type_keys.key>.nodes.[].filter.tags") | List, items: String |  | `['all']` |  | Limit configured VLANs to those matching the given tags. Set to ['all'] for all VLANs (default). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.nodes.[].filter.tags.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allow_vrfs</samp>](## "<node_type_keys.key>.nodes.[].filter.allow_vrfs") | List, items: String |  | `['all']` |  | Limit configured Network Services to those defined under these VRFs. Set to ['all'] for all VRFs (default).<br>This list also limits VRFs included by `always_include_vrfs_in_tenants`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.nodes.[].filter.allow_vrfs.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;deny_vrfs</samp>](## "<node_type_keys.key>.nodes.[].filter.deny_vrfs") | List, items: String |  | `['all']` |  | Prevent configuration of Network Services defined under these VRFs.<br>This list prevents the given VRFs to be included by any other filtering mechanism. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.nodes.[].filter.deny_vrfs.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_include_vrfs_in_tenants</samp>](## "<node_type_keys.key>.nodes.[].filter.always_include_vrfs_in_tenants") | List, items: String |  |  |  | List of tenants where VRFs will be configured even if VLANs are not included in tags.<br>Useful for L3 "border" leaf.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<node_type_keys.key>.nodes.[].filter.always_include_vrfs_in_tenants.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;only_vlans_in_use</samp>](## "<node_type_keys.key>.nodes.[].filter.only_vlans_in_use") | Boolean |  | `False` |  | Only configure VLANs, SVIs, VRFs in use by connected endpoints or downstream L2 switches.<br>Note! This feature only considers configuration managed by eos_designs.<br>This excludes structured_config, custom_structured_configuration_, raw_eos_cli, eos_cli, custom templates, configlets etc.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;igmp_snooping_enabled</samp>](## "<node_type_keys.key>.nodes.[].igmp_snooping_enabled") | Boolean |  |  |  | Activate or deactivate IGMP snooping on device level. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:

        # Possibility to prevent configuration of Tenant VRFs and SVIs.
        # Override node definition "network_services_l3" from node_type_keys.
        # This allows support for centralized routing.
        evpn_services_l2_only: <bool; default=False>

        # Filter L3 and L2 network services based on tenant and tags (and operation filter).
        # If filter is not defined it will default to all.
        filter:

          # Limit configured Network Services to those defined under these Tenants. Set to ['all'] for all Tenants (default).
          # This list also limits Tenants included by `always_include_vrfs_in_tenants`.
          tenants: # default=['all']
            - <str>

          # Limit configured VLANs to those matching the given tags. Set to ['all'] for all VLANs (default).
          tags: # default=['all']
            - <str>

          # Limit configured Network Services to those defined under these VRFs. Set to ['all'] for all VRFs (default).
          # This list also limits VRFs included by `always_include_vrfs_in_tenants`.
          allow_vrfs: # default=['all']
            - <str>

          # Prevent configuration of Network Services defined under these VRFs.
          # This list prevents the given VRFs to be included by any other filtering mechanism.
          deny_vrfs: # default=['all']
            - <str>

          # List of tenants where VRFs will be configured even if VLANs are not included in tags.
          # Useful for L3 "border" leaf.
          always_include_vrfs_in_tenants:
            - <str>

          # Only configure VLANs, SVIs, VRFs in use by connected endpoints or downstream L2 switches.
          # Note! This feature only considers configuration managed by eos_designs.
          # This excludes structured_config, custom_structured_configuration_, raw_eos_cli, eos_cli, custom templates, configlets etc.
          only_vlans_in_use: <bool; default=False>

        # Activate or deactivate IGMP snooping on device level.
        igmp_snooping_enabled: <bool>

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>

              # Possibility to prevent configuration of Tenant VRFs and SVIs.
              # Override node definition "network_services_l3" from node_type_keys.
              # This allows support for centralized routing.
              evpn_services_l2_only: <bool; default=False>

              # Filter L3 and L2 network services based on tenant and tags (and operation filter).
              # If filter is not defined it will default to all.
              filter:

                # Limit configured Network Services to those defined under these Tenants. Set to ['all'] for all Tenants (default).
                # This list also limits Tenants included by `always_include_vrfs_in_tenants`.
                tenants: # default=['all']
                  - <str>

                # Limit configured VLANs to those matching the given tags. Set to ['all'] for all VLANs (default).
                tags: # default=['all']
                  - <str>

                # Limit configured Network Services to those defined under these VRFs. Set to ['all'] for all VRFs (default).
                # This list also limits VRFs included by `always_include_vrfs_in_tenants`.
                allow_vrfs: # default=['all']
                  - <str>

                # Prevent configuration of Network Services defined under these VRFs.
                # This list prevents the given VRFs to be included by any other filtering mechanism.
                deny_vrfs: # default=['all']
                  - <str>

                # List of tenants where VRFs will be configured even if VLANs are not included in tags.
                # Useful for L3 "border" leaf.
                always_include_vrfs_in_tenants:
                  - <str>

                # Only configure VLANs, SVIs, VRFs in use by connected endpoints or downstream L2 switches.
                # Note! This feature only considers configuration managed by eos_designs.
                # This excludes structured_config, custom_structured_configuration_, raw_eos_cli, eos_cli, custom templates, configlets etc.
                only_vlans_in_use: <bool; default=False>

              # Activate or deactivate IGMP snooping on device level.
              igmp_snooping_enabled: <bool>

          # Possibility to prevent configuration of Tenant VRFs and SVIs.
          # Override node definition "network_services_l3" from node_type_keys.
          # This allows support for centralized routing.
          evpn_services_l2_only: <bool; default=False>

          # Filter L3 and L2 network services based on tenant and tags (and operation filter).
          # If filter is not defined it will default to all.
          filter:

            # Limit configured Network Services to those defined under these Tenants. Set to ['all'] for all Tenants (default).
            # This list also limits Tenants included by `always_include_vrfs_in_tenants`.
            tenants: # default=['all']
              - <str>

            # Limit configured VLANs to those matching the given tags. Set to ['all'] for all VLANs (default).
            tags: # default=['all']
              - <str>

            # Limit configured Network Services to those defined under these VRFs. Set to ['all'] for all VRFs (default).
            # This list also limits VRFs included by `always_include_vrfs_in_tenants`.
            allow_vrfs: # default=['all']
              - <str>

            # Prevent configuration of Network Services defined under these VRFs.
            # This list prevents the given VRFs to be included by any other filtering mechanism.
            deny_vrfs: # default=['all']
              - <str>

            # List of tenants where VRFs will be configured even if VLANs are not included in tags.
            # Useful for L3 "border" leaf.
            always_include_vrfs_in_tenants:
              - <str>

            # Only configure VLANs, SVIs, VRFs in use by connected endpoints or downstream L2 switches.
            # Note! This feature only considers configuration managed by eos_designs.
            # This excludes structured_config, custom_structured_configuration_, raw_eos_cli, eos_cli, custom templates, configlets etc.
            only_vlans_in_use: <bool; default=False>

          # Activate or deactivate IGMP snooping on device level.
          igmp_snooping_enabled: <bool>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>

          # Possibility to prevent configuration of Tenant VRFs and SVIs.
          # Override node definition "network_services_l3" from node_type_keys.
          # This allows support for centralized routing.
          evpn_services_l2_only: <bool; default=False>

          # Filter L3 and L2 network services based on tenant and tags (and operation filter).
          # If filter is not defined it will default to all.
          filter:

            # Limit configured Network Services to those defined under these Tenants. Set to ['all'] for all Tenants (default).
            # This list also limits Tenants included by `always_include_vrfs_in_tenants`.
            tenants: # default=['all']
              - <str>

            # Limit configured VLANs to those matching the given tags. Set to ['all'] for all VLANs (default).
            tags: # default=['all']
              - <str>

            # Limit configured Network Services to those defined under these VRFs. Set to ['all'] for all VRFs (default).
            # This list also limits VRFs included by `always_include_vrfs_in_tenants`.
            allow_vrfs: # default=['all']
              - <str>

            # Prevent configuration of Network Services defined under these VRFs.
            # This list prevents the given VRFs to be included by any other filtering mechanism.
            deny_vrfs: # default=['all']
              - <str>

            # List of tenants where VRFs will be configured even if VLANs are not included in tags.
            # Useful for L3 "border" leaf.
            always_include_vrfs_in_tenants:
              - <str>

            # Only configure VLANs, SVIs, VRFs in use by connected endpoints or downstream L2 switches.
            # Note! This feature only considers configuration managed by eos_designs.
            # This excludes structured_config, custom_structured_configuration_, raw_eos_cli, eos_cli, custom templates, configlets etc.
            only_vlans_in_use: <bool; default=False>

          # Activate or deactivate IGMP snooping on device level.
          igmp_snooping_enabled: <bool>
    ```
