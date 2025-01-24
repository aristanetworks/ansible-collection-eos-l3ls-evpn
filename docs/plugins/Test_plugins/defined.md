---
# This title is used for search results
title: arista.avd.defined
---
<!--
  ~ Copyright (c) 2023-2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# defined

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.defined` when using this plugin.

Test if the value is not `Undefined` or `None`.

## Synopsis

The `arista.avd.defined` test returns `False` if the passed value is `Undefined` or `None`. Else it will return `True`.

The `arista.avd.defined` test also accepts an optional `test_value` argument to test if the value equals this.

The optional `var_type` argument can also be used to test if the variable is of the expected type.

Optionally, the test can emit warnings or errors if the test fails.

Compared to the built-in `is defined` test, this test will also test for `None` and can even test for a specific value or class.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>_input</samp> | any | True | None |  | Value to test |
| <samp>test_value</samp> | any | optional | None |  | Value to match for in addition to defined and not none |
| <samp>var_type</samp> | string | optional | None | Valid values:<br>- <code>float</code><br>- <code>int</code><br>- <code>str</code><br>- <code>list</code><br>- <code>dict</code><br>- <code>tuple</code><br>- <code>bool</code> | Type or Class to test for |
| <samp>fail_action</samp> | string | optional | None | Valid values:<br>- <code>warning</code><br>- <code>error</code> | Optional action if a test fails to emit a Warning or Error |
| <samp>var_name</samp> | string | optional | None |  | Optional string to use as a variable name in warning or error messages |

## Examples

```yaml
# Test if "my_var" is defined and not none:
is_defined_and_not_none: "{{ my_var is arista.avd.defined }}"

# Test if "my_var" is defined, not none and has value "something"
is_defined_and_set_to_something: "{{ my_var is arista.avd.defined('something') }}"

# Test if "my_var" is defined and if not print a warning message with the variable name
test_result: "{{ my_dict.my_list[12].my_var is arista.avd.defined(fail_action='warning', var_name='my_dict.my_list[12].my_var' }}"
# Output >>> [WARNING]: my_dict.my_list[12].my_var was expected but not set. Output may be incorrect or incomplete!
```

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | boolean | Returns `False` if the passed value is `Undefined` or `None` or if any of the optional checks fail. Otherwise `True`. |

## Authors

- Arista Ansible Team (@aristanetworks)
