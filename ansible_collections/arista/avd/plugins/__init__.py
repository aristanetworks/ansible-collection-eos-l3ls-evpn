# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from contextlib import suppress
from os import environ
from pathlib import Path

PYTHON_AVD_PATH = Path(__file__).parents[4] / "python-avd"
RUNNING_FROM_SOURCE_PATH = PYTHON_AVD_PATH / "pyavd/running_from_src.txt"
RUNNING_FROM_SOURCE = RUNNING_FROM_SOURCE_PATH.exists() and not environ.get("AVD_NEVER_RUN_FROM_SOURCE")

if RUNNING_FROM_SOURCE:
    import sys

    # TODO: @gmuloc - once proper logging has been implemented for the collection, replace this with a log statement.
    # Note that we can't output anything to stdout or stderr in normal mode or it breaks ansible-sanity
    with suppress(ImportError):
        from ansible.utils.display import Display

        display = Display()

        display.v(f"AVD detected it is running from source, prepending the path to the source of pyavd '{PYTHON_AVD_PATH}' to PATH to use it.")

    sys.path = [str(PYTHON_AVD_PATH), *sys.path]
