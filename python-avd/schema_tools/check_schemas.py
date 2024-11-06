# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging

from pyavd.constants import RUNNING_FROM_SRC
from schema_tools.build_schemas import build_schemas
from schema_tools.hash_dir import changed_hash

from .constants import (
    EOS_CLI_CONFIG_GEN_FRAGMENTS_PATH,
    EOS_DESIGNS_FRAGMENTS_PATH,
)

LOGGER = logging.getLogger(__name__)


def check_schemas() -> None:
    """
    Verify if eos_designs or eos_cli_config_gen schema need to be recompiled when running from source.

    Always recompiling both
    """
    if not RUNNING_FROM_SRC:
        return

    LOGGER.info("pyavd running from source detected, checking schemas for any changes...")

    # eos_designs
    eos_designs_changed, eos_designs_new_hash = changed_hash(EOS_DESIGNS_FRAGMENTS_PATH)
    eos_cli_config_gen_changed, eos_cli_config_gen_new_hash = changed_hash(EOS_CLI_CONFIG_GEN_FRAGMENTS_PATH)
    if eos_designs_changed or eos_cli_config_gen_changed:
        LOGGER.info("Recompiling schemas...")
        build_schemas()
        with (EOS_DESIGNS_FRAGMENTS_PATH / ".hash").open("w") as fd:
            fd.write(eos_designs_new_hash)
        with (EOS_CLI_CONFIG_GEN_FRAGMENTS_PATH / ".hash").open("w") as fd:
            fd.write(eos_cli_config_gen_new_hash)
