# host6

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
<<<<<<< HEAD:ansible_collections/arista/avd/molecule/eos_cli_config_gen/documentation/devices/host6.md
- [Monitoring](#monitoring)
  - [SNMP](#snmp)
=======
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [TACACS Servers](#tacacs-servers)

>>>>>>> 762c5af13 (adding support for salt arg):ansible_collections/arista/avd/molecule/eos_cli_config_gen/documentation/devices/host4_inline_jinja.md

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | OOB_MANAGEMENT | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description OOB_MANAGEMENT
   vrf MGMT
   ip address 10.73.255.122/24
```

## Monitoring

<<<<<<< HEAD:ansible_collections/arista/avd/molecule/eos_cli_config_gen/documentation/devices/host6.md

### SNMP

=======

### Local Users

#### Local Users Summary

| User | Privilege | Role | Disabled | Shell |
| ---- | --------- | ---- | -------- | ----- |
| sha-user | 15 | network-admin | False | - |
| sha-user-the-second | 15 | network-admin | False | - |

#### Local Users Device Configuration

```eos
!
username sha-user privilege 15 role network-admin secret sha512 <removed>
username sha-user-the-second privilege 15 role network-admin secret sha512 <removed>
```

### TACACS Servers
>>>>>>>
>>>>>>> 762c5af13 (adding support for salt arg):ansible_collections/arista/avd/molecule/eos_cli_config_gen/documentation/devices/host4_inline_jinja.md

#### SNMP Configuration Summary

| Contact | Location | SNMP Traps | State |
| ------- | -------- | ---------- | ----- |
| - | - | All | Disabled |

#### SNMP Hosts Configuration

| Host | VRF | Community | Username | Authentication level | SNMP Version |
| ---- |---- | --------- | -------- | -------------------- | ------------ |
| 10.6.75.121 | MGMT | SNMP-COMMUNITY-1 | - | - | 1 |
| 10.6.75.121 | MGMT | SNMP-COMMUNITY-2 | - | - | 2c |

#### SNMP Device Configuration

```eos
!
snmp-server host 10.6.75.121 vrf MGMT version 1 SNMP-COMMUNITY-1
snmp-server host 10.6.75.121 vrf MGMT version 2c SNMP-COMMUNITY-2
```
