<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>transceiver_qsfp_default_mode_4x10</samp>](## "transceiver_qsfp_default_mode_4x10") | Boolean |  | `True` |  | On all front panel ports which support this feature, the following global configuration command changes the QSFP mode from 40G to 4x10G (default). When set to false the command reverts the default QSFP mode back to 40G.<br> |

=== "YAML"

    ```yaml
    # On all front panel ports which support this feature, the following global configuration command changes the QSFP mode from 40G to 4x10G (default). When set to false the command reverts the default QSFP mode back to 40G.
    transceiver_qsfp_default_mode_4x10: <bool; default=True>
    ```
