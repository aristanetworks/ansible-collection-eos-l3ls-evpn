---
# This title is used for search results
title: arista.avd.hide_passwords
---
<!--
  ~ Copyright (c) 2023-2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# hide_passwords

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.hide_passwords` when using this plugin.

Replace a value by &#34;&lt;removed&gt;&#34;

## Synopsis

Replace the input data by &#34;&lt;removed&gt;&#34; if the hide_passwords parameter is true

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>_input</samp> | raw | True | None |  | Value to replace. |
| <samp>hide_passwords</samp> | bool | True | None |  | Flag to indicate whether or not the string should be replaced. |

## Examples

```yaml
cli_with_hidden_password: "ip ospf authentication-key 7 {{ vlan_interface.ospf_authentication_key | arista.avd.hide_passwords(true) }}"
```

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | string | The original input or &#39;&lt;removed&gt;&#39; |

## Authors

- Arista Ansible Team (@aristanetworks)
