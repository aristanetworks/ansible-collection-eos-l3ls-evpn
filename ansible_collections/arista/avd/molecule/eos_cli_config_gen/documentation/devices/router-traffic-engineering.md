# router-traffic-engineering

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Routing](#routing)
  - [Router Traffic-Engineering](#router-traffic-engineering-1)

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

### Router Traffic-Engineering

- Traffic Engineering is enabled.

#### Segment Routing Summary

- SRTE is enabled.

- system-colored-tunnel-rib is enabled

##### SRTE Policies

| Endpoint | Color | Preference | Name | Description | SBFD Remote Discriminator | Label Stack | Index  | Weight | Explicit Null |
| -------- | ----- | ---------- | ---- | ----------- | ------------------------- | ----------- | ------ | ------ | ------------- |
| 1.2.3.4 | 70810 | 180 | SRTE-1.2.3.4-70810 | SRTE POLICY FOR 1.2.3.4 COLOR 70810 | 155.2.1.1 | 900002 900003 900005 900006 | 200 | - | ipv4 ipv6 |
| 1.2.3.4 | 80810 | 100 | SRTE-1.2.3.4-80810 | SRTE POLICY FOR 1.2.3.4 COLOR 80810 | - | 900002 900008 900007 900006 | 100 | 20 | none |
| 5.6.7.8 | 20320 | 80 | - | - | 2600599809 | 900002 900003 900005 900006 | 300 | 120 | ipv4 |
| 5.6.7.8 | 20320 | 80 | - | - | 2600599809 | 900002 900004 900007 900006 | 400 | 220 | ipv4 |
| 5.6.7.8 | 20320 | 120 | - | - | 2600599809 | 900002 900008 900009 900006 | - | - | ipv6 |
| 5.6.7.8 | 20320 | 120 | - | - | 2600599809 | 900002 900010 900011 900012 | - | - | ipv6 |

#### Router Traffic Engineering Device Configuration

```eos
!
router traffic-engineering
   segment-routing
      rib system-colored-tunnel-rib
      !
      policy endpoint 1.2.3.4 color 70810
         binding-sid 970810
         name SRTE-1.2.3.4-70810
         description SRTE POLICY FOR 1.2.3.4 COLOR 70810
         sbfd remote-discriminator 155.2.1.1
         !
         path-group preference 180
            explicit-null ipv4 ipv6
            segment-list label-stack 900002 900003 900005 900006 index 200
      !
      policy endpoint 1.2.3.4 color 80810
         name SRTE-1.2.3.4-80810
         description SRTE POLICY FOR 1.2.3.4 COLOR 80810
         !
         path-group preference 100
            explicit-null none
            segment-list label-stack 900002 900008 900007 900006 weight 20 index 100
      !
      policy endpoint 5.6.7.8 color 20320
         binding-sid 978320
         sbfd remote-discriminator 2600599809
         !
         path-group preference 80
            explicit-null ipv4
            segment-list label-stack 900002 900003 900005 900006 weight 120 index 300
            segment-list label-stack 900002 900004 900007 900006 weight 220 index 400
         !
         path-group preference 120
            explicit-null ipv6
            segment-list label-stack 900002 900008 900009 900006
            segment-list label-stack 900002 900010 900011 900012
   router-id ipv4 10.0.0.1
   router-id ipv6 2001:beef:cafe::1
```
