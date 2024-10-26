# spanning-tree-bpdu

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

STP mode: **mstp**

#### Global Spanning-Tree Settings

- Global BPDU Guard for Edge ports is disabled.
- Global BPDU Filter for Edge ports is disabled.

### Spanning Tree Device Configuration

```eos
!
no spanning-tree edge-port bpduguard default
no spanning-tree edge-port bpdufilter default
spanning-tree bpduguard rate-limit default
spanning-tree bpduguard rate-limit count 100
```
