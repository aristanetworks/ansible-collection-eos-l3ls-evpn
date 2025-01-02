# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from os import environ
from pathlib import Path

RUNNING_FROM_SRC = Path(__file__).parent.joinpath("running_from_src.txt").exists() and not environ.get("AVD_NEVER_RUN_FROM_SOURCE")
EOS_CLI_CONFIG_GEN_SCHEMA_ID = "eos_cli_config_gen"
EOS_DESIGNS_SCHEMA_ID = "eos_designs"
EOS_CLI_CONFIG_GEN_JINJA2_CONFIG_TEMPLATE = "eos-intended-config.j2"
EOS_CLI_CONFIG_GEN_JINJA2_DOCUMENTAITON_TEMPLATE = "eos-device-documentation.j2"
JINJA2_EXTENSIONS = ["jinja2.ext.loopcontrols", "jinja2.ext.do", "jinja2.ext.i18n"]
EOS_CLI_CONFIG_GEN_JINJA2_TEMPLATE_PATH = Path(__file__).parent.joinpath("_eos_cli_config_gen/j2templates")
EOS_CLI_CONFIG_GEN_JINJA2_PRECOMPILED_TEMPLATE_PATH = EOS_CLI_CONFIG_GEN_JINJA2_TEMPLATE_PATH.joinpath("compiled_templates")
EOS_DESIGNS_JINJA2_TEMPLATE_PATH = Path(__file__).parent.joinpath("_eos_designs/j2templates")
EOS_DESIGNS_JINJA2_PRECOMPILED_TEMPLATE_PATH = EOS_DESIGNS_JINJA2_TEMPLATE_PATH.joinpath("compiled_templates")
