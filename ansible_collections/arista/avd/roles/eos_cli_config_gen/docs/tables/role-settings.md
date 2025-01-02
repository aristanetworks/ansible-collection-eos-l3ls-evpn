<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>eos_cli_config_gen_configuration</samp>](## "eos_cli_config_gen_configuration") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enable</samp>](## "eos_cli_config_gen_configuration.enable") | Boolean |  | `True` |  | Generate device EOS configurations. |
    | [<samp>&nbsp;&nbsp;hide_passwords</samp>](## "eos_cli_config_gen_configuration.hide_passwords") | Boolean |  | `False` |  | Replace the input data using the `hide_passwords` filter in the Jinja2 templates by '<removed>' in the configuration if true.<br> |
    | [<samp>eos_cli_config_gen_documentation</samp>](## "eos_cli_config_gen_documentation") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enable</samp>](## "eos_cli_config_gen_documentation.enable") | Boolean |  | `True` |  | Generate device Markdown documentation. |
    | [<samp>&nbsp;&nbsp;hide_passwords</samp>](## "eos_cli_config_gen_documentation.hide_passwords") | Boolean |  | `True` |  | Replace the input data using the `hide_passwords` filter in the Jinja2 templates by '<removed>' in the documentation if true.<br> |
    | [<samp>generate_device_documentation</samp>](## "generate_device_documentation") <span style="color:red">deprecated</span> | Boolean |  | `True` |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>eos_cli_config_gen_documentation.enable</samp> instead.</span> |

=== "YAML"

    ```yaml
    eos_cli_config_gen_configuration:

      # Generate device EOS configurations.
      enable: <bool; default=True>

      # Replace the input data using the `hide_passwords` filter in the Jinja2 templates by '<removed>' in the configuration if true.
      hide_passwords: <bool; default=False>
    eos_cli_config_gen_documentation:

      # Generate device Markdown documentation.
      enable: <bool; default=True>

      # Replace the input data using the `hide_passwords` filter in the Jinja2 templates by '<removed>' in the documentation if true.
      hide_passwords: <bool; default=True>
    # This key is deprecated.
    # Support will be removed in AVD version 6.0.0.
    # Use <samp>eos_cli_config_gen_documentation.enable</samp> instead.
    generate_device_documentation: <bool; default=True>
    ```
