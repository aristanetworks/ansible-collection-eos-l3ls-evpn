# pe2

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [Enable Password](#enable-password)
- [Management Security](#management-security)
  - [Management Security Summary](#management-security-summary)
  - [Management Security Device Configuration](#management-security-device-configuration)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Device Configuration](#internal-vlan-allocation-policy-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router OSPF](#router-ospf)
  - [Router ISIS](#router-isis)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [MPLS](#mpls)
  - [MPLS and LDP](#mpls-and-ldp)
  - [MPLS Interfaces](#mpls-interfaces)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | 172.16.1.102/24 | 172.16.1.1 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | OOB_MANAGEMENT | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description OOB_MANAGEMENT
   no shutdown
   vrf MGMT
   ip address 172.16.1.102/24
```

### Management API HTTP

#### Management API HTTP Summary

| HTTP | HTTPS | Default Services |
| ---- | ----- | ---------------- |
| False | True | - |

#### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| MGMT | - | - |

#### Management API HTTP Device Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf MGMT
      no shutdown
```

## Authentication

### Local Users

#### Local Users Summary

| User | Privilege | Role | Disabled | Shell |
| ---- | --------- | ---- | -------- | ----- |
| admin | 15 | network-admin | False | - |
| ansible | 15 | network-admin | False | - |

#### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin nopassword
username ansible privilege 15 role network-admin secret sha512 <removed>
```

### Enable Password

Enable password has been disabled

## Management Security

### Management Security Summary

| Settings | Value |
| -------- | ----- |
| Common password encryption key | True |

### Management Security Device Configuration

```eos
!
management security
   password encryption-key common
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **none**

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode none
```

## Internal VLAN Allocation Policy

### Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

### Internal VLAN Allocation Policy Device Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

##### Encapsulation Dot1q Interfaces

| Interface | Description | Vlan ID | Dot1q VLAN Tag | Dot1q Inner VLAN Tag |
| --------- | ----------- | ------- | -------------- | -------------------- |
| Ethernet4.10 | C1_L3_SERVICE | - | 10 | - |
| Ethernet4.20 | C2_L3_SERVICE | - | 20 | - |

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_p2_Ethernet1 | - | 10.255.3.4/31 | default | 1500 | False | - | - |
| Ethernet2 | P2P_p1_Ethernet2 | - | 10.255.3.6/31 | default | 1500 | False | - | - |
| Ethernet4.10 | C1_L3_SERVICE | - | 10.0.1.2/29 | C1_VRF1 | - | False | - | - |
| Ethernet4.20 | C2_L3_SERVICE | - | 10.1.1.2/29 | C2_VRF1 | - | False | - | - |

##### ISIS

| Interface | Channel Group | ISIS Instance | ISIS BFD | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | ISIS Authentication Mode |
| --------- | ------------- | ------------- | -------- | ----------- | ---- | ----------------- | ------------- | ------------------------ |
| Ethernet1 | - | CORE | - | 50 | point-to-point | level-2 | True | md5 |
| Ethernet2 | - | CORE | - | 50 | point-to-point | level-2 | True | md5 |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_p2_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ip address 10.255.3.4/31
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
   isis enable CORE
   isis circuit-type level-2
   isis metric 50
   isis hello padding
   isis network point-to-point
   isis authentication mode md5
   isis authentication key 7 <removed>
!
interface Ethernet2
   description P2P_p1_Ethernet2
   no shutdown
   mtu 1500
   no switchport
   ip address 10.255.3.6/31
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
   isis enable CORE
   isis circuit-type level-2
   isis metric 50
   isis hello padding
   isis network point-to-point
   isis authentication mode md5
   isis authentication key 7 <removed>
!
interface Ethernet4
   no shutdown
   no switchport
!
interface Ethernet4.10
   description C1_L3_SERVICE
   no shutdown
   encapsulation dot1q vlan 10
   vrf C1_VRF1
   ip address 10.0.1.2/29
   ip ospf area 0.0.0.0
!
interface Ethernet4.20
   description C2_L3_SERVICE
   no shutdown
   encapsulation dot1q vlan 20
   vrf C2_VRF1
   ip address 10.1.1.2/29
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | ROUTER_ID | default | 10.255.1.2/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | ROUTER_ID | default | - |

##### ISIS

| Interface | ISIS instance | ISIS metric | Interface mode |
| --------- | ------------- | ----------- | -------------- |
| Loopback0 | CORE | - | passive |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description ROUTER_ID
   no shutdown
   ip address 10.255.1.2/32
   mpls ldp interface
   isis enable CORE
   isis passive
```

## Routing

### Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

### Virtual Router MAC Address

#### Virtual Router MAC Address Summary

Virtual Router MAC Address: 00:1c:73:00:dc:00

#### Virtual Router MAC Address Device Configuration

```eos
!
ip virtual-router mac-address 00:1c:73:00:dc:00
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| C1_VRF1 | True |
| C2_VRF1 | True |
| MGMT | False |

#### IP Routing Device Configuration

```eos
!
ip routing
ip routing vrf C1_VRF1
ip routing vrf C2_VRF1
no ip routing vrf MGMT
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| C1_VRF1 | false |
| C2_VRF1 | false |
| MGMT | false |

### Static Routes

#### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP | Exit interface | Administrative Distance | Tag | Route Name | Metric |
| --- | ------------------ | ----------- | -------------- | ----------------------- | --- | ---------- | ------ |
| MGMT | 0.0.0.0/0 | 172.16.1.1 | - | 1 | - | - | - |

#### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 172.16.1.1
```

### Router OSPF

#### Router OSPF Summary

| Process ID | Router ID | Default Passive Interface | No Passive Interface | BFD | Max LSA | Default Information Originate | Log Adjacency Changes Detail | Auto Cost Reference Bandwidth | Maximum Paths | MPLS LDP Sync Default | Distribute List In |
| ---------- | --------- | ------------------------- | -------------------- | --- | ------- | ----------------------------- | ---------------------------- | ----------------------------- | ------------- | --------------------- | ------------------ |
| 10 | 10.255.1.2 | enabled | Ethernet4.10 <br> | disabled | default | disabled | disabled | - | - | - | - |

#### Router OSPF Router Redistribution

| Process ID | Source Protocol | Include Leaked | Route Map |
| ---------- | --------------- | -------------- | --------- |
| 10 | bgp | disabled | - |

#### OSPF Interfaces

| Interface | Area | Cost | Point To Point |
| -------- | -------- | -------- | -------- |
| Ethernet4.10 | 0.0.0.0 | - | False |

#### Router OSPF Device Configuration

```eos
!
router ospf 10 vrf C1_VRF1
   router-id 10.255.1.2
   passive-interface default
   no passive-interface Ethernet4.10
   redistribute bgp
```

### Router ISIS

#### Router ISIS Summary

| Settings | Value |
| -------- | ----- |
| Instance | CORE |
| Net-ID | 49.0001.0102.5500.1002.00 |
| Type | level-2 |
| Router-ID | 10.255.1.2 |
| Log Adjacency Changes | True |
| MPLS LDP Sync Default | True |

#### ISIS Interfaces Summary

| Interface | ISIS Instance | ISIS Metric | Interface Mode |
| --------- | ------------- | ----------- | -------------- |
| Ethernet1 | CORE | 50 | point-to-point |
| Ethernet2 | CORE | 50 | point-to-point |
| Loopback0 | CORE | - | passive |

#### ISIS IPv4 Address Family Summary

| Settings | Value |
| -------- | ----- |
| IPv4 Address-family Enabled | True |
| Maximum-paths | 4 |

#### Router ISIS Device Configuration

```eos
!
router isis CORE
   net 49.0001.0102.5500.1002.00
   router-id ipv4 10.255.1.2
   is-type level-2
   log-adjacency-changes
   mpls ldp sync default
   !
   address-family ipv4 unicast
      maximum-paths 4
   !
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65001 | 10.255.1.2 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| maximum-paths 4 ecmp 4 |

#### Router BGP Peer Groups

##### MPLS-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | mpls |
| Remote AS | 65001 |
| Source | Loopback0 |
| BFD | True |
| Send community | all |
| Maximum routes | 0 (no limit) |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 10.255.2.1 | Inherited from peer group MPLS-OVERLAY-PEERS | default | - | Inherited from peer group MPLS-OVERLAY-PEERS | Inherited from peer group MPLS-OVERLAY-PEERS | - | Inherited from peer group MPLS-OVERLAY-PEERS | - | - | - | - |
| 10.255.2.2 | Inherited from peer group MPLS-OVERLAY-PEERS | default | - | Inherited from peer group MPLS-OVERLAY-PEERS | Inherited from peer group MPLS-OVERLAY-PEERS | - | Inherited from peer group MPLS-OVERLAY-PEERS | - | - | - | - |
| 10.1.1.3 | 65123 | C2_VRF1 | - | standard | 100 | - | - | - | - | - | - |

#### Router BGP VPN-IPv4 Address Family

##### VPN-IPv4 Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | RCF In | RCF Out |
| ---------- | -------- | ------------ | ------------- | ------ | ------- |
| MPLS-OVERLAY-PEERS | True | - | - | - | - |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| C1_VRF1 | 10.255.1.2:10 | connected<br>ospf |
| C2_VRF1 | 10.255.1.2:20 | connected |

#### Router BGP Device Configuration

```eos
!
router bgp 65001
   router-id 10.255.1.2
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   maximum-paths 4 ecmp 4
   neighbor MPLS-OVERLAY-PEERS peer group
   neighbor MPLS-OVERLAY-PEERS remote-as 65001
   neighbor MPLS-OVERLAY-PEERS update-source Loopback0
   neighbor MPLS-OVERLAY-PEERS bfd
   neighbor MPLS-OVERLAY-PEERS password 7 <removed>
   neighbor MPLS-OVERLAY-PEERS send-community
   neighbor MPLS-OVERLAY-PEERS maximum-routes 0
   neighbor 10.255.2.1 peer group MPLS-OVERLAY-PEERS
   neighbor 10.255.2.1 description rr1_Loopback0
   neighbor 10.255.2.2 peer group MPLS-OVERLAY-PEERS
   neighbor 10.255.2.2 description rr2_Loopback0
   !
   address-family ipv4
      no neighbor MPLS-OVERLAY-PEERS activate
   !
   address-family vpn-ipv4
      neighbor MPLS-OVERLAY-PEERS activate
      neighbor default encapsulation mpls next-hop-self source-interface Loopback0
   !
   vrf C1_VRF1
      rd 10.255.1.2:10
      route-target import vpn-ipv4 10:10
      route-target export vpn-ipv4 10:10
      router-id 10.255.1.2
      redistribute connected
      redistribute ospf
   !
   vrf C2_VRF1
      rd 10.255.1.2:20
      route-target import vpn-ipv4 20:20
      route-target export vpn-ipv4 20:20
      router-id 10.255.1.2
      neighbor 10.1.1.3 remote-as 65123
      neighbor 10.1.1.3 description C2_ROUTER1
      neighbor 10.1.1.3 send-community standard
      neighbor 10.1.1.3 maximum-routes 100
      redistribute connected
      !
      address-family ipv4
         neighbor 10.1.1.3 activate
```

## BFD

### Router BFD

#### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 300 | 300 | 3 |

#### Router BFD Device Configuration

```eos
!
router bfd
   multihop interval 300 min-rx 300 multiplier 3
```

## MPLS

### MPLS and LDP

#### MPLS and LDP Summary

| Setting | Value |
| -------- | ---- |
| MPLS IP Enabled | True |
| LDP Enabled | True |
| LDP Router ID | 10.255.1.2 |
| LDP Interface Disabled Default | True |
| LDP Transport-Address Interface | Loopback0 |

#### MPLS and LDP Device Configuration

```eos
!
mpls ip
!
mpls ldp
   router-id 10.255.1.2
   transport-address interface Loopback0
   interface disabled default
   no shutdown
```

### MPLS Interfaces

| Interface | MPLS IP Enabled | LDP Enabled | IGP Sync |
| --------- | --------------- | ----------- | -------- |
| Ethernet1 | True | True | True |
| Ethernet2 | True | True | True |
| Loopback0 | - | True | - |

## Multicast

### IP IGMP Snooping

#### IP IGMP Snooping Summary

| IGMP Snooping | Fast Leave | Interface Restart Query | Proxy | Restart Query Interval | Robustness Variable |
| ------------- | ---------- | ----------------------- | ----- | ---------------------- | ------------------- |
| Enabled | - | - | - | - | - |

#### IP IGMP Snooping Device Configuration

```eos
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| C1_VRF1 | enabled |
| C2_VRF1 | enabled |
| MGMT | disabled |

### VRF Instances Device Configuration

```eos
!
vrf instance C1_VRF1
!
vrf instance C2_VRF1
!
vrf instance MGMT
```
