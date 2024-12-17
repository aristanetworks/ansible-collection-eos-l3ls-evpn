---
# This title is used for search results
title: Ansible Collection Role cvp_configlet_upload
---
<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# cvp_configlet_upload

## Overview

**cvp_configlet_upload**, is a role that deploys configlets stored in a local folder to the CloudVision server.

## Role requirements

This role requires to install `arista.cvp` collection to support CloudVision interactions.

```shell
ansible-galaxy collection install arista.cvp
```

## Role Inputs and Outputs

Figure 1 below provides a visualization of the role's inputs, outputs, and tasks in order executed by the role.

![Figure 1: Ansible Role cvp_configlet_upload](../../docs/_media/cvp_configlet_upload_dark.svg#only-dark)
![Figure 1: Ansible Role cvp_configlet_upload](../../docs/_media/cvp_configlet_upload_light.svg#only-light)

1. Read content of `{{ configlet_directory }}` and create **cv_configlet** input structure.
2. Collect CloudVision facts.
3. Create or update configlets on CloudVision server with content from `{{ configlet_directory }}`

### Inputs

#### Inventory configuration

An entry must be part of the inventory to describe the CloudVision server. `arista.cvp` modules use the httpapi approach. The example below provides a framework to use in your inventory.

```yaml
all:
  children:
    cloudvision:
      hosts:
        cv_server01:
          ansible_host: 10.83.28.164
          ansible_user: ansible
          ansible_password: ansible
          ansible_connection: httpapi
          ansible_httpapi_use_ssl: true
          ansible_httpapi_validate_certs: false
          ansible_network_os: eos
          ansible_httpapi_port: 443
```

For complete list of authentication options available with CloudVision Ansible collection, you can read dedicated page on [arista.cvp collection](https://cvp.avd.sh/en/latest/docs/how-to/cvp-authentication/).

#### Module variables

- **`configlet_directory`**: Folder where local configlets are stored. Default: `configlets`.
- **`file_extension`**: File extension to look for configlet in their local folder. Default: `conf`.
- **`configlets_cvp_prefix`**: Prefix to use for configlet on CV side. Default: *Not set* and it's required.
- **`execute_tasks`**:  `true` / `false`. Support automatically executing pending tasks. Default: `false`.
- **`cv_collection`**: Version of CloudVision collection to use. Can be `v1` or `v3`. Default is `v3`.

*Example*:

```yaml
tasks:
  - name: Upload cvp configlets
    ansible.builtin.import_role:
        name: arista.avd.cvp_configlet_upload
    vars:
      configlet_directory: 'configlets/'
      file_extension: 'txt'
      configlets_cvp_prefix: 'DC1-AVD'
      execute_tasks: false
      cv_collection: v3
```

This module also supports tags to run a subset of ansible tasks:

- **`build`**: Generate `cv_configlet` input structure.
- **`provision`**: Run `build` tags + configure CloudVision with information generated in previous tasks

```shell
ansible-playbook playbook.to.deploy.with.cvp.yml --tags "provision"
```

#### Outputs

- None.

### Tasks

1. Read content of `{{ configlet_directory }}` and create **cv_configlet** input structure.
2. Collect CloudVision facts.
3. Create or update configlets on CloudVision server with content from `{{ configlet_directory }}`

## Requirements

Requirements are located here: [avd-requirements](../../docs/installation/collection-installation.md#python-requirements-installation)

## License

Project is published under [Apache 2.0 License](../../LICENSE)
