# DC1-BL1A

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [IP Name Servers](#ip-name-servers)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [Enable Password](#enable-password)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
  - [SNMP](#snmp)
  - [Hardware](#hardware)
- [Hardware TCAM Profile](#hardware-tcam-profile)
  - [Hardware TCAM Device Configuration](#hardware-tcam-device-configuration)
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
- [Queue Monitor](#queue-monitor)
  - [Queue Monitor Length](#queue-monitor-length)
  - [Queue Monitor Configuration](#queue-monitor-configuration)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
- [Filters](#filters)
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Platform](#platform)
  - [Platform Summary](#platform-summary)
  - [Platform Device Configuration](#platform-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | 192.168.200.110/24 | 192.168.200.5 |

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
   ip address 192.168.200.110/24
```

### IP Name Servers

#### IP Name Servers Summary

| Name Server | VRF | Priority |
| ----------- | --- | -------- |
| 192.168.200.5 | MGMT | - |
| 8.8.8.8 | MGMT | - |
| 1.1.1.1 | MGMT | - |

#### IP Name Servers Device Configuration

```eos
ip name-server vrf MGMT 1.1.1.1
ip name-server vrf MGMT 8.8.8.8
ip name-server vrf MGMT 192.168.200.5
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
| cvpadmin | 15 | network-admin | False | - |

#### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin nopassword
username cvpadmin privilege 15 role network-admin secret sha512 <removed>
```

### Enable Password

Enable password has been disabled

## Monitoring

### TerminAttr Daemon

#### TerminAttr Daemon Summary

| CV Compression | CloudVision Servers | VRF | Authentication | Smash Excludes | Ingest Exclude | Bypass AAA |
| -------------- | ------------------- | --- | -------------- | -------------- | -------------- | ---------- |
| gzip | 192.168.200.11:9910 | MGMT | key,telarista | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | False |

#### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvaddr=192.168.200.11:9910 -cvauth=key,<removed> -cvvrf=MGMT -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -taillogs
   no shutdown
```

### SNMP

#### SNMP Configuration Summary

| Contact | Location | SNMP Traps | State |
| ------- | -------- | ---------- | ----- |
| example@example.com | DC1_FABRIC DC1-BL1A | All | Disabled |

#### SNMP Device Configuration

```eos
!
snmp-server contact example@example.com
snmp-server location DC1_FABRIC DC1-BL1A
```

### Hardware

#### Hardware Device Configuration

```eos
!
hardware speed-group 1 serdes 10G
hardware speed-group 2 serdes 25G
hardware speed-group 3 serdes 25G
hardware speed-group 4 serdes 10G
```

## Hardware TCAM Profile

TCAM profile **`vxlan-routing`** is active

### Hardware TCAM Device Configuration

```eos
!
hardware tcam
   system profile vxlan-routing
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **mstp**

STP Root Super: **True**

#### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 4096 |

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
spanning-tree root super
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
| 150 | Tenant_A_WAN_Zone_1 | - |
| 250 | Tenant_B_WAN_Zone_1 | - |
| 350 | Tenant_C_WAN_Zone_1 | - |

### VLANs Device Configuration

```eos
!
vlan 150
   name Tenant_A_WAN_Zone_1
!
vlan 250
   name Tenant_B_WAN_Zone_1
!
vlan 350
   name Tenant_C_WAN_Zone_1
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
| Ethernet10.100 | subinterface test | - | 100 | - |
| Ethernet10.200 | subinterface test with vlan override | - | 121 | - |

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet7 | test | - | 10.10.10.10/24 | Tenant_A_WAN_Zone | 9000 | False | - | - |
| Ethernet8 | test | - | 10.10.10.10/24 | Tenant_L3_VRF_Zone | 9000 | False | - | - |
| Ethernet9 | test | - | 10.10.20.20/24 | Tenant_L3_VRF_Zone | 9000 | False | - | - |
| Ethernet10.100 | subinterface test | - | 10.10.11.10/24 | Tenant_L3_VRF_Zone | 9000 | False | - | - |
| Ethernet10.200 | subinterface test with vlan override | - | 10.10.21.10/24 | Tenant_L3_VRF_Zone | 9000 | False | - | - |
| Ethernet41 | CUSTOM_P2P_LINK_TO_DC1-SPINE1_Ethernet6 | - | 172.31.255.81/31 | default | 1500 | False | - | - |
| Ethernet42 | CUSTOM_P2P_LINK_TO_DC1-SPINE2_Ethernet6 | - | 172.31.255.83/31 | default | 1500 | False | - | - |
| Ethernet43 | CUSTOM_P2P_LINK_TO_DC1-SPINE3_Ethernet6 | - | 172.31.255.85/31 | default | 1500 | False | - | - |
| Ethernet44 | CUSTOM_P2P_LINK_TO_DC1-SPINE4_Ethernet6 | - | 172.31.255.87/31 | default | 1500 | False | - | - |
| Ethernet4000 | My test | - | 10.3.2.1/21 | default | 1500 | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet7
   description test
   no shutdown
   mtu 9000
   no switchport
   vrf Tenant_A_WAN_Zone
   ip address 10.10.10.10/24
!
interface Ethernet8
   description test
   no shutdown
   mtu 9000
   no switchport
   vrf Tenant_L3_VRF_Zone
   ip address 10.10.10.10/24
!
interface Ethernet9
   description test
   no shutdown
   mtu 9000
   no switchport
   vrf Tenant_L3_VRF_Zone
   ip address 10.10.20.20/24
!
interface Ethernet10
   no shutdown
   no switchport
!
interface Ethernet10.100
   description subinterface test
   no shutdown
   mtu 9000
   encapsulation dot1q vlan 100
   vrf Tenant_L3_VRF_Zone
   ip address 10.10.11.10/24
!
interface Ethernet10.200
   description subinterface test with vlan override
   no shutdown
   mtu 9000
   encapsulation dot1q vlan 121
   vrf Tenant_L3_VRF_Zone
   ip address 10.10.21.10/24
!
interface Ethernet41
   description CUSTOM_P2P_LINK_TO_DC1-SPINE1_Ethernet6
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.81/31
!
interface Ethernet42
   description CUSTOM_P2P_LINK_TO_DC1-SPINE2_Ethernet6
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.83/31
!
interface Ethernet43
   description CUSTOM_P2P_LINK_TO_DC1-SPINE3_Ethernet6
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.85/31
!
interface Ethernet44
   description CUSTOM_P2P_LINK_TO_DC1-SPINE4_Ethernet6
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.87/31
!
interface Ethernet4000
   description My test
   no shutdown
   mtu 1500
   no switchport
   ip address 10.3.2.1/21
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | CUSTOM_EVPN_Overlay_Peering_L3LEAF | default | 192.168.255.14/32 |
| Loopback1 | CUSTOM_VTEP_VXLAN_Tunnel_Source_L3LEAF | default | 192.168.254.14/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | CUSTOM_EVPN_Overlay_Peering_L3LEAF | default | - |
| Loopback1 | CUSTOM_VTEP_VXLAN_Tunnel_Source_L3LEAF | default | - |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description CUSTOM_EVPN_Overlay_Peering_L3LEAF
   no shutdown
   ip address 192.168.255.14/32
!
interface Loopback1
   description CUSTOM_VTEP_VXLAN_Tunnel_Source_L3LEAF
   no shutdown
   ip address 192.168.254.14/32
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan150 | Tenant_A_WAN_Zone_1 | Tenant_A_WAN_Zone | - | False |
| Vlan250 | Tenant_B_WAN_Zone_1 | Tenant_B_WAN_Zone | - | False |
| Vlan350 | Tenant_C_WAN_Zone_1 | Tenant_C_WAN_Zone | - | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| Vlan150 |  Tenant_A_WAN_Zone  |  -  |  10.1.40.1/24  |  -  |  -  |  -  |
| Vlan250 |  Tenant_B_WAN_Zone  |  -  |  10.2.50.1/24  |  -  |  -  |  -  |
| Vlan350 |  Tenant_C_WAN_Zone  |  -  |  10.3.50.1/24  |  -  |  -  |  -  |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan150
   description Tenant_A_WAN_Zone_1
   no shutdown
   vrf Tenant_A_WAN_Zone
   ip address virtual 10.1.40.1/24
!
interface Vlan250
   description Tenant_B_WAN_Zone_1
   no shutdown
   vrf Tenant_B_WAN_Zone
   ip address virtual 10.2.50.1/24
!
interface Vlan350
   description Tenant_C_WAN_Zone_1
   no shutdown
   vrf Tenant_C_WAN_Zone
   ip address virtual 10.3.50.1/24
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
| 150 | 10150 | - | - |
| 250 | 20250 | - | - |

##### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| Tenant_A_WAN_Zone | 14 | - |
| Tenant_B_OP_Zone | 20 | - |
| Tenant_B_WAN_Zone | 21 | - |
| Tenant_C_WAN_Zone | 31 | - |
| Tenant_L3_VRF_Zone | 15 | - |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description DC1-BL1A_VTEP
   vxlan source-interface Loopback1
   vxlan udp-port 4789
   vxlan vlan 150 vni 10150
   vxlan vlan 250 vni 20250
   vxlan vrf Tenant_A_WAN_Zone vni 14
   vxlan vrf Tenant_B_OP_Zone vni 20
   vxlan vrf Tenant_B_WAN_Zone vni 21
   vxlan vrf Tenant_C_WAN_Zone vni 31
   vxlan vrf Tenant_L3_VRF_Zone vni 15
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

Virtual Router MAC Address: 00:dc:00:00:00:0a

#### Virtual Router MAC Address Device Configuration

```eos
!
ip virtual-router mac-address 00:dc:00:00:00:0a
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| MGMT | False |
| Tenant_A_WAN_Zone | True |
| Tenant_B_OP_Zone | True |
| Tenant_B_WAN_Zone | True |
| Tenant_C_WAN_Zone | True |
| Tenant_L3_VRF_Zone | True |

#### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
ip routing vrf Tenant_A_WAN_Zone
ip routing vrf Tenant_B_OP_Zone
ip routing vrf Tenant_B_WAN_Zone
ip routing vrf Tenant_C_WAN_Zone
ip routing vrf Tenant_L3_VRF_Zone
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| MGMT | false |
| Tenant_A_WAN_Zone | false |
| Tenant_B_OP_Zone | false |
| Tenant_B_WAN_Zone | false |
| Tenant_C_WAN_Zone | false |
| Tenant_L3_VRF_Zone | false |

### Static Routes

#### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP | Exit interface | Administrative Distance | Tag | Route Name | Metric |
| --- | ------------------ | ----------- | -------------- | ----------------------- | --- | ---------- | ------ |
| MGMT | 0.0.0.0/0 | 192.168.200.5 | - | 1 | - | - | - |
| Tenant_A_WAN_Zone | 10.3.4.0/24 | 1.2.3.4 | - | 1 | - | - | - |
| Tenant_A_WAN_Zone | 1.1.1.0/24 | 10.1.1.1 | vlan101 | 1 | - | - | - |
| Tenant_A_WAN_Zone | 1.1.2.0/24 | 10.1.1.1 | vlan101 | 200 | 666 | RT-TO-FAKE-DMZ | - |
| Tenant_A_WAN_Zone | 10.3.5.0/24 | - | Null0 | 1 | - | - | - |

#### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 192.168.200.5
ip route vrf Tenant_A_WAN_Zone 1.1.1.0/24 Vlan101 10.1.1.1
ip route vrf Tenant_A_WAN_Zone 1.1.2.0/24 Vlan101 10.1.1.1 200 tag 666 name RT-TO-FAKE-DMZ
ip route vrf Tenant_A_WAN_Zone 10.3.4.0/24 1.2.3.4
ip route vrf Tenant_A_WAN_Zone 10.3.5.0/24 Null0
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65104 | 192.168.255.14 |

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
| Ebgp multihop | 3 |
| Send community | all |
| Maximum routes | 0 (no limit) |

##### UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 172.31.255.80 | 65001 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.31.255.82 | 65001 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.31.255.84 | 65001 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.31.255.86 | 65001 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - | - | - | - |
| 192.168.255.1 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.255.2 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.255.3 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.255.4 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 123.1.1.10 | 1234 | Tenant_A_WAN_Zone | - | standard extended | 0 (no limit) | - | - | - | - | - | - |
| 123.1.1.11 | 1234 | Tenant_A_WAN_Zone | - | standard extended | 0 (no limit) | - | - | - | - | - | - |
| fd5a:fe45:8831:06c5::a | 12345 | Tenant_A_WAN_Zone | - | all | - | - | - | - | - | - | - |
| fd5a:fe45:8831:06c5::b | 12345 | Tenant_A_WAN_Zone | - | - | - | - | - | - | - | - | - |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Encapsulation |
| ---------- | -------- | ------------- |
| EVPN-OVERLAY-PEERS | True | default |

##### EVPN Host Flapping Settings

| State | Window | Threshold | Expiry Timeout |
| ----- | ------ | --------- | -------------- |
| Disabled | - | - | - |

#### Router BGP VLAN Aware Bundles

| VLAN Aware Bundle | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute | VLANs |
| ----------------- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ | ----- |
| Tenant_A_WAN_Zone | 192.168.255.14:14 | 14:14 | - | - | learned | 150 |
| Tenant_B_WAN_Zone | 192.168.255.14:21 | 21:21 | - | - | learned | 250 |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Tenant_A_WAN_Zone | 192.168.255.14:14 | connected<br>static |
| Tenant_B_OP_Zone | 192.168.255.14:20 | connected |
| Tenant_B_WAN_Zone | 192.168.255.14:21 | connected |
| Tenant_C_WAN_Zone | 192.168.255.14:31 | connected |
| Tenant_L3_VRF_Zone | 192.168.255.14:15 | connected |

#### Router BGP Device Configuration

```eos
!
router bgp 65104
   router-id 192.168.255.14
   update wait-install
   no bgp default ipv4-unicast
   maximum-paths 4 ecmp 4
   distance bgp 20 200 200
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS password 7 <removed>
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor UNDERLAY-PEERS peer group
   neighbor UNDERLAY-PEERS password 7 <removed>
   neighbor UNDERLAY-PEERS send-community
   neighbor UNDERLAY-PEERS maximum-routes 12000
   neighbor 172.31.255.80 peer group UNDERLAY-PEERS
   neighbor 172.31.255.80 remote-as 65001
   neighbor 172.31.255.80 description DC1-SPINE1_Ethernet6
   neighbor 172.31.255.82 peer group UNDERLAY-PEERS
   neighbor 172.31.255.82 remote-as 65001
   neighbor 172.31.255.82 description DC1-SPINE2_Ethernet6
   neighbor 172.31.255.84 peer group UNDERLAY-PEERS
   neighbor 172.31.255.84 remote-as 65001
   neighbor 172.31.255.84 description DC1-SPINE3_Ethernet6
   neighbor 172.31.255.86 peer group UNDERLAY-PEERS
   neighbor 172.31.255.86 remote-as 65001
   neighbor 172.31.255.86 description DC1-SPINE4_Ethernet6
   neighbor 192.168.255.1 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.1 remote-as 65001
   neighbor 192.168.255.1 description DC1-SPINE1_Loopback0
   neighbor 192.168.255.2 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.2 remote-as 65001
   neighbor 192.168.255.2 description DC1-SPINE2_Loopback0
   neighbor 192.168.255.3 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.3 remote-as 65001
   neighbor 192.168.255.3 description DC1-SPINE3_Loopback0
   neighbor 192.168.255.4 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.4 remote-as 65001
   neighbor 192.168.255.4 description DC1-SPINE4_Loopback0
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan-aware-bundle Tenant_A_WAN_Zone
      rd 192.168.255.14:14
      route-target both 14:14
      redistribute learned
      vlan 150
   !
   vlan-aware-bundle Tenant_B_WAN_Zone
      rd 192.168.255.14:21
      route-target both 21:21
      redistribute learned
      vlan 250
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
      no host-flap detection
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor UNDERLAY-PEERS activate
   !
   vrf Tenant_A_WAN_Zone
      rd 192.168.255.14:14
      route-target import evpn 14:14
      route-target import evpn 65000:456
      route-target import vpn-ipv4 65000:123
      route-target export evpn 14:14
      route-target export evpn 65000:789
      route-target export vpn-ipv4 65000:123
      router-id 192.168.255.14
      update wait-install
      neighbor 123.1.1.10 remote-as 1234
      neighbor 123.1.1.10 local-as 123 no-prepend replace-as
      neighbor 123.1.1.10 update-source Loopback123
      neighbor 123.1.1.10 description External IPv4 BGP peer
      neighbor 123.1.1.10 ebgp-multihop 3
      neighbor 123.1.1.10 route-map RM-123-1-1-10-IN in
      neighbor 123.1.1.10 route-map RM-Tenant_A_WAN_Zone-123.1.1.10-SET-NEXT-HOP-OUT out
      neighbor 123.1.1.10 password 7 <removed>
      neighbor 123.1.1.10 default-originate route-map RM-Tenant_A_WAN_Zone-123.1.1.10-SET-NEXT-HOP-OUT
      neighbor 123.1.1.10 send-community standard extended
      neighbor 123.1.1.10 maximum-routes 0
      neighbor 123.1.1.11 remote-as 1234
      neighbor 123.1.1.11 local-as 123 no-prepend replace-as
      neighbor 123.1.1.11 update-source Loopback123
      neighbor 123.1.1.11 description External IPv4 BGP peer
      neighbor 123.1.1.11 ebgp-multihop 3
      neighbor 123.1.1.11 route-map RM-123-1-1-11-IN in
      neighbor 123.1.1.11 route-map RM-123-1-1-11-OUT out
      neighbor 123.1.1.11 password 7 <removed>
      neighbor 123.1.1.11 default-originate
      neighbor 123.1.1.11 send-community standard extended
      neighbor 123.1.1.11 maximum-routes 0
      neighbor fd5a:fe45:8831:06c5::a remote-as 12345
      neighbor fd5a:fe45:8831:06c5::a route-map RM-Tenant_A_WAN_Zone-fd5a:fe45:8831:06c5::a-SET-NEXT-HOP-OUT out
      neighbor fd5a:fe45:8831:06c5::a send-community
      neighbor fd5a:fe45:8831:06c5::b remote-as 12345
      redistribute connected
      redistribute static
      !
      address-family ipv4
         neighbor 123.1.1.10 activate
         neighbor 123.1.1.11 activate
      !
      address-family ipv6
         neighbor fd5a:fe45:8831:06c5::a activate
         neighbor fd5a:fe45:8831:06c5::b activate
   !
   vrf Tenant_B_OP_Zone
      rd 192.168.255.14:20
      route-target import evpn 20:20
      route-target export evpn 20:20
      router-id 192.168.255.14
      redistribute connected
   !
   vrf Tenant_B_WAN_Zone
      rd 192.168.255.14:21
      route-target import evpn 21:21
      route-target export evpn 21:21
      router-id 192.168.255.14
      redistribute connected
   !
   vrf Tenant_C_WAN_Zone
      rd 192.168.255.14:31
      route-target import evpn 31:31
      route-target export evpn 31:31
      router-id 192.168.255.14
      redistribute connected
   !
   vrf Tenant_L3_VRF_Zone
      rd 192.168.255.14:15
      route-target import evpn 15:15
      route-target export evpn 15:15
      router-id 192.168.255.14
      redistribute connected
```

## BFD

### Router BFD

#### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 1200 | 1200 | 3 |

#### Router BFD Device Configuration

```eos
!
router bfd
   multihop interval 1200 min-rx 1200 multiplier 3
```

## Queue Monitor

### Queue Monitor Length

| Enabled | Logging Interval | Default Thresholds High | Default Thresholds Low | Notifying | TX Latency | CPU Thresholds High | CPU Thresholds Low |
| ------- | ---------------- | ----------------------- | ---------------------- | --------- | ---------- | ------------------- | ------------------ |
| True | 5 | - | - | enabled | disabled | - | - |

### Queue Monitor Configuration

```eos
!
queue-monitor length
queue-monitor length notifying
!
queue-monitor length log 5
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
| 10 | permit 192.168.255.0/24 eq 32 |
| 20 | permit 192.168.254.0/24 eq 32 |

#### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 192.168.255.0/24 eq 32
   seq 20 permit 192.168.254.0/24 eq 32
```

### Route-maps

#### Route-maps Summary

##### RM-CONN-2-BGP

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY | - | - | - |

##### RM-Tenant_A_WAN_Zone-123.1.1.10-SET-NEXT-HOP-OUT

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | - | ip next-hop 123.1.1.1 | - | - |

##### RM-Tenant_A_WAN_Zone-fd5a:fe45:8831:06c5::a-SET-NEXT-HOP-OUT

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | - | ipv6 next-hop fd5a:fe45:8831:06c5::1 | - | - |

#### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
!
route-map RM-Tenant_A_WAN_Zone-123.1.1.10-SET-NEXT-HOP-OUT permit 10
   set ip next-hop 123.1.1.1
!
route-map RM-Tenant_A_WAN_Zone-fd5a:fe45:8831:06c5::a-SET-NEXT-HOP-OUT permit 10
   set ipv6 next-hop fd5a:fe45:8831:06c5::1
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT | disabled |
| Tenant_A_WAN_Zone | enabled |
| Tenant_B_OP_Zone | enabled |
| Tenant_B_WAN_Zone | enabled |
| Tenant_C_WAN_Zone | enabled |
| Tenant_L3_VRF_Zone | enabled |

### VRF Instances Device Configuration

```eos
!
vrf instance MGMT
!
vrf instance Tenant_A_WAN_Zone
!
vrf instance Tenant_B_OP_Zone
!
vrf instance Tenant_B_WAN_Zone
!
vrf instance Tenant_C_WAN_Zone
!
vrf instance Tenant_L3_VRF_Zone
```

## Platform

### Platform Summary

#### Platform Sand Summary

| Settings | Value |
| -------- | ----- |
| Hardware Only Lag | True |

### Platform Device Configuration

```eos
!
platform sand lag hardware-only
```
