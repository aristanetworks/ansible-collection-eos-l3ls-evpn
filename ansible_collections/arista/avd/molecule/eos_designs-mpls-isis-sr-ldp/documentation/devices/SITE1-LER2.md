# SITE1-LER2

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Enable Password](#enable-password)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Device Configuration](#internal-vlan-allocation-policy-device-configuration)
- [VLANs](#vlans)
  - [VLANs Summary](#vlans-summary)
  - [VLANs Device Configuration](#vlans-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
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
- [Patch Panel](#patch-panel)
  - [Patch Panel Summary](#patch-panel-summary)
  - [Patch Panel Device Configuration](#patch-panel-device-configuration)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [EOS CLI Device Configuration](#eos-cli-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | 192.168.200.106/24 | 192.168.200.5 |

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
   ip address 192.168.200.106/24
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

### Enable Password

Enable password has been disabled

## Spanning Tree

### Spanning Tree Summary

STP mode: **mstp**

#### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 4096 |

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
spanning-tree mst 0 priority 4096
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

## VLANs

### VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 10 | TENANT_A_L2_SERVICE | - |
| 20 | TENANT_A_L2_SERVICE | - |
| 2020 | TENANT_B_INSIDE_FW | - |

### VLANs Device Configuration

```eos
!
vlan 10
   name TENANT_A_L2_SERVICE
!
vlan 20
   name TENANT_A_L2_SERVICE
!
vlan 2020
   name TENANT_B_INSIDE_FW
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
| Ethernet5.100 | TENANT_B_SITE_3 | - | 100 | - |

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_SITE1-LSR2_Ethernet1 | - | 100.64.48.2/31 | default | 9214 | False | - | - |
| Ethernet2 | P2P_SITE1-LER1_Ethernet2 | - | 100.64.48.5/31 | default | 9178 | False | - | - |
| Ethernet5.100 | TENANT_B_SITE_3 | - | 192.168.48.0/31 | TENANT_B_WAN | - | False | - | - |

##### IPv6

| Interface | Description | Channel Group | IPv6 Address | VRF | MTU | Shutdown | ND RA Disabled | Managed Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | ----------- | --------------| ------------ | --- | --- | -------- | -------------- | -------------------| ----------- | ------------ |
| Ethernet1 | P2P_SITE1-LSR2_Ethernet1 | - | - | default | 9214 | False | - | - | - | - |
| Ethernet2 | P2P_SITE1-LER1_Ethernet2 | - | - | default | 9178 | False | - | - | - | - |

##### ISIS

| Interface | Channel Group | ISIS Instance | ISIS BFD | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | Authentication Mode |
| --------- | ------------- | ------------- | -------- | ----------- | ---- | ----------------- | ------------- | ------------------- |
| Ethernet1 | - | CORE | - | 50 | point-to-point | level-1-2 | False | md5 |
| Ethernet2 | - | CORE | - | 500 | point-to-point | level-2 | False | md5 |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_SITE1-LSR2_Ethernet1
   no shutdown
   mtu 9214
   speed forced 100gfull
   no switchport
   ip address 100.64.48.2/31
   ipv6 enable
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
   isis enable CORE
   isis circuit-type level-1-2
   isis metric 50
   no isis hello padding
   isis network point-to-point
   isis authentication mode md5
   isis authentication key 7 <removed>
   link-debounce time 1000

!
interface Ethernet2
   description P2P_SITE1-LER1_Ethernet2
   no shutdown
   mtu 9178
   speed forced 10000full
   no switchport
   ip address 100.64.48.5/31
   ipv6 enable
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
   isis enable CORE
   isis circuit-type level-2
   isis metric 500
   no isis hello padding
   isis network point-to-point
   isis authentication mode md5
   isis authentication key 7 <removed>
   link-debounce time 1500

!
interface Ethernet3
   no shutdown
   channel-group 3 mode active
!
interface Ethernet4
   no shutdown
   channel-group 3 mode active
!
interface Ethernet5
   no shutdown
   no switchport
!
interface Ethernet5.100
   description TENANT_B_SITE_3
   no shutdown
   encapsulation dot1q vlan 100
   vrf TENANT_B_WAN
   ip address 192.168.48.0/31
!
interface Ethernet8
   description CPE_CPE_TENANT_A_SITE1_Ethernet2
   no shutdown
   channel-group 8 mode active
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |

##### Flexible Encapsulation Interfaces

| Interface | Description | Vlan ID | Client Encapsulation | Client Inner Encapsulation | Client VLAN | Client Outer VLAN Tag | Client Inner VLAN Tag | Network Encapsulation | Network Inner Encapsulation | Network VLAN | Network Outer VLAN Tag | Network Inner VLAN Tag |
| --------- | ----------- | ------- | --------------- | --------------------- | ----------- | --------------------- | --------------------- | ---------------- | ---------------------- | ------------ | ---------------------- | ---------------------- |
| Port-Channel3.1000 | - | - | dot1q | - | 1000 | - | - | client | - | - | - | - |
| Port-Channel3.1001 | - | - | dot1q | - | 1001 | - | - | client | - | - | - | - |
| Port-Channel3.1002 | - | - | dot1q | - | 1002 | - | - | client | - | - | - | - |
| Port-Channel3.1003 | - | - | dot1q | - | 1003 | - | - | client | - | - | - | - |
| Port-Channel3.1004 | - | - | dot1q | - | 1004 | - | - | client | - | - | - | - |
| Port-Channel8.111 | - | 111 | dot1q | - | 111 | - | - | client | - | - | - | - |
| Port-Channel8.222 | - | 222 | dot1q | - | 222 | - | - | client | - | - | - | - |
| Port-Channel8.333 | - | 434 | dot1q | - | 333 | - | - | client | - | - | - | - |

##### EVPN Multihoming

####### EVPN Multihoming Summary

| Interface | Ethernet Segment Identifier | Multihoming Redundancy Mode | Route Target |
| --------- | --------------------------- | --------------------------- | ------------ |
| Port-Channel3 | 0000:0000:0102:0000:0034 | all-active | 01:02:00:00:00:34 |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel3
   no shutdown
   no switchport
   !
   evpn ethernet-segment
      identifier 0000:0000:0102:0000:0034
      route-target import 01:02:00:00:00:34
   lacp system-id 0102.0000.0034
!
interface Port-Channel3.1000
   no shutdown
   !
   encapsulation vlan
      client dot1q 1000 network client
!
interface Port-Channel3.1001
   no shutdown
   !
   encapsulation vlan
      client dot1q 1001 network client
!
interface Port-Channel3.1002
   no shutdown
   !
   encapsulation vlan
      client dot1q 1002 network client
!
interface Port-Channel3.1003
   no shutdown
   !
   encapsulation vlan
      client dot1q 1003 network client
!
interface Port-Channel3.1004
   no shutdown
   !
   encapsulation vlan
      client dot1q 1004 network client
!
interface Port-Channel8
   description CPE_CPE_TENANT_A_SITE1_EVPN-A-A-PortChannel
   no shutdown
   no switchport
!
interface Port-Channel8.111
   vlan id 111
   !
   encapsulation vlan
      client dot1q 111 network client
!
interface Port-Channel8.222
   vlan id 222
   !
   encapsulation vlan
      client dot1q 222 network client
!
interface Port-Channel8.333
   vlan id 434
   !
   encapsulation vlan
      client dot1q 333 network client
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | ROUTER_ID | default | 100.70.0.6/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | ROUTER_ID | default | 2000:1234:ffff:ffff::6/128 |

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
   ip address 100.70.0.6/32
   ipv6 address 2000:1234:ffff:ffff::6/128
   mpls ldp interface
   node-segment ipv4 index 206
   node-segment ipv6 index 206
   isis enable CORE
   isis passive
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan2020 | TENANT_B_INSIDE_FW | TENANT_B_INTRA | - | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| Vlan2020 |  TENANT_B_INTRA  |  -  |  -  |  -  |  -  |  -  |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan2020
   description TENANT_B_INSIDE_FW
   no shutdown
   vrf TENANT_B_INTRA
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
| MGMT | False |
| TENANT_B_INTRA | True |
| TENANT_B_WAN | True |

#### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
ip routing vrf TENANT_B_INTRA
ip routing vrf TENANT_B_WAN
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| MGMT | false |
| TENANT_B_INTRA | false |
| TENANT_B_WAN | false |

#### IPv6 Routing Device Configuration

```eos
!
ipv6 unicast-routing
```

### Static Routes

#### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP | Exit interface | Administrative Distance | Tag | Route Name | Metric |
| --- | ------------------ | ----------- | -------------- | ----------------------- | --- | ---------- | ------ |
| MGMT | 0.0.0.0/0 | 192.168.200.5 | - | 1 | - | - | - |

#### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 192.168.200.5
```

### Router ISIS

#### Router ISIS Summary

| Settings | Value |
| -------- | ----- |
| Instance | CORE |
| Net-ID | 49.0001.1000.7000.0006.00 |
| Type | level-1-2 |
| Router-ID | 100.70.0.6 |
| Log Adjacency Changes | True |
| MPLS LDP Sync Default | True |
| Local Convergence Delay (ms) | 15000 |
| Advertise Passive-only | True |
| SR MPLS Enabled | True |

#### ISIS Interfaces Summary

| Interface | ISIS Instance | ISIS Metric | Interface Mode |
| --------- | ------------- | ----------- | -------------- |
| Ethernet1 | CORE | 50 | point-to-point |
| Ethernet2 | CORE | 500 | point-to-point |
| Loopback0 | CORE | - | passive |

#### ISIS Segment-routing Node-SID

| Loopback | IPv4 Index | IPv6 Index |
| -------- | ---------- | ---------- |
| Loopback0 | 206 | 206 |

#### ISIS IPv4 Address Family Summary

| Settings | Value |
| -------- | ----- |
| IPv4 Address-family Enabled | True |
| Maximum-paths | 4 |
| TI-LFA Mode | link-protection |

#### ISIS IPv6 Address Family Summary

| Settings | Value |
| -------- | ----- |
| IPv6 Address-family Enabled | True |
| Maximum-paths | 4 |
| TI-LFA Mode | link-protection |

#### Router ISIS Device Configuration

```eos
!
router isis CORE
   net 49.0001.1000.7000.0006.00
   router-id ipv4 100.70.0.6
   is-type level-1-2
   log-adjacency-changes
   mpls ldp sync default
   timers local-convergence-delay 15000 protected-prefixes
   advertise passive-only
   !
   address-family ipv4 unicast
      maximum-paths 4
      fast-reroute ti-lfa mode link-protection
   !
   address-family ipv6 unicast
      maximum-paths 4
      fast-reroute ti-lfa mode link-protection
   !
   segment-routing mpls
      no shutdown
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65000 | 100.70.0.6 |

| BGP Tuning |
| ---------- |
| distance bgp 20 200 200 |
| update wait-install |
| no bgp default ipv4-unicast |
| maximum-paths 4 ecmp 4 |

#### Router BGP Peer Groups

##### MPLS-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | mpls |
| Remote AS | 65000 |
| Source | Loopback0 |
| BFD | True |
| Send community | all |
| Maximum routes | 0 (no limit) |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 100.70.0.5 | Inherited from peer group MPLS-OVERLAY-PEERS | default | - | Inherited from peer group MPLS-OVERLAY-PEERS | Inherited from peer group MPLS-OVERLAY-PEERS | - | Inherited from peer group MPLS-OVERLAY-PEERS | - | - | - | - |
| 100.70.0.7 | Inherited from peer group MPLS-OVERLAY-PEERS | default | - | Inherited from peer group MPLS-OVERLAY-PEERS | Inherited from peer group MPLS-OVERLAY-PEERS | - | Inherited from peer group MPLS-OVERLAY-PEERS | - | - | - | - |
| 100.70.0.8 | Inherited from peer group MPLS-OVERLAY-PEERS | default | - | Inherited from peer group MPLS-OVERLAY-PEERS | Inherited from peer group MPLS-OVERLAY-PEERS | - | Inherited from peer group MPLS-OVERLAY-PEERS | - | - | - | - |
| 100.70.0.9 | Inherited from peer group MPLS-OVERLAY-PEERS | default | - | Inherited from peer group MPLS-OVERLAY-PEERS | Inherited from peer group MPLS-OVERLAY-PEERS | - | Inherited from peer group MPLS-OVERLAY-PEERS | - | - | - | - |
| 192.168.48.1 | 65201 | TENANT_B_WAN | - | - | - | - | - | - | - | - | - |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | Encapsulation |
| ---------- | -------- | ------------ | ------------- | ------------- |
| MPLS-OVERLAY-PEERS | True |  - | - | default |

##### EVPN Neighbor Default Encapsulation

| Neighbor Default Encapsulation | Next-hop-self Source Interface |
| ------------------------------ | ------------------------------ |
| mpls | Loopback0 |

#### Router BGP VPN-IPv4 Address Family

##### VPN-IPv4 Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | RCF In | RCF Out |
| ---------- | -------- | ------------ | ------------- | ------ | ------- |
| MPLS-OVERLAY-PEERS | True | - | - | - | - |

#### Router BGP VPN-IPv6 Address Family

##### VPN-IPv6 Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | RCF In | RCF Out |
| ---------- | -------- | ------------ | ------------- | ------ | ------- |
| MPLS-OVERLAY-PEERS | True | - | - | - | - |

#### Router BGP VLANs

| VLAN | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute |
| ---- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ |
| 10 | 100.70.0.6:10010 | 65000:10010 | - | - | learned |
| 20 | 100.70.0.6:123456 | 65000:123456 | - | - | learned |
| 2020 | 100.70.0.6:22020 | 65000:22020 | - | - | learned |

#### Router BGP VPWS Instances

| Instance | Route-Distinguisher | Both Route-Target | MPLS Control Word | Label Flow | MTU | Pseudowire | Local ID | Remote ID |
| -------- | ------------------- | ----------------- | ----------------- | -----------| --- | ---------- | -------- | --------- |
| TENANT_B | 100.70.0.6:2000 | 65000:2000 | False | False | - | TEN_B_site3_site5_eline_vlan_based_1000 | 31000 | 51000 |
| TENANT_B | 100.70.0.6:2000 | 65000:2000 | False | False | - | TEN_B_site3_site5_eline_vlan_based_1001 | 31001 | 51001 |
| TENANT_B | 100.70.0.6:2000 | 65000:2000 | False | False | - | TEN_B_site3_site5_eline_vlan_based_1002 | 31002 | 51002 |
| TENANT_B | 100.70.0.6:2000 | 65000:2000 | False | False | - | TEN_B_site3_site5_eline_vlan_based_1003 | 31003 | 51003 |
| TENANT_B | 100.70.0.6:2000 | 65000:2000 | False | False | - | TEN_B_site3_site5_eline_vlan_based_1004 | 31004 | 51004 |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| TENANT_B_INTRA | 100.70.0.6:19 | connected |
| TENANT_B_WAN | 100.70.0.6:20 | connected |

#### Router BGP Device Configuration

```eos
!
router bgp 65000
   router-id 100.70.0.6
   update wait-install
   no bgp default ipv4-unicast
   maximum-paths 4 ecmp 4
   distance bgp 20 200 200
   neighbor MPLS-OVERLAY-PEERS peer group
   neighbor MPLS-OVERLAY-PEERS remote-as 65000
   neighbor MPLS-OVERLAY-PEERS update-source Loopback0
   neighbor MPLS-OVERLAY-PEERS bfd
   neighbor MPLS-OVERLAY-PEERS password 7 <removed>
   neighbor MPLS-OVERLAY-PEERS send-community
   neighbor MPLS-OVERLAY-PEERS maximum-routes 0
   neighbor 100.70.0.5 peer group MPLS-OVERLAY-PEERS
   neighbor 100.70.0.5 description SITE1-LER1_Loopback0
   neighbor 100.70.0.7 peer group MPLS-OVERLAY-PEERS
   neighbor 100.70.0.7 description SITE2-LER1_Loopback0
   neighbor 100.70.0.8 peer group MPLS-OVERLAY-PEERS
   neighbor 100.70.0.8 description SITE1-RR1_Loopback0
   neighbor 100.70.0.9 peer group MPLS-OVERLAY-PEERS
   neighbor 100.70.0.9 description SITE2-RR1_Loopback0
   !
   vlan 10
      rd 100.70.0.6:10010
      route-target both 65000:10010
      redistribute learned
   !
   vlan 20
      rd 100.70.0.6:123456
      route-target both 65000:123456
      redistribute learned
   !
   vlan 2020
      rd 100.70.0.6:22020
      route-target both 65000:22020
      redistribute learned
   !
   vpws TENANT_B
      rd 100.70.0.6:2000
      route-target import export evpn 65000:2000
      !
      pseudowire TEN_B_site3_site5_eline_vlan_based_1000
         evpn vpws id local 31000 remote 51000
      !
      pseudowire TEN_B_site3_site5_eline_vlan_based_1001
         evpn vpws id local 31001 remote 51001
      !
      pseudowire TEN_B_site3_site5_eline_vlan_based_1002
         evpn vpws id local 31002 remote 51002
      !
      pseudowire TEN_B_site3_site5_eline_vlan_based_1003
         evpn vpws id local 31003 remote 51003
      !
      pseudowire TEN_B_site3_site5_eline_vlan_based_1004
         evpn vpws id local 31004 remote 51004
   !
   address-family evpn
      neighbor default encapsulation mpls next-hop-self source-interface Loopback0
      neighbor MPLS-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor MPLS-OVERLAY-PEERS activate
   !
   address-family vpn-ipv4
      neighbor MPLS-OVERLAY-PEERS activate
      neighbor default encapsulation mpls next-hop-self source-interface Loopback0
   !
   address-family vpn-ipv6
      neighbor MPLS-OVERLAY-PEERS activate
      neighbor default encapsulation mpls next-hop-self source-interface Loopback0
   !
   vrf TENANT_B_INTRA
      rd 100.70.0.6:19
      route-target import evpn 65000:19
      route-target export evpn 65000:19
      router-id 100.70.0.6
      redistribute connected
   !
   vrf TENANT_B_WAN
      rd 100.70.0.6:20
      route-target import vpn-ipv4 65000:20
      route-target import vpn-ipv6 65000:20
      route-target export vpn-ipv4 65000:20
      route-target export vpn-ipv6 65000:20
      router-id 100.70.0.6
      update wait-install
      neighbor 192.168.48.1 remote-as 65201
      neighbor 192.168.48.1 description TENANT_B_CPE_SITE3
      neighbor 192.168.48.1 password 7 <removed>
      redistribute connected
      !
      address-family ipv4
         neighbor 192.168.48.1 activate
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
| LDP Router ID | 100.70.0.6 |
| LDP Interface Disabled Default | True |
| LDP Transport-Address Interface | Loopback0 |

#### MPLS and LDP Device Configuration

```eos
!
mpls ip
!
mpls ldp
   router-id 100.70.0.6
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

## Patch Panel

### Patch Panel Summary

#### Patch Panel Connections

| Patch Name | Enabled | Connector A Type | Connector A Endpoint | Connector B Type | Connector B Endpoint |
| ---------- | ------- | ---------------- | -------------------- | ---------------- | -------------------- |
| TEN_B_site3_site5_eline_vlan_based_1000 | True | Interface | Port-Channel3.1000 | Pseudowire | bgp vpws TENANT_B pseudowire TEN_B_site3_site5_eline_vlan_based_1000 |
| TEN_B_site3_site5_eline_vlan_based_1001 | True | Interface | Port-Channel3.1001 | Pseudowire | bgp vpws TENANT_B pseudowire TEN_B_site3_site5_eline_vlan_based_1001 |
| TEN_B_site3_site5_eline_vlan_based_1002 | True | Interface | Port-Channel3.1002 | Pseudowire | bgp vpws TENANT_B pseudowire TEN_B_site3_site5_eline_vlan_based_1002 |
| TEN_B_site3_site5_eline_vlan_based_1003 | True | Interface | Port-Channel3.1003 | Pseudowire | bgp vpws TENANT_B pseudowire TEN_B_site3_site5_eline_vlan_based_1003 |
| TEN_B_site3_site5_eline_vlan_based_1004 | True | Interface | Port-Channel3.1004 | Pseudowire | bgp vpws TENANT_B pseudowire TEN_B_site3_site5_eline_vlan_based_1004 |

### Patch Panel Device Configuration

```eos
!
patch panel
   patch TEN_B_site3_site5_eline_vlan_based_1000
      connector 1 interface Port-Channel3.1000
      connector 2 pseudowire bgp vpws TENANT_B pseudowire TEN_B_site3_site5_eline_vlan_based_1000
   !
   patch TEN_B_site3_site5_eline_vlan_based_1001
      connector 1 interface Port-Channel3.1001
      connector 2 pseudowire bgp vpws TENANT_B pseudowire TEN_B_site3_site5_eline_vlan_based_1001
   !
   patch TEN_B_site3_site5_eline_vlan_based_1002
      connector 1 interface Port-Channel3.1002
      connector 2 pseudowire bgp vpws TENANT_B pseudowire TEN_B_site3_site5_eline_vlan_based_1002
   !
   patch TEN_B_site3_site5_eline_vlan_based_1003
      connector 1 interface Port-Channel3.1003
      connector 2 pseudowire bgp vpws TENANT_B pseudowire TEN_B_site3_site5_eline_vlan_based_1003
   !
   patch TEN_B_site3_site5_eline_vlan_based_1004
      connector 1 interface Port-Channel3.1004
      connector 2 pseudowire bgp vpws TENANT_B pseudowire TEN_B_site3_site5_eline_vlan_based_1004
   !
```

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
| MGMT | disabled |
| TENANT_B_INTRA | enabled |
| TENANT_B_WAN | enabled |

### VRF Instances Device Configuration

```eos
!
vrf instance MGMT
!
vrf instance TENANT_B_INTRA
!
vrf instance TENANT_B_WAN
```

## EOS CLI Device Configuration

```eos
!
management security
   password encryption-key common

```
