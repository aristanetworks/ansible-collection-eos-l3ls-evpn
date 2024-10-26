# qos

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
- [ACL](#acl)
  - [Extended Access-lists](#extended-access-lists)
  - [IPv6 Extended Access-lists](#ipv6-extended-access-lists)
- [Quality Of Service](#quality-of-service)
  - [QOS](#qos-1)
  - [QOS Class Maps](#qos-class-maps)
  - [QOS Policy Maps](#qos-policy-maps)
  - [QOS Profiles](#qos-profiles)
  - [QOS Interfaces](#qos-interfaces)
  - [Priority Flow Control](#priority-flow-control-1)

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

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet3 | MLAG_PEER_DC1-LEAF1B_Ethernet3 | *trunk | *2-4094 | *- | *LEAF_PEER_L3, MLAG | 3 |
| Ethernet4 | MLAG_PEER_DC1-LEAF1B_Ethernet4 | *trunk | *2-4094 | *- | *LEAF_PEER_L3, MLAG | 3 |
| Ethernet6 | SRV-POD02_Eth1 | trunk | 110-111,210-211 | - | - | - |
| Ethernet7 | Test-with-policymap | trunk | 110-111,210-211 | - | - | - |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_LINK_TO_DC1-SPINE1_Ethernet1 | - | 172.31.255.1/31 | default | 1500 | - | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_DC1-SPINE1_Ethernet1
   mtu 1500
   no switchport
   ip address 172.31.255.1/31
   service-policy type qos input pmap_test1
   service-profile test
   qos trust dscp
   qos dscp 48
!
interface Ethernet3
   description MLAG_PEER_DC1-LEAF1B_Ethernet3
   channel-group 3 mode active
!
interface Ethernet4
   description MLAG_PEER_DC1-LEAF1B_Ethernet4
   channel-group 3 mode active
!
interface Ethernet6
   description SRV-POD02_Eth1
   switchport trunk allowed vlan 110-111,210-211
   switchport mode trunk
   switchport
   service-profile experiment
   qos trust cos
   qos cos 2
   !
   tx-queue 2
      random-detect ecn count
!
interface Ethernet7
   description Test-with-policymap
   switchport trunk allowed vlan 110-111,210-211
   switchport mode trunk
   switchport
   service-profile qprof_testwithpolicy
   !
   uc-tx-queue 4
      random-detect ecn count
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel3 | MLAG_PEER_DC1-LEAF1B_Po3 | trunk | 2-4094 | - | LEAF_PEER_L3, MLAG | - | - | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel3
   description MLAG_PEER_DC1-LEAF1B_Po3
   switchport trunk allowed vlan 2-4094
   switchport mode trunk
   switchport trunk group LEAF_PEER_L3
   switchport trunk group MLAG
   switchport
   service-policy type qos input pmap_test1
   service-profile experiment
   qos trust cos
   qos cos 2
```

## ACL

### Extended Access-lists

#### Extended Access-lists Summary

##### acl_qos_tc0_v4

| Sequence | Action |
| -------- | ------ |
| 10 | permit ip any 192.0.2.0/29 |

##### acl_qos_tc5_v4

| Sequence | Action |
| -------- | ------ |
| 10 | permit ip any any dscp ef |

#### Extended Access-lists Device Configuration

```eos
!
ip access-list acl_qos_tc0_v4
   10 permit ip any 192.0.2.0/29
!
ip access-list acl_qos_tc5_v4
   10 permit ip any any dscp ef
```

### IPv6 Extended Access-lists

#### IPv6 Extended Access-lists Summary

##### acl_qos_tc0_v6

| Sequence | Action |
| -------- | ------ |
| 10 | permit ipv6 any any dscp cs1 |

##### acl_qos_tc5_v6

| Sequence | Action |
| -------- | ------ |
| 10 | permit ipv6 any 2001:db8::/48 |

#### IPv6 Extended Access-lists Device Configuration

```eos
!
ipv6 access-list acl_qos_tc0_v6
   10 permit ipv6 any any dscp cs1
!
ipv6 access-list acl_qos_tc5_v6
   10 permit ipv6 any 2001:db8::/48
```

## Quality Of Service

### QOS

#### QOS Summary

QOS rewrite DSCP: **enabled**

QOS random-detect ECN is set to allow **non-ect** **chip-based**

##### QOS Mappings

| COS to Traffic Class mappings |
| ----------------------------- |
| 1 2 3 4 to traffic-class 2 |
| 3 to traffic-class 3 |

| DSCP to Traffic Class mappings |
| ------------------------------ |
| 8 9 10 11 12 13 14 15 16 17 19 21 23 24 25 27 29 31 32 33 35 37 39 40 41 42 43 44 45 47 49 50 51 52 53 54 55 57 58 59 60 61 62 63 to traffic-class 1 |
| 18 20 22 26 28 30 34 36 38 to traffic-class 4 drop-precedence 2 |
| 46 to traffic-class 5 |

| EXP to Traffic Class mappings |
| ----------------------------- |
| 0 to traffic-class 0 |

| Traffic Class to DSCP or COS mappings |
| ------------------------------------- |
| 1 to dscp 56 |
| 2 4 5 to cos 7 |
| 6 to tx-queue 2 |

#### QOS Device Configuration

```eos
!
qos rewrite dscp
qos map cos 1 2 3 4 to traffic-class 2
qos map cos 3 to traffic-class 3
qos map dscp 8 9 10 11 12 13 14 15 16 17 19 21 23 24 25 27 29 31 32 33 35 37 39 40 41 42 43 44 45 47 49 50 51 52 53 54 55 57 58 59 60 61 62 63 to traffic-class 1
qos map dscp 18 20 22 26 28 30 34 36 38 to traffic-class 4 drop-precedence 2
qos map dscp 46 to traffic-class 5
qos map traffic-class 1 to dscp 56
qos map traffic-class 2 4 5 to cos 7
qos map traffic-class 6 to tx-queue 2
qos map exp 0 to traffic-class 0
!
qos random-detect ecn allow non-ect chip-based
```

### QOS Class Maps

#### QOS Class Maps Summary

| Name | Field | Value |
| ---- | ----- | ----- |
| cmap_tc0_v4 | acl | acl_qos_tc0_v4 |
| cmap_tc0_v6 | - | - |
| cmap_tc5_v4 | acl | acl_qos_tc5_v4 |
| cmap_tc5_v6 | - | - |

#### Class-maps Device Configuration

```eos
!
class-map type qos match-any cmap_tc0_v4
   match ip access-group acl_qos_tc0_v4
!
class-map type qos match-any cmap_tc0_v6
   match ipv6 access-group acl_qos_tc0_v6
!
class-map type qos match-any cmap_tc5_v4
   match ip access-group acl_qos_tc5_v4
!
class-map type qos match-any cmap_tc5_v6
   match ipv6 access-group acl_qos_tc5_v6
```

### QOS Policy Maps

#### QOS Policy Maps Summary

##### pmap_test1

| Class Name | COS | DSCP | Traffic Class | Drop Precedence | Police Rate (Burst) -> Action |
| ---------- | --- | -----| ------------- | --------------- | ----------------------------- |
| cmap_tc0_v4 | - | - | 0 | - | - |
| cmap_tc5_v4 | - | - | 5 | - | - |
| cmap_tc5_v6 | - | - | 5 | - | - |
| cmap_tc0_v6 | - | - | 0 | - | - |
| class-default | - | - | 1 | - | - |

#### QOS Policy Maps Device Configuration

```eos
!
policy-map type quality-of-service pmap_test1
   class cmap_tc0_v4
      set traffic-class 0
   !
   class cmap_tc5_v4
      set traffic-class 5
   !
   class cmap_tc5_v6
      set traffic-class 5
   !
   class cmap_tc0_v6
      set traffic-class 0
   !
   class class-default
      set traffic-class 1
```

### QOS Profiles

#### QOS Profiles Summary

##### QOS Profile: **experiment**

###### Settings

| Default COS | Default DSCP | Trust | Shape Rate | QOS Service Policy |
| ----------- | ------------ | ----- | ---------- | ------------------ |
| 2 | - | cos | - | test_qos_policy_v1 |

###### TX Queues

| TX queue | Type | Bandwidth | Priority | Shape Rate | Comment |
| -------- | ---- | --------- | -------- | ---------- | ------- |
| 3 | All | 30 | no priority | - | - |
| 4 | All | 10 | - | - | - |
| 5 | All | 40 | - | - | - |
| 7 | All | 30 | - | 40 percent | - |

##### QOS Profile: **no_qos_trust**

###### Settings

| Default COS | Default DSCP | Trust | Shape Rate | QOS Service Policy |
| ----------- | ------------ | ----- | ---------- | ------------------ |
| 3 | 4 | disabled | - | - |

##### QOS Profile: **qprof_testwithpolicy**

###### Settings

| Default COS | Default DSCP | Trust | Shape Rate | QOS Service Policy |
| ----------- | ------------ | ----- | ---------- | ------------------ |
| - | - | - | - | pmap_test1 |

###### TX Queues

| TX queue | Type | Bandwidth | Priority | Shape Rate | Comment |
| -------- | ---- | --------- | -------- | ---------- | ------- |
| 0 | All | 1 | - | - | - |
| 1 | All | 80 | - | - | - |
| 5 | All | 19 | no priority | - | Multi-line comment<br>here. |

##### QOS Profile: **test**

###### Settings

| Default COS | Default DSCP | Trust | Shape Rate | QOS Service Policy |
| ----------- | ------------ | ----- | ---------- | ------------------ |
| - | 46 | dscp | 80 percent | - |

###### TX Queues

| TX queue | Type | Bandwidth | Priority | Shape Rate | Comment |
| -------- | ---- | --------- | -------- | ---------- | ------- |
| 1 | All | 50 | no priority | - | - |
| 2 | All | 10 | priority strict | - | - |
| 4 | All | 10 | - | - | - |

###### ECN Configuration

| TX queue | Type | Min Threshold | Max Threshold | Max Mark Probability |
| -------- | ---- | ------------- | ------------- | -------------------- |
| 1 | All | -  | -  | - |
| 2 | All | 320 kbytes | 320 kbytes | 90 |
| 4 | All | 320 segments | 320 segments | - |

##### QOS Profile: **test_with_pfc**

###### Settings

| Default COS | Default DSCP | Trust | Shape Rate | QOS Service Policy |
| ----------- | ------------ | ----- | ---------- | ------------------ |
| - | - | - | - | pmap_test1 |

###### TX Queues

| TX queue | Type | Bandwidth | Priority | Shape Rate | Comment |
| -------- | ---- | --------- | -------- | ---------- | ------- |
| 0 | All | 1 | - | - | - |
| 1 | All | 80 | - | - | - |
| 5 | All | 19 | no priority | - | - |

###### Priority Flow Control

Priority Flow Control is **enabled**.

| Priority | Action |
| -------- | ------ |
| 0 | no-drop |
| 1 | drop |

###### Priority Flow Control Watchdog Settings

| Enabled | Action | Timeout | Recovery | Polling |
| ------- | ------ | ------- | -------- | ------- |
| True | drop | 0.05 | 1.11 | auto |

##### QOS Profile: **uc_mc_queues_test**

###### Settings

| Default COS | Default DSCP | Trust | Shape Rate | QOS Service Policy |
| ----------- | ------------ | ----- | ---------- | ------------------ |
| - | - | - | - | - |

###### TX Queues

| TX queue | Type | Bandwidth | Priority | Shape Rate | Comment |
| -------- | ---- | --------- | -------- | ---------- | ------- |
| 1 | Unicast | 50 | no priority | - | Test no priority |
| 2 | Unicast | 10 | priority strict | - | - |
| 4 | Unicast | 10 | - | - | Test guaranteed percent |
| 1 | Multicast | 50 | no priority | - | - |
| 2 | Multicast | 10 | priority strict | - | Test strict priority |
| 4 | Multicast | 10 | - | - | Test guaranteed percent |

###### ECN Configuration

| TX queue | Type | Min Threshold | Max Threshold | Max Mark Probability |
| -------- | ---- | ------------- | ------------- | -------------------- |
| 1 | Unicast | 3 milliseconds | 9 milliseconds | 90 |
| 2 | Unicast | 320 kbytes | 320 kbytes | 90 |
| 4 | Unicast | 320 segments | 320 segments | - |
| 1 | Multicast | - | - | - |
| 2 | Multicast | - | - | - |
| 4 | Multicast | - | - | - |

##### QOS Profile: **wred_queues_test**

###### Settings

| Default COS | Default DSCP | Trust | Shape Rate | QOS Service Policy |
| ----------- | ------------ | ----- | ---------- | ------------------ |
| - | - | - | - | - |

###### TX Queues

| TX queue | Type | Bandwidth | Priority | Shape Rate | Comment |
| -------- | ---- | --------- | -------- | ---------- | ------- |
| 1 | All | 50 | no priority | - | Test no priority |
| 2 | All | 10 | priority strict | - | - |
| 3 | All | 10 | priority strict | - | - |
| 4 | All | 10 | - | - | Test guaranteed percent |
| 1 | Multicast | 50 | no priority | - | - |
| 2 | Multicast | 10 | priority strict | - | Test strict priority |
| 4 | Multicast | 10 | - | - | Test guaranteed percent |

###### ECN Configuration

| TX queue | Type | Min Threshold | Max Threshold | Max Mark Probability |
| -------- | ---- | ------------- | ------------- | -------------------- |
| 1 | All | -  | -  | - |
| 2 | All | -  | -  | - |
| 3 | All | 320 kbytes | 320 kbytes | - |
| 4 | All | -  | -  | - |
| 1 | Multicast | - | - | - |
| 2 | Multicast | - | - | - |
| 4 | Multicast | - | - | - |

###### WRED Configuration

| TX queue | Type | Drop Precedence | Min Threshold | Max Threshold | Drop Probability | Weight |
| -------- | ---- | --------------- | ------------- | ------------- | ---------------- | ------ |
| 1 | All | - | 1 kbytes | 10 kbytes | 100 | - |
| 2 | All | 2 | 2 kbytes | 200 kbytes | 50 | 10 |
| 3 | All | - | -  | -  | - | - |
| 4 | All | - | 1 kbytes | 10 kbytes | 90 | - |
| 1 | Multicast | - | - | - | - | - |
| 2 | Multicast | - | - | - | - | - |
| 4 | Multicast | - | - | - | - | - |

##### QOS Profile: **wred_uc_queues_test**

###### Settings

| Default COS | Default DSCP | Trust | Shape Rate | QOS Service Policy |
| ----------- | ------------ | ----- | ---------- | ------------------ |
| - | - | - | - | - |

###### TX Queues

| TX queue | Type | Bandwidth | Priority | Shape Rate | Comment |
| -------- | ---- | --------- | -------- | ---------- | ------- |
| 1 | Unicast | 50 | no priority | - | Test no priority |
| 2 | Unicast | 10 | priority strict | - | - |
| 4 | Unicast | 10 | - | - | Test guaranteed percent |

###### WRED Configuration

| TX queue | Type | Drop Precedence | Min Threshold | Max Threshold | Drop Probability | Weight |
| -------- | ---- | --------------- | ------------- | ------------- | ---------------- | ------ |
| 1 | Unicast | - |1 microseconds | 10 microseconds | 90 | 15 |
| 2 | Unicast | 1 |2 milliseconds | 20 milliseconds | 80 | - |
| 4 | Unicast | - |1 microseconds | 10 microseconds | 90 | - |

#### QOS Profile Device Configuration

```eos
!
qos profile experiment
   qos trust cos
   qos cos 2
   service-policy type qos input test_qos_policy_v1
   !
   tx-queue 3
      no priority
      bandwidth percent 30
   !
   tx-queue 4
      bandwidth guaranteed percent 10
   !
   tx-queue 5
      bandwidth percent 40
   !
   tx-queue 7
      bandwidth percent 30
      shape rate 40 percent
!
qos profile no_qos_trust
   no qos trust
   qos cos 3
   qos dscp 4
!
qos profile qprof_testwithpolicy
   service-policy type qos input pmap_test1
   !
   tx-queue 0
      bandwidth percent 1
   !
   tx-queue 1
      bandwidth percent 80
   !
   tx-queue 5
      !! Multi-line comment
      !! here.
      no priority
      bandwidth percent 19
!
qos profile test
   qos trust dscp
   qos dscp 46
   shape rate 80 percent
   !
   tx-queue 1
      no priority
      bandwidth percent 50
   !
   tx-queue 2
      priority strict
      bandwidth percent 10
      random-detect ecn minimum-threshold 320 kbytes maximum-threshold 320 kbytes max-mark-probability 90
   !
   tx-queue 4
      bandwidth guaranteed percent 10
      random-detect ecn minimum-threshold 320 segments maximum-threshold 320 segments weight 10
!
qos profile test_with_pfc
   service-policy type qos input pmap_test1
   !
   tx-queue 0
      bandwidth percent 1
   !
   tx-queue 1
      bandwidth percent 80
   !
   tx-queue 5
      no priority
      bandwidth percent 19
   !
   priority-flow-control on
   priority-flow-control priority 0 no-drop
   priority-flow-control priority 1 drop
   priority-flow-control pause watchdog
   priority-flow-control pause watchdog port action drop
   priority-flow-control pause watchdog port timer timeout 0.05 polling-interval auto recovery-time 1.11 forced
!
qos profile uc_mc_queues_test
   !
   uc-tx-queue 1
      !! Test no priority
      no priority
      bandwidth percent 50
      random-detect ecn minimum-threshold 3 milliseconds maximum-threshold 9 milliseconds max-mark-probability 90
   !
   uc-tx-queue 2
      priority strict
      bandwidth percent 10
      random-detect ecn minimum-threshold 320 kbytes maximum-threshold 320 kbytes max-mark-probability 90
   !
   uc-tx-queue 4
      !! Test guaranteed percent
      bandwidth guaranteed percent 10
      random-detect ecn minimum-threshold 320 segments maximum-threshold 320 segments weight 10
   !
   mc-tx-queue 1
      no priority
      bandwidth percent 50
   !
   mc-tx-queue 2
      !! Test strict priority
      priority strict
      bandwidth percent 10
   !
   mc-tx-queue 4
      !! Test guaranteed percent
      bandwidth guaranteed percent 10
!
qos profile wred_queues_test
   !
   tx-queue 1
      !! Test no priority
      no priority
      bandwidth percent 50
      random-detect drop minimum-threshold 1 kbytes maximum-threshold 10 kbytes drop-probability 100
   !
   tx-queue 2
      priority strict
      bandwidth percent 10
      random-detect drop drop-precedence 2 minimum-threshold 2 kbytes maximum-threshold 200 kbytes drop-probability 50 weight 10
   !
   tx-queue 3
      priority strict
      bandwidth percent 10
      random-detect ecn minimum-threshold 320 kbytes maximum-threshold 320 kbytes weight 10
   !
   tx-queue 4
      !! Test guaranteed percent
      bandwidth guaranteed percent 10
      random-detect drop minimum-threshold 1 kbytes maximum-threshold 10 kbytes drop-probability 90
   !
   mc-tx-queue 1
      no priority
      bandwidth percent 50
   !
   mc-tx-queue 2
      !! Test strict priority
      priority strict
      bandwidth percent 10
   !
   mc-tx-queue 4
      !! Test guaranteed percent
      bandwidth guaranteed percent 10
!
qos profile wred_uc_queues_test
   !
   uc-tx-queue 1
      !! Test no priority
      no priority
      bandwidth percent 50
      random-detect drop minimum-threshold 1 microseconds maximum-threshold 10 microseconds drop-probability 90 weight 15
   !
   uc-tx-queue 2
      priority strict
      bandwidth percent 10
      random-detect drop drop-precedence 1 minimum-threshold 2 milliseconds maximum-threshold 20 milliseconds drop-probability 80
   !
   uc-tx-queue 4
      !! Test guaranteed percent
      bandwidth guaranteed percent 10
      random-detect drop minimum-threshold 1 microseconds maximum-threshold 10 microseconds drop-probability 90
```

### QOS Interfaces

| Interface | Trust | Default DSCP | Default COS | Shape rate |
| --------- | ----- | ------------ | ----------- | ---------- |
| Ethernet1 | dscp | 48 | - | - |
| Ethernet6 | cos | - | 2 | - |
| Port-Channel3 | cos | - | 2 | - |

### Priority Flow Control

#### Global Settings

Priority Flow Control is **Off** on all interfaces.

##### Priority Flow Control Watchdog Settings

| Action | Timeout | Recovery | Polling | Override Action Drop |
| ------ | ------- | -------- | ------- |
| no-drop | 0.05 | 1.22 | 10.001 | False |

```eos
!
priority-flow-control all off
priority-flow-control pause watchdog default timeout 0.05
priority-flow-control pause watchdog default recovery-time 1.22
priority-flow-control pause watchdog default polling-interval 10.001
priority-flow-control pause watchdog action no-drop
```
