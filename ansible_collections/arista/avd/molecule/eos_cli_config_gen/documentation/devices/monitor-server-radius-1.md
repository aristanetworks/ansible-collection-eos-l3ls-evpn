# monitor-server-radius-1

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitor Server Radius Summary](#monitor-server-radius-summary)
  - [Server Probe Settings](#server-probe-settings)
  - [Monitor Server Radius Device Configuration](#monitor-server-radius-device-configuration)

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

## Monitor Server Radius Summary

Monitor servers are used for 802.1x authentication.

### Server Probe Settings

| Setting | Value |
| ------- | ----- |
| Probe interval | 100 |
| Threshold failure | 100 |
| Probe method | access-request |

### Monitor Server Radius Device Configuration

```eos
!
monitor server radius
   service dot1x
   probe interval 100 seconds
   probe threshold failure 100
   probe method access-request username arista password 7 141600021F102B
```
