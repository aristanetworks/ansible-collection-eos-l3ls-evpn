<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>vrfs</samp>](## "vrfs") | List, items: Dictionary |  |  |  | These keys are ignored if the name of the vrf is 'default'.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "vrfs.[].name") | String | Required, Unique |  |  | VRF Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "vrfs.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_routing</samp>](## "vrfs.[].ip_routing") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_routing</samp>](## "vrfs.[].ipv6_routing") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_routing_ipv6_interfaces</samp>](## "vrfs.[].ip_routing_ipv6_interfaces") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tenant</samp>](## "vrfs.[].tenant") | String |  |  |  | Key only used for documentation or validation purposes. |

=== "YAML"

    ```yaml
    # These keys are ignored if the name of the vrf is 'default'.
    vrfs:

        # VRF Name.
      - name: <str; required; unique>
        description: <str>
        ip_routing: <bool>
        ipv6_routing: <bool>
        ip_routing_ipv6_interfaces: <bool>

        # Key only used for documentation or validation purposes.
        tenant: <str>
    ```
