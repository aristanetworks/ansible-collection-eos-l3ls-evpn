# router-bgp-vpn-ipv4-vpn-ipv6

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
| 65103 | 192.168.255.3 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| maximum-paths 2 ecmp 2 |

#### Router BGP Peer Groups

##### MPLS-IBGP-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | vpn-ipv4, vpn-ipv6 |
| Remote AS | 65000 |
| Local AS | 65000 |
| Send community | all |
| Maximum routes | 0 (no limit) |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 192.168.255.1 | Inherited from peer group MPLS-IBGP-PEERS | default | - | Inherited from peer group MPLS-IBGP-PEERS | Inherited from peer group MPLS-IBGP-PEERS | - | - | - | - | - | - |
| 192.168.255.2 | Inherited from peer group MPLS-IBGP-PEERS | default | - | Inherited from peer group MPLS-IBGP-PEERS | Inherited from peer group MPLS-IBGP-PEERS | - | - | - | - | - | - |
| 192.168.255.4 | 65004 | default | - | all | - | - | - | - | - | - | - |
| 2001:cafe:192:168::4 | 65004 | default | - | all | - | - | - | - | - | - | - |

#### Router BGP VPN-IPv4 Address Family

- VPN import pruning is **enabled**

##### VPN-IPv4 Neighbors

| Neighbor | Activate | Route-map In | Route-map Out | RCF In | RCF Out |
| -------- | -------- | ------------ | ------------- | ------ | ------- |
| 192.168.255.4 | True | RM-NEIGHBOR-PEER-IN4 | RM-NEIGHBOR-PEER-OUT4 | - | - |
| 192.168.255.5 | False | - | - | Address_Family_VPN_IPV4_In() | Address_Family_VPN_IPV4_Out() |

##### VPN-IPv4 Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | RCF In | RCF Out |
| ---------- | -------- | ------------ | ------------- | ------ | ------- |
| MPLS-IBGP-PEERS | True | RM-IBGP-PEER-IN4 | RM-IBGP-PEER-OUT4 | - | - |
| Test_RCF | False | - | - | Address_Family_VPN_IPV4_In() | Address_Family_VPN_IPV4_Out() |

#### Router BGP VPN-IPv6 Address Family

- VPN import pruning is **enabled**

##### VPN-IPv6 Neighbors

| Neighbor | Activate | Route-map In | Route-map Out | RCF In | RCF Out |
| -------- | -------- | ------------ | ------------- | ------ | ------- |
| 2001:cafe:192:168::4 | True | RM-NEIGHBOR-PEER-IN6 | RM-NEIGHBOR-PEER-OUT6 | - | - |
| 2001:cafe:192:168::5 | False | - | - | Address_Family_VPN_IPV6_In() | Address_Family_VPN_IPV6_Out() |

##### VPN-IPv6 Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | RCF In | RCF Out |
| ---------- | -------- | ------------ | ------------- | ------ | ------- |
| MPLS-IBGP-PEERS | True | RM-IBGP-PEER-IN6 | RM-IBGP-PEER-OUT6 | - | - |
| Test_RCF | False | - | - | Address_Family_VPN_IPV6_In() | Address_Family_VPN_IPV6_Out() |

#### Router BGP Device Configuration

```eos
!
router bgp 65103
   router-id 192.168.255.3
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 2 ecmp 2
   neighbor MPLS-IBGP-PEERS peer group
   neighbor MPLS-IBGP-PEERS remote-as 65000
   neighbor MPLS-IBGP-PEERS local-as 65000 no-prepend replace-as
   neighbor MPLS-IBGP-PEERS password 7 <removed>
   neighbor MPLS-IBGP-PEERS send-community
   neighbor MPLS-IBGP-PEERS maximum-routes 0
   neighbor 192.168.255.1 peer group MPLS-IBGP-PEERS
   neighbor 192.168.255.2 peer group MPLS-IBGP-PEERS
   neighbor 192.168.255.4 remote-as 65004
   neighbor 192.168.255.4 send-community
   neighbor 2001:cafe:192:168::4 remote-as 65004
   neighbor 2001:cafe:192:168::4 send-community
   !
   address-family vpn-ipv4
      neighbor MPLS-IBGP-PEERS activate
      neighbor MPLS-IBGP-PEERS route-map RM-IBGP-PEER-IN4 in
      neighbor MPLS-IBGP-PEERS route-map RM-IBGP-PEER-OUT4 out
      neighbor Test_RCF rcf in Address_Family_VPN_IPV4_In()
      neighbor Test_RCF rcf out Address_Family_VPN_IPV4_Out()
      neighbor 192.168.255.4 activate
      neighbor 192.168.255.4 route-map RM-NEIGHBOR-PEER-IN4 in
      neighbor 192.168.255.4 route-map RM-NEIGHBOR-PEER-OUT4 out
      neighbor 192.168.255.5 rcf in Address_Family_VPN_IPV4_In()
      neighbor 192.168.255.5 rcf out Address_Family_VPN_IPV4_Out()
      neighbor default encapsulation mpls next-hop-self source-interface Loopback0
      domain identifier 65000:0
      route import match-failure action discard
   !
   address-family vpn-ipv6
      neighbor MPLS-IBGP-PEERS activate
      neighbor MPLS-IBGP-PEERS route-map RM-IBGP-PEER-IN6 in
      neighbor MPLS-IBGP-PEERS route-map RM-IBGP-PEER-OUT6 out
      neighbor Test_RCF rcf in Address_Family_VPN_IPV6_In()
      neighbor Test_RCF rcf out Address_Family_VPN_IPV6_Out()
      neighbor 2001:cafe:192:168::4 activate
      neighbor 2001:cafe:192:168::4 route-map RM-NEIGHBOR-PEER-IN6 in
      neighbor 2001:cafe:192:168::4 route-map RM-NEIGHBOR-PEER-OUT6 out
      neighbor 2001:cafe:192:168::5 rcf in Address_Family_VPN_IPV6_In()
      neighbor 2001:cafe:192:168::5 rcf out Address_Family_VPN_IPV6_Out()
      neighbor default encapsulation mpls next-hop-self source-interface Loopback0
      domain identifier 65000:0
      route import match-failure action discard
```
