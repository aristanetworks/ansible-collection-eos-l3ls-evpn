# DC1.POD1.LEAF2A

## Table of Contents

- [Management](#management)
  - [IP Domain-list](#ip-domain-list)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [Enable Password](#enable-password)
- [Monitoring](#monitoring)
  - [SNMP](#snmp)
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
  - [Route-maps](#route-maps)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Virtual Source NAT](#virtual-source-nat)
  - [Virtual Source NAT Summary](#virtual-source-nat-summary)
  - [Virtual Source NAT Configuration](#virtual-source-nat-configuration)
- [EOS CLI Device Configuration](#eos-cli-device-configuration)

## Management

### IP Domain-list

#### Domains List

- structured-config.set.on.node
- structured-config.set.under.vrf.common-vrf

#### IP Domain-list Device Configuration

```eos
ip domain-list structured-config.set.on.node
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
| - | TWODC_5STAGE_CLOS DC1 DC1_POD1 DC1.POD1.LEAF2A | All | Disabled |

#### SNMP Device Configuration

```eos
!
snmp-server location TWODC_5STAGE_CLOS DC1 DC1_POD1 DC1.POD1.LEAF2A
```

## MLAG

### MLAG Summary

| Domain-id | Local-interface | Peer-address | Peer-link |
| --------- | --------------- | ------------ | --------- |
| RACK2_MLAG | Vlan4094 | 172.20.110.3 | Port-Channel5 |

Dual primary detection is enabled. The detection delay is 5 seconds.

### MLAG Device Configuration

```eos
!
mlag configuration
   domain-id RACK2_MLAG
   local-interface Vlan4094
   peer-address 172.20.110.3
   peer-address heartbeat 192.168.1.9 vrf MGMT
   peer-link Port-Channel5
   dual-primary detection delay 5 action errdisable all-interfaces
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

- Spanning Tree disabled for VLANs: **4094**

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
no spanning-tree vlan-id 4094
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
| 4085 | L2LEAF_INBAND_MGMT | - |
| 4094 | MLAG | MLAG |

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
!
vlan 4085
   name L2LEAF_INBAND_MGMT
!
vlan 4094
   name MLAG
   trunk group MLAG
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet3 | L2_DC1-POD1-L2LEAF2A_Ethernet1 | *trunk | *110-113,1100-1102,2500,2600-2601,4085 | *- | *- | 3 |
| Ethernet4 | L2_DC1-POD1-L2LEAF2B_Ethernet1 | *trunk | *110-113,1100-1102,2500,2600-2601,4085 | *- | *- | 3 |
| Ethernet5 | MLAG_DC1-POD1-LEAF2B_Ethernet5 | *trunk | *- | *- | *MLAG | 5 |
| Ethernet6 | MLAG_DC1-POD1-LEAF2B_Ethernet6 | *trunk | *- | *- | *MLAG | 5 |
| Ethernet16 | SERVER_server-1_Eth1 | *access | *110 | *- | *- | 16 |
| Ethernet17 | Set using structured_config on server adapter | *access | *110 | *- | *- | 17 |
| Ethernet18 | SERVER_server-1_Eth5 | *access | *110 | *- | *- | 18 |
| Ethernet19 | SERVER_server-1_Eth7 | *access | *110 | *- | *- | 19 |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_DC1-POD1-SPINE1_Ethernet4 | - | 172.17.110.9/31 | default | - | False | - | - |
| Ethernet2 | P2P_DC1-POD1-SPINE2_Ethernet4 | - | 172.17.110.11/31 | default | - | False | - | - |
| Ethernet7 | P2P_DC2-POD1-LEAF1A_Ethernet6 | - | 100.100.100.101/24 | default | - | False | - | - |
| Ethernet11 | P2P_DC1-POD1-SPINE1_Ethernet7 | - | 172.17.110.13/31 | default | - | False | - | - |
| Ethernet12 | P2P_DC1-POD1-SPINE2_Ethernet7 | - | 172.17.110.15/31 | default | - | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_DC1-POD1-SPINE1_Ethernet4
   no shutdown
   no switchport
   ip address 172.17.110.9/31
   mac security profile MACSEC_PROFILE
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet2
   description P2P_DC1-POD1-SPINE2_Ethernet4
   no shutdown
   no switchport
   ip address 172.17.110.11/31
   mac security profile MACSEC_PROFILE
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet3
   description L2_DC1-POD1-L2LEAF2A_Ethernet1
   no shutdown
   channel-group 3 mode active
!
interface Ethernet4
   description L2_DC1-POD1-L2LEAF2B_Ethernet1
   no shutdown
   channel-group 3 mode active
!
interface Ethernet5
   description MLAG_DC1-POD1-LEAF2B_Ethernet5
   no shutdown
   channel-group 5 mode active
!
interface Ethernet6
   description MLAG_DC1-POD1-LEAF2B_Ethernet6
   no shutdown
   channel-group 5 mode active
!
interface Ethernet7
   description P2P_DC2-POD1-LEAF1A_Ethernet6
   no shutdown
   no switchport
   ip address 100.100.100.101/24
!
interface Ethernet11
   description P2P_DC1-POD1-SPINE1_Ethernet7
   no shutdown
   no switchport
   ip address 172.17.110.13/31
   mac security profile MACSEC_PROFILE
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet12
   description P2P_DC1-POD1-SPINE2_Ethernet7
   no shutdown
   no switchport
   ip address 172.17.110.15/31
   mac security profile MACSEC_PROFILE
   ptp enable
   service-profile QOS-PROFILE
!
interface Ethernet16
   description SERVER_server-1_Eth1
   no shutdown
   channel-group 16 mode active
   comment
   Comment created from raw_eos_cli under profile TENANT_A
   EOF

!
interface Ethernet17
   description Set using structured_config on server adapter
   no shutdown
   channel-group 17 mode active
   comment
   Comment created from raw_eos_cli under adapter for switch Eth17
   EOF

!
interface Ethernet18
   description SERVER_server-1_Eth5
   no shutdown
   channel-group 18 mode active
   comment
   Comment created from raw_eos_cli under profile NESTED_TENANT_A
   EOF

!
interface Ethernet19
   description SERVER_server-1_Eth7
   no shutdown
   channel-group 19 mode active
   comment
   Comment created from raw_eos_cli under profile NESTED_TENANT_A
   EOF

```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel3 | L2_RACK2_MLAG_Port-Channel1 | trunk | 110-113,1100-1102,2500,2600-2601,4085 | - | - | - | - | 3 | - |
| Port-Channel5 | MLAG_DC1-POD1-LEAF2B_Port-Channel5 | trunk | - | - | MLAG | - | - | - | - |
| Port-Channel16 | PortChannel | access | 110 | - | - | - | - | 16 | - |
| Port-Channel17 | Set using structured_config on server adapter port-channel | access | 110 | - | - | - | - | 17 | - |
| Port-Channel18 | PortChannel | access | 110 | - | - | - | - | 18 | - |
| Port-Channel19 | PortChannel | access | 110 | - | - | - | - | 19 | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel3
   description L2_RACK2_MLAG_Port-Channel1
   no shutdown
   switchport trunk allowed vlan 110-113,1100-1102,2500,2600-2601,4085
   switchport mode trunk
   switchport
   mlag 3
   service-profile QOS-PROFILE
!
interface Port-Channel5
   description MLAG_DC1-POD1-LEAF2B_Port-Channel5
   no shutdown
   switchport mode trunk
   switchport trunk group MLAG
   switchport
   service-profile QOS-PROFILE
!
interface Port-Channel16
   description PortChannel
   no shutdown
   switchport access vlan 110
   switchport mode access
   switchport
   mlag 16
   service-profile bar
!
interface Port-Channel17
   description Set using structured_config on server adapter port-channel
   no shutdown
   switchport access vlan 110
   switchport mode access
   switchport
   mlag 17
   service-profile foo
!
interface Port-Channel18
   description PortChannel
   no shutdown
   switchport access vlan 110
   switchport mode access
   switchport
   mlag 18
   service-profile foo
   comment
   Comment created from raw_eos_cli under port_channel on profile NESTED_TENANT_A
   EOF

!
interface Port-Channel19
   description PortChannel
   no shutdown
   switchport access vlan 110
   switchport mode access
   switchport
   mlag 19
   service-profile foo
   comment
   Comment created from raw_eos_cli under adapter port_channel for switch Po19
   EOF

```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | ROUTER_ID | default | 172.16.110.4/32 |
| Loopback1 | VXLAN_TUNNEL_SOURCE | default | 172.18.110.4/32 |
| Loopback100 | DIAG_VRF_vrf_with_loopbacks_from_overlapping_pool | vrf_with_loopbacks_from_overlapping_pool | 10.100.0.4/32 |
| Loopback101 | DIAG_VRF_vrf_with_loopbacks_from_pod_pools | vrf_with_loopbacks_from_pod_pools | 10.101.101.4/32 |
| Loopback102 | DIAG_VRF_vrf_with_loopbacks_dc1_pod1_only | vrf_with_loopbacks_dc1_pod1_only | 10.102.101.4/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | ROUTER_ID | default | - |
| Loopback1 | VXLAN_TUNNEL_SOURCE | default | - |
| Loopback100 | DIAG_VRF_vrf_with_loopbacks_from_overlapping_pool | vrf_with_loopbacks_from_overlapping_pool | - |
| Loopback101 | DIAG_VRF_vrf_with_loopbacks_from_pod_pools | vrf_with_loopbacks_from_pod_pools | - |
| Loopback102 | DIAG_VRF_vrf_with_loopbacks_dc1_pod1_only | vrf_with_loopbacks_dc1_pod1_only | - |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description ROUTER_ID
   no shutdown
   ip address 172.16.110.4/32
!
interface Loopback1
   description VXLAN_TUNNEL_SOURCE
   no shutdown
   ip address 172.18.110.4/32
!
interface Loopback100
   description DIAG_VRF_vrf_with_loopbacks_from_overlapping_pool
   no shutdown
   vrf vrf_with_loopbacks_from_overlapping_pool
   ip address 10.100.0.4/32
!
interface Loopback101
   description DIAG_VRF_vrf_with_loopbacks_from_pod_pools
   no shutdown
   vrf vrf_with_loopbacks_from_pod_pools
   ip address 10.101.101.4/32
!
interface Loopback102
   description DIAG_VRF_vrf_with_loopbacks_dc1_pod1_only
   no shutdown
   vrf vrf_with_loopbacks_dc1_pod1_only
   ip address 10.102.101.4/32
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan110 | set from structured_config on svi for DC1.POD1.LEAF2A (was Tenant_A_OP_Zone_1) | Common_VRF | - | False |
| Vlan111 | Tenant_A_OP_Zone_2 | Common_VRF | - | True |
| Vlan112 | Tenant_A_OP_Zone_3 | Common_VRF | - | False |
| Vlan113 | SVI_with_no_vxlan | Common_VRF | - | False |
| Vlan1100 | test_svi | vrf_with_loopbacks_from_overlapping_pool | - | False |
| Vlan1101 | test_svi | vrf_with_loopbacks_from_pod_pools | - | False |
| Vlan1102 | test_svi | vrf_with_loopbacks_dc1_pod1_only | - | False |
| Vlan4085 | L2LEAF_INBAND_MGMT | default | - | False |
| Vlan4094 | MLAG | default | - | False |

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
| Vlan4085 |  default  |  172.21.110.2/24  |  -  |  172.21.110.1  |  -  |  -  |
| Vlan4094 |  default  |  172.20.110.2/31  |  -  |  -  |  -  |  -  |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan110
   description set from structured_config on svi for DC1.POD1.LEAF2A (was Tenant_A_OP_Zone_1)
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
!
interface Vlan4085
   description L2LEAF_INBAND_MGMT
   no shutdown
   ip address 172.21.110.2/24
   ip attached-host route export 19
   ip virtual-router address 172.21.110.1
!
interface Vlan4094
   description MLAG
   no shutdown
   no autostate
   ip address 172.20.110.2/31
```

### VXLAN Interface

#### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| Source Interface | Loopback1 |
| UDP port | 4789 |
| EVPN MLAG Shared Router MAC | mlag-system-id |

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
   description DC1.POD1.LEAF2A_VTEP
   vxlan source-interface Loopback1
   vxlan virtual-router encapsulation mac-address mlag-system-id
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
| 65112.100 | 172.16.110.4 |

| BGP Tuning |
| ---------- |
| distance bgp 20 200 200 |
| update wait-install |
| no bgp default ipv4-unicast |
| maximum-paths 4 ecmp 4 |

#### Router BGP Peer Groups

##### EVPN-OVERLAY-CORE

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 15 |
| Send community | all |
| Maximum routes | 0 (no limit) |

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

##### MLAG-IPv4-UNDERLAY-PEER

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65112.100 |
| Next-hop self | True |
| Send community | all |
| Maximum routes | 12000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 100.100.100.201 | 65211 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.16.10.1 | 65101 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 172.16.110.1 | 65110.100 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 172.16.110.3 | 65111.100 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 172.16.120.3 | 65121 | default | - | Inherited from peer group EVPN-OVERLAY-CORE | Inherited from peer group EVPN-OVERLAY-CORE | - | Inherited from peer group EVPN-OVERLAY-CORE | - | - | - | - |
| 172.17.110.8 | 65110.100 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.17.110.10 | 65110.100 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.17.110.12 | 65110.100 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.17.110.14 | 65110.100 | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.20.110.3 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | default | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |

#### Router BGP EVPN Address Family

- VPN import pruning is **enabled**

##### EVPN Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | Encapsulation |
| ---------- | -------- | ------------ | ------------- | ------------- |
| EVPN-OVERLAY-CORE | True |  - | - | default |
| EVPN-OVERLAY-PEERS | True |  - | - | default |

##### EVPN DCI Gateway Summary

| Settings | Value |
| -------- | ----- |
| Remote Domain Peer Groups | EVPN-OVERLAY-CORE |
| L3 Gateway Configured | True |
| L3 Gateway Inter-domain | True |

#### Router BGP VLANs

| VLAN | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute |
| ---- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ |
| 110 | 172.16.110.4:99110 | 99110:99110 | - | - | learned<br>router-mac system |
| 111 | 172.16.110.4:50111 | 50111:50111 | - | - | learned<br>router-mac system |
| 112 | 172.16.110.4:20112 | 20112:20112 | - | - | learned<br>router-mac system |
| 2500 | 172.16.110.4:2500 | 2500:2500 | - | - | learned |
| 2600 | 172.16.110.4:32600 | 32600:32600 | - | - | learned<br>router-mac system |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Common_VRF | 172.16.110.4:1025 | connected |
| vrf_with_loopbacks_dc1_pod1_only | 172.16.110.4:1102 | connected |
| vrf_with_loopbacks_from_overlapping_pool | 172.16.110.4:1100 | connected |
| vrf_with_loopbacks_from_pod_pools | 172.16.110.4:1101 | connected |

#### Router BGP Device Configuration

```eos
!
router bgp 65112.100
   router-id 172.16.110.4
   update wait-install
   no bgp default ipv4-unicast
   maximum-paths 4 ecmp 4
   distance bgp 20 200 200
   neighbor EVPN-OVERLAY-CORE peer group
   neighbor EVPN-OVERLAY-CORE update-source Loopback0
   neighbor EVPN-OVERLAY-CORE bfd
   neighbor EVPN-OVERLAY-CORE ebgp-multihop 15
   neighbor EVPN-OVERLAY-CORE send-community
   neighbor EVPN-OVERLAY-CORE maximum-routes 0
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
   neighbor MLAG-IPv4-UNDERLAY-PEER peer group
   neighbor MLAG-IPv4-UNDERLAY-PEER remote-as 65112.100
   neighbor MLAG-IPv4-UNDERLAY-PEER next-hop-self
   neighbor MLAG-IPv4-UNDERLAY-PEER description DC1-POD1-LEAF2B
   neighbor MLAG-IPv4-UNDERLAY-PEER route-map RM-MLAG-PEER-IN in
   neighbor MLAG-IPv4-UNDERLAY-PEER password 7 <removed>
   neighbor MLAG-IPv4-UNDERLAY-PEER send-community
   neighbor MLAG-IPv4-UNDERLAY-PEER maximum-routes 12000
   neighbor 100.100.100.201 peer group IPv4-UNDERLAY-PEERS
   neighbor 100.100.100.201 remote-as 65211
   neighbor 100.100.100.201 description DC2-POD1-LEAF1A
   neighbor 172.16.10.1 peer group EVPN-OVERLAY-PEERS
   neighbor 172.16.10.1 remote-as 65101
   neighbor 172.16.10.1 description DC1-RS1_Loopback0
   neighbor 172.16.10.1 route-map RM-EVPN-FILTER-AS65101 out
   neighbor 172.16.110.1 peer group EVPN-OVERLAY-PEERS
   neighbor 172.16.110.1 remote-as 65110.100
   neighbor 172.16.110.1 description DC1-POD1-SPINE1_Loopback0
   neighbor 172.16.110.1 route-map RM-EVPN-FILTER-AS65110.100 out
   neighbor 172.16.110.3 peer group EVPN-OVERLAY-PEERS
   neighbor 172.16.110.3 remote-as 65111.100
   neighbor 172.16.110.3 description DC1-POD1-LEAF1A_Loopback0
   neighbor 172.16.110.3 route-map RM-EVPN-FILTER-AS65111.100 out
   neighbor 172.16.120.3 peer group EVPN-OVERLAY-CORE
   neighbor 172.16.120.3 remote-as 65121
   neighbor 172.16.120.3 description DC1-POD2-LEAF1A_Loopback0
   neighbor 172.17.110.8 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.110.8 remote-as 65110.100
   neighbor 172.17.110.8 description DC1-POD1-SPINE1_Ethernet4
   neighbor 172.17.110.10 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.110.10 remote-as 65110.100
   neighbor 172.17.110.10 description DC1-POD1-SPINE2_Ethernet4
   neighbor 172.17.110.12 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.110.12 remote-as 65110.100
   neighbor 172.17.110.12 description DC1-POD1-SPINE1_Ethernet7
   neighbor 172.17.110.14 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.17.110.14 remote-as 65110.100
   neighbor 172.17.110.14 description DC1-POD1-SPINE2_Ethernet7
   neighbor 172.20.110.3 peer group MLAG-IPv4-UNDERLAY-PEER
   neighbor 172.20.110.3 description DC1-POD1-LEAF2B_Vlan4094
   redistribute connected
   redistribute attached-host
   !
   vlan 110
      rd 172.16.110.4:99110
      route-target both 99110:99110
      redistribute learned
      redistribute router-mac system
      !
      comment
      comment created from raw_eos_cli under router bgp svis inherited from svi profile
      EOF

   !
   vlan 111
      rd 172.16.110.4:50111
      route-target both 50111:50111
      redistribute learned
      redistribute router-mac system
      !
      comment
      comment created from raw_eos_cli under router bgp svi 111
      EOF

   !
   vlan 112
      rd 172.16.110.4:20112
      route-target both 20112:20112
      redistribute learned
      redistribute router-mac system
      !
      comment
      comment created from raw_eos_cli under router bgp svis inherited from svi parent profile
      EOF

   !
   vlan 2500
      rd 172.16.110.4:2500
      route-target both 2500:2500
      redistribute learned
   !
   vlan 2600
      rd 172.16.110.4:32600
      route-target both 32600:32600
      redistribute learned
      redistribute router-mac system
      !
      comment
      comment created from raw_eos_cli under router bgp l2vlan 2600
      EOF

   !
   address-family evpn
      neighbor EVPN-OVERLAY-CORE activate
      neighbor EVPN-OVERLAY-CORE domain remote
      neighbor EVPN-OVERLAY-PEERS activate
      route import match-failure action discard
      neighbor default next-hop-self received-evpn-routes route-type ip-prefix inter-domain
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-CORE activate
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
      neighbor MLAG-IPv4-UNDERLAY-PEER activate
   !
   address-family rt-membership
      neighbor EVPN-OVERLAY-CORE activate
      neighbor EVPN-OVERLAY-PEERS activate
   !
   vrf Common_VRF
      rd 172.16.110.4:1025
      route-target import evpn 1025:1025
      route-target export evpn 1025:1025
      router-id 172.16.110.4
      redistribute connected
      !
      comment
      Comment created from raw_eos_cli under BGP for VRF Common_VRF
      EOF

   !
   vrf vrf_with_loopbacks_dc1_pod1_only
      rd 172.16.110.4:1102
      route-target import evpn 1102:1102
      route-target export evpn 1102:1102
      router-id 172.16.110.4
      redistribute connected
   !
   vrf vrf_with_loopbacks_from_overlapping_pool
      rd 172.16.110.4:1100
      route-target import evpn 1100:1100
      route-target export evpn 1100:1100
      router-id 172.16.110.4
      redistribute connected
   !
   vrf vrf_with_loopbacks_from_pod_pools
      rd 172.16.110.4:1101
      route-target import evpn 1101:1101
      route-target export evpn 1101:1101
      router-id 172.16.110.4
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

### Route-maps

#### Route-maps Summary

##### RM-EVPN-FILTER-AS65101

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | deny | as 65101 | - | - | - |
| 20 | permit | - | - | - | - |

##### RM-EVPN-FILTER-AS65110.100

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | deny | as 65110.100 | - | - | - |
| 20 | permit | - | - | - | - |

##### RM-EVPN-FILTER-AS65111.100

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | deny | as 65111.100 | - | - | - |
| 20 | permit | - | - | - | - |

##### RM-MLAG-PEER-IN

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | - | origin incomplete | - | - |

#### Route-maps Device Configuration

```eos
!
route-map RM-EVPN-FILTER-AS65101 deny 10
   match as 65101
!
route-map RM-EVPN-FILTER-AS65101 permit 20
!
route-map RM-EVPN-FILTER-AS65110.100 deny 10
   match as 65110.100
!
route-map RM-EVPN-FILTER-AS65110.100 permit 20
!
route-map RM-EVPN-FILTER-AS65111.100 deny 10
   match as 65111.100
!
route-map RM-EVPN-FILTER-AS65111.100 permit 20
!
route-map RM-MLAG-PEER-IN permit 10
   description Make routes learned over MLAG Peer-link less preferred on spines to ensure optimal routing
   set origin incomplete
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
| vrf_with_loopbacks_dc1_pod1_only | 10.102.101.4 |
| vrf_with_loopbacks_from_overlapping_pool | 10.100.0.4 |
| vrf_with_loopbacks_from_pod_pools | 10.101.101.4 |

### Virtual Source NAT Configuration

```eos
!
ip address virtual source-nat vrf vrf_with_loopbacks_dc1_pod1_only address 10.102.101.4
ip address virtual source-nat vrf vrf_with_loopbacks_from_overlapping_pool address 10.100.0.4
ip address virtual source-nat vrf vrf_with_loopbacks_from_pod_pools address 10.101.101.4
```

## EOS CLI Device Configuration

```eos
!
interface Loopback1002
  description Loopback created from raw_eos_cli under l3leaf node-group RACK2_MLAG

interface Loopback1111
  description Loopback created from raw_eos_cli under platform_settings vEOS-LAB

interface Loopback1000
  description Loopback created from raw_eos_cli under VRF Common_VRF

```
