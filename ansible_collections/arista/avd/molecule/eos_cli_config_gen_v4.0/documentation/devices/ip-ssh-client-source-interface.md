# ip-ssh-client-source-interface

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [IP SSH Client Source Interfaces](#ip-ssh-client-source-interfaces)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

##### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | oob_management | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   vrf MGMT
   ip address 10.73.255.122/24
```

### IP SSH Client Source Interfaces

#### IP SSH Client Source Interfaces

| VRF | Source Interface Name |
| --- | --------------- |
| default | Ethernet10 |
| default | Loopback0 |
| MGMT | Management0 |

#### IP SSH Client Source Interfaces Device Configuration

```eos
!
ip ssh client source-interface Ethernet10
ip ssh client source-interface Loopback0 vrf default
ip ssh client source-interface Management0 vrf MGMT
```
