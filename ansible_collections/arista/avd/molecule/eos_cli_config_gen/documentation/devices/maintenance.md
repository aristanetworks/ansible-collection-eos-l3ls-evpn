# maintenance

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Maintenance Mode](#maintenance-mode)
  - [Maintenance](#maintenance-1)

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

## Maintenance Mode

### Maintenance

#### Maintenance defaults

Default maintenance bgp profile: **BP1**

Default maintenance interface profile: **IP1**

Default maintenance unit profile: **UP1**

#### Maintenance profiles

| BGP profile | Initiator route-map |
| ----------- | ------------------- |
| BP1 | RM-MAINTENANCE |
| BP2 | RM-MAINTENANCE2 |
| BP3 | RM-MAINTENANCE3 |

| Interface profile | Rate monitoring load interval (s) | Rate monitoring threshold in/out (kbps) | Shutdown Max Delay |
|-------------------|-----------------------------------|-----------------------------------------|--------------------|
| IP1 | 10 | 500 | 300 |

| Unit profile | on-boot duration (s) |
| ------------ | -------------------- |
| UP1 | 900 |
| UP2 | 600 |

#### Maintenance units

| Unit | Interface groups | BGP groups | Unit profile | Quiesce |
| ---- | ---------------- | ---------- | ------------ | ------- |
| System | - | - | UP1 | No |
| UNIT1 | INTERFACE_GROUP_1 | BGP_GROUP_1<br/>BGP_GROUP_2 | UP1 | No |

#### Maintenance Device Configuration

```eos
!
maintenance
   profile bgp BP1
      initiator route-map RM-MAINTENANCE inout
   !
   profile bgp BP2
      initiator route-map RM-MAINTENANCE2 inout
   !
   profile bgp BP3
      initiator route-map RM-MAINTENANCE3 inout
   profile bgp BP1 default
   profile interface IP1 default
   profile unit UP1 default
   !
   profile interface IP1
      rate-monitoring load-interval 10
      rate-monitoring threshold 500
      shutdown max-delay 300
   !
   profile unit UP1
      on-boot duration 900
   !
   profile unit UP2
      on-boot duration 600
   !
   unit System
   !
   unit UNIT1
      group bgp BGP_GROUP_1
      group bgp BGP_GROUP_2
      group interface INTERFACE_GROUP_1
      profile unit UP1
```
