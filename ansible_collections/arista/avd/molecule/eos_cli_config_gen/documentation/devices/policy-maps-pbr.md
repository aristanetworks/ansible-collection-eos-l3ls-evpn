# policy-maps-pbr

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Routing](#routing)
  - [PBR Policy Maps](#pbr-policy-maps)

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

## Routing

### PBR Policy Maps

#### PBR Policy Maps Summary

##### POLICY_DROP_THEN_NEXTHOP

| Class | Index | Drop | Nexthop | Recursive |
| ----- | ----- | ---- | ------- | --------- |
| CLASS_DROP | 10 | True | - | - |
| CLASS_NEXTHOP | 20 | - | 172.30.1.2 | True |
| NO_ACTION | - | - | - | - |

#### PBR Policy Maps Device Configuration

```eos
!
policy-map type pbr POLICY_DROP_THEN_NEXTHOP
   10 class CLASS_DROP
      drop
   !
   20 class CLASS_NEXTHOP
      set nexthop recursive 172.30.1.2
   !
   class NO_ACTION
```
