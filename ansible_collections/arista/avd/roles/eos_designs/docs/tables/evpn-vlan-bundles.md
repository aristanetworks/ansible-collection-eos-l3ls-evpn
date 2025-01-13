<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>evpn_vlan_bundles</samp>](## "evpn_vlan_bundles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "evpn_vlan_bundles.[].name") | String | Required, Unique |  |  | Specify an EVPN vlan-aware-bundle name.<br>EVPN vlan-aware-bundles group VLANs and define common settings.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "evpn_vlan_bundles.[].id") | Integer | Required |  |  | "id" may be used for vlan-aware-bundle RD/RT ID so it should not overlap with l2vlan IDs which are not part of this bundle.<br>See "overlay_rd_type" and "overlay_rt_type" for details.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rt_override</samp>](## "evpn_vlan_bundles.[].rt_override") | String |  |  |  | By default the MAC VRF bundle RT will be derived from mac_vrf_id_base + bundle_id.<br>The rt_override allows us to override this value and statically define it.<br>rt_override will default to vni_override if set.<br><br>rt_override supports two formats:<br>  - A single number which will be used in the RT fields instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rt_type' for details).<br>  - A full RT string with colon separator which will override the full RT.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rd_override</samp>](## "evpn_vlan_bundles.[].rd_override") | String |  |  |  | By default the MAC VRF bundle RD will be derived from mac_vrf_id_base + bundle_id.<br>The rt_override allows us to override this value and statically define it.<br>rd_override will default to rt_override or vni_override if set.<br><br>rd_override supports two formats:<br>  - A single number which will be used in the RD assigned number field instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rd_type' for details).<br>  - A full RD string with colon separator which will override the full RD.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multi_domain</samp>](## "evpn_vlan_bundles.[].evpn_l2_multi_domain") | Boolean |  |  |  | Explicitly extend VLAN-Aware Bundle to remote EVPN domains.<br>Overrides `<network_services_key>.[].evpn_l2_multi_domain`.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bgp</samp>](## "evpn_vlan_bundles.[].bgp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "evpn_vlan_bundles.[].bgp.raw_eos_cli") | String |  |  |  | EOS cli commands rendered on router_bgp.vlans-aware-bundle.<br> |

=== "YAML"

    ```yaml
    evpn_vlan_bundles:

        # Specify an EVPN vlan-aware-bundle name.
        # EVPN vlan-aware-bundles group VLANs and define common settings.
      - name: <str; required; unique>

        # "id" may be used for vlan-aware-bundle RD/RT ID so it should not overlap with l2vlan IDs which are not part of this bundle.
        # See "overlay_rd_type" and "overlay_rt_type" for details.
        id: <int; required>

        # By default the MAC VRF bundle RT will be derived from mac_vrf_id_base + bundle_id.
        # The rt_override allows us to override this value and statically define it.
        # rt_override will default to vni_override if set.
        #
        # rt_override supports two formats:
        #   - A single number which will be used in the RT fields instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rt_type' for details).
        #   - A full RT string with colon separator which will override the full RT.
        rt_override: <str>

        # By default the MAC VRF bundle RD will be derived from mac_vrf_id_base + bundle_id.
        # The rt_override allows us to override this value and statically define it.
        # rd_override will default to rt_override or vni_override if set.
        #
        # rd_override supports two formats:
        #   - A single number which will be used in the RD assigned number field instead of mac_vrf_id/mac_vrf_vni (see 'overlay_rd_type' for details).
        #   - A full RD string with colon separator which will override the full RD.
        rd_override: <str>

        # Explicitly extend VLAN-Aware Bundle to remote EVPN domains.
        # Overrides `<network_services_key>.[].evpn_l2_multi_domain`.
        evpn_l2_multi_domain: <bool>
        bgp:

          # EOS cli commands rendered on router_bgp.vlans-aware-bundle.
          raw_eos_cli: <str>
    ```
