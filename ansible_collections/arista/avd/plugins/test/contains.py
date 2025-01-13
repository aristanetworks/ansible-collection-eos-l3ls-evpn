# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

"""
arista.avd.contains test plugin.

Example:
A = [1, 2]
B = [3, 4]
C = [2, 3]

Jinja test examples:
{% if A is arista.avd.contains(B) %}  =>  false
{% if B is arista.avd.contains(C) %}  =>  true
{% if C is arista.avd.contains(A) %}  =>  true
{% if C is arista.avd.contains(B) %}  =>  true
{% if A is arista.avd.contains(0) %}  =>  false
{% if B is arista.avd.contains(1) %}  =>  false
{% if C is arista.avd.contains(2) %}  =>  true
{% if D is arista.avd.contains(3) %}  =>  false <- Protecting against undefined gracefully.
"""

from ansible.errors import AnsibleFilterError

from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse, wrap_test

PLUGIN_NAME = "arista.avd.contains"

try:
    from pyavd.j2tests.contains import contains
except ImportError as e:
    contains = RaiseOnUse(
        AnsibleFilterError(
            f"The '{PLUGIN_NAME}' plugin requires the 'pyavd' Python library. Got import error",
            orig_exc=e,
        ),
    )


DOCUMENTATION = r"""
---
name: contains
collection: arista.avd
author: Arista Ansible Team (@aristanetworks)
version_added: "2.0"
short_description: Test if a list contains one or more of the supplied values.
description:
  - The `arista.avd.contains` test will test if the passed list contains one or more of the supplied test_values.
  - The test accepts either a single test_value or a list of test_values.
positional: _input
options:
  _input:
    description: List of items to test.
    type: list
    required: true
  test_value:
    description: Single item or list of items to test for in value.
    default: None
"""

EXAMPLES = r"""
---
vars:
  mylist: ["test", "test2"]
  item_is_in_my_list: "{{ mylist is arista.avd.contains('test') }}"
  any_item_is_in_my_list: "{{ mylist is arista.avd.contains(['test2', 'test3']) }}"
  platform_settings: "{{ platform_settings | selectattr('platforms', 'arista.avd.contains', switch_platform) }}"
"""

RETURN = r"""
---
_value:
  description:
    - Returns `False` if either the passed value or the test_values are `Undefined` or `none`.
    - Returns `True` if the passed list contains one or more of the supplied test_values. `False` otherwise.
  type: boolean
"""


class TestModule:
    def tests(self) -> dict:
        return {"contains": wrap_test(PLUGIN_NAME)(contains)}
