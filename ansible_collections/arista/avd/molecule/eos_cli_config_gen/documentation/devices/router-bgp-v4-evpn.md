# router-bgp-v4-evpn

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

#### Router BGP Peer Groups

##### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Remote AS | 65001 |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 3 |
| Send community | all |
| Maximum routes | 0 (no limit) |

##### EXTENDED-COMMUNITY

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | extended |

##### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65001 |
| Send community | all |
| Maximum routes | 12000 |

##### LARGE-COMMUNITY

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | large |

##### LOCAL-AS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Local AS | 65000 |

##### MLAG-IPv4-UNDERLAY-PEER

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remove Private AS Outbound | True (All) (Replace AS) |
| Remove Private AS Inbound | True (Replace AS) |
| Remote AS | 65101 |
| Next-hop self | True |
| Send community | all |
| Maximum routes | 12000 |

##### MULTIPLE-COMMUNITY

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | standard large |

##### NO-COMMUNITY

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |

##### STARDARD-COMMUNITY

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | standard |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 10.255.251.1 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | default | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |
| 172.31.255.0 | Inherited from peer group IPv4-UNDERLAY-PEERS | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.31.255.2 | Inherited from peer group IPv4-UNDERLAY-PEERS | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 192.168.255.1 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.255.2 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.251.1 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | TENANT_A_PROJECT01 | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |
| 10.2.3.4 | 1234 | TENANT_A_PROJECT01 | - | all | 0 (no limit) | - | - | - | - | - | - |
| 10.255.251.1 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | TENANT_A_PROJECT02 | - | standard | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |
| 10.255.251.2 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | TENANT_A_PROJECT02 | - | extended | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |
| 10.255.251.3 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | TENANT_A_PROJECT02 | - | large | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |
| 10.255.251.4 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | TENANT_A_PROJECT02 | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | True | - | - | - | - |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | Encapsulation |
| ---------- | -------- | ------------ | ------------- | ------------- |
| EVPN-OVERLAY-PEERS | True |  - | - | default |
| IPv4-UNDERLAY-PEERS | False |  - | - | default |
| MLAG-IPv4-UNDERLAY-PEER | False |  - | - | default |

#### Router BGP VLAN Aware Bundles

