# queue-monitor-length

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Queue Monitor](#queue-monitor)
  - [Queue Monitor Length](#queue-monitor-length-1)
  - [Queue Monitor Configuration](#queue-monitor-configuration)

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

## Queue Monitor

### Queue Monitor Length

| Enabled | Logging Interval | Default Thresholds High | Default Thresholds Low | Notifying | TX Latency | CPU Thresholds High | CPU Thresholds Low |
| ------- | ---------------- | ----------------------- | ---------------------- | --------- | ---------- | ------------------- | ------------------ |
| True | 100 | 100 | 10 | enabled | enabled | 200000 | 100000 |

### Queue Monitor Configuration

```eos
!
queue-monitor length
queue-monitor length notifying
queue-monitor length tx-latency
queue-monitor length default thresholds 100 10
queue-monitor length cpu thresholds 200000 100000
!
queue-monitor length log 100
```
