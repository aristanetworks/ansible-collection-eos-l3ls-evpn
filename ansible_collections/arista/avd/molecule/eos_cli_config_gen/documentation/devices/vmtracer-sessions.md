# vmtracer-sessions

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitoring](#monitoring)
  - [VM Tracer Sessions](#vm-tracer-sessions)

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

### VM Tracer Sessions

#### VM Tracer Summary

| Session | URL | Username | Autovlan | VRF | Source Interface |
| ------- | --- | -------- | -------- | --- | ---------------- |
| session_1 | https://192.168.0.10 | user1 | disabled | MGMT | Management1 |
| session_2 | https://192.168.0.10 | user1 | enabled | - | - |

#### VM Tracer Device Configuration

```eos
!
vmtracer session session_1
   url https://192.168.0.10
   username user1
   password 7 encrypted_password
   autovlan disable
   vrf MGMT
   source-interface Management1
!
vmtracer session session_2
   url https://192.168.0.10
   username user1
   password 7 encrypted_password
```
