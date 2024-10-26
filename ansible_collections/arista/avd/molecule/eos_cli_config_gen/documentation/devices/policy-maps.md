# policy-maps

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Routing](#routing)
  - [PBR Policy Maps](#pbr-policy-maps)
- [Quality Of Service](#quality-of-service)
  - [QOS Policy Maps](#qos-policy-maps)
  - [Control-plane Policy Map](#control-plane-policy-map)

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

## Routing

### PBR Policy Maps

#### PBR Policy Maps Summary

##### PM_PBR_BREAKOUT

| Class | Index | Drop | Nexthop | Recursive |
| ----- | ----- | ---- | ------- | --------- |
| CM_PBR_EXCLUDE | - | - | - | - |
| CM_PBR_INCLUDE | - | - | 192.168.4.2 | True |

#### PBR Policy Maps Device Configuration

```eos
!
policy-map type pbr PM_PBR_BREAKOUT
   class CM_PBR_EXCLUDE
   !
   class CM_PBR_INCLUDE
      set nexthop recursive 192.168.4.2
```

## Quality Of Service

### QOS Policy Maps

#### QOS Policy Maps Summary

##### PM_REPLICATION_LD

| Class Name | COS | DSCP | Traffic Class | Drop Precedence | Police Rate (Burst) -> Action |
| ---------- | --- | -----| ------------- | --------------- | ----------------------------- |
| CM_REPLICATION_LD | - | af11 | 2 | 1 | 10 kbps (260 kbytes) -> drop-precedence<br> 30 kbps(270 kbytes) -> drop |
| CM_REPLICATION_LD_2 | - | af11 | 2 | - | - |

##### PM_REPLICATION_LD2

| Class Name | COS | DSCP | Traffic Class | Drop Precedence | Police Rate (Burst) -> Action |
| ---------- | --- | -----| ------------- | --------------- | ----------------------------- |
| CM_REPLICATION_LD | 4 | af11 | - | - | 30 kbps (280 bytes) -> dscp<br> 1 mbps(270 bytes) -> drop |

##### PM_REPLICATION_LD3

| Class Name | COS | DSCP | Traffic Class | Drop Precedence | Police Rate (Burst) -> Action |
| ---------- | --- | -----| ------------- | --------------- | ----------------------------- |
| CM_REPLICATION_LD | 6 | af11 | - | - | 10000 bps (260 kbytes) -> drop |

#### QOS Policy Maps Device Configuration

```eos
!
policy-map type quality-of-service PM_REPLICATION_LD
   class CM_REPLICATION_LD
      set dscp af11
      set traffic-class 2
      set drop-precedence 1
      police rate 10 kbps burst-size 260 kbytes action set drop-precedence rate 30 kbps burst-size 270 kbytes
   !
   class CM_REPLICATION_LD_2
      set dscp af11
      set traffic-class 2
!
policy-map type quality-of-service PM_REPLICATION_LD2
   class CM_REPLICATION_LD
      set dscp af11
      set cos 4
      police rate 30 kbps burst-size 280 bytes action set dscp af11 rate 1 mbps burst-size 270 bytes
!
policy-map type quality-of-service PM_REPLICATION_LD3
   class CM_REPLICATION_LD
      set dscp af11
      set cos 6
      police rate 10000 bps burst-size 260 kbytes
```

### Control-plane Policy Map

#### Control-plane Policy Map Summary

##### copp-system-policy

| Class | Shape | Bandwidth | Rate Unit |
| ----- | ----- | --------- | --------- |
| copp-system-aaa | - | - | - |
| copp-system-cvx | 2000 | 2000 | pps |
| copp-system-OspfIsis | 1000 | 1000 | kbps |

#### COPP Policy Maps Device Configuration

```eos
!
policy-map type copp copp-system-policy
   class copp-system-OspfIsis
      shape kbps 1000
      bandwidth kbps 1000
   !
   class copp-system-cvx
      shape pps 2000
      bandwidth pps 2000
   !
   class copp-system-aaa
```
