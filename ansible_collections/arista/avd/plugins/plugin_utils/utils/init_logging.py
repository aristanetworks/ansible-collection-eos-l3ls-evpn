# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging

from ansible.utils.display import Display

from .python_to_ansible_logging_handler import PythonToAnsibleHandler


def init_pyavd_logging() -> None:
    """
    Specify logger parameters for pyavd and schematools.

    The verbosity depends on the verbosity level passed to Ansible
    - Ansible verbosity 0 translate to a level of warning
    - Ansible verbosity 1 to 2 (-v to -vv) translates to a level of info
    - Ansible verbosity 3 and above translates to a level of debug
    """
    pyavd_logger = logging.getLogger("pyavd")
    schema_tools_logger = logging.getLogger("schema_tools")
    # Avoid duplicate logs
    pyavd_logger.propagate = False
    schema_tools_logger.propagate = False

    pyavd_handler = PythonToAnsibleHandler(None)
    pyavd_formatter = logging.Formatter("[pyavd] - %(message)s")
    pyavd_handler.setFormatter(pyavd_formatter)

    pyavd_logger.addHandler(pyavd_handler)
    schema_tools_logger.addHandler(pyavd_handler)

    verbosity = Display().verbosity
    if verbosity >= 3:
        pyavd_logger.setLevel(logging.DEBUG)
        schema_tools_logger.setLevel(logging.DEBUG)
    elif verbosity > 0:
        pyavd_logger.setLevel(logging.INFO)
        schema_tools_logger.setLevel(logging.INFO)
    else:
        pyavd_logger.setLevel(logging.WARNING)
        schema_tools_logger.setLevel(logging.WARNING)
