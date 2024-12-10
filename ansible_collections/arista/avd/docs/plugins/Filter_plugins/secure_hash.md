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

Generate a SHA-512 password hash for an EOS user.

## Synopsis

This filter generates a SHA-512 password hash from a cleartext password for a local user. A randomly generated salt will be used unless the user specifies one.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>_input</samp> | string | True | None |  | Clear text password to be hashed. |
| <samp>salt</samp> | string | optional | None |  | Salt value to be used when creating password hash.<br>The salt value can only contain the characters `./`, digits `0-9`, and uppercase or lowercase letters `A-Z a-z`.<br>The salt value should not be greater than 16 characters long.<br>If a salt value is not included then a random salt will be generated. |

## Examples

```yaml
---
local_users:
  # Create sha512 password hash with random salt. Note: this will create a new hash each time it is run
  - name: admin
    sha512_password: "{{ 'password123' | arista.avd.secure_hash }}"

  # Create sha512 password hash with user defined salt value
  - name: cvpadmin
    sha512_password: "{{ 'securepassword' | arista.avd.secure_hash(salt='Yar49ahkzKddRVYS') }}"
```

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | string | the SHA512-Crypt password hash. |

## Authors

- Arista Ansible Team (@aristanetworks)
