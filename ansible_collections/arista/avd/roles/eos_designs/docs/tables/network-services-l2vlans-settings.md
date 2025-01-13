<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;network_services_keys.name&gt;</samp>](## "<network_services_keys.name>") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "<network_services_keys.name>.[].name") | String | Required, Unique |  |  | Specify a tenant name.<br>Tenant provide a construct to group L3 VRFs and L2 VLANs.<br>Networks services can be filtered by tenant name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l2vlans</samp>](## "<network_services_keys.name>.[].l2vlans") | List, items: Dictionary |  |  |  | Define L2 network services organized by vlan id. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "<network_services_keys.name>.[].l2vlans.[].id") | Integer | Required |  | Min: 1<br>Max: 4094 | VLAN ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni_override</samp>](## "<network_services_keys.name>.[].l2vlans.[].vni_override") | Integer |  |  | Min: 1<br>Max: 16777215 | By default the VNI will be derived from mac_vrf_vni_base.<br>The vni_override, allows to override this value and statically define it.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rt_override</samp>](## "<network_services_keys.name>.[].l2vlans.[].rt_override") | String |  |  |  | By default the MAC VRF RT will be derived from mac_vrf_id_base + vlan_id.<br>The rt_override allows us to override this value and statically define it.<br>rt_override will default to vni_override if set.<br><br>rt_override supports two formats:<br>  - A single number which will be used in the RT fields instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rt_type' for details).<br>  - A full RT string with colon separator which will override the full RT.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rd_override</samp>](## "<network_services_keys.name>.[].l2vlans.[].rd_override") | String |  |  |  | By default the MAC VRF RD will be derived from mac_vrf_id_base + vlan_id.<br>The rt_override allows us to override this value and statically define it.<br>rd_override will default to rt_override or vni_override if set.<br><br>rd_override supports two formats:<br>  - A single number which will be used in the RD assigned number field instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rd_type' for details).<br>  - A full RD string with colon separator which will override the full RD.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<network_services_keys.name>.[].l2vlans.[].name") | String | Required |  |  | VLAN name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "<network_services_keys.name>.[].l2vlans.[].tags") | List, items: String |  | `['all']` |  | Tags leveraged for networks services filtering.<br>Tags are matched against filter.tags defined under node type settings.<br>Tags are also matched against the node_group name under node type settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].l2vlans.[].tags.[]") | String |  | `all` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "<network_services_keys.name>.[].l2vlans.[].vxlan") | Boolean |  | `True` |  | Extend this L2VLAN over VXLAN. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;spanning_tree_priority</samp>](## "<network_services_keys.name>.[].l2vlans.[].spanning_tree_priority") | Integer |  |  |  | Setting spanning-tree priority per VLAN is only supported with `spanning_tree_mode: rapid-pvst` under node type settings.<br>The default priority for rapid-PVST is set under the node type settings with `spanning_tree_priority` (default=32768). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_vlan_bundle</samp>](## "<network_services_keys.name>.[].l2vlans.[].evpn_vlan_bundle") | String |  |  |  | Name of a bundle defined under 'evpn_vlan_bundles' to inherit configuration.<br>This setting overrides "evpn_vlan_bundle" set at tenant level.<br>The common option "evpn_vlan_aware_bundles" is disregarded for this option.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;trunk_groups</samp>](## "<network_services_keys.name>.[].l2vlans.[].trunk_groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].l2vlans.[].trunk_groups.[]") | String |  |  |  | Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group.<br>Requires enable_trunk_groups: true.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multi_domain</samp>](## "<network_services_keys.name>.[].l2vlans.[].evpn_l2_multi_domain") | Boolean |  |  |  | Explicitly extend this VLAN to remote EVPN domains.<br>Overrides `<network_services_key>[].evpn_l2_multi_domain`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "<network_services_keys.name>.[].l2vlans.[].bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<network_services_keys.name>.[].l2vlans.[].bgp.structured_config") | Dictionary |  |  |  | Custom structured config added under router_bgp.vlans.[id=<vlan>] for eos_cli_config_gen.<br>This configuration will not be applied to vlan aware bundles.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "<network_services_keys.name>.[].l2vlans.[].bgp.raw_eos_cli") | String |  |  |  | EOS cli commands rendered on router_bgp.vlans.<br>This configuration will not be applied to vlan aware bundles.<br> |

=== "YAML"

    ```yaml
    <network_services_keys.name>:

        # Specify a tenant name.
        # Tenant provide a construct to group L3 VRFs and L2 VLANs.
        # Networks services can be filtered by tenant name.
      - name: <str; required; unique>

        # Define L2 network services organized by vlan id.
        l2vlans:

            # VLAN ID.
          - id: <int; 1-4094; required>

            # By default the VNI will be derived from mac_vrf_vni_base.
            # The vni_override, allows to override this value and statically define it.
            vni_override: <int; 1-16777215>

            # By default the MAC VRF RT will be derived from mac_vrf_id_base + vlan_id.
            # The rt_override allows us to override this value and statically define it.
            # rt_override will default to vni_override if set.
            #
            # rt_override supports two formats:
            #   - A single number which will be used in the RT fields instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rt_type' for details).
            #   - A full RT string with colon separator which will override the full RT.
            rt_override: <str>

            # By default the MAC VRF RD will be derived from mac_vrf_id_base + vlan_id.
            # The rt_override allows us to override this value and statically define it.
            # rd_override will default to rt_override or vni_override if set.
            #
            # rd_override supports two formats:
            #   - A single number which will be used in the RD assigned number field instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rd_type' for details).
            #   - A full RD string with colon separator which will override the full RD.
            rd_override: <str>

            # VLAN name.
            name: <str; required>

            # Tags leveraged for networks services filtering.
            # Tags are matched against filter.tags defined under node type settings.
            # Tags are also matched against the node_group name under node type settings.
            tags: # default=['all']
              - <str; default="all">

            # Extend this L2VLAN over VXLAN.
            vxlan: <bool; default=True>

            # Setting spanning-tree priority per VLAN is only supported with `spanning_tree_mode: rapid-pvst` under node type settings.
            # The default priority for rapid-PVST is set under the node type settings with `spanning_tree_priority` (default=32768).
            spanning_tree_priority: <int>

            # Name of a bundle defined under 'evpn_vlan_bundles' to inherit configuration.
            # This setting overrides "evpn_vlan_bundle" set at tenant level.
            # The common option "evpn_vlan_aware_bundles" is disregarded for this option.
            evpn_vlan_bundle: <str>
            trunk_groups:

                # Trunk groups are used for limiting vlans to trunk ports assigned to the same trunk group.
                # Requires enable_trunk_groups: true.
              - <str>

            # Explicitly extend this VLAN to remote EVPN domains.
            # Overrides `<network_services_key>[].evpn_l2_multi_domain`.
            evpn_l2_multi_domain: <bool>
            bgp:

              # Custom structured config added under router_bgp.vlans.[id=<vlan>] for eos_cli_config_gen.
              # This configuration will not be applied to vlan aware bundles.
              structured_config: <dict>

              # EOS cli commands rendered on router_bgp.vlans.
              # This configuration will not be applied to vlan aware bundles.
              raw_eos_cli: <str>
    ```
