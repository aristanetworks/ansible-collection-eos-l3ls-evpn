---
# This title is used for search results
title: arista.avd.secure_hash
---
<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# secure_hash

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.secure_hash` when using this plugin.

Generate a sha512 password hash for a local user

## Synopsis

Generate a SHA512-Crypt password hash with a random salt value for a local user.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>_input</samp> | string | True | None |  | Clear text password to be hashed. |

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | string | the SHA512-Crypt password hash. |

## Authors

- Arista Ansible Team (@aristanetworks)
