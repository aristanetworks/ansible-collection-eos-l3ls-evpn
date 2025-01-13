<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>new_network_services_bgp_vrf_config</samp>](## "new_network_services_bgp_vrf_config") <span style="color:red">removed</span> | Boolean |  | `True` |  | This key was used to generate BGP configuration for network services even when `evpn` is not in the address families for the node as well as the VRF.<br>This is now part of the default behavior so this key has been removed.<span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. See [here](https://avd.arista.com/5.x/docs/porting-guides/5.x.x.html#bgp-is-now-configured-for-network-services-vrfs-even-if-evpn-is-not-part-of-the-address-families) for details.</span> |

=== "YAML"

    ```yaml

    ```
