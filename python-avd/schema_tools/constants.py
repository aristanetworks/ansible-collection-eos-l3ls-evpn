# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""AVD schematools constants."""

from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).parents[2]
PYAVD_DIR = REPO_ROOT.joinpath("python-avd/pyavd")

LICENSE_HEADER = REPO_ROOT.joinpath("development/license-short.txt").read_text(encoding="UTF-8").strip()

METASCHEMA_DIR = PYAVD_DIR.joinpath("_schema")
EOS_CLI_CONFIG_GEN_SCHEMA_DIR = PYAVD_DIR.joinpath("_eos_cli_config_gen/schema")
EOS_DESIGNS_SCHEMA_DIR = PYAVD_DIR.joinpath("_eos_designs/schema")


@dataclass(frozen=True)
class SchemaPaths:
    yaml_file: Path
    pickled_schema: Path
    fragments_dir: Path | None = None
    python_class: Path | None = None
    docs_path: Path | None = None


# Remember to also update PICKLED_SCHEMAS in pyavd/_schema/constants.py
SCHEMAS = {
    "avd_meta_schema": SchemaPaths(
        yaml_file=METASCHEMA_DIR.joinpath("avd_meta_schema.json"),
        pickled_schema=METASCHEMA_DIR.joinpath("avd_meta_schema.pickle"),
    ),
    "eos_cli_config_gen": SchemaPaths(
        yaml_file=EOS_CLI_CONFIG_GEN_SCHEMA_DIR.joinpath("eos_cli_config_gen.schema.yml"),
        pickled_schema=EOS_CLI_CONFIG_GEN_SCHEMA_DIR.joinpath("eos_cli_config_gen.schema.pickle"),
        fragments_dir=EOS_CLI_CONFIG_GEN_SCHEMA_DIR.joinpath("schema_fragments"),
        python_class=EOS_CLI_CONFIG_GEN_SCHEMA_DIR.joinpath("__init__.py"),
        docs_path=REPO_ROOT.joinpath("ansible_collections/arista/avd/roles/eos_cli_config_gen/docs"),
    ),
    "eos_designs": SchemaPaths(
        yaml_file=EOS_DESIGNS_SCHEMA_DIR.joinpath("eos_designs.schema.yml"),
        pickled_schema=EOS_DESIGNS_SCHEMA_DIR.joinpath("eos_designs.schema.pickle"),
        fragments_dir=EOS_DESIGNS_SCHEMA_DIR.joinpath("schema_fragments"),
        python_class=EOS_DESIGNS_SCHEMA_DIR.joinpath("__init__.py"),
        docs_path=REPO_ROOT.joinpath("ansible_collections/arista/avd/roles/eos_designs/docs"),
    ),
}
