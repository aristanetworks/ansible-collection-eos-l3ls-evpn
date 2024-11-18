# router-bgp-ipv4-labeled-unicast

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Routing](#routing)
  - [Router BGP](#router-bgp)

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

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65101 | - |

#### Router BGP IPv4 Labeled Unicast

##### General Settings

| Settings | Value |
| -------- | ----- |
| Update wait-for-convergence | Enabled |
| Next-hop Unchanged | True |
| Label local-termination | implicit-null |

##### IPv4 BGP-LU Peer-groups

| Peer-group | Activate | Route-map In | Route-map Out | RCF In | RCF Out |
| ---------- | -------- | ------------ | ------------- | ------ | ------- |
| PG-BGP-LU | True | - | - | - | - |

##### IPv4 BGP-LU Neighbors

| Neighbor | Activate | Route-map In | Route-map Out | RCF In | RCF Out |
| -------- | -------- | ------------ | ------------- | ------ | ------- |
| 198.51.100.1 | True | - | - | RCF_TEST(ARGS) | - |
| 198.51.100.2 | False | - | RM_OUT_TEST | - | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65101
   timers bgp 4 6 min-hold-time 5 send-failure hold-time 67
   !
   address-family ipv4 labeled-unicast
      update wait-for-convergence
      bgp missing-policy include community-list direction in action deny
      bgp additional-paths receive
      bgp additional-paths send ecmp limit 20
      bgp next-hop-unchanged
      next-hop resolution ribs tunnel-rib colored system-colored-tunnel-rib tunnel-rib test-rib system-connected
      neighbor PG-BGP-LU activate
      neighbor 198.51.100.1 activate
      neighbor 198.51.100.1 additional-paths receive
      neighbor 198.51.100.1 graceful-restart
      neighbor 198.51.100.1 rcf in RCF_TEST(ARGS)
      neighbor 198.51.100.1 additional-paths send ecmp
      neighbor 198.51.100.1 maximum-advertised-routes 0
      no neighbor 198.51.100.2 activate
      neighbor 198.51.100.2 graceful-restart-helper stale-route route-map RM_STALE
      neighbor 198.51.100.2 route-map RM_OUT_TEST out
      neighbor 198.51.100.2 next-hop-unchanged
      neighbor 198.51.100.2 aigp-session
      neighbor 198.51.100.2 multi-path
      network 203.0.113.0/25 route-map RM-TEST
      network 203.0.113.128/25
      label local-termination implicit-null
      tunnel source-protocol isis segment-routing
      tunnel source-protocol ldp rcf TEST(ARGS)
      aigp-session confederation
      aigp-session ebgp
```
