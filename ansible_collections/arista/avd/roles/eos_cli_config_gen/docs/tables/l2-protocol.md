<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>l2_protocol</samp>](## "l2_protocol") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;forwarding_profiles</samp>](## "l2_protocol.forwarding_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "l2_protocol.forwarding_profiles.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocols</samp>](## "l2_protocol.forwarding_profiles.[].protocols") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "l2_protocol.forwarding_profiles.[].protocols.[].name") | String | Required, Unique |  | Valid Values:<br>- <code>bfd per-link rfc-7130</code><br>- <code>e-lmi</code><br>- <code>isis</code><br>- <code>lacp</code><br>- <code>lldp</code><br>- <code>macsec</code><br>- <code>pause</code><br>- <code>stp</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;forward</samp>](## "l2_protocol.forwarding_profiles.[].protocols.[].forward") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tagged_forward</samp>](## "l2_protocol.forwarding_profiles.[].protocols.[].tagged_forward") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;untagged_forward</samp>](## "l2_protocol.forwarding_profiles.[].protocols.[].untagged_forward") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    l2_protocol:
      forwarding_profiles:
        - name: <str; required; unique>
          protocols:
            - name: <str; "bfd per-link rfc-7130" | "e-lmi" | "isis" | "lacp" | "lldp" | "macsec" | "pause" | "stp"; required; unique>
              forward: <bool>
              tagged_forward: <bool>
              untagged_forward: <bool>
    ```
