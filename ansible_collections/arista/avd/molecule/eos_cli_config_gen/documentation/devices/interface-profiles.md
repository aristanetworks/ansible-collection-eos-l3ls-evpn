# interface-profiles

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Interfaces](#interfaces)
  - [Interface Profiles](#interface-profiles-1)

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

## Interfaces

### Interface Profiles

#### Interface Profiles Summary

- TEST-PROFILE-1
- TEST-PROFILE-2

#### Interface Profiles Device Configuration

```eos
!
interface profile TEST-PROFILE-1
   command description Molecule
   command no switchport
   command no lldp transmit
!
interface profile TEST-PROFILE-2
   command mtu 9214
   command ptp enable
```
