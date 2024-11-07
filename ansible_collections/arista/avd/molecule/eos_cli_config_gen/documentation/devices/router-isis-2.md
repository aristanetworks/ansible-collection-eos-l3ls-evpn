# router-isis-2

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Routing](#routing)
  - [Router ISIS](#router-isis)

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

### Router ISIS

#### Router ISIS Summary

| Settings | Value |
| -------- | ----- |
| Instance | EVPN_UNDERLAY |

#### ISIS Route Timers

| Settings | Value |
| -------- | ----- |
| LSP Generation Maximum Interval | 30 seconds |

#### ISIS Interfaces Summary

| Interface | ISIS Instance | ISIS Metric | Interface Mode |
| --------- | ------------- | ----------- | -------------- |

#### Router ISIS Device Configuration

```eos
!
router isis EVPN_UNDERLAY
   set-overload-bit
   set-overload-bit on-startup 55
   timers lsp generation 30
   authentication mode sha key-id 4 rx-disabled
   !
```
