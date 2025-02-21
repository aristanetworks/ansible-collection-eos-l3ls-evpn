---
# This title is used for search results
title: Single Data Center - L3LS
---
<!--
  ~ Copyright (c) 2023-2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->

# Single Data Center - L3LS

## Introduction

This example is meant to be used as the logical second step in introducing AVD to new users, directly following the [Introduction to Ansible and AVD](../../../../../docs/getting-started/intro-to-ansible-and-avd.md) section. New users with access to virtual switches (using Arista vEOS-lab or cEOS) can learn how to generate configuration and documentation for a complete fabric environment. Users with access to physical switches will have to adapt a few settings. This is all documented inline in the comments included in the YAML files. If a lab with virtual or physical switches is not accessible, this example can be used only to generate the output from AVD if required.

The example includes and describes all the AVD files and their content used to build an L3LS EVPN/VXLAN Symmetric IRB network covering a single DC using the following:

- Two (virtual) spine switches.
- Two sets of (virtual) leaf switches, serving endpoints such as servers.
- Two (virtual) layer2-only switches, often used for server management connectivity.

Ansible playbooks are included to show the following:

- Building the intended configuration and documentation
- Deploying the configuration directly to the switches using eAPI
- Deploying the configuration via CloudVision to the switches, including a full change-based workflow with rollback capability etc.

## Installation

--8<--
ansible_collections/arista/avd/examples/common/example-installation.md
--8<--

```shell
ansible-avd-examples/ (or wherever the playbook was run)
  |── single-dc-l3ls
    ├── ansible.cfg
    ├── documentation
    ├── group_vars
    ├── images
    ├── intended
    ├── inventory.yml
    ├── build.yml
    ├── deploy.yml
    ├── deploy-cvp.yml
    ├── README.md
    └── switch-basic-configurations
```

## Overall design overview

### Physical topology

The drawing below shows the physical topology used in this example. The interface assignment shown here are referenced across the entire example, so keep that in mind if this example must be adapted to a different topology. Finally, the Ansible host is connected to the dedicated out-of-band management port (Ethernet0 when using vEOS-lab):

![Figure: Arista Leaf Spine physical topology](images/avd-single-dc-l3ls-example.svg)

### IP ranges used

| Out-of-band management IP allocation for DC1        | 172.16.1.0/24               |
|-----------------------------------------------------|-----------------------------|
| Default gateway                                     | 172.16.1.1                  |
| dc1-spine1                                          | 172.16.1.11                 |
| dc1-spine2                                          | 172.16.1.12                 |
| dc1-leaf1a                                          | 172.16.1.101                |
| dc1-leaf1b                                          | 172.16.1.102                |
| dc1-leaf2a                                          | 172.16.1.103                |
| dc1-leaf2b                                          | 172.16.1.104                |
| dc1-leaf1c                                          | 172.16.1.151                |
| dc1-leaf2c                                          | 172.16.1.152                |
| **Point-to-point links between leaf and spine**     | **(Underlay)**              |
| DC1                                                 | 10.255.255.0/26             |
| **Loopback0 interfaces used for EVPN peering**      | 10.255.0.0/27               |
| **Loopback1 interfaces used for VTEP**              | **(Leaf switches)**         |
| DC1                                                 | 10.255.1.0/27               |
| **VTEP Loopbacks used for diagnostics**             | **(Leaf switches)**         |
| VRF10                                               | 10.255.10.0/27              |
| VRF11                                               | 10.255.11.0/27              |
| **SVIs (interface vlan...)**                        | **10.10.`<VLAN-ID>`.0/24**  |
| For example `interface VLAN11` has the IP address:  | 10.10.11.1                  |
| **MLAG Peer-link (interface vlan 4094)**            | **(Leaf switches)**         |
| DC1                                                 | 10.255.1.64/27              |
| **MLAG iBGP Peering (interface vlan 4093)**         | **(Leaf switches)**         |
| DC1                                                 | 10.255.1.96/27              |
| **CloudVision Portal**                              |                             |
| cvp                                                 | 192.168.1.12                |

### BGP design

=== "Underlay"

    ![Figure: Arista Underlay BGP Design](images/bgp-underlay.svg)

