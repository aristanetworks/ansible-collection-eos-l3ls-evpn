# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

"""
arista.avd.defined test plugin.

Example:
A is undefined
B is none
C is "c"
D is "d"

Jinja test examples:
{% if A is arista.avd.defined %}  =>  false
{% if B is arista.avd.defined %}  =>  false
{% if C is arista.avd.defined %}  =>  true
{% if D is arista.avd.defined %}  =>  true
{% if A is arista.avd.defined("c") %}  =>  false
{% if B is arista.avd.defined("c") %}  =>  false
{% if C is arista.avd.defined("c") %}  =>  true
{% if D is arista.avd.defined("c") %}  =>  false
"""

from ansible.errors import AnsibleTemplateError

from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse, wrap_test

PLUGIN_NAME = "arista.avd.defined"

try:
    from pyavd.j2tests.defined import defined
except ImportError as e:
    defined = RaiseOnUse(
        AnsibleTemplateError(
            f"The '{PLUGIN_NAME}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        ),
    )


DOCUMENTATION = r"""
---
name: defined
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "2.0"
short_description: Test if the value is not `Undefined` or `None`.
description:
  - The `arista.avd.defined` test returns `False` if the passed value is `Undefined` or `None`. Else it will return `True`.
  - The `arista.avd.defined` test also accepts an optional `test_value` argument to test if the value equals this.
  - The optional `var_type` argument can also be used to test if the variable is of the expected type.
  - Optionally, the test can emit warnings or errors if the test fails.
  - Compared to the built-in `is defined` test, this test will also test for `None` and can even test for a specific value or class.
positional: _input
options:
  _input:
    description: Value to test
    required: true
  test_value:
    description: Value to match for in addition to defined and not none
    default: None
  var_type:
    type: string
    description: Type or Class to test for
    choices: ['float', 'int', 'str', 'list', 'dict', 'tuple', 'bool']
  fail_action:
    type: string
    description: Optional action if a test fails to emit a Warning or Error
    choices: ['warning', 'error']
  var_name:
    type: string
    description: Optional string to use as a variable name in warning or error messages
"""

EXAMPLES = r"""
# Test if "my_var" is defined and not none:
is_defined_and_not_none: "{{ my_var is arista.avd.defined }}"

# Test if "my_var" is defined, not none and has value "something"
is_defined_and_set_to_something: "{{ my_var is arista.avd.defined('something') }}"

# Test if "my_var" is defined and if not print a warning message with the variable name
test_result: "{{ my_dict.my_list[12].my_var is arista.avd.defined(fail_action='warning', var_name='my_dict.my_list[12].my_var' }}"
# Output >>> [WARNING]: my_dict.my_list[12].my_var was expected but not set. Output may be incorrect or incomplete!
"""

RETURN = r"""
---
_value:
  description:
    - Returns `False` if the passed value is `Undefined` or `None` or if any of the optional checks fail. Otherwise `True`.
  type: boolean
"""


class TestModule:
    def tests(self) -> dict:
        return {"defined": wrap_test(PLUGIN_NAME)(defined)}
