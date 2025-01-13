<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>static_routes</samp>](## "static_routes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;vrf</samp>](## "static_routes.[].vrf") | String |  |  |  | VRF Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;destination_address_prefix</samp>](## "static_routes.[].destination_address_prefix") | String |  |  |  | IPv4_network/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "static_routes.[].interface") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;gateway</samp>](## "static_routes.[].gateway") | String |  |  |  | IPv4 Address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;track_bfd</samp>](## "static_routes.[].track_bfd") | Boolean |  |  |  | Track next-hop using BFD. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "static_routes.[].distance") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tag</samp>](## "static_routes.[].tag") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "static_routes.[].name") | String |  |  |  | Description. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;metric</samp>](## "static_routes.[].metric") | Integer |  |  | Min: 0<br>Max: 4294967295 |  |

=== "YAML"

    ```yaml
    static_routes:

        # VRF Name.
      - vrf: <str>

        # IPv4_network/Mask.
        destination_address_prefix: <str>
        interface: <str>

        # IPv4 Address.
        gateway: <str>

        # Track next-hop using BFD.
        track_bfd: <bool>
        distance: <int; 1-255>
        tag: <int; 0-4294967295>

        # Description.
        name: <str>
        metric: <int; 0-4294967295>
    ```