=== "Overlay"

    ![Figure: Arista Underlay BGP Design](images/bgp-overlay.svg)

### Basic EOS config

Basic connectivity between the Ansible host and the switches must be established before Ansible can be used to push configurations. You must configure the following on all switches:

- A hostname configured purely for ease of understanding.
- An IP enabled interface - in this example, the dedicated out-of-band management interface is used.
- A username and password with the proper access privileges.

Below is the basic configuration file for `dc1-leaf1a`:

```eos title="dc1-leaf1a-basic-configuration.txt"
--8<--
ansible_collections/arista/avd/examples/single-dc-l3ls/switch-basic-configurations/dc1-leaf1a-basic-configuration.txt
--8<--
```

!!! note
    The folder `single-dc-l3ls/switch-basic-configurations/` contains a file per device for the initial configurations.

## Ansible inventory, group vars, and naming scheme

The following drawing shows a graphic overview of the Ansible inventory, group variables, and naming scheme used in this example:

![Figure: Ansible inventory and vars](images/ansible-groups.svg)

!!! note
    The two servers `dc1-leaf1-server1` and `dc1-leaf2-server1` at the bottom are **not** configured by AVD, but the switch ports used to connect to the servers are.

Group names use uppercase and underscore syntax:

- CLOUDVISION
- FABRIC
- DC1
- DC1_SPINES
- DC1_L3_LEAVES
- DC1_L2_LEAVES

All hostnames use lowercase and dashes, for example:

- cvp
- dc1-spine1
- dc1-leaf1a
- dc1-leaf2c

The drawing also shows the relationships between groups and their children:

- For example, `dc1-spine1` and `dc1-spine2` are both children of the group called `DC1_SPINES`.

Additionally, groups themselves can be children of another group, for example:

- `DC1_L3_LEAVES` is a group consisting of the groups `DC1_LEAF1` and `DC1_LEAF2`
- `DC1_L3_LEAVES` is also a child of the group `DC1`.

This naming convention makes it possible to extend anything easily, but as always, this can be changed based on your preferences. Just ensure that the names of all groups and hosts are unique.

### Content of the inventory.yml file

This section describes the entire `ansible-avd-examples/single-dc-l3ls/inventory.yml` file used to represent the above topology.

It is important that the hostnames specified in the inventory exist either in DNS or in the hosts file on your Ansible host to allow successful name lookup and be able to reach the switches directly. A successful ping from the Ansible host to each inventory host verifies name resolution(e.g., `ping dc1-spine1`).

Alternatively, if there is no DNS available, or if devices need to be reached using a fully qualified domain name (FQDN), define `ansible_host` to be an IP address or FQDN for each device - see below for an example:

```yaml title="inventory.yml"
--8<--
ansible_collections/arista/avd/examples/single-dc-l3ls/inventory.yml
--8<--
```

The above is what is included in this example, *purely* to make it as simple as possible to get started. However, in the future, please do not carry over this practice to a production environment, where an inventory file for an identical topology should look as follows when using DNS:

```yaml title="inventory.yml"
--8<--
examples/single-dc-l3ls/inventory_without_ip.yml
--8<--
```

