# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging
import subprocess
from pathlib import Path
from textwrap import indent

from deepmerge import always_merger
from yaml import CSafeDumper, CSafeLoader
from yaml import dump as yaml_dump
from yaml import load as yaml_load

from .constants import DOCS_PATHS, LICENSE_HEADER, PYTHON_CLASS_PATHS, SCHEMA_FRAGMENTS_PATHS, SCHEMA_PATHS
from .generate_classes.src_generators import FileSrc
from .generate_classes.utils import generate_class_name
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
    LOGGER.info("Rebuilding schema documentation tables...")
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


def build_schema_classes() -> None:
    """Build Python Classes from schema."""
    LOGGER.info("Rebuilding schema Python Classes...")
    # We use a special schema store since we only wish to resolve a subset of the $defs. This is to have more reuse of the generated classes
    raw_yaml_schema_store = create_store(load_from_yaml=True)
    for schema_name, python_class_path in PYTHON_CLASS_PATHS.items():
        if schema_name not in raw_yaml_schema_store:
            msg = f"Invalid schema name '{schema_name}'"
            raise KeyError(msg)

        schema = AristaAvdSchema(_resolve_schema=schema_name, **raw_yaml_schema_store[schema_name])
        LOGGER.info("Building Python Classes from schema: %s", schema_name)
        schemasrc = schema._generate_class_src(class_name=generate_class_name(schema_name))
        src_file_contents = FileSrc(classes=[schemasrc.cls])
        with python_class_path.open(mode="w", encoding="UTF-8") as file:
            file.write(str(src_file_contents))

        LOGGER.info("Running 'ruff' for Python class file: %s", python_class_path)
        subprocess.run(["ruff", "check", "--fix", str(python_class_path)], check=False)  # noqa: S603, S607
        subprocess.run(["ruff", "format", str(python_class_path)], check=False)  # noqa: S603, S607


def build_schemas() -> None:
    """Combines the schema fragments, and rebuild the pickled schemas."""
    combine_schemas()
    LOGGER.info("Rebuilding pickled schemas")
    schema_store = create_store(force_rebuild=True)
    validate_schemas(schema_store)
    build_schema_tables(schema_store)
    build_schema_classes()
