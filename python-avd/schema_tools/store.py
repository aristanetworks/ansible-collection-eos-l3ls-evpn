# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from copy import deepcopy
from functools import lru_cache
from hashlib import sha1
from pathlib import Path
from pickle import HIGHEST_PROTOCOL
from pickle import dump as pickle_dump
from pickle import load as pickle_load

from yaml import safe_load

from .avdschemaresolver import AvdSchemaResolver
from .constants import PICKLED_SCHEMAS, SCHEMA_PATHS


@lru_cache
def create_store(*, load_from_yaml: bool = False, force_rebuild: bool = False) -> dict[str, dict]:
    """
    Create and return a schema store.

    A schema store is a dict of all our schemas like
    {
        "avd_meta_schema": {...avd meta schema as dict...},
        "eos_cli_config_gen": {...schema as dict...},
        "eos_designs": {...schema as dict...},
    }
    The function is cached to save time on multiple calls.

    If load_from_yaml is True it will read and return unresolved schemas from yml files.

    If force_rebuild is True or if this is the first time running AVD after changing schemas/upgrade/install
    the schema yml files will be read, fully resolved, saved as pickle to a file and returned in the
    store dict.
    """
    store = {}

    # Load from YAML if set. This is used by the tool that creates the pickle.
    if load_from_yaml:
        return _create_store_from_yaml()

    # Recompile schemas if needed and store in pickles for next time.
    if force_rebuild or _should_recompile_schemas():
        return _compile_schemas()

    # Load from Pickle.
    for schema_id, schema_file in PICKLED_SCHEMAS.items():
        with Path(schema_file).open("rb") as file:
            store[schema_id] = pickle_load(file)  # noqa: S301

    return store


def _should_recompile_schemas() -> bool:
    """Returns true if pickled schemas should be recompiled."""
    # Check if any pickled schema is missing
    for pickle_file in PICKLED_SCHEMAS.values():
        if not pickle_file.exists():
            return True

    # Check if any hash file is missing and if any stored hash does not match the hash of the schema file
    for schema_file in SCHEMA_PATHS.values():
        hash_file = schema_file.with_suffix(".sha1")
        if not hash_file.exists():
            return True

        existing_hash = hash_file.with_suffix(".sha1").read_text(encoding="UTF-8")
        new_hash = sha1(schema_file.read_bytes(), usedforsecurity=False).hexdigest()  # NOSONAR
        if existing_hash != new_hash:
            return True

    return False


def _create_store_from_yaml() -> dict[str, dict]:
    """Returns a schema store loaded from yaml files with $ref."""
    store = {}
    for schema_id, schema_file in SCHEMA_PATHS.items():
        with Path(schema_file).open(encoding="UTF-8") as stream:
            store[schema_id] = safe_load(stream)
    return store


def _compile_schemas() -> dict:
    """
    Resolve full schemas and save as pickle files.

    Load schemas from yaml files
    create a temporary "store",
    resolve all $refs and save the resulting schemas as pickles.
    """
    schema_store = _create_store_from_yaml()

    # We rely on eos_cli_config_gen being before eos_designs,
    # so anything in eos_cli_config_gen can be resolved and $def popped before resolving from eos_designs.
    for schema_name, pickle_file in PICKLED_SCHEMAS.items():
        if schema_name == "avd_meta_schema":
            # Do not resolve $ref in the meta schema.
            resolved_schema = schema_store[schema_name]
        else:
            resolved_schema = _resolve_schema(schema_store[schema_name], schema_store)

            # Inplace update the schema store with the resolved variant without $def.
            # This is needed so eos_designs will not resolve to a schema with another $ref.
            schema_store[schema_name] = resolved_schema

        # Update pickle file with binary version of the completely resolved schema.
        try:
            with pickle_file.open("wb") as stream:
                pickle_dump(resolved_schema, stream, HIGHEST_PROTOCOL)

            # Update the .sha1 file with the new hash of the yaml schema file.
            schema_file = SCHEMA_PATHS[schema_name]
            new_hash = sha1(schema_file.read_bytes(), usedforsecurity=False).hexdigest()  # NOSONAR
            schema_file.with_suffix(".sha1").write_text(new_hash, encoding="UTF-8")
        except PermissionError:
            # Ignoring PermissionError so we can operate in read-only environments
            # (like "ansible-test units" containers).
            pass

    return schema_store


def _resolve_schema(schema: dict, store: dict) -> dict:
    """
    Get fully resolved schema (where all $ref has been expanded recursively).

    .schemaresolver performs inplace update of the argument so we give it a copy of the existing schema.
    """
    resolved_schema = deepcopy(schema)
    schemaresolver = AvdSchemaResolver(schema["$id"], store)
    schemaresolver.resolve(resolved_schema)

    # Since the schema is now fully resolved we can drop the $defs.
    resolved_schema.pop("$defs", None)

    return resolved_schema
