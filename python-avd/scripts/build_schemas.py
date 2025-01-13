#!/usr/bin/env python3
# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging
from pathlib import Path
from sys import argv, path

# Override global path to load schema from source instead of any installed version.
path.insert(0, str(Path(__file__).parents[1]))

from schema_tools.build_schemas import build_schemas

if __name__ == "__main__":
    log_level_str = argv[1].upper() if len(argv) > 1 else "DEBUG"
    log_level = logging.getLevelName(log_level_str)
    logging.basicConfig(level=log_level, format="[build_schemas] - %(message)s")
    build_schemas()
