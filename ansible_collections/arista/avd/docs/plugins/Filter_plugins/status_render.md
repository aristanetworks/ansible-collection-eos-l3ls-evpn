---
# This title is used for search results
title: arista.avd.status_render
---
<!--
  ~ Copyright (c) 2023-2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# status_render

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.status_render` when using this plugin.

Convert Text to EMOJI code.

## Synopsis

Returns the input value unless `rendering` is set to &#34;github&#34;.

Returns `:x:` if input status string is `FAIL` and `rendering` is set to &#34;github&#34;.

Returns `:white_check_mark:` if input status string is `PASS` and `rendering` is set to &#34;github&#34;.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>_input</samp> | string | True | None |  | Text to convert to EMOJI. |
| <samp>rendering</samp> | string | True | None |  | Markdown Flavor to use for Emoji rendering. Only &#34;github&#34; is supported. |

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | string | Input value or GitHub Markdown emoji code. |

## Authors

- Arista Ansible Team (@aristanetworks)
