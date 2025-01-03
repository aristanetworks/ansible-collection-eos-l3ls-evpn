# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from pathlib import Path
from sys import path

# Since the pyavd and schema_tools code it stored a layer deeper than the repo root,
# we need to add it to the path when running pytest from repo root.
# That is relevant when using pytest extensions in IDE (VSCode)
path.insert(0, str(Path(__file__).parents[1]))
