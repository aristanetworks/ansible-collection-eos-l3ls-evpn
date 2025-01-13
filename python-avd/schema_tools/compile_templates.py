# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging

from pyavd.constants import (
    EOS_CLI_CONFIG_GEN_JINJA2_PRECOMPILED_TEMPLATE_PATH,
    EOS_CLI_CONFIG_GEN_JINJA2_TEMPLATE_PATH,
    EOS_DESIGNS_JINJA2_PRECOMPILED_TEMPLATE_PATH,
    EOS_DESIGNS_JINJA2_TEMPLATE_PATH,
    RUNNING_FROM_SRC,
)
from pyavd.templater import Templar

from .hash_dir import changed_hash, hash_dir

LOGGER = logging.getLogger(__name__)


def compile_eos_cli_config_gen_templates() -> None:
    """Compile eos_cli_config_gen Jinja2 templates."""
    templar = Templar(precompiled_templates_path=EOS_CLI_CONFIG_GEN_JINJA2_PRECOMPILED_TEMPLATE_PATH, searchpaths=[EOS_CLI_CONFIG_GEN_JINJA2_TEMPLATE_PATH])
    templar.compile_templates_in_paths(
        precompiled_templates_path=EOS_CLI_CONFIG_GEN_JINJA2_PRECOMPILED_TEMPLATE_PATH, searchpaths=[EOS_CLI_CONFIG_GEN_JINJA2_TEMPLATE_PATH]
    )


def compile_eos_designs_templates() -> None:
    """Compile eos_designs Jinja2 templates."""
    templar = Templar(precompiled_templates_path=EOS_DESIGNS_JINJA2_PRECOMPILED_TEMPLATE_PATH, searchpaths=[EOS_DESIGNS_JINJA2_TEMPLATE_PATH])
    templar.compile_templates_in_paths(precompiled_templates_path=EOS_DESIGNS_JINJA2_PRECOMPILED_TEMPLATE_PATH, searchpaths=[EOS_DESIGNS_JINJA2_TEMPLATE_PATH])


def check_eos_designs_templates() -> bool:
    """
    Verify if eos_designs need to be recompiled when running from source.

    Returns:
    --------
    bool:
        True if any templates changed, False otherwise
    """
    if not RUNNING_FROM_SRC:
        return False

    LOGGER.info("pyavd running from source detected, checking eos_designs templates for any changes...")
    dir_path = EOS_DESIGNS_JINJA2_TEMPLATE_PATH

    return changed_hash(dir_path)


def recompile_eos_designs_templates() -> None:
    """Recompile eos_designs templates."""
    LOGGER.info("Recompiling eos_designs templates...")
    dir_path = EOS_DESIGNS_JINJA2_TEMPLATE_PATH
    compile_eos_designs_templates()
    new_hash = hash_dir(dir_path)
    with (dir_path / ".hash").open("w") as fd:
        fd.write(new_hash)


def check_eos_cli_config_gen_templates() -> bool:
    """
    Verify if eos_cli_config_gen need to be recompiled when running from source.

    Returns:
    --------
    bool:
        True if any templates changed, False otherwise
    """
    if not RUNNING_FROM_SRC:
        return False

    LOGGER.info("pyavd running from source detected, checking eos_cli_config_gen templates for any changes...")
    dir_path = EOS_CLI_CONFIG_GEN_JINJA2_TEMPLATE_PATH

    return changed_hash(dir_path)


def recompile_eos_cli_config_gen_templates() -> None:
    """Recompile eos_cli_config_gen templates."""
    LOGGER.info("Recompiling eos_cli_config_gen templates...")
    dir_path = EOS_CLI_CONFIG_GEN_JINJA2_TEMPLATE_PATH
    compile_eos_cli_config_gen_templates()
    new_hash = hash_dir(dir_path)
    with (dir_path / ".hash").open("w") as fd:
        fd.write(new_hash)


def check_templates() -> bool:
    """
    Check both eos_designs and eos_cli_config_gen templates.

    Returns:
    --------
    bool:
        True if any templates changed, False otherwise
    """
    eos_cli_config_gen_changed = check_eos_cli_config_gen_templates()
    eos_designs_changed = check_eos_designs_templates()
    return eos_designs_changed or eos_cli_config_gen_changed


def recompile_templates() -> None:
    """Recompile eos_cli_config_gen and eos_designs templates."""
    recompile_eos_cli_config_gen_templates()
    recompile_eos_designs_templates()
