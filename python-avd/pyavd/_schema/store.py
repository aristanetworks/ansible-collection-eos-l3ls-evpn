# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from functools import lru_cache
from pathlib import Path
from pickle import load

from .constants import PICKLED_SCHEMAS


@lru_cache
def create_store(*, load_from_yaml: bool = False) -> dict:
    if load_from_yaml:
        msg = "'load_from_yaml' not supported for create_store under PyAVD"
        raise NotImplementedError(msg)
    store = {}
    for schema_id, schema_file in PICKLED_SCHEMAS.items():
        with Path(schema_file).open("rb") as file:
            store[schema_id] = load(file)  # noqa: S301

    return store
