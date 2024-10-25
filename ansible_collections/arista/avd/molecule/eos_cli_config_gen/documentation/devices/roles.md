# roles

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Authentication](#authentication)
  - [Roles](#roles-1)

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

## Authentication

### Roles

#### Roles Summary

##### Role network-limited

| Sequence | Action | Mode | Command |
| -------- | ------ | ---- | ------- |
| 10 | permit | exec | ssh |
| 20 | deny | - | telnet |
| 30 | permit | exec | traceroute |

#### Roles Device Configuration

```eos
!
role network-limited
   10 permit mode exec command ssh
   20 deny command telnet
   30 permit mode exec command traceroute
```
