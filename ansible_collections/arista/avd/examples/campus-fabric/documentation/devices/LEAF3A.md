# LEAF3A

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [IP Name Servers](#ip-name-servers)
  - [NTP](#ntp)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [Enable Password](#enable-password)
  - [AAA Authorization](#aaa-authorization)
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
- [802.1X Port Security](#8021x-port-security)
  - [802.1X Summary](#8021x-summary)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management0 | OOB_MANAGEMENT | oob | MGMT | 172.16.100.106/24 | 172.16.100.1 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management0 | OOB_MANAGEMENT | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management0
   description OOB_MANAGEMENT
   no shutdown
   vrf MGMT
   ip address 172.16.100.106/24
```

### IP Name Servers

#### IP Name Servers Summary

| Name Server | VRF | Priority |
| ----------- | --- | -------- |
| 8.8.4.4 | MGMT | - |
| 8.8.8.8 | MGMT | - |

#### IP Name Servers Device Configuration

```eos
ip name-server vrf MGMT 8.8.4.4
ip name-server vrf MGMT 8.8.8.8
```

### NTP

#### NTP Summary

##### NTP Local Interface

| Interface | VRF |
| --------- | --- |
| Management0 | MGMT |

##### NTP Servers

| Server | VRF | Preferred | Burst | iBurst | Version | Min Poll | Max Poll | Local-interface | Key |
| ------ | --- | --------- | ----- | ------ | ------- | -------- | -------- | --------------- | --- |
| pool.ntp.org | MGMT | - | - | - | - | - | - | - | - |
| time.google.com | MGMT | True | - | - | - | - | - | - | - |

#### NTP Device Configuration

```eos
!
ntp local-interface vrf MGMT Management0
ntp server vrf MGMT pool.ntp.org
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

#### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin secret sha512 <removed>
```

### Enable Password

Enable password has been disabled

### AAA Authorization

#### AAA Authorization Summary

| Type | User Stores |
| ---- | ----------- |
| Exec | local |

Authorization for configuration commands is disabled.

#### AAA Authorization Device Configuration

```eos
aaa authorization exec default local
!
```

## MLAG

### MLAG Summary

| Domain-id | Local-interface | Peer-address | Peer-link |
| --------- | --------------- | ------------ | --------- |
| IDF3_AGG | Vlan4094 | 192.168.0.11 | Port-Channel983 |

Dual primary detection is disabled.

### MLAG Device Configuration

```eos
!
mlag configuration
   domain-id IDF3_AGG
   local-interface Vlan4094
   peer-address 192.168.0.11
   peer-link Port-Channel983
   reload-delay mlag 300
   reload-delay non-mlag 330
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **mstp**

#### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 16384 |

#### Global Spanning-Tree Settings

- Spanning Tree disabled for VLANs: **4094**

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
no spanning-tree vlan-id 4094
spanning-tree mst 0 priority 16384
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
| 10 | INBAND_MGMT | - |
| 310 | IDF3-Data | - |
| 320 | IDF3-Voice | - |
| 330 | IDF3-Guest | - |
| 4094 | MLAG | MLAG |

### VLANs Device Configuration

```eos
!
vlan 10
   name INBAND_MGMT
!
vlan 310
   name IDF3-Data
!
vlan 320
   name IDF3-Voice
!
vlan 330
   name IDF3-Guest
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
| Ethernet1 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet2 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet3 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet4 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet5 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet6 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet7 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet8 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet9 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet10 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet11 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet12 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet13 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet14 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet15 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet16 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet17 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet18 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet19 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet20 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet21 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet22 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet23 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet24 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet25 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet26 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet27 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet28 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet29 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet30 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet31 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet32 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet33 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet34 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet35 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet36 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet37 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet38 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet39 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet40 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet41 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet42 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet43 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet44 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet45 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet46 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet47 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet48 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet49 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet50 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet51 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet52 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet53 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet54 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet55 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet56 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet57 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet58 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet59 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet60 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet61 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet62 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet63 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet64 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet65 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet66 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet67 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet68 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet69 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet70 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet71 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet72 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet73 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet74 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet75 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet76 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet77 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet78 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet79 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet80 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet81 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet82 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet83 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet84 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet85 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet86 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet87 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet88 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet89 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet90 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet91 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet92 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet93 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet94 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet95 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet96 | IDF3 Standard Port | trunk phone | - | 310 | - | - |
| Ethernet97/1 | L2_SPINE1_Ethernet50/1 | *trunk | *10,310,320,330 | *- | *- | 971 |
| Ethernet97/2 | L2_SPINE2_Ethernet50/1 | *trunk | *10,310,320,330 | *- | *- | 971 |
| Ethernet97/3 | L2_LEAF3C_Ethernet97/1 | *trunk | *10,310,320,330 | *- | *- | 973 |
| Ethernet97/4 | L2_LEAF3D_Ethernet97/1 | *trunk | *10,310,320,330 | *- | *- | 974 |
| Ethernet98/1 | L2_LEAF3E_Ethernet97/1 | *trunk | *10,310,320,330 | *- | *- | 981 |
| Ethernet98/3 | MLAG_LEAF3B_Ethernet98/3 | *trunk | *- | *- | *MLAG | 983 |
| Ethernet98/4 | MLAG_LEAF3B_Ethernet98/4 | *trunk | *- | *- | *MLAG | 983 |

*Inherited from Port-Channel Interface

##### Phone Interfaces

| Interface | Mode | Native VLAN | Phone VLAN | Phone VLAN Mode |
| --------- | ---- | ----------- | ---------- | --------------- |
| Ethernet1 | trunk phone | 310 | 320 | untagged |
| Ethernet2 | trunk phone | 310 | 320 | untagged |
| Ethernet3 | trunk phone | 310 | 320 | untagged |
| Ethernet4 | trunk phone | 310 | 320 | untagged |
| Ethernet5 | trunk phone | 310 | 320 | untagged |
| Ethernet6 | trunk phone | 310 | 320 | untagged |
| Ethernet7 | trunk phone | 310 | 320 | untagged |
| Ethernet8 | trunk phone | 310 | 320 | untagged |
| Ethernet9 | trunk phone | 310 | 320 | untagged |
| Ethernet10 | trunk phone | 310 | 320 | untagged |
| Ethernet11 | trunk phone | 310 | 320 | untagged |
| Ethernet12 | trunk phone | 310 | 320 | untagged |
| Ethernet13 | trunk phone | 310 | 320 | untagged |
| Ethernet14 | trunk phone | 310 | 320 | untagged |
| Ethernet15 | trunk phone | 310 | 320 | untagged |
| Ethernet16 | trunk phone | 310 | 320 | untagged |
| Ethernet17 | trunk phone | 310 | 320 | untagged |
| Ethernet18 | trunk phone | 310 | 320 | untagged |
| Ethernet19 | trunk phone | 310 | 320 | untagged |
| Ethernet20 | trunk phone | 310 | 320 | untagged |
| Ethernet21 | trunk phone | 310 | 320 | untagged |
| Ethernet22 | trunk phone | 310 | 320 | untagged |
| Ethernet23 | trunk phone | 310 | 320 | untagged |
| Ethernet24 | trunk phone | 310 | 320 | untagged |
| Ethernet25 | trunk phone | 310 | 320 | untagged |
| Ethernet26 | trunk phone | 310 | 320 | untagged |
| Ethernet27 | trunk phone | 310 | 320 | untagged |
| Ethernet28 | trunk phone | 310 | 320 | untagged |
| Ethernet29 | trunk phone | 310 | 320 | untagged |
| Ethernet30 | trunk phone | 310 | 320 | untagged |
| Ethernet31 | trunk phone | 310 | 320 | untagged |
| Ethernet32 | trunk phone | 310 | 320 | untagged |
| Ethernet33 | trunk phone | 310 | 320 | untagged |
| Ethernet34 | trunk phone | 310 | 320 | untagged |
| Ethernet35 | trunk phone | 310 | 320 | untagged |
| Ethernet36 | trunk phone | 310 | 320 | untagged |
| Ethernet37 | trunk phone | 310 | 320 | untagged |
| Ethernet38 | trunk phone | 310 | 320 | untagged |
| Ethernet39 | trunk phone | 310 | 320 | untagged |
| Ethernet40 | trunk phone | 310 | 320 | untagged |
| Ethernet41 | trunk phone | 310 | 320 | untagged |
| Ethernet42 | trunk phone | 310 | 320 | untagged |
| Ethernet43 | trunk phone | 310 | 320 | untagged |
| Ethernet44 | trunk phone | 310 | 320 | untagged |
| Ethernet45 | trunk phone | 310 | 320 | untagged |
| Ethernet46 | trunk phone | 310 | 320 | untagged |
| Ethernet47 | trunk phone | 310 | 320 | untagged |
| Ethernet48 | trunk phone | 310 | 320 | untagged |
| Ethernet49 | trunk phone | 310 | 320 | untagged |
| Ethernet50 | trunk phone | 310 | 320 | untagged |
| Ethernet51 | trunk phone | 310 | 320 | untagged |
| Ethernet52 | trunk phone | 310 | 320 | untagged |
| Ethernet53 | trunk phone | 310 | 320 | untagged |
| Ethernet54 | trunk phone | 310 | 320 | untagged |
| Ethernet55 | trunk phone | 310 | 320 | untagged |
| Ethernet56 | trunk phone | 310 | 320 | untagged |
| Ethernet57 | trunk phone | 310 | 320 | untagged |
| Ethernet58 | trunk phone | 310 | 320 | untagged |
| Ethernet59 | trunk phone | 310 | 320 | untagged |
| Ethernet60 | trunk phone | 310 | 320 | untagged |
| Ethernet61 | trunk phone | 310 | 320 | untagged |
| Ethernet62 | trunk phone | 310 | 320 | untagged |
| Ethernet63 | trunk phone | 310 | 320 | untagged |
| Ethernet64 | trunk phone | 310 | 320 | untagged |
| Ethernet65 | trunk phone | 310 | 320 | untagged |
| Ethernet66 | trunk phone | 310 | 320 | untagged |
| Ethernet67 | trunk phone | 310 | 320 | untagged |
| Ethernet68 | trunk phone | 310 | 320 | untagged |
| Ethernet69 | trunk phone | 310 | 320 | untagged |
| Ethernet70 | trunk phone | 310 | 320 | untagged |
| Ethernet71 | trunk phone | 310 | 320 | untagged |
| Ethernet72 | trunk phone | 310 | 320 | untagged |
| Ethernet73 | trunk phone | 310 | 320 | untagged |
| Ethernet74 | trunk phone | 310 | 320 | untagged |
| Ethernet75 | trunk phone | 310 | 320 | untagged |
| Ethernet76 | trunk phone | 310 | 320 | untagged |
| Ethernet77 | trunk phone | 310 | 320 | untagged |
| Ethernet78 | trunk phone | 310 | 320 | untagged |
| Ethernet79 | trunk phone | 310 | 320 | untagged |
| Ethernet80 | trunk phone | 310 | 320 | untagged |
| Ethernet81 | trunk phone | 310 | 320 | untagged |
| Ethernet82 | trunk phone | 310 | 320 | untagged |
| Ethernet83 | trunk phone | 310 | 320 | untagged |
| Ethernet84 | trunk phone | 310 | 320 | untagged |
| Ethernet85 | trunk phone | 310 | 320 | untagged |
| Ethernet86 | trunk phone | 310 | 320 | untagged |
| Ethernet87 | trunk phone | 310 | 320 | untagged |
| Ethernet88 | trunk phone | 310 | 320 | untagged |
| Ethernet89 | trunk phone | 310 | 320 | untagged |
| Ethernet90 | trunk phone | 310 | 320 | untagged |
| Ethernet91 | trunk phone | 310 | 320 | untagged |
| Ethernet92 | trunk phone | 310 | 320 | untagged |
| Ethernet93 | trunk phone | 310 | 320 | untagged |
| Ethernet94 | trunk phone | 310 | 320 | untagged |
| Ethernet95 | trunk phone | 310 | 320 | untagged |
| Ethernet96 | trunk phone | 310 | 320 | untagged |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet2
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet8
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet9
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet10
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet11
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet12
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet13
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet14
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet15
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet16
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet17
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet18
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet19
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet20
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet21
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet22
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet23
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet24
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet25
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet26
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet27
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet28
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet29
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet30
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet31
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet32
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet33
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet34
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet35
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet36
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet37
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet38
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet39
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet40
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet41
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet42
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet43
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet44
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet45
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet46
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet47
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet48
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet49
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet50
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet51
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet52
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet53
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet54
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet55
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet56
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet57
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet58
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet59
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet60
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet61
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet62
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet63
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet64
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet65
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet66
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet67
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet68
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet69
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet70
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet71
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet72
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet73
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet74
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet75
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet76
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet77
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet78
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet79
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet80
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet81
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet82
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet83
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet84
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet85
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet86
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet87
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet88
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet89
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet90
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet91
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet92
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet93
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet94
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet95
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet96
   description IDF3 Standard Port
   no shutdown
   switchport trunk native vlan 310
   switchport phone vlan 320
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 330
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet97/1
   description L2_SPINE1_Ethernet50/1
   no shutdown
   channel-group 971 mode active
!
interface Ethernet97/2
   description L2_SPINE2_Ethernet50/1
   no shutdown
   channel-group 971 mode active
!
interface Ethernet97/3
   description L2_LEAF3C_Ethernet97/1
   no shutdown
   channel-group 973 mode active
!
interface Ethernet97/4
   description L2_LEAF3D_Ethernet97/1
   no shutdown
   channel-group 974 mode active
!
interface Ethernet98/1
   description L2_LEAF3E_Ethernet97/1
   no shutdown
   channel-group 981 mode active
!
interface Ethernet98/3
   description MLAG_LEAF3B_Ethernet98/3
   no shutdown
   channel-group 983 mode active
!
interface Ethernet98/4
   description MLAG_LEAF3B_Ethernet98/4
   no shutdown
   channel-group 983 mode active
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel971 | L2_SPINES_Port-Channel501 | trunk | 10,310,320,330 | - | - | - | - | 971 | - |
| Port-Channel973 | L2_LEAF3C_Port-Channel971 | trunk | 10,310,320,330 | - | - | - | - | 973 | - |
| Port-Channel974 | L2_LEAF3D_Port-Channel971 | trunk | 10,310,320,330 | - | - | - | - | 974 | - |
| Port-Channel981 | L2_LEAF3E_Port-Channel971 | trunk | 10,310,320,330 | - | - | - | - | 981 | - |
| Port-Channel983 | MLAG_LEAF3B_Port-Channel983 | trunk | - | - | MLAG | - | - | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel971
   description L2_SPINES_Port-Channel501
   no shutdown
   switchport trunk allowed vlan 10,310,320,330
   switchport mode trunk
   switchport
   mlag 971
!
interface Port-Channel973
   description L2_LEAF3C_Port-Channel971
   no shutdown
   switchport trunk allowed vlan 10,310,320,330
   switchport mode trunk
   switchport
   mlag 973
!
interface Port-Channel974
   description L2_LEAF3D_Port-Channel971
   no shutdown
   switchport trunk allowed vlan 10,310,320,330
   switchport mode trunk
   switchport
   mlag 974
!
interface Port-Channel981
   description L2_LEAF3E_Port-Channel971
   no shutdown
   switchport trunk allowed vlan 10,310,320,330
   switchport mode trunk
   switchport
   mlag 981
!
interface Port-Channel983
   description MLAG_LEAF3B_Port-Channel983
   no shutdown
   switchport mode trunk
   switchport trunk group MLAG
   switchport
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan10 | Inband Management | default | 1500 | False |
| Vlan4094 | MLAG | default | 1500 | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| Vlan10 |  default  |  10.10.10.9/24  |  -  |  -  |  -  |  -  |
| Vlan4094 |  default  |  192.168.0.10/31  |  -  |  -  |  -  |  -  |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan10
   description Inband Management
   no shutdown
   mtu 1500
   ip address 10.10.10.9/24
!
interface Vlan4094
   description MLAG
   no shutdown
   mtu 1500
   no autostate
   ip address 192.168.0.10/31
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
| MGMT | 0.0.0.0/0 | 172.16.100.1 | - | 1 | - | - | - |
| default | 0.0.0.0/0 | 10.10.10.1 | - | 1 | - | - | - |

#### Static Routes Device Configuration

```eos
!
ip route 0.0.0.0/0 10.10.10.1
ip route vrf MGMT 0.0.0.0/0 172.16.100.1
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

## 802.1X Port Security

### 802.1X Summary

#### 802.1X Interfaces

| Interface | PAE Mode | State | Phone Force Authorized | Reauthentication | Auth Failure Action | Host Mode | Mac Based Auth | Eapol |
| --------- | -------- | ------| ---------------------- | ---------------- | ------------------- | --------- | -------------- | ------ |
| Ethernet1 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet2 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet3 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet4 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet5 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet6 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet7 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet8 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet9 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet10 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet11 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet12 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet13 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet14 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet15 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet16 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet17 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet18 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet19 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet20 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet21 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet22 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet23 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet24 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet25 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet26 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet27 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet28 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet29 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet30 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet31 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet32 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet33 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet34 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet35 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet36 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet37 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet38 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet39 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet40 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet41 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet42 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet43 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet44 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet45 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet46 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet47 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet48 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet49 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet50 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet51 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet52 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet53 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet54 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet55 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet56 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet57 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet58 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet59 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet60 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet61 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet62 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet63 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet64 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet65 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet66 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet67 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet68 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet69 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet70 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet71 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet72 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet73 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet74 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet75 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet76 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet77 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet78 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet79 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet80 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet81 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet82 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet83 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet84 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet85 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet86 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet87 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet88 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet89 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet90 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet91 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet92 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet93 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet94 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet95 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |
| Ethernet96 | authenticator | auto | - | True | allow vlan 330 | multi-host | True | - |

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
