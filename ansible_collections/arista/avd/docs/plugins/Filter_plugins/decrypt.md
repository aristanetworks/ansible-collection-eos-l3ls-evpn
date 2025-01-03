---
# This title is used for search results
title: arista.avd.decrypt
---
<!--
  ~ Copyright (c) 2023-2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# decrypt

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.decrypt` when using this plugin.

Decrypt supported EOS passwords.

## Synopsis

The filter is used to decrypt supported EOS passwords into clear text.
Note - For now this filter only supports decryption from type `7` and not type `8a` for OSPF and BGP passwords.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>_input</samp> | string | True | None |  | Encrypted EOS password. |
| <samp>passwd_type</samp> | string | True | None | Valid values:<br>- <code>bgp</code><br>- <code>ospf_simple</code><br>- <code>ospf_message_digest</code><br>- <code>isis</code> | Type of password to decrypt.<br>`bgp` and `ospf_simple` requires the `password` and `key` inputs.<br>`ospf_message_digest` requires the `password`, `key`, `hash_algorithm`, `key_id` inputs.<br>`isis` requires the `password`, `key` and `isis_mode` inputs. |
| <samp>key</samp> | string | True | None |  | Encryption key. The value depends on the type of password.<br>For BGP passwords the key is the Neighbor IP or the BGP Peer Group Name in EOS.<br>For OSPF passwords the key is the interface name (e.g., `Ethernet1`).<br>For ISIS passwords the key is the ISIS instance name (from `router isis &lt;instance name&gt;` or `isis enable &lt;instance name&gt;`). |
| <samp>hash_algorithm</samp> | string | optional | None | Valid values:<br>- <code>md5</code><br>- <code>sha1</code><br>- <code>sha256</code><br>- <code>sha384</code><br>- <code>sha512</code> | Hash algorithm to use with `passwd_type=ospf_message_digest`. |
| <samp>key_id</samp> | integer | optional | None | Min value: <code>1</code><br>Max value: <code>255</code> | Key ID to use with `passwd_type=ospf_message_digest`. |
| <samp>isis_mode</samp> | string | optional | None | Valid values:<br>- <code>none</code><br>- <code>text</code><br>- <code>md5</code><br>- <code>sha</code><br>- <code>sha-1</code><br>- <code>sha-224</code><br>- <code>sha-256</code><br>- <code>sha-384</code><br>- <code>sha1-512</code> | ISIS encryption mode (`none`, `text`, `md5`, `sha`) or shared-secret algorithm (`sha-1`, `sha-224`, `sha-256`, `sha-384`, `sha1-512`). |

## Examples

```yaml
---
- # Decrypt BGP password for peer group "IPv4-UNDERLAY-PEERS"
  cleartext: "{{ encrypted_password | arista.avd.decrypt(passwd_type='bgp', key='IPv4-UNDERLAY-PEERS') }}"

- # Decrypt OSPF simple password for interface "Ethernet1"
  cleartext: "{{ encrypted_password | arista.avd.decrypt(passwd_type='ospf_simple', key='Ethernet1') }}"

- # Decrypt OSPF message digest password for Ethernet1, MD5 and key id 1
  cleartext: "{{ encrypted_password | arista.avd.decrypt(passwd_type='ospf_message_digest', key='Ethernet1', hash_algorithm='md5', key_id='1') }}"
```

## Return Values

| Name | Type | Description |
| ---- | ---- | ----------- |
| _value | string | Decrypted cleartext password. |

## Authors

- Arista Ansible Team (@aristanetworks)
