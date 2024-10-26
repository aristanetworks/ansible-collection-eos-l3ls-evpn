# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import re
from unicodedata import normalize

HEADING_PATTERN = re.compile(r"#+ ")


def add_md_toc(md_input: str, skip_lines: int = 0, toc_levels: int = 3, toc_marker: str = "<!-- toc -->") -> str:
    """Parse the input Markdown and add a TOC between the toc_markers.

    Parameters
    ----------
    md_input: str
        Markdown which will be processed
    skip_lines: int, optional
        Skip first x lines when parsing MD file
        default: 0
    toc_levels: int, optional
        How many levels of headings will be included in the TOC (Default:3)
        default: 3
    toc_marker: str, optional
        TOC will be inserted or updated between two of these markers in the MD file
        default: '<!-- toc -->'

    Returns:
    -------
    str
        MD with added TOC
    """
    if not isinstance(skip_lines, int):
        msg = f"add_md_toc 'skip_lines' argument must be an integer. Got '{skip_lines}'({type(skip_lines)})."
        raise TypeError(msg)

    if not isinstance(toc_levels, int) or toc_levels < 1:
        msg = f"add_md_toc 'toc_levels' argument must be >0. Got '{toc_levels}'({type(skip_lines)})."
        raise TypeError(msg)

    if not isinstance(toc_marker, str) or not toc_marker:
        msg = f"add_md_toc 'toc_marker' argument must be a non-empty string. Got '{toc_marker}'({type(skip_lines)})."
        raise TypeError(msg)

    if not isinstance(md_input, str):
        msg = f"add_md_toc expects a string. Got {type(md_input)}."
        raise TypeError(msg)

    md_lines = md_input.split("\n")
    toc_marker_positions = []
    toc_lines = []

    # all_anchor_ids is used to hold anchors for the full MD document even if we are skipping lines or levels for the TOC.
    all_anchor_ids = []

    # toc_level_offset ensures we start the TOC at the lowest level within the unskipped lines.
    toc_level_offset = 99

    for line_num, line in enumerate(md_lines):
        if line == toc_marker:
            # Register line number or the TOC marker.
            toc_marker_positions.append(line_num)
            continue
        if re.match(HEADING_PATTERN, line):
            # This is a heading.
            # First get info for this line, including building an anchor and adding this anchor to all_anchor_ids.
            # This is important, since skipped headings will still be associated with an anchor-id during parsing of the final Markdown file.
            level, text, anchor_id = _get_line_info(line, all_anchor_ids)

            # Do not create a TOC line if we are skipping or at a deeper level than we want.
            if line_num < skip_lines or level > toc_levels:
                continue

            # Create the TOC line
            toc_level_offset = min(toc_level_offset, level)
            prefix = ("  " * (level - toc_level_offset)) + "- "
            toc_lines.append(f"{prefix}[{text}](#{anchor_id})")

    if len(toc_marker_positions) != 2:
        msg = f"add_md_toc expects exactly two occurrences of the toc marker '{toc_marker}' on their own lines. Found {len(toc_marker_positions)} occurrences."
        raise ValueError(msg)

    return "\n".join(md_lines[: toc_marker_positions[0]] + toc_lines + md_lines[toc_marker_positions[1] + 1 :])


def _get_line_info(line: str, all_anchor_ids: list[str]) -> tuple[int, str, str]:
    """Split heading and return level, text and anchor_id.

    Since we know the line is already a heading, we can assume correct formatting.
    Update all_anchor_ids with the missing anchor if not found.

    Parameters
    ----------
    line: str
        Line to parse
    all_anchor_ids: list
        List of existing anchor_ids

    Returns:
    -------
    int, str, str:
        The level of the heading, the text of the heading and the anchor_id for the heading.
    """
    pounds, text = line.split(" ", maxsplit=1)
    level = len(pounds)
    anchor_id = _get_anchor_id(text, all_anchor_ids)

    return level, text, anchor_id


def _get_anchor_id(text: str, all_anchor_ids: list[str]) -> str:
    """
    Returns a unique anchor_id after adding it to 'all_anchor_ids'.

    The logic here follow the auto-id generation algorithm of the Markdown spec.

    Parameters
    ----------
    text: str
        Text to generate an anchor for.
    all_anchor_ids: list
        List of existing anchor_ids

    Returns:
    -------
    str:
        The anchor ID for the text.
    """
    tmp_anchor_id = normalize("NFKD", text).encode("ascii", "ignore")
    tmp_anchor_id = re.sub(r"[^\w\s-]", "", tmp_anchor_id.decode("ascii")).strip().lower()
    tmp_anchor_id = re.sub(r"[-\s]+", "-", tmp_anchor_id)

    anchor_id = tmp_anchor_id
    counter = 0
    while anchor_id in all_anchor_ids:
        counter += 1
        anchor_id = f"{tmp_anchor_id}-{counter}"
    all_anchor_ids.append(anchor_id)
    return anchor_id
