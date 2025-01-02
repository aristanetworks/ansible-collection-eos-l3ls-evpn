# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path

import pytest
from yaml import safe_load

ARTIFACTS_PATH = Path(__file__).parent.joinpath("artifacts")
EOS_DESIGNS_SCHEMA_PATH = ARTIFACTS_PATH.joinpath("eos_designs.schema.yml")
EOS_CLI_CONFIG_GEN_SCHEMA_PATH = ARTIFACTS_PATH.joinpath("eos_cli_config_gen.schema.yml")

# The schemas are read of test artifacts which are frozen copies of the regular schemas.
# We keep a frozen copy of the schemas here, so the expected outputs don't change as the schemas evolve.
with Path(EOS_CLI_CONFIG_GEN_SCHEMA_PATH).open(encoding="UTF-8") as file:
    test_eos_cli_config_gen_schema = safe_load(file)
with Path(EOS_DESIGNS_SCHEMA_PATH).open(encoding="UTF-8") as file:
    test_eos_designs_schema = safe_load(file)


@pytest.fixture(scope="module")
def artifacts_path() -> Path:
    return ARTIFACTS_PATH


@pytest.fixture(scope="module")
def output_path() -> Path:
    return ARTIFACTS_PATH.joinpath("output")


@pytest.fixture(scope="module")
def schema_store() -> dict[str, dict]:
    """
    Return dict with schemas.

    {
        "eos_cli_config_gen": dict
        "eos_designs": dict
    }.
    """
    return {
        "eos_cli_config_gen": test_eos_cli_config_gen_schema,
        "eos_designs": test_eos_designs_schema,
    }


@pytest.fixture(scope="module")
def schema_paths() -> dict[str, dict]:
    """
    Return dict with schema paths.

    {
        "eos_cli_config_gen": Path
        "eos_designs": Path
    }.
    """
    return {
        "eos_cli_config_gen": EOS_CLI_CONFIG_GEN_SCHEMA_PATH,
        "eos_designs": EOS_DESIGNS_SCHEMA_PATH,
    }
