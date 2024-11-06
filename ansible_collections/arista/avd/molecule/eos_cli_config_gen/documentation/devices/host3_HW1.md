# host3_HW1

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [ACL](#acl)
  - [Extended Access-lists](#extended-access-lists)
  - [IP Access-lists](#ip-access-lists)
- [IP NAT](#ip-nat)
  - [NAT Profiles](#nat-profiles)
  - [NAT Pools](#nat-pools)
  - [NAT Synchronization](#nat-synchronization)
  - [NAT Translation Settings](#nat-translation-settings)
  - [IP NAT Device Configuration](#ip-nat-device-configuration)

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

## ACL

### Extended Access-lists

#### Extended Access-lists Summary

##### ACL-02

| Sequence | Action |
| -------- | ------ |
| 20 | permit ip 10.0.0.0/8 any |
| - | permit response traffic nat |

#### Extended Access-lists Device Configuration

```eos
!
ip access-list ACL-02
   20 permit ip 10.0.0.0/8 any
   permit response traffic nat
```

### IP Access-lists

#### IP Access-lists Device Configuration

```eos
!
ip access-list ACL_SEQUENCE
   10 remark test acl with sequence numbers
   permit response traffic nat
```

## IP NAT

### NAT Profiles

#### Profile: NAT-PROFILE-NO-VRF-1

#### Profile: NAT-PROFILE-NO-VRF-2

##### IP NAT: Source Static

| Direction | Original IP | Original Port | Access List | Translated IP | Translated Port | Protocol | Group | Priority | Comment |
| --------- | ----------- | ------------- | ----------- | ------------- | --------------- | -------- | ----- | -------- | ------- |
| - | 3.0.0.1 | - | - | 4.0.0.1 | - | - | - | 0 | - |
| - | 3.0.0.2 | 22 | - | 4.0.0.2 | - | - | - | 0 | - |
| - | 3.0.0.3 | 22 | - | 4.0.0.3 | 23 | - | - | 0 | - |
| - | 3.0.0.4 | 22 | - | 4.0.0.4 | 23 | UDP | - | 0 | - |
| - | 3.0.0.5 | 22 | - | 4.0.0.5 | 23 | TCP | 1 | 0 | - |
| - | 3.0.0.6 | 22 | - | 4.0.0.6 | 23 | TCP | 2 | 5 | Comment Test |
| - | 3.0.0.7 | - | ACL21 | 4.0.0.7 | - | - | - | 0 | - |
| ingress | 3.0.0.8 | - | - | 4.0.0.8 | - | - | - | 0 | - |

##### IP NAT: Source Dynamic

| Access List | NAT Type | Pool Name | Priority | Comment |
| ----------- | -------- | --------- | -------- | ------- |
| ACL11 | pool | POOL11 | 0 | - |
| ACL12 | pool | POOL11 | 0 | POOL11 shared with ACL11/12 |
| ACL13 | pool | POOL13 | 10 | - |
| ACL14 | pool | POOL14 | 1 | Priority low end |
| ACL15 | pool | POOL15 | 4294967295 | Priority high end |
| ACL16 | pool | POOL16 | 0 | Priority default |
| ACL17 | overload | - | 10 | Priority_10 |
| ACL18 | pool-address-only | POOL18 | 10 | Priority_10 |
| ACL19 | pool-full-cone | POOL19 | 10 | Priority_10 |

##### IP NAT: Destination Static

| Direction | Original IP | Original Port | Access List | Translated IP | Translated Port | Protocol | Group | Priority | Comment |
| --------- | ----------- | ------------- | ----------- | ------------- | --------------- | -------- | ----- | -------- | ------- |
| - | 1.0.0.1 | - | - | 2.0.0.1 | - | - | - | 0 | - |
| - | 1.0.0.2 | 22 | - | 2.0.0.2 | - | - | - | 0 | - |
| - | 1.0.0.2 | 23 | - | 2.0.0.3 | 23 | - | - | 0 | - |
| - | 1.0.0.4 | 22 | - | 2.0.0.4 | 23 | udp | - | 0 | - |
| - | 1.0.0.5 | 22 | - | 2.0.0.5 | 23 | tcp | 1 | 0 | - |
| - | 1.0.0.6 | 22 | - | 2.0.0.6 | 23 | tcp | 2 | 5 | Comment Test |
| - | 1.0.0.7 | - | ACL21 | 2.0.0.7 | - | - | - | 0 | - |
| egress | 239.0.0.1 | - | - | 239.0.0.2 | - | - | - | 0 | - |

##### IP NAT: Destination Dynamic

| Access List | Pool Name | Priority | Comment |
| ----------- | --------- | -------- | ------- |
| ACL1 | POOL1 | 0 | - |
| ACL2 | POOL1 | 0 | POOL1 shared with ACL1/2 |
| ACL3 | POOL3 | 10 | - |
| ACL4 | POOL4 | 1 | Priority low end |
| ACL5 | POOL5 | 4294967295 | Priority high end |
| ACL6 | POOL6 | 0 | Priority default |

#### Profile: NAT-PROFILE-TEST-VRF

NAT profile VRF is: TEST

### NAT Pools

| Pool Name | Pool Type | Prefix Length | Utilization Log Threshold | First-Last IP Addresses | First-Last Ports |
| --------- | --------- | ------------- | ------------------------- | ----------------------- | ---------------- |
| port-only_3 | port-only | - | - | - | 10- |
| port_only_1 | port-only | - | - | - | - |
| port_only_2 | port-only | - | - | - | 1024-65535 |

### NAT Synchronization

| Setting | Value |
| -------- | ----- |
| State | Enabled |
| Port Range Split | Enabled |

### NAT Translation Settings

| Setting | Value |
| -------- | ----- |
| Address Selection | Any |

### IP NAT Device Configuration

```eos
!
ip nat translation address selection any
!
ip nat profile NAT-PROFILE-NO-VRF-1
!
ip nat profile NAT-PROFILE-NO-VRF-2
   ip nat destination static 1.0.0.1 2.0.0.1
   ip nat destination static 1.0.0.2 22 2.0.0.2
   ip nat destination static 1.0.0.2 23 2.0.0.3 23
   ip nat destination static 1.0.0.4 22 2.0.0.4 23 protocol udp
   ip nat destination static 1.0.0.7 access-list ACL21 2.0.0.7
   ip nat source static 3.0.0.1 4.0.0.1
   ip nat source static 3.0.0.2 22 4.0.0.2
   ip nat source static 3.0.0.3 22 4.0.0.3 23
   ip nat source static 3.0.0.4 22 4.0.0.4 23 protocol udp
   ip nat source static 3.0.0.7 access-list ACL21 4.0.0.7
   ip nat source ingress static 3.0.0.8 4.0.0.8
   ip nat destination egress static 239.0.0.1 239.0.0.2
   ip nat source static 3.0.0.5 22 4.0.0.5 23 protocol tcp group 1
   ip nat destination static 1.0.0.5 22 2.0.0.5 23 protocol tcp group 1
   ip nat source static 3.0.0.6 22 4.0.0.6 23 protocol tcp group 2 comment Comment Test
   ip nat destination static 1.0.0.6 22 2.0.0.6 23 protocol tcp group 2 comment Comment Test
   ip nat destination dynamic access-list ACL1 pool POOL1
   ip nat source dynamic access-list ACL11 pool POOL11
   ip nat source dynamic access-list ACL12 pool POOL11 comment POOL11 shared with ACL11/12
   ip nat source dynamic access-list ACL13 pool POOL13 priority 10
   ip nat source dynamic access-list ACL14 pool POOL14 priority 1 comment Priority low end
   ip nat source dynamic access-list ACL15 pool POOL15 priority 4294967295 comment Priority high end
   ip nat source dynamic access-list ACL16 pool POOL16 comment Priority default
   ip nat source dynamic access-list ACL17 overload priority 10 comment Priority_10
   ip nat source dynamic access-list ACL18 pool POOL18 address-only priority 10 comment Priority_10
   ip nat source dynamic access-list ACL19 pool POOL19 full-cone priority 10 comment Priority_10
   ip nat destination dynamic access-list ACL2 pool POOL1 comment POOL1 shared with ACL1/2
   ip nat destination dynamic access-list ACL3 pool POOL3 priority 10
   ip nat destination dynamic access-list ACL4 pool POOL4 priority 1 comment Priority low end
   ip nat destination dynamic access-list ACL5 pool POOL5 priority 4294967295 comment Priority high end
   ip nat destination dynamic access-list ACL6 pool POOL6 comment Priority default
!
ip nat profile NAT-PROFILE-TEST-VRF vrf TEST
!
ip nat pool port-only_3 port-only
ip nat pool port_only_1 port-only
ip nat pool port_only_2 port-only
   port range 1024 65535
```
