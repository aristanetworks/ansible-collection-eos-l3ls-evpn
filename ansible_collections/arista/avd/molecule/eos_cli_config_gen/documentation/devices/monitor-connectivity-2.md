# monitor-connectivity-2

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitor Connectivity](#monitor-connectivity)
  - [Global Configuration](#global-configuration)
  - [Monitor Connectivity Device Configuration](#monitor-connectivity-device-configuration)

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

## Monitor Connectivity

### Global Configuration

#### Interface Sets

| Name | Interfaces |
| ---- | ---------- |
| HOST_SET2 | Loopback2-4, Loopback10-12 |

#### Probing Configuration

| Enabled | Interval | Default Interface Set | Address Only |
| ------- | -------- | --------------------- | ------------ |
| False | 5 | HOST_SET2 | False |

### Monitor Connectivity Device Configuration

```eos
!
monitor connectivity
   interval 5
   shutdown
   interface set HOST_SET2 Loopback2-4, Loopback10-12
   local-interfaces HOST_SET2 default
```
