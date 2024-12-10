# LEAF1B

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
| Management0 | OOB_MANAGEMENT | oob | MGMT | 172.16.100.104/24 | 172.16.100.1 |

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
   ip address 172.16.100.104/24
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
| IDF1 | Vlan4094 | 192.168.0.4 | Port-Channel53 |

Dual primary detection is disabled.

### MLAG Device Configuration

```eos
!
mlag configuration
   domain-id IDF1
   local-interface Vlan4094
   peer-address 192.168.0.4
   peer-link Port-Channel53
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
| 110 | IDF1-Data | - |
| 120 | IDF1-Voice | - |
| 130 | IDF1-Guest | - |
| 4094 | MLAG | MLAG |

### VLANs Device Configuration

```eos
!
vlan 10
   name INBAND_MGMT
!
vlan 110
   name IDF1-Data
!
vlan 120
   name IDF1-Voice
!
vlan 130
   name IDF1-Guest
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
| Ethernet1 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet2 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet3 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet4 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet5 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet6 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet7 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet8 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet9 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet10 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet11 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet12 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet13 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet14 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet15 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet16 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet17 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet18 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet19 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet20 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet21 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet22 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet23 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet24 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet25 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet26 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet27 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet28 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet29 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet30 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet31 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet32 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet33 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet34 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet35 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet36 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet37 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet38 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet39 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet40 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet41 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet42 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet43 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet44 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet45 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet46 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet47 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet48 | IDF1 Standard Port | trunk phone | - | 110 | - | - |
| Ethernet51 | L2_SPINE2_Ethernet1 | *trunk | *10,110,120,130 | *- | *- | 51 |
| Ethernet53 | MLAG_LEAF1A_Ethernet53 | *trunk | *- | *- | *MLAG | 53 |
| Ethernet54 | MLAG_LEAF1A_Ethernet54 | *trunk | *- | *- | *MLAG | 53 |

*Inherited from Port-Channel Interface

##### Phone Interfaces

