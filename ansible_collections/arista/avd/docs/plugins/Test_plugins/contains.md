---
# This title is used for search results
title: arista.avd.contains
---
<!--
  ~ Copyright (c) 2023-2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# contains

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.contains` when using this plugin.

Test if a list contains one or more of the supplied values.

## Synopsis

The `arista.avd.contains` test will test if the passed list contains one or more of the supplied test_values.

The test accepts either a single test_value or a list of test_values.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>_input</samp> | list | True | None |  | List of items to test. |
| <samp>test_value</samp> | any | optional | None |  | Single item or list of items to test for in value. |

## Examples

```yaml
---
vars:
  mylist: ["test", "test2"]
  item_is_in_my_list: "{{ mylist is arista.avd.contains('test') }}"
  any_item_is_in_my_list: "{{ mylist is arista.avd.contains(['test2', 'test3']) }}"
  platform_settings: "{{ platform_settings | selectattr('platforms', 'arista.avd.contains', switch_platform) }}"
```

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | boolean | Returns `False` if either the passed value or the test_values are `Undefined` or `none`.<br>Returns `True` if the passed list contains one or more of the supplied test_values. `False` otherwise. |

## Authors

- Arista Ansible Team (@aristanetworks)
