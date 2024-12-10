# DC1-POD1-L2LEAF2A

## Table of Contents

- [Management](#management)
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
  - [VLAN Interfaces](#vlan-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [EOS CLI Device Configuration](#eos-cli-device-configuration)

## Management

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
| - | TWODC_5STAGE_CLOS DC1 DC1_POD1 DC1-POD1-L2LEAF2A | All | Disabled |

#### SNMP Device Configuration

```eos
!
snmp-server location TWODC_5STAGE_CLOS DC1 DC1_POD1 DC1-POD1-L2LEAF2A
```

## MLAG

### MLAG Summary

| Domain-id | Local-interface | Peer-address | Peer-link |
| --------- | --------------- | ------------ | --------- |
| RACK2_MLAG | Vlan4094 | 172.20.110.3 | Port-Channel3 |

Dual primary detection is disabled.

### MLAG Device Configuration

```eos
!
mlag configuration
   domain-id RACK2_MLAG
   local-interface Vlan4094
   peer-address 172.20.110.3
   peer-link Port-Channel3
   reload-delay mlag 300
   reload-delay non-mlag 330
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **mstp**

#### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 8192 |

#### Global Spanning-Tree Settings

- Spanning Tree disabled for VLANs: **4094**

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
no spanning-tree vlan-id 4094
spanning-tree mst 0 priority 8192
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
| Ethernet1 | L2_DC1.POD1.LEAF2A_Ethernet3 | *trunk | *110-113,1100-1102,2500,2600-2601,4085 | *- | *- | 1 |
| Ethernet2 | L2_DC1-POD1-LEAF2B_Ethernet3 | *trunk | *110-113,1100-1102,2500,2600-2601,4085 | *- | *- | 1 |
| Ethernet3 | MLAG_DC1-POD1-L2LEAF2B_Ethernet3 | *trunk | *- | *- | *MLAG | 3 |
| Ethernet4 | MLAG_DC1-POD1-L2LEAF2B_Ethernet4 | *trunk | *- | *- | *MLAG | 3 |

*Inherited from Port-Channel Interface

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description L2_DC1.POD1.LEAF2A_Ethernet3
   no shutdown
   channel-group 1 mode active
!
interface Ethernet2
   description L2_DC1-POD1-LEAF2B_Ethernet3
   no shutdown
   channel-group 1 mode active
!
interface Ethernet3
   description MLAG_DC1-POD1-L2LEAF2B_Ethernet3
   no shutdown
   channel-group 3 mode active
!
interface Ethernet4
   description MLAG_DC1-POD1-L2LEAF2B_Ethernet4
   no shutdown
   channel-group 3 mode active
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel1 | L2_RACK2_MLAG_Port-Channel3 | trunk | 110-113,1100-1102,2500,2600-2601,4085 | - | - | - | - | 1 | - |
| Port-Channel3 | MLAG_DC1-POD1-L2LEAF2B_Port-Channel3 | trunk | - | - | MLAG | - | - | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel1
   description L2_RACK2_MLAG_Port-Channel3
   no shutdown
   switchport trunk allowed vlan 110-113,1100-1102,2500,2600-2601,4085
   switchport mode trunk
   switchport
   mlag 1
   service-profile QOS-PROFILE
!
interface Port-Channel3
   description MLAG_DC1-POD1-L2LEAF2B_Port-Channel3
   no shutdown
   switchport mode trunk
   switchport trunk group MLAG
   switchport
   service-profile QOS-PROFILE
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan4085 | L2LEAF_INBAND_MGMT | default | - | False |
| Vlan4094 | MLAG | default | - | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| Vlan4085 |  default  |  172.21.110.5/24  |  -  |  -  |  -  |  -  |
| Vlan4094 |  default  |  172.20.110.2/31  |  -  |  -  |  -  |  -  |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan4085
   description L2LEAF_INBAND_MGMT
   no shutdown
   ip address 172.21.110.5/24
!
interface Vlan4094
   description MLAG
   no shutdown
   no autostate
   ip address 172.20.110.2/31
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
| default | False |
| MGMT | False |

#### IP Routing Device Configuration

```eos
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
| MGMT | 0.0.0.0/0 | 192.168.1.254 | - | 1 | - | - | - |
| default | 0.0.0.0/0 | 172.21.110.1 | - | 1 | - | - | - |

#### Static Routes Device Configuration

```eos
!
ip route 0.0.0.0/0 172.21.110.1
ip route vrf MGMT 0.0.0.0/0 192.168.1.254
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

### VRF Instances Device Configuration

```eos
!
vrf instance MGMT
```

## EOS CLI Device Configuration

```eos
!
interface Loopback1002
  description Loopback created from raw_eos_cli under l2leaf node-group RACK2_MLAG

interface Loopback1111
  description Loopback created from raw_eos_cli under platform_settings vEOS-LAB

```
