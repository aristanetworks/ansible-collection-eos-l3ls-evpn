# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging

from pyavd.constants import RUNNING_FROM_SRC
from schema_tools.build_schemas import build_schemas
from schema_tools.hash_dir import changed_hash, hash_dir

from .constants import (
    EOS_CLI_CONFIG_GEN_FRAGMENTS_PATH,
    EOS_DESIGNS_FRAGMENTS_PATH,
)

LOGGER = logging.getLogger(__name__)


def check_schemas() -> bool:
    """
    Verify if eos_designs or eos_cli_config_gen schema need to be recompiled when running from source.

    Returns:
    --------
    bool:
        True if any schema changed, False otherwise
    """
    if not RUNNING_FROM_SRC:
        return False

    LOGGER.info("pyavd running from source detected, checking schemas for any changes...")

    return changed_hash(EOS_DESIGNS_FRAGMENTS_PATH) or changed_hash(EOS_CLI_CONFIG_GEN_FRAGMENTS_PATH)


def rebuild_schemas() -> None:
    """Rebuild the schema and saves the new hashes."""
    LOGGER.info("Recompiling schemas...")
    build_schemas()
    with (EOS_DESIGNS_FRAGMENTS_PATH / ".hash").open("w") as fd:
        eos_designs_new_hash = hash_dir(EOS_DESIGNS_FRAGMENTS_PATH)
        fd.write(eos_designs_new_hash)
    with (EOS_CLI_CONFIG_GEN_FRAGMENTS_PATH / ".hash").open("w") as fd:
        eos_cli_config_gen_new_hash = hash_dir(EOS_CLI_CONFIG_GEN_FRAGMENTS_PATH)
        fd.write(eos_cli_config_gen_new_hash)
