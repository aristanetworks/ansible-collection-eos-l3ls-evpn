# ip-extended-community-lists

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Filters](#filters)
  - [IP Extended Community Lists](#ip-extended-community-lists-1)

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

### IP Extended Community Lists

#### IP Extended Community Lists Summary

| List Name | Type | Extended Communities |
| --------- | ---- | -------------------- |
| TEST1 | permit | 65000:65000 |
| TEST1 | deny | 65002:65002 |
| TEST2 | deny | 65001:65001 |

#### IP Extended Community Lists Device Configuration

```eos
!
ip extcommunity-list TEST1 permit 65000:65000
ip extcommunity-list TEST1 deny 65002:65002
!
ip extcommunity-list TEST2 deny 65001:65001
```
