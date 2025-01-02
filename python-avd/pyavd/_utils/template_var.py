# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from typing import Any

from .template import template


def template_var(template_file: str, template_vars: Any, templar: object) -> str:
    """
    Wrap "template" for single values like IP addresses.

    The result is forced into a string and leading/trailing newlines and whitespaces are removed.

    Parameters
    ----------
    template_file : str
        Path to Jinja2 template file
    template_vars : any
        Variables to use when rendering template
    templar : func
        Instance of Ansible Templar class
    searchpath : list of str
        List of Paths

    Returns:
    -------
    str
        The rendered template
    """
    return str(template(template_file, template_vars, templar)).strip()
