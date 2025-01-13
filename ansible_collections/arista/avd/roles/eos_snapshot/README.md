---
# This title is used for search results
title: Ansible Collection Role eos_snapshot
---
<!--
  ~ Copyright (c) 2023-2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# eos_snapshot

## Overview

**eos_snapshot** is a role leveraged to collect commands on Arista EOS devices and generate a report.
It supports reports with the following format: text, markdown, JSON, and YAML.

## Role Inputs and Outputs

Figure 1 below visualizes the role's inputs, outputs, and tasks.

![Figure 1: Ansible Role eos_snapshot](../../docs/_media/eos_snapshot_dark.svg#only-dark)
![Figure 1: Ansible Role eos_snapshot](../../docs/_media/eos_snapshot_light.svg#only-light)

**Inputs:**

Ansible inventory to connect to EOS devices. The default variables can be changed to select a report format and include others commands.

**Outputs:**

- Text files: one file per device and show command
- Markdown file: one report per device
- JSON file: one report per fabric
- YAML file: one report per fabric

**Tasks:**

1. Create output structure
2. Collect show commands on device
3. Save the collected commands
4. Generate a JSON report
5. Generate a YAML report
6. Generate a markdown report

## Default Variables

The following default variables are defined, and can be modified as desired:

```yaml
---

root_dir: '{{ inventory_dir }}'
snapshots_backup_dir_name: 'commands'
snapshots_backup_dir: '{{ root_dir }}/{{ commands_backup_dir_name }}'

# list of desired formats. Supported values are markdown, json and text.
# text: one file per device and show command
# markdown: one report per device
# json: one report per fabric
# yaml: one report per fabric
output_format:
 - text
 - markdown
 # - json
 # - yaml

commands_list:
  - show lldp neighbors
  - show ip interface brief
  - show interfaces description
  - show version
  - show running-config
```

## Requirements

Requirements are located here: [avd-requirements](../../docs/installation/collection-installation.md#python-requirements-installation)

## Example Playbook

```yaml
---
- name: Collect commands
  hosts: DC1_FABRIC
  connection: local
  gather_facts: false
  collections:
    - arista.avd
  tasks:
    - name: Collect commands
      ansible.builtin.import_role:
        name: eos_snapshot
```

## Input example

### inventory/inventory.ini

```yaml
---
all:
  children:
    DC1:
      children:
        DC1_FABRIC:
          children:
            DC1_SPINES:
              hosts:
                switch2:
                  ansible_host: 10.83.28.190
            DC1_L3LEAFS:
              children:
                DC1_LEAF1:
                  hosts:
                    switch1:
                      ansible_host: 10.83.28.216
                DC1_LEAF2:
                  hosts:
                    switch3:
                      ansible_host: 10.83.28.191
```

### inventory/group_vars/DC1.yml

```yaml
ansible_user: 'arista'
ansible_password: 'arista'
ansible_network_os: eos
ansible_become: true
ansible_become_method: enable
```

```yaml
output_format:
 - text
 - markdown
 # - json
 # - yaml

commands_list:
  - show lldp neighbors
  - show ip interface brief
  - show interfaces description
  - show version
  - show running-config
```

## Usage example

```shell
ansible-playbook playbooks/pb_collect_yml --inventory inventory/inventory.yml
```

## License

Project is published under [Apache 2.0 License](../../LICENSE)
