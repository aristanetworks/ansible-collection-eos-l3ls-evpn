# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging
from pathlib import Path
from textwrap import indent

from deepmerge import always_merger
from yaml import CSafeDumper, CSafeLoader
from yaml import dump as yaml_dump
from yaml import load as yaml_load

from .constants import DOCS_PATHS, LICENSE_HEADER, SCHEMA_FRAGMENTS_PATHS, SCHEMA_PATHS
from .generate_docs.mdtabsgen import get_md_tabs
from .metaschema.meta_schema_model import AristaAvdSchema
from .store import create_store

try:
    import jsonschema_rs

    HAS_JSONSCHEMA_RS = True
except ImportError:
    HAS_JSONSCHEMA_RS = False

FRAGMENTS_PATTERN = "*.yml"

LOGGER = logging.getLogger(__name__)


def combine_schemas() -> None:
    """Combine all schema fragments into a single YAML file."""
    for schema_name, fragments_path in SCHEMA_FRAGMENTS_PATHS.items():
        LOGGER.info("Combining fragments %s", fragments_path)
        if schema_name not in SCHEMA_PATHS:
            msg = f"Invalid schema name '{schema_name}'"
            raise KeyError(msg)

        schema = {}
        for fragment_filename in sorted(fragments_path.glob(FRAGMENTS_PATTERN)):
            with fragment_filename.open(mode="r", encoding="UTF-8") as fragment_stream:
                schema = always_merger.merge(schema, yaml_load(fragment_stream, Loader=CSafeLoader))

        with SCHEMA_PATHS[schema_name].open(mode="w", encoding="UTF-8") as schema_stream:
            schema_stream.write(indent(LICENSE_HEADER, prefix="# ") + "\n")
            schema_stream.write(
                "# yaml-language-server: $schema=../../_schema/avd_meta_schema.json\n"
                "# Line above is used by RedHat's YAML Schema vscode extension\n"
                "# Use Ctrl + Space to get suggestions for every field. Autocomplete will pop up after typing 2 letters.\n",
            )
            schema_stream.write(yaml_dump(schema, Dumper=CSafeDumper, sort_keys=False))


def validate_schemas(schema_store: dict) -> None:
    """Validate schemas according to metaschema."""
    if not HAS_JSONSCHEMA_RS:
        LOGGER.warning(
            "'jsonschema_rs' was not found. If you are a developer using AVD make sure to install the dev requirements for the collection. "
            "The schemas could not be validated."
        )
        return
    schema_validator = jsonschema_rs.Draft7Validator(schema_store["avd_meta_schema"])
    for schema_name in SCHEMA_FRAGMENTS_PATHS:
        LOGGER.info("Validating schema '%s'", schema_name)
        schema_validator.validate(schema_store[schema_name])


def build_schema_tables(schema_store: dict) -> None:
    """Build schema tables."""
    for schema_name in SCHEMA_PATHS:
        if schema_name not in SCHEMA_FRAGMENTS_PATHS:
            continue

        schema = AristaAvdSchema(**schema_store[schema_name])
        table_names = sorted(schema._descendant_tables)
        output_dir = DOCS_PATHS[schema_name].joinpath("tables")
        for table_name in table_names:
            LOGGER.debug("Building table: %s from schema %s", table_name, schema_name)
            table_file = output_dir.joinpath(f"{table_name}.md")
            with Path(table_file).open(mode="w", encoding="UTF-8") as file:
                file.write(get_md_tabs(schema, table_name))

        # Clean up other markdown files not covered by the tables.
        remove_files = [file for file in output_dir.glob("*.md") if file.is_file() and file.name.removesuffix(".md") not in table_names]
        for file in remove_files:
            LOGGER.info("Deleting file %s", file.absolute())
            file.unlink()


def build_schemas() -> None:
    """Combines the schema fragments, and rebuild the pickled schemas."""
    combine_schemas()
    LOGGER.info("Rebuilding pickled schemas")
    schema_store = create_store(force_rebuild=True)
    validate_schemas(schema_store)
    LOGGER.info("Rebuilding schemas documentation tables...")
    build_schema_tables(schema_store)
