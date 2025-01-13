<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>virtual_source_nat_vrfs</samp>](## "virtual_source_nat_vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "virtual_source_nat_vrfs.[].name") | String | Required, Unique |  |  | VRF Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "virtual_source_nat_vrfs.[].ip_address") | String |  |  |  | IPv4 Address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "virtual_source_nat_vrfs.[].ipv6_address") | String |  |  |  | IPv6 Address. |

=== "YAML"

    ```yaml
    virtual_source_nat_vrfs:

        # VRF Name.
      - name: <str; required; unique>

        # IPv4 Address.
        ip_address: <str>

        # IPv6 Address.
        ipv6_address: <str>
    ```
