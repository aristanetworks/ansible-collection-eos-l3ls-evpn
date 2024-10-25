# ip-extended-community-lists-regexp

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Filters](#filters)
  - [IP Extended Community RegExp Lists](#ip-extended-community-regexp-lists)

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

### IP Extended Community RegExp Lists

#### IP Extended Community RegExp Lists Summary

| List Name | Type | Regular Expression |
| --------- | ---- | ------------------ |
| TEST1 | permit | 65[0-9]{3}:[0-9]+ |
| TEST1 | deny | .* |
| TEST2 | deny | 6500[0-1]:650[0-9][0-9] |

#### IP Extended Community RegExp Lists Device Configuration

```eos
!
ip extcommunity-list regexp TEST1 permit 65[0-9]{3}:[0-9]+
ip extcommunity-list regexp TEST1 deny .*
!
ip extcommunity-list regexp TEST2 deny 6500[0-1]:650[0-9][0-9]
```
