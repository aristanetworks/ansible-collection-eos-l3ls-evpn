<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>dc_name</samp>](## "dc_name") | String |  |  |  | DC Name is used in:<br>- Fabric Documentation (Optional, falls back to fabric_name)<br>- SNMP Location: `snmp_settings.location` (Optional)<br>- HER Overlay DC scoped flood lists: `overlay_her_flood_list_scope: dc` (Required)<br> |
    | [<samp>fabric_name</samp>](## "fabric_name") | String | Required |  |  | Fabric Name, required to match Ansible Group name covering all devices in the Fabric, **must** be an inventory group name. |
    | [<samp>pod_name</samp>](## "pod_name") | String |  |  |  | POD Name is used in:<br>- Fabric Documentation (Optional, falls back to dc_name and then to fabric_name)<br>- SNMP Location: `snmp_settings.location` (Optional)<br>- VRF Loopbacks: `vtep_diagnostic.loopback_ip_pools.pod` (Required)<br><br>Recommended to be common between Spines and Leafs within a POD (One l3ls topology).<br> |

=== "YAML"

    ```yaml
    # DC Name is used in:
    # - Fabric Documentation (Optional, falls back to fabric_name)
    # - SNMP Location: `snmp_settings.location` (Optional)
    # - HER Overlay DC scoped flood lists: `overlay_her_flood_list_scope: dc` (Required)
    dc_name: <str>

    # Fabric Name, required to match Ansible Group name covering all devices in the Fabric, **must** be an inventory group name.
    fabric_name: <str; required>

    # POD Name is used in:
    # - Fabric Documentation (Optional, falls back to dc_name and then to fabric_name)
    # - SNMP Location: `snmp_settings.location` (Optional)
    # - VRF Loopbacks: `vtep_diagnostic.loopback_ip_pools.pod` (Required)
    #
    # Recommended to be common between Spines and Leafs within a POD (One l3ls topology).
    pod_name: <str>
    ```
