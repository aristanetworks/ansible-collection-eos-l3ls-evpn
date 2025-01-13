<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>is_deployed</samp>](## "is_deployed") | Boolean |  | `True` |  | If the device is already deployed in the fabric.<br>When set to false, interfaces toward this device may be shutdown depending on the `shutdown_interfaces_towards_undeployed_peers` setting.<br>Furthermore `eos_config_deploy_cvp` will not attempt to move or apply configurations to the device.<br> |

=== "YAML"

    ```yaml
    # If the device is already deployed in the fabric.
    # When set to false, interfaces toward this device may be shutdown depending on the `shutdown_interfaces_towards_undeployed_peers` setting.
    # Furthermore `eos_config_deploy_cvp` will not attempt to move or apply configurations to the device.
    is_deployed: <bool; default=True>
    ```
