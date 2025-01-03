---
# This title is used for search results
title: arista.avd.default
---
<!--
  ~ Copyright (c) 2023-2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# default

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.default` when using this plugin.

Returns input value if defined and is not none. Otherwise, return default value.

## Synopsis

The `arista.avd.default` filter can provide the same essential capability as the built-in `default` filter.
It will return the input value only if it&#39;s valid and, if not, provide a default value instead.
Our custom filter requires a value to be `not undefined` and `not None` to pass through.
Furthermore, the filter allows multiple default values as arguments, which will undergo the same validation until we find a valid default value.
As a last resort, the filter will return `None`.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>_input</samp> | any | True | None |  | Default value to check. Will be returned untouched if `not undefined` and `not None`. |
| <samp>default_values</samp> | any | optional | None |  | One or more default values will be tested individually, and the first valid value will be used. |

## Examples

```yaml
---
myvalue: "{{ variable | arista.avd.default(default_value_1, default_value_2) }}"
```

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | any | Input value if `not undefined` and `not None`. Otherwise, return the first defined default value or `None`. |

## Authors

- Arista Ansible Team (@aristanetworks)
