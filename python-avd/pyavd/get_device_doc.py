# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.


def get_device_doc(structured_config: dict, add_md_toc: bool = False) -> str:
    """
    Render and return the device documentation using AVD eos_cli_config_gen templates.

    Args:
        structured_config: Dictionary with structured configuration.
            Variables should be converted and validated according to AVD `eos_cli_config_gen` schema first using `pyavd.validate_structured_config`.
        add_md_toc: Add a table of contents for markdown headings.

    Returns:
        Device documentation in Markdown format.
    """
    # pylint: disable=import-outside-toplevel
    from .constants import EOS_CLI_CONFIG_GEN_JINJA2_DOCUMENTAITON_TEMPLATE, EOS_CLI_CONFIG_GEN_JINJA2_PRECOMPILED_TEMPLATE_PATH
    from .j2filters import add_md_toc as filter_add_md_toc
    from .templater import Templar

    # pylint: enable=import-outside-toplevel

    templar = Templar(precompiled_templates_path=EOS_CLI_CONFIG_GEN_JINJA2_PRECOMPILED_TEMPLATE_PATH)
    result: str = templar.render_template_from_file(EOS_CLI_CONFIG_GEN_JINJA2_DOCUMENTAITON_TEMPLATE, structured_config)
    if add_md_toc:
        return filter_add_md_toc(result, skip_lines=3)

    return result
