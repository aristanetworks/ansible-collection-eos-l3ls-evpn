# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path

PYAVD_DIR = Path(__file__).parents[1]

EOS_DESIGNS_SCHEMA_DIR = PYAVD_DIR.joinpath("_eos_designs/schema")
EOS_DESIGNS_PICKLED_SCHEMA_PATH = EOS_DESIGNS_SCHEMA_DIR.joinpath("eos_designs.schema.pickle")

EOS_CLI_CONFIG_GEN_SCHEMA_DIR = PYAVD_DIR.joinpath("_eos_cli_config_gen/schema")
EOS_CLI_CONFIG_GEN_PICKLED_SCHEMA_PATH = EOS_CLI_CONFIG_GEN_SCHEMA_DIR.joinpath("eos_cli_config_gen.schema.pickle")

METASCHEMA_DIR = PYAVD_DIR.joinpath("_schema")
METASCHEMA_PICKLED_SCHEMA_PATH = METASCHEMA_DIR.joinpath("avd_meta_schema.pickle")

PICKLED_SCHEMAS = {
    "avd_meta_schema": METASCHEMA_PICKLED_SCHEMA_PATH,
    "eos_cli_config_gen": EOS_CLI_CONFIG_GEN_PICKLED_SCHEMA_PATH,
    "eos_designs": EOS_DESIGNS_PICKLED_SCHEMA_PATH,
}

ACCEPTED_COERCION_MAP = {
    int: (str, bool),
    str: (int, bool, float),
    bool: (str, int),
}
"""Map of target_types and allowed source types for automatic coercion."""
