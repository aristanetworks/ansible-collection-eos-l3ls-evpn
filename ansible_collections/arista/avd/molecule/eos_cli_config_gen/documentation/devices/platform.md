# platform

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Platform](#platform-1)
  - [Platform Summary](#platform-summary)
  - [Platform Device Configuration](#platform-device-configuration)

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

## Platform

### Platform Summary

#### Platform Trident Summary

| Settings | Value |
| -------- | ----- |
| Routing MAC Address per VLAN | true |
| Forwarding Table Partition | 2 |
| MMU Applied Profile | mc_example_profile |

#### Trident MMU QUEUE PROFILES

##### mc_example_profile

| Type | Egress Queue | Threshold | Reserved | Drop-Precedence |
| ---- | ------------ | --------- | -------- | --------------- |
| Unicast | 1 | - | 0 bytes | - |
| Unicast | 2 | 1/8 | 0 cells | - |
| Multicast | 0 | - | 0 bytes | - |
| Multicast | 1 | 1/64 | 0 cells | - |
| Multicast | 7 | 1/64 | 0 cells | - |

##### unused_profile

| Type | Egress Queue | Threshold | Reserved | Drop-Precedence |
| ---- | ------------ | --------- | -------- | --------------- |
| Unicast | 1 | - | 0 bytes | - |
| Unicast | 2 | 1/8 | 0 cells | - |
| Unicast | 7 | - | - bytes | - |
| Multicast | 0 | - | 0 bytes | - |
| Multicast | 1 | 8 | 0 cells | - |

#### Platform Sand Summary

| Settings | Value |
| -------- | ----- |
| Forwarding Mode | arad |
| Hardware Only Lag | True |
| Lag Mode | 512x32 |
| Default Multicast Replication | ingress |

##### Internal Network QOS Mapping

| Traffic Class | To Network QOS |
| ------------- | -------------- |
| 0 | 0 |
| 1 | 7 |
| 2 | 15 |

#### Platform Software Forwarding Engine Summary

| Settings | Value |
| -------- | ----- |
| Maximum CPU Allocation | 42 |

### Platform Device Configuration

```eos
!
platform trident l3 routing mac-address per-vlan
platform trident forwarding-table partition 2
platform sand forwarding mode arad
platform sand lag mode 512x32
platform sand lag hardware-only
platform sand qos map traffic-class 0 to network-qos 0
platform sand qos map traffic-class 1 to network-qos 7
platform sand qos map traffic-class 2 to network-qos 15
platform sand multicast replication default ingress
platform sand mdb profile l3-xxl
platform sfe data-plane cpu allocation maximum 42
```