| Interface | Mode | Native VLAN | Phone VLAN | Phone VLAN Mode |
| --------- | ---- | ----------- | ---------- | --------------- |
| Ethernet1 | trunk phone | 110 | 120 | untagged |
| Ethernet2 | trunk phone | 110 | 120 | untagged |
| Ethernet3 | trunk phone | 110 | 120 | untagged |
| Ethernet4 | trunk phone | 110 | 120 | untagged |
| Ethernet5 | trunk phone | 110 | 120 | untagged |
| Ethernet6 | trunk phone | 110 | 120 | untagged |
| Ethernet7 | trunk phone | 110 | 120 | untagged |
| Ethernet8 | trunk phone | 110 | 120 | untagged |
| Ethernet9 | trunk phone | 110 | 120 | untagged |
| Ethernet10 | trunk phone | 110 | 120 | untagged |
| Ethernet11 | trunk phone | 110 | 120 | untagged |
| Ethernet12 | trunk phone | 110 | 120 | untagged |
| Ethernet13 | trunk phone | 110 | 120 | untagged |
| Ethernet14 | trunk phone | 110 | 120 | untagged |
| Ethernet15 | trunk phone | 110 | 120 | untagged |
| Ethernet16 | trunk phone | 110 | 120 | untagged |
| Ethernet17 | trunk phone | 110 | 120 | untagged |
| Ethernet18 | trunk phone | 110 | 120 | untagged |
| Ethernet19 | trunk phone | 110 | 120 | untagged |
| Ethernet20 | trunk phone | 110 | 120 | untagged |
| Ethernet21 | trunk phone | 110 | 120 | untagged |
| Ethernet22 | trunk phone | 110 | 120 | untagged |
| Ethernet23 | trunk phone | 110 | 120 | untagged |
| Ethernet24 | trunk phone | 110 | 120 | untagged |
| Ethernet25 | trunk phone | 110 | 120 | untagged |
| Ethernet26 | trunk phone | 110 | 120 | untagged |
| Ethernet27 | trunk phone | 110 | 120 | untagged |
| Ethernet28 | trunk phone | 110 | 120 | untagged |
| Ethernet29 | trunk phone | 110 | 120 | untagged |
| Ethernet30 | trunk phone | 110 | 120 | untagged |
| Ethernet31 | trunk phone | 110 | 120 | untagged |
| Ethernet32 | trunk phone | 110 | 120 | untagged |
| Ethernet33 | trunk phone | 110 | 120 | untagged |
| Ethernet34 | trunk phone | 110 | 120 | untagged |
| Ethernet35 | trunk phone | 110 | 120 | untagged |
| Ethernet36 | trunk phone | 110 | 120 | untagged |
| Ethernet37 | trunk phone | 110 | 120 | untagged |
| Ethernet38 | trunk phone | 110 | 120 | untagged |
| Ethernet39 | trunk phone | 110 | 120 | untagged |
| Ethernet40 | trunk phone | 110 | 120 | untagged |
| Ethernet41 | trunk phone | 110 | 120 | untagged |
| Ethernet42 | trunk phone | 110 | 120 | untagged |
| Ethernet43 | trunk phone | 110 | 120 | untagged |
| Ethernet44 | trunk phone | 110 | 120 | untagged |
| Ethernet45 | trunk phone | 110 | 120 | untagged |
| Ethernet46 | trunk phone | 110 | 120 | untagged |
| Ethernet47 | trunk phone | 110 | 120 | untagged |
| Ethernet48 | trunk phone | 110 | 120 | untagged |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet2
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet8
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet9
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet10
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet11
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet12
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet13
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet14
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet15
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet16
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet17
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet18
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet19
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet20
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet21
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet22
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet23
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet24
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet25
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet26
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet27
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet28
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet29
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet30
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet31
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet32
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet33
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet34
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet35
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet36
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet37
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet38
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet39
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet40
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet41
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet42
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet43
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet44
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet45
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet46
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet47
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet48
   description IDF1 Standard Port
   no shutdown
   switchport trunk native vlan 110
   switchport phone vlan 120
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 130
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet51
   description L2_SPINE2_Ethernet1
   no shutdown
   channel-group 51 mode active
!
interface Ethernet53
   description MLAG_LEAF1A_Ethernet53
   no shutdown
   channel-group 53 mode active
!
interface Ethernet54
   description MLAG_LEAF1A_Ethernet54
   no shutdown
   channel-group 53 mode active
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel51 | L2_SPINES_Port-Channel1 | trunk | 10,110,120,130 | - | - | - | - | 51 | - |
| Port-Channel53 | MLAG_LEAF1A_Port-Channel53 | trunk | - | - | MLAG | - | - | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel51
   description L2_SPINES_Port-Channel1
   no shutdown
   switchport trunk allowed vlan 10,110,120,130
   switchport mode trunk
   switchport
   mlag 51
!
interface Port-Channel53
   description MLAG_LEAF1A_Port-Channel53
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
| Vlan10 |  default  |  10.10.10.7/24  |  -  |  -  |  -  |  -  |
| Vlan4094 |  default  |  192.168.0.5/31  |  -  |  -  |  -  |  -  |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan10
   description Inband Management
   no shutdown
   mtu 1500
   ip address 10.10.10.7/24
!
interface Vlan4094
   description MLAG
   no shutdown
   mtu 1500
   no autostate
   ip address 192.168.0.5/31
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
| Ethernet1 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet2 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet3 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet4 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet5 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet6 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet7 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet8 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet9 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet10 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet11 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet12 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet13 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet14 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet15 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet16 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet17 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet18 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet19 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet20 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet21 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet22 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet23 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet24 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet25 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet26 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet27 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet28 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet29 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet30 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet31 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet32 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet33 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet34 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet35 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet36 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet37 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet38 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet39 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet40 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet41 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet42 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet43 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet44 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet45 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet46 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet47 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |
| Ethernet48 | authenticator | auto | - | True | allow vlan 130 | multi-host | True | - |

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