| VLAN Aware Bundle | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute | VLANs |
| ----------------- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ | ----- |
| B-ELAN-201 | 192.168.255.3:20201 | 20201:20201 | - | - | learned | 201 |
| TENANT_A_PROJECT01 | 192.168.255.3:11 | 11:11 | - | - | learned | 110 |
| TENANT_A_PROJECT02 | 192.168.255.3:12 | 12:12 | - | - | learned | 112 |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| TENANT_A_PROJECT01 | 192.168.255.3:11 | connected<br>static |
| TENANT_A_PROJECT02 | 192.168.255.3:12 | connected<br>static |

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
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS remote-as 65001
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS password 7 <removed>
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor EXTENDED-COMMUNITY peer group
   neighbor EXTENDED-COMMUNITY send-community extended
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS remote-as 65001
   neighbor IPv4-UNDERLAY-PEERS password 7 <removed>
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor LARGE-COMMUNITY peer group
   neighbor LARGE-COMMUNITY send-community large
   neighbor LOCAL-AS peer group
   neighbor LOCAL-AS local-as 65000 no-prepend replace-as
   neighbor MLAG-IPv4-UNDERLAY-PEER peer group
   neighbor MLAG-IPv4-UNDERLAY-PEER remote-as 65101
   neighbor MLAG-IPv4-UNDERLAY-PEER next-hop-self
   neighbor MLAG-IPv4-UNDERLAY-PEER remove-private-as all replace-as
   neighbor MLAG-IPv4-UNDERLAY-PEER route-map RM-MLAG-PEER-IN in
   neighbor MLAG-IPv4-UNDERLAY-PEER route-map RM-MLAG-PEER-OUT out
   neighbor MLAG-IPv4-UNDERLAY-PEER password 7 <removed>
   neighbor MLAG-IPv4-UNDERLAY-PEER send-community
   neighbor MLAG-IPv4-UNDERLAY-PEER maximum-routes 12000
   neighbor MLAG-IPv4-UNDERLAY-PEER remove-private-as ingress replace-as
   neighbor MULTIPLE-COMMUNITY peer group
   neighbor MULTIPLE-COMMUNITY send-community standard large
   neighbor NO-COMMUNITY peer group
   neighbor STARDARD-COMMUNITY peer group
   neighbor STARDARD-COMMUNITY send-community standard
   neighbor 10.255.251.1 peer group MLAG-IPv4-UNDERLAY-PEER
   neighbor 172.31.255.0 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.31.255.0 password 7 <removed>
   neighbor 172.31.255.2 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.255.1 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.2 peer group EVPN-OVERLAY-PEERS
   redistribute connected route-map RM-CONN-2-BGP
   redistribute isis level-2 include leaked rcf RCF-CONN-2-BGP()
   redistribute ospfv3 match internal include leaked route-map RM-CONN-2-BGP
   redistribute ospfv3 match nssa-external include leaked route-map RM-CONN-2-BGP
   redistribute dynamic rcf RCF-CONN-2-BGP()
   !
   vlan-aware-bundle B-ELAN-201
      rd 192.168.255.3:20201
      route-target both 20201:20201
      redistribute learned
      vlan 201
   !
   vlan-aware-bundle TENANT_A_PROJECT01
      rd 192.168.255.3:11
      route-target both 11:11
      redistribute learned
      vlan 110
   !
   vlan-aware-bundle TENANT_A_PROJECT02
      rd 192.168.255.3:12
      route-target both 12:12
      redistribute learned
      vlan 112
   !
   address-family evpn
      bgp additional-paths send backup
      neighbor EVPN-OVERLAY-PEERS activate
      no neighbor IPv4-UNDERLAY-PEERS activate
      no neighbor MLAG-IPv4-UNDERLAY-PEER activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
      neighbor MLAG-IPv4-UNDERLAY-PEER activate
      neighbor TEST_PEER_GRP activate
      neighbor TEST_PEER_GRP next-hop address-family ipv6 originate
      redistribute isis level-1 include leaked rcf Address_Family_IPV4_ISIS()
      redistribute ospf match internal include leaked route-map RM_BGP_EVPN_IPV4
      redistribute ospfv3 match internal include leaked route-map RM_BGP_EVPN_IPV4
   !
   address-family ipv4 multicast
      redistribute attached-host route-map AFIPV4M_ATTACHED_HOST
      redistribute connected route-map AFIPV4M_CONNECTED
      redistribute isis level-1-2 include leaked route-map AFIPV4M_ISIS
      redistribute ospf match internal route-map AFIPV4M_OSPF_INTERNAL
      redistribute ospfv3 route-map AFIPV4M_OSPFV3
      redistribute ospf match external route-map AFIPV4M_OSPF_EXTERNAL
      redistribute ospf match nssa-external route-map AFIPV4M_OSPF_NSSA
      redistribute static route-map AFIPV4M_STATIC
   !
   address-family ipv6
      redistribute bgp leaked route-map RM-REDISTRIBUTE-BGP
      redistribute connected include leaked rcf Address_Family_IPV6_Connected()
      redistribute dynamic route-map RM-REDISTRIBUTE-DYNAMIC
      redistribute isis level-1-2 rcf RCF_Address_Family_IPV6_ISIS()
      redistribute ospfv3 match internal include leaked route-map RM-REDISTRIBUTE-OSPF-INTERNAL
      redistribute ospfv3 match external include leaked
      redistribute ospfv3 match nssa-external 1 include leaked route-map RM-REDISTRIBUTE-OSPF-NSSA-EXTERNAL
      redistribute static route-map RM-IPV6-STATIC-TO-BGP
   !
   address-family ipv6 multicast
      redistribute connected route-map RM-address_family_ipv6_multicast-Connected
      redistribute isis include leaked route-map RM-address_family_ipv6_multicast-ISIS
      redistribute ospf route-map RM-address_family_ipv6_multicast-OSPF
      redistribute ospfv3 route-map RM-address_family_ipv6_multicast-OSPFv3
      redistribute ospfv3 match external route-map RM-address_family_ipv6_multicast-OSPFv3-External
      redistribute ospfv3 match nssa-external 2 route-map RM-address_family_ipv6_multicast-OSPFv3-External
      redistribute ospf match external route-map RM-address_family_ipv6_multicast-OSPF-External
      redistribute ospf match nssa-external 2 route-map RM-address_family_ipv6_multicast-OSPF-External
      redistribute static route-map RM-address_family_ipv6_multicast-Static
   !
   vrf TENANT_A_PROJECT01
      rd 192.168.255.3:11
      route-target import evpn 11:11
      route-target export evpn 11:11
      router-id 192.168.255.3
      update wait-for-convergence
      update wait-install
      neighbor 10.2.3.4 remote-as 1234
      neighbor 10.2.3.4 remove-private-as all
      neighbor 10.2.3.4 local-as 123 no-prepend replace-as
      neighbor 10.2.3.4 description Tenant A BGP Peer
      neighbor 10.2.3.4 ebgp-multihop 3
      neighbor 10.2.3.4 route-map RM-10.2.3.4-SET-NEXT-HOP-OUT out
      neighbor 10.2.3.4 default-originate route-map RM-10.2.3.4-SET-NEXT-HOP-OUT always
      neighbor 10.2.3.4 send-community
      neighbor 10.2.3.4 maximum-routes 0
      neighbor 10.255.251.1 peer group MLAG-IPv4-UNDERLAY-PEER
      network 10.0.0.0/8
      network 100.64.0.0/10
      redistribute connected
      redistribute static
      !
      address-family ipv4
         bgp additional-paths install
         bgp missing-policy direction in action permit
         bgp missing-policy direction out action deny
         bgp additional-paths receive
         bgp additional-paths send ecmp
         neighbor 10.2.3.4 activate
         neighbor 10.2.3.4 route-map RM-10.2.3.4-SET-NEXT-HOP-OUT out
         neighbor 10.2.3.5 activate
         neighbor 10.2.3.5 route-map RM-10.2.3.5-SET-NEXT-HOP-IN in
         neighbor 10.2.3.6 next-hop address-family ipv6
         neighbor 10.2.3.7 next-hop address-family ipv6 originate
         no neighbor 10.2.3.8 next-hop address-family ipv6
         neighbor 10.2.3.9 activate
         neighbor 10.2.3.9 rcf in VRF_AFIPV4_RCF_IN()
         neighbor 10.2.3.10 activate
         neighbor 10.2.3.10 rcf out VRF_AFIPV4_RCF_OUT()
         network 10.0.0.0/8
         network 100.64.0.0/10 route-map RM-10.2.3.4
         redistribute connected rcf VRF_AFIPV4_RCF_CONNECTED()
         redistribute static route-map VRF_AFIPV4_RM_STATIC
   !
   vrf TENANT_A_PROJECT02
      rd 192.168.255.3:12
      route-target import evpn 12:12
      route-target export evpn 12:12
      router-id 192.168.255.3
      timers bgp 5 15
      neighbor 10.255.251.1 peer group MLAG-IPv4-UNDERLAY-PEER
      neighbor 10.255.251.1 next-hop-self
      neighbor 10.255.251.1 description ABCDEFG
      neighbor 10.255.251.1 timers 1 3
      neighbor 10.255.251.1 send-community standard
      neighbor 10.255.251.2 peer group MLAG-IPv4-UNDERLAY-PEER
      neighbor 10.255.251.2 description ABCDEFGfg
      neighbor 10.255.251.2 timers 1 3
      neighbor 10.255.251.2 send-community extended
      neighbor 10.255.251.3 peer group MLAG-IPv4-UNDERLAY-PEER
      neighbor 10.255.251.3 next-hop-self
      neighbor 10.255.251.3 description ABCDEFGfgLCLCLCLC
      neighbor 10.255.251.3 timers 1 3
      neighbor 10.255.251.3 default-originate always
      neighbor 10.255.251.3 send-community large
      neighbor 10.255.251.4 peer group MLAG-IPv4-UNDERLAY-PEER
      neighbor 10.255.251.4 bfd
      neighbor 10.255.251.4 description Test_Bfd
      redistribute connected
      redistribute static route-map RM-CONN-2-BGP
```
