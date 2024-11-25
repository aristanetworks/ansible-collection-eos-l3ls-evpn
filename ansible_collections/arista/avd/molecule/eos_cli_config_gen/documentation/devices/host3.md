# host3

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
| 65101.0001 | 192.168.255.3 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| update wait-install |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| maximum-paths 2 ecmp 2 |
| graceful-restart-helper long-lived |
| bgp additional-paths send limit 5 |

#### Router BGP Device Configuration

```eos
!
router bgp 65101.0001
   router-id 192.168.255.3
   graceful-restart-helper long-lived
   no bgp default ipv4-unicast
   update wait-install
   distance bgp 20 200 200
   graceful-restart restart-time 300
   maximum-paths 2 ecmp 2
   bgp additional-paths send limit 5
   redistribute ospf include leaked route-map RM-OSPF-TO-BGP
   redistribute static
   !
   address-family ipv4 multicast
      redistribute attached-host
      redistribute connected
      redistribute isis rcf Router_BGP_Isis()
      redistribute ospf match internal
      redistribute ospfv3 match internal
      redistribute ospfv3 match external
      redistribute ospfv3 match nssa-external 2
      redistribute ospf match external
      redistribute ospf match nssa-external 2
   !
   address-family ipv6
      redistribute ospfv3 include leaked route-map RM-REDISTRIBUTE-OSPFV3
      redistribute ospfv3 match external include leaked route-map RM-REDISTRIBUTE-OSPFV3-EXTERNAL
```
