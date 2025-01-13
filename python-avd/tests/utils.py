# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from json import JSONDecodeError
from json import loads as json_loads
from pathlib import Path
from sys import stdin

from yaml import CSafeLoader
from yaml import load as yaml_load


def read_file(filename: str) -> str:
    if filename == "/dev/stdin" and stdin.isatty():
        print("Write variables in YAML or JSON format and end with ctrl+d to exit")  # noqa: T201 accepting print for stdin inputs
    with Path.open(filename, encoding="UTF-8") as file:
        return file.read()


def read_vars(filename: str) -> dict:
    data = read_file(filename)

    try:
        return json_loads(data)
    except JSONDecodeError:
        pass

    return yaml_load(data, Loader=CSafeLoader) or {}


def write_result(filename: str, result: str) -> None:
    mode = "w+"
    if filename == "/dev/stdout":
        mode = "w"

    with Path.open(filename, mode, encoding="UTF-8") as file:
        file.write(result)


def create_common_vars(common_varfiles: list) -> dict:
    common_vars = {}
    for file in common_varfiles:
        common_vars.update(read_vars(file))
    return common_vars


def get_files_in_folder(folder_path: str) -> list:
    return [
        Path(
            root,
            filename,
        )
        for root, _, filenames in Path(folder_path).walk()
        for filename in filenames
    ]
