# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from schema_tools.metaschema.meta_schema_model import AristaAvdSchema

TABLE_HEADER = [
    "| Variable | Type | Required | Default | Value Restrictions | Description |",
    "| -------- | ---- | -------- | ------- | ------------------ | ----------- |",
]


def get_table(schema: AristaAvdSchema, target_table: str | None = None) -> str:
    """Returns one markdown table either containing all keys of the given schema or only a subset if "target_table" is set."""
    lines = [*TABLE_HEADER]
    lines.extend(str(row) for row in schema._generate_table_rows(target_table=target_table))
    lines.append("")  # Add final newline
    return "\n".join(lines)
