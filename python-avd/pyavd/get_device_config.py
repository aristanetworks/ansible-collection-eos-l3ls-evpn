# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.


def get_device_config(structured_config: dict) -> str:
    """
    Render and return the device configuration using AVD eos_cli_config_gen templates.

    Args:
        structured_config: Dictionary with structured configuration.
            Variables should be converted and validated according to AVD `eos_cli_config_gen` schema first using `pyavd.validate_structured_config`.

    Returns:
        Device configuration in EOS CLI format.
    """
    # pylint: disable=import-outside-toplevel
    from .constants import EOS_CLI_CONFIG_GEN_JINJA2_CONFIG_TEMPLATE, EOS_CLI_CONFIG_GEN_JINJA2_PRECOMPILED_TEMPLATE_PATH
    from .templater import Templar

    # pylint: enable=import-outside-toplevel

    templar = Templar(precompiled_templates_path=EOS_CLI_CONFIG_GEN_JINJA2_PRECOMPILED_TEMPLATE_PATH)
    return templar.render_template_from_file(EOS_CLI_CONFIG_GEN_JINJA2_CONFIG_TEMPLATE, structured_config)
