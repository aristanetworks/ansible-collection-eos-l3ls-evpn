# SITE2-LSR2

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
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router ISIS](#router-isis)
- [MPLS](#mpls)
  - [MPLS and LDP](#mpls-and-ldp)
  - [MPLS Interfaces](#mpls-interfaces)
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
| Management1 | OOB_MANAGEMENT | oob | MGMT | 192.168.200.104/24 | 192.168.200.5 |

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
   ip address 192.168.200.104/24
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
| Ethernet3 | P2P_SITE1-LSR2_Ethernet3 | - | 100.64.48.11/31 | default | 9178 | False | - | - |
| Ethernet12 | P2P_SITE2-LER1_Ethernet11 | 12 | *100.64.49.1/30 | **default | *9178 | *False | **- | **- |
| Ethernet13 | P2P_SITE2-LER1_Ethernet12 | 12 | *100.64.49.1/30 | **default | *9178 | *False | **- | **- |
| Ethernet14 | P2P_SITE2-LER1_Ethernet13 | 110 | *100.64.49.5/30 | **default | *9178 | *False | **- | **- |
| Ethernet15 | P2P_SITE2-LER1_Ethernet14 | 110 | *100.64.49.5/30 | **default | *9178 | *False | **- | **- |

*Inherited from Port-Channel Interface

##### IPv6

| Interface | Description | Channel Group | IPv6 Address | VRF | MTU | Shutdown | ND RA Disabled | Managed Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | ----------- | --------------| ------------ | --- | --- | -------- | -------------- | -------------------| ----------- | ------------ |
| Ethernet3 | P2P_SITE1-LSR2_Ethernet3 | - | - | default | 9178 | False | - | - | - | - |
| Ethernet12 | P2P_SITE2-LER1_Ethernet11 | 12 | *- | *default | *9178 | *False | *- | *- | *- | *- |
| Ethernet13 | P2P_SITE2-LER1_Ethernet12 | 12 | *- | *default | *9178 | *False | *- | *- | *- | *- |
| Ethernet14 | P2P_SITE2-LER1_Ethernet13 | 110 | *- | *default | *9178 | *False | *- | *- | *- | *- |
| Ethernet15 | P2P_SITE2-LER1_Ethernet14 | 110 | *- | *default | *9178 | *False | *- | *- | *- | *- |

*Inherited from Port-Channel Interface

##### ISIS

| Interface | Channel Group | ISIS Instance | ISIS BFD | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | ISIS Authentication Mode |
| --------- | ------------- | ------------- | -------- | ----------- | ---- | ----------------- | ------------- | ------------------------ |
| Ethernet3 | - | CUSTOM_NAME | - | 60 | point-to-point | level-2 | False | md5 |
| Ethernet12 | 12 | *CUSTOM_NAME | - | *60 | *point-to-point | *level-2 | *False | *md5 |
| Ethernet13 | 12 | *CUSTOM_NAME | - | *60 | *point-to-point | *level-2 | *False | *md5 |
| Ethernet14 | 110 | *CUSTOM_NAME | - | *60 | *point-to-point | *level-2 | *False | *md5 |
| Ethernet15 | 110 | *CUSTOM_NAME | - | *60 | *point-to-point | *level-2 | *False | *md5 |

*Inherited from Port-Channel Interface

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet3
   description P2P_SITE1-LSR2_Ethernet3
   no shutdown
   mtu 9178
   speed forced 40gfull
   no switchport
   ip address 100.64.48.11/31
   ipv6 enable
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
   isis enable CUSTOM_NAME
   isis circuit-type level-2
   isis metric 60
   no isis hello padding
   isis network point-to-point
   isis authentication mode md5
   isis authentication key 7 <removed>
   link-debounce time 1000

!
interface Ethernet12
   description P2P_SITE2-LER1_Ethernet11
   no shutdown
   speed forced 40gfull
   channel-group 12 mode active
!
interface Ethernet13
   description P2P_SITE2-LER1_Ethernet12
   no shutdown
   speed forced 40gfull
   channel-group 12 mode active
!
interface Ethernet14
   description P2P_SITE2-LER1_Ethernet13
   no shutdown
   speed forced 40gfull
   channel-group 110 mode active
!
interface Ethernet15
   description P2P_SITE2-LER1_Ethernet14
   no shutdown
   speed forced 40gfull
   channel-group 110 mode active
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |

##### IPv4

| Interface | Description | MLAG ID | IP Address | VRF | MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------- | ---------- | --- | --- | -------- | ------ | ------- |
| Port-Channel12 | P2P_SITE2-LER1_Port-Channel11 | - | 100.64.49.1/30 | default | 9178 | False | - | - |
| Port-Channel110 | P2P_SITE2-LER1_Port-Channel220 | - | 100.64.49.5/30 | default | 9178 | False | - | - |

##### ISIS

| Interface | ISIS Instance | ISIS BFD | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | ISIS Authentication Mode |
| --------- | ------------- | -------- | ----------- | ---- | ----------------- | ------------- | ------------------------ |
| Port-Channel12 | CUSTOM_NAME | - | 60 | point-to-point | level-2 | False | md5 |
| Port-Channel110 | CUSTOM_NAME | - | 60 | point-to-point | level-2 | False | md5 |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel12
   description P2P_SITE2-LER1_Port-Channel11
   no shutdown
   mtu 9178
   no switchport
   ip address 100.64.49.1/30
   ipv6 enable
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
   isis enable CUSTOM_NAME
   isis circuit-type level-2
   isis metric 60
   no isis hello padding
   isis network point-to-point
   isis authentication mode md5
   isis authentication key 7 <removed>
   link-debounce time 1600

!
interface Port-Channel110
   description P2P_SITE2-LER1_Port-Channel220
   no shutdown
   mtu 9178
   no switchport
   ip address 100.64.49.5/30
   ipv6 enable
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
   isis enable CUSTOM_NAME
   isis circuit-type level-2
   isis metric 60
   no isis hello padding
   isis network point-to-point
   isis authentication mode md5
   isis authentication key 7 <removed>
   link-debounce time 1600

```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | ROUTER_ID | default | 100.70.0.4/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | ROUTER_ID | default | 2000:1234:ffff:ffff::4/128 |

##### ISIS

| Interface | ISIS instance | ISIS metric | Interface mode |
| --------- | ------------- | ----------- | -------------- |
| Loopback0 | CUSTOM_NAME | - | passive |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description ROUTER_ID
   no shutdown
   ip address 100.70.0.4/32
   ipv6 address 2000:1234:ffff:ffff::4/128
   mpls ldp interface
   node-segment ipv4 index 304
   node-segment ipv6 index 304
   isis enable CUSTOM_NAME
   isis passive
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
| default | True |
| MGMT | False |

#### IP Routing Device Configuration

```eos
!
ip routing
no ip routing vrf MGMT
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| MGMT | false |

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
| Instance | CUSTOM_NAME |
| Net-ID | 49.0001.1000.7000.0004.00 |
| Type | level-2 |
| Router-ID | 100.70.0.4 |
| Log Adjacency Changes | True |
| MPLS LDP Sync Default | True |
| Advertise Passive-only | True |
| SR MPLS Enabled | True |

#### ISIS Route Timers

| Settings | Value |
| -------- | ----- |
| Local Convergence Delay | 15000 milliseconds |

#### ISIS Interfaces Summary

| Interface | ISIS Instance | ISIS Metric | Interface Mode |
| --------- | ------------- | ----------- | -------------- |
| Ethernet3 | CUSTOM_NAME | 60 | point-to-point |
| Loopback0 | CUSTOM_NAME | - | passive |

#### ISIS Segment-routing Node-SID

| Loopback | IPv4 Index | IPv6 Index |
| -------- | ---------- | ---------- |
| Loopback0 | 304 | 304 |

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
router isis CUSTOM_NAME
   net 49.0001.1000.7000.0004.00
   router-id ipv4 100.70.0.4
   is-type level-2
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

## MPLS

### MPLS and LDP

#### MPLS and LDP Summary

| Setting | Value |
| -------- | ---- |
| MPLS IP Enabled | True |
| LDP Enabled | True |
| LDP Router ID | 100.70.0.4 |
| LDP Interface Disabled Default | True |
| LDP Transport-Address Interface | Loopback0 |

#### MPLS and LDP Device Configuration

```eos
!
mpls ip
!
mpls ldp
   router-id 100.70.0.4
   transport-address interface Loopback0
   interface disabled default
   no shutdown
```

### MPLS Interfaces

| Interface | MPLS IP Enabled | LDP Enabled | IGP Sync |
| --------- | --------------- | ----------- | -------- |
| Ethernet3 | True | True | True |
| Loopback0 | - | True | - |
| Port-Channel12 | True | True | True |
| Port-Channel110 | True | True | True |

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
management security
   password encryption-key common

```
