---
# This title is used for search results
title: arista.avd.is_in_filter
---
<!--
  ~ Copyright (c) 2023-2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# is_in_filter

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.is_in_filter` when using this plugin.

Returns `True` if the input hostname matches the `hostname_filter`.

## Synopsis

The filter matches if any filter strings are found in the input hostname.
`hostname_filter=[all]` or `hostname_filter=none` will match all hostnames.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>_input</samp> | string | True | None |  | One hostname to match with `hostname_filter`. |
| <samp>hostname_filter</samp> | any | True | None |  | Filter as a list of strings or `None`. |

## Examples

```yaml
---
found_all_1: "{{ 'myhostname' | arista.avd.is_in_filter(['all']) }}"
found_all_2: "{{ 'myhostname' | arista.avd.is_in_filter(none) }}"
found_1: "{{ 'myhostname' | arista.avd.is_in_filter(['my']) }}"
found_2: "{{ 'myhostname' | arista.avd.is_in_filter(['hostname']) }}"
not_found_1: "{{ 'myhostname' | arista.avd.is_in_filter(['myhost1', 'MYhostname']) }}"
```

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | boolean | `True` if the input hostname matches the `hostname_filter`. Otherwise `False` |

## Authors

- Arista Ansible Team (@aristanetworks)