1. `CLOUDVISION`

   - Defines the relevant values required to enable communication with CloudVision.

   - Specifically the hostname (`cvp`) of the CloudVision Portal server used, the username (`ansible`) and password (`ansible`), connection method (`httpapi`), SSL and certificate settings.

   - Please note that the username (`ansible`) and password (`ansible`) defined here must exist in CloudVision.

   - More information is available [here](https://avd.arista.com/stable/roles/eos_config_deploy_cvp/index.html?h=is_deployed#inputs)

2. `NETWORK_SERVICES`

    - Creates a group named `NETWORK_SERVICES`. Ansible variable resolution resolves this group name to the identically named group_vars file (`ansible-avd-examples/single-dc-l3ls/group_vars/NETWORK_SERVICES.yml`).

    - The file's contents, which in this case are specifications of VRFs and VLANs, are then applied to the group's children. In this case, the two groups `DC1_L3_LEAVES` and `DC1_L2_LEAVES`.

3. `CONNECTED_ENDPOINTS`

    - Creates a group named `CONNECTED_ENDPOINTS`. Ansible variable resolution resolves this group name to the identically named group_vars file (`ansible-avd-examples/single-dc-l3ls/group_vars/CONNECTED_ENDPOINTS.yml`).

    - The file's contents, which in this case are specifications of connected endpoints (typically servers), are then applied to the children of the group, in this case, the two groups `DC1_L3_LEAVES` and `DC1_L2_LEAVES`.

## Defining device types

Since this example covers building an L3LS network, AVD must know about the device types, for example, spines, L3 leaves, L2 leaves, etc. The devices are already grouped in the inventory, so the device types are specified in the group variable files with the following names and content:

=== "spines.yml"

    ```yaml
    --8<--
    ansible_collections/arista/avd/examples/single-dc-l3ls/group_vars/DC1_SPINES.yml
    --8<--
    ```

=== "l3_leaves.yml"

    ```yaml
    --8<--
    ansible_collections/arista/avd/examples/single-dc-l3ls/group_vars/DC1_L3_LEAVES.yml
    --8<--
    ```

=== "l2_leaves.yml"

    ```yaml
    --8<--
    ansible_collections/arista/avd/examples/single-dc-l3ls/group_vars/DC1_L2_LEAVES.yml
    --8<--
    ```

For example, all switches that are children of the DC1_SPINES group defined in the inventory will be of type `spine`.

## Setting fabric-wide configuration parameters

The `ansible-avd-examples/single-dc-l3ls/group_vars/FABRIC` folder contain files that defines generic settings that apply to all children of the `FABRIC` group as specified in the inventory described earlier.

The first file defines how the Ansible host connects to the devices:

```yaml title="fabric_ansible_connectivity.yml"
--8<--
examples/single-dc-l3ls/group_vars/FABRIC/fabric_ansible_connectivity.yml
--8<--
```

The following section specifies variables that generate configuration to be applied to all devices in the fabric:

```yaml title="fabric_variables.yml"
--8<--
examples/single-dc-l3ls/group_vars/FABRIC/fabric_variables.yml
--8<--
```

## Setting device specific configuration parameters

The `ansible-avd-examples/single-dc-l3ls/group_vars/DCI/dc1.yml` file defines settings that apply to all children of the `DC1` group as specified in the inventory described earlier. However, this time the settings defined are no longer fabric-wide but are limited to DC1. This example is of limited benefit with only a single data center. Still, it allows us to scale the configuration to a scenario with multiple data centers in the future.

```yaml title="dc1.yml"
--8<--
examples/single-dc-l3ls/group_vars/DC1/dc1.yml
--8<--
```

The `ansible-avd-examples/single-dc-l3ls/group_vars/DC1_SPINES/spines.yml` covers the spine switches.

```yaml title="spines.yml"
--8<--
examples/single-dc-l3ls/group_vars/DC1_SPINES/spines.yml
--8<--
```

The `ansible-avd-examples/single-dc-l3ls/group_vars/DC1_L3_LEAVES/l3_leaves.yml` covers the L3 leaf switches. Significantly more settings need to be set compared to the spine switches.

```yaml title="l3_leaves.yml"
--8<--
examples/single-dc-l3ls/group_vars/DC1_L3_LEAVES/l3_leaves.yml
--8<--
```

Finally, more of the same, but this time for the L2 leaf switches:

```yaml title="l2_leaves.yml"
--8<--
examples/single-dc-l3ls/group_vars/DC1_L2_LEAVES/l2_leaves.yml
--8<--
```

An L2 leaf switch is simpler than an L3 switch. Hence there are fewer settings to define.

## Specifying network services (VRFs and VLANs) in the EVPN/VXLAN fabric

The `ansible-avd-examples/single-dc-l3ls/group_vars/NETWORK_SERVICES/network_services.yml` file defines All VRF and VLANs. This means that regardless of where a given VRF or VLAN must exist, its existence is defined in this file, but it does not indicate ***where*** in the fabric it exists. That was done at the bottom of the inventory file previously described in the [Inventory](#content-of-the-inventoryyml-file) section.

```yaml title="network_services.yml"
--8<--
examples/single-dc-l3ls/group_vars/NETWORK_SERVICES/network_services.yml
--8<--
```

AVD offers granular control of where Tenants and VLANs are configured using `tags` and `filter`. Those areas are not covered in this basic example.

## Specifying endpoint connectivity in the EVPN/VXLAN fabric

After the previous section, all VRFs and VLANs across the fabric are now defined. The `ansible-avd-examples/single-dc-l3ls/group_vars/CONNECTED_ENDPOINTS/connected_endpoints.yml` file specifies the connectivity for all endpoints in the fabric (typically servers):

```yaml title="connected_endpoints.yml"
--8<--
ansible_collections/arista/avd/examples/single-dc-l3ls/group_vars/CONNECTED_ENDPOINTS.yml
--8<--
```

This defines the settings for the relevant switch ports to which the endpoints connect, in this case the two servers `dc1-leaf1-server1` and `dc1-leaf2-server1`.

## The playbooks

In this example, three playbooks are included, of which two must be used:

1. The first playbook `build.yml` is mandatory and is used to build the structured configuration, documentation and finally the actual EOS CLI configuration.
2. The second playbook is a choice between:
   1. `deploy.yml` to deploy the configurations generated by `build.yml` directly to the Arista switches using eAPI.
   2. `deploy-cvp.yml` to deploy the configurations generated by `build.yml` to the Arista switches using CloudVision.

The `build.yml` playbook looks like the following:

```yaml title="build.yml"
--8<--
ansible_collections/arista/avd/examples/single-dc-l3ls/build.yml
--8<--
```

1. At the highest level, the name and scope of the playbook are set, which in this example is the entire fabric. For instance, `FABRIC` is a group name defined in the inventory. If the playbook should only apply to a subset of devices, it can be changed here.
2. This task uses the role `arista.avd.eos_designs`, which generates structured configuration for each device. This structured configuration can be found in the `ansible-avd-examples/single-dc-l3ls/intended/structured_configs` folder.
3. This task uses the role `arista.avd.eos_cli_config_gen`, which generates the Arista EOS CLI configurations found in the `ansible-avd-examples/single-dc-l3ls/intended/configs` folder, along with the device-specific and fabric wide documentation found in the `ansible-avd-examples/single-dc-l3ls/documentation/` folder. In addition, it relies on the structured configuration generated by `arista.avd.eos_designs`.

The `deploy.yml` playbook looks like the following:

```yaml title="deploy.yml"
--8<--
ansible_collections/arista/avd/examples/single-dc-l3ls/deploy.yml
--8<--
```

1. At the highest level, the name and scope of the playbook are set, which in this example is the entire fabric. For instance, `FABRIC` is a group name defined in the inventory. If the playbook should only apply to a subset of devices, it can be changed here.
2. This task uses the `arista.avd.eos_config_deploy_eapi` role to deploy the configurations directly to EOS nodes that were generated by the `arista.avd.eos_cli_config_gen` role.

The `deploy-cvp.yml` playbook looks like the following:

```yaml title="deploy-cvp.yml"
--8<--
ansible_collections/arista/avd/examples/single-dc-l3ls/deploy-cvp.yml
--8<--
```

1. At the highest level, the name and scope of the playbook are set, which in this example is the CloudVision server named `CLOUDVISION`.
2. This task uses the `arista.avd.eos_config_deploy_cvp` role to deploy and manage the Fabric with CloudVision.
3. Sets `v3` as the version of the collection to use (default in AVD 4.x).
4. `fabric_name` is used to specify the container root in CVP (must match a group name).

In addition, the `arista.avd.eos_config_deploy_cvp` collection performs the following actions:

- Reads the AVD inventory and builds the container topology in CloudVision
- Looks for configuration previously generated by arista.avd.eos_cli_config_gen and builds configlets list, one per device
- Looks for additional configlets to attach to either devices or containers
- Build configlets on CVP
- Create containers topology
- Move devices to the container
- Bind configlet to device
- Deploy Fabric configuration by running all pending tasks (optional, if execute_tasks == true)

### Testing AVD output without a lab

Using the `build.yml` playbook without any actual devices is possible. The playbook will generate all the output (variables, configurations, documentation) but will not attempt to communicate with devices.

Please look through the folders and files described above to learn more about the output generated by AVD.

### Playbook Run

To build the configuration files, run the playbook called `build.yml`.

``` bash
### Build Configurations and Documentation
ansible-playbook playbooks/build.yml
```

After the playbook run finishes, EOS CLI intended configuration files were written to `intended/configs`.

To build and deploy the configurations to your switches directly, using eAPI, run the playbook called `deploy.yml`. This assumes that your Ansible host has access and authentication rights to the switches. Those auth variables are defined in FABRIC.yml.

``` bash
### Deploy Configurations to Devices using eAPI
ansible-playbook playbooks/deploy.yml
```

To build and deploy the configurations to your switches using CloudVision Portal, run the playbook called `deploy-cvp.yml`. This assumes that your CloudVision Portal server has access and authentication rights to the switches. Those auth variables are defined in FABRIC.yml.

``` bash
### Deploy Configurations to Devices Using CloudVision Portal
ansible-playbook playbooks/deploy-cvp.yml
```

### EOS Intended Configurations

Your configuration files should be similar to these.

=== "dc1-spine1"

    ``` shell
    --8<--
    ansible_collections/arista/avd/examples/single-dc-l3ls/intended/configs/dc1-spine1.cfg
    --8<--
    ```

=== "dc1-spine2"

    ``` shell
    --8<--
    ansible_collections/arista/avd/examples/single-dc-l3ls/intended/configs/dc1-spine2.cfg
    --8<--
    ```

=== "dc1-leaf1a"

    ``` shell
    --8<--
    ansible_collections/arista/avd/examples/single-dc-l3ls/intended/configs/dc1-leaf1a.cfg
    --8<--
    ```

=== "dc1-leaf1b"

    ``` shell
    --8<--
    ansible_collections/arista/avd/examples/single-dc-l3ls/intended/configs/dc1-leaf1b.cfg
    --8<--
    ```

=== "dc1-leaf1c"

    ``` shell
    --8<--
    ansible_collections/arista/avd/examples/single-dc-l3ls/intended/configs/dc1-leaf1c.cfg
    --8<--
    ```

=== "dc1-leaf2a"

    ``` shell
    --8<--
    ansible_collections/arista/avd/examples/single-dc-l3ls/intended/configs/dc1-leaf2a.cfg
    --8<--
    ```

=== "dc1-leaf2b"

    ``` shell
    --8<--
    ansible_collections/arista/avd/examples/single-dc-l3ls/intended/configs/dc1-leaf2b.cfg
    --8<--
    ```

=== "dc1-leaf2c"

    ``` shell
    --8<--
    ansible_collections/arista/avd/examples/single-dc-l3ls/intended/configs/dc1-leaf2c.cfg
    --8<--
    ```

The execution of the playbook should produce the following output:

```shell
user@ubuntu:~/ansible-avd-examples/single-dc-l3ls$ ansible-playbook build.yml

PLAY [Run AVD] *****************************************************************************************************************************************************************************

TASK [arista.avd.eos_designs : Collection arista.avd version 4.0.0 loaded from /home/user/.ansible/collections/ansible_collections] ******************************************************
ok: [dc1-leaf1a]

TASK [arista.avd.eos_designs : Create required output directories if not present] **********************************************************************************************************
ok: [dc1-leaf1a -> localhost] => (item=/home/user/Documents/git_projects/ansible-avd-examples/single-dc-l3ls/intended/structured_configs)
ok: [dc1-leaf1a -> localhost] => (item=/home/user/Documents/git_projects/ansible-avd-examples/single-dc-l3ls/documentation/fabric)
(...)
```

If similar output is not shown, make sure:

1. The documented [requirements](../../../../../docs/installation/collection-installation.md) are met.
2. The latest `arista.avd` collection is installed.

## Troubleshooting

### EVPN not working

If after doing the following steps:

1. Manually copy/paste the switch-basic-configuration to the devices.
2. Run the playbook and push the generated configuration to the fabric.
3. Log in to a leaf device, for example, dc1-leaf1a and run the command `show bgp evpn summary` to view EVPN routes.

The following error message is shown:

```eos
dc1-leaf1a#show bgp evpn summ
% Not supported
dc1-leaf1a#
```

This is caused by AVD pushing the configuration line `service routing protocols model multi-agent`, which enables the multi-agent routing process supporting EVPN. This change *requires* a reboot of the device.
