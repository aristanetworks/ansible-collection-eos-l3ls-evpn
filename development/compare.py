#!/usr/bin/env python
# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from itertools import groupby
from pathlib import Path

import yaml


@dataclass(frozen=True, eq=True)
class ConfigLine:
    config: str
    config_source: str = field(compare=False)
    line_number: int = field(compare=False)
    indentation: int
    parent: ConfigLine | None


def parse_config(config: str, config_source: str) -> set[ConfigLine]:
    parsed_config = set()
    last_config_line = ConfigLine(config="", config_source="", line_number=0, indentation=0, parent=None)
    for line_number, config_line in enumerate(config.splitlines(), start=1):
        indentation = len(config_line) - len(config_line.lstrip(" "))
        if indentation == last_config_line.indentation:
            parent = last_config_line.parent
        elif indentation > last_config_line.indentation:
            parent = last_config_line
        else:
            # We may be jumping out multiple levels at once
            parent = last_config_line.parent.parent if last_config_line.parent is not None else last_config_line.parent
            while parent is not None and indentation <= getattr(parent, "indentation", -1):
                parent = parent.parent

        new_config_line = ConfigLine(
            config=config_line,
            config_source=config_source,
            line_number=line_number,
            indentation=indentation,
            parent=parent,
        )
        parsed_config.add(new_config_line)
        last_config_line = new_config_line
    return parsed_config


def get_line_number(stuff: tuple[bool, ConfigLine]) -> int:
    return stuff[1].line_number


def get_family_line(config_line: ConfigLine) -> set[tuple[bool, ConfigLine]]:
    """
    Return set of tuples (is_config_diff: bool, config_line: ConfigLine).

    Diff config lines are marked with true.
    Their ancestors are marked with false.
    """
    parent = config_line.parent
    family = {(True, config_line)}
    while parent is not None:
        family.add((False, parent))
        parent = parent.parent
    return family


def main() -> None:
    """Diff two config files and print out the changes with context awareness and ignoring reordering."""
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    parser.add_argument("old_file")
    parser.add_argument("old_hex")
    parser.add_argument("old_mode")
    parser.add_argument("new_file")
    parser.add_argument("new_hex")
    parser.add_argument("new_mode")
    args = parser.parse_args()

    old = Path(args.old_file).read_text()
    new = Path(args.new_file).read_text()

    if args.old_file.endswith(("yml", "yaml")):
        old = yaml.dump(yaml.load(old, Loader=yaml.CSafeLoader), Dumper=yaml.CDumper, sort_keys=True, indent=2)
    if args.new_file.endswith(("yml", "yaml")):
        new = yaml.dump(yaml.load(new, Loader=yaml.CSafeLoader), Dumper=yaml.CDumper, sort_keys=True, indent=2)

    # Build set of diffs
    diffs = parse_config(old, "old").symmetric_difference(parse_config(new, "new"))

    # Build set of lines including diffs and all their ancestors
    # Each entry is a tuple with a boolean indicating if this is a diff or just a parent.
    interesting_lines: set[tuple[bool, ConfigLine]] = set()
    for diff in diffs:
        interesting_lines.update(get_family_line(diff))

    # Print filename if we have some diffs.
    if interesting_lines:
        print(args.path)  # noqa: T201

    # Group lines together in case a context like Ethernet1 is both a parent as well as being added/removed itself.
    for line_number, lines_gen in groupby(sorted(interesting_lines, key=get_line_number), get_line_number):
        lines = list(lines_gen)
        if len(lines) > 1:
            # We have a line with no +/- that is a parent and a line with +/- that is the actual diff.
            # Remove the one without +/- - [0] is the boolean signalling this is a diff
            lines = [line for line in lines if line[0]]

        for is_diff, config_line in lines:
            if not is_diff:
                # Print line for parent
                print(f" {line_number:5}    {config_line.config}")  # noqa: T201
            elif config_line.config_source == "old":
                # Print line for removal
                print(f"-{line_number:5}    {config_line.config}")  # noqa: T201
            else:
                # Print line for addition
                print(f"+{line_number:5}    {config_line.config}")  # noqa: T201


if __name__ == "__main__":
    main()
