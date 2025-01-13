---
# This title is used for search results
title: arista.avd.inventory_to_container
---
<!--
  ~ Copyright (c) 2023-2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# inventory_to_container

!!! note
    Always use the FQCN (Fully Qualified Collection Name) `arista.avd.inventory_to_container` when using this plugin.

Transform information from inventory to arista.cvp collection

## Synopsis

Transform information from ansible inventory to be able to provision CloudVision Platform using arista.cvp collection and its specific data structure.

## Parameters

| Argument | Type | Required | Default | Value Restrictions | Description |
| -------- | ---- | -------- | ------- | ------------------ | ----------- |
| <samp>inventory</samp> | str | False | None |  | Optional YAML inventory file to parse. If not set the loaded inventory will be parsed. |
| <samp>container_root</samp> | str | True | None |  | Ansible group name to consider to be Root of our topology. |
| <samp>configlet_dir</samp> | str | False | None |  | Directory where intended configurations are located. |
| <samp>configlet_prefix</samp> | str | False | AVD |  | Prefix to put on configlet. |
| <samp>destination</samp> | str | False | None |  | Optional path to save variable. |
| <samp>device_filter</samp> | list | False | ['all'] |  | Filter to apply intended mode on a set of configlet. If not used, then module only uses ADD mode. device_filter list devices that can be modified or deleted based on configlets entries. |

## Examples

```yaml
- name: generate intended variables
  inventory_to_container:
    inventory: 'inventory.yml'
    container_root: 'DC1_FABRIC'
    configlet_dir: 'intended_configs'
    configlet_prefix: 'AVD'
    device_filter: ['DC1-LE']
    # destination: 'generated_vars/{{ inventory_hostname }}.yml'
  register: cvp_vars

- name: 'Collecting facts from CVP {{ inventory_hostname }}.'
  arista.cvp.cv_facts:
  register: cvp_facts

- name: 'Create configlets on CVP {{ inventory_hostname }}.'
  arista.cvp.cv_configlet:
    cvp_facts: "{{ cvp_facts.ansible_facts }}"
    configlets: "{{ cvp_vars.cvp_configlets }}"
    configlet_filter: ["AVD"]

- name: "Building Container topology on {{ inventory_hostname }}"
  arista.cvp.cv_container:
    topology: '{{ cvp_vars.cvp_topology }}'
    cvp_facts: '{{ cvp_facts.ansible_facts }}'
    save_topology: true
```

## Authors

- Ansible Arista Team (@aristanetworks)
