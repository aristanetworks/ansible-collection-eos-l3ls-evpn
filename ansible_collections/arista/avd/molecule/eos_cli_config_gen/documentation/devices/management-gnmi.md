# management-gnmi

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Management API gNMI](#management-api-gnmi)

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

### Management API gNMI

#### Management API gNMI Summary

| Transport | SSL Profile | VRF | Notification Timestamp | ACL | Port |
| --------- | ----------- | --- | ---------------------- | --- | ---- |
| MGMT | - | MGMT | last-change-time | ACL-GNMI | 6030 |
| MONITORING | - | MONITORING | last-change-time | - | 6031 |

Provider eos-native is configured.

#### Management API gNMI Device Configuration

```eos
!
management api gnmi
   transport grpc MGMT
      vrf MGMT
      ip access-group ACL-GNMI
   !
   transport grpc MONITORING
      port 6031
      vrf MONITORING
   provider eos-native
```
