---
# This title is used for search results
title: Ansible Collection Role eos_config_deploy_eapi
---
<!--
  ~ Copyright (c) 2023-2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# eos_config_deploy_eapi

## Overview

**eos_config_deploy_eapi** is a role that deploys the configuration to Arista EOS devices.

The **eos_config_deploy_eapi** role:

- Designed to replace device running configuration with intended configuration.
- Backup configuration after a successful change.

## Role Inputs and Outputs

Figure 1 below provides a visualization of the role's inputs, outputs, and tasks in order executed by the role.

![Figure 1: Ansible Role eos_config_deploy_eapi](../../docs/_media/eos_config_deploy_eapi_dark.svg#only-dark)
![Figure 1: Ansible Role eos_config_deploy_eapi](../../docs/_media/eos_config_deploy_eapi_light.svg#only-light)

**Inputs:**

- Device configuration file in EOS CLI syntax.

**Outputs:**

- Device running configuration before configuration is replaced (snapshot).
- Device running configuration after configuration is replaced (backup).

**Tasks:**

1. Take a backup of the running configuration before configuration is replaced (pre) - (optional, default false).
   1. Destination: `{{ pre_running_config_backup_dir }}/{{ pre_running_config_backup_filename }}`
2. Replace configuration on device with intended EOS configuration. If changed, saves to startup-config, and notifies handler to backup configuration.
3. Backup Configuration after the configuration is replaced (post) with handler.
   1. Destination: `{{ post_running_config_backup_dir }}/{{ post_running_config_backup_filename }}`.

## Default Variables

``` yaml
--8<--
roles/eos_config_deploy_eapi/defaults/main.yml
--8<--
```

## Requirements

Requirements are located here: [avd-requirements](../../docs/installation/collection-installation.md#python-requirements-installation)

## License

Project is published under [Apache 2.0 License](../../LICENSE)
