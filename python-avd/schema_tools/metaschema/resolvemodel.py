# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from copy import deepcopy
from functools import lru_cache
from typing import Literal

from deepmerge import conservative_merger

from schema_tools.store import create_store


def merge_schema_from_ref(schema: dict, resolve_schema: Literal["eos_designs", "eos_cli_config_gen", "all"] | None = None) -> dict:
    """
    Returns a copy of the schema with any $ref resolved.

    If the referenced schema also has a $ref, that too will be resolved.

    Any child schemas will _not_ be resolved.

    By setting "resolve_schema" to a string it is possible to only resolve $refs to this schema.
    If $refs are overridden with anything like extra keys etc it will still be resolved.
    """
    if "$ref" not in schema:
        return schema

    schema = deepcopy(schema)
    ref: str = schema["$ref"]
    ref_schema = merge_schema_from_ref(get_schema_from_ref(ref), resolve_schema)
    if ref_schema["type"] != schema["type"]:
        # TODO: Consider if this should be a pyavd specific error
        msg = (
            f"Incompatible schema types from ref '{ref}' ref type '{ref_schema['type']}' schema type '{schema['type']}'\nschema: {schema}\nref_schema:"
            f" {ref_schema})"
        )
        raise ValueError(msg)

    pure_ref_schema = (
        {"type", "$ref", "description", "documentation_options", "deprecation", "relaxed_validation"}.issuperset(schema.keys())
        and resolve_schema not in [None, "all"]
        and not schema["$ref"].startswith(f"{resolve_schema}#")
    )

    # If this is a pure ref schema we will not resolve it unless it is a native list.
    # This ensures that the generated classes will use the class created in the ref.
    # Some lists can be built as an AvdIndexedList, so we don't have to resolve it.
    if pure_ref_schema and (schema["type"] != "list" or (ref_schema.get("primary_key") and not ref_schema.get("allow_duplicate_primary_key"))):
        schema.setdefault("description", ref_schema.get("description"))
        return schema

    schema.pop("$ref")
    return conservative_merger.merge(schema, ref_schema)


@lru_cache
def get_schema_from_ref(ref: str) -> dict:
    """
    Returns the schema found in the schema store using the given absolute ref.

    The ref is in the style "schema_name#/path/to/schema/element"
    """
    schema_store = create_store(load_from_yaml=True)

    if "#" not in ref:
        msg = "Missing # in ref"
        raise ValueError(msg)

    schema_name, ref = ref.split("#", maxsplit=1)
    if schema_name not in schema_store:
        msg = f"Invalid schema name '{schema_name}' from $ref '{ref}'"
        raise KeyError(msg)

    schema = schema_store[schema_name]
    path = ref.split("/")
    ref_schema = walk_schema(schema, path)
    if ref_schema is None:
        msg = f"Unable to resolve schema ref '{ref}' for schema '{schema_name}'"
        raise KeyError(msg)

    return ref_schema


def walk_schema(schema: dict, path: list[str]) -> dict | None:
    """
    Paths the dictionary along the given path. Empty steps are ignored.

    If the path is invalid it will return None, so the calling function can raise an error with the original schema ref.
    """
    if not path:
        return schema

    step = path.pop(0)
    if step == "":
        return walk_schema(schema, path)

    if step in schema:
        return walk_schema(schema[step], path)

    return None
