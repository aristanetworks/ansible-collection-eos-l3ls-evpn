#!/usr/bin/env python3
# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import logging
from pathlib import Path
from sys import argv, path

# Override global path to load pyavd from pwd instead of any installed version.
path.insert(0, str(Path(__file__).parent.parent))

from schema_tools.compile_templates import compile_eos_cli_config_gen_templates, compile_eos_designs_templates


def main(log_level: int = logging.INFO) -> None:
    """
    Main entrypoint for the script.

    It combines the schema fragments, and rebuild the pickled schemas.

    """
    logging.basicConfig(level=log_level, format="[compile_templates] - %(message)s")
    compile_eos_cli_config_gen_templates()
    compile_eos_designs_templates()


if __name__ == "__main__":
    log_level_str = argv[1].upper() if len(argv) > 1 else "DEBUG"
    log_level = logging.getLevelName(log_level_str)
    main(log_level)
