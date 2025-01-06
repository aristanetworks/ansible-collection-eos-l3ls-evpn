# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from schema_tools.metaschema.meta_schema_model import AvdSchemaField


def render_schema_field(schema: AvdSchemaField, target_table: str | None) -> bool:
    """
    Returns boolean indicating whether this field should be rendered in the targeted table.

    - The root dict is always rendered.
    - Render keys with matching _table
    - Always render the ancestors of a field included in the table.
    - Always render primary keys in list of dicts.
    """
    if not schema._path:
        # Always render the root dict. Actually the root dict will not be rendered as a field, but we need this to render the children.
        return True

    if target_table == schema._table:
        # Target table matches the field table name.
        return True

    if schema._is_primary_key:
        # Always render the field if it is the primary key in a list of dicts.
        return True

    # Keeping this check at the end, since _descendant_tables is a recursive function that can be "expensive"
    # Always render the field if a descendant field has the target table
    return target_table in schema._descendant_tables
