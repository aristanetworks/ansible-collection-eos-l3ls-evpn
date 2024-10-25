# peer-filters

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Filters](#filters)
  - [Peer Filters](#peer-filters-1)

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

### Peer Filters

#### Peer Filters Summary

##### PF1

| Sequence | Match |
| -------- | ----- |
| 10 | as-range 1-2 result reject |
| 20 | as-range 1-100 result accept |

##### PF2

| Sequence | Match |
| -------- | ----- |
| 30 | as-range 65000 result accept |

#### Peer Filters Device Configuration

```eos
!
peer-filter PF1
   10 match as-range 1-2 result reject
   20 match as-range 1-100 result accept
!
peer-filter PF2
   30 match as-range 65000 result accept
```
