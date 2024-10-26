# ntp

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [NTP](#ntp-1)

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

### NTP

#### NTP Summary

##### NTP Local Interface

| Interface | VRF |
| --------- | --- |
| lo1 | default |

##### NTP Servers

| Server | VRF | Preferred | Burst | iBurst | Version | Min Poll | Max Poll | Local-interface | Key |
| ------ | --- | --------- | ----- | ------ | ------- | -------- | -------- | --------------- | --- |
| 1.2.3.4 | - | - | - | - | - | - | - | lo0 | - |
| 2.2.2.55 | - | - | - | - | - | - | - | - | - |
| 10.1.1.1 | - | - | - | - | - | - | - | - | - |
| 10.1.1.2 | - | True | - | - | - | - | - | - | - |
| 20.20.20.1 | - | - | - | - | - | - | - | - | 2 |
| ie.pool.ntp.org | - | - | False | True | - | - | - | - | 1 |

##### NTP Authentication

- Authentication enabled

- Trusted Keys: 1-3

##### NTP Authentication Keys

| ID | Algorithm |
| -- | -------- |
| 1 | md5 |
| 2 | md5 |
| 3 | sha1 |

#### NTP Device Configuration

```eos
!
ntp authentication-key 1 md5 <removed>
ntp authentication-key 2 md5 7 <removed>
ntp authentication-key 3 sha1 8a <removed>
ntp trusted-key 1-3
ntp authenticate
ntp local-interface lo1
ntp server 1.2.3.4 local-interface lo0
ntp server 2.2.2.55
ntp server 10.1.1.1
ntp server 10.1.1.2 prefer
ntp server 20.20.20.1 key <removed>
ntp server ie.pool.ntp.org iburst key <removed>
```
