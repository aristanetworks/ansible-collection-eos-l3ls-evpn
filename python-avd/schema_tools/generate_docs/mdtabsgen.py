# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from textwrap import indent
from typing import TYPE_CHECKING

from schema_tools.constants import LICENSE_HEADER

from .tablegen import get_table
from .yamlgen import get_yaml

if TYPE_CHECKING:
    from schema_tools.metaschema.meta_schema_model import AristaAvdSchema


def get_md_tabs(schema: AristaAvdSchema, target_table: str | None = None) -> str:
    """
    Generate the content of a markdown file with mkdocs tabs containing documentation of of the schema optionally filtered using "target_table".

    - Table tab contains a markdown table.
    - YAML tab contains a markdown code block with YAML.
    """
    return f"""\
<!--
{indent(LICENSE_HEADER, "  ~ ")}
  -->
=== "Table"

{indent(get_table(schema, target_table), "    ")}
=== "YAML"

{indent(get_yaml(schema, target_table), "    ")}\
"""
