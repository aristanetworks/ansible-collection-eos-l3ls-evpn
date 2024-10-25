# monitor-layer1

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitor Layer 1 Logging](#monitor-layer-1-logging)
  - [Monitor Layer 1 Device Configuration](#monitor-layer-1-device-configuration)

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

## Monitor Layer 1 Logging

| Layer 1 Event | Logging |
| ------------- | ------- |
| MAC fault | True |
| Logging Transceiver | True |
| Transceiver DOM | True |
| Transceiver communication | True |

### Monitor Layer 1 Device Configuration

```eos
!
monitor layer1
   logging transceiver
   logging transceiver dom
   logging transceiver communication
   logging mac fault
```
