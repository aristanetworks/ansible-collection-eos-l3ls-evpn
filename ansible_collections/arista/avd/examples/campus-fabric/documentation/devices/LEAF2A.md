# LEAF2A

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
- [Power Over Ethernet (PoE)](#power-over-ethernet-poe)
  - [PoE Summary](#poe-summary)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management0 | OOB_MANAGEMENT | oob | MGMT | 172.16.100.105/24 | 172.16.100.1 |

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
   ip address 172.16.100.105/24
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

## Spanning Tree

### Spanning Tree Summary

STP mode: **mstp**

#### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 16384 |

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
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
| 210 | IDF2-Data | - |
| 220 | IDF2-Voice | - |
| 230 | IDF2-Guest | - |

### VLANs Device Configuration

```eos
!
vlan 10
   name INBAND_MGMT
!
vlan 210
   name IDF2-Data
!
vlan 220
   name IDF2-Voice
!
vlan 230
   name IDF2-Guest
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet1/1 | L2_SPINE1_Ethernet49/1 | *trunk | *10,210,220,230 | *- | *- | 11 |
| Ethernet1/3 | L2_SPINE2_Ethernet49/1 | *trunk | *10,210,220,230 | *- | *- | 11 |
| Ethernet3/1 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/2 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/3 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/4 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/5 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/6 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/7 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/8 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/9 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/10 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/11 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/12 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/13 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/14 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/15 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/16 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/17 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/18 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/19 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/20 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/21 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/22 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/23 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/24 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/25 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/26 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/27 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/28 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/29 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/30 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/31 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/32 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/33 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/34 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/35 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/36 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/37 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/38 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/39 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/40 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/41 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/42 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/43 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/44 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/45 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/46 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/47 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet3/48 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/1 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/2 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/3 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/4 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/5 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/6 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/7 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/8 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/9 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/10 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/11 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/12 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/13 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/14 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/15 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/16 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/17 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/18 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/19 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/20 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/21 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/22 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/23 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/24 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/25 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/26 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/27 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/28 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/29 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/30 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/31 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/32 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/33 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/34 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/35 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/36 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/37 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/38 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/39 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/40 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/41 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/42 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/43 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/44 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/45 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/46 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/47 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet4/48 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/1 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/2 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/3 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/4 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/5 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/6 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/7 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/8 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/9 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/10 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/11 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/12 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/13 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/14 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/15 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/16 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/17 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/18 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/19 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/20 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/21 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/22 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/23 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/24 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/25 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/26 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/27 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/28 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/29 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/30 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/31 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/32 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/33 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/34 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/35 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/36 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/37 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/38 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/39 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/40 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/41 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/42 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/43 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/44 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/45 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/46 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/47 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet5/48 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/1 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/2 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/3 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/4 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/5 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/6 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/7 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/8 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/9 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/10 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/11 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/12 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/13 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/14 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/15 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/16 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/17 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/18 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/19 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/20 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/21 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/22 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/23 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/24 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/25 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/26 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/27 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/28 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/29 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/30 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/31 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/32 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/33 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/34 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/35 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/36 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/37 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/38 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/39 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/40 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/41 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/42 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/43 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/44 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/45 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/46 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/47 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet6/48 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/1 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/2 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/3 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/4 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/5 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/6 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/7 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/8 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/9 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/10 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/11 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/12 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/13 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/14 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/15 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/16 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/17 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/18 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/19 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/20 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/21 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/22 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/23 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/24 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/25 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/26 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/27 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/28 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/29 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/30 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/31 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/32 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/33 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/34 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/35 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/36 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/37 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/38 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/39 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/40 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/41 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/42 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/43 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/44 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/45 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/46 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/47 | IDF2 Standard Port | trunk phone | - | 210 | - | - |
| Ethernet7/48 | IDF2 Standard Port | trunk phone | - | 210 | - | - |

*Inherited from Port-Channel Interface

##### Phone Interfaces

| Interface | Mode | Native VLAN | Phone VLAN | Phone VLAN Mode |
| --------- | ---- | ----------- | ---------- | --------------- |
| Ethernet3/1 | trunk phone | 210 | 220 | untagged |
| Ethernet3/2 | trunk phone | 210 | 220 | untagged |
| Ethernet3/3 | trunk phone | 210 | 220 | untagged |
| Ethernet3/4 | trunk phone | 210 | 220 | untagged |
| Ethernet3/5 | trunk phone | 210 | 220 | untagged |
| Ethernet3/6 | trunk phone | 210 | 220 | untagged |
| Ethernet3/7 | trunk phone | 210 | 220 | untagged |
| Ethernet3/8 | trunk phone | 210 | 220 | untagged |
| Ethernet3/9 | trunk phone | 210 | 220 | untagged |
| Ethernet3/10 | trunk phone | 210 | 220 | untagged |
| Ethernet3/11 | trunk phone | 210 | 220 | untagged |
| Ethernet3/12 | trunk phone | 210 | 220 | untagged |
| Ethernet3/13 | trunk phone | 210 | 220 | untagged |
| Ethernet3/14 | trunk phone | 210 | 220 | untagged |
| Ethernet3/15 | trunk phone | 210 | 220 | untagged |
| Ethernet3/16 | trunk phone | 210 | 220 | untagged |
| Ethernet3/17 | trunk phone | 210 | 220 | untagged |
| Ethernet3/18 | trunk phone | 210 | 220 | untagged |
| Ethernet3/19 | trunk phone | 210 | 220 | untagged |
| Ethernet3/20 | trunk phone | 210 | 220 | untagged |
| Ethernet3/21 | trunk phone | 210 | 220 | untagged |
| Ethernet3/22 | trunk phone | 210 | 220 | untagged |
| Ethernet3/23 | trunk phone | 210 | 220 | untagged |
| Ethernet3/24 | trunk phone | 210 | 220 | untagged |
| Ethernet3/25 | trunk phone | 210 | 220 | untagged |
| Ethernet3/26 | trunk phone | 210 | 220 | untagged |
| Ethernet3/27 | trunk phone | 210 | 220 | untagged |
| Ethernet3/28 | trunk phone | 210 | 220 | untagged |
| Ethernet3/29 | trunk phone | 210 | 220 | untagged |
| Ethernet3/30 | trunk phone | 210 | 220 | untagged |
| Ethernet3/31 | trunk phone | 210 | 220 | untagged |
| Ethernet3/32 | trunk phone | 210 | 220 | untagged |
| Ethernet3/33 | trunk phone | 210 | 220 | untagged |
| Ethernet3/34 | trunk phone | 210 | 220 | untagged |
| Ethernet3/35 | trunk phone | 210 | 220 | untagged |
| Ethernet3/36 | trunk phone | 210 | 220 | untagged |
| Ethernet3/37 | trunk phone | 210 | 220 | untagged |
| Ethernet3/38 | trunk phone | 210 | 220 | untagged |
| Ethernet3/39 | trunk phone | 210 | 220 | untagged |
| Ethernet3/40 | trunk phone | 210 | 220 | untagged |
| Ethernet3/41 | trunk phone | 210 | 220 | untagged |
| Ethernet3/42 | trunk phone | 210 | 220 | untagged |
| Ethernet3/43 | trunk phone | 210 | 220 | untagged |
| Ethernet3/44 | trunk phone | 210 | 220 | untagged |
| Ethernet3/45 | trunk phone | 210 | 220 | untagged |
| Ethernet3/46 | trunk phone | 210 | 220 | untagged |
| Ethernet3/47 | trunk phone | 210 | 220 | untagged |
| Ethernet3/48 | trunk phone | 210 | 220 | untagged |
| Ethernet4/1 | trunk phone | 210 | 220 | untagged |
| Ethernet4/2 | trunk phone | 210 | 220 | untagged |
| Ethernet4/3 | trunk phone | 210 | 220 | untagged |
| Ethernet4/4 | trunk phone | 210 | 220 | untagged |
| Ethernet4/5 | trunk phone | 210 | 220 | untagged |
| Ethernet4/6 | trunk phone | 210 | 220 | untagged |
| Ethernet4/7 | trunk phone | 210 | 220 | untagged |
| Ethernet4/8 | trunk phone | 210 | 220 | untagged |
| Ethernet4/9 | trunk phone | 210 | 220 | untagged |
| Ethernet4/10 | trunk phone | 210 | 220 | untagged |
| Ethernet4/11 | trunk phone | 210 | 220 | untagged |
| Ethernet4/12 | trunk phone | 210 | 220 | untagged |
| Ethernet4/13 | trunk phone | 210 | 220 | untagged |
| Ethernet4/14 | trunk phone | 210 | 220 | untagged |
| Ethernet4/15 | trunk phone | 210 | 220 | untagged |
| Ethernet4/16 | trunk phone | 210 | 220 | untagged |
| Ethernet4/17 | trunk phone | 210 | 220 | untagged |
| Ethernet4/18 | trunk phone | 210 | 220 | untagged |
| Ethernet4/19 | trunk phone | 210 | 220 | untagged |
| Ethernet4/20 | trunk phone | 210 | 220 | untagged |
| Ethernet4/21 | trunk phone | 210 | 220 | untagged |
| Ethernet4/22 | trunk phone | 210 | 220 | untagged |
| Ethernet4/23 | trunk phone | 210 | 220 | untagged |
| Ethernet4/24 | trunk phone | 210 | 220 | untagged |
| Ethernet4/25 | trunk phone | 210 | 220 | untagged |
| Ethernet4/26 | trunk phone | 210 | 220 | untagged |
| Ethernet4/27 | trunk phone | 210 | 220 | untagged |
| Ethernet4/28 | trunk phone | 210 | 220 | untagged |
| Ethernet4/29 | trunk phone | 210 | 220 | untagged |
| Ethernet4/30 | trunk phone | 210 | 220 | untagged |
| Ethernet4/31 | trunk phone | 210 | 220 | untagged |
| Ethernet4/32 | trunk phone | 210 | 220 | untagged |
| Ethernet4/33 | trunk phone | 210 | 220 | untagged |
| Ethernet4/34 | trunk phone | 210 | 220 | untagged |
| Ethernet4/35 | trunk phone | 210 | 220 | untagged |
| Ethernet4/36 | trunk phone | 210 | 220 | untagged |
| Ethernet4/37 | trunk phone | 210 | 220 | untagged |
| Ethernet4/38 | trunk phone | 210 | 220 | untagged |
| Ethernet4/39 | trunk phone | 210 | 220 | untagged |
| Ethernet4/40 | trunk phone | 210 | 220 | untagged |
| Ethernet4/41 | trunk phone | 210 | 220 | untagged |
| Ethernet4/42 | trunk phone | 210 | 220 | untagged |
| Ethernet4/43 | trunk phone | 210 | 220 | untagged |
| Ethernet4/44 | trunk phone | 210 | 220 | untagged |
| Ethernet4/45 | trunk phone | 210 | 220 | untagged |
| Ethernet4/46 | trunk phone | 210 | 220 | untagged |
| Ethernet4/47 | trunk phone | 210 | 220 | untagged |
| Ethernet4/48 | trunk phone | 210 | 220 | untagged |
| Ethernet5/1 | trunk phone | 210 | 220 | untagged |
| Ethernet5/2 | trunk phone | 210 | 220 | untagged |
| Ethernet5/3 | trunk phone | 210 | 220 | untagged |
| Ethernet5/4 | trunk phone | 210 | 220 | untagged |
| Ethernet5/5 | trunk phone | 210 | 220 | untagged |
| Ethernet5/6 | trunk phone | 210 | 220 | untagged |
| Ethernet5/7 | trunk phone | 210 | 220 | untagged |
| Ethernet5/8 | trunk phone | 210 | 220 | untagged |
| Ethernet5/9 | trunk phone | 210 | 220 | untagged |
| Ethernet5/10 | trunk phone | 210 | 220 | untagged |
| Ethernet5/11 | trunk phone | 210 | 220 | untagged |
| Ethernet5/12 | trunk phone | 210 | 220 | untagged |
| Ethernet5/13 | trunk phone | 210 | 220 | untagged |
| Ethernet5/14 | trunk phone | 210 | 220 | untagged |
| Ethernet5/15 | trunk phone | 210 | 220 | untagged |
| Ethernet5/16 | trunk phone | 210 | 220 | untagged |
| Ethernet5/17 | trunk phone | 210 | 220 | untagged |
| Ethernet5/18 | trunk phone | 210 | 220 | untagged |
| Ethernet5/19 | trunk phone | 210 | 220 | untagged |
| Ethernet5/20 | trunk phone | 210 | 220 | untagged |
| Ethernet5/21 | trunk phone | 210 | 220 | untagged |
| Ethernet5/22 | trunk phone | 210 | 220 | untagged |
| Ethernet5/23 | trunk phone | 210 | 220 | untagged |
| Ethernet5/24 | trunk phone | 210 | 220 | untagged |
| Ethernet5/25 | trunk phone | 210 | 220 | untagged |
| Ethernet5/26 | trunk phone | 210 | 220 | untagged |
| Ethernet5/27 | trunk phone | 210 | 220 | untagged |
| Ethernet5/28 | trunk phone | 210 | 220 | untagged |
| Ethernet5/29 | trunk phone | 210 | 220 | untagged |
| Ethernet5/30 | trunk phone | 210 | 220 | untagged |
| Ethernet5/31 | trunk phone | 210 | 220 | untagged |
| Ethernet5/32 | trunk phone | 210 | 220 | untagged |
| Ethernet5/33 | trunk phone | 210 | 220 | untagged |
| Ethernet5/34 | trunk phone | 210 | 220 | untagged |
| Ethernet5/35 | trunk phone | 210 | 220 | untagged |
| Ethernet5/36 | trunk phone | 210 | 220 | untagged |
| Ethernet5/37 | trunk phone | 210 | 220 | untagged |
| Ethernet5/38 | trunk phone | 210 | 220 | untagged |
| Ethernet5/39 | trunk phone | 210 | 220 | untagged |
| Ethernet5/40 | trunk phone | 210 | 220 | untagged |
| Ethernet5/41 | trunk phone | 210 | 220 | untagged |
| Ethernet5/42 | trunk phone | 210 | 220 | untagged |
| Ethernet5/43 | trunk phone | 210 | 220 | untagged |
| Ethernet5/44 | trunk phone | 210 | 220 | untagged |
| Ethernet5/45 | trunk phone | 210 | 220 | untagged |
| Ethernet5/46 | trunk phone | 210 | 220 | untagged |
| Ethernet5/47 | trunk phone | 210 | 220 | untagged |
| Ethernet5/48 | trunk phone | 210 | 220 | untagged |
| Ethernet6/1 | trunk phone | 210 | 220 | untagged |
| Ethernet6/2 | trunk phone | 210 | 220 | untagged |
| Ethernet6/3 | trunk phone | 210 | 220 | untagged |
| Ethernet6/4 | trunk phone | 210 | 220 | untagged |
| Ethernet6/5 | trunk phone | 210 | 220 | untagged |
| Ethernet6/6 | trunk phone | 210 | 220 | untagged |
| Ethernet6/7 | trunk phone | 210 | 220 | untagged |
| Ethernet6/8 | trunk phone | 210 | 220 | untagged |
| Ethernet6/9 | trunk phone | 210 | 220 | untagged |
| Ethernet6/10 | trunk phone | 210 | 220 | untagged |
| Ethernet6/11 | trunk phone | 210 | 220 | untagged |
| Ethernet6/12 | trunk phone | 210 | 220 | untagged |
| Ethernet6/13 | trunk phone | 210 | 220 | untagged |
| Ethernet6/14 | trunk phone | 210 | 220 | untagged |
| Ethernet6/15 | trunk phone | 210 | 220 | untagged |
| Ethernet6/16 | trunk phone | 210 | 220 | untagged |
| Ethernet6/17 | trunk phone | 210 | 220 | untagged |
| Ethernet6/18 | trunk phone | 210 | 220 | untagged |
| Ethernet6/19 | trunk phone | 210 | 220 | untagged |
| Ethernet6/20 | trunk phone | 210 | 220 | untagged |
| Ethernet6/21 | trunk phone | 210 | 220 | untagged |
| Ethernet6/22 | trunk phone | 210 | 220 | untagged |
| Ethernet6/23 | trunk phone | 210 | 220 | untagged |
| Ethernet6/24 | trunk phone | 210 | 220 | untagged |
| Ethernet6/25 | trunk phone | 210 | 220 | untagged |
| Ethernet6/26 | trunk phone | 210 | 220 | untagged |
| Ethernet6/27 | trunk phone | 210 | 220 | untagged |
| Ethernet6/28 | trunk phone | 210 | 220 | untagged |
| Ethernet6/29 | trunk phone | 210 | 220 | untagged |
| Ethernet6/30 | trunk phone | 210 | 220 | untagged |
| Ethernet6/31 | trunk phone | 210 | 220 | untagged |
| Ethernet6/32 | trunk phone | 210 | 220 | untagged |
| Ethernet6/33 | trunk phone | 210 | 220 | untagged |
| Ethernet6/34 | trunk phone | 210 | 220 | untagged |
| Ethernet6/35 | trunk phone | 210 | 220 | untagged |
| Ethernet6/36 | trunk phone | 210 | 220 | untagged |
| Ethernet6/37 | trunk phone | 210 | 220 | untagged |
| Ethernet6/38 | trunk phone | 210 | 220 | untagged |
| Ethernet6/39 | trunk phone | 210 | 220 | untagged |
| Ethernet6/40 | trunk phone | 210 | 220 | untagged |
| Ethernet6/41 | trunk phone | 210 | 220 | untagged |
| Ethernet6/42 | trunk phone | 210 | 220 | untagged |
| Ethernet6/43 | trunk phone | 210 | 220 | untagged |
| Ethernet6/44 | trunk phone | 210 | 220 | untagged |
| Ethernet6/45 | trunk phone | 210 | 220 | untagged |
| Ethernet6/46 | trunk phone | 210 | 220 | untagged |
| Ethernet6/47 | trunk phone | 210 | 220 | untagged |
| Ethernet6/48 | trunk phone | 210 | 220 | untagged |
| Ethernet7/1 | trunk phone | 210 | 220 | untagged |
| Ethernet7/2 | trunk phone | 210 | 220 | untagged |
| Ethernet7/3 | trunk phone | 210 | 220 | untagged |
| Ethernet7/4 | trunk phone | 210 | 220 | untagged |
| Ethernet7/5 | trunk phone | 210 | 220 | untagged |
| Ethernet7/6 | trunk phone | 210 | 220 | untagged |
| Ethernet7/7 | trunk phone | 210 | 220 | untagged |
| Ethernet7/8 | trunk phone | 210 | 220 | untagged |
| Ethernet7/9 | trunk phone | 210 | 220 | untagged |
| Ethernet7/10 | trunk phone | 210 | 220 | untagged |
| Ethernet7/11 | trunk phone | 210 | 220 | untagged |
| Ethernet7/12 | trunk phone | 210 | 220 | untagged |
| Ethernet7/13 | trunk phone | 210 | 220 | untagged |
| Ethernet7/14 | trunk phone | 210 | 220 | untagged |
| Ethernet7/15 | trunk phone | 210 | 220 | untagged |
| Ethernet7/16 | trunk phone | 210 | 220 | untagged |
| Ethernet7/17 | trunk phone | 210 | 220 | untagged |
| Ethernet7/18 | trunk phone | 210 | 220 | untagged |
| Ethernet7/19 | trunk phone | 210 | 220 | untagged |
| Ethernet7/20 | trunk phone | 210 | 220 | untagged |
| Ethernet7/21 | trunk phone | 210 | 220 | untagged |
| Ethernet7/22 | trunk phone | 210 | 220 | untagged |
| Ethernet7/23 | trunk phone | 210 | 220 | untagged |
| Ethernet7/24 | trunk phone | 210 | 220 | untagged |
| Ethernet7/25 | trunk phone | 210 | 220 | untagged |
| Ethernet7/26 | trunk phone | 210 | 220 | untagged |
| Ethernet7/27 | trunk phone | 210 | 220 | untagged |
| Ethernet7/28 | trunk phone | 210 | 220 | untagged |
| Ethernet7/29 | trunk phone | 210 | 220 | untagged |
| Ethernet7/30 | trunk phone | 210 | 220 | untagged |
| Ethernet7/31 | trunk phone | 210 | 220 | untagged |
| Ethernet7/32 | trunk phone | 210 | 220 | untagged |
| Ethernet7/33 | trunk phone | 210 | 220 | untagged |
| Ethernet7/34 | trunk phone | 210 | 220 | untagged |
| Ethernet7/35 | trunk phone | 210 | 220 | untagged |
| Ethernet7/36 | trunk phone | 210 | 220 | untagged |
| Ethernet7/37 | trunk phone | 210 | 220 | untagged |
| Ethernet7/38 | trunk phone | 210 | 220 | untagged |
| Ethernet7/39 | trunk phone | 210 | 220 | untagged |
| Ethernet7/40 | trunk phone | 210 | 220 | untagged |
| Ethernet7/41 | trunk phone | 210 | 220 | untagged |
| Ethernet7/42 | trunk phone | 210 | 220 | untagged |
| Ethernet7/43 | trunk phone | 210 | 220 | untagged |
| Ethernet7/44 | trunk phone | 210 | 220 | untagged |
| Ethernet7/45 | trunk phone | 210 | 220 | untagged |
| Ethernet7/46 | trunk phone | 210 | 220 | untagged |
| Ethernet7/47 | trunk phone | 210 | 220 | untagged |
| Ethernet7/48 | trunk phone | 210 | 220 | untagged |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1/1
   description L2_SPINE1_Ethernet49/1
   no shutdown
   channel-group 11 mode active
!
interface Ethernet1/3
   description L2_SPINE2_Ethernet49/1
   no shutdown
   channel-group 11 mode active
!
interface Ethernet3/1
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/2
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/3
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/4
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/5
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/6
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/7
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/8
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/9
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/10
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/11
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/12
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/13
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/14
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/15
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/16
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/17
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/18
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/19
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/20
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/21
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/22
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/23
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/24
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/25
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/26
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/27
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/28
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/29
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/30
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/31
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/32
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/33
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/34
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/35
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/36
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/37
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/38
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/39
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/40
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/41
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/42
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/43
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/44
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/45
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/46
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/47
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet3/48
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/1
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/2
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/3
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/4
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/5
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/6
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/7
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/8
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/9
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/10
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/11
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/12
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/13
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/14
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/15
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/16
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/17
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/18
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/19
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/20
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/21
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/22
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/23
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/24
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/25
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/26
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/27
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/28
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/29
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/30
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/31
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/32
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/33
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/34
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/35
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/36
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/37
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/38
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/39
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/40
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/41
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/42
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/43
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/44
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/45
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/46
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/47
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet4/48
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/1
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/2
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/3
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/4
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/5
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/6
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/7
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/8
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/9
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/10
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/11
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/12
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/13
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/14
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/15
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/16
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/17
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/18
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/19
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/20
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/21
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/22
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/23
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/24
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/25
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/26
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/27
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/28
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/29
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/30
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/31
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/32
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/33
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/34
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/35
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/36
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/37
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/38
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/39
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/40
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/41
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/42
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/43
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/44
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/45
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/46
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/47
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet5/48
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/1
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/2
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/3
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/4
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/5
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/6
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/7
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/8
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/9
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/10
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/11
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/12
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/13
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/14
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/15
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/16
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/17
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/18
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/19
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/20
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/21
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/22
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/23
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/24
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/25
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/26
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/27
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/28
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/29
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/30
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/31
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/32
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/33
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/34
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/35
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/36
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/37
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/38
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/39
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/40
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/41
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/42
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/43
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/44
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/45
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/46
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/47
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet6/48
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/1
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/2
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/3
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/4
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/5
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/6
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/7
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/8
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/9
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/10
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/11
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/12
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/13
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/14
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/15
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/16
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/17
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/18
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/19
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/20
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/21
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/22
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/23
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/24
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/25
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/26
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/27
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/28
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/29
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/30
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/31
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/32
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/33
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/34
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/35
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/36
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/37
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/38
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/39
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/40
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/41
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/42
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/43
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/44
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/45
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/46
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/47
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
!
interface Ethernet7/48
   description IDF2 Standard Port
   no shutdown
   switchport trunk native vlan 210
   switchport phone vlan 220
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 30.00 watts
   spanning-tree portfast
   spanning-tree bpduguard enable
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 230
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout tx-period 3
   dot1x timeout reauth-period server
   dot1x reauthorization request limit 3
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel11 | L2_SPINES_Port-Channel491 | trunk | 10,210,220,230 | - | - | - | - | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel11
   description L2_SPINES_Port-Channel491
   no shutdown
   switchport trunk allowed vlan 10,210,220,230
   switchport mode trunk
   switchport
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan10 | Inband Management | default | 1500 | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| Vlan10 |  default  |  10.10.10.8/24  |  -  |  -  |  -  |  -  |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan10
   description Inband Management
   no shutdown
   mtu 1500
   ip address 10.10.10.8/24
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
| Ethernet3/1 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/2 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/3 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/4 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/5 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/6 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/7 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/8 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/9 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/10 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/11 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/12 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/13 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/14 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/15 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/16 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/17 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/18 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/19 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/20 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/21 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/22 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/23 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/24 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/25 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/26 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/27 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/28 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/29 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/30 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/31 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/32 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/33 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/34 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/35 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/36 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/37 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/38 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/39 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/40 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/41 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/42 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/43 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/44 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/45 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/46 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/47 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet3/48 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/1 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/2 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/3 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/4 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/5 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/6 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/7 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/8 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/9 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/10 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/11 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/12 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/13 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/14 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/15 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/16 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/17 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/18 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/19 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/20 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/21 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/22 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/23 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/24 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/25 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/26 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/27 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/28 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/29 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/30 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/31 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/32 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/33 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/34 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/35 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/36 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/37 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/38 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/39 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/40 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/41 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/42 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/43 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/44 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/45 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/46 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/47 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet4/48 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/1 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/2 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/3 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/4 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/5 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/6 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/7 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/8 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/9 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/10 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/11 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/12 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/13 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/14 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/15 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/16 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/17 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/18 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/19 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/20 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/21 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/22 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/23 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/24 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/25 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/26 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/27 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/28 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/29 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/30 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/31 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/32 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/33 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/34 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/35 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/36 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/37 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/38 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/39 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/40 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/41 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/42 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/43 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/44 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/45 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/46 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/47 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet5/48 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/1 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/2 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/3 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/4 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/5 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/6 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/7 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/8 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/9 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/10 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/11 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/12 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/13 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/14 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/15 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/16 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/17 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/18 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/19 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/20 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/21 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/22 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/23 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/24 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/25 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/26 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/27 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/28 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/29 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/30 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/31 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/32 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/33 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/34 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/35 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/36 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/37 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/38 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/39 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/40 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/41 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/42 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/43 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/44 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/45 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/46 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/47 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet6/48 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/1 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/2 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/3 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/4 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/5 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/6 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/7 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/8 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/9 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/10 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/11 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/12 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/13 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/14 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/15 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/16 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/17 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/18 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/19 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/20 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/21 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/22 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/23 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/24 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/25 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/26 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/27 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/28 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/29 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/30 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/31 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/32 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/33 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/34 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/35 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/36 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/37 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/38 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/39 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/40 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/41 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/42 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/43 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/44 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/45 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/46 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/47 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |
| Ethernet7/48 | authenticator | auto | - | True | allow vlan 230 | multi-host | True | - |

## Power Over Ethernet (PoE)

### PoE Summary

#### PoE Interfaces

| Interface | PoE Enabled | Priority | Limit | Reboot Action | Link Down Action | Shutdown Action | LLDP Negotiation | Legacy Detection |
| --------- | --------- | --------- | ----------- | ----------- | ----------- | ----------- | --------- | --------- |
| Ethernet3/1 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/2 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/3 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/4 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/5 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/6 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/7 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/8 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/9 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/10 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/11 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/12 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/13 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/14 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/15 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/16 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/17 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/18 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/19 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/20 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/21 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/22 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/23 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/24 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/25 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/26 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/27 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/28 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/29 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/30 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/31 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/32 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/33 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/34 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/35 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/36 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/37 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/38 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/39 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/40 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/41 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/42 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/43 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/44 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/45 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/46 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/47 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet3/48 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/1 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/2 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/3 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/4 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/5 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/6 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/7 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/8 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/9 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/10 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/11 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/12 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/13 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/14 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/15 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/16 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/17 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/18 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/19 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/20 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/21 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/22 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/23 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/24 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/25 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/26 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/27 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/28 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/29 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/30 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/31 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/32 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/33 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/34 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/35 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/36 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/37 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/38 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/39 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/40 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/41 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/42 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/43 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/44 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/45 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/46 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/47 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet4/48 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/1 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/2 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/3 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/4 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/5 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/6 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/7 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/8 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/9 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/10 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/11 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/12 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/13 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/14 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/15 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/16 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/17 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/18 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/19 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/20 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/21 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/22 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/23 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/24 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/25 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/26 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/27 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/28 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/29 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/30 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/31 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/32 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/33 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/34 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/35 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/36 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/37 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/38 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/39 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/40 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/41 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/42 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/43 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/44 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/45 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/46 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/47 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet5/48 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/1 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/2 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/3 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/4 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/5 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/6 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/7 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/8 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/9 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/10 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/11 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/12 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/13 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/14 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/15 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/16 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/17 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/18 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/19 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/20 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/21 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/22 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/23 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/24 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/25 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/26 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/27 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/28 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/29 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/30 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/31 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/32 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/33 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/34 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/35 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/36 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/37 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/38 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/39 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/40 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/41 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/42 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/43 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/44 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/45 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/46 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/47 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet6/48 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/1 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/2 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/3 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/4 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/5 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/6 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/7 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/8 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/9 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/10 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/11 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/12 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/13 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/14 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/15 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/16 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/17 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/18 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/19 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/20 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/21 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/22 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/23 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/24 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/25 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/26 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/27 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/28 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/29 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/30 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/31 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/32 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/33 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/34 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/35 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/36 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/37 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/38 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/39 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/40 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/41 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/42 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/43 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/44 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/45 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/46 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/47 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |
| Ethernet7/48 | True | critical | 30.00 watts | maintain | maintain | power-off | - | - |

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
