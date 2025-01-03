# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""AVD Jinja2 test defined.

The test checks if a passed variable is defined, and if specified, its value and its type.
"""

from __future__ import annotations

import warnings
from typing import Any

from jinja2.runtime import Undefined


def defined(
    value: Any, test_value: Any = None, var_type: str | None = None, fail_action: str | None = None, var_name: str | None = None, *, run_tests: bool = False
) -> bool | tuple[bool, int]:
    """
    defined - Ansible test plugin to test if a variable is defined and not none.

    Arista.avd.defined will test value if defined and is not none and return true or false.
    If test_value is supplied, the value must also pass == test_value to return true.
    If var_type is supplied, the value must also be of the specified class/type
    If fail_action is 'warning' a warning will be emitted on failure.
    If fail_action is 'error' an error will be emitted on failure and the task will fail.
    If var_name is supplied it will be used in the warning and error messages to ease troubleshooting.

    Examples:
    1. Test if var is defined and not none:
    {% if spanning_tree is arista.avd.defined %}
    ...
    {% endif %}

    2. Test if variable is defined, not none and has value "something"
    {% if extremely_long_variable_name is arista.avd.defined("something") %}
    ...
    {% endif %}

    3. Test if variable is defined and of not print a warning message with the variable name
    {% if my_dict.my_list[12].my_var is arista.avd.defined(fail_action='warning', var_name='my_dict.my_list[12].my_var' %}

    Parameters
    ----------
    value : any
        Value to test from ansible
    test_value : any, optional
        Value to test in addition of defined and not none, by default None
    var_type : ['float', 'int', 'str', 'list', 'dict', 'tuple', 'bool'], optional
        Type or Class to test for
    fail_action : ['warning', 'error'], optional
        Optional action if test fails to emit a Warning or Error
    var_name : <string>, optional
        Optional string to use as variable name in warning or error messages

    Returns:
    -------
    bool
        True if variable matches criteria, False in other cases.
    """
    if isinstance(value, Undefined) or value is None:
        # Invalid value - return false
        if str(fail_action).lower() == "warning":
            warnings_count = {}
            if var_name is not None:
                warning_msg = f"{var_name} was expected but not set. Output may be incorrect or incomplete!"
                warnings.warn(warning_msg)  # noqa: B028
                warnings_count["[WARNING]: " + warning_msg] = warnings_count.get("[WARNING]: " + warning_msg, 0) + 1
            else:
                warning_msg = "A variable was expected but not set. Output may be incorrect or incomplete!"
                warnings.warn(warning_msg)  # noqa: B028
                warnings_count["[WARNING]: " + warning_msg] = warnings_count.get("[WARNING]: " + warning_msg, 0) + 1
        elif str(fail_action).lower() == "error":
            if var_name is not None:
                msg = f"{var_name} was expected but not set!"
                raise ValueError(msg)
            msg = "A variable was expected but not set!"
            raise ValueError(msg)
        if run_tests:
            return False, warnings_count
        return False

    if test_value is not None and value != test_value:
        # Valid value but not matching the optional argument
        if str(fail_action).lower() == "warning":
            warnings_count = {}
            if var_name is not None:
                warning_msg = f"{var_name} was set to {value} but we expected {test_value}. Output may be incorrect or incomplete!"
                warnings.warn(warning_msg)  # noqa: B028
                warnings_count["[WARNING]: " + warning_msg] = warnings_count.get("[WARNING]: " + warning_msg, 0) + 1
            else:
                warning_msg = f"A variable was set to {value} but we expected {test_value}. Output may be incorrect or incomplete!"
                warnings.warn(warning_msg)  # noqa: B028
                warnings_count["[WARNING]: " + warning_msg] = warnings_count.get("[WARNING]: " + warning_msg, 0) + 1
        elif str(fail_action).lower() == "error":
            if var_name is not None:
                msg = f"{var_name} was set to {value} but we expected {test_value}!"
                raise ValueError(msg)
            msg = f"A variable was set to {value} but we expected {test_value}!"
            raise ValueError(msg)
        if run_tests:
            return False, warnings_count
        return False
    if str(var_type).lower() in ["float", "int", "str", "list", "dict", "tuple", "bool"] and str(var_type).lower() != type(value).__name__:
        # Invalid class - return false
        if str(fail_action).lower() == "warning":
            warnings_count = {}
            if var_name is not None:
                warning_msg = f"{var_name} was a {type(value).__name__} but we expected a {str(var_type).lower()}. Output may be incorrect or incomplete!"
                warnings.warn(warning_msg)  # noqa: B028
                warnings_count["[WARNING]: " + warning_msg] = warnings_count.get("[WARNING]: " + warning_msg, 0) + 1
            else:
                warning_msg = f"A variable was a {type(value).__name__} but we expected a {str(var_type).lower()}. Output may be incorrect or incomplete!"
                warnings.warn(warning_msg)  # noqa: B028
                warnings_count["[WARNING]: " + warning_msg] = warnings_count.get("[WARNING]: " + warning_msg, 0) + 1
        elif str(fail_action).lower() == "error":
            if var_name is not None:
                msg = f"{var_name} was a {type(value).__name__} but we expected a {str(var_type).lower()}!"
                raise ValueError(msg)
            msg = f"A variable was a {type(value).__name__} but we expected a {str(var_type).lower()}!"
            raise ValueError(msg)
        if run_tests:
            return False, warnings_count
        return False
    # Valid value and is matching optional argument if provided - return true
    return True
