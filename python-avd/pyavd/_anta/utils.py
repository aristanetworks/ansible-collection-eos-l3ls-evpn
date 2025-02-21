# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Utility functions used by PyAVD for ANTA."""

from __future__ import annotations

from logging import getLogger
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from anta.catalog import AntaCatalog


LOGGER = getLogger(__name__)


def dump_anta_catalog(hostname: str, catalog: AntaCatalog, catalog_dir: str) -> None:
    """Dump the ANTA catalog for a device to the provided catalog directory.

    The catalog will be saved as a JSON file named after the device: `<device>.json`.
    """
    catalog_path = Path(catalog_dir) / f"{hostname}.json"
    catalog_dump = catalog.dump()

    LOGGER.debug("<%s> dumping ANTA catalog at %s", hostname, catalog_path)
    with catalog_path.open(mode="w", encoding="UTF-8") as stream:
        stream.write(catalog_dump.to_json())
