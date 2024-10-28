# pf2

## Table of Contents

- [Management](#management)
  - [Agents](#agents)
  - [Management Interfaces](#management-interfaces)
  - [DNS Domain](#dns-domain)
  - [IP Name Servers](#ip-name-servers)
  - [NTP](#ntp)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [Enable Password](#enable-password)
  - [AAA Authorization](#aaa-authorization)
- [Management Security](#management-security)
  - [Management Security Summary](#management-security-summary)
  - [Management Security SSL Profiles](#management-security-ssl-profiles)
  - [SSL profile STUN-DTLS Certificates Summary](#ssl-profile-stun-dtls-certificates-summary)
  - [Management Security Device Configuration](#management-security-device-configuration)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
  - [Flow Tracking](#flow-tracking)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [IP Security](#ip-security)
  - [IKE policies](#ike-policies)
  - [Security Association policies](#security-association-policies)
  - [IPSec profiles](#ipsec-profiles)
  - [IP Security Device Configuration](#ip-security-device-configuration)
- [Interfaces](#interfaces)
  - [DPS Interfaces](#dps-interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [VXLAN Interface](#vxlan-interface)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [Router Adaptive Virtual Topology](#router-adaptive-virtual-topology)
  - [Router Traffic-Engineering](#router-traffic-engineering)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [Filters](#filters)
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)
  - [IP Extended Community Lists](#ip-extended-community-lists)
- [ACL](#acl)
  - [IP Access-lists](#ip-access-lists)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Platform](#platform)
  - [Platform Summary](#platform-summary)
  - [Platform Device Configuration](#platform-device-configuration)
- [Application Traffic Recognition](#application-traffic-recognition)
  - [Applications](#applications)
  - [Application Profiles](#application-profiles)
  - [Field Sets](#field-sets)
  - [Router Application-Traffic-Recognition Device Configuration](#router-application-traffic-recognition-device-configuration)
  - [Router Path-selection](#router-path-selection)
- [STUN](#stun)
  - [STUN Server](#stun-server)
  - [STUN Device Configuration](#stun-device-configuration)

## Management

### Agents

#### Agent KernelFib

##### Environment Variables

| Name | Value |
| ---- | ----- |
| KERNELFIB_PROGRAM_ALL_ECMP | 1 |

#### Agents Device Configuration

```eos
!
agent KernelFib environment KERNELFIB_PROGRAM_ALL_ECMP=1
```

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | 192.168.17.11/24 | 192.168.17.1 |

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
   ip address 192.168.17.11/24
   no lldp transmit
   no lldp receive
```

### DNS Domain

DNS domain: wan.example.local

#### DNS Domain Device Configuration

```eos
dns domain wan.example.local
!
```

### IP Name Servers

#### IP Name Servers Summary

| Name Server | VRF | Priority |
| ----------- | --- | -------- |
| 192.168.17.1 | MGMT | - |

#### IP Name Servers Device Configuration

```eos
ip name-server vrf MGMT 192.168.17.1
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
| 0.pool.ntp.org | MGMT | True | - | - | - | - | - | - | - |

#### NTP Device Configuration

```eos
!
ntp local-interface vrf MGMT Management1
ntp server vrf MGMT 0.pool.ntp.org prefer
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
| ansible | 15 | network-admin | False | - |
| arista | 15 | network-admin | False | - |
| cvpadmin | 15 | network-admin | False | - |

#### Local Users Device Configuration

```eos
!
username ansible privilege 15 role network-admin secret sha512 <removed>
username arista privilege 15 role network-admin secret sha512 <removed>
username cvpadmin privilege 15 role network-admin secret sha512 <removed>
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

## Management Security

### Management Security Summary

| Settings | Value |
| -------- | ----- |

### Management Security SSL Profiles

| SSL Profile Name | TLS protocol accepted | Certificate filename | Key filename | Cipher List | CRLs |
| ---------------- | --------------------- | -------------------- | ------------ | ----------- | ---- |
| STUN-DTLS | 1.2 | STUN-DTLS.crt | STUN-DTLS.key | - | - |

### SSL profile STUN-DTLS Certificates Summary

| Trust Certificates | Requirement | Policy | System |
| ------------------ | ----------- | ------ | ------ |
| aristaDeviceCertProvisionerDefaultRootCA.crt | - | - | - |

### Management Security Device Configuration

```eos
!
management security
   !
   ssl profile STUN-DTLS
      tls versions 1.2
      trust certificate aristaDeviceCertProvisionerDefaultRootCA.crt
      certificate STUN-DTLS.crt key STUN-DTLS.key
```

## Monitoring

### TerminAttr Daemon

#### TerminAttr Daemon Summary

| CV Compression | CloudVision Servers | VRF | Authentication | Smash Excludes | Ingest Exclude | Bypass AAA |
| -------------- | ------------------- | --- | -------------- | -------------- | -------------- | ---------- |
| gzip | www.cv-staging.corp.arista.io:443 | MGMT | token-secure,/tmp/cv-onboarding-token | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | False |

#### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvaddr=www.cv-staging.corp.arista.io:443 -cvauth=token-secure,/tmp/cv-onboarding-token -cvvrf=MGMT -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -taillogs
   no shutdown
```

### Flow Tracking

#### Flow Tracking Hardware

##### Trackers Summary

| Tracker Name | Record Export On Inactive Timeout | Record Export On Interval | Number of Exporters | Applied On |
| ------------ | --------------------------------- | ------------------------- | ------------------- | ---------- |
| FLOW-TRACKER | 70000 | 5000 | 1 | Dps1 |

##### Exporters Summary

| Tracker Name | Exporter Name | Collector IP/Host | Collector Port | Local Interface |
| ------------ | ------------- | ----------------- | -------------- | --------------- |
| FLOW-TRACKER | CV-TELEMETRY | - | - | Loopback0 |

#### Flow Tracking Device Configuration

```eos
!
flow tracking hardware
   tracker FLOW-TRACKER
      record export on inactive timeout 70000
      record export on interval 5000
      exporter CV-TELEMETRY
         collector 127.0.0.1
         local interface Loopback0
   no shutdown
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **none**

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode none
```

## IP Security

### IKE policies

| Policy name | IKE lifetime | Encryption | DH group | Local ID |
| ----------- | ------------ | ---------- | -------- | -------- |
| CP-IKE-POLICY | - | - | - | 192.168.42.2 |

### Security Association policies

| Policy name | ESP Integrity | ESP Encryption | Lifetime | PFS DH Group |
| ----------- | ------------- | -------------- | -------- | ------------ |
| CP-SA-POLICY | - | aes256gcm128 | - | 14 |

### IPSec profiles

| Profile name | IKE policy | SA policy | Connection | DPD Interval | DPD Time | DPD action | Mode | Flow Parallelization |
| ------------ | ---------- | ----------| ---------- | ------------ | -------- | ---------- | ---- | -------------------- |
| CP-PROFILE | CP-IKE-POLICY | CP-SA-POLICY | start | - | - | - | transport | - |

### IP Security Device Configuration

```eos
!
ip security
   ike policy CP-IKE-POLICY
      local-id 192.168.42.2
   !
   sa policy CP-SA-POLICY
      esp encryption aes256gcm128
      pfs dh-group 14
   !
   profile CP-PROFILE
      ike-policy CP-IKE-POLICY
      sa-policy CP-SA-POLICY
      connection start
      shared-key 7 <removed>
      dpd 10 50 clear
      mode transport
```

## Interfaces

### DPS Interfaces

#### DPS Interfaces Summary

| Interface | IP address | Shutdown | MTU | Flow tracker(s) | TCP MSS Ceiling |
| --------- | ---------- | -------- | --- | --------------- | --------------- |
| Dps1 | 192.168.42.2/32 | - | 9194 | Hardware: FLOW-TRACKER |  |

#### DPS Interfaces Device Configuration

```eos
!
interface Dps1
   description DPS Interface
   mtu 9194
   flow tracker hardware FLOW-TRACKER
   ip address 192.168.42.2/32
```

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | ACME-MPLS-INC_mpls-pf2_mpls-cloud_Ethernet2 | - | 172.18.200.2/24 | default | - | False | - | - |
| Ethernet2 | GLOBAL-INTERNET-LIMITED_inet-pf2_inet-cloud_Ethernet2 | - | 100.64.200.2/24 | default | - | False | ACL-PF-INTERNET-IN_Ethernet2 | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description ACME-MPLS-INC_mpls-pf2_mpls-cloud_Ethernet2
   no shutdown
   no switchport
   ip address 172.18.200.2/24
!
interface Ethernet2
   description GLOBAL-INTERNET-LIMITED_inet-pf2_inet-cloud_Ethernet2
   no shutdown
   no switchport
   ip address 100.64.200.2/24
   ip access-group ACL-PF-INTERNET-IN_Ethernet2 in
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | ROUTER_ID | default | 192.168.255.2/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | ROUTER_ID | default | - |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description ROUTER_ID
   no shutdown
   ip address 192.168.255.2/32
```

### VXLAN Interface

#### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| Source Interface | Dps1 |
| UDP port | 4789 |

##### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| BLUE | 100 | - |
| default | 1 | - |
| RED | 101 | - |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description pf2_VTEP
   vxlan source-interface Dps1
   vxlan udp-port 4789
   vxlan vrf BLUE vni 100
   vxlan vrf default vni 1
   vxlan vrf RED vni 101
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
| default | False |
| MGMT | false |

### Static Routes

#### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP | Exit interface | Administrative Distance | Tag | Route Name | Metric |
| --- | ------------------ | ----------- | -------------- | ----------------------- | --- | ---------- | ------ |
| MGMT | 0.0.0.0/0 | 192.168.17.1 | - | 1 | - | - | - |
| default | 172.18.0.0/16 | 172.18.200.1 | - | 1 | - | - | - |
| default | 0.0.0.0/0 | 100.64.200.1 | - | 1 | - | - | - |

#### Static Routes Device Configuration

```eos
!
ip route 0.0.0.0/0 100.64.200.1
ip route 172.18.0.0/16 172.18.200.1
ip route vrf MGMT 0.0.0.0/0 192.168.17.1
```

### Router Adaptive Virtual Topology

#### Router Adaptive Virtual Topology Summary

Topology role: pathfinder

#### AVT Profiles

| Profile name | Load balance policy | Internet exit policy |
| ------------ | ------------------- | -------------------- |
| BLUE-POLICY-DEFAULT | LB-BLUE-POLICY-DEFAULT | - |
| BLUE-POLICY-VIDEO | LB-BLUE-POLICY-VIDEO | - |
| BLUE-POLICY-VOICE | LB-BLUE-POLICY-VOICE | - |
| DEFAULT-POLICY-CONTROL-PLANE | LB-DEFAULT-POLICY-CONTROL-PLANE | - |
| DEFAULT-POLICY-DEFAULT | LB-DEFAULT-POLICY-DEFAULT | - |
| RED-POLICY-CRITICAL-SECRET-DATA | LB-RED-POLICY-CRITICAL-SECRET-DATA | - |
| RED-POLICY-NORMAL-DATA | LB-RED-POLICY-NORMAL-DATA | - |
| RED-POLICY-NOT-SO-IMPORTANT-DATA | LB-RED-POLICY-NOT-SO-IMPORTANT-DATA | - |

#### AVT Policies

##### AVT policy BLUE-POLICY

| Application profile | AVT Profile | Traffic Class | DSCP |
| ------------------- | ----------- | ------------- | ---- |
| VIDEO | BLUE-POLICY-VIDEO | - | - |
| VOICE | BLUE-POLICY-VOICE | - | 46 |
| default | BLUE-POLICY-DEFAULT | - | - |

##### AVT policy DEFAULT-POLICY-WITH-CP

| Application profile | AVT Profile | Traffic Class | DSCP |
| ------------------- | ----------- | ------------- | ---- |
| APP-PROFILE-CONTROL-PLANE | DEFAULT-POLICY-CONTROL-PLANE | - | - |
| default | DEFAULT-POLICY-DEFAULT | - | - |

##### AVT policy RED-POLICY

| Application profile | AVT Profile | Traffic Class | DSCP |
| ------------------- | ----------- | ------------- | ---- |
| CRITICAL-SECRET-DATA | RED-POLICY-CRITICAL-SECRET-DATA | - | - |
| NORMAL-DATA | RED-POLICY-NORMAL-DATA | - | - |
| NOT-SO-IMPORTANT-DATA | RED-POLICY-NOT-SO-IMPORTANT-DATA | - | - |

#### VRFs configuration

##### VRF BLUE

| AVT policy |
| ---------- |
| BLUE-POLICY |

| AVT Profile | AVT ID |
| ----------- | ------ |
| BLUE-POLICY-DEFAULT | 1 |
| BLUE-POLICY-VIDEO | 2 |
| BLUE-POLICY-VOICE | 3 |

##### VRF default

| AVT policy |
| ---------- |
| DEFAULT-POLICY-WITH-CP |

| AVT Profile | AVT ID |
| ----------- | ------ |
| DEFAULT-POLICY-DEFAULT | 1 |
| DEFAULT-POLICY-CONTROL-PLANE | 254 |

##### VRF RED

| AVT policy |
| ---------- |
| RED-POLICY |

| AVT Profile | AVT ID |
| ----------- | ------ |
| RED-POLICY-CRITICAL-SECRET-DATA | 2 |
| RED-POLICY-NORMAL-DATA | 3 |
| RED-POLICY-NOT-SO-IMPORTANT-DATA | 4 |

#### Router Adaptive Virtual Topology Configuration

```eos
!
router adaptive-virtual-topology
   topology role pathfinder
   !
   policy BLUE-POLICY
      !
      match application-profile VIDEO
         avt profile BLUE-POLICY-VIDEO
      !
      match application-profile VOICE
         avt profile BLUE-POLICY-VOICE
         dscp 46
      !
      match application-profile default
         avt profile BLUE-POLICY-DEFAULT
   !
   policy DEFAULT-POLICY-WITH-CP
      !
      match application-profile APP-PROFILE-CONTROL-PLANE
         avt profile DEFAULT-POLICY-CONTROL-PLANE
      !
      match application-profile default
         avt profile DEFAULT-POLICY-DEFAULT
   !
   policy RED-POLICY
      !
      match application-profile CRITICAL-SECRET-DATA
         avt profile RED-POLICY-CRITICAL-SECRET-DATA
      !
      match application-profile NORMAL-DATA
         avt profile RED-POLICY-NORMAL-DATA
      !
      match application-profile NOT-SO-IMPORTANT-DATA
         avt profile RED-POLICY-NOT-SO-IMPORTANT-DATA
   !
   profile BLUE-POLICY-DEFAULT
      path-selection load-balance LB-BLUE-POLICY-DEFAULT
   !
   profile BLUE-POLICY-VIDEO
      path-selection load-balance LB-BLUE-POLICY-VIDEO
   !
   profile BLUE-POLICY-VOICE
      path-selection load-balance LB-BLUE-POLICY-VOICE
   !
   profile DEFAULT-POLICY-CONTROL-PLANE
      path-selection load-balance LB-DEFAULT-POLICY-CONTROL-PLANE
   !
   profile DEFAULT-POLICY-DEFAULT
      path-selection load-balance LB-DEFAULT-POLICY-DEFAULT
   !
   profile RED-POLICY-CRITICAL-SECRET-DATA
      path-selection load-balance LB-RED-POLICY-CRITICAL-SECRET-DATA
   !
   profile RED-POLICY-NORMAL-DATA
      path-selection load-balance LB-RED-POLICY-NORMAL-DATA
   !
   profile RED-POLICY-NOT-SO-IMPORTANT-DATA
      path-selection load-balance LB-RED-POLICY-NOT-SO-IMPORTANT-DATA
   !
   vrf BLUE
      avt policy BLUE-POLICY
      avt profile BLUE-POLICY-DEFAULT id 1
      avt profile BLUE-POLICY-VIDEO id 2
      avt profile BLUE-POLICY-VOICE id 3
   !
   vrf default
      avt policy DEFAULT-POLICY-WITH-CP
      avt profile DEFAULT-POLICY-DEFAULT id 1
      avt profile DEFAULT-POLICY-CONTROL-PLANE id 254
   !
   vrf RED
      avt policy RED-POLICY
      avt profile RED-POLICY-CRITICAL-SECRET-DATA id 2
      avt profile RED-POLICY-NORMAL-DATA id 3
      avt profile RED-POLICY-NOT-SO-IMPORTANT-DATA id 4
```

### Router Traffic-Engineering

- Traffic Engineering is enabled.

#### Router Traffic Engineering Device Configuration

```eos
!
router traffic-engineering
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65000 | 192.168.255.2 |

| BGP AS | Cluster ID |
| ------ | --------- |
| 65000 | 192.168.255.2 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| maximum-paths 16 |

#### Router BGP Listen Ranges

| Prefix | Peer-ID Include Router ID | Peer Group | Peer-Filter | Remote-AS | VRF |
| ------ | ------------------------- | ---------- | ----------- | --------- | --- |
| 192.168.42.0/24 | - | WAN-OVERLAY-PEERS | - | 65000 | default |

#### Router BGP Peer Groups

##### WAN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | wan |
| Remote AS | 65000 |
| Route Reflector Client | Yes |
| Source | Dps1 |
| BFD | True |
| BFD Timers | interval: 1000, min_rx: 1000, multiplier: 10 |
| TTL Max Hops | 1 |
| Send community | all |
| Maximum routes | 0 (no limit) |

##### WAN-RR-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | wan |
| Remote AS | 65000 |
| Route Reflector Client | Yes |
| Source | Dps1 |
| BFD | True |
| BFD Timers | interval: 1000, min_rx: 1000, multiplier: 10 |
| TTL Max Hops | 1 |
| Send community | all |
| Maximum routes | 0 (no limit) |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 192.168.42.1 | Inherited from peer group WAN-RR-OVERLAY-PEERS | default | - | Inherited from peer group WAN-RR-OVERLAY-PEERS | Inherited from peer group WAN-RR-OVERLAY-PEERS | - | Inherited from peer group WAN-RR-OVERLAY-PEERS(interval: 1000, min_rx: 1000, multiplier: 10) | - | Inherited from peer group WAN-RR-OVERLAY-PEERS | - | Inherited from peer group WAN-RR-OVERLAY-PEERS |

#### Router BGP EVPN Address Family

- Next-hop resolution is **disabled**

##### EVPN Peer Groups

| Peer Group | Activate | Encapsulation |
| ---------- | -------- | ------------- |
| WAN-OVERLAY-PEERS | True | path-selection |
| WAN-RR-OVERLAY-PEERS | True | path-selection |

#### Router BGP IPv4 SR-TE Address Family

##### IPv4 SR-TE Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out |
| ---------- | -------- | ------------ | ------------- |
| WAN-OVERLAY-PEERS | True | - | - |
| WAN-RR-OVERLAY-PEERS | True | - | - |

#### Router BGP Link-State Address Family

##### Link-State Peer Groups

| Peer Group | Activate | Missing policy In action | Missing policy Out action |
| ---------- | -------- | ------------------------ | ------------------------- |
| WAN-OVERLAY-PEERS | True | - | deny |
| WAN-RR-OVERLAY-PEERS | True | - | - |

##### Link-State Path Selection Configuration

| Settings | Value |
| -------- | ----- |
| Role(s) | consumer<br>propagator |

#### Router BGP Path-Selection Address Family

##### Path-Selection Peer Groups

| Peer Group | Activate |
| ---------- | -------- |
| WAN-OVERLAY-PEERS | True |
| WAN-RR-OVERLAY-PEERS | True |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| default | 192.168.255.2:1 | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65000
   router-id 192.168.255.2
   no bgp default ipv4-unicast
   bgp cluster-id 192.168.255.2
   maximum-paths 16
   bgp listen range 192.168.42.0/24 peer-group WAN-OVERLAY-PEERS remote-as 65000
   neighbor WAN-OVERLAY-PEERS peer group
   neighbor WAN-OVERLAY-PEERS remote-as 65000
   neighbor WAN-OVERLAY-PEERS update-source Dps1
   neighbor WAN-OVERLAY-PEERS bfd
   neighbor WAN-OVERLAY-PEERS bfd interval 1000 min-rx 1000 multiplier 10
   neighbor WAN-OVERLAY-PEERS ttl maximum-hops 1
   neighbor WAN-OVERLAY-PEERS route-reflector-client
   neighbor WAN-OVERLAY-PEERS password 7 <removed>
   neighbor WAN-OVERLAY-PEERS send-community
   neighbor WAN-OVERLAY-PEERS maximum-routes 0
   neighbor WAN-RR-OVERLAY-PEERS peer group
   neighbor WAN-RR-OVERLAY-PEERS remote-as 65000
   neighbor WAN-RR-OVERLAY-PEERS update-source Dps1
   neighbor WAN-RR-OVERLAY-PEERS bfd
   neighbor WAN-RR-OVERLAY-PEERS bfd interval 1000 min-rx 1000 multiplier 10
   neighbor WAN-RR-OVERLAY-PEERS ttl maximum-hops 1
   neighbor WAN-RR-OVERLAY-PEERS route-reflector-client
   neighbor WAN-RR-OVERLAY-PEERS password 7 <removed>
   neighbor WAN-RR-OVERLAY-PEERS send-community
   neighbor WAN-RR-OVERLAY-PEERS maximum-routes 0
   neighbor 192.168.42.1 peer group WAN-RR-OVERLAY-PEERS
   neighbor 192.168.42.1 description pf1_Dps1
   redistribute connected route-map RM-CONN-2-BGP
   !
   address-family evpn
      neighbor WAN-OVERLAY-PEERS activate
      neighbor WAN-OVERLAY-PEERS encapsulation path-selection
      neighbor WAN-RR-OVERLAY-PEERS activate
      neighbor WAN-RR-OVERLAY-PEERS encapsulation path-selection
      next-hop resolution disabled
   !
   address-family ipv4
      no neighbor WAN-OVERLAY-PEERS activate
      no neighbor WAN-RR-OVERLAY-PEERS activate
   !
   address-family ipv4 sr-te
      neighbor WAN-OVERLAY-PEERS activate
      neighbor WAN-RR-OVERLAY-PEERS activate
   !
   address-family link-state
      neighbor WAN-OVERLAY-PEERS activate
      neighbor WAN-OVERLAY-PEERS missing-policy direction out action deny
      neighbor WAN-RR-OVERLAY-PEERS activate
      path-selection role consumer propagator
   !
   address-family path-selection
      bgp additional-paths receive
      bgp additional-paths send any
      neighbor WAN-OVERLAY-PEERS activate
      neighbor WAN-RR-OVERLAY-PEERS activate
   !
   vrf default
      rd 192.168.255.2:1
      route-target import evpn 1:1
      route-target export evpn 1:1
      route-target export evpn route-map RM-EVPN-EXPORT-VRF-DEFAULT
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

## Filters

### Prefix-lists

#### Prefix-lists Summary

##### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 192.168.255.0/24 eq 32 |

#### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 192.168.255.0/24 eq 32
```

### Route-maps

#### Route-maps Summary

##### RM-CONN-2-BGP

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY | extcommunity soo 192.168.255.2:0 additive | - | - |

##### RM-EVPN-EXPORT-VRF-DEFAULT

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | extcommunity ECL-EVPN-SOO | - | - | - |

#### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   set extcommunity soo 192.168.255.2:0 additive
!
route-map RM-EVPN-EXPORT-VRF-DEFAULT permit 10
   match extcommunity ECL-EVPN-SOO
```

### IP Extended Community Lists

#### IP Extended Community Lists Summary

| List Name | Type | Extended Communities |
| --------- | ---- | -------------------- |
| ECL-EVPN-SOO | permit | soo 192.168.255.2:0 |

#### IP Extended Community Lists Device Configuration

```eos
!
ip extcommunity-list ECL-EVPN-SOO permit soo 192.168.255.2:0
```

## ACL

### IP Access-lists

#### IP Access-lists Device Configuration

```eos
!
ip access-list ACL-PF-INTERNET-IN_Ethernet2
   1 remark Not for PRODUCTION: This ACL is built this way because the lab has an out-of-band interface
   10 permit udp any host 100.64.200.2 eq isakmp non500-isakmp
   20 permit udp any host 100.64.200.2 eq 3478
   30 permit icmp any host 100.64.200.2
   deny ip any any
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

## Platform

### Platform Summary

#### Platform Software Forwarding Engine Summary

| Settings | Value |
| -------- | ----- |
| Maximum CPU Allocation | 1 |

### Platform Device Configuration

```eos
!
platform sfe data-plane cpu allocation maximum 1
```

## Application Traffic Recognition

### Applications

#### IPv4 Applications

| Name | Source Prefix | Destination Prefix | Protocols | Protocol Ranges | TCP Source Port Set | TCP Destination Port Set | UDP Source Port Set | UDP Destination Port Set | DSCP |
| ---- | ------------- | ------------------ | --------- | --------------- | ------------------- | ------------------------ | ------------------- | ------------------------ | ---- |
| APP-CONTROL-PLANE | PFX-LOCAL-VTEP-IP | - | - | - | - | - | - | - | - |
| CRITICAL-SECRET-DATA-APP | - | - | - | - | - | - | - | - | 46 |
| NORMAL-DATA-APP | - | - | - | - | - | - | - | - | af23 |
| NOT-SO-IMPORTANT-DATA-APP | - | - | - | - | - | - | - | - | 0 |
| VIDEO-APP | - | - | tcp, udp | - | - | VIDEO-PORTS | - | VIDEO-PORTS | - |
| VOICE-APP | - | - | tcp | - | - | VOICE-PORTS | - | - | - |

### Application Profiles

#### Application Profile Name APP-PROFILE-CONTROL-PLANE

| Type | Name | Service |
| ---- | ---- | ------- |
| application | APP-CONTROL-PLANE | - |

#### Application Profile Name CRITICAL-SECRET-DATA

| Type | Name | Service |
| ---- | ---- | ------- |
| application | CRITICAL-SECRET-DATA-APP | - |

#### Application Profile Name NORMAL-DATA

| Type | Name | Service |
| ---- | ---- | ------- |
| application | NORMAL-DATA-APP | - |

#### Application Profile Name NOT-SO-IMPORTANT-DATA

| Type | Name | Service |
| ---- | ---- | ------- |
| application | NOT-SO-IMPORTANT-DATA-APP | - |

#### Application Profile Name VIDEO

| Type | Name | Service |
| ---- | ---- | ------- |
| application | VIDEO-APP | - |

#### Application Profile Name VOICE

| Type | Name | Service |
| ---- | ---- | ------- |
| application | VOICE-APP | - |

### Field Sets

#### L4 Port Sets

| Name | Ports |
| ---- | ----- |
| VIDEO-PORTS | 4242-4244 |
| VOICE-PORTS | 666-667 |

#### IPv4 Prefix Sets

| Name | Prefixes |
| ---- | -------- |
| PFX-LOCAL-VTEP-IP | 192.168.42.2/32 |

### Router Application-Traffic-Recognition Device Configuration

```eos
!
application traffic recognition
   !
   application ipv4 APP-CONTROL-PLANE
      source prefix field-set PFX-LOCAL-VTEP-IP
   !
   application ipv4 CRITICAL-SECRET-DATA-APP
      dscp 46
   !
   application ipv4 NORMAL-DATA-APP
      dscp af23
   !
   application ipv4 NOT-SO-IMPORTANT-DATA-APP
      dscp 0
   !
   application ipv4 VIDEO-APP
      protocol tcp destination port field-set VIDEO-PORTS
      protocol udp destination port field-set VIDEO-PORTS
   !
   application ipv4 VOICE-APP
      protocol tcp destination port field-set VOICE-PORTS
   !
   application-profile APP-PROFILE-CONTROL-PLANE
      application APP-CONTROL-PLANE
   !
   application-profile CRITICAL-SECRET-DATA
      application CRITICAL-SECRET-DATA-APP
   !
   application-profile NORMAL-DATA
      application NORMAL-DATA-APP
   !
   application-profile NOT-SO-IMPORTANT-DATA
      application NOT-SO-IMPORTANT-DATA-APP
   !
   application-profile VIDEO
      application VIDEO-APP
   !
   application-profile VOICE
      application VOICE-APP
   !
   field-set ipv4 prefix PFX-LOCAL-VTEP-IP
      192.168.42.2/32
   !
   field-set l4-port VIDEO-PORTS
      4242-4244
   !
   field-set l4-port VOICE-PORTS
      666-667
```

### Router Path-selection

#### Router Path-selection Summary

| Setting | Value |
| ------  | ----- |
| Dynamic peers source | STUN |

#### TCP MSS Ceiling Configuration

| IPV4 segment size | Direction |
| ----------------- | --------- |
| auto | ingress |

#### Path Groups

##### Path Group INTERNET

| Setting | Value |
| ------  | ----- |
| Path Group ID | 102 |
| IPSec profile | CP-PROFILE |

###### Local Interfaces

| Interface name | Public address | STUN server profile(s) |
| -------------- | -------------- | ---------------------- |
| Ethernet2 | - |  |

###### Static Peers

| Router IP | Name | IPv4 address(es) |
| --------- | ---- | ---------------- |
| 192.168.42.1 | pf1 | 100.64.100.2 |

##### Path Group LAN_HA

| Setting | Value |
| ------  | ----- |
| Path Group ID | 65535 |
| Flow assignment | LAN |

##### Path Group MPLS

| Setting | Value |
| ------  | ----- |
| Path Group ID | 101 |
| IPSec profile | CP-PROFILE |

###### Local Interfaces

| Interface name | Public address | STUN server profile(s) |
| -------------- | -------------- | ---------------------- |
| Ethernet1 | - |  |

###### Static Peers

| Router IP | Name | IPv4 address(es) |
| --------- | ---- | ---------------- |
| 192.168.42.1 | pf1 | 172.18.100.2 |

#### Load-balance Policies

| Policy Name | Jitter (ms) | Latency (ms) | Loss Rate (%) | Path Groups (priority) | Lowest Hop Count |
| ----------- | ----------- | ------------ | ------------- | ---------------------- | ---------------- |
| LB-BLUE-POLICY-DEFAULT | - | - | - | INTERNET (1)<br>LAN_HA (1)<br>MPLS (1) | False |
| LB-BLUE-POLICY-VIDEO | - | - | - | INTERNET (1)<br>LAN_HA (1)<br>MPLS (2) | False |
| LB-BLUE-POLICY-VOICE | 30 | 150 | 1 | LAN_HA (1)<br>MPLS (1)<br>INTERNET (2) | True |
| LB-DEFAULT-POLICY-CONTROL-PLANE | - | - | - | INTERNET (1)<br>LAN_HA (1)<br>MPLS (1) | False |
| LB-DEFAULT-POLICY-DEFAULT | - | - | - | INTERNET (1)<br>LAN_HA (1)<br>MPLS (1) | False |
| LB-RED-POLICY-CRITICAL-SECRET-DATA | - | - | - | LAN_HA (1)<br>MPLS (1) | False |
| LB-RED-POLICY-NORMAL-DATA | - | - | - | INTERNET (1)<br>LAN_HA (1)<br>MPLS (2) | False |
| LB-RED-POLICY-NOT-SO-IMPORTANT-DATA | - | - | - | INTERNET (1)<br>LAN_HA (1) | False |

#### Router Path-selection Device Configuration

```eos
!
router path-selection
   peer dynamic source stun
   tcp mss ceiling ipv4 ingress
   !
   path-group INTERNET id 102
      ipsec profile CP-PROFILE
      !
      local interface Ethernet2
      !
      peer static router-ip 192.168.42.1
         name pf1
         ipv4 address 100.64.100.2
   !
   path-group LAN_HA id 65535
      flow assignment lan
   !
   path-group MPLS id 101
      ipsec profile CP-PROFILE
      !
      local interface Ethernet1
      !
      peer static router-ip 192.168.42.1
         name pf1
         ipv4 address 172.18.100.2
   !
   load-balance policy LB-BLUE-POLICY-DEFAULT
      path-group INTERNET
      path-group LAN_HA
      path-group MPLS
   !
   load-balance policy LB-BLUE-POLICY-VIDEO
      path-group INTERNET
      path-group LAN_HA
      path-group MPLS priority 2
   !
   load-balance policy LB-BLUE-POLICY-VOICE
      latency 150
      jitter 30
      loss-rate 1
      hop count lowest
      path-group LAN_HA
      path-group MPLS
      path-group INTERNET priority 2
   !
   load-balance policy LB-DEFAULT-POLICY-CONTROL-PLANE
      path-group INTERNET
      path-group LAN_HA
      path-group MPLS
   !
   load-balance policy LB-DEFAULT-POLICY-DEFAULT
      path-group INTERNET
      path-group LAN_HA
      path-group MPLS
   !
   load-balance policy LB-RED-POLICY-CRITICAL-SECRET-DATA
      path-group LAN_HA
      path-group MPLS
   !
   load-balance policy LB-RED-POLICY-NORMAL-DATA
      path-group INTERNET
      path-group LAN_HA
      path-group MPLS priority 2
   !
   load-balance policy LB-RED-POLICY-NOT-SO-IMPORTANT-DATA
      path-group INTERNET
      path-group LAN_HA
```

## STUN

### STUN Server

| Server Local Interfaces | Bindings Timeout (s) | SSL Profile | SSL Connection Lifetime | Port |
| ----------------------- | -------------------- | ----------- | ----------------------- | ---- |
| Ethernet1<br>Ethernet2 | - | STUN-DTLS | - | 3478 |

### STUN Device Configuration

```eos
!
stun
   server
      local-interface Ethernet1
      local-interface Ethernet2
      ssl profile STUN-DTLS
```
