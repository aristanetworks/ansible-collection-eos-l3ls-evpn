# DC1-SVC3A

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
- [Virtual Source NAT](#virtual-source-nat)
  - [Virtual Source NAT Summary](#virtual-source-nat-summary)
  - [Virtual Source NAT Configuration](#virtual-source-nat-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | 192.168.200.108/24 | 192.168.200.5 |

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
   ip address 192.168.200.108/24
```

### IP Name Servers

#### IP Name Servers Summary

| Name Server | VRF | Priority |
| ----------- | --- | -------- |
| 192.168.200.5 | MGMT | - |
| 8.8.8.8 | MGMT | - |

#### IP Name Servers Device Configuration

```eos
ip name-server vrf MGMT 8.8.8.8
ip name-server vrf MGMT 192.168.200.5
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
| 192.168.200.5 | MGMT | True | - | - | - | - | - | - | - |

#### NTP Device Configuration

```eos
!
ntp local-interface vrf MGMT Management1
ntp server vrf MGMT 192.168.200.5 prefer
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
| example@example.com | DC1_FABRIC DC1-SVC3A | All | Disabled |

#### SNMP Device Configuration

```eos
!
snmp-server contact example@example.com
snmp-server location DC1_FABRIC DC1-SVC3A
```

## MLAG

### MLAG Summary

| Domain-id | Local-interface | Peer-address | Peer-link |
| --------- | --------------- | ------------ | --------- |
| DC1_SVC3 | Vlan4092 | 10.255.252.7 | Port-Channel5 |

Dual primary detection is disabled.

### MLAG Device Configuration

```eos
!
mlag configuration
   domain-id DC1_SVC3
   local-interface Vlan4092
   peer-address 10.255.252.7
   peer-link Port-Channel5
   reload-delay mlag 300
   reload-delay non-mlag 330
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **mstp**

STP Root Super: **True**

#### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 4096 |

#### Global Spanning-Tree Settings

- Spanning Tree disabled for VLANs: **4092**

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
no spanning-tree vlan-id 4092
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
| 2 | MLAG_L3_VRF_Tenant_C_OP_Zone | MLAG |
| 110 | Tenant_A_OP_Zone_1 | - |
| 111 | Tenant_A_OP_Zone_2 | - |
| 120 | Tenant_A_WEB_Zone_1 | - |
| 121 | Tenant_A_WEBZone_2 | - |
| 122 | Tenant_a_WEB_DHCP_no_source_int_no_vrf | - |
| 123 | Tenant_a_WEB_DHCP_source_int_no_vrf | - |
| 124 | Tenant_a_WEB_DHCP_vrf_no_source_int | - |
| 130 | Tenant_A_APP_Zone_1 | - |
| 131 | Tenant_A_APP_Zone_2 | - |
| 140 | Tenant_A_DB_BZone_1 | - |
| 141 | Tenant_A_DB_Zone_2 | - |
| 150 | Tenant_A_WAN_Zone_1 | - |
| 160 | Tenant_A_VMOTION | - |
| 161 | Tenant_A_NFS | - |
| 162 | Tenant_A_FTP | - |
| 210 | Tenant_B_OP_Zone_1 | - |
| 211 | Tenant_B_OP_Zone_2 | - |
| 250 | Tenant_B_WAN_Zone_1 | - |
| 310 | Tenant_C_OP_Zone_1 | - |
| 311 | Tenant_C_OP_Zone_2 | - |
| 350 | Tenant_C_WAN_Zone_1 | - |
| 3009 | MLAG_L3_VRF_Tenant_A_OP_Zone | MLAG |
| 3010 | MLAG_L3_VRF_Tenant_A_WEB_Zone | MLAG |
| 3011 | MLAG_L3_VRF_Tenant_A_APP_Zone | MLAG |
| 3012 | MLAG_L3_VRF_Tenant_A_DB_Zone | MLAG |
| 3013 | MLAG_L3_VRF_Tenant_A_WAN_Zone | MLAG |
| 3019 | MLAG_L3_VRF_Tenant_B_OP_Zone | MLAG |
| 3020 | MLAG_L3_VRF_Tenant_B_WAN_Zone | MLAG |
| 3030 | MLAG_L3_VRF_Tenant_C_WAN_Zone | MLAG |
| 4092 | MLAG | MLAG |

### VLANs Device Configuration

```eos
!
vlan 2
   name MLAG_L3_VRF_Tenant_C_OP_Zone
   trunk group MLAG
!
vlan 110
   name Tenant_A_OP_Zone_1
!
vlan 111
   name Tenant_A_OP_Zone_2
!
vlan 120
   name Tenant_A_WEB_Zone_1
!
vlan 121
   name Tenant_A_WEBZone_2
!
vlan 122
   name Tenant_a_WEB_DHCP_no_source_int_no_vrf
!
vlan 123
   name Tenant_a_WEB_DHCP_source_int_no_vrf
!
vlan 124
   name Tenant_a_WEB_DHCP_vrf_no_source_int
!
vlan 130
   name Tenant_A_APP_Zone_1
!
vlan 131
   name Tenant_A_APP_Zone_2
!
vlan 140
   name Tenant_A_DB_BZone_1
!
vlan 141
   name Tenant_A_DB_Zone_2
!
vlan 150
   name Tenant_A_WAN_Zone_1
!
vlan 160
   name Tenant_A_VMOTION
!
vlan 161
   name Tenant_A_NFS
!
vlan 162
   name Tenant_A_FTP
!
vlan 210
   name Tenant_B_OP_Zone_1
!
vlan 211
   name Tenant_B_OP_Zone_2
!
vlan 250
   name Tenant_B_WAN_Zone_1
!
vlan 310
   name Tenant_C_OP_Zone_1
!
vlan 311
   name Tenant_C_OP_Zone_2
!
vlan 350
   name Tenant_C_WAN_Zone_1
!
vlan 3009
   name MLAG_L3_VRF_Tenant_A_OP_Zone
   trunk group MLAG
!
vlan 3010
   name MLAG_L3_VRF_Tenant_A_WEB_Zone
   trunk group MLAG
!
vlan 3011
   name MLAG_L3_VRF_Tenant_A_APP_Zone
   trunk group MLAG
!
vlan 3012
   name MLAG_L3_VRF_Tenant_A_DB_Zone
   trunk group MLAG
!
vlan 3013
   name MLAG_L3_VRF_Tenant_A_WAN_Zone
   trunk group MLAG
!
vlan 3019
   name MLAG_L3_VRF_Tenant_B_OP_Zone
   trunk group MLAG
!
vlan 3020
   name MLAG_L3_VRF_Tenant_B_WAN_Zone
   trunk group MLAG
!
vlan 3030
   name MLAG_L3_VRF_Tenant_C_WAN_Zone
   trunk group MLAG
!
vlan 4092
   name MLAG
   trunk group MLAG
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet5 | CUSTOM_MLAG_PEER_DC1-SVC3B_Ethernet5 | *trunk | *- | *- | *MLAG | 5 |
| Ethernet6 | CUSTOM_MLAG_PEER_DC1-SVC3B_Ethernet6 | *trunk | *- | *- | *MLAG | 5 |
| Ethernet7 | CUSTOM_DC1-L2LEAF2A_Ethernet1 | *trunk | *110-111,120-124,130-131,140-141,150,160-162,210-211,250,310-311,350 | *- | *- | 7 |
| Ethernet8 | CUSTOM_DC1-L2LEAF2B_Ethernet1 | *trunk | *110-111,120-124,130-131,140-141,150,160-162,210-211,250,310-311,350 | *- | *- | 7 |
| Ethernet10 | CUSTOM_server03_ESI_Eth1 | *trunk | *110-111,210-211 | *- | *- | 10 |
| Ethernet11 | CUSTOM_server04_inherit_all_from_profile_Eth1 | trunk | 1-4094 | - | - | - |
| Ethernet12 | CUSTOM_server05_no_profile_Eth1 | trunk | 1-4094 | - | - | - |
| Ethernet13 | CUSTOM_server06_override_profile_Eth1 | access | 210 | - | - | - |
| Ethernet14 | CUSTOM_server07_inherit_all_from_profile_port_channel_Eth1 | *trunk | *1-4094 | *- | *- | 14 |
| Ethernet15 | CUSTOM_server08_no_profile_port_channel_Eth1 | *trunk | *1-4094 | *- | *- | 15 |
| Ethernet16 | CUSTOM_server09_override_profile_no_port_channel_Eth1 | access | 210 | - | - | - |
| Ethernet17 | CUSTOM_server10_no_profile_port_channel_lacp_fallback_Eth1 | *trunk | *1-4094 | *- | *- | 17 |
| Ethernet18 | CUSTOM_server11_inherit_profile_port_channel_lacp_fallback_Eth1 | *trunk | *1-4094 | *- | *- | 18 |
| Ethernet19 | CUSTOM_server12_inherit_nested_profile_port_channel_lacp_fallback_Eth1 | *trunk | *1-4094 | *- | *- | 19 |
| Ethernet20 | CUSTOM_server13_disabled_interfaces_Eth1 | access | 110 | - | - | - |
| Ethernet21 | CUSTOM_server14_explicitly_enabled_interfaces_Eth1 | access | 110 | - | - | - |
| Ethernet22 | CUSTOM_server15_port_channel_disabled_interfaces_Eth1 | *access | *110 | *- | *- | 22 |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet41 | CUSTOM_P2P_LINK_TO_DC1-SPINE1_Ethernet4 | - | 172.31.255.49/31 | default | 1500 | False | - | - |
| Ethernet42 | CUSTOM_P2P_LINK_TO_DC1-SPINE2_Ethernet4 | - | 172.31.255.51/31 | default | 1500 | False | - | - |
| Ethernet43 | CUSTOM_P2P_LINK_TO_DC1-SPINE3_Ethernet4 | - | 172.31.255.53/31 | default | 1500 | False | - | - |
| Ethernet44 | CUSTOM_P2P_LINK_TO_DC1-SPINE4_Ethernet4 | - | 172.31.255.55/31 | default | 1500 | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet5
   description CUSTOM_MLAG_PEER_DC1-SVC3B_Ethernet5
   no shutdown
   channel-group 5 mode active
!
interface Ethernet6
   description CUSTOM_MLAG_PEER_DC1-SVC3B_Ethernet6
   no shutdown
   channel-group 5 mode active
!
interface Ethernet7
   description CUSTOM_DC1-L2LEAF2A_Ethernet1
   no shutdown
   channel-group 7 mode active
!
interface Ethernet8
   description CUSTOM_DC1-L2LEAF2B_Ethernet1
   no shutdown
   channel-group 7 mode active
!
interface Ethernet10
   description CUSTOM_server03_ESI_Eth1
   no shutdown
   channel-group 10 mode active
!
interface Ethernet11
   description CUSTOM_server04_inherit_all_from_profile_Eth1
   no shutdown
   l2 mtu 8000
   switchport trunk allowed vlan 1-4094
   switchport mode trunk
   switchport
   storm-control broadcast level pps 100
   storm-control multicast level 1
   storm-control unknown-unicast level 2
   storm-control all level 10
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet12
   description CUSTOM_server05_no_profile_Eth1
   no shutdown
   switchport trunk allowed vlan 1-4094
   switchport mode trunk
   switchport
   storm-control broadcast level pps 100
   storm-control multicast level 1
   storm-control unknown-unicast level 2
   storm-control all level 10
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Ethernet13
   description CUSTOM_server06_override_profile_Eth1
   no shutdown
   l2 mtu 8000
   switchport access vlan 210
   switchport mode access
   switchport
   storm-control broadcast level 200
   storm-control multicast level 1
   storm-control unknown-unicast level 2
   storm-control all level pps 20
   spanning-tree portfast network
   spanning-tree bpduguard enable
!
interface Ethernet14
   description CUSTOM_server07_inherit_all_from_profile_port_channel_Eth1
   no shutdown
   channel-group 14 mode active
!
interface Ethernet15
   description CUSTOM_server08_no_profile_port_channel_Eth1
   no shutdown
   channel-group 15 mode on
!
interface Ethernet16
   description CUSTOM_server09_override_profile_no_port_channel_Eth1
   no shutdown
   l2 mtu 8000
   switchport access vlan 210
   switchport mode access
   switchport
   storm-control broadcast level 200
   storm-control multicast level 1
   storm-control unknown-unicast level 2
   storm-control all level pps 20
   spanning-tree portfast network
   spanning-tree bpduguard enable
!
interface Ethernet17
   description CUSTOM_server10_no_profile_port_channel_lacp_fallback_Eth1
   no shutdown
   channel-group 17 mode active
   lacp port-priority 8192
!
interface Ethernet18
   description CUSTOM_server11_inherit_profile_port_channel_lacp_fallback_Eth1
   no shutdown
   channel-group 18 mode active
   lacp port-priority 8192
!
interface Ethernet19
   description CUSTOM_server12_inherit_nested_profile_port_channel_lacp_fallback_Eth1
   no shutdown
   channel-group 19 mode active
   lacp port-priority 8192
!
interface Ethernet20
   description CUSTOM_server13_disabled_interfaces_Eth1
   shutdown
   switchport access vlan 110
   switchport mode access
   switchport
!
interface Ethernet21
   description CUSTOM_server14_explicitly_enabled_interfaces_Eth1
   no shutdown
   switchport access vlan 110
   switchport mode access
   switchport
!
interface Ethernet22
   description CUSTOM_server15_port_channel_disabled_interfaces_Eth1
   shutdown
   channel-group 22 mode active
!
interface Ethernet41
   description CUSTOM_P2P_LINK_TO_DC1-SPINE1_Ethernet4
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.49/31
!
interface Ethernet42
   description CUSTOM_P2P_LINK_TO_DC1-SPINE2_Ethernet4
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.51/31
!
interface Ethernet43
   description CUSTOM_P2P_LINK_TO_DC1-SPINE3_Ethernet4
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.53/31
!
interface Ethernet44
   description CUSTOM_P2P_LINK_TO_DC1-SPINE4_Ethernet4
   no shutdown
   mtu 1500
   speed forced 100gfull
   no switchport
   ip address 172.31.255.55/31
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel5 | CUSTOM_MLAG_PEER_DC1-SVC3B_Po5 | trunk | - | - | MLAG | - | - | - | - |
| Port-Channel7 | CUSTOM_DC1-L2LEAF2A_Po1 | trunk | 110-111,120-124,130-131,140-141,150,160-162,210-211,250,310-311,350 | - | - | - | - | 7 | - |
| Port-Channel10 | CUSTOM_server03_ESI_PortChanne1 | trunk | 110-111,210-211 | - | - | - | - | - | 0000:1234:0303:0202:0101 |
| Port-Channel14 | CUSTOM_server07_inherit_all_from_profile_port_channel_ALL_WITH_SECURITY_PORT_CHANNEL | trunk | 1-4094 | - | - | - | - | 14 | - |
| Port-Channel15 | CUSTOM_server08_no_profile_port_channel_server08_no_profile_port_channel | trunk | 1-4094 | - | - | - | - | 15 | - |
| Port-Channel17 | CUSTOM_server10_no_profile_port_channel_lacp_fallback_server10_no_profile_port_channel_lacp_fallback | trunk | 1-4094 | - | - | 90 | static | 17 | - |
| Port-Channel18 | CUSTOM_server11_inherit_profile_port_channel_lacp_fallback_ALL_WITH_SECURITY_PORT_CHANNEL | trunk | 1-4094 | - | - | 10 | static | 18 | - |
| Port-Channel19 | CUSTOM_server12_inherit_nested_profile_port_channel_lacp_fallback_NESTED_ALL_WITH_SECURITY_PORT_CHANNEL | trunk | 1-4094 | - | - | 10 | static | 19 | - |
| Port-Channel22 | CUSTOM_server15_port_channel_disabled_interfaces_ | access | 110 | - | - | - | - | 22 | - |

##### EVPN Multihoming

####### EVPN Multihoming Summary

| Interface | Ethernet Segment Identifier | Multihoming Redundancy Mode | Route Target |
| --------- | --------------------------- | --------------------------- | ------------ |
| Port-Channel10 | 0000:1234:0303:0202:0101 | all-active | 03:03:02:02:01:01 |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel5
   description CUSTOM_MLAG_PEER_DC1-SVC3B_Po5
   no shutdown
   switchport mode trunk
   switchport trunk group MLAG
   switchport
!
interface Port-Channel7
   description CUSTOM_DC1-L2LEAF2A_Po1
   no shutdown
   switchport trunk allowed vlan 110-111,120-124,130-131,140-141,150,160-162,210-211,250,310-311,350
   switchport mode trunk
   switchport
   mlag 7
!
interface Port-Channel10
   description CUSTOM_server03_ESI_PortChanne1
   no shutdown
   switchport trunk allowed vlan 110-111,210-211
   switchport mode trunk
   switchport
   !
   evpn ethernet-segment
      identifier 0000:1234:0303:0202:0101
      route-target import 03:03:02:02:01:01
   lacp system-id 0303.0202.0101
!
interface Port-Channel14
   description CUSTOM_server07_inherit_all_from_profile_port_channel_ALL_WITH_SECURITY_PORT_CHANNEL
   no shutdown
   switchport trunk allowed vlan 1-4094
   switchport mode trunk
   switchport
   l2 mtu 8000
   mlag 14
   storm-control broadcast level pps 100
   storm-control multicast level 1
   storm-control unknown-unicast level 2
   storm-control all level 10
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Port-Channel15
   description CUSTOM_server08_no_profile_port_channel_server08_no_profile_port_channel
   no shutdown
   switchport trunk allowed vlan 1-4094
   switchport mode trunk
   switchport
   mlag 15
   storm-control broadcast level pps 100
   storm-control multicast level 1
   storm-control unknown-unicast level 2
   storm-control all level 10
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Port-Channel17
   description CUSTOM_server10_no_profile_port_channel_lacp_fallback_server10_no_profile_port_channel_lacp_fallback
   no shutdown
   switchport trunk allowed vlan 1-4094
   switchport mode trunk
   switchport
   port-channel lacp fallback static
   port-channel lacp fallback timeout 90
   mlag 17
   storm-control broadcast level pps 100
   storm-control multicast level 1
   storm-control unknown-unicast level 2
   storm-control all level 10
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Port-Channel18
   description CUSTOM_server11_inherit_profile_port_channel_lacp_fallback_ALL_WITH_SECURITY_PORT_CHANNEL
   no shutdown
   switchport trunk allowed vlan 1-4094
   switchport mode trunk
   switchport
   port-channel lacp fallback static
   port-channel lacp fallback timeout 10
   l2 mtu 8000
   mlag 18
   storm-control broadcast level pps 100
   storm-control multicast level 1
   storm-control unknown-unicast level 2
   storm-control all level 10
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Port-Channel19
   description CUSTOM_server12_inherit_nested_profile_port_channel_lacp_fallback_NESTED_ALL_WITH_SECURITY_PORT_CHANNEL
   no shutdown
   switchport trunk allowed vlan 1-4094
   switchport mode trunk
   switchport
   port-channel lacp fallback static
   port-channel lacp fallback timeout 10
   l2 mtu 8000
   mlag 19
   storm-control broadcast level pps 100
   storm-control multicast level 1
   storm-control unknown-unicast level 2
   storm-control all level 10
   spanning-tree portfast
   spanning-tree bpdufilter enable
!
interface Port-Channel22
   description CUSTOM_server15_port_channel_disabled_interfaces_
   no shutdown
   switchport access vlan 110
   switchport mode access
   switchport
   mlag 22
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | CUSTOM_EVPN_Overlay_Peering_L3LEAF | default | 192.168.255.12/32 |
| Loopback1 | CUSTOM_VTEP_VXLAN_Tunnel_Source_L3LEAF | default | 192.168.254.12/32 |
| Loopback100 | CUSTOM_VTEP_DIAGNOSTICS_LOOPBACK_DESC | Tenant_A_OP_Zone | 10.255.1.12/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | CUSTOM_EVPN_Overlay_Peering_L3LEAF | default | - |
| Loopback1 | CUSTOM_VTEP_VXLAN_Tunnel_Source_L3LEAF | default | - |
| Loopback100 | CUSTOM_VTEP_DIAGNOSTICS_LOOPBACK_DESC | Tenant_A_OP_Zone | - |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description CUSTOM_EVPN_Overlay_Peering_L3LEAF
   no shutdown
   ip address 192.168.255.12/32
!
interface Loopback1
   description CUSTOM_VTEP_VXLAN_Tunnel_Source_L3LEAF
   no shutdown
   ip address 192.168.254.12/32
!
interface Loopback100
   description CUSTOM_VTEP_DIAGNOSTICS_LOOPBACK_DESC
   no shutdown
   vrf Tenant_A_OP_Zone
   ip address 10.255.1.12/32
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan2 | MLAG_L3_VRF_Tenant_C_OP_Zone | Tenant_C_OP_Zone | 1500 | False |
| Vlan110 | SVI 110 CUSTOM DESCRIPTION | Tenant_A_OP_Zone | - | False |
| Vlan111 | SVI 111 CUSTOM DESCRIPTION | Tenant_A_OP_Zone | - | False |
| Vlan120 | Tenant_A_WEB_Zone_1 | Tenant_A_WEB_Zone | - | False |
| Vlan121 | Tenant_A_WEBZone_2 | Tenant_A_WEB_Zone | 1560 | True |
| Vlan122 | Tenant_a_WEB_DHCP_no_source_int_no_vrf | Tenant_A_WEB_Zone | - | False |
| Vlan123 | Tenant_a_WEB_DHCP_source_int_no_vrf | Tenant_A_WEB_Zone | - | False |
| Vlan124 | Tenant_a_WEB_DHCP_vrf_no_source_int | Tenant_A_WEB_Zone | - | False |
| Vlan130 | Tenant_A_APP_Zone_1 | Tenant_A_APP_Zone | - | False |
| Vlan131 | Tenant_A_APP_Zone_2 | Tenant_A_APP_Zone | - | False |
| Vlan140 | Tenant_A_DB_BZone_1 | Tenant_A_DB_Zone | - | False |
| Vlan141 | Tenant_A_DB_Zone_2 | Tenant_A_DB_Zone | - | False |
| Vlan150 | Tenant_A_WAN_Zone_1 | Tenant_A_WAN_Zone | - | False |
| Vlan210 | Tenant_B_OP_Zone_1 | Tenant_B_OP_Zone | - | False |
| Vlan211 | Tenant_B_OP_Zone_2 | Tenant_B_OP_Zone | - | False |
| Vlan250 | Tenant_B_WAN_Zone_1 | Tenant_B_WAN_Zone | - | False |
| Vlan310 | Tenant_C_OP_Zone_1 | Tenant_C_OP_Zone | - | False |
| Vlan311 | Tenant_C_OP_Zone_2 | Tenant_C_OP_Zone | - | False |
| Vlan350 | Tenant_C_WAN_Zone_1 | Tenant_C_WAN_Zone | - | False |
| Vlan3009 | MLAG_L3_VRF_Tenant_A_OP_Zone | Tenant_A_OP_Zone | 1500 | False |
| Vlan3010 | MLAG_L3_VRF_Tenant_A_WEB_Zone | Tenant_A_WEB_Zone | 1500 | False |
| Vlan3011 | MLAG_L3_VRF_Tenant_A_APP_Zone | Tenant_A_APP_Zone | 1500 | False |
| Vlan3012 | MLAG_L3_VRF_Tenant_A_DB_Zone | Tenant_A_DB_Zone | 1500 | False |
| Vlan3013 | MLAG_L3_VRF_Tenant_A_WAN_Zone | Tenant_A_WAN_Zone | 1500 | False |
| Vlan3019 | MLAG_L3_VRF_Tenant_B_OP_Zone | Tenant_B_OP_Zone | 1500 | False |
| Vlan3020 | MLAG_L3_VRF_Tenant_B_WAN_Zone | Tenant_B_WAN_Zone | 1500 | False |
| Vlan3030 | MLAG_L3_VRF_Tenant_C_WAN_Zone | Tenant_C_WAN_Zone | 1500 | False |
| Vlan4092 | MLAG | default | 1500 | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| Vlan2 |  Tenant_C_OP_Zone  |  10.255.252.6/31  |  -  |  -  |  -  |  -  |
| Vlan110 |  Tenant_A_OP_Zone  |  -  |  10.1.10.1/24  |  -  |  -  |  -  |
| Vlan111 |  Tenant_A_OP_Zone  |  -  |  10.1.11.1/24  |  -  |  -  |  -  |
| Vlan120 |  Tenant_A_WEB_Zone  |  -  |  10.1.20.1/24  |  -  |  -  |  -  |
| Vlan121 |  Tenant_A_WEB_Zone  |  -  |  10.1.10.254/24  |  -  |  -  |  -  |
| Vlan122 |  Tenant_A_WEB_Zone  |  -  |  10.1.22.1/24  |  -  |  -  |  -  |
| Vlan123 |  Tenant_A_WEB_Zone  |  -  |  10.1.23.1/24  |  -  |  -  |  -  |
| Vlan124 |  Tenant_A_WEB_Zone  |  -  |  10.1.24.1/24  |  -  |  -  |  -  |
| Vlan130 |  Tenant_A_APP_Zone  |  -  |  10.1.30.1/24  |  -  |  -  |  -  |
| Vlan131 |  Tenant_A_APP_Zone  |  -  |  10.1.31.1/24  |  -  |  -  |  -  |
| Vlan140 |  Tenant_A_DB_Zone  |  -  |  10.1.40.1/24  |  -  |  -  |  -  |
| Vlan141 |  Tenant_A_DB_Zone  |  -  |  10.1.41.1/24  |  -  |  -  |  -  |
| Vlan150 |  Tenant_A_WAN_Zone  |  -  |  10.1.40.1/24  |  -  |  -  |  -  |
| Vlan210 |  Tenant_B_OP_Zone  |  -  |  10.2.10.1/24  |  -  |  -  |  -  |
| Vlan211 |  Tenant_B_OP_Zone  |  -  |  10.2.11.1/24  |  -  |  -  |  -  |
| Vlan250 |  Tenant_B_WAN_Zone  |  -  |  10.2.50.1/24  |  -  |  -  |  -  |
| Vlan310 |  Tenant_C_OP_Zone  |  -  |  10.3.10.1/24  |  -  |  -  |  -  |
| Vlan311 |  Tenant_C_OP_Zone  |  -  |  10.3.11.1/24  |  -  |  -  |  -  |
| Vlan350 |  Tenant_C_WAN_Zone  |  -  |  10.3.50.1/24  |  -  |  -  |  -  |
| Vlan3009 |  Tenant_A_OP_Zone  |  10.255.252.6/31  |  -  |  -  |  -  |  -  |
| Vlan3010 |  Tenant_A_WEB_Zone  |  10.255.252.6/31  |  -  |  -  |  -  |  -  |
| Vlan3011 |  Tenant_A_APP_Zone  |  10.255.252.6/31  |  -  |  -  |  -  |  -  |
| Vlan3012 |  Tenant_A_DB_Zone  |  10.255.252.6/31  |  -  |  -  |  -  |  -  |
| Vlan3013 |  Tenant_A_WAN_Zone  |  10.255.252.6/31  |  -  |  -  |  -  |  -  |
| Vlan3019 |  Tenant_B_OP_Zone  |  10.255.252.6/31  |  -  |  -  |  -  |  -  |
| Vlan3020 |  Tenant_B_WAN_Zone  |  10.255.252.6/31  |  -  |  -  |  -  |  -  |
| Vlan3030 |  Tenant_C_WAN_Zone  |  10.255.252.6/31  |  -  |  -  |  -  |  -  |
| Vlan4092 |  default  |  10.255.252.6/31  |  -  |  -  |  -  |  -  |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan2
   description MLAG_L3_VRF_Tenant_C_OP_Zone
   no shutdown
   mtu 1500
   vrf Tenant_C_OP_Zone
   ip address 10.255.252.6/31
!
interface Vlan110
   description SVI 110 CUSTOM DESCRIPTION
   no shutdown
   vrf Tenant_A_OP_Zone
   ip helper-address 1.2.3.4
   ip address virtual 10.1.10.1/24
!
interface Vlan111
   description SVI 111 CUSTOM DESCRIPTION
   no shutdown
   vrf Tenant_A_OP_Zone
   ip helper-address 1.1.1.1 vrf MGMT source-interface lo100
   ip address virtual 10.1.11.1/24
!
interface Vlan120
   description Tenant_A_WEB_Zone_1
   no shutdown
   vrf Tenant_A_WEB_Zone
   ip helper-address 1.1.1.1 vrf TEST source-interface lo100
   ip address virtual 10.1.20.1/24
!
interface Vlan121
   description Tenant_A_WEBZone_2
   shutdown
   mtu 1560
   vrf Tenant_A_WEB_Zone
   ip address virtual 10.1.10.254/24
!
interface Vlan122
   description Tenant_a_WEB_DHCP_no_source_int_no_vrf
   no shutdown
   vrf Tenant_A_WEB_Zone
   ip helper-address 1.1.1.1
   ip address virtual 10.1.22.1/24
!
interface Vlan123
   description Tenant_a_WEB_DHCP_source_int_no_vrf
   no shutdown
   vrf Tenant_A_WEB_Zone
   ip helper-address 1.1.1.1 source-interface lo100
   ip address virtual 10.1.23.1/24
!
interface Vlan124
   description Tenant_a_WEB_DHCP_vrf_no_source_int
   no shutdown
   vrf Tenant_A_WEB_Zone
   ip helper-address 1.1.1.1 vrf TEST
   ip address virtual 10.1.24.1/24
!
interface Vlan130
   description Tenant_A_APP_Zone_1
   no shutdown
   vrf Tenant_A_APP_Zone
   ip address virtual 10.1.30.1/24
!
interface Vlan131
   description Tenant_A_APP_Zone_2
   no shutdown
   vrf Tenant_A_APP_Zone
   ip address virtual 10.1.31.1/24
!
interface Vlan140
   description Tenant_A_DB_BZone_1
   no shutdown
   vrf Tenant_A_DB_Zone
   ip address virtual 10.1.40.1/24
!
interface Vlan141
   description Tenant_A_DB_Zone_2
   no shutdown
   vrf Tenant_A_DB_Zone
   ip address virtual 10.1.41.1/24
!
interface Vlan150
   description Tenant_A_WAN_Zone_1
   no shutdown
   vrf Tenant_A_WAN_Zone
   ip address virtual 10.1.40.1/24
!
interface Vlan210
   description Tenant_B_OP_Zone_1
   no shutdown
   vrf Tenant_B_OP_Zone
   ip address virtual 10.2.10.1/24
!
interface Vlan211
   description Tenant_B_OP_Zone_2
   no shutdown
   vrf Tenant_B_OP_Zone
   ip address virtual 10.2.11.1/24
!
interface Vlan250
   description Tenant_B_WAN_Zone_1
   no shutdown
   vrf Tenant_B_WAN_Zone
   ip address virtual 10.2.50.1/24
!
interface Vlan310
   description Tenant_C_OP_Zone_1
   no shutdown
   vrf Tenant_C_OP_Zone
   ip address virtual 10.3.10.1/24
!
interface Vlan311
   description Tenant_C_OP_Zone_2
   no shutdown
   vrf Tenant_C_OP_Zone
   ip address virtual 10.3.11.1/24
!
interface Vlan350
   description Tenant_C_WAN_Zone_1
   no shutdown
   vrf Tenant_C_WAN_Zone
   ip address virtual 10.3.50.1/24
!
interface Vlan3009
   description MLAG_L3_VRF_Tenant_A_OP_Zone
   no shutdown
   mtu 1500
   vrf Tenant_A_OP_Zone
   ip address 10.255.252.6/31
!
interface Vlan3010
   description MLAG_L3_VRF_Tenant_A_WEB_Zone
   no shutdown
   mtu 1500
   vrf Tenant_A_WEB_Zone
   ip address 10.255.252.6/31
!
interface Vlan3011
   description MLAG_L3_VRF_Tenant_A_APP_Zone
   no shutdown
   mtu 1500
   vrf Tenant_A_APP_Zone
   ip address 10.255.252.6/31
!
interface Vlan3012
   description MLAG_L3_VRF_Tenant_A_DB_Zone
   no shutdown
   mtu 1500
   vrf Tenant_A_DB_Zone
   ip address 10.255.252.6/31
!
interface Vlan3013
   description MLAG_L3_VRF_Tenant_A_WAN_Zone
   no shutdown
   mtu 1500
   vrf Tenant_A_WAN_Zone
   ip address 10.255.252.6/31
!
interface Vlan3019
   description MLAG_L3_VRF_Tenant_B_OP_Zone
   no shutdown
   mtu 1500
   vrf Tenant_B_OP_Zone
   ip address 10.255.252.6/31
!
interface Vlan3020
   description MLAG_L3_VRF_Tenant_B_WAN_Zone
   no shutdown
   mtu 1500
   vrf Tenant_B_WAN_Zone
   ip address 10.255.252.6/31
!
interface Vlan3030
   description MLAG_L3_VRF_Tenant_C_WAN_Zone
   no shutdown
   mtu 1500
   vrf Tenant_C_WAN_Zone
   ip address 10.255.252.6/31
!
interface Vlan4092
   description MLAG
   no shutdown
   mtu 1500
   no autostate
   ip address 10.255.252.6/31
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
| 120 | 10120 | - | - |
| 121 | 10121 | - | - |
| 122 | 10122 | - | - |
| 123 | 10123 | - | - |
| 124 | 10124 | - | - |
| 130 | 10130 | - | - |
| 140 | 10140 | - | - |
| 141 | 10141 | - | - |
| 150 | 10150 | - | - |
| 160 | 10160 | - | - |
| 161 | 10161 | - | - |
| 162 | 10162 | - | - |
| 210 | 20210 | - | - |
| 211 | 20211 | - | - |
| 250 | 20250 | - | - |
| 310 | 30310 | - | - |
| 311 | 30311 | - | - |

##### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| Tenant_A_APP_Zone | 12 | - |
| Tenant_A_DB_Zone | 13 | - |
| Tenant_A_OP_Zone | 10 | - |
| Tenant_A_WAN_Zone | 14 | - |
| Tenant_A_WEB_Zone | 11 | - |
| Tenant_B_OP_Zone | 20 | - |
| Tenant_B_WAN_Zone | 21 | - |
| Tenant_C_OP_Zone | 30 | - |
| Tenant_C_WAN_Zone | 31 | - |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description DC1-SVC3A_VTEP
   vxlan source-interface Loopback1
   vxlan virtual-router encapsulation mac-address mlag-system-id
   vxlan udp-port 4789
   vxlan vlan 110 vni 10110
   vxlan vlan 111 vni 50111
   vxlan vlan 120 vni 10120
   vxlan vlan 121 vni 10121
   vxlan vlan 122 vni 10122
   vxlan vlan 123 vni 10123
   vxlan vlan 124 vni 10124
   vxlan vlan 130 vni 10130
   vxlan vlan 140 vni 10140
   vxlan vlan 141 vni 10141
   vxlan vlan 150 vni 10150
   vxlan vlan 160 vni 10160
   vxlan vlan 161 vni 10161
   vxlan vlan 162 vni 10162
   vxlan vlan 210 vni 20210
   vxlan vlan 211 vni 20211
   vxlan vlan 250 vni 20250
   vxlan vlan 310 vni 30310
   vxlan vlan 311 vni 30311
   vxlan vrf Tenant_A_APP_Zone vni 12
   vxlan vrf Tenant_A_DB_Zone vni 13
   vxlan vrf Tenant_A_OP_Zone vni 10
   vxlan vrf Tenant_A_WAN_Zone vni 14
   vxlan vrf Tenant_A_WEB_Zone vni 11
   vxlan vrf Tenant_B_OP_Zone vni 20
   vxlan vrf Tenant_B_WAN_Zone vni 21
   vxlan vrf Tenant_C_OP_Zone vni 30
   vxlan vrf Tenant_C_WAN_Zone vni 31
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
| Tenant_A_APP_Zone | True |
| Tenant_A_DB_Zone | True |
| Tenant_A_OP_Zone | True |
| Tenant_A_WAN_Zone | True |
| Tenant_A_WEB_Zone | True |
| Tenant_B_OP_Zone | True |
| Tenant_B_WAN_Zone | True |
| Tenant_C_OP_Zone | True |
| Tenant_C_WAN_Zone | True |

#### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
ip routing vrf Tenant_A_APP_Zone
ip routing vrf Tenant_A_DB_Zone
ip routing vrf Tenant_A_OP_Zone
ip routing vrf Tenant_A_WAN_Zone
ip routing vrf Tenant_A_WEB_Zone
ip routing vrf Tenant_B_OP_Zone
ip routing vrf Tenant_B_WAN_Zone
ip routing vrf Tenant_C_OP_Zone
ip routing vrf Tenant_C_WAN_Zone
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| MGMT | false |
| Tenant_A_APP_Zone | false |
| Tenant_A_DB_Zone | false |
| Tenant_A_OP_Zone | false |
| Tenant_A_WAN_Zone | false |
| Tenant_A_WEB_Zone | false |
| Tenant_B_OP_Zone | false |
| Tenant_B_WAN_Zone | false |
| Tenant_C_OP_Zone | false |
| Tenant_C_WAN_Zone | false |

### Static Routes

#### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP | Exit interface | Administrative Distance | Tag | Route Name | Metric |
| --- | ------------------ | ----------- | -------------- | ----------------------- | --- | ---------- | ------ |
| MGMT | 0.0.0.0/0 | 192.168.200.5 | - | 1 | - | - | - |
| Tenant_A_WAN_Zone | 10.3.5.0/24 | - | Null0 | 1 | - | - | - |

#### Static Routes Device Configuration

```eos
!
ip route vrf MGMT 0.0.0.0/0 192.168.200.5
ip route vrf Tenant_A_WAN_Zone 10.3.5.0/24 Null0
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65103 | 192.168.255.12 |

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

##### MLAG-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65103 |
| Next-hop self | True |
| Send community | all |
| Maximum routes | 12000 |

##### UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 10.255.252.7 | Inherited from peer group MLAG-PEERS | default | - | Inherited from peer group MLAG-PEERS | Inherited from peer group MLAG-PEERS | - | - | - | - | - | - |
| 172.31.255.48 | 65001 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.31.255.50 | 65001 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.31.255.52 | 65001 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.31.255.54 | 65001 | default | - | Inherited from peer group UNDERLAY-PEERS | Inherited from peer group UNDERLAY-PEERS | - | - | - | - | - | - |
| 192.168.255.1 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.255.2 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.255.3 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.255.4 | 65001 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.252.7 | Inherited from peer group MLAG-PEERS | Tenant_A_APP_Zone | - | Inherited from peer group MLAG-PEERS | Inherited from peer group MLAG-PEERS | - | - | - | - | - | - |
| 10.255.252.7 | Inherited from peer group MLAG-PEERS | Tenant_A_DB_Zone | - | Inherited from peer group MLAG-PEERS | Inherited from peer group MLAG-PEERS | - | - | - | - | - | - |
| 10.255.252.7 | Inherited from peer group MLAG-PEERS | Tenant_A_OP_Zone | - | Inherited from peer group MLAG-PEERS | Inherited from peer group MLAG-PEERS | - | - | - | - | - | - |
| 10.255.252.7 | Inherited from peer group MLAG-PEERS | Tenant_A_WAN_Zone | - | Inherited from peer group MLAG-PEERS | Inherited from peer group MLAG-PEERS | - | - | - | - | - | - |
| 10.255.252.7 | Inherited from peer group MLAG-PEERS | Tenant_A_WEB_Zone | - | Inherited from peer group MLAG-PEERS | Inherited from peer group MLAG-PEERS | - | - | - | - | - | - |
| 10.255.252.7 | Inherited from peer group MLAG-PEERS | Tenant_B_OP_Zone | - | Inherited from peer group MLAG-PEERS | Inherited from peer group MLAG-PEERS | - | - | - | - | - | - |
| 10.255.252.7 | Inherited from peer group MLAG-PEERS | Tenant_B_WAN_Zone | - | Inherited from peer group MLAG-PEERS | Inherited from peer group MLAG-PEERS | - | - | - | - | - | - |
| 10.255.252.7 | Inherited from peer group MLAG-PEERS | Tenant_C_OP_Zone | - | Inherited from peer group MLAG-PEERS | Inherited from peer group MLAG-PEERS | - | - | - | - | - | - |
| 10.255.252.7 | Inherited from peer group MLAG-PEERS | Tenant_C_WAN_Zone | - | Inherited from peer group MLAG-PEERS | Inherited from peer group MLAG-PEERS | - | - | - | - | - | - |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | Encapsulation |
| ---------- | -------- | ------------ | ------------- | ------------- |
| EVPN-OVERLAY-PEERS | True |  - | - | default |

##### EVPN Host Flapping Settings

| State | Window | Threshold | Expiry Timeout |
| ----- | ------ | --------- | -------------- |
| Disabled | - | - | - |

#### Router BGP VLAN Aware Bundles

| VLAN Aware Bundle | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute | VLANs |
| ----------------- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ | ----- |
| Tenant_A_APP_Zone | 192.168.255.12:12 | 12:12 | - | - | learned | 130 |
| Tenant_A_DB_Zone | 192.168.255.12:13 | 13:13 | - | - | learned | 140-141 |
| Tenant_A_FTP | 192.168.255.12:10162 | 10162:10162 | - | - | learned | 162 |
| Tenant_A_NFS | 192.168.255.12:10161 | 10161:10161 | - | - | learned | 161 |
| Tenant_A_OP_Zone | 192.168.255.12:10 | 10:10 | - | - | learned | 110-111 |
| Tenant_A_VMOTION | 192.168.255.12:10160 | 10160:10160 | - | - | learned | 160 |
| Tenant_A_WAN_Zone | 192.168.255.12:14 | 14:14 | - | - | learned | 150 |
| Tenant_A_WEB_Zone | 192.168.255.12:11 | 11:11 | - | - | learned | 120-124 |
| Tenant_B_OP_Zone | 192.168.255.12:20 | 20:20 | - | - | learned | 210-211 |
| Tenant_B_WAN_Zone | 192.168.255.12:21 | 21:21 | - | - | learned | 250 |
| Tenant_C_OP_Zone | 192.168.255.12:30030 | 30030:30030 | - | - | learned | 310-311 |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Tenant_A_APP_Zone | 192.168.255.12:12 | connected |
| Tenant_A_DB_Zone | 192.168.255.12:13 | connected |
| Tenant_A_OP_Zone | 192.168.255.12:10 | connected |
| Tenant_A_WAN_Zone | 192.168.255.12:14 | connected<br>static |
| Tenant_A_WEB_Zone | 192.168.255.12:11 | connected |
| Tenant_B_OP_Zone | 192.168.255.12:20 | connected |
| Tenant_B_WAN_Zone | 192.168.255.12:21 | connected |
| Tenant_C_OP_Zone | 192.168.255.12:30 | connected |
| Tenant_C_WAN_Zone | 192.168.255.12:31 | connected |

#### Router BGP Device Configuration

```eos
!
router bgp 65103
   router-id 192.168.255.12
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
   neighbor MLAG-PEERS peer group
   neighbor MLAG-PEERS remote-as 65103
   neighbor MLAG-PEERS next-hop-self
   neighbor MLAG-PEERS description DC1-SVC3B
   neighbor MLAG-PEERS route-map RM-MLAG-PEER-IN in
   neighbor MLAG-PEERS password 7 <removed>
   neighbor MLAG-PEERS send-community
   neighbor MLAG-PEERS maximum-routes 12000
   neighbor UNDERLAY-PEERS peer group
   neighbor UNDERLAY-PEERS password 7 <removed>
   neighbor UNDERLAY-PEERS send-community
   neighbor UNDERLAY-PEERS maximum-routes 12000
   neighbor 10.255.252.7 peer group MLAG-PEERS
   neighbor 10.255.252.7 description DC1-SVC3B_Vlan4092
   neighbor 172.31.255.48 peer group UNDERLAY-PEERS
   neighbor 172.31.255.48 remote-as 65001
   neighbor 172.31.255.48 description DC1-SPINE1_Ethernet4
   neighbor 172.31.255.50 peer group UNDERLAY-PEERS
   neighbor 172.31.255.50 remote-as 65001
   neighbor 172.31.255.50 description DC1-SPINE2_Ethernet4
   neighbor 172.31.255.52 peer group UNDERLAY-PEERS
   neighbor 172.31.255.52 remote-as 65001
   neighbor 172.31.255.52 description DC1-SPINE3_Ethernet4
   neighbor 172.31.255.54 peer group UNDERLAY-PEERS
   neighbor 172.31.255.54 remote-as 65001
   neighbor 172.31.255.54 description DC1-SPINE4_Ethernet4
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
   vlan-aware-bundle Tenant_A_APP_Zone
      rd 192.168.255.12:12
      route-target both 12:12
      redistribute learned
      vlan 130
   !
   vlan-aware-bundle Tenant_A_DB_Zone
      rd 192.168.255.12:13
      route-target both 13:13
      redistribute learned
      vlan 140-141
   !
   vlan-aware-bundle Tenant_A_FTP
      rd 192.168.255.12:10162
      route-target both 10162:10162
      redistribute learned
      vlan 162
   !
   vlan-aware-bundle Tenant_A_NFS
      rd 192.168.255.12:10161
      route-target both 10161:10161
      redistribute learned
      vlan 161
   !
   vlan-aware-bundle Tenant_A_OP_Zone
      rd 192.168.255.12:10
      route-target both 10:10
      redistribute learned
      vlan 110-111
   !
   vlan-aware-bundle Tenant_A_VMOTION
      rd 192.168.255.12:10160
      route-target both 10160:10160
      redistribute learned
      vlan 160
   !
   vlan-aware-bundle Tenant_A_WAN_Zone
      rd 192.168.255.12:14
      route-target both 14:14
      redistribute learned
      vlan 150
   !
   vlan-aware-bundle Tenant_A_WEB_Zone
      rd 192.168.255.12:11
      route-target both 11:11
      redistribute learned
      vlan 120-124
   !
   vlan-aware-bundle Tenant_B_OP_Zone
      rd 192.168.255.12:20
      route-target both 20:20
      redistribute learned
      vlan 210-211
   !
   vlan-aware-bundle Tenant_B_WAN_Zone
      rd 192.168.255.12:21
      route-target both 21:21
      redistribute learned
      vlan 250
   !
   vlan-aware-bundle Tenant_C_OP_Zone
      rd 192.168.255.12:30030
      route-target both 30030:30030
      redistribute learned
      vlan 310-311
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
      no host-flap detection
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor MLAG-PEERS activate
      neighbor UNDERLAY-PEERS activate
   !
   vrf Tenant_A_APP_Zone
      rd 192.168.255.12:12
      route-target import evpn 12:12
      route-target export evpn 12:12
      router-id 192.168.255.12
      update wait-install
      neighbor 10.255.252.7 peer group MLAG-PEERS
      neighbor 10.255.252.7 description DC1-SVC3B_Vlan3011
      redistribute connected route-map RM-CONN-2-BGP-VRFS
   !
   vrf Tenant_A_DB_Zone
      rd 192.168.255.12:13
      route-target import evpn 13:13
      route-target export evpn 13:13
      router-id 192.168.255.12
      update wait-install
      neighbor 10.255.252.7 peer group MLAG-PEERS
      neighbor 10.255.252.7 description DC1-SVC3B_Vlan3012
      redistribute connected route-map RM-CONN-2-BGP-VRFS
   !
   vrf Tenant_A_OP_Zone
      rd 192.168.255.12:10
      route-target import evpn 10:10
      route-target export evpn 10:10
      router-id 192.168.255.12
      update wait-install
      neighbor 10.255.252.7 peer group MLAG-PEERS
      neighbor 10.255.252.7 description DC1-SVC3B_Vlan3009
      redistribute connected route-map RM-CONN-2-BGP-VRFS
   !
   vrf Tenant_A_WAN_Zone
      rd 192.168.255.12:14
      route-target import evpn 14:14
      route-target import evpn 65000:456
      route-target export evpn 14:14
      route-target export evpn 65000:789
      router-id 192.168.255.12
      update wait-install
      neighbor 10.255.252.7 peer group MLAG-PEERS
      neighbor 10.255.252.7 description DC1-SVC3B_Vlan3013
      redistribute connected route-map RM-CONN-2-BGP-VRFS
      redistribute static
   !
   vrf Tenant_A_WEB_Zone
      rd 192.168.255.12:11
      route-target import evpn 11:11
      route-target export evpn 11:11
      router-id 192.168.255.12
      update wait-install
      neighbor 10.255.252.7 peer group MLAG-PEERS
      neighbor 10.255.252.7 description DC1-SVC3B_Vlan3010
      redistribute connected route-map RM-CONN-2-BGP-VRFS
   !
   vrf Tenant_B_OP_Zone
      rd 192.168.255.12:20
      route-target import evpn 20:20
      route-target export evpn 20:20
      router-id 192.168.255.12
      update wait-install
      neighbor 10.255.252.7 peer group MLAG-PEERS
      neighbor 10.255.252.7 description DC1-SVC3B_Vlan3019
      redistribute connected route-map RM-CONN-2-BGP-VRFS
   !
   vrf Tenant_B_WAN_Zone
      rd 192.168.255.12:21
      route-target import evpn 21:21
      route-target export evpn 21:21
      router-id 192.168.255.12
      update wait-install
      neighbor 10.255.252.7 peer group MLAG-PEERS
      neighbor 10.255.252.7 description DC1-SVC3B_Vlan3020
      redistribute connected route-map RM-CONN-2-BGP-VRFS
   !
   vrf Tenant_C_OP_Zone
      rd 192.168.255.12:30
      route-target import evpn 30:30
      route-target export evpn 30:30
      router-id 192.168.255.12
      update wait-install
      neighbor 10.255.252.7 peer group MLAG-PEERS
      neighbor 10.255.252.7 description DC1-SVC3B_Vlan2
      redistribute connected route-map RM-CONN-2-BGP-VRFS
   !
   vrf Tenant_C_WAN_Zone
      rd 192.168.255.12:31
      route-target import evpn 31:31
      route-target export evpn 31:31
      router-id 192.168.255.12
      update wait-install
      neighbor 10.255.252.7 peer group MLAG-PEERS
      neighbor 10.255.252.7 description DC1-SVC3B_Vlan3030
      redistribute connected route-map RM-CONN-2-BGP-VRFS
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
| True | 5 | - | - | disabled | disabled | - | - |

### Queue Monitor Configuration

```eos
!
queue-monitor length
!
queue-monitor length log 5
```

## Multicast

### IP IGMP Snooping

#### IP IGMP Snooping Summary

| IGMP Snooping | Fast Leave | Interface Restart Query | Proxy | Restart Query Interval | Robustness Variable |
| ------------- | ---------- | ----------------------- | ----- | ---------------------- | ------------------- |
| Enabled | - | - | - | - | - |

##### IP IGMP Snooping Vlan Summary

| Vlan | IGMP Snooping | Fast Leave | Max Groups | Proxy |
| ---- | ------------- | ---------- | ---------- | ----- |
| 120 | False | - | - | - |
| 160 | True | - | - | - |
| 161 | False | - | - | - |

#### IP IGMP Snooping Device Configuration

```eos
!
no ip igmp snooping vlan 120
ip igmp snooping vlan 160
no ip igmp snooping vlan 161
```

## Filters

### Prefix-lists

#### Prefix-lists Summary

##### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 192.168.255.0/24 eq 32 |
| 20 | permit 192.168.254.0/24 eq 32 |

##### PL-MLAG-PEER-VRFS

| Sequence | Action |
| -------- | ------ |
| 10 | permit 10.255.252.6/31 |

#### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 192.168.255.0/24 eq 32
   seq 20 permit 192.168.254.0/24 eq 32
!
ip prefix-list PL-MLAG-PEER-VRFS
   seq 10 permit 10.255.252.6/31
```

### Route-maps

#### Route-maps Summary

##### RM-CONN-2-BGP

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY | - | - | - |

##### RM-CONN-2-BGP-VRFS

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | deny | ip address prefix-list PL-MLAG-PEER-VRFS | - | - | - |
| 20 | permit | - | - | - | - |

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
route-map RM-CONN-2-BGP-VRFS deny 10
   match ip address prefix-list PL-MLAG-PEER-VRFS
!
route-map RM-CONN-2-BGP-VRFS permit 20
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
| Tenant_A_APP_Zone | enabled |
| Tenant_A_DB_Zone | enabled |
| Tenant_A_OP_Zone | enabled |
| Tenant_A_WAN_Zone | enabled |
| Tenant_A_WEB_Zone | enabled |
| Tenant_B_OP_Zone | enabled |
| Tenant_B_WAN_Zone | enabled |
| Tenant_C_OP_Zone | enabled |
| Tenant_C_WAN_Zone | enabled |

### VRF Instances Device Configuration

```eos
!
vrf instance MGMT
!
vrf instance Tenant_A_APP_Zone
!
vrf instance Tenant_A_DB_Zone
!
vrf instance Tenant_A_OP_Zone
!
vrf instance Tenant_A_WAN_Zone
!
vrf instance Tenant_A_WEB_Zone
!
vrf instance Tenant_B_OP_Zone
!
vrf instance Tenant_B_WAN_Zone
!
vrf instance Tenant_C_OP_Zone
!
vrf instance Tenant_C_WAN_Zone
```

## Virtual Source NAT

### Virtual Source NAT Summary

| Source NAT VRF | Source NAT IP Address |
| -------------- | --------------------- |
| Tenant_A_OP_Zone | 10.255.1.12 |

### Virtual Source NAT Configuration

```eos
!
ip address virtual source-nat vrf Tenant_A_OP_Zone address 10.255.1.12
```
