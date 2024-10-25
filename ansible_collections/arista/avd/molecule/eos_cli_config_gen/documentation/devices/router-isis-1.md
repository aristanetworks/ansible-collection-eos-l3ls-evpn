# router-isis-1

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
| MPLS LDP Sync Default | True |
| SPF Interval | 250 seconds |
| SPF Interval Wait Time| 30 milliseconds |

#### ISIS Interfaces Summary

| Interface | ISIS Instance | ISIS Metric | Interface Mode |
| --------- | ------------- | ----------- | -------------- |

#### Prefix Segments

| Prefix Segment | Index |
| -------------- | ----- |

#### Router ISIS Device Configuration

```eos
!
router isis EVPN_UNDERLAY
   mpls ldp sync default
   set-overload-bit
   set-overload-bit on-startup wait-for-bgp timeout 10
   spf-interval 250 30
   authentication mode shared-secret profile test1 algorithm md5 rx-disabled
   authentication key 0 password
   !
   segment-routing mpls
```
