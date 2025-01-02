# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import json
from pathlib import Path
from sys import path
from typing import Any

import yaml

# Override global path to load schema from source instead of any installed version.
# Avoids to load from pyavd to avoid relying on pyavd vendor things being generated.
path.insert(0, str(Path(__file__).parents[3]))

from schema_tools.metaschema.meta_schema_model import AristaAvdSchema
from schema_tools.store import create_store

raw_schema = create_store()["eos_designs"]


class NoAliasDumper(yaml.Dumper):
    """Dump YAML without generating aliases and anchors for reused ids."""

    def ignore_aliases(self, _: Any) -> bool:
        return True


def test_pydantic_dump_matches_original_yaml() -> None:
    """
    Loads the schema _without_ resolving the $ref and then dumps the schema again as json.

    Then compares the input schema with the dumped schema.
    """
    pydantic_schema = AristaAvdSchema(_resolve_schema=False, **raw_schema)

    dump_raw_schema = yaml.dump(raw_schema, Dumper=NoAliasDumper)
    dump_pydantic_schema = yaml.dump(json.loads(pydantic_schema.model_dump_json(by_alias=True, exclude_unset=True)), Dumper=NoAliasDumper)
    assert dump_raw_schema == dump_pydantic_schema
