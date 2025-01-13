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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_vrf_vni_base</samp>](## "<network_services_keys.name>.[].mac_vrf_vni_base") | Integer |  |  | Min: 0<br>Max: 16770000 | Base number for MAC VRF VXLAN Network Identifier (required with VXLAN).<br>VXLAN VNI is derived from the base number with simple addition.<br>i.e. mac_vrf_vni_base = 10000, svi 100 = VNI 10100, svi 300 = VNI 10300.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_vrf_id_base</samp>](## "<network_services_keys.name>.[].mac_vrf_id_base") | Integer |  |  | Min: 0<br>Max: 16770000 | If not set, "mac_vrf_vni_base" will be used.<br>Base number for MAC VRF RD/RT ID (Required unless mac_vrf_vni_base is set)<br>ID is derived from the base number with simple addition.<br>i.e. mac_vrf_id_base = 10000, svi 100 = RD/RT 10100, svi 300 = RD/RT 10300.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vlan_aware_bundle_number_base</samp>](## "<network_services_keys.name>.[].vlan_aware_bundle_number_base") | Integer |  | `0` |  | Base number for VLAN aware bundle RD/RT.<br>The "Assigned Number" part of RD/RT is derived from vrf_vni + vlan_aware_bundle_number_base.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_vlan_bundle</samp>](## "<network_services_keys.name>.[].evpn_vlan_bundle") | String |  |  |  | Enable `evpn_vlan_bundle` for all l2vlans and SVIs under the tenant. This `evpn_vlan_bundle` should be present in `evpn_vlan_bundles`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;evpn_l2_multi_domain</samp>](## "<network_services_keys.name>.[].evpn_l2_multi_domain") | Boolean |  | `True` |  | Explicitly extend all VLANs/VLAN-Aware Bundles inside the tenant to remote EVPN domains. |

=== "YAML"

    ```yaml
    <network_services_keys.name>:

        # Specify a tenant name.
        # Tenant provide a construct to group L3 VRFs and L2 VLANs.
        # Networks services can be filtered by tenant name.
      - name: <str; required; unique>

        # Base number for MAC VRF VXLAN Network Identifier (required with VXLAN).
        # VXLAN VNI is derived from the base number with simple addition.
        # i.e. mac_vrf_vni_base = 10000, svi 100 = VNI 10100, svi 300 = VNI 10300.
        mac_vrf_vni_base: <int; 0-16770000>

        # If not set, "mac_vrf_vni_base" will be used.
        # Base number for MAC VRF RD/RT ID (Required unless mac_vrf_vni_base is set)
        # ID is derived from the base number with simple addition.
        # i.e. mac_vrf_id_base = 10000, svi 100 = RD/RT 10100, svi 300 = RD/RT 10300.
        mac_vrf_id_base: <int; 0-16770000>

        # Base number for VLAN aware bundle RD/RT.
        # The "Assigned Number" part of RD/RT is derived from vrf_vni + vlan_aware_bundle_number_base.
        vlan_aware_bundle_number_base: <int; default=0>

        # Enable `evpn_vlan_bundle` for all l2vlans and SVIs under the tenant. This `evpn_vlan_bundle` should be present in `evpn_vlan_bundles`.
        evpn_vlan_bundle: <str>

        # Explicitly extend all VLANs/VLAN-Aware Bundles inside the tenant to remote EVPN domains.
        evpn_l2_multi_domain: <bool; default=True>
    ```
