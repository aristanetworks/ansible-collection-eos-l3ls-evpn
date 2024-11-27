# leaf1

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [IP Name Servers](#ip-name-servers)
  - [NTP](#ntp)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [Enable Password](#enable-password)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
- [MLAG](#mlag)
  - [MLAG Summary](#mlag-summary)
  - [MLAG Device Configuration](#mlag-device-configuration)
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
  - [VXLAN Interface](#vxlan-interface)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
- [Filters](#filters)
  - [IPv6 Prefix-lists](#ipv6-prefix-lists)
  - [Route-maps](#route-maps)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Virtual Source NAT](#virtual-source-nat)
  - [Virtual Source NAT Summary](#virtual-source-nat-summary)
  - [Virtual Source NAT Configuration](#virtual-source-nat-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 172.16.1.101/24 | 172.16.1.1 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | oob_management | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   no shutdown
   vrf MGMT
   ip address 172.16.1.101/24
```

### IP Name Servers

#### IP Name Servers Summary

| Name Server | VRF | Priority |
| ----------- | --- | -------- |
| 8.8.8.8 | MGMT | - |

#### IP Name Servers Device Configuration

```eos
ip name-server vrf MGMT 8.8.8.8
```

### NTP

#### NTP Summary

##### NTP Local Interface

| Interface | VRF |
| --------- | --- |
| Management1 | MGMT |

##### NTP Servers

| Server | VRF | Preferred | Burst | iBurst | Version | Min Poll | Max Poll | Local-interface | Key |
| ------ | --- | --------- | ----- | ------ | ------- | -------- | -------- | --------------- | --- |
| time.google.com | MGMT | True | - | - | - | - | - | - | - |

#### NTP Device Configuration

```eos
!
ntp local-interface vrf MGMT Management1
ntp server vrf MGMT time.google.com prefer
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

## Monitoring

### TerminAttr Daemon

#### TerminAttr Daemon Summary

| CV Compression | CloudVision Servers | VRF | Authentication | Smash Excludes | Ingest Exclude | Bypass AAA |
| -------------- | ------------------- | --- | -------------- | -------------- | -------------- | ---------- |
| gzip | 192.168.1.100:9910 | MGMT | token,/tmp/token | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | True |

#### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvaddr=192.168.1.100:9910 -cvauth=token,/tmp/token -cvvrf=MGMT -disableaaa -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -taillogs
   no shutdown
```

## MLAG

### MLAG Summary

| Domain-id | Local-interface | Peer-address | Peer-link |
| --------- | --------------- | ------------ | --------- |
| DC1_L3_LEAF1 | Vlan4094 | 2001:db8:3::2 | Port-Channel11 |

Dual primary detection is disabled.

### MLAG Device Configuration

```eos
!
mlag configuration
   domain-id DC1_L3_LEAF1
   local-interface Vlan4094
   peer-address 2001:db8:3::2
   peer-link Port-Channel11
   reload-delay mlag 300
   reload-delay non-mlag 330
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **mstp**

#### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 4096 |

#### Global Spanning-Tree Settings

- Spanning Tree disabled for VLANs: **4093-4094**

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
no spanning-tree vlan-id 4093-4094
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
| 11 | VRF10_VLAN11 | - |
| 12 | VRF10_VLAN12 | - |
| 21 | VRF11_VLAN21 | - |
| 22 | VRF11_VLAN22 | - |
| 3009 | MLAG_iBGP_VRF10 | LEAF_PEER_L3 |
| 3010 | MLAG_iBGP_VRF11 | LEAF_PEER_L3 |
| 3401 | L2_VLAN3401 | - |
| 3402 | L2_VLAN3402 | - |
| 4093 | LEAF_PEER_L3 | LEAF_PEER_L3 |
| 4094 | MLAG_PEER | MLAG |

### VLANs Device Configuration

```eos
!
vlan 11
   name VRF10_VLAN11
!
vlan 12
   name VRF10_VLAN12
!
vlan 21
   name VRF11_VLAN21
!
vlan 22
   name VRF11_VLAN22
!
vlan 3009
   name MLAG_iBGP_VRF10
   trunk group LEAF_PEER_L3
!
vlan 3010
   name MLAG_iBGP_VRF11
   trunk group LEAF_PEER_L3
!
vlan 3401
   name L2_VLAN3401
!
vlan 3402
   name L2_VLAN3402
!
vlan 4093
   name LEAF_PEER_L3
   trunk group LEAF_PEER_L3
!
vlan 4094
   name MLAG_PEER
   trunk group MLAG
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet5 | dc1-leaf1-server1_PCI1 | *trunk | *11-12,21-22 | *4092 | *- | 5 |
| Ethernet11 | MLAG_PEER_leaf2_Ethernet11 | *trunk | *- | *- | *LEAF_PEER_L3, MLAG | 11 |
| Ethernet12 | MLAG_PEER_leaf2_Ethernet12 | *trunk | *- | *- | *LEAF_PEER_L3, MLAG | 11 |

*Inherited from Port-Channel Interface

##### IPv6

| Interface | Description | Channel Group | IPv6 Address | VRF | MTU | Shutdown | ND RA Disabled | Managed Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | ----------- | --------------| ------------ | --- | --- | -------- | -------------- | -------------------| ----------- | ------------ |
| Ethernet1 | P2P_LINK_TO_SPINE1_Ethernet1 | - | 2001:db8:2::2/64 | default | 1500 | False | - | - | - | - |
| Ethernet2 | P2P_LINK_TO_SPINE2_Ethernet1 | - | 2001:db8:2:1::2/64 | default | 1500 | False | - | - | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_SPINE1_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ipv6 address 2001:db8:2::2/64
!
interface Ethernet2
   description P2P_LINK_TO_SPINE2_Ethernet1
   no shutdown
   mtu 1500
   no switchport
   ipv6 address 2001:db8:2:1::2/64
!
interface Ethernet5
   description dc1-leaf1-server1_PCI1
   no shutdown
   channel-group 5 mode active
!
interface Ethernet11
   description MLAG_PEER_leaf2_Ethernet11
   no shutdown
   channel-group 11 mode active
!
interface Ethernet12
   description MLAG_PEER_leaf2_Ethernet12
   no shutdown
   channel-group 11 mode active
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel5 | dc1-leaf1-server1_PortChannel dc1-leaf1-server1 | trunk | 11-12,21-22 | 4092 | - | - | - | 5 | - |
| Port-Channel11 | MLAG_PEER_leaf2_Po11 | trunk | - | - | LEAF_PEER_L3, MLAG | - | - | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel5
   description dc1-leaf1-server1_PortChannel dc1-leaf1-server1
   no shutdown
   switchport
   switchport trunk allowed vlan 11-12,21-22
   switchport trunk native vlan 4092
   switchport mode trunk
   mlag 5
   spanning-tree portfast
!
interface Port-Channel11
   description MLAG_PEER_leaf2_Po11
   no shutdown
   switchport
   switchport mode trunk
   switchport trunk group LEAF_PEER_L3
   switchport trunk group MLAG
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | - |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | - |
| Loopback10 | VRF10_VTEP_DIAGNOSTICS | VRF10 | 10.255.10.1/32 |
| Loopback11 | VRF11_VTEP_DIAGNOSTICS | VRF11 | 10.255.11.1/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | 2001:db8:1:1::1/64 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 2001:db8:5:1::1/64 |
| Loopback10 | VRF10_VTEP_DIAGNOSTICS | VRF10 | - |
| Loopback11 | VRF11_VTEP_DIAGNOSTICS | VRF11 | - |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   no shutdown
   ipv6 address 2001:db8:1:1::1/64
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   no shutdown
   ipv6 address 2001:db8:5:1::1/64
!
interface Loopback10
   description VRF10_VTEP_DIAGNOSTICS
   no shutdown
   vrf VRF10
   ip address 10.255.10.1/32
!
interface Loopback11
   description VRF11_VTEP_DIAGNOSTICS
   no shutdown
   vrf VRF11
   ip address 10.255.11.1/32
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan11 | VRF10_VLAN11 | VRF10 | - | False |
| Vlan12 | VRF10_VLAN12 | VRF10 | - | False |
| Vlan21 | VRF11_VLAN21 | VRF11 | - | False |
| Vlan22 | VRF11_VLAN22 | VRF11 | - | False |
| Vlan3009 | MLAG_PEER_L3_iBGP: vrf VRF10 | VRF10 | 1500 | False |
| Vlan3010 | MLAG_PEER_L3_iBGP: vrf VRF11 | VRF11 | 1500 | False |
| Vlan4093 | MLAG_PEER_L3_PEERING | default | 1500 | False |
| Vlan4094 | MLAG_PEER | default | 1500 | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| Vlan11 |  VRF10  |  -  |  10.10.11.1/24  |  -  |  -  |  -  |
| Vlan12 |  VRF10  |  -  |  10.10.12.1/24  |  -  |  -  |  -  |
| Vlan21 |  VRF11  |  -  |  10.10.21.1/24  |  -  |  -  |  -  |
| Vlan22 |  VRF11  |  -  |  10.10.22.1/24  |  -  |  -  |  -  |
| Vlan3009 |  VRF10  |  -  |  -  |  -  |  -  |  -  |
| Vlan3010 |  VRF11  |  -  |  -  |  -  |  -  |  -  |
| Vlan4093 |  default  |  -  |  -  |  -  |  -  |  -  |
| Vlan4094 |  default  |  -  |  -  |  -  |  -  |  -  |

##### IPv6

| Interface | VRF | IPv6 Address | IPv6 Virtual Addresses | Virtual Router Addresses | ND RA Disabled | Managed Config Flag | Other Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | --- | ------------ | ---------------------- | ------------------------ | -------------- | ------------------- | ----------------- | ----------- | ------------ |
| Vlan3009 | VRF10 | 2001:db8:4::1/64 | - | - | - | - | - | - | - |
| Vlan3010 | VRF11 | 2001:db8:4::1/64 | - | - | - | - | - | - | - |
| Vlan4093 | default | 2001:db8:4::1/64 | - | - | - | - | - | - | - |
| Vlan4094 | default | 2001:db8:3::1/64 | - | - | - | - | - | - | - |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan11
   description VRF10_VLAN11
   no shutdown
   vrf VRF10
   ip address virtual 10.10.11.1/24
!
interface Vlan12
   description VRF10_VLAN12
   no shutdown
   vrf VRF10
   ip address virtual 10.10.12.1/24
!
interface Vlan21
   description VRF11_VLAN21
   no shutdown
   vrf VRF11
   ip address virtual 10.10.21.1/24
!
interface Vlan22
   description VRF11_VLAN22
   no shutdown
   vrf VRF11
   ip address virtual 10.10.22.1/24
!
interface Vlan3009
   description MLAG_PEER_L3_iBGP: vrf VRF10
   no shutdown
   mtu 1500
   vrf VRF10
   ipv6 address 2001:db8:4::1/64
!
interface Vlan3010
   description MLAG_PEER_L3_iBGP: vrf VRF11
   no shutdown
   mtu 1500
   vrf VRF11
   ipv6 address 2001:db8:4::1/64
!
interface Vlan4093
   description MLAG_PEER_L3_PEERING
   no shutdown
   mtu 1500
   ipv6 address 2001:db8:4::1/64
!
interface Vlan4094
   description MLAG_PEER
   no shutdown
   mtu 1500
   no autostate
   ipv6 address 2001:db8:3::1/64
```

### VXLAN Interface

#### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| Source Interface | Loopback1 |
| UDP port | 4789 |
| vxlan encapsulation ipv6 | Enabled |
| EVPN MLAG Shared Router MAC | mlag-system-id |

##### VLAN to VNI, Flood List and Multicast Group Mappings

| VLAN | VNI | Flood List | Multicast Group |
| ---- | --- | ---------- | --------------- |
| 11 | 10011 | - | - |
| 12 | 10012 | - | - |
| 21 | 10021 | - | - |
| 22 | 10022 | - | - |
| 3401 | 13401 | - | - |
| 3402 | 13402 | - | - |

##### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| VRF10 | 10 | - |
| VRF11 | 11 | - |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description leaf1_VTEP
   vxlan source-interface Loopback1
   vxlan virtual-router encapsulation mac-address mlag-system-id
   vxlan udp-port 4789
   vxlan encapsulation ipv6
   vxlan vlan 11 vni 10011
   vxlan vlan 12 vni 10012
   vxlan vlan 21 vni 10021
   vxlan vlan 22 vni 10022
   vxlan vlan 3401 vni 13401
   vxlan vlan 3402 vni 13402
   vxlan vrf VRF10 vni 10
   vxlan vrf VRF11 vni 11
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

Virtual Router MAC Address: 00:1c:73:00:00:99

#### Virtual Router MAC Address Device Configuration

```eos
!
ip virtual-router mac-address 00:1c:73:00:00:99
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| MGMT | False |
| VRF10 | True |
| VRF11 | True |

#### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
ip routing vrf VRF10
ip routing vrf VRF11
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| MGMT | false |
| VRF10 | false |
| VRF11 | false |

#### IPv6 Routing Device Configuration

```eos
!
ipv6 unicast-routing
```

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

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65101 | 10.255.1.1 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| maximum-paths 4 ecmp 4 |

#### Router BGP Peer Groups

##### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 3 |
| Send community | all |
| Maximum routes | 0 (no limit) |

##### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

##### MLAG-IPv4-UNDERLAY-PEER

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65101 |
| Next-hop self | True |
| Send community | all |
| Maximum routes | 12000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 2001:db8:0:1::1 | 65100 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 2001:db8:0:2::1 | 65100 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 2001:db8:2:1::1 | 65100 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 2001:db8:2::1 | 65100 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 2001:db8:4::2 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | default | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |
| 2001:db8:4::2 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | VRF10 | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |
| 2001:db8:4::2 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | VRF11 | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Encapsulation |
| ---------- | -------- | ------------- |
| EVPN-OVERLAY-PEERS | True | default |

#### Router BGP VLANs

| VLAN | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute |
| ---- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ |
| 11 | 10.255.1.1:10011 | 10011:10011 | - | - | learned |
| 12 | 10.255.1.1:10012 | 10012:10012 | - | - | learned |
| 21 | 10.255.1.1:10021 | 10021:10021 | - | - | learned |
| 22 | 10.255.1.1:10022 | 10022:10022 | - | - | learned |
| 3401 | 10.255.1.1:13401 | 13401:13401 | - | - | learned |
| 3402 | 10.255.1.1:13402 | 13402:13402 | - | - | learned |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| VRF10 | 10.255.1.1:10 | connected |
| VRF11 | 10.255.1.1:11 | connected |

#### Router BGP Device Configuration

```eos
!
router bgp 65101
   router-id 10.255.1.1
   maximum-paths 4 ecmp 4
   no bgp default ipv4-unicast
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS password 7 <removed>
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS password 7 <removed>
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor MLAG-IPv4-UNDERLAY-PEER peer group
   neighbor MLAG-IPv4-UNDERLAY-PEER remote-as 65101
   neighbor MLAG-IPv4-UNDERLAY-PEER next-hop-self
   neighbor MLAG-IPv4-UNDERLAY-PEER description leaf2
   neighbor MLAG-IPv4-UNDERLAY-PEER password 7 <removed>
   neighbor MLAG-IPv4-UNDERLAY-PEER send-community
   neighbor MLAG-IPv4-UNDERLAY-PEER maximum-routes 12000
   neighbor MLAG-IPv4-UNDERLAY-PEER route-map RM-MLAG-PEER-IN in
   neighbor 2001:db8:0:1::1 peer group EVPN-OVERLAY-PEERS
   neighbor 2001:db8:0:1::1 remote-as 65100
   neighbor 2001:db8:0:1::1 description spine1
   neighbor 2001:db8:0:2::1 peer group EVPN-OVERLAY-PEERS
   neighbor 2001:db8:0:2::1 remote-as 65100
   neighbor 2001:db8:0:2::1 description spine2
   neighbor 2001:db8:2:1::1 peer group IPv4-UNDERLAY-PEERS
   neighbor 2001:db8:2:1::1 remote-as 65100
   neighbor 2001:db8:2:1::1 description spine2_Ethernet1
   neighbor 2001:db8:2::1 peer group IPv4-UNDERLAY-PEERS
   neighbor 2001:db8:2::1 remote-as 65100
   neighbor 2001:db8:2::1 description spine1_Ethernet1
   neighbor 2001:db8:4::2 peer group MLAG-IPv4-UNDERLAY-PEER
   neighbor 2001:db8:4::2 description leaf2
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan 11
      rd 10.255.1.1:10011
      route-target both 10011:10011
      redistribute learned
   !
   vlan 12
      rd 10.255.1.1:10012
      route-target both 10012:10012
      redistribute learned
   !
   vlan 21
      rd 10.255.1.1:10021
      route-target both 10021:10021
      redistribute learned
   !
   vlan 22
      rd 10.255.1.1:10022
      route-target both 10022:10022
      redistribute learned
   !
   vlan 3401
      rd 10.255.1.1:13401
      route-target both 13401:13401
      redistribute learned
   !
   vlan 3402
      rd 10.255.1.1:13402
      route-target both 13402:13402
      redistribute learned
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
      neighbor MLAG-IPv4-UNDERLAY-PEER activate
   !
   address-family ipv6
      neighbor IPv4-UNDERLAY-PEERS activate
      neighbor MLAG-IPv4-UNDERLAY-PEER activate
   !
   vrf VRF10
      rd 10.255.1.1:10
      route-target import evpn 10:10
      route-target export evpn 10:10
      router-id 10.255.1.1
      neighbor 2001:db8:4::2 peer group MLAG-IPv4-UNDERLAY-PEER
      redistribute connected
   !
   vrf VRF11
      rd 10.255.1.1:11
      route-target import evpn 11:11
      route-target export evpn 11:11
      router-id 10.255.1.1
      neighbor 2001:db8:4::2 peer group MLAG-IPv4-UNDERLAY-PEER
      redistribute connected
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

## Multicast

### IP IGMP Snooping

#### IP IGMP Snooping Summary

| IGMP Snooping | Fast Leave | Interface Restart Query | Proxy | Restart Query Interval | Robustness Variable |
| ------------- | ---------- | ----------------------- | ----- | ---------------------- | ------------------- |
| Enabled | - | - | - | - | - |

#### IP IGMP Snooping Device Configuration

```eos
```

## Filters

### IPv6 Prefix-lists

#### IPv6 Prefix-lists Summary

##### PL-LOOPBACKS-EVPN-OVERLAY-V6

| Sequence | Action |
| -------- | ------ |
| 10 | permit 2001:DB8:1::/48 eq 64 |
| 20 | permit 2001:DB8:5::/48 eq 64 |

#### IPv6 Prefix-lists Device Configuration

```eos
!
ipv6 prefix-list PL-LOOPBACKS-EVPN-OVERLAY-V6
   seq 10 permit 2001:DB8:1::/48 eq 64
   seq 20 permit 2001:DB8:5::/48 eq 64
```

### Route-maps

#### Route-maps Summary

##### RM-CONN-2-BGP

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY | - | - | - |
| 30 | permit | ipv6 address prefix-list PL-LOOPBACKS-EVPN-OVERLAY-V6 | - | - | - |

##### RM-MLAG-PEER-IN

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | - | origin incomplete | - | - |

#### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
!
route-map RM-CONN-2-BGP permit 30
   match ipv6 address prefix-list PL-LOOPBACKS-EVPN-OVERLAY-V6
!
route-map RM-MLAG-PEER-IN permit 10
   description Make routes learned over MLAG Peer-link less preferred on spines to ensure optimal routing
   set origin incomplete
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |
| VRF10 | enabled |
| VRF11 | enabled |

### VRF Instances Device Configuration

```eos
!
vrf instance MGMT
!
vrf instance VRF10
!
vrf instance VRF11
```

## Virtual Source NAT

### Virtual Source NAT Summary

| Source NAT VRF | Source NAT IP Address |
| -------------- | --------------------- |
| VRF10 | 10.255.10.1 |
| VRF11 | 10.255.11.1 |

### Virtual Source NAT Configuration

```eos
!
ip address virtual source-nat vrf VRF10 address 10.255.10.1
ip address virtual source-nat vrf VRF11 address 10.255.11.1
```
