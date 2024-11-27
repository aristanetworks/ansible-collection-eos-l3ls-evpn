# prefix-lists

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Filters](#filters)
  - [Dynamic Prefix-lists](#dynamic-prefix-lists)
  - [Prefix-lists](#prefix-lists-1)
  - [IPv6 Prefix-lists](#ipv6-prefix-lists)

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

## Filters

### Dynamic Prefix-lists

#### Dynamic Prefix-lists Summary

| Dynamic Prefix-List Name | Match Map | IPv4 Prefix-list | IPv6 Prefix-list |
| ------------------------ | --------- | ---------------- | ---------------- |
| DYNAMIC_PREFIX_LIST_NAME_1 | Test_1 | IPV4_PREFIX_LIST | - |
| DYNAMIC_PREFIX_LIST_NAME_2 | Test_2 | - | IPV6_PREFIX_LIST |
| DYNAMIC_PREFIX_LIST_NAME_3 | Test_2 | IPV4_PREFIX_LIST | IPV6_PREFIX_LIST |

#### Dynamic Prefix-lists Device Configuration

```eos
!
dynamic prefix-list DYNAMIC_PREFIX_LIST_NAME_1
   match-map Test_1
   prefix-list ipv4 IPV4_PREFIX_LIST
!
dynamic prefix-list DYNAMIC_PREFIX_LIST_NAME_2
   match-map Test_2
   prefix-list ipv6 IPV6_PREFIX_LIST
!
dynamic prefix-list DYNAMIC_PREFIX_LIST_NAME_3
   match-map Test_2
   prefix-list ipv4 IPV4_PREFIX_LIST
   prefix-list ipv6 IPV6_PREFIX_LIST
```

### Prefix-lists

#### Prefix-lists Summary

##### PL-BGP-DEFAULT-BLUE-C1

| Sequence | Action |
| -------- | ------ |
| 10 | permit 0.0.0.0/0 le 1 |

##### PL-BGP-DEFAULT-RED-IN-C1

| Sequence | Action |
| -------- | ------ |
| 10 | permit 0.0.0.0/0 |

##### PL-BGP-DEFAULT-RED-OUT-C1

| Sequence | Action |
| -------- | ------ |
| 10 | permit 10.0.0.0/8 |

##### PL-IPV4-LOOPBACKS

| Sequence | Action |
| -------- | ------ |

##### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 192.168.255.0/24 eq 32 |
| 20 | permit 192.168.254.0/24 eq 32 |

#### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-BGP-DEFAULT-BLUE-C1
   seq 10 permit 0.0.0.0/0 le 1
!
ip prefix-list PL-BGP-DEFAULT-RED-IN-C1
   seq 10 permit 0.0.0.0/0
!
ip prefix-list PL-BGP-DEFAULT-RED-OUT-C1
   seq 10 permit 10.0.0.0/8
!
ip prefix-list PL-IPV4-LOOPBACKS
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 192.168.255.0/24 eq 32
   seq 20 permit 192.168.254.0/24 eq 32
```

### IPv6 Prefix-lists

#### IPv6 Prefix-lists Summary

##### PL-IPV6-LOOPBACKS

| Sequence | Action |
| -------- | ------ |
| 10 | permit 1b11:3a00:22b0:0082::/64 eq 128 |

#### IPv6 Prefix-lists Device Configuration

```eos
!
ipv6 prefix-list PL-IPV6-LOOPBACKS
   seq 10 permit 1b11:3a00:22b0:0082::/64 eq 128
```
