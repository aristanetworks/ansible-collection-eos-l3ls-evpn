# router-bgp-vrf-address-families

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
| 65001 | 1.0.1.1 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 1.1.1.1 | - | VRF02 | - | - | - | - | - | - | - | - | - |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| VRF01 | - | user<br>static<br>rip<br>ospf<br>ospfv3<br>isis<br>connected<br>bgp<br>attached_host |
| VRF02 | - | dynamic<br>user<br>static<br>rip<br>ospf<br>ospfv3<br>isis<br>connected<br>bgp<br>attached_host |
| VRF03 | - | dynamic |

#### Router BGP Device Configuration

```eos
!
router bgp 65001
   router-id 1.0.1.1
   !
   address-family flow-spec ipv4
      neighbor FOOBAR activate
   !
   address-family flow-spec ipv6
      no neighbor FOOBAR activate
   !
   address-family ipv4
      neighbor FOOBAR activate
      neighbor FOOBAR next-hop address-family ipv6 originate
   !
   address-family ipv4 multicast
      bgp additional-paths receive
      neighbor FOOBAR activate
      neighbor FOOBAR additional-paths receive
      neighbor 10.1.1.1 activate
      neighbor 10.1.1.1 additional-paths receive
   !
   address-family ipv6
      no neighbor FOOBAR activate
   !
   address-family ipv6 multicast
      bgp additional-paths receive
      no neighbor FOOBAR activate
      neighbor FOOBAR additional-paths receive
      neighbor aa::1 additional-paths receive
      redistribute isis rcf Router_BGP_Isis()
      redistribute ospf match internal
      redistribute ospfv3 match external
      redistribute ospfv3 match nssa-external 2
   !
   vrf VRF01
      bgp additional-paths install
      bgp additional-paths receive
      bgp additional-paths send any
      no bgp redistribute-internal
      redistribute connected include leaked rcf RCF_VRF_CONNECTED()
      redistribute isis level-2 rcf RCF_VRF_ISIS()
      redistribute ospf match internal include leaked route-map RM_VRF_OSPF
      redistribute ospf match external include leaked route-map RM_VRF_OSPF
      redistribute ospf match nssa-external 1 include leaked route-map RM_VRF_OSPF
      redistribute ospfv3 match internal include leaked route-map RM_VRF_OSPF
      redistribute static route-map RM_VRF_STATIC
      redistribute rip route-map RM_VRF_RIP
      redistribute attached-host route-map RM_VRF_ATTACHED-HOST
      redistribute bgp leaked route-map RM_VRF_BGP
      redistribute user rcf RCF_VRF_USER()
      !
      address-family flow-spec ipv4
         bgp missing-policy direction in action permit
         bgp missing-policy direction out action permit
         neighbor 1.2.3.4 activate
      !
      address-family flow-spec ipv6
         bgp missing-policy direction in action permit
         bgp missing-policy direction out action deny
         neighbor aa::1 activate
      !
      address-family ipv4
         bgp additional-paths install ecmp-primary
         bgp missing-policy direction in action deny
         bgp missing-policy direction out action permit
         bgp additional-paths receive
         bgp additional-paths send ecmp limit 4
         neighbor 1.2.3.4 activate
         neighbor 1.2.3.4 additional-paths receive
         neighbor 1.2.3.4 route-map FOO in
         neighbor 1.2.3.4 route-map BAR out
         neighbor 1.2.3.4 additional-paths send any
         network 2.3.4.0/24 route-map BARFOO
         no bgp redistribute-internal
         redistribute attached-host route-map VRF_AFIPV4_RM_HOST
         redistribute bgp leaked route-map VRF_AFIPV4_RM_BGP
         redistribute connected include leaked rcf VRF_AFIPV4_RCF_CONNECTED_1()
         redistribute dynamic route-map VRF_AFIPV4_RM_DYNAMIC
         redistribute user rcf VRF_AFIPV4_RCF_USER()
         redistribute isis level-1 include leaked rcf VRF_AFIPV4_RCF_ISIS()
         redistribute ospf include leaked route-map VRF_AFIPV4_RM_OSPF
         redistribute ospfv3 match internal include leaked route-map VRF_AFIPV4_RM_OSPF
         redistribute ospfv3 match external include leaked route-map VRF_AFIPV4_RM_OSPF
         redistribute ospfv3 match nssa-external 2 include leaked route-map VRF_AFIPV4_RM_OSPF
         redistribute ospf match external include leaked route-map VRF_AFIPV4_RM_OSPF
         redistribute ospf match nssa-external 1 include leaked route-map VRF_AFIPV4_RM_OSPF
         redistribute rip route-map VRF_AFIPV4_RM_RIP
         redistribute static include leaked route-map VRF_AFIPV4_RM_STATIC_1
      !
      address-family ipv4 multicast
         bgp missing-policy direction in action permit
         bgp missing-policy direction out action permit
         bgp additional-paths receive
         neighbor 1.2.3.4 additional-paths receive
         neighbor 1.2.3.4 route-map FOO in
         neighbor 1.2.3.4 route-map BAR out
         network 239.0.0.0/24 route-map BARFOO
         redistribute attached-host route-map VRF_AFIPV4MULTI_RM_HOST
         redistribute connected route-map VRF_AFIPV4MULTI_RM_CONNECTED
         redistribute isis level-1 include leaked route-map VRF_AFIPV4MULTI_RM_ISIS
         redistribute ospf match internal route-map VRF_AFIPV4MULTI_RM_OSPF
         redistribute ospfv3 match internal route-map VRF_AFIPV4MULTI_RM_OSPFv3
         redistribute ospfv3 match external route-map VRF_AFIPV4MULTI_RM_OSPFv3
         redistribute ospfv3 match nssa-external 1 route-map VRF_AFIPV4MULTI_RM_OSPFv3
         redistribute ospf match external route-map VRF_AFIPV4MULTI_RM_OSPF
         redistribute ospf match nssa-external 2 route-map VRF_AFIPV4MULTI_RM_OSPF
         redistribute static route-map VRF_AFIPV4MULTI_RM_STATIC
      !
      address-family ipv6
         bgp additional-paths install
         bgp missing-policy direction in action deny-in-out
         bgp missing-policy direction out action deny-in-out
         bgp additional-paths receive
         bgp additional-paths send any
         neighbor aa::1 activate
         neighbor aa::1 additional-paths receive
         neighbor aa::1 route-map FOO in
         neighbor aa::1 route-map BAR out
         neighbor aa::1 additional-paths send any
         neighbor aa::2 activate
         neighbor aa::2 rcf in VRF_AFIPV6_RCF_IN()
         neighbor aa::2 rcf out VRF_AFIPV6_RCF_OUT()
         network aa::/64
         no bgp redistribute-internal
         redistribute connected rcf VRF_AFIPV6_RCF_CONNECTED()
         redistribute isis include leaked
         redistribute ospfv3 match internal include leaked
         redistribute ospfv3 match external
         redistribute ospfv3 match nssa-external
         redistribute static route-map VRF_AFIPV6_RM_STATIC
      !
      address-family ipv6 multicast
         bgp missing-policy direction in action deny
         bgp missing-policy direction out action deny
         bgp additional-paths receive
         neighbor aa::1 additional-paths receive
         network ff08:1::/64
         redistribute connected route-map VRF_AFIPV6MULTI_RM_CONNECTED
         redistribute isis level-1-2 include leaked route-map VRF_AFIPV6MULTI_RM_ISIS
         redistribute ospf route-map VRF_AFIPV6MULTI_RM_OSPF
         redistribute ospfv3 match internal route-map VRF_AFIPV6MULTI_RM_OSPFv3
         redistribute ospfv3 match external route-map VRF_AFIPV6MULTI_RM_OSPFv3
         redistribute ospfv3 match nssa-external 1 route-map VRF_AFIPV6MULTI_RM_OSPFv3
         redistribute ospf match external route-map VRF_AFIPV6MULTI_RM_OSPF
         redistribute ospf match nssa-external 1 route-map VRF_AFIPV6MULTI_RM_OSPF
         redistribute static route-map VRF_AFIPV6MULTI_RM_STATIC
   !
   vrf VRF02
      neighbor 1.1.1.1 additional-paths receive
      neighbor 1.1.1.1 additional-paths send ecmp limit 24
      redistribute connected include leaked route-map RM_VRF_CONNECTED
      redistribute isis level-2 include leaked route-map RM_VRF_ISIS
      redistribute ospf include leaked route-map RM_VRF_OSPF
      redistribute ospfv3 include leaked route-map RM_VRF_OSPFv3
      redistribute ospfv3 match external include leaked route-map RM_VRF_OSPFv3
      redistribute ospfv3 match nssa-external 1 include leaked route-map RM_VRF_OSPFv3
      redistribute static include leaked
      redistribute rip
      redistribute attached-host route-map RM_VRF_HOST
      redistribute dynamic route-map RM_VRF_DYNAMIC
      redistribute bgp leaked route-map RM_VRF_BGP
      redistribute user
      !
      address-family ipv4
         bgp additional-paths send backup
      !
      address-family ipv6
         bgp additional-paths send limit 3
   !
   vrf VRF03
      maximum-paths 10 ecmp 10
      redistribute dynamic rcf VRF_RCF_DYNAMIC()
      !
      address-family ipv4
         bgp additional-paths send ecmp
```
