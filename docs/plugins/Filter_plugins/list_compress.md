---
# This title is used for search results
title: arista.avd.list_compress
---
<!--
  ~ Copyright (c) 2023-2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# list_compress

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.list_compress` when using this plugin.

Compress a list of integers to a range string.

## Synopsis

Provides the capability to generate a string representing ranges of VLANs or VNIs.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>_input</samp> | list | True | None |  | List of integers to compress into a range. |

## Examples

```yaml
---
list1: "{{ [1,2,3,4,5] | arista.avd.list_compress }}" # -> "1-5"
list2: "{{ [1,2,3,7,8] | arista.avd.list_compress }}" # -> "1-3,7-8"
```

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | string | Range string like &#34;1-3,7-8&#34; |

## Authors

- Arista Ansible Team (@aristanetworks)
