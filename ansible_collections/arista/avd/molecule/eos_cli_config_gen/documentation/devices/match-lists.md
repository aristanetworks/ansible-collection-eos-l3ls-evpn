# match-lists

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Filters](#filters)
  - [Match-lists](#match-lists-1)

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

### Match-lists

#### Match-list Input IPv4-prefix Summary

| Prefix List Name | Prefixes |
| ---------------- | -------- |
| molecule_v4 | 10.10.10.0/24, 10.10.20.0/24 |

#### Match-list Input IPv6-prefix Summary

| Prefix List Name | Prefixes |
| ---------------- | -------- |
| molecule_v6 | 2001:0DB8::/32 |

#### Match-list Input String Summary

##### molecule

| Sequence | Match Regex |
| -------- | ------ |
| 10 | ^.*MOLECULE.*$ |
| 20 | ^.*TESTING.*$ |

#### Match-lists Device Configuration

```eos
!
match-list input string molecule
   10 match regex ^.*MOLECULE.*$
   20 match regex ^.*TESTING.*$
!
match-list input prefix-ipv4 molecule_v4
   match prefix-ipv4 10.10.10.0/24
   match prefix-ipv4 10.10.20.0/24
!
match-list input prefix-ipv6 molecule_v6
   match prefix-ipv6 2001:0DB8::/32
```
