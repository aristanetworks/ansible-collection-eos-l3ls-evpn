# DC1-POD2-LEAF1A

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [IP Domain-list](#ip-domain-list)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [Enable Password](#enable-password)
- [Monitoring](#monitoring)
  - [SNMP](#snmp)
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
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Virtual Source NAT](#virtual-source-nat)
  - [Virtual Source NAT Summary](#virtual-source-nat-summary)
  - [Virtual Source NAT Configuration](#virtual-source-nat-configuration)
- [EOS CLI Device Configuration](#eos-cli-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | 192.168.1.15/24 | 192.168.1.254 |

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
   ip address 192.168.1.15/24
```

### IP Domain-list

#### Domains List

- structured-config.set.under.vrf.common-vrf

#### IP Domain-list Device Configuration

```eos
ip domain-list structured-config.set.under.vrf.common-vrf
!
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

#### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin secret sha512 <removed>
```

### Enable Password

Enable password has been disabled

## Monitoring

### SNMP

#### SNMP Configuration Summary

| Contact | Location | SNMP Traps | State |
| ------- | -------- | ---------- | ----- |
| - | TWODC_5STAGE_CLOS DC1 DC1_POD2 DC1-POD2-LEAF1A | All | Disabled |

#### SNMP Device Configuration

```eos
!
snmp-server location TWODC_5STAGE_CLOS DC1 DC1_POD2 DC1-POD2-LEAF1A
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

## VLANs

### VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 110 | Tenant_A_OP_Zone_1 | - |
| 111 | Tenant_A_OP_Zone_2 | - |
| 112 | Tenant_A_OP_Zone_3 | - |
| 113 | SVI_with_no_vxlan | - |
| 1100 | test_svi | - |
| 1101 | test_svi | - |
| 1102 | test_svi | - |
| 2500 | web-l2-vlan | - |
| 2600 | web-l2-vlan-2 | - |
| 2601 | l2vlan_with_no_vxlan | - |

### VLANs Device Configuration

```eos
!
vlan 110
   name Tenant_A_OP_Zone_1
!
vlan 111
   name Tenant_A_OP_Zone_2
!
vlan 112
   name Tenant_A_OP_Zone_3
!
vlan 113
   name SVI_with_no_vxlan
!
vlan 1100
   name test_svi
!
vlan 1101
   name test_svi
!
vlan 1102
   name test_svi
!
vlan 2500
   name web-l2-vlan
!
vlan 2600
   name web-l2-vlan-2
!
vlan 2601
   name l2vlan_with_no_vxlan
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
| Ethernet1 | P2P_DC1-POD2-SPINE1_Ethernet3 | - | 172.17.120.1/31 | default | - | False | - | - |
| Ethernet2 | P2P_DC1-POD2-SPINE2_Ethernet3 | - | 172.17.120.3/31 | default | - | False | - | - |
| Ethernet3 | P2P_DC1-RS2_Ethernet3 | - | 172.17.10.12/31 | default | - | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_DC1-POD2-SPINE1_Ethernet3
   no shutdown
   no switchport
   ip address 172.17.120.1/31
   mac security profile MACSEC_PROFILE
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet2
   description P2P_DC1-POD2-SPINE2_Ethernet3
   no shutdown
   no switchport
   ip address 172.17.120.3/31
   mac security profile MACSEC_PROFILE
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet3
   description P2P_DC1-RS2_Ethernet3
   no shutdown
   no switchport
   ip address 172.17.10.12/31
   service-profile QOS-PROFILE
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | ROUTER_ID | default | 172.16.120.3/32 |
| Loopback1 | VXLAN_TUNNEL_SOURCE | default | 172.18.120.3/32 |
| Loopback100 | DIAG_VRF_vrf_with_loopbacks_from_overlapping_pool | vrf_with_loopbacks_from_overlapping_pool | 10.100.0.3/32 |
| Loopback101 | DIAG_VRF_vrf_with_loopbacks_from_pod_pools | vrf_with_loopbacks_from_pod_pools | 10.101.102.3/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | ROUTER_ID | default | - |
| Loopback1 | VXLAN_TUNNEL_SOURCE | default | - |
| Loopback100 | DIAG_VRF_vrf_with_loopbacks_from_overlapping_pool | vrf_with_loopbacks_from_overlapping_pool | - |
| Loopback101 | DIAG_VRF_vrf_with_loopbacks_from_pod_pools | vrf_with_loopbacks_from_pod_pools | - |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description ROUTER_ID
   no shutdown
   ip address 172.16.120.3/32
!
interface Loopback1
   description VXLAN_TUNNEL_SOURCE
   no shutdown
   ip address 172.18.120.3/32
!
interface Loopback100
   description DIAG_VRF_vrf_with_loopbacks_from_overlapping_pool
   no shutdown
   vrf vrf_with_loopbacks_from_overlapping_pool
   ip address 10.100.0.3/32
!
interface Loopback101
   description DIAG_VRF_vrf_with_loopbacks_from_pod_pools
   no shutdown
   vrf vrf_with_loopbacks_from_pod_pools
   ip address 10.101.102.3/32
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan110 | set from structured_config on svi (was Tenant_A_OP_Zone_1) | Common_VRF | - | False |
| Vlan111 | Tenant_A_OP_Zone_2 | Common_VRF | - | True |
| Vlan112 | Tenant_A_OP_Zone_3 | Common_VRF | - | False |
| Vlan113 | SVI_with_no_vxlan | Common_VRF | - | False |
| Vlan1100 | test_svi | vrf_with_loopbacks_from_overlapping_pool | - | False |
| Vlan1101 | test_svi | vrf_with_loopbacks_from_pod_pools | - | False |
| Vlan1102 | test_svi | vrf_with_loopbacks_dc1_pod1_only | - | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| Vlan110 |  Common_VRF  |  -  |  10.1.10.1/24  |  -  |  -  |  -  |
| Vlan111 |  Common_VRF  |  -  |  10.1.11.1/24  |  -  |  -  |  -  |
| Vlan112 |  Common_VRF  |  -  |  10.1.12.1/24  |  -  |  -  |  -  |
| Vlan113 |  Common_VRF  |  -  |  10.10.13.1/24  |  -  |  -  |  -  |
| Vlan1100 |  vrf_with_loopbacks_from_overlapping_pool  |  -  |  10.100.100.1/24  |  -  |  -  |  -  |
| Vlan1101 |  vrf_with_loopbacks_from_pod_pools  |  -  |  10.101.100.1/24  |  -  |  -  |  -  |
| Vlan1102 |  vrf_with_loopbacks_dc1_pod1_only  |  -  |  10.102.100.1/24  |  -  |  -  |  -  |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan110
   description set from structured_config on svi (was Tenant_A_OP_Zone_1)
   no shutdown
   vrf Common_VRF
   ip address virtual 10.1.10.1/24
!
interface Vlan111
   description Tenant_A_OP_Zone_2
   shutdown
   vrf Common_VRF
   ip address virtual 10.1.11.1/24
!
interface Vlan112
   description Tenant_A_OP_Zone_3
   no shutdown
   vrf Common_VRF
   ip address virtual 10.1.12.1/24
   comment
   Comment created from raw_eos_cli under SVI 112 in VRF Common_VRF
   EOF

!
interface Vlan113
   description SVI_with_no_vxlan
   no shutdown
   vrf Common_VRF
   ip address virtual 10.10.13.1/24
!
interface Vlan1100
   description test_svi
   no shutdown
   vrf vrf_with_loopbacks_from_overlapping_pool
   ip address virtual 10.100.100.1/24
!
interface Vlan1101
   description test_svi
   no shutdown
   vrf vrf_with_loopbacks_from_pod_pools
   ip address virtual 10.101.100.1/24
!
interface Vlan1102
   description test_svi
   no shutdown
   vrf vrf_with_loopbacks_dc1_pod1_only
   ip address virtual 10.102.100.1/24
```

### VXLAN Interface

#### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| Source Interface | Loopback1 |
| UDP port | 4789 |

##### VLAN to VNI, Flood List and Multicast Group Mappings

| VLAN | VNI | Flood List | Multicast Group |
| ---- | --- | ---------- | --------------- |
| 110 | 10110 | - | - |
| 111 | 50111 | - | - |
| 112 | 10112 | - | - |
| 2500 | 2500 | - | - |
| 2600 | 12600 | - | - |

##### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| Common_VRF | 1025 | - |
| vrf_with_loopbacks_dc1_pod1_only | 1102 | - |
| vrf_with_loopbacks_from_overlapping_pool | 1100 | - |
| vrf_with_loopbacks_from_pod_pools | 1101 | - |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description DC1-POD2-LEAF1A_VTEP
   vxlan source-interface Loopback1
   vxlan udp-port 4789
   vxlan vlan 110 vni 10110
   vxlan vlan 111 vni 50111
   vxlan vlan 112 vni 10112
   vxlan vlan 2500 vni 2500
   vxlan vlan 2600 vni 12600
   vxlan vrf Common_VRF vni 1025
   vxlan vrf vrf_with_loopbacks_dc1_pod1_only vni 1102
   vxlan vrf vrf_with_loopbacks_from_overlapping_pool vni 1100
   vxlan vrf vrf_with_loopbacks_from_pod_pools vni 1101
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

Virtual Router MAC Address: 00:1c:73:00:dc:01

#### Virtual Router MAC Address Device Configuration

```eos
!
ip virtual-router mac-address 00:1c:73:00:dc:01
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| Common_VRF | True |
| MGMT | False |
| vrf_with_loopbacks_dc1_pod1_only | True |
| vrf_with_loopbacks_from_overlapping_pool | True |
| vrf_with_loopbacks_from_pod_pools | True |

#### IP Routing Device Configuration

```eos
!
ip routing
ip routing vrf Common_VRF
no ip routing vrf MGMT
ip routing vrf vrf_with_loopbacks_dc1_pod1_only
ip routing vrf vrf_with_loopbacks_from_overlapping_pool
ip routing vrf vrf_with_loopbacks_from_pod_pools
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| Common_VRF | false |
| MGMT | false |
| vrf_with_loopbacks_dc1_pod1_only | false |
| vrf_with_loopbacks_from_overlapping_pool | false |
| vrf_with_loopbacks_from_pod_pools | false |

### Static Routes

#### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP | Exit interface | Administrative Distance | Tag | Route Name | Metric |
| --- | ------------------ | ----------- | -------------- | ----------------------- | --- | ---------- | ------ |
| MGMT | 0.0.0.0/0 | 192.168.1.254 | - | 1 | - | - | - |

#### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 192.168.1.254
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65121 | 172.16.120.3 |

| BGP Tuning |
| ---------- |
| distance bgp 20 200 200 |
| update wait-install |
| no bgp default ipv4-unicast |
| maximum-paths 4 ecmp 4 |

#### Router BGP Peer Groups

##### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 5 |
| Send community | all |
| Maximum routes | 0 (no limit) |

##### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 172.16.120.1 | 65120 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 172.16.120.2 | 65120 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 172.17.10.13 | 65102 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | True | - | - | - | - |
| 172.17.120.0 | 65120 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.17.120.2 | 65120 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |

#### Router BGP EVPN Address Family

- VPN import pruning is **enabled**

##### EVPN Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | Encapsulation |
| ---------- | -------- | ------------ | ------------- | ------------- |
| EVPN-OVERLAY-PEERS | True |  - | - | default |

#### Router BGP VLANs

| VLAN | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute |
| ---- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ |
| 110 | 172.16.120.3:99110 | 99110:99110 | - | - | learned<br>router-mac system |
| 111 | 172.16.120.3:50111 | 50111:50111 | - | - | learned<br>router-mac system |
| 112 | 172.16.120.3:20112 | 20112:20112 | - | - | learned<br>router-mac system |
| 2500 | 172.16.120.3:2500 | 2500:2500 | - | - | learned |
| 2600 | 172.16.120.3:32600 | 32600:32600 | - | - | learned<br>router-mac system |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Common_VRF | 172.16.120.3:1025 | connected |
| vrf_with_loopbacks_dc1_pod1_only | 172.16.120.3:1102 | connected |
| vrf_with_loopbacks_from_overlapping_pool | 172.16.120.3:1100 | connected |
| vrf_with_loopbacks_from_pod_pools | 172.16.120.3:1101 | connected |

#### Router BGP Device Configuration

```eos
!
router bgp 65121
   router-id 172.16.120.3
   update wait-install
   no bgp default ipv4-unicast
   maximum-paths 4 ecmp 4
   distance bgp 20 200 200
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 5
   neighbor EVPN-OVERLAY-PEERS password 7 <removed>
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS password 7 <removed>
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor 172.16.120.1 peer group EVPN-OVERLAY-PEERS
   neighbor 172.16.120.1 remote-as 65120
   neighbor 172.16.120.1 description DC1-POD2-SPINE1_Loopback0
   neighbor 172.16.120.1 route-map RM-EVPN-FILTER-AS65120 out
   neighbor 172.16.120.2 peer group EVPN-OVERLAY-PEERS
   neighbor 172.16.120.2 remote-as 65120
   neighbor 172.16.120.2 description DC1-POD2-SPINE2_Loopback0
   neighbor 172.16.120.2 route-map RM-EVPN-FILTER-AS65120 out
   neighbor 172.17.10.13 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.10.13 remote-as 65102
   neighbor 172.17.10.13 bfd
   neighbor 172.17.10.13 description DC1-RS2_Ethernet3
   neighbor 172.17.120.0 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.120.0 remote-as 65120
   neighbor 172.17.120.0 description DC1-POD2-SPINE1_Ethernet3
   neighbor 172.17.120.2 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.120.2 remote-as 65120
   neighbor 172.17.120.2 description DC1-POD2-SPINE2_Ethernet3
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan 110
      rd 172.16.120.3:99110
      route-target both 99110:99110
      redistribute learned
      redistribute router-mac system
      !
      comment
      comment created from raw_eos_cli under router bgp svis inherited from svi profile
      EOF

   !
   vlan 111
      rd 172.16.120.3:50111
      route-target both 50111:50111
      redistribute learned
      redistribute router-mac system
      !
      comment
      comment created from raw_eos_cli under router bgp svi 111
      EOF

   !
   vlan 112
      rd 172.16.120.3:20112
      route-target both 20112:20112
      redistribute learned
      redistribute router-mac system
      !
      comment
      comment created from raw_eos_cli under router bgp svis inherited from svi parent profile
      EOF

   !
   vlan 2500
      rd 172.16.120.3:2500
      route-target both 2500:2500
      redistribute learned
   !
   vlan 2600
      rd 172.16.120.3:32600
      route-target both 32600:32600
      redistribute learned
      redistribute router-mac system
      !
      comment
      comment created from raw_eos_cli under router bgp l2vlan 2600
      EOF

   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
      route import match-failure action discard
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
   !
   address-family rt-membership
      neighbor EVPN-OVERLAY-PEERS activate
   !
   vrf Common_VRF
      rd 172.16.120.3:1025
      route-target import evpn 1025:1025
      route-target export evpn 1025:1025
      router-id 172.16.120.3
      redistribute connected
      !
      comment
      Comment created from raw_eos_cli under BGP for VRF Common_VRF
      EOF

   !
   vrf vrf_with_loopbacks_dc1_pod1_only
      rd 172.16.120.3:1102
      route-target import evpn 1102:1102
      route-target export evpn 1102:1102
      router-id 172.16.120.3
      redistribute connected
   !
   vrf vrf_with_loopbacks_from_overlapping_pool
      rd 172.16.120.3:1100
      route-target import evpn 1100:1100
      route-target export evpn 1100:1100
      router-id 172.16.120.3
      redistribute connected
   !
   vrf vrf_with_loopbacks_from_pod_pools
      rd 172.16.120.3:1101
      route-target import evpn 1101:1101
      route-target export evpn 1101:1101
      router-id 172.16.120.3
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

### Prefix-lists

#### Prefix-lists Summary

##### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 172.16.120.0/24 eq 32 |
| 20 | permit 172.18.120.0/24 eq 32 |

#### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 172.16.120.0/24 eq 32
   seq 20 permit 172.18.120.0/24 eq 32
```

### Route-maps

#### Route-maps Summary

##### RM-CONN-2-BGP

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY | - | - | - |

##### RM-EVPN-FILTER-AS65120

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | deny | as 65120 | - | - | - |
| 20 | permit | - | - | - | - |

#### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
!
route-map RM-EVPN-FILTER-AS65120 deny 10
   match as 65120
!
route-map RM-EVPN-FILTER-AS65120 permit 20
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| Common_VRF | enabled |
| MGMT | disabled |
| vrf_with_loopbacks_dc1_pod1_only | enabled |
| vrf_with_loopbacks_from_overlapping_pool | enabled |
| vrf_with_loopbacks_from_pod_pools | enabled |

### VRF Instances Device Configuration

```eos
!
vrf instance Common_VRF
!
vrf instance MGMT
!
vrf instance vrf_with_loopbacks_dc1_pod1_only
!
vrf instance vrf_with_loopbacks_from_overlapping_pool
!
vrf instance vrf_with_loopbacks_from_pod_pools
```

## Virtual Source NAT

### Virtual Source NAT Summary

| Source NAT VRF | Source NAT IP Address |
| -------------- | --------------------- |
| vrf_with_loopbacks_from_overlapping_pool | 10.100.0.3 |
| vrf_with_loopbacks_from_pod_pools | 10.101.102.3 |

### Virtual Source NAT Configuration

```eos
!
ip address virtual source-nat vrf vrf_with_loopbacks_from_overlapping_pool address 10.100.0.3
ip address virtual source-nat vrf vrf_with_loopbacks_from_pod_pools address 10.101.102.3
```

## EOS CLI Device Configuration

```eos
!
interface Loopback1111
  description Loopback created from raw_eos_cli under platform_settings vEOS-LAB

interface Loopback1000
  description Loopback created from raw_eos_cli under VRF Common_VRF

```
