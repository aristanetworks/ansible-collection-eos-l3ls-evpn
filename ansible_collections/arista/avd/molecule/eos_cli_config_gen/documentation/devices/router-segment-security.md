# router-segment-security

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Group-Based Multi-domain Segmentation Services (MSS-Group)](#group-based-multi-domain-segmentation-services-mss-group)
  - [Segmentation Policies](#segmentation-policies)
  - [Segment Definitions](#segment-definitions)
  - [Router MSS-G Device Configuration](#router-mss-g-device-configuration)

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

## Group-Based Multi-domain Segmentation Services (MSS-Group)

MSS-G is enabled.

### Segmentation Policies

#### POLICY-TEST1

| Sequence Number | Application Name | Action | Next-Hop | Log | Stateless |
| --------------- | ---------------- | ------ | -------- | --- | --------- |
| 10 | APP-TEST-1 | forward | - | - | False |
| 20 | APP-TEST-2 | drop | - | True | - |
| 25 | APP-TEST-3 | redirect | 198.51.100.1 | - | - |

### Segment Definitions

#### VRF default Segmentation

##### Segment SEGMENT-TEST1 Definitions

| Interface | Match-List Name | Covered Prefix-List Name | Address Family |
| --------- |---------------- | ------------------------ | -------------- |
| - | MATCH-LIST10 | - | ipv4 |
| - | MATCH-LIST11 | - | ipv6 |

##### Segment SEGMENT-TEST1 Policies

| Source Segment | Policy Applied |
| -------------- | -------------- |
| MATCH-LIST22 | POLICY-TEST1 |

##### Segment SEGMENT-TEST2 Definitions

| Interface | Match-List Name | Covered Prefix-List Name | Address Family |
| --------- |---------------- | ------------------------ | -------------- |
| - | MATCH-LIST4 | - | ipv4 |
| - | MATCH-LIST3 | - | ipv6 |

##### Segment SEGMENT-TEST2 Policies

| Source Segment | Policy Applied |
| -------------- | -------------- |
| MATCH-LIST20 | policy-forward-all |
| MATCH-LIST21 | POLICY-TEST1 |
| MATCH-LIST30 | policy-drop-all |

#### VRF SECURE Segmentation

##### Segment SEGMENT-TEST1 Definitions

| Interface | Match-List Name | Covered Prefix-List Name | Address Family |
| --------- |---------------- | ------------------------ | -------------- |
| Ethernet1 | - | - | - |
| Ethernet2 | - | - | - |
| - | - | PREFIX-LIST10 | ipv4 |
| - | - | PREFIX-LIST1 | ipv6 |

##### Segment SEGMENT-TEST1 Policies

| Source Segment | Policy Applied |
| -------------- | -------------- |
| MATCH-LIST20 | policy-forward-all |
| MATCH-LIST30 | policy-drop-all |

Configured Fallback Policy: policy-custom

### Router MSS-G Device Configuration

```eos
!
router segment-security
   no shutdown
   !
   policy POLICY-TEST1
      10 application APP-TEST-1 action forward
      20 application APP-TEST-2 action drop stateless log
      25 application APP-TEST-3 action redirect next-hop 198.51.100.1 stateless
   !
   vrf default
      segment SEGMENT-TEST1
         definition
            match prefix-ipv4 MATCH-LIST10
            match prefix-ipv6 MATCH-LIST11
         !
         policies
            from MATCH-LIST22 policy POLICY-TEST1
      !
      segment SEGMENT-TEST2
         definition
            match prefix-ipv4 MATCH-LIST4
            match prefix-ipv6 MATCH-LIST3
         !
         policies
            from MATCH-LIST20 policy policy-forward-all
            from MATCH-LIST21 policy POLICY-TEST1
            from MATCH-LIST30 policy policy-drop-all
   !
   vrf SECURE
      segment SEGMENT-TEST1
         definition
            match interface Ethernet1
            match interface Ethernet2
            match covered prefix-list ipv4 PREFIX-LIST10
            match covered prefix-list ipv6 PREFIX-LIST1
         !
         policies
            from MATCH-LIST20 policy policy-forward-all
            from MATCH-LIST30 policy policy-drop-all
            fallback policy policy-custom
   !
```
