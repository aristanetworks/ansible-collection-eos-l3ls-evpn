# ip-access-lists

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [ACL](#acl)
  - [IP Access-lists](#ip-access-lists-1)

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
