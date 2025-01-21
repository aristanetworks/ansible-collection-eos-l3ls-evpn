<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>generate_default_config</samp>](## "generate_default_config") <span style="color:red">deprecated</span> | Boolean |  | `False` |  | The `generate_default_config` knob allows to omit default EOS configuration.<br>This can be useful when leveraging `eos_cli_config_gen` to generate configlets with CloudVision.<br><br>The following commands will be omitted when `generate_default_config` is set to `false`:<br><br>- RANCID Content Type<br>- Hostname (even if `hostname` variable is not set. Then the hostname is picked up from `inventory_hostname`)<br>- Default configuration for `aaa`<br>- Default configuration for `enable password`<br>- Transceiver qsfp default mode<br>- End of configuration delimiter<br><span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. See [here](https://avd.arista.com/5.x/docs/porting-guides/5.x.x.html#default-eos-configuration-is-no-longer-automatically-generated) for details.</span> |

=== "YAML"

    ```yaml
    # The `generate_default_config` knob allows to omit default EOS configuration.
    # This can be useful when leveraging `eos_cli_config_gen` to generate configlets with CloudVision.
    #
    # The following commands will be omitted when `generate_default_config` is set to `false`:
    #
    # - RANCID Content Type
    # - Hostname (even if `hostname` variable is not set. Then the hostname is picked up from `inventory_hostname`)
    # - Default configuration for `aaa`
    # - Default configuration for `enable password`
    # - Transceiver qsfp default mode
    # - End of configuration delimiter
    # This key is deprecated.
    # Support will be removed in AVD version 6.0.0.
    # See [here](https://avd.arista.com/5.x/docs/porting-guides/5.x.x.html#default-eos-configuration-is-no-longer-automatically-generated) for details.
    generate_default_config: <bool; default=False>
    ```
