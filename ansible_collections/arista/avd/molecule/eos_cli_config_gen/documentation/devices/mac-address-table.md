# mac-address-table

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [MAC Address Table](#mac-address-table-1)
  - [MAC Address Table Summary](#mac-address-table-summary)
  - [MAC Address Table Device Configuration](#mac-address-table-device-configuration)

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

## MAC Address Table

### MAC Address Table Summary

- MAC address table entry maximum age: 100 seconds

- Logging MAC address interface flapping is Enabled

- 2 MAC moves are considered as one flap

- Size of the flap detection time window: 10 seconds

### MAC Address Table Device Configuration

```eos
!
mac address-table aging-time 100
!
mac address-table notification host-flap logging
mac address-table notification host-flap detection window 10
mac address-table notification host-flap detection moves 2
```
