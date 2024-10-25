# logging-minimal

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitoring](#monitoring)
  - [Logging](#logging)

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

### Logging

#### Logging Servers and Features Summary

| Type | Level |
| -----| ----- |
| Console | informational |
| Monitor | debugging |
| Buffer | - |

**Syslog facility value:** syslog

#### Logging Servers and Features Device Configuration

```eos
!
no logging repeat-messages
logging buffered 64000
logging console informational
logging monitor debugging
logging facility syslog
!
logging event link-status global
```
