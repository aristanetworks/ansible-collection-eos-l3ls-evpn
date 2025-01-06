# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

GH_CODE = {
    "PASS": ":white_check_mark:",  # Github MD code for Emoji checked box
    "FAIL": ":x:",  # GH MD code for Emoji Fail
}


def status_render(state_string: str, rendering: str) -> str:
    """
    status_render Convert Text to EMOJI code.

    Parameters
    ----------
    state_string : str
        Text to convert in EMOJI
    rendering : string
        Markdown Flavor to use for Emoji rendering.

    Returns:
    -------
    str
        Value to render in markdown
    """
    if rendering == "github":
        return GH_CODE[state_string.upper()]
    return state_string
