# router-bgp-v4-v6-evpn

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
| 65100 | 10.50.64.15 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| update wait-install |
| distance bgp 20 200 200 |
| maximum-paths 4 ecmp 4 |

#### Router BGP Peer Groups

##### EVPN-OVERLAY

| Settings | Value |
| -------- | ----- |
| Remote AS | 65000 |
| Next-hop unchanged | True |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 5 |
| Send community | all |
| Maximum routes | 0 (no limit) |

##### IPV4-UNDERLAY

| Settings | Value |
| -------- | ----- |
| Remote AS | 65000 |
| Send community | all |
| Maximum routes | 12000 |

##### IPV4-UNDERLAY-MLAG

| Settings | Value |
| -------- | ----- |
| Remote AS | 65100 |
| Next-hop self | True |
| Send community | all |
| Maximum routes | 12000 |

##### IPV6-UNDERLAY

| Settings | Value |
| -------- | ----- |
| Remote AS | 65000 |
| Send community | all |
| Maximum routes | 12000 |

##### IPV6-UNDERLAY-MLAG

| Settings | Value |
| -------- | ----- |
| Remote AS | 65100 |
| Next-hop self | True |
| Send community | all |
| Maximum routes | 12000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 1.1.1.1 | 1 | default | False | - | - | - | - | - | - | - | - |
| 1b11:3a00:22b0:0088::1 | Inherited from peer group IPV6-UNDERLAY | default | - | Inherited from peer group IPV6-UNDERLAY | Inherited from peer group IPV6-UNDERLAY | - | - | - | - | - | - |
| 1b11:3a00:22b0:0088::3 | Inherited from peer group IPV6-UNDERLAY | default | - | Inherited from peer group IPV6-UNDERLAY | Inherited from peer group IPV6-UNDERLAY | - | - | - | - | - | - |
| 1b11:3a00:22b0:0088::5 | Inherited from peer group IPV6-UNDERLAY | default | - | Inherited from peer group IPV6-UNDERLAY | Inherited from peer group IPV6-UNDERLAY | - | - | - | - | - | - |
| 10.50.2.1 | Inherited from peer group IPV4-UNDERLAY | default | - | Inherited from peer group IPV4-UNDERLAY | Inherited from peer group IPV4-UNDERLAY | - | - | - | - | - | - |
| 10.50.2.3 | Inherited from peer group IPV4-UNDERLAY | default | - | Inherited from peer group IPV4-UNDERLAY | Inherited from peer group IPV4-UNDERLAY | - | - | - | - | - | - |
| 10.50.2.5 | Inherited from peer group IPV4-UNDERLAY | default | - | Inherited from peer group IPV4-UNDERLAY | Inherited from peer group IPV4-UNDERLAY | - | - | - | - | - | - |
| 10.50.64.11 | Inherited from peer group EVPN-OVERLAY | default | - | Inherited from peer group EVPN-OVERLAY | Inherited from peer group EVPN-OVERLAY | - | Inherited from peer group EVPN-OVERLAY | - | - | - | - |
| 10.50.64.12 | Inherited from peer group EVPN-OVERLAY | default | - | Inherited from peer group EVPN-OVERLAY | Inherited from peer group EVPN-OVERLAY | - | Inherited from peer group EVPN-OVERLAY | - | - | - | - |
| 10.50.64.13 | Inherited from peer group EVPN-OVERLAY | default | - | Inherited from peer group EVPN-OVERLAY | Inherited from peer group EVPN-OVERLAY | - | Inherited from peer group EVPN-OVERLAY | - | - | - | - |
| 169.254.252.1 | Inherited from peer group IPV4-UNDERLAY-MLAG | default | - | Inherited from peer group IPV4-UNDERLAY-MLAG | Inherited from peer group IPV4-UNDERLAY-MLAG | - | - | - | - | - | - |
| fe80::b%Vl4094 | Inherited from peer group IPV6-UNDERLAY-MLAG | default | - | Inherited from peer group IPV6-UNDERLAY-MLAG | Inherited from peer group IPV6-UNDERLAY-MLAG | - | - | - | - | - | - |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | Encapsulation |
| ---------- | -------- | ------------ | ------------- | ------------- |
| EVPN-OVERLAY | True |  RM-HIDE-AS-PATH | RM-HIDE-AS-PATH | default |
| RCF_TEST | False |  - | - | default |

