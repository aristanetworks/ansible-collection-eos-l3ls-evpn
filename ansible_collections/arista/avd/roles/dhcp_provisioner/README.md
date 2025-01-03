---
# This title is used for search results
title: Ansible Collection Role dhcp_provisioner
---
<!--
  ~ Copyright (c) 2023-2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# dhcp_provisioner

## Overview

**dhcp_provisioner** is a role to build and deploy a DHCP configuration file to support Zero Touch Provisioning with Arista EOS devices.

!!! tip
    The role supports two modes: `offline` and `online`:

- `Offline` mode let you generate a configuration you can apply on your DHCP server after carefully reviewing it.
- `Online` mode lets you generate and push configuration to CloudVision, RHEL, or Ubuntu-based Linux systems.

## Role requirements

This role requires installing the `arista.cvp` collection to support CloudVision interactions.

```shell
ansible-galaxy collection install arista.cvp
```

## Role Inputs and Outputs

### Inputs

#### Inventory configuration

An entry must be part of the inventory to describe DHCP server.

```yaml
all:
  children:
    TOOLS:
      hosts:
        dhcp_server01:
```

#### Module variables

#### Variables dedicated to DHCP device

- **`fabric_group`**: Ansible group where devices are defined per type.
- **`ztp_network_summary`**: Subnet where DHCP will listen for request.
- **`ztp_pool_start`**: First IP available in the pool.
- **`ztp_pool_end`**: Last IP available in the pool.
- **`ztp_lease_time`**: Maximum lease time before devices lose IP. Renewal is max/2 (default is 300 sec).
- **`ztp_mac_source`**: Define which mac-address field is used for identification: interface mac-address (`interface`) or system-mac-address (`system`). Default: `system`
- **`ztp_mode`**: Define how role works either `offline` or `online` (Default `offline`).
- **`avd_dhcp_provisioner_provision`**: Run `arista.cvp.dhcp_configuration` in either online or offline mode (Default `true`).

*Example*:

```yaml
---
- name: Build Switch configuration
  hosts: TOOLS
  connection: local
  gather_facts: false
  tasks:
    - name: Create dhcp configuration file
      ansible.builtin.import_role:
        name: arista.avd.dhcp_provisioner
      vars:
        ztp_network_summary: 10.73.1.0/24
        ztp_pool_start: 10.73.1.200
        ztp_pool_end: 10.73.1.210
        ztp_lease_time: 300
        fabric_group: 'DC1_FABRIC'
        ztp_mac_source: system
```

This module also reads information from the fabric definition. For any node defined under **spine**, **l3leaf**, and **l2leaf**, the role generates a DHCP entry if mac-address is found. Entry is based on the following fields:

- **`mgmt_ip`**: Management IP set as per `eos_designs`.
- **`mac_address`**: MAC address used for DHCP. It can be either interface mac-address or system-mac-address.

```yaml
# Spine Switches
spine:
  platform: vEOS-LAB
  bgp_as: 65001
  # defines the range of acceptable remote ASNs from leaf switches
  nodes:
    AVD2-SPINE1:
      id: 1
      mgmt_ip: 10.73.254.1/24
      mac_address: '0c:1d:c0:1d:62:01'
    AVD2-SPINE2:
      id: 2
      mgmt_ip: 10.73.254.2/24
      mac_address: '0c:1d:c0:1d:62:02'
```

This module also uses the `cvp_instance_ip` or `cvp_instance_ips` knobs to set correct registration URL. In case you need to extend the TerminAttr daemon, you should use an approach similar to the following code:

```yaml
cvp_instance_ips:
  - < cvp instance 01 >
  - < cvp instance 02 >
  - < cvp instance 03 >
cvp_ingestauth_key: < Fake ingest key overwritten by custom_structured_configuration >

# CloudVision server information
custom_structured_configuration_daemon_terminattr:
  cvauth:
    method: "token"
    token_file: "< path to the token file >"
```

#### Outputs

- DHCP configuration file under `intended/configs/dhcpd.conf`

### Tasks

1. Generate structured configuration for DHCP configuration as documented in [`arista.cvp.dhcp_configuration`](https://cvp.avd.sh/en/latest/roles/dhcp_configuration/).
2. Load generated variables.
3. Create DHCP configuration file.
4. If mode is online, apply configuration to DHCP server.

## Requirements

Requirements are located here: [avd-requirements](../../docs/installation/collection-installation.md#python-requirements-installation)

## License

Project is published under [Apache 2.0 License](../../LICENSE)
