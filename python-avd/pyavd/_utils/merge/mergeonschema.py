# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pyavd._schema.avdschema import AvdSchema

from deepmerge import STRATEGY_END


class MergeOnSchema:
    """
    MergeOnSchema provides the method "strategy" to be used as list merge strategy with the deepmerge library.

    The class is needed to allow a schema to be passed along to the method.
    """

    def __init__(self, schema: AvdSchema = None) -> None:
        self.schema = schema

    def strategy(self, config: object, path: list, base: list, nxt: list) -> list:
        """
        Custom strategy to merge lists on schema primary key.

        The argument "config" should be an instance of deepmerge.Merger, but Ansible sanity test breaks type hinting with imported libs.
        """
        # Skip if no schema is supplied
        if not self.schema:
            return STRATEGY_END

        # Skip if we cannot load subschema for path
        try:
            schema = self.schema.subschema(path)
        except Exception:  # pylint: disable=broad-exception-caught
            return STRATEGY_END

        # Skip if the schema for this list is not having "primary_key"
        if "primary_key" not in schema:
            return STRATEGY_END

        primary_key = schema["primary_key"]

        # "merged_nxt_indexes" will contain a list of indexes in nxt that we merged.
        # These will be removed from nxt before passing on to the next strategy.
        merged_nxt_indexes = []

        try:
            # Nested iterations over nxt and base.
            for nxt_index, nxt_item in enumerate(nxt):
                # Skipping items if they are not dicts or don't have primary_key
                if not (isinstance(nxt_item, dict) and primary_key in nxt_item):
                    continue

                for base_index, base_item in enumerate(base):
                    # Skipping items if they are not dicts or don't have primary_key
                    if not (isinstance(base_item, dict) and primary_key in base_item):
                        continue

                    # Skipping items primary_keys don't match.
                    if base_item[primary_key] != nxt_item[primary_key]:
                        continue

                    # Perform regular dict merge on the matching items.
                    merged_nxt_indexes.append(nxt_index)
                    base[base_index] = config.value_strategy(path, base_item, nxt_item)

        except Exception as e:
            msg = f"An issue occurred while trying to do schema-based deepmerge for the schema path {path} using primary key '{primary_key}'"
            raise RuntimeError(msg) from e
        # If all nxt items got merged, we can just return the updated base.
        if len(merged_nxt_indexes) == len(nxt):
            return base

        try:
            # Since some nxt items were not merged, we pass along a reduced nxt to the next strategy.
            # Reverse to avoid changing indexes when removing from nxt.
            merged_nxt_indexes.sort(reverse=True)
            for merged_nxt_index in merged_nxt_indexes:
                del nxt[merged_nxt_index]

        except Exception as e:
            msg = (
                f"An issue occurred after schema-based deepmerge for the schema path {path} using primary key '{primary_key}', "
                f"while preparing remaining items with to be merged with regular strategies. Merged indexes were {merged_nxt_indexes}"
            )
            raise RuntimeError(msg) from e
        return STRATEGY_END