#### Router BGP VLANs

| VLAN | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute |
| ---- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ |
| 24 | 10.50.64.15:10024 | 1:10024 | - | - | learned |
| 41 | 10.50.64.15:10041 | 1:10041 | - | - | learned |
| 42 | 10.50.64.15:10042 | 1:10042 | - | - | learned |
| 65 | 10.50.64.15:10065 | 1:10065 | - | - | learned |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Tenant_A | 10.50.64.15:30001 | ospf<br>ospfv3<br>connected |
| Tenant_B | 10.50.64.15:30002 | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65100
   router-id 10.50.64.15
   no bgp default ipv4-unicast
   update wait-install
   distance bgp 20 200 200
   maximum-paths 4 ecmp 4
   neighbor EVPN-OVERLAY peer group
   neighbor EVPN-OVERLAY remote-as 65000
   neighbor EVPN-OVERLAY next-hop-unchanged
   neighbor EVPN-OVERLAY update-source Loopback0
   neighbor EVPN-OVERLAY bfd
   neighbor EVPN-OVERLAY ebgp-multihop 5
   neighbor EVPN-OVERLAY password 7 <removed>
   neighbor EVPN-OVERLAY send-community
   neighbor EVPN-OVERLAY maximum-routes 0
   neighbor IPV4-UNDERLAY peer group
   neighbor IPV4-UNDERLAY remote-as 65000
   neighbor IPV4-UNDERLAY password 7 <removed>
   neighbor IPV4-UNDERLAY send-community
   neighbor IPV4-UNDERLAY maximum-routes 12000
   neighbor IPV4-UNDERLAY-MLAG peer group
   neighbor IPV4-UNDERLAY-MLAG remote-as 65100
   neighbor IPV4-UNDERLAY-MLAG next-hop-self
   neighbor IPV4-UNDERLAY-MLAG password 7 <removed>
   neighbor IPV4-UNDERLAY-MLAG send-community
   neighbor IPV4-UNDERLAY-MLAG maximum-routes 12000
   neighbor IPV6-UNDERLAY peer group
   neighbor IPV6-UNDERLAY remote-as 65000
   neighbor IPV6-UNDERLAY password 7 <removed>
   neighbor IPV6-UNDERLAY send-community
   neighbor IPV6-UNDERLAY maximum-routes 12000
   neighbor IPV6-UNDERLAY-MLAG peer group
   neighbor IPV6-UNDERLAY-MLAG remote-as 65100
   neighbor IPV6-UNDERLAY-MLAG next-hop-self
   neighbor IPV6-UNDERLAY-MLAG password 7 <removed>
   neighbor IPV6-UNDERLAY-MLAG send-community
   neighbor IPV6-UNDERLAY-MLAG maximum-routes 12000
   neighbor 1.1.1.1 remote-as 1
   neighbor 1.1.1.1 description TEST
   neighbor 1b11:3a00:22b0:0088::1 peer group IPV6-UNDERLAY
   neighbor 1b11:3a00:22b0:0088::3 peer group IPV6-UNDERLAY
   neighbor 1b11:3a00:22b0:0088::5 peer group IPV6-UNDERLAY
   neighbor 10.50.2.1 peer group IPV4-UNDERLAY
   neighbor 10.50.2.3 peer group IPV4-UNDERLAY
   neighbor 10.50.2.5 peer group IPV4-UNDERLAY
   neighbor 10.50.64.11 peer group EVPN-OVERLAY
   neighbor 10.50.64.12 peer group EVPN-OVERLAY
   neighbor 10.50.64.13 peer group EVPN-OVERLAY
   neighbor 169.254.252.1 peer group IPV4-UNDERLAY-MLAG
   neighbor fe80::b%Vl4094 peer group IPV6-UNDERLAY-MLAG
   redistribute connected route-map RM-CONN-2-BGP
   redistribute static route-map RM-STATIC-2-BGP
   !
   vlan 24
      rd 10.50.64.15:10024
      route-target both 1:10024
      redistribute learned
   !
   vlan 41
      rd 10.50.64.15:10041
      route-target both 1:10041
      redistribute learned
   !
   vlan 42
      rd 10.50.64.15:10042
      route-target both 1:10042
      redistribute learned
   !
   vlan 65
      rd 10.50.64.15:10065
      route-target both 1:10065
      redistribute learned
   !
   address-family evpn
      neighbor EVPN-OVERLAY activate
      neighbor EVPN-OVERLAY route-map RM-HIDE-AS-PATH in
      neighbor EVPN-OVERLAY route-map RM-HIDE-AS-PATH out
      neighbor RCF_TEST rcf in Address_Family_EVPN_In()
      neighbor RCF_TEST rcf out Address_Family_EVPN_Out()
   !
   address-family ipv4
      neighbor IPV4-UNDERLAY activate
      neighbor IPV4-UNDERLAY route-map RM-HIDE-AS-PATH in
      neighbor IPV4-UNDERLAY route-map RM-HIDE-AS-PATH out
      neighbor IPV4-UNDERLAY-MLAG activate
      neighbor TEST_RCF rcf in Address_Family_IPV4_In()
      neighbor TEST_RCF rcf out Address_Family_IPV4_Out()
   !
   address-family ipv4 multicast
      neighbor IPV4-UNDERLAY activate
      neighbor IPV4-UNDERLAY-MLAG activate
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
      neighbor IPV6-UNDERLAY activate
      neighbor IPV6-UNDERLAY route-map RM-HIDE-AS-PATH in
      neighbor IPV6-UNDERLAY route-map RM-HIDE-AS-PATH out
      neighbor IPV6-UNDERLAY-MLAG activate
      neighbor TEST_RCF rcf in Address_Family_IPV6_In()
      neighbor TEST_RCF rcf out Address_Family_IPV6_Out()
      redistribute attached-host route-map RM-Address_Family_IPV6_Attached-Host
      redistribute bgp leaked
      redistribute dhcp route-map RM-Address_Family_IPV6_DHCP
      redistribute connected route-map RM-Address_Family_IPV6_Connected
      redistribute dynamic rcf RCF_Address_Family_IPV6_Dynamic()
      redistribute user rcf RCF_Address_Family_IPV6_User()
      redistribute isis include leaked route-map RM-Address_Family_IPV6_ISIS
      redistribute ospfv3 include leaked route-map RM-REDISTRIBUTE-OSPFV3
      redistribute ospfv3 match external include leaked route-map RM-REDISTRIBUTE-OSPFV3-EXTERNAL
      redistribute static include leaked rcf RCF_IPV6_STATIC_TO_BGP{}
   !
   vrf Tenant_A
      rd 10.50.64.15:30001
      route-target import evpn 1:30001
      route-target import evpn route-map RM-DENY-DEFAULT
      route-target import vpn-ipv4 1:30011
      route-target import vpn-ipv4 rcf RT_IMPORT_AF_RCF() vpn-route filter-rcf RT_IMPORT_AF_RCF_FILTER()
      route-target import vpn-ipv4 route-map RT_IMPORT_AF_RM
      route-target export evpn 1:30001
      route-target export evpn rcf RT_EXPORT_AF_RCF()
      redistribute connected
      redistribute ospf match external include leaked
      redistribute ospfv3
      redistribute ospfv3 match nssa-external
   !
   vrf Tenant_B
      rd 10.50.64.15:30002
      route-target import evpn 1:30002
      route-target export evpn 1:30002
      route-target export evpn route-map RM-DEFAULT-EXTRA-COMM
```
