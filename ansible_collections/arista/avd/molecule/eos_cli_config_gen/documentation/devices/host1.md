# host1

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [ACL](#acl)
  - [Standard Access-lists](#standard-access-lists)
  - [Extended Access-lists](#extended-access-lists)
  - [IP Access-lists](#ip-access-lists)
  - [IPv6 Standard Access-lists](#ipv6-standard-access-lists)
  - [IPv6 Extended Access-lists](#ipv6-extended-access-lists)
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

### Standard Access-lists

#### Standard Access-lists Summary

##### 99

| Sequence | Action |
| -------- | ------ |
| 10 | remark ACL to restrict access RFC1918 addresses |
| 20 | permit 10.0.0.0/8 |
| 30 | permit 172.16.0.0/12 |
| 40 | permit 192.168.0.0/16 |

##### ACL-API

| Sequence | Action |
| -------- | ------ |
| 10 | remark ACL to restrict access to switch API to CVP and Ansible |
| 20 | permit host 10.10.10.10 |
| 30 | permit host 10.10.10.11 |
| 40 | permit host 10.10.10.12 |

##### ACL-SSH

ACL has counting mode `counters per-entry` enabled!

| Sequence | Action |
| -------- | ------ |
| 10 | remark ACL to restrict access RFC1918 addresses |
| 20 | permit 10.0.0.0/8 |
| 30 | permit 172.16.0.0/12 |
| 40 | permit 192.168.0.0/16 |

##### ACL-SSH-VRF

| Sequence | Action |
| -------- | ------ |
| 10 | remark ACL to restrict access RFC1918 addresses |
| 20 | permit 10.0.0.0/8 |
| 30 | permit 172.16.0.0/12 |
| 40 | permit 192.168.0.0/16 |

#### Standard Access-lists Device Configuration

```eos
!
ip access-list standard 99
   10 remark ACL to restrict access RFC1918 addresses
   20 permit 10.0.0.0/8
   30 permit 172.16.0.0/12
   40 permit 192.168.0.0/16
!
ip access-list standard ACL-API
   10 remark ACL to restrict access to switch API to CVP and Ansible
   20 permit host 10.10.10.10
   30 permit host 10.10.10.11
   40 permit host 10.10.10.12
!
ip access-list standard ACL-SSH
   counters per-entry
   10 remark ACL to restrict access RFC1918 addresses
   20 permit 10.0.0.0/8
   30 permit 172.16.0.0/12
   40 permit 192.168.0.0/16
!
ip access-list standard ACL-SSH-VRF
   10 remark ACL to restrict access RFC1918 addresses
   20 permit 10.0.0.0/8
   30 permit 172.16.0.0/12
   40 permit 192.168.0.0/16
```

### Extended Access-lists

#### Extended Access-lists Summary

##### 4

| Sequence | Action |
| -------- | ------ |
| 10 | remark ACL to restrict access RFC1918 addresses |
| 20 | deny ip 10.0.0.0/8 any |
| 30 | permit ip 192.0.2.0/24 any |

##### ACL-01

| Sequence | Action |
| -------- | ------ |
| 10 | remark ACL to restrict access to switch API to CVP and Ansible |
| 20 | deny ip host 192.0.2.1 any |
| 30 | permit ip 192.0.2.0/24 any |

##### ACL-02

ACL has counting mode `counters per-entry` enabled!

| Sequence | Action |
| -------- | ------ |
| 10 | remark ACL to restrict access RFC1918 addresses |
| 20 | permit ip 10.0.0.0/8 any |
| 30 | permit ip 192.0.2.0/24 any |
| - | permit response traffic nat |

##### ACL-03

| Sequence | Action |
| -------- | ------ |
| 10 | remark ACL to restrict access RFC1918 addresses |
| 20 | deny ip 10.0.0.0/8 any |
| 30 | permit ip 192.0.2.0/24 any |

##### ACL-04

ACL has counting mode `counters per-entry` enabled!

| Sequence | Action |
| -------- | ------ |
| 20 | deny ip 12.0.0.0/8 any |
| 30 | permit ip 194.0.2.0/24 any |
| - | permit response traffic nat |

#### Extended Access-lists Device Configuration

```eos
!
ip access-list 4
   10 remark ACL to restrict access RFC1918 addresses
   20 deny ip 10.0.0.0/8 any
   30 permit ip 192.0.2.0/24 any
!
ip access-list ACL-01
   10 remark ACL to restrict access to switch API to CVP and Ansible
   20 deny ip host 192.0.2.1 any
   30 permit ip 192.0.2.0/24 any
!
ip access-list ACL-02
   counters per-entry
   10 remark ACL to restrict access RFC1918 addresses
   20 permit ip 10.0.0.0/8 any
   30 permit ip 192.0.2.0/24 any
   permit response traffic nat
!
ip access-list ACL-03
   10 remark ACL to restrict access RFC1918 addresses
   20 deny ip 10.0.0.0/8 any
   30 permit ip 192.0.2.0/24 any
!
ip access-list ACL-04
   counters per-entry
   20 deny ip 12.0.0.0/8 any
   30 permit ip 194.0.2.0/24 any
   permit response traffic nat
```

### IP Access-lists

#### IP Access-lists Summary

- The maximum number of ACL entries allowed to be provisioned per switch: 10000

#### IP Access-lists Device Configuration

```eos
!
ip access-list ACL_NO_SEQUENCE
   remark test acl without sequence numbers
   deny udp any any log
   permit icmp any any 3 4 ttl eq 40
   permit icmp any any unreachable ttl gt 3
   permit ip any any fragments dscp 46
   permit ip any any tracked dscp ef
   permit ip any any nexthop-group NH_TEST
   permit vlan inner 123 0x000 ip any any
   permit vlan 234 0xFFF ip any any
   permit icmp any any
!
ip access-list ACL_SEQUENCE_AND_COUNTERS
   counters per-entry
   10 remark test acl with sequence numbers
   20 permit ip 10.0.0.0/8 any
   30 permit tcp host 192.168.122.22 any established
   40 permit tcp any gt 1023 host 172.16.16.16 eq 22
   50 permit tcp any range 1000 1100 any range 10 20
   4294967295 deny ip any any
   permit response traffic nat
```

### IPv6 Standard Access-lists

#### IPv6 Standard Access-lists Summary

##### TEST4

| Sequence | Action |
| -------- | ------ |
| 5 | deny fe80::/64 |
| 10 | permit fe90::/64 |

##### TEST5

ACL has counting mode `counters per-entry` enabled!

| Sequence | Action |
| -------- | ------ |
| 5 | permit 2001:db8::/64 |
| 10 | deny 2001:db8::/32 |

##### TEST6

| Sequence | Action |
| -------- | ------ |
| 5 | deny 2001:db8:1000::/64 |
| 10 | permit 2001:db8::/32 |

#### IPv6 Standard Access-lists Device Configuration

```eos
!
ipv6 access-list standard TEST4
   5 deny fe80::/64
   10 permit fe90::/64
!
ipv6 access-list standard TEST5
   counters per-entry
   5 permit 2001:db8::/64
   10 deny 2001:db8::/32
!
ipv6 access-list standard TEST6
   5 deny 2001:db8:1000::/64
   10 permit 2001:db8::/32
```

### IPv6 Extended Access-lists

#### IPv6 Extended Access-lists Summary

##### TEST1

| Sequence | Action |
| -------- | ------ |
| 5 | deny ipv6 fe80::/64 any |
| 10 | permit ipv6 fe90::/64 any |

##### TEST2

ACL has counting mode `counters per-entry` enabled!

| Sequence | Action |
| -------- | ------ |
| 5 | permit ipv6 2001:db8::/64 any |
| 10 | deny ipv6 2001:db8::/32 any |

##### TEST3

| Sequence | Action |
| -------- | ------ |
| 5 | deny ipv6 2001:db8:1000::/64 any |
| 10 | permit ipv6 2001:db8::/32 any |

#### IPv6 Extended Access-lists Device Configuration

```eos
!
ipv6 access-list TEST1
   5 deny ipv6 fe80::/64 any
   10 permit ipv6 fe90::/64 any
!
ipv6 access-list TEST2
   counters per-entry
   5 permit ipv6 2001:db8::/64 any
   10 deny ipv6 2001:db8::/32 any
!
ipv6 access-list TEST3
   5 deny ipv6 2001:db8:1000::/64 any
   10 permit ipv6 2001:db8::/32 any
```

## IP NAT

| Setting | Value |
| -------- | ----- |
| Kernel Buffer Size | 64 MB |

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
| port_only_1 | port-only | - | - | - | - |
| port_only_2 | port-only | - | - | - | 10-15<br>1024-65535 |
| prefix_16 | ip-port | 16 | 91 | 10.0.0.1-10.0.255.254<br>10.1.0.0-10.1.255.255 | -<br>1024-65535 |
| prefix_21 | ip-port | 21 | - | - | - |
| prefix_24 | ip-port | 24 | 100 | - | - |
| prefix_32 | ip-port | 32 | - | 10.2.0.1-10.2.0.1<br>10.2.0.2-10.2.0.3 | 1024-65535<br>- |

### NAT Synchronization

| Setting | Value |
| -------- | ----- |
| State | Disabled |
| Expiry Interval | 60 Seconds |
| Interface | Ethernet1 |
| Peer IP Address | 1.1.1.1 |
| Port Range | 1024 - 65535 |
| Port Range Split | Disabled |

### NAT Translation Settings

| Setting | Value |
| -------- | ----- |
| Address Selection | Any |
| Address Selection | Hash Source IP Field |
| Counters | Enabled |
| Global Connection Limit | max. 100000 Connections |
| per Host Connection Limit | max. 1000 Connections |
| IP Host 10.0.0.1 Connection Limit | max. 100 Connections |
| IP Host 10.0.0.2 Connection Limit | max. 200 Connections |
| Global Connection Limit Low Mark | 50 % |
| per Host Connection Limit Low Mark | 50 % |
| UDP Connection Timeout | 3600 Seconds |
| TCP Connection Timeout | 7200 Seconds |

### IP NAT Device Configuration

```eos
!
ip nat translation address selection hash field source-ip
ip nat translation address selection any
ip nat translation tcp-timeout 7200
ip nat translation udp-timeout 3600
ip nat translation max-entries 100000
ip nat translation low-mark 50
ip nat translation max-entries 1000 host
ip nat translation low-mark 50 host
ip nat translation max-entries 100 10.0.0.1
ip nat translation max-entries 200 10.0.0.2
ip nat kernel buffer size 64
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
ip nat pool prefix_16 prefix-length 16
   range 10.0.0.1 10.0.255.254
   range 10.1.0.0 10.1.255.255 1024 65535
   utilization threshold 91 action log
ip nat pool prefix_21 prefix-length 21
ip nat pool prefix_24 prefix-length 24
   utilization threshold 100 action log
ip nat pool prefix_32 prefix-length 32
   range 10.2.0.1 10.2.0.1 1024 65535
   range 10.2.0.2 10.2.0.3
ip nat pool port_only_1 port-only
ip nat pool port_only_2 port-only
   port range 10 15
   port range 1024 65535
ip nat synchronization
   description test sync config
   expiry-interval 60
   shutdown
   peer-address 1.1.1.1
   local-interface Ethernet1
   port-range 1024 65535
   port-range split disabled
```
