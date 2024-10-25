# hardware

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitoring](#monitoring)
  - [Hardware](#hardware-1)

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

### Hardware

#### Hardware Device Configuration

```eos
!
hardware port-group 1 select Et32/1-4
hardware port-group 2 select Et32/1,Et32/3,Et34
!
hardware access-list mechanism tcam
!
hardware speed-group 1 serdes 10g
hardware speed-group 2 serdes 25g
hardware speed-group 3/1 serdes 25g
```
