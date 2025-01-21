# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""AVD schematools constants."""

from pathlib import Path

REPO_ROOT = Path(__file__).parents[2]
PYAVD_DIR = REPO_ROOT.joinpath("python-avd/pyavd")

EOS_DESIGNS_SCHEMA_DIR = PYAVD_DIR.joinpath("_eos_designs/schema")
EOS_DESIGNS_SCHEMA_PATH = EOS_DESIGNS_SCHEMA_DIR.joinpath("eos_designs.schema.yml")
EOS_DESIGNS_FRAGMENTS_PATH = EOS_DESIGNS_SCHEMA_DIR.joinpath("schema_fragments")
EOS_DESIGNS_PICKLED_SCHEMA_PATH = EOS_DESIGNS_SCHEMA_DIR.joinpath("eos_designs.schema.pickle")
EOS_DESIGNS_DOCS_PATH = REPO_ROOT.joinpath("ansible_collections/arista/avd/roles/eos_designs/docs")

EOS_CLI_CONFIG_GEN_SCHEMA_DIR = PYAVD_DIR.joinpath("_eos_cli_config_gen/schema")
EOS_CLI_CONFIG_GEN_SCHEMA_PATH = EOS_CLI_CONFIG_GEN_SCHEMA_DIR.joinpath("eos_cli_config_gen.schema.yml")
EOS_CLI_CONFIG_GEN_FRAGMENTS_PATH = EOS_CLI_CONFIG_GEN_SCHEMA_DIR.joinpath("schema_fragments")
EOS_CLI_CONFIG_GEN_PICKLED_SCHEMA_PATH = EOS_CLI_CONFIG_GEN_SCHEMA_DIR.joinpath("eos_cli_config_gen.schema.pickle")
EOS_CLI_CONFIG_GEN_DOCS_PATH = REPO_ROOT.joinpath("ansible_collections/arista/avd/roles/eos_cli_config_gen/docs")

METASCHEMA_DIR = PYAVD_DIR.joinpath("_schema")
METASCHEMA_PATH = METASCHEMA_DIR.joinpath("avd_meta_schema.json")
METASCHEMA_PICKLED_SCHEMA_PATH = METASCHEMA_DIR.joinpath("avd_meta_schema.pickle")

SCHEMA_PATHS = {
    "avd_meta_schema": METASCHEMA_PATH,
    "eos_cli_config_gen": EOS_CLI_CONFIG_GEN_SCHEMA_PATH,
    "eos_designs": EOS_DESIGNS_SCHEMA_PATH,
}
SCHEMA_FRAGMENTS_PATHS = {
    "eos_cli_config_gen": EOS_CLI_CONFIG_GEN_FRAGMENTS_PATH,
    "eos_designs": EOS_DESIGNS_FRAGMENTS_PATH,
}
PICKLED_SCHEMAS = {
    "avd_meta_schema": METASCHEMA_PICKLED_SCHEMA_PATH,
    "eos_cli_config_gen": EOS_CLI_CONFIG_GEN_PICKLED_SCHEMA_PATH,
    "eos_designs": EOS_DESIGNS_PICKLED_SCHEMA_PATH,
}
PYTHON_CLASS_PATHS = {
    "eos_cli_config_gen": EOS_CLI_CONFIG_GEN_SCHEMA_DIR.joinpath("__init__.py"),
    "eos_designs": EOS_DESIGNS_SCHEMA_DIR.joinpath("__init__.py"),
}
DOCS_PATHS = {
    "eos_cli_config_gen": EOS_CLI_CONFIG_GEN_DOCS_PATH,
    "eos_designs": EOS_DESIGNS_DOCS_PATH,
}
LICENSE_HEADER = REPO_ROOT.joinpath("development/license-short.txt").read_text(encoding="UTF-8").strip()
