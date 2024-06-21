# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""AVD Jinja2 test contains.

The test checks if a list contains any of the value(s) passed in test_value.
"""

from __future__ import annotations

import warnings

from jinja2.runtime import Undefined


def defined(value, test_value=None, var_type=None, fail_action=None, var_name=None, run_tests=False):
    """
    defined - Ansible test plugin to test if a variable is defined and not none

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

    Returns
    -------
    boolean
        True if variable matches criteria, False in other cases.
    """
    if isinstance(value, Undefined) or value is None:
        # Invalid value - return false
        if str(fail_action).lower() == "warning":
            warnings_count = {}
            if var_name is not None:
                warning_msg = f"{var_name} was expected but not set. Output may be incorrect or incomplete!"
                warnings.warn(warning_msg)
                warnings_count["[WARNING]: " + warning_msg] = warnings_count.get("[WARNING]: " + warning_msg, 0) + 1
            else:
                warning_msg = "A variable was expected but not set. Output may be incorrect or incomplete!"
                warnings.warn(warning_msg)
                warnings_count["[WARNING]: " + warning_msg] = warnings_count.get("[WARNING]: " + warning_msg, 0) + 1
        elif str(fail_action).lower() == "error":
            if var_name is not None:
                raise ValueError(f"{var_name} was expected but not set!")
            else:
                raise ValueError("A variable was expected but not set!")
        if run_tests:
            return False, warnings_count
        return False

    if test_value is not None and value != test_value:
        # Valid value but not matching the optional argument
        if str(fail_action).lower() == "warning":
            warnings_count = {}
            if var_name is not None:
                warning_msg = f"{var_name} was set to {value} but we expected {test_value}. Output may be incorrect or incomplete!"
                warnings.warn(warning_msg)
                warnings_count["[WARNING]: " + warning_msg] = warnings_count.get("[WARNING]: " + warning_msg, 0) + 1
            else:
                warning_msg = f"A variable was set to {value} but we expected {test_value}. Output may be incorrect or incomplete!"
                warnings.warn(warning_msg)
                warnings_count["[WARNING]: " + warning_msg] = warnings_count.get("[WARNING]: " + warning_msg, 0) + 1
        elif str(fail_action).lower() == "error":
            if var_name is not None:
                raise ValueError(f"{var_name} was set to {value} but we expected {test_value}!")
            else:
                raise ValueError(f"A variable was set to {value} but we expected {test_value}!")
        if run_tests:
            return False, warnings_count
        return False
    if str(var_type).lower() in ["float", "int", "str", "list", "dict", "tuple", "bool"] and str(var_type).lower() != type(value).__name__:
        # Invalid class - return false
        if str(fail_action).lower() == "warning":
            warnings_count = {}
            if var_name is not None:
                warning_msg = f"{var_name} was a {type(value).__name__} but we expected a {str(var_type).lower()}. Output may be incorrect or incomplete!"
                warnings.warn(warning_msg)
                warnings_count["[WARNING]: " + warning_msg] = warnings_count.get("[WARNING]: " + warning_msg, 0) + 1
            else:
                warning_msg = f"A variable was a {type(value).__name__} but we expected a {str(var_type).lower()}. Output may be incorrect or incomplete!"
                warnings.warn(warning_msg)
                warnings_count["[WARNING]: " + warning_msg] = warnings_count.get("[WARNING]: " + warning_msg, 0) + 1
        elif str(fail_action).lower() == "error":
            if var_name is not None:
                raise ValueError(f"{var_name} was a {type(value).__name__} but we expected a {str(var_type).lower()}!")
            else:
                raise ValueError(f"A variable was a {type(value).__name__} but we expected a {str(var_type).lower()}!")
        if run_tests:
            return False, warnings_count
        return False
    else:
        # Valid value and is matching optional argument if provided - return true
        return True
