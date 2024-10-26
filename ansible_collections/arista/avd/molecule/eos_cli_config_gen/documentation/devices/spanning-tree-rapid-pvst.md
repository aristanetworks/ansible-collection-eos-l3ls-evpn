# spanning-tree-rapid-pvst

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)

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

## Spanning Tree

### Spanning Tree Summary

STP mode: **rapid-pvst**

#### Rapid-PVST Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 1,2,3,4,5,10-15 | 4096 |
| 3 | 8192 |
| 100-500 | 16384 |

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode rapid-pvst
spanning-tree vlan-id 1,2,3,4,5,10-15 priority 4096
spanning-tree vlan-id 3 priority 8192
spanning-tree vlan-id 100-500 priority 16384
```
