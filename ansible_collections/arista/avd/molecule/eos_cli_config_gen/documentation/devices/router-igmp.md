# router-igmp

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Multicast](#multicast)
  - [Router IGMP](#router-igmp-1)

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

## Multicast

### Router IGMP

#### Router IGMP Summary

| VRF | SSM Aware | Host Proxy |
| --- | --------- | ---------- |
| - | Enabled | - |
| default | - | all |
| BLUE | - | iif |

#### Router IGMP Device Configuration

```eos
!
router igmp
   host-proxy match mroute all
   ssm aware
   !
   vrf BLUE
     host-proxy match mroute iif
```
