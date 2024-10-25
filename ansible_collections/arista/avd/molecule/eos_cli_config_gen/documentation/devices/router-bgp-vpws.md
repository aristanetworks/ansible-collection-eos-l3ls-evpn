# router-bgp-vpws

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
| 65101 | 192.168.255.3 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| maximum-paths 2 ecmp 2 |

#### Router BGP VPWS Instances

| Instance | Route-Distinguisher | Both Route-Target | MPLS Control Word | Label Flow | MTU | Pseudowire | Local ID | Remote ID |
| -------- | ------------------- | ----------------- | ----------------- | -----------| --- | ---------- | -------- | --------- |
| TENANT_A | 100.70.0.2:1000 | 65000:1000 | True | True | 1600 | TEN_A_site1_site3_pw | 15 | 35 |
| TENANT_A | 100.70.0.2:1000 | 65000:1000 | True | True | 1600 | TEN_A_site2_site5_pw | 25 | 57 |
| TENANT_B | 100.70.0.2:2000 | 65000:2000 | False | False | - | TEN_B_site2_site5_pw | 26 | 58 |

#### Router BGP Device Configuration

```eos
!
router bgp 65101
   router-id 192.168.255.3
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 2 ecmp 2
   !
   vpws TENANT_A
      rd 100.70.0.2:1000
      route-target import export evpn 65000:1000
      mpls control-word
      label flow
      mtu 1600
      !
      pseudowire TEN_A_site1_site3_pw
         evpn vpws id local 15 remote 35
      !
      pseudowire TEN_A_site2_site5_pw
         evpn vpws id local 25 remote 57
   !
   vpws TENANT_B
      rd 100.70.0.2:2000
      route-target import export evpn 65000:2000
      !
      pseudowire TEN_B_site2_site5_pw
         evpn vpws id local 26 remote 58
```
