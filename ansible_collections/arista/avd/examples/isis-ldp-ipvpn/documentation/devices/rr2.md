# rr2

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
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router ISIS](#router-isis)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [MPLS](#mpls)
  - [MPLS and LDP](#mpls-and-ldp)
  - [MPLS Interfaces](#mpls-interfaces)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | 172.16.1.152/24 | 172.16.1.1 |

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
   ip address 172.16.1.152/24
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

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet2 | P2P_p4_Ethernet2 | - | 10.255.3.18/31 | default | 1500 | False | - | - |
| Ethernet3 | P2P_p2_Ethernet3 | - | 10.255.3.16/31 | default | 1500 | False | - | - |
| Ethernet4 | P2P_rr1_Ethernet4 | - | 10.255.3.15/31 | default | 1500 | False | - | - |

##### ISIS

| Interface | Channel Group | ISIS Instance | ISIS BFD | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | ISIS Authentication Mode |
| --------- | ------------- | ------------- | -------- | ----------- | ---- | ----------------- | ------------- | ------------------------ |
| Ethernet2 | - | CORE | - | 50 | point-to-point | level-2 | True | md5 |
| Ethernet3 | - | CORE | - | 50 | point-to-point | level-2 | True | md5 |
| Ethernet4 | - | CORE | - | 50 | point-to-point | level-2 | True | md5 |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet2
   description P2P_p4_Ethernet2
   no shutdown
   mtu 1500
   no switchport
   ip address 10.255.3.18/31
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
interface Ethernet3
   description P2P_p2_Ethernet3
   no shutdown
   mtu 1500
   no switchport
   ip address 10.255.3.16/31
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
   description P2P_rr1_Ethernet4
   no shutdown
   mtu 1500
   no switchport
   ip address 10.255.3.15/31
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
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | ROUTER_ID | default | 10.255.2.2/32 |

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
   ip address 10.255.2.2/32
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

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| MGMT | False |

#### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
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

### Router ISIS

#### Router ISIS Summary

| Settings | Value |
| -------- | ----- |
| Instance | CORE |
| Net-ID | 49.0001.0102.5500.2002.00 |
| Type | level-2 |
| Router-ID | 10.255.2.2 |
| Log Adjacency Changes | True |
| MPLS LDP Sync Default | True |

#### ISIS Interfaces Summary

| Interface | ISIS Instance | ISIS Metric | Interface Mode |
| --------- | ------------- | ----------- | -------------- |
| Ethernet2 | CORE | 50 | point-to-point |
| Ethernet3 | CORE | 50 | point-to-point |
| Ethernet4 | CORE | 50 | point-to-point |
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
   net 49.0001.0102.5500.2002.00
   router-id ipv4 10.255.2.2
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
| 65001 | 10.255.2.2 |

| BGP AS | Cluster ID |
| ------ | --------- |
| 65001 | 10.255.2.2 |

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
| Route Reflector Client | Yes |
| Source | Loopback0 |
| BFD | True |
| Send community | all |
| Maximum routes | 0 (no limit) |

##### RR-OVERLAY-PEERS

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
| 10.255.1.1 | Inherited from peer group MPLS-OVERLAY-PEERS | default | - | Inherited from peer group MPLS-OVERLAY-PEERS | Inherited from peer group MPLS-OVERLAY-PEERS | - | Inherited from peer group MPLS-OVERLAY-PEERS | - | Inherited from peer group MPLS-OVERLAY-PEERS | - | - |
| 10.255.1.2 | Inherited from peer group MPLS-OVERLAY-PEERS | default | - | Inherited from peer group MPLS-OVERLAY-PEERS | Inherited from peer group MPLS-OVERLAY-PEERS | - | Inherited from peer group MPLS-OVERLAY-PEERS | - | Inherited from peer group MPLS-OVERLAY-PEERS | - | - |
| 10.255.1.3 | Inherited from peer group MPLS-OVERLAY-PEERS | default | - | Inherited from peer group MPLS-OVERLAY-PEERS | Inherited from peer group MPLS-OVERLAY-PEERS | - | Inherited from peer group MPLS-OVERLAY-PEERS | - | Inherited from peer group MPLS-OVERLAY-PEERS | - | - |
| 10.255.2.1 | Inherited from peer group RR-OVERLAY-PEERS | default | - | Inherited from peer group RR-OVERLAY-PEERS | Inherited from peer group RR-OVERLAY-PEERS | - | Inherited from peer group RR-OVERLAY-PEERS | - | - | - | - |

#### Router BGP VPN-IPv4 Address Family

##### VPN-IPv4 Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | RCF In | RCF Out |
| ---------- | -------- | ------------ | ------------- | ------ | ------- |
| MPLS-OVERLAY-PEERS | True | - | - | - | - |
| RR-OVERLAY-PEERS | True | - | - | - | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65001
   router-id 10.255.2.2
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   bgp cluster-id 10.255.2.2
   maximum-paths 4 ecmp 4
   neighbor MPLS-OVERLAY-PEERS peer group
   neighbor MPLS-OVERLAY-PEERS remote-as 65001
   neighbor MPLS-OVERLAY-PEERS update-source Loopback0
   neighbor MPLS-OVERLAY-PEERS bfd
   neighbor MPLS-OVERLAY-PEERS route-reflector-client
   neighbor MPLS-OVERLAY-PEERS password 7 <removed>
   neighbor MPLS-OVERLAY-PEERS send-community
   neighbor MPLS-OVERLAY-PEERS maximum-routes 0
   neighbor RR-OVERLAY-PEERS peer group
   neighbor RR-OVERLAY-PEERS remote-as 65001
   neighbor RR-OVERLAY-PEERS update-source Loopback0
   neighbor RR-OVERLAY-PEERS bfd
   neighbor RR-OVERLAY-PEERS password 7 <removed>
   neighbor RR-OVERLAY-PEERS send-community
   neighbor RR-OVERLAY-PEERS maximum-routes 0
   neighbor 10.255.1.1 peer group MPLS-OVERLAY-PEERS
   neighbor 10.255.1.1 description pe1_Loopback0
   neighbor 10.255.1.2 peer group MPLS-OVERLAY-PEERS
   neighbor 10.255.1.2 description pe2_Loopback0
   neighbor 10.255.1.3 peer group MPLS-OVERLAY-PEERS
   neighbor 10.255.1.3 description pe3_Loopback0
   neighbor 10.255.2.1 peer group RR-OVERLAY-PEERS
   neighbor 10.255.2.1 description rr1_Loopback0
   !
   address-family ipv4
      no neighbor MPLS-OVERLAY-PEERS activate
      no neighbor RR-OVERLAY-PEERS activate
   !
   address-family vpn-ipv4
      neighbor MPLS-OVERLAY-PEERS activate
      neighbor RR-OVERLAY-PEERS activate
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
| LDP Router ID | 10.255.2.2 |
| LDP Interface Disabled Default | True |
| LDP Transport-Address Interface | Loopback0 |

#### MPLS and LDP Device Configuration

```eos
!
mpls ip
!
mpls ldp
   router-id 10.255.2.2
   transport-address interface Loopback0
   interface disabled default
   no shutdown
```

### MPLS Interfaces

| Interface | MPLS IP Enabled | LDP Enabled | IGP Sync |
| --------- | --------------- | ----------- | -------- |
| Ethernet2 | True | True | True |
| Ethernet3 | True | True | True |
| Ethernet4 | True | True | True |
| Loopback0 | - | True | - |

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |

### VRF Instances Device Configuration

```eos
!
vrf instance MGMT
```
