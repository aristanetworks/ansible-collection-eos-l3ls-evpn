# hostname-set-via-hostname-var

## Table of Contents

- [Management](#management)
  - [Agents](#agents)
  - [Management Interfaces](#management-interfaces)
  - [IP Domain-list](#ip-domain-list)
  - [Clock Settings](#clock-settings)
  - [NTP](#ntp)
  - [System Control-Plane](#system-control-plane)
  - [Management SSH](#management-ssh)
  - [Management Tech-Support](#management-tech-support)
  - [IP Client Source Interfaces](#ip-client-source-interfaces)
- [CVX](#cvx)
  - [CVX Services](#cvx-services)
  - [CVX Device Configuration](#cvx-device-configuration)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [Roles](#roles)
  - [Enable Password](#enable-password)
  - [TACACS Servers](#tacacs-servers)
  - [IP TACACS Source Interfaces](#ip-tacacs-source-interfaces)
  - [RADIUS Server](#radius-server)
  - [IP RADIUS Source Interfaces](#ip-radius-source-interfaces)
  - [AAA Server Groups](#aaa-server-groups)
  - [AAA Authentication](#aaa-authentication)
  - [AAA Authorization](#aaa-authorization)
  - [AAA Accounting](#aaa-accounting)
- [Management Security](#management-security)
  - [Management Security Summary](#management-security-summary)
  - [Management Security SSL Profiles](#management-security-ssl-profiles)
  - [SSL profile test1-chain-cert Certificates Summary](#ssl-profile-test1-chain-cert-certificates-summary)
  - [SSL profile test1-trust-cert Certificates Summary](#ssl-profile-test1-trust-cert-certificates-summary)
  - [SSL profile test2-chain-cert Certificates Summary](#ssl-profile-test2-chain-cert-certificates-summary)
  - [SSL profile test2-trust-cert Certificates Summary](#ssl-profile-test2-trust-cert-certificates-summary)
  - [Password Policies](#password-policies)
  - [Session Shared-secret Profiles](#session-shared-secret-profiles)
  - [Management Security Device Configuration](#management-security-device-configuration)
- [Prompt Device Configuration](#prompt-device-configuration)
- [Aliases Device Configuration](#aliases-device-configuration)
- [DHCP Relay](#dhcp-relay)
  - [DHCP Relay Summary](#dhcp-relay-summary)
  - [DHCP Relay Device Configuration](#dhcp-relay-device-configuration)
- [DHCP Server](#dhcp-server)
  - [DHCP Servers Summary](#dhcp-servers-summary)
  - [DHCP Server Configuration](#dhcp-server-configuration)
  - [DHCP Server Interfaces](#dhcp-server-interfaces)
- [System Boot Settings](#system-boot-settings)
  - [Boot Secret Summary](#boot-secret-summary)
  - [System Boot Device Configuration](#system-boot-device-configuration)
- [Monitoring](#monitoring)
  - [Custom daemons](#custom-daemons)
  - [Logging](#logging)
  - [MCS Client Summary](#mcs-client-summary)
  - [Monitor Sessions](#monitor-sessions)
  - [Tap Aggregation](#tap-aggregation)
  - [SFlow](#sflow)
  - [VM Tracer Sessions](#vm-tracer-sessions)
  - [Event Handler](#event-handler)
  - [Object Tracking](#object-tracking)
  - [Monitor Telemetry Postcard Policy](#monitor-telemetry-postcard-policy)
  - [Monitor Server Radius Summary](#monitor-server-radius-summary)
- [Monitor Connectivity](#monitor-connectivity)
  - [Global Configuration](#global-configuration)
  - [VRF Configuration](#vrf-configuration)
  - [Monitor Connectivity Device Configuration](#monitor-connectivity-device-configuration)
- [Monitor Layer 1 Logging](#monitor-layer-1-logging)
  - [Monitor Layer 1 Device Configuration](#monitor-layer-1-device-configuration)
  - [Link Tracking](#link-tracking)
- [MLAG](#mlag)
  - [MLAG Summary](#mlag-summary)
  - [MLAG Device Configuration](#mlag-device-configuration)
- [LACP](#lacp)
  - [LACP Summary](#lacp-summary)
  - [LACP Device Configuration](#lacp-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Device Configuration](#internal-vlan-allocation-policy-device-configuration)
- [VLANs](#vlans)
  - [VLANs Summary](#vlans-summary)
  - [VLANs Device Configuration](#vlans-device-configuration)
- [MAC Address Table](#mac-address-table)
  - [MAC Address Table Summary](#mac-address-table-summary)
  - [MAC Address Table Device Configuration](#mac-address-table-device-configuration)
- [IP Security](#ip-security)
  - [IKE policies](#ike-policies)
  - [Security Association policies](#security-association-policies)
  - [IPSec profiles](#ipsec-profiles)
  - [Key controller](#key-controller)
  - [IP Security Device Configuration](#ip-security-device-configuration)
- [Interfaces](#interfaces)
  - [Switchport Default](#switchport-default)
  - [Interface Profiles](#interface-profiles)
  - [DPS Interfaces](#dps-interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [Tunnel Interfaces](#tunnel-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
  - [VXLAN Interface](#vxlan-interface)
- [Switchport Port-security](#switchport-port-security)
  - [Switchport Port-security Summary](#switchport-port-security-summary)
  - [Switchport Port-security Device Configuration](#switchport-port-security-device-configuration)
- [Routing](#routing)
  - [Service Routing Configuration BGP](#service-routing-configuration-bgp)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [Static Routes](#static-routes)
  - [IPv6 Static Routes](#ipv6-static-routes)
  - [IPv6 Neighbors](#ipv6-neighbors)
  - [ARP](#arp)
  - [Router Adaptive Virtual Topology](#router-adaptive-virtual-topology)
  - [Router General](#router-general)
- [Router Service Insertion](#router-service-insertion)
  - [Connections](#connections)
  - [Router Service Insertion Configuration](#router-service-insertion-configuration)
  - [Router Traffic-Engineering](#router-traffic-engineering)
  - [Router BGP](#router-bgp)
  - [PBR Policy Maps](#pbr-policy-maps)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
  - [BFD Interfaces](#bfd-interfaces)
- [MPLS](#mpls)
  - [MPLS Interfaces](#mpls-interfaces)
- [Patch Panel](#patch-panel)
  - [Patch Panel Summary](#patch-panel-summary)
  - [Patch Panel Device Configuration](#patch-panel-device-configuration)
- [Queue Monitor](#queue-monitor)
  - [Queue Monitor Length](#queue-monitor-length)
  - [Queue Monitor Streaming](#queue-monitor-streaming)
  - [Queue Monitor Configuration](#queue-monitor-configuration)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
  - [Router Multicast](#router-multicast)
  - [PIM Sparse Mode](#pim-sparse-mode)
  - [Router MSDP](#router-msdp)
  - [Router IGMP](#router-igmp)
- [Filters](#filters)
  - [IP Community-lists](#ip-community-lists)
  - [Peer Filters](#peer-filters)
  - [Route-maps](#route-maps)
  - [IP Extended Community Lists](#ip-extended-community-lists)
  - [IP Extended Community RegExp Lists](#ip-extended-community-regexp-lists)
  - [Match-lists](#match-lists)
  - [AS Path Lists](#as-path-lists)
- [802.1X Port Security](#8021x-port-security)
  - [802.1X Summary](#8021x-summary)
- [Power Over Ethernet (PoE)](#power-over-ethernet-poe)
  - [PoE Summary](#poe-summary)
- [ACL](#acl)
  - [Standard Access-lists](#standard-access-lists)
  - [Extended Access-lists](#extended-access-lists)
  - [IP Access-lists](#ip-access-lists)
  - [IPv6 Standard Access-lists](#ipv6-standard-access-lists)
  - [IPv6 Extended Access-lists](#ipv6-extended-access-lists)
  - [MAC Access-lists](#mac-access-lists)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Virtual Source NAT](#virtual-source-nat)
  - [Virtual Source NAT Summary](#virtual-source-nat-summary)
  - [Virtual Source NAT Configuration](#virtual-source-nat-configuration)
- [System L1](#system-l1)
  - [Unsupported Interface Configurations](#unsupported-interface-configurations)
  - [System L1 Device Configuration](#system-l1-device-configuration)
- [Application Traffic Recognition](#application-traffic-recognition)
  - [Applications](#applications)
  - [Application Profiles](#application-profiles)
  - [Categories](#categories)
  - [Field Sets](#field-sets)
  - [Router Application-Traffic-Recognition Device Configuration](#router-application-traffic-recognition-device-configuration)
- [Group-Based Multi-domain Segmentation Services (MSS-Group)](#group-based-multi-domain-segmentation-services-mss-group)
  - [Segmentation Policies](#segmentation-policies)
  - [Segment Definitions](#segment-definitions)
  - [Router MSS-G Device Configuration](#router-mss-g-device-configuration)
  - [Router Path-selection](#router-path-selection)
  - [Router Internet Exit](#router-internet-exit)
- [Router L2 VPN](#router-l2-vpn)
  - [Router L2 VPN Summary](#router-l2-vpn-summary)
  - [Router L2 VPN Device Configuration](#router-l2-vpn-device-configuration)
- [IP DHCP Relay](#ip-dhcp-relay)
  - [IP DHCP Relay Summary](#ip-dhcp-relay-summary)
  - [IP DHCP Relay Device Configuration](#ip-dhcp-relay-device-configuration)
- [IPv6 DHCP Relay](#ipv6-dhcp-relay)
  - [IPv6 DHCP Relay Summary](#ipv6-dhcp-relay-summary)
  - [IPv6 DHCP Relay Device Configuration](#ipv6-dhcp-relay-device-configuration)
- [IP DHCP Snooping](#ip-dhcp-snooping)
  - [IP DHCP Snooping Device Configuration](#ip-dhcp-snooping-device-configuration)
- [IP NAT](#ip-nat)
  - [NAT Profiles](#nat-profiles)
  - [NAT Pools](#nat-pools)
  - [NAT Synchronization](#nat-synchronization)
  - [NAT Translation Settings](#nat-translation-settings)
  - [IP NAT Device Configuration](#ip-nat-device-configuration)
- [Errdisable](#errdisable)
  - [Errdisable Summary](#errdisable-summary)
- [Quality Of Service](#quality-of-service)
  - [QOS Class Maps](#qos-class-maps)
  - [QOS Policy Maps](#qos-policy-maps)
  - [QOS Interfaces](#qos-interfaces)
  - [Control-plane Policy Map](#control-plane-policy-map)
- [InfluxDB Telemetry](#influxdb-telemetry)
  - [InfluxDB Telemetry Summary](#influxdb-telemetry-summary)
  - [InfluxDB Telemetry Device Configuration](#influxdb-telemetry-device-configuration)
- [STUN](#stun)
  - [STUN Client](#stun-client)
  - [STUN Server](#stun-server)
  - [STUN Device Configuration](#stun-device-configuration)
- [Maintenance Mode](#maintenance-mode)
  - [BGP Groups](#bgp-groups)
  - [Interface Groups](#interface-groups)
  - [Maintenance](#maintenance)

## Management

### Agents

#### Agent Dummy

##### Environment Variables

| Name | Value |
| ---- | ----- |
| V1 | 42 |
| V2 | 666 |

#### Agent KernelFib

##### Environment Variables

| Name | Value |
| ---- | ----- |
| KERNELFIB_PROGRAM_ALL_ECMP | true |

#### Agents Device Configuration

```eos
!
agent Dummy environment V1=42:V2=666
agent KernelFib environment KERNELFIB_PROGRAM_ALL_ECMP=true
```

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | OOB_MANAGEMENT | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description OOB_MANAGEMENT
   vrf MGMT
   ip address 10.73.255.122/24
```

### IP Domain-list

#### Domains List

- domain1.local
- domain2.local

#### IP Domain-list Device Configuration

```eos
ip domain-list domain1.local
ip domain-list domain2.local
!
```

### Clock Settings

#### Clock Timezone Settings

Clock Timezone is set to **GMT**.

#### Clock Device Configuration

```eos
!
clock timezone GMT
```

### NTP

#### NTP Summary

##### NTP Local Interface

| Interface | VRF |
| --------- | --- |
| lo1 | default |

##### NTP Servers

| Server | VRF | Preferred | Burst | iBurst | Version | Min Poll | Max Poll | Local-interface | Key |
| ------ | --- | --------- | ----- | ------ | ------- | -------- | -------- | --------------- | --- |
| 1.2.3.4 | - | - | - | - | - | - | - | lo0 | - |
| 2.2.2.55 | - | - | - | - | - | - | - | - | - |
| 10.1.1.1 | - | - | - | - | - | - | - | - | - |
| 10.1.1.2 | - | True | - | - | - | - | - | - | - |
| 20.20.20.1 | - | - | - | - | - | - | - | - | 2 |
| ie.pool.ntp.org | - | - | False | True | - | - | - | - | 1 |

##### NTP Authentication

- Authentication enabled

- Trusted Keys: 1-3

##### NTP Authentication Keys

| ID | Algorithm |
| -- | -------- |
| 1 | md5 |
| 2 | md5 |
| 3 | sha1 |

#### NTP Device Configuration

```eos
!
ntp authentication-key 1 md5 <removed>
ntp authentication-key 2 md5 7 <removed>
ntp authentication-key 3 sha1 8a <removed>
ntp trusted-key 1-3
ntp authenticate
ntp local-interface lo1
ntp server 1.2.3.4 local-interface lo0
ntp server 2.2.2.55
ntp server 10.1.1.1
ntp server 10.1.1.2 prefer
ntp server 20.20.20.1 key <removed>
ntp server ie.pool.ntp.org iburst key <removed>
```

### System Control-Plane

#### TCP MSS Ceiling

| Protocol | Segment Size |
| -------- | -------------|
| IPv4 | 1344 |
| IPv6 | 1366 |

#### Control-Plane Access-Groups

| Protocol | VRF | Access-list |
| -------- | --- | ------------|
| IPv4 Ingress default | All | ingress_ipv4_acl |
| IPv4 | default | acl4_1 |
| IPv4 | red | acl4_2 |
| IPv4 | red_1 | acl4_2 |
| IPv4 | default | acl4_3 |
| IPv6 Ingress default | All | ingress_ipv6_acl |
| IPv6 | default | acl6_1 |
| IPv6 | blue | acl6_2 |
| IPv6 | blue_1 | acl6_2 |
| IPv6 | default | acl6_3 |

#### System Control-Plane Device Configuration

```eos
!
system control-plane
   tcp mss ceiling ipv4 1344 ipv6 1366
   ip access-group ingress default ingress_ipv4_acl
   ip access-group acl4_1 in
   ip access-group acl4_3 vrf default in
   ip access-group acl4_2 vrf red in
   ip access-group acl4_2 vrf red_1 in
   ipv6 access-group ingress default ingress_ipv6_acl
   ipv6 access-group acl6_1 in
   ipv6 access-group acl6_3 vrf default in
   ipv6 access-group acl6_2 vrf blue in
   ipv6 access-group acl6_2 vrf blue_1 in
```

### Management SSH

#### Authentication Settings

| Authentication protocols | Empty passwords |
| ------------------------ | --------------- |
| keyboard-interactive, password, public-key | permit |

#### IPv4 ACL

| IPv4 ACL | VRF |
| -------- | --- |
| ACL-SSH | - |
| ACL-SSH-VRF | mgt |

#### SSH Timeout and Management

| Idle Timeout | SSH Management |
| ------------ | -------------- |
| 15 | Enabled |

#### Max number of SSH sessions limit and per-host limit

| Connection Limit | Max from a single Host |
| ---------------- | ---------------------- |
| 50 | 10 |

#### Ciphers and Algorithms

| Ciphers | Key-exchange methods | MAC algorithms | Hostkey server algorithms |
|---------|----------------------|----------------|---------------------------|
| default | default | default | default |

#### VRFs

| VRF | Status |
| --- | ------ |
| mgt | Enabled |

#### Management SSH Device Configuration

```eos
!
management ssh
   ip access-group ACL-SSH in
   ip access-group ACL-SSH-VRF vrf mgt in
   idle-timeout 15
   authentication protocol keyboard-interactive password public-key
   connection per-host 10
   fips restrictions
   hostkey client strict-checking
   connection limit 50
   authentication empty-passwords permit
   client-alive interval 666
   client-alive count-max 42
   no shutdown
   log-level debug
   !
   vrf mgt
      no shutdown
```

### Management Tech-Support

#### Policy

##### Exclude Commands

| Command | Type |
| ------- | ---- |
| show platform fap ip route | text |
| show platform fap ipv6 route | text |
| show ip bgp vrf all | text |
| show ipv6 bgp vrf all | text |
| show kernel ip route vrf all | text |
| show kernel ipv6 route vrf all | text |
| show ip route vrf all detail | text |
| show ipv6 route vrf all detail | text |
| show version detail | json |

##### Include Commands

| Command |
| ------- |
| show version detail \| grep TerminAttr |

#### Policy Device Configuration

```eos
!
management tech-support
   policy show tech-support
      exclude command show ip bgp vrf all
      exclude command show ip route vrf all detail
      exclude command show ipv6 bgp vrf all
      exclude command show ipv6 route vrf all detail
      exclude command show kernel ip route vrf all
      exclude command show kernel ipv6 route vrf all
      exclude command show platform fap ip route
      exclude command show platform fap ipv6 route
      exclude command json show version detail
      include command show version detail | grep TerminAttr
   exit
```

### IP Client Source Interfaces

| IP Client | VRF | Source Interface Name |
| --------- | --- | --------------------- |
| FTP | default | Ethernet10 |
| FTP | default | Loopback0 |
| FTP | MGMT | Management0 |
| HTTP | default | Loopback0 |
| HTTP | MGMT | Management0 |
| HTTP | default | Ethernet10 |
| SSH | default | Ethernet10 |
| SSH | default | Loopback0 |
| SSH | MGMT | Management0 |
| Telnet | default | Ethernet10 |
| Telnet | default | Loopback0 |
| Telnet | MGMT | Management0 |
| TFTP | default | Ethernet10 |
| TFTP | default | Loopback0 |
| TFTP | MGMT | Management0 |

#### IP Client Source Interfaces Device Configuration

```eos
!
ip ftp client source-interface Ethernet10
ip ftp client source-interface Loopback0 vrf default
ip ftp client source-interface Management0 vrf MGMT
ip http client local-interface Loopback0 vrf default
ip http client local-interface Management0 vrf MGMT
ip http client local-interface Ethernet10
ip ssh client source-interface Ethernet10
ip ssh client source-interface Loopback0 vrf default
ip ssh client source-interface Management0 vrf MGMT
ip telnet client source-interface Ethernet10
ip telnet client source-interface Loopback0 vrf default
ip telnet client source-interface Management0 vrf MGMT
ip tftp client source-interface Ethernet10
ip tftp client source-interface Loopback0 vrf default
ip tftp client source-interface Management0 vrf MGMT
 ```

## CVX

| Peer Hosts |
| ---------- |
| 1.1.1.1, 2.2.2.2 |

CVX is enabled

### CVX Services

| Service | Enabled | Settings |
| ------- | ------- | -------- |
| MCS | True | Redis Password Set |
| VXLAN | True | VTEP MAC learning: control-plane |

### CVX Device Configuration

```eos
!
cvx
   no shutdown
   peer host 1.1.1.1
   peer host 2.2.2.2
   !
   service mcs
      redis password 7 <removed>
      no shutdown
   !
   service vxlan
      no shutdown
      vtep mac-learning control-plane
```

## Authentication

### Local Users

#### Local Users Summary

| User | Privilege | Role | Disabled | Shell |
| ---- | --------- | ---- | -------- | ----- |
| admin | 15 | network-admin | False | - |
| admin1 | - | - | True | - |
| ansible | 15 | network-admin | False | - |
| cvpadmin | 15 | network-admin | False | - |
| shell | - | - | False | /sbin/nologin |

#### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin nopassword
no username admin1
username ansible privilege 15 role network-admin secret sha512 <removed>
username cvpadmin privilege 15 role network-admin secret sha512 <removed>
username cvpadmin ssh-key ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC9OuVC4D+ARBrc9sP0VRmP6osTo8fgA4Z/dkacQuiOgph6VTHaBkIuqR7XswKKCOH36GXeIChnIF+d1HSoe05mZX+bT2Nu1SObnO8jZjqIFZqUlXUTHWgmnChchABmXS3KMQlivVDE/r9o3vmHEFTfKPZsmG7YHZuavfYXxFJtqtDW0nGH/WJ+mm4v2CP1tOPBLvNE3mLXXyTepDkmrCH/fkwgPR3gBqLrkhWlma0bz+7I851RpCQemhVJFxeI/SnvQfL2VJU2ZMM3pPRSTlLry7Od6kZNAkr4dIOFDCVAaIDbBxPUZ/LvPfyEUwicEo/EKmpLBQ6E2UqcCK2pTyV/K63682spi2mkxp4FgaLi4CjWkpnL1A/MD7WhrSNgqXToF7QCb9Lidagy9IHafQxfu7LwkFdyQIMu8XNwDZIycuf29wHbDdz1N+YNVK8zwyNAbMOeKMqblsEm2YIorgjzQX1m9+/rJeFBKz77PSgeMp/Rc3txFVuSmFmeTy3aMkU= cvpadmin@hostmachine.local
username shell shell /sbin/nologin nopassword
username shell ssh-key ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDHMTFuLHPz/prREZZIks0ca4btBIzEbvY6KRYGzhN7JCG5CTfre0Y9UCbNul7qNl7cxomQkh/0VjQNX6ecPd0HyOTKL2EK002ejNyvooUDarnglMWtjKIl40NgDR/GNSkvC3nEylvX1H7Rfmu38NCqiwIpWA8JFwgLCLvkWUoORxHhIIy8/vttLgMxr66HGlVAnRidf3VVCnlILm4gUpc3fR43EhvVoYByY3jEa/fypiS2nDP9K2fXtpXGrIHSbyMu4Mj3fnSdcqWysRF7Tqc6Kvet8ImS07fLcgpbdLp31ssF1rssbTnD1zWuAozvXpK1d+vFO4EfFr5yzkE2Q8lM0wPpdS4LBWQfJdWgi6t5XEXewWyTYfIDKCBOI2dECGtkDjme+PDNIL9IQiiYC2iXMmQrun9fsp8jicdw1svGef8Otdb4kmHXiQ3mAxTeHLgeYPfYyekKq/+dFMcAZT+sv0g24AHc4ulitfLRoGjxYHZLGg2KQpFfAn0aQKCd5vk= noname@hostmachine-asd-cl
username shell ssh-key secondary ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDHMTFuLHPz/prREZZIks0ca4btBIzEbvY6KRYGzhN7JCG5CTfre0Y9UCbNul7qNl7cxomQkh/0VjQNX6ecPd0HyOTKL2EK002ejNyvooUDarnglMWtjKIl40NgDR/GNSkvC3nEylvX1H7Rfmu38NCqiwIpWA8JFwgLCLvkWUoORxHhIIy8/vttLgMxr66HGlVAnRidf3VVCnlILm4gUpc3fR43EhvVoYByY3jEa/fypiS2nDP9K2fXtpXGrIHSbyMu4Mj3fnSdcqWysRF7Tqc6Kvet8ImS07fLcgpbdLp31ssF1rssbTnD1zWuAozvXpK1d+vFO4EfFr5yzkE2Q8lM0wPpdS4LBWQfJdWgi6t5XEXewWyTYfIDKCBOI2dECGtkDjme+PDNIL9IQiiYC2iXMmQrun9fsp8jicdw1svGef8Otdb4kmHXiQ3mAxTeHLgeYPfYyekKq/+dFMcAZT+sv0g24AHc4ulitfLRoGjxYHZLGg2KQpFfAn0aQKCd5vk= noname@hostmachine-asd-cl
```

### Roles

#### Roles Summary

##### Role network-limited

| Sequence | Action | Mode | Command |
| -------- | ------ | ---- | ------- |
| 10 | permit | exec | ssh |
| 20 | deny | - | telnet |
| 30 | permit | exec | traceroute |

#### Roles Device Configuration

```eos
!
role network-limited
   10 permit mode exec command ssh
   20 deny command telnet
   30 permit mode exec command traceroute
```

### Enable Password

sha512 encrypted enable password is configured

#### Enable Password Device Configuration

```eos
!
enable password sha512 <removed>
!
```

### TACACS Servers

#### TACACS Servers

| VRF | TACACS Servers | Single-Connection | Timeout |
| --- | -------------- | ----------------- | ------- |
| mgt | 10.10.10.157 | True | - |
| default | 10.10.10.249 | False | 23 |
| default | 10.10.10.158 | False | - |
| default | 10.10.10.159 | False | - |
| default | 10.10.10.160 | False | - |

Policy unknown-mandatory-attribute ignore is configured

Global timeout: 10 seconds

#### TACACS Servers Device Configuration

```eos
!
tacacs-server timeout 10
tacacs-server policy unknown-mandatory-attribute ignore
tacacs-server host 10.10.10.157 single-connection vrf mgt key 7 <removed>
tacacs-server host 10.10.10.249 timeout 23 key 7 <removed>
tacacs-server host 10.10.10.158 key 7 <removed>
tacacs-server host 10.10.10.159 key 8a <removed>
tacacs-server host 10.10.10.160
```

### IP TACACS Source Interfaces

#### IP TACACS Source Interfaces

| VRF | Source Interface Name |
| --- | --------------- |
| default | loopback1 |
| TEST1 | lo3 |
| default | loopback10 |

#### IP TACACS Source Interfaces Device Configuration

```eos
!
ip tacacs vrf default source-interface loopback1
!
ip tacacs vrf TEST1 source-interface lo3
!
ip tacacs source-interface loopback10
```

### RADIUS Server

- Time to skip a non-responsive server is 10 minutes

- Attribute 32 is included in access requests using hostname

- Global RADIUS TLS SSL profile is GLOBAL_RADIUS_SSL_PROFILE

- Dynamic Authorization is enabled on port 1700

- Dynamic Authorization for TLS connections uses SSL profile SSL_PROFILE

#### RADIUS Server Hosts

| VRF | RADIUS Servers | TLS | SSL Profile | Timeout | Retransmit |
| --- | -------------- | --- | ----------- | ------- | ---------- |
| mgt | 10.10.10.157 | - | - | - | - |
| default | 10.10.10.249 | - | - | - | - |
| default | 10.10.10.158 | - | - | - | - |
| mgt | 10.10.11.157 | - | - | 1 | 1 |
| mgt | 10.10.11.159 | - | - | - | 1 |
| mgt | 10.10.11.160 | - | - | 1 | - |
| mgt | 10.10.11.248 | - | - | - | - |
| default | 10.10.11.249 | - | - | 1 | 1 |
| default | 10.10.11.158 | - | - | 1 | 1 |
| default | 10.10.11.156 | True | - | 1 | 1 |
| mgt | 10.10.11.155 | True | HOST_SSL_PROFILE | 1 | 1 |

#### RADIUS Server Device Configuration

```eos
!
radius-server deadtime 10
radius-server attribute 32 include-in-access-req hostname
radius-server dynamic-authorization port 1700
radius-server tls ssl-profile GLOBAL_RADIUS_SSL_PROFILE
radius-server dynamic-authorization tls ssl-profile SSL_PROFILE
radius-server host 10.10.10.157 vrf mgt key 7 <removed>
radius-server host 10.10.10.249 key 7 <removed>
radius-server host 10.10.10.158 key 7 <removed>
radius-server host 10.10.11.157 vrf mgt timeout 1 retransmit 1 key 7 <removed>
radius-server host 10.10.11.159 vrf mgt retransmit 1 key 7 <removed>
radius-server host 10.10.11.160 vrf mgt timeout 1 key 7 <removed>
radius-server host 10.10.11.248 vrf mgt key 7 <removed>
radius-server host 10.10.11.249 timeout 1 retransmit 1 key 7 <removed>
radius-server host 10.10.11.158 timeout 1 retransmit 1 key 7 <removed>
radius-server host 10.10.11.156 tls port 1700 timeout 1 retransmit 1
radius-server host 10.10.11.155 vrf mgt tls ssl-profile HOST_SSL_PROFILE port 2083 timeout 1 retransmit 1
```

### IP RADIUS Source Interfaces

#### IP RADIUS Source Interfaces

| VRF | Source Interface Name |
| --- | --------------- |
| default | loopback1 |
| MGMT | Ma1 |
| default | loopback10 |

#### IP SOURCE Source Interfaces Device Configuration

```eos
!
ip radius vrf default source-interface loopback1
!
ip radius vrf MGMT source-interface Ma1
!
ip radius source-interface loopback10
```

### AAA Server Groups

#### AAA Server Groups Summary

| Server Group Name | Type  | VRF | IP address |
| ------------------| ----- | --- | ---------- |
| TACACS | tacacs+ | mgt | 10.10.11.157 |
| TACACS | tacacs+ | default | 10.10.11.249 |
| TACACS1 | tacacs+ | mgt | 10.10.10.157 |
| TACACS1 | tacacs+ | default | 10.10.10.249 |
| TACACS2 | tacacs+ | mgt | 192.168.10.157 |
| TACACS2 | tacacs+ | default | 10.10.10.248 |
| LDAP1 | ldap | mgt | 192.168.10.157 |
| LDAP1 | ldap | default | 10.10.10.248 |
| LADP2 | ldap | mgt | 10.10.10.157 |
| LADP2 | ldap | default | 10.10.10.249 |
| RADIUS1 | radius | mgt | 192.168.10.157 |
| RADIUS1 | radius | default | 10.10.10.248 |
| RADIUS2 | radius | mgt | 10.10.10.157 |
| RADIUS2 | radius | default | 10.10.10.249 |

#### AAA Server Groups Device Configuration

```eos
!
aaa group server ldap LADP2
   server 10.10.10.157 vrf mgt
   server 10.10.10.249
!
aaa group server ldap LDAP1
   server 192.168.10.157 vrf mgt
   server 10.10.10.248
!
aaa group server radius RADIUS1
   server 192.168.10.157 vrf mgt
   server 10.10.10.248
!
aaa group server radius RADIUS2
   server 10.10.10.157 vrf mgt
   server 10.10.10.249
!
aaa group server tacacs+ TACACS
   server 10.10.11.157 vrf mgt
   server 10.10.11.249
!
aaa group server tacacs+ TACACS1
   server 10.10.10.157 vrf mgt
   server 10.10.10.249
!
aaa group server tacacs+ TACACS2
   server 192.168.10.157 vrf mgt
   server 10.10.10.248
```

### AAA Authentication

#### AAA Authentication Summary

| Type | Sub-type | User Stores |
| ---- | -------- | ---------- |
| Login | default | group TACACS local |
| Login | console | local |

AAA Authentication on-failure log has been enabled

AAA Authentication on-success log has been enabled

Policy local allow-nopassword-remote-login has been enabled.

Policy lockout has been enabled. After **3** failed login attempts within **900** minutes, you'll be locked out for **300** minutes.

#### AAA Authentication Device Configuration

```eos
aaa authentication login default group TACACS local
aaa authentication login console local
aaa authentication enable default group TACACS local
aaa authentication dot1x default group RADIUS1
aaa authentication policy on-failure log
aaa authentication policy on-success log
aaa authentication policy local allow-nopassword-remote-login
aaa authentication policy lockout failure 3 window 900 duration 300
!
```

### AAA Authorization

#### AAA Authorization Summary

| Type | User Stores |
| ---- | ----------- |
| Exec | group TACACS local |
| Default Role | network-admin |
| Additional Dynamic Authorization Groups | radius, RADIUS1 |

Authorization for configuration commands is enabled.

Authorization for serial console is enabled.

#### AAA Authorization Privilege Levels Summary

| Privilege Level | User Stores |
| --------------- | ----------- |
| all | group TACACS |
| 5 | group radius |
| 10,15 | group tacacs+ local |

#### AAA Authorization Device Configuration

```eos
aaa authorization policy local default-role network-admin
aaa authorization serial-console
aaa authorization dynamic dot1x additional-groups group radius group RADIUS1
aaa authorization exec default group TACACS local
aaa authorization commands all default group TACACS
aaa authorization commands 5 default group radius
aaa authorization commands 10,15 default group tacacs+ local
!
```

### AAA Accounting

#### AAA Accounting Summary

| Type | Commands | Record type | Group | Logging |
| ---- | -------- | ----------- | ----- | ------- |
| Exec - Console | - | start-stop | TACACS | True |
| Commands - Console | all | start-stop | TACACS | True |
| Commands - Console | 0 | start-stop |  -  | True |
| Commands - Console | 1 | start-stop | TACACS1 | False |
| Exec - Default | - | start-stop | TACACS | True |
| System - Default | - | start-stop | TACACS | - |
| Dot1x - Default  | - | start-stop | RADIUS | - |
| Commands - Default | all | start-stop | TACACS | True |
| Commands - Default | 0 | start-stop | - | True |
| Commands - Default | 1 | start-stop | TACACS | False |

#### AAA Accounting Device Configuration

```eos
aaa accounting exec console start-stop group TACACS logging
aaa accounting commands all console start-stop group TACACS logging
aaa accounting commands 0 console start-stop logging
aaa accounting commands 1 console start-stop group TACACS1
aaa accounting exec default start-stop group TACACS logging
aaa accounting system default start-stop group TACACS
aaa accounting dot1x default start-stop group RADIUS
aaa accounting commands all default start-stop group TACACS logging
aaa accounting commands 0 default start-stop logging
aaa accounting commands 1 default start-stop group TACACS
```

## Management Security

### Management Security Summary

| Settings | Value |
| -------- | ----- |
| Entropy sources | hardware, haveged, cpu jitter, hardware exclusive |
| Common password encryption key | True |
| Reversible password encryption | aes-256-gcm |
| Minimum password length | 17 |

### Management Security SSL Profiles

| SSL Profile Name | TLS protocol accepted | Certificate filename | Key filename | Cipher List | CRLs |
| ---------------- | --------------------- | -------------------- | ------------ | ----------- | ---- |
| certificate-profile | - | eAPI.crt | eAPI.key | - | ca.crl<br>intermediate.crl |
| cipher-list-profile | - | - | - | ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384 | - |
| test1-chain-cert | - | - | - | - | - |
| test1-trust-cert | - | - | - | - | - |
| test2-chain-cert | - | - | - | - | - |
| test2-trust-cert | - | - | - | - | - |
| tls-single-version-profile-as-float | 1.0 | - | - | - | - |
| tls-single-version-profile-as-string | 1.1 | - | - | - | - |
| tls-versions-profile | 1.0 1.1 | - | - | - | - |

### SSL profile test1-chain-cert Certificates Summary

| Chain Certificates | Requirement |
| ------------------ | ----------- |
| test-chain-cert1.crt, test-chain-cert2.crt | Basic Constraint CA |

### SSL profile test1-trust-cert Certificates Summary

| Trust Certificates | Requirement | Policy | System |
| ------------------ | ----------- | ------ | ------ |
| test-trust1.crt, test-trust2.crt | Basic Constraint CA | Ignore Expiry Date | - |

### SSL profile test2-chain-cert Certificates Summary

| Chain Certificates | Requirement |
| ------------------ | ----------- |
| - | Root CA Included |

### SSL profile test2-trust-cert Certificates Summary

| Trust Certificates | Requirement | Policy | System |
| ------------------ | ----------- | ------ | ------ |
| - | Hostname must be FQDN | - | Enabled |

### Password Policies

| Policy Name | Digits | Length | Lowercase letters | Special characters | Uppercase letters | Repetitive characters | Sequential characters |
|-------------|--------|--------|-------------------|--------------------|-------------------|-----------------------|----------------------|
| AVD_POLICY | > 1 | > 2 | > 3 | > 4 | > 5 | < 6 | < 7 |

### Session Shared-secret Profiles

#### profile0

| Secret Name | Receive Lifetime | Transmit Lifetime | Timezone |
| ----------- | ---------------- | ----------------- | -------- |
| Secret1 | 12/20/2024 10:00:00 - 12/20/2025 10:00:00 | Infinite | Local Time |
| Secret2 | Infinite | Infinite | UTC |

#### profile1

| Secret Name | Receive Lifetime | Transmit Lifetime | Timezone |
| ----------- | ---------------- | ----------------- | -------- |
| Secret3 | 2024-12-20 10:00:00 - 2025-12-20 10:00:00 | 12/20/2024 10:00:00 - 12/10/2025 10:00:00 | UTC |

#### profile2

| Secret Name | Receive Lifetime | Transmit Lifetime | Timezone |
| ----------- | ---------------- | ----------------- | -------- |
| Secret4 | 2024-12-20 10:00:00 - 2025-12-20 10:00:00 | 2024-12-20 10:00:00 - 2025-12-20 10:00:00 | UTC |

### Management Security Device Configuration

```eos
!
management security
   entropy source hardware haveged cpu jitter
   entropy source hardware exclusive
   password minimum length 17
   password encryption-key common
   password encryption reversible aes-256-gcm
   !
   password policy AVD_POLICY
      minimum digits 1
      minimum length 2
      minimum lower 3
      minimum special 4
      minimum upper 5
      maximum repetitive 6
      maximum sequential 7
   !
   session shared-secret profile profile0
      secret Secret1 7 <removed> receive-lifetime 12/20/2024 10:00:00 12/20/2025 10:00:00 transmit-lifetime infinite local-time
      secret Secret2 7 <removed> receive-lifetime infinite transmit-lifetime infinite
   !
   session shared-secret profile profile1
      secret Secret3 8a <removed> receive-lifetime 2024-12-20 10:00:00 2025-12-20 10:00:00 transmit-lifetime 12/20/2024 10:00:00 12/10/2025 10:00:00
   !
   session shared-secret profile profile2
      secret Secret4 0 <removed> receive-lifetime 2024-12-20 10:00:00 2025-12-20 10:00:00 transmit-lifetime 2024-12-20 10:00:00 2025-12-20 10:00:00
   !
   ssl profile certificate-profile
      certificate eAPI.crt key eAPI.key
      crl ca.crl
      crl intermediate.crl
   !
   ssl profile cipher-list-profile
      cipher-list ECDHE-RSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-SHA384
   !
   ssl profile test1-chain-cert
      chain certificate test-chain-cert1.crt
      chain certificate test-chain-cert2.crt
      chain certificate requirement basic-constraint ca true
   !
   ssl profile test1-trust-cert
      trust certificate test-trust1.crt
      trust certificate test-trust2.crt
      trust certificate requirement basic-constraint ca true
      trust certificate policy expiry-date ignore
   !
   ssl profile test2-chain-cert
      chain certificate requirement include root-ca
   !
   ssl profile test2-trust-cert
      trust certificate system
      trust certificate requirement hostname fqdn
   !
   ssl profile tls-single-version-profile-as-float
      tls versions 1.0
   !
   ssl profile tls-single-version-profile-as-string
      tls versions 1.1
   !
   ssl profile tls-versions-profile
      tls versions 1.0 1.1
```

## Prompt Device Configuration

```eos
!
prompt %H__%D{%H:%M:%S}%v%P
```

## Aliases Device Configuration

```eos
alias wr copy running-config startup-config
alias siib show ip interface brief

!
```

## DHCP Relay

### DHCP Relay Summary

- DHCP Relay is disabled for tunnelled requests
- DHCP Relay is disabled for MLAG peer-link requests

| DHCP Relay Servers |
| ------------------ |
| dhcp-relay-server1 |
| dhcp-relay-server2 |

### DHCP Relay Device Configuration

```eos
!
dhcp relay
   tunnel requests disabled
   mlag peer-link requests disabled
   server dhcp-relay-server1
   server dhcp-relay-server2
```

## DHCP Server

### DHCP Servers Summary

| DHCP Server Enabled | VRF | IPv4 DNS Domain | IPv4 DNS Servers | IPv4 Bootfile | IPv4 Lease Time | IPv6 DNS Domain | IPv6 DNS Servers | IPv6 Bootfile | IPv6 Lease Time |
| ------------------- | --- | --------------- | ---------------- | ------------- | --------------- | --------------- | ---------------- | ------------- | --------------- |
| True | AVRF | - | - | - | - | - | - | - | - |
| True | defauls | - | - | - | - | - | - | - | - |
| True | default | - | 10.0.0.1, 192.168.255.254 | https://www.arista.io/ztp/bootstrap | - | - | 2001:db8::1, 2001:db8::2 | https://2001:0db8:fe/ztp/bootstrap | - |
| True | defaulu | - | - | - | - | - | - | - | - |
| True | TEST | testv4.com | - | - | 10 days 10 hours 10 minutes | testv6.com | - | - | 12 days 12 hours 12 minutes |
| False | VRF01 | - | - | - | - | - | - | - | - |

#### VRF AVRF DHCP Server

##### Subnets

| Subnet | Name | DNS Servers | Default Gateway | Lease Time | Ranges |
| ------ | ---- | ----------- | --------------- | ---------- | ------ |
| 172.16.254.0/24 | - | - | 172.16.254.1 | - | - |

#### VRF default DHCP Server

##### Subnets

| Subnet | Name | DNS Servers | Default Gateway | Lease Time | Ranges |
| ------ | ---- | ----------- | --------------- | ---------- | ------ |
| 2a00:2::/64 | - | - | - | - | - |
| 10.2.3.0/24 | - | - | - | - | - |

##### IPv4 Vendor Options

| Vendor ID | Sub-option Code | Sub-option Type | Sub-option Data |
| --------- | ----------------| --------------- | --------------- |
| NTP | 42 | ipv4-address | 10.1.1.1 |

#### VRF TEST DHCP Server

##### Subnets

| Subnet | Name | DNS Servers | Default Gateway | Lease Time | Ranges |
| ------ | ---- | ----------- | --------------- | ---------- | ------ |
| 10.0.0.0/24 | TEST1 | 10.1.1.12, 10.1.1.13 | 10.0.0.1 | 0 days, 0 hours, 10 minutes | 10.0.0.10-10.0.0.100, 10.0.0.110-10.0.0.120 |
| 2001:db8:abcd:1234:c000::/66 | - | - | - | - | - |

###### DHCP Reservations in subnet 10.0.0.0/24

| Mac Address | IPv4 Address | IPv6 Address | Hostname |
| ----------- | ------------ | ------------ | -------- |
| 0001.0001.0001 | 10.0.0.2 | - |  host3 |
| 1a1b.1c1d.1e1f | 10.0.0.1 | - |  host1 |

###### DHCP Reservations in subnet 2001:db8:abcd:1234:c000::/66

| Mac Address | IPv4 Address | IPv6 Address | Hostname |
| ----------- | ------------ | ------------ | -------- |
| 0003.0003.003 | - | 2001:db8:abcd:1234:c000::1 |  - |

##### IPv4 Vendor Options

| Vendor ID | Sub-option Code | Sub-option Type | Sub-option Data |
| --------- | ----------------| --------------- | --------------- |
| NTP | 1 | string | test |
| NTP | 42 | ipv4-address | 10.1.1.1 |
| NTP | 66 | array ipv4-address | 1.1.1.1 2.2.2.2 |

#### VRF VRF01 DHCP Server

##### Subnets

| Subnet | Name | DNS Servers | Default Gateway | Lease Time | Ranges |
| ------ | ---- | ----------- | --------------- | ---------- | ------ |
| 192.168.0.0/24 | - | - | - | - | - |

### DHCP Server Configuration

```eos
!
dhcp server vrf AVRF
   !
   subnet 172.16.254.0/24
      default-gateway 172.16.254.1
   dns server ipv4 10.0.0.1 192.168.255.254
   client class ipv4 definition Class1
!
dhcp server vrf defauls
!
dhcp server
   dns server ipv4 10.0.0.1 192.168.255.254
   dns server ipv6 2001:db8::1 2001:db8::2
   tftp server file ipv4 https://www.arista.io/ztp/bootstrap
   tftp server file ipv6 https://2001:0db8:fe/ztp/bootstrap
   !
   subnet 2a00:2::/64
   !
   subnet 10.2.3.0/24
   !
   vendor-option ipv4 NTP
      sub-option 42 type ipv4-address data 10.1.1.1
!
dhcp server vrf defaulu
!
dhcp server vrf TEST
   lease time ipv4 10 days 10 hours 10 minutes
   dns domain name ipv4 testv4.com
   lease time ipv6 12 days 12 hours 12 minutes
   dns domain name ipv6 testv6.com
   !
   subnet 10.0.0.0/24
      reservations
         mac-address 0001.0001.0001
            ipv4-address 10.0.0.2
            hostname host3
         !
         mac-address 1a1b.1c1d.1e1f
            ipv4-address 10.0.0.1
            hostname host1
      !
      range 10.0.0.10 10.0.0.100
      !
      range 10.0.0.110 10.0.0.120
      name TEST1
      dns server 10.1.1.12 10.1.1.13
      lease time 0 days 0 hours 10 minutes
      default-gateway 10.0.0.1
   !
   subnet 2001:db8:abcd:1234:c000::/66
      reservations
         mac-address 0003.0003.003
            ipv6-address 2001:db8:abcd:1234:c000::1
   !
   vendor-option ipv4 NTP
      sub-option 1 type string data "test"
      sub-option 42 type ipv4-address data 10.1.1.1
      sub-option 66 type array ipv4-address data 1.1.1.1 2.2.2.2
!
dhcp server vrf VRF01
   !
   subnet 192.168.0.0/24
   disabled
```

### DHCP Server Interfaces

| Interface name | DHCP IPv4 | DHCP IPv6 |
| -------------- | --------- | --------- |
| Ethernet64 | True | True |

## System Boot Settings

### Boot Secret Summary

- The md5 hashed Aboot password is configured

### System Boot Device Configuration

```eos
!
boot secret 5 <removed>
```

## Monitoring

### Custom daemons

#### Custom Daemons Device Configuration

```eos
!
daemon ocprometheus
   exec /usr/bin/ocprometheus -config /usr/bin/ocprometheus.yml -addr localhost:6042
   no shutdown
!
daemon random
   exec /usr/bin/random
   shutdown
```

### Logging

#### Logging Servers and Features Summary

| Type | Level |
| -----| ----- |
| Console | errors |
| Buffer | warnings |
| Trap | disabled |
| Synchronous | critical |

| Format Type | Setting |
| ----------- | ------- |
| Timestamp | traditional year timezone |
| Hostname | hostname |
| Sequence-numbers | false |
| RFC5424 | True |

| VRF | Source Interface |
| --- | ---------------- |
| default | Loopback0 |
| mgt | Management0 |

| VRF | Hosts | Ports | Protocol |
| --- | ----- | ----- | -------- |
| default | 20.20.20.7 | Default | UDP |
| default | 50.50.50.7 | 100, 200 | TCP |
| default | 60.60.60.7 | 100, 200 | UDP |
| default | 2001:db8::20:7 | Default | UDP |
| default | 2001:db8::50:7 | 100, 200 | TCP |
| default | 2001:db8::60:7 | 100, 200 | UDP |
| mgt | 10.10.10.7 | Default | UDP |
| mgt | 30.30.30.7 | 100, 200 | TCP |
| mgt | 40.40.40.7 | 300, 400 | UDP |
| mgt | 2001:db8::10:7 | Default | UDP |
| mgt | 2001:db8::30:7 | 100, 200 | TCP |
| mgt | 2001:db8::40:7 | 300, 400 | UDP |
| vrf_with_no_source_interface | 1.2.3.4 | Default | UDP |
| vrf_with_no_source_interface | 2001:db8::1:2:3:4 | Default | UDP |

| Facility | Severity |
| -------- | -------- |
| AAA | warnings |
| ACL | critical |
| BGP | 0 |

#### Logging Servers and Features Device Configuration

```eos
!
logging event storm-control discards global
logging event storm-control discards interval 10
!
logging event congestion-drops interval 10
!
logging repeat-messages
logging buffered 1000000 warnings
no logging trap
logging console errors
logging synchronous level critical
logging host 20.20.20.7
logging host 50.50.50.7 100 200 protocol tcp
logging host 60.60.60.7 100 200
logging host 2001:db8::20:7
logging host 2001:db8::50:7 100 200 protocol tcp
logging host 2001:db8::60:7 100 200
logging vrf mgt host 10.10.10.7
logging vrf mgt host 30.30.30.7 100 200 protocol tcp
logging vrf mgt host 40.40.40.7 300 400
logging vrf mgt host 2001:db8::10:7
logging vrf mgt host 2001:db8::30:7 100 200 protocol tcp
logging vrf mgt host 2001:db8::40:7 300 400
logging vrf vrf_with_no_source_interface host 1.2.3.4
logging vrf vrf_with_no_source_interface host 2001:db8::1:2:3:4
logging format timestamp traditional year timezone
logging format rfc5424
logging source-interface Loopback0
logging vrf mgt source-interface Management0
logging policy match match-list molecule discard
!
logging level AAA warnings
logging level ACL critical
logging level BGP 0
!
no logging event link-status global
```

### MCS Client Summary

MCS client is enabled

| Secondary CVX cluster | Server Hosts | Enabled |
| --------------------- | ------------ | ------- |
| default | 10.90.224.188, 10.90.224.189, leaf2.atd.lab | True |

#### MCS Client Device Configuration

```eos
!
mcs client
   no shutdown
   !
   cvx secondary default
      no shutdown
      server host 10.90.224.188
      server host 10.90.224.189
      server host leaf2.atd.lab
```

### Monitor Sessions

#### Monitor Sessions Summary

##### myMonitoringSession1

####### myMonitoringSession1 Sources

| Sources | Direction | Access Group Type | Access Group Name | Access Group Priority |
| ------- | --------- | ----------------- | ----------------- | --------------------- |
| Ethernet1 | both | ipv6 | ipv6ACL | - |
| Ethernet5 | both | ip | ipv4ACL | 10 |

####### myMonitoringSession1 Destinations and Session Settings

| Settings | Values |
| -------- | ------ |
| Destinations | Ethernet48 |
| Encapsulation Gre Metadata Tx | True |
| Header Remove Size | 32 |
| Truncate Enabled | True |

##### myMonitoringSession2

####### myMonitoringSession2 Sources

| Sources | Direction | Access Group Type | Access Group Name | Access Group Priority |
| ------- | --------- | ----------------- | ----------------- | --------------------- |
| Ethernet3, Ethernet5 | rx | - | - | - |
| Ethernet10-15 | rx | - | - | - |
| Ethernet12 | rx | - | - | - |
| Ethernet18 | tx | - | - | 100 |

####### myMonitoringSession2 Destinations and Session Settings

| Settings | Values |
| -------- | ------ |
| Destinations | Cpu, Ethernet50 |
| Encapsulation Gre Metadata Tx | True |
| Access Group Type | ip |
| Access Group Name | ipv4ACL |
| Sample | 50 |

##### myMonitoringSession3

####### myMonitoringSession3 Sources

| Sources | Direction | Access Group Type | Access Group Name | Access Group Priority |
| ------- | --------- | ----------------- | ----------------- | --------------------- |
| Ethernet20 | both | ip | ipv4ACL | 10 |

####### myMonitoringSession3 Destinations and Session Settings

| Settings | Values |
| -------- | ------ |
| Destinations | - |

##### myMonitoringSession4

####### myMonitoringSession4 Sources

| Sources | Direction | Access Group Type | Access Group Name | Access Group Priority |
| ------- | --------- | ----------------- | ----------------- | --------------------- |
| Ethernet3, Ethernet5 | rx | - | - | - |
| Ethernet10-15 | rx | - | - | - |
| Ethernet12 | rx | - | - | - |
| Ethernet18 | tx | mac | macACL | 100 |

####### myMonitoringSession4 Destinations and Session Settings

| Settings | Values |
| -------- | ------ |
| Destinations | Cpu, Ethernet50 |
| Encapsulation Gre Metadata Tx | True |

##### Monitor Session Default Settings

| Settings | Values |
| -------- | ------ |
| Encapsulation GRE Payload | inner-packet |

#### Monitor Sessions Device Configuration

```eos
!
monitor session myMonitoringSession1 source Ethernet1 ipv6 access-group ipv6ACL
monitor session myMonitoringSession1 source Ethernet5 both ip access-group ipv4ACL priority 10
monitor session myMonitoringSession1 destination Ethernet48
monitor session myMonitoringSession1 truncate
monitor session myMonitoringSession1 header remove size 32
monitor session myMonitoringSession1 encapsulation gre metadata tx
monitor session myMonitoringSession2 ip access-group ipv4ACL
monitor session myMonitoringSession2 source Ethernet3, Ethernet5 rx
monitor session myMonitoringSession2 source Ethernet10-15 rx
monitor session myMonitoringSession2 source Ethernet12 rx
monitor session myMonitoringSession2 source Ethernet18 tx
monitor session myMonitoringSession2 destination Cpu
monitor session myMonitoringSession2 destination Ethernet50
monitor session myMonitoringSession2 sample 50
monitor session myMonitoringSession2 encapsulation gre metadata tx
monitor session myMonitoringSession3 source Ethernet20 both ip access-group ipv4ACL priority 10
monitor session myMonitoringSession4 source Ethernet3, Ethernet5 rx
monitor session myMonitoringSession4 source Ethernet10-15 rx
monitor session myMonitoringSession4 source Ethernet12 rx
monitor session myMonitoringSession4 source Ethernet18 tx mac access-group macACL priority 100
monitor session myMonitoringSession4 destination Cpu
monitor session myMonitoringSession4 destination Ethernet50
monitor session myMonitoringSession4 encapsulation gre metadata tx
!
monitor session default encapsulation gre payload inner-packet
```

### Tap Aggregation

#### Tap Aggregation Summary

| Settings | Values |
| -------- | ------ |
| Mode Exclusive | True |
| Mode Exclusive Profile | tap-aggregation-extended |
| Mode Exclusive No-Errdisable | Ethernet1/1, Ethetnet 42/1, Port-Channel200 |
| Encapsulation Dot1br Strip | True |
| Encapsulation Vn Tag Strip | True |
| Protocol LLDP Trap | True |
| Truncation Size | 169 |
| Mac Timestamp | Header Format 64-bit |
| Mac Timestamp | Header eth-type 5 |
| Mac FCS Error | pass-through |

#### Tap Aggregation Device Configuration

```eos
!
tap aggregation
   mode exclusive profile tap-aggregation-extended
   encapsulation dot1br strip
   encapsulation vn-tag strip
   protocol lldp trap
   mode exclusive no-errdisable Ethernet1/1
   mode exclusive no-errdisable Ethetnet 42/1
   mode exclusive no-errdisable Port-Channel200
   truncation size 169
   mac timestamp header format 64-bit
   mac timestamp header eth-type 5
   mac fcs-error pass-through
```

### SFlow

#### SFlow Summary

| VRF | SFlow Source | SFlow Destination | Port |
| --- | ------------ | ----------------- | ---- |
| AAA | - | 10.6.75.62 | 123 |
| AAA | - | 10.6.75.63 | 333 |
| AAA | Ethernet2 | - | - |
| BBB | - | 10.6.75.62 | 6343 |
| BBB | 1.1.1.1 | - | - |
| CCC | - | 10.6.75.62 | 6343 |
| CCC | Management1 | - | - |
| MGMT | - | 10.6.75.59 | 6343 |
| MGMT | - | 10.6.75.62 | 123 |
| MGMT | - | 10.6.75.63 | 333 |
| MGMT | Ethernet3 | - | - |
| default | - | 10.6.75.62 | 123 |
| default | - | 10.6.75.61 | 6343 |
| default | Management0 | - | - |

sFlow Sample Rate: 1000

sFlow Sample Input Subinterface is enabled.

sFlow Sample Output Subinterface is enabled.

sFlow Polling Interval: 10

sFlow is enabled.

sFlow is disabled on all interfaces by default.

Unmodified egress sFlow is enabled on all interfaces by default.

sFlow hardware acceleration is enabled.

sFlow hardware accelerated Sample Rate: 1024

#### SFlow Hardware Accelerated Modules

| Module | Acceleration Enabled |
| ------ | -------------------- |
| Linecard1 | True |
| Linecard2 | True |
| Linecard3 | False |

#### SFlow Extensions

| Extension | Enabled |
| --------- | ------- |
| bgp | True |
| router | True |
| switch | False |
| tunnel | False |

#### SFlow Interfaces

| Interface | Ingress Enabled | Egress Enabled |
| --------- | --------------- | -------------- |
| Ethernet50 | True | - |
| Ethernet51 | - | True |
| Ethernet52 | True | True (unmodified) |
| Ethernet53 | False | False |
| Ethernet54 | False | False (unmodified) |
| Port-Channel117 | True | True |
| Port-Channel118 | True | True (unmodified) |
| Port-Channel119 | False | False |
| Port-Channel120 | False | False (unmodified) |

#### SFlow Device Configuration

```eos
!
sflow sample dangerous 1000
sflow polling-interval 10
sflow vrf AAA destination 10.6.75.62 123
sflow vrf AAA destination 10.6.75.63 333
sflow vrf AAA source-interface Ethernet2
sflow vrf BBB destination 10.6.75.62
sflow vrf BBB source 1.1.1.1
sflow vrf CCC destination 10.6.75.62
sflow vrf CCC source-interface Management1
sflow vrf MGMT destination 10.6.75.59
sflow vrf MGMT destination 10.6.75.62 123
sflow vrf MGMT destination 10.6.75.63 333
sflow vrf MGMT source-interface Ethernet3
sflow destination 10.6.75.61
sflow destination 10.6.75.62 123
sflow source-interface Management0
sflow sample input subinterface
sflow sample output subinterface
sflow extension bgp
sflow extension router
no sflow extension switch
no sflow extension tunnel
sflow interface disable default
sflow interface egress unmodified enable default
sflow run
sflow hardware acceleration
sflow hardware acceleration sample 1024
sflow hardware acceleration module Linecard1
sflow hardware acceleration module Linecard2
no sflow hardware acceleration module Linecard3
```

### VM Tracer Sessions

#### VM Tracer Summary

| Session | URL | Username | Autovlan | VRF | Source Interface |
| ------- | --- | -------- | -------- | --- | ---------------- |
| session_1 | https://192.168.0.10 | user1 | disabled | MGMT | Management1 |
| session_2 | https://192.168.0.10 | user1 | enabled | - | - |

#### VM Tracer Device Configuration

```eos
!
vmtracer session session_1
   url https://192.168.0.10
   username user1
   password 7 0011D0516421B120A25735E080A16001D1617
   autovlan disable
   vrf MGMT
   source-interface Management1
!
vmtracer session session_2
   url https://192.168.0.10
   username user1
   password 7 0011D0516421B120A25735E080A16001D1617
```

### Event Handler

#### Event Handler Summary

| Handler | Actions | Trigger | Trigger Config |
| ------- | ------- | ------- | -------------- |
| CONFIG_VERSIONING | bash <code>FN=/mnt/flash/startup-config; LFN="`ls -1 $FN.*-* \| tail -n 1`"; if [ -z "$LFN" -o -n "`diff -I 'last modified' $FN $LFN`" ]; then cp $FN $FN.`date +%Y%m%d-%H%M%S`; ls -1r $FN.*-* \| tail -n +11 \| xargs -I % rm %; fi</code> | on-startup-config | - |
| trigger-on-boot | bash <code>if [ 15 -gt 10 ]\nthen\n  echo "a is greater than 10"\nfi</code><br>increment device health metric Metric1 | on-boot | - |
| trigger-on-counters | log | on-counters | poll interval 10<br>condition ( Arad*.IptCrcErrCnt.delta > 100 ) and ( Arad*.UcFifoFullDrop.delta > 100 )<br>granularity per-source |
| trigger-on-counters2 | - | on-counters | condition ( Arad*.IptCrcErrCnt.delta > 100 ) and ( Arad*.UcFifoFullDrop.delta > 100 )<br>granularity per-source |
| trigger-on-counters3 | - | on-counters | - |
| trigger-on-intf | - | on-intf | trigger on-intf Ethernet4 operstatus ip ip6 |
| trigger-on-intf2 | - | on-intf | - |
| trigger-on-intf3 | - | on-intf | - |
| trigger-on-intf4 | - | on-intf | trigger on-intf Ethernet4 ip |
| trigger-on-intf5 | - | on-intf | trigger on-intf Ethernet5 ip6 |
| trigger-on-intf6 | - | on-intf | trigger on-intf Ethernet6 operstatus |
| trigger-on-logging | increment device health metric Metric2 | on-logging | poll interval 10<br>regex ab* |
| trigger-on-logging2 | - | on-logging | regex ab* |
| trigger-on-logging3 | - | on-logging | - |
| trigger-on-maintenance1 | - | on-maintenance | trigger on-maintenance enter interface Management3 after stage linkdown |
| trigger-on-maintenance2 | bash <code>echo "on-maintenance"</code> | on-maintenance | trigger on-maintenance exit unit unit1 before stage bgp |
| trigger-on-maintenance3 | bash <code>echo "on-maintenance"</code> | on-maintenance | trigger on-maintenance enter bgp 10.0.0.2 vrf vrf1 all |
| trigger-on-maintenance4 | - | on-maintenance | - |
| trigger-on-maintenance5 | - | on-maintenance | - |
| trigger-vm-tracer | bash <code>echo "vm-tracer vm"</code> | vm-tracer vm | - |
| trigger-vm-tracer2 | bash <code>echo "vm-tracer vm"\nEOF</code> | vm-tracer vm | - |
| without-trigger-key | - | - | - |

#### Event Handler Device Configuration

```eos
!
event-handler CONFIG_VERSIONING
   trigger on-startup-config
   action bash FN=/mnt/flash/startup-config; LFN="`ls -1 $FN.*-* | tail -n 1`"; if [ -z "$LFN" -o -n "`diff -I 'last modified' $FN $LFN`" ]; then cp $FN $FN.`date +%Y%m%d-%H%M%S`; ls -1r $FN.*-* | tail -n +11 | xargs -I % rm %; fi
   delay 0
!
event-handler trigger-on-boot
   trigger on-boot
   action bash
      if [ 15 -gt 10 ]
      then
        echo "a is greater than 10"
      fi
      EOF
   action log
   action increment device-health metric Metric1
!
event-handler trigger-on-counters
   action log
   trigger on-counters
      poll interval 10
      condition ( Arad*.IptCrcErrCnt.delta > 100 ) and ( Arad*.UcFifoFullDrop.delta > 100 )
      granularity per-source
!
event-handler trigger-on-counters2
   trigger on-counters
      condition ( Arad*.IptCrcErrCnt.delta > 100 ) and ( Arad*.UcFifoFullDrop.delta > 100 )
      granularity per-source
!
event-handler trigger-on-counters3
   trigger on-counters
!
event-handler trigger-on-intf
   trigger on-intf Ethernet4 operstatus ip ip6
!
event-handler trigger-on-intf2
!
event-handler trigger-on-intf3
!
event-handler trigger-on-intf4
   trigger on-intf Ethernet4 ip
!
event-handler trigger-on-intf5
   trigger on-intf Ethernet5 ip6
!
event-handler trigger-on-intf6
   trigger on-intf Ethernet6 operstatus
!
event-handler trigger-on-logging
   action increment device-health metric Metric2
   trigger on-logging
      poll interval 10
      regex ab*
!
event-handler trigger-on-logging2
   trigger on-logging
      regex ab*
!
event-handler trigger-on-logging3
   trigger on-logging
!
event-handler trigger-on-maintenance1
   trigger on-maintenance enter interface Management3 after stage linkdown
!
event-handler trigger-on-maintenance2
   trigger on-maintenance exit unit unit1 before stage bgp
   action bash echo "on-maintenance"
!
event-handler trigger-on-maintenance3
   trigger on-maintenance enter bgp 10.0.0.2 vrf vrf1 all
   action bash echo "on-maintenance"
!
event-handler trigger-on-maintenance4
!
event-handler trigger-on-maintenance5
!
event-handler trigger-vm-tracer
   trigger vm-tracer vm
   action bash echo "vm-tracer vm"
!
event-handler trigger-vm-tracer2
   trigger vm-tracer vm
   action bash echo "vm-tracer vm"\nEOF
!
event-handler without-trigger-key
```

### Object Tracking

#### Object Tracking Summary

| Name | Interface | Tracked Property |
| ---- | --------- | ---------------- |
| MyTrackNoProperty | Ethernet1/1 | line-protocol |
| MyTrackSetProperty | Ethernet2/1 | line-protocol |

#### Object Tracking Device Configuration

```eos
!
track MyTrackNoProperty interface Ethernet1/1 line-protocol
track MyTrackSetProperty interface Ethernet2/1 line-protocol
```

### Monitor Telemetry Postcard Policy

#### Sample Policy Summary

##### samplepo1

###### Match rules

| Rule Name | Rule Type | Source Prefix | Destination Prefix | Protocol | Source Ports | Destination Ports |
| --------- | --------- | ------------- | ------------------ | -------- | ------------ | ----------------- |
| rule1 | ipv4 | 3.4.5.0/24 | 10.3.3.0/24 | tcp<br>udp | -<br>98 | 77, 78-80, 82<br>99 |
| rule2 | ipv6 | 5::0/128 | 4::0/128 | udp | - | 747, 748-800 |
| rule3 | ipv4 | - | - | - | - | - |

##### samplepo2

###### Match rules

| Rule Name | Rule Type | Source Prefix | Destination Prefix | Protocol | Source Ports | Destination Ports |
| --------- | --------- | ------------- | ------------------ | -------- | ------------ | ----------------- |
| rule1 | ipv4 | 3.4.5.0/24 | 10.3.3.0/24 | udp | bgp | https |

#### Telemetry Postcard Policy Profiles

| Profile Name | Ingress Sample Policy |
| ------------ | --------------------- |
| profile1 | samplepo1 |
| profile2 | samplepo2 |

#### Monitor Telemetry Postcard Policy Configuration

```eos
!
monitor telemetry postcard policy
   no disabled
   ingress sample rate 16384
   marker vxlan header word 0 bit 30
   ingress collection gre source 10.3.3.3 destination 10.3.3.4 version 2
   !
   sample policy samplepo1
      match rule1 ipv4
         source prefix 3.4.5.0/24
         destination prefix 10.3.3.0/24
         protocol tcp destination port 77, 78-80, 82
         protocol udp source port 98 destination port 99
      !
      match rule2 ipv6
         source prefix 5::0/128
         destination prefix 4::0/128
         protocol udp destination port 747, 748-800
      !
      match rule3 ipv4
   !
   sample policy samplepo2
      match rule1 ipv4
         source prefix 3.4.5.0/24
         destination prefix 10.3.3.0/24
         protocol udp source port bgp destination port https
   !
   profile profile1
      ingress sample policy samplepo1
   !
   profile profile2
      ingress sample policy samplepo2
```

### Monitor Server Radius Summary

Monitor servers are used for 802.1x authentication.

#### Server Probe Settings

| Setting | Value |
| ------- | ----- |
| Probe interval | 100 |
| Threshold failure | 100 |
| Probe method | access-request |

#### Monitor Server Radius Device Configuration

```eos
!
monitor server radius
   service dot1x
   probe interval 100 seconds
   probe threshold failure 100
   probe method access-request username arista password 7 <removed>
```

## Monitor Connectivity

### Global Configuration

#### Interface Sets

| Name | Interfaces |
| ---- | ---------- |
| GLOBAL_SET | Ethernet1-4 |
| HOST_SET | Loopback2-4, Loopback10-12 |

#### Probing Configuration

| Enabled | Interval | Default Interface Set | Address Only |
| ------- | -------- | --------------------- | ------------ |
| True | 5 | GLOBAL_SET | True |

#### Host Parameters

| Host Name | Description | IPv4 Address | Probing Interface Set | Address Only | URL |
| --------- | ----------- | ------------ | --------------------- | ------------ | --- |
| server1 | server1_connectivity_monitor | 10.10.10.1 | HOST_SET | True | https://server1.local.com |
| server2 | server2_connectivity_monitor | 10.10.10.2 | HOST_SET | True | https://server2.local.com |
| server3 | server3_connectivity_monitor | 10.10.10.3 | HOST_SET | False | - |
| server4 | - | - | - | True | - |

### VRF Configuration

| Name | Description | Default Interface Set | Address Only |
| ---- | ----------- | --------------------- | ------------ |
| blue | - | VRF_GLOBAL_SET | False |
| red | vrf_connectivity_monitor | VRF_GLOBAL_SET | True |
| yellow | - | - | True |

#### Vrf blue Configuration

##### Interface Sets

| Name | Interfaces |
| ---- | ---------- |
| VRF_GLOBAL_SET | Vlan21-24, Vlan29-32 |

##### Host Parameters

| Host Name | Description | IPv4 Address | Probing Interface Set | Address Only | URL |
| --------- | ----------- | ------------ | --------------------- | ------------ | --- |
| server4 | server4_connectivity_monitor | 10.10.20.1 | VRF_GLOBAL_SET | False | https://server2.local.com |
| server5 | server5_connectivity_monitor | 10.10.20.11 | VRF_GLOBAL_SET | True | https://server5.local.com |
| server6 | - | - | - | True | - |

#### Vrf red Configuration

##### Interface Sets

| Name | Interfaces |
| ---- | ---------- |
| VRF_GLOBAL_SET | Vlan21-24, Vlan29-32 |
| VRF_HOST_SET | Loopback12-14, 19-23 |

##### Host Parameters

| Host Name | Description | IPv4 Address | Probing Interface Set | Address Only | URL |
| --------- | ----------- | ------------ | --------------------- | ------------ | --- |
| server2 | server2_connectivity_monitor | 10.10.20.1 | VRF_HOST_SET | True | https://server2.local.com |

#### Vrf yellow Configuration

##### Interface Sets

| Name | Interfaces |
| ---- | ---------- |

### Monitor Connectivity Device Configuration

```eos
!
monitor connectivity
   vrf blue
      interface set VRF_GLOBAL_SET Vlan21-24, Vlan29-32
      local-interfaces VRF_GLOBAL_SET default
      !
      host server4
         description
         server4_connectivity_monitor
         local-interfaces VRF_GLOBAL_SET
         ip 10.10.20.1
         url https://server2.local.com
      !
      host server5
         description
         server5_connectivity_monitor
         local-interfaces VRF_GLOBAL_SET address-only
         ip 10.10.20.11
         url https://server5.local.com
      !
      host server6
   !
   vrf red
      interface set VRF_GLOBAL_SET Vlan21-24, Vlan29-32
      interface set VRF_HOST_SET Loopback12-14, 19-23
      description
      vrf_connectivity_monitor
      local-interfaces VRF_GLOBAL_SET address-only default
      !
      host server2
         description
         server2_connectivity_monitor
         local-interfaces VRF_HOST_SET address-only
         ip 10.10.20.1
         url https://server2.local.com
   !
   vrf yellow
   interval 5
   no shutdown
   interface set GLOBAL_SET Ethernet1-4
   interface set HOST_SET Loopback2-4, Loopback10-12
   local-interfaces GLOBAL_SET address-only default
   !
   host server1
      description
      server1_connectivity_monitor
      local-interfaces HOST_SET address-only
      ip 10.10.10.1
      url https://server1.local.com
   !
   host server2
      description
      server2_connectivity_monitor
      local-interfaces HOST_SET address-only
      ip 10.10.10.2
      url https://server2.local.com
   !
   host server3
      description
      server3_connectivity_monitor
      local-interfaces HOST_SET
      ip 10.10.10.3
   !
   host server4
```

## Monitor Layer 1 Logging

| Layer 1 Event | Logging |
| ------------- | ------- |
| MAC fault | True |
| Logging Transceiver | True |
| Transceiver DOM | True |
| Transceiver communication | True |

### Monitor Layer 1 Device Configuration

```eos
!
monitor layer1
   logging transceiver
   logging transceiver dom
   logging transceiver communication
   logging mac fault
```

### Link Tracking

#### Link Tracking Groups Summary

| Group Name | Minimum Links | Recovery Delay |
| ---------- | ------------- | -------------- |
| EVPN_MH_ES1 | 30 | 500 |
| EVPN_MH_ES2 | - | - |

#### Link Tracking Groups Device Configuration

```eos
!
link tracking group EVPN_MH_ES1
   links minimum 30
   recovery delay 500
link tracking group EVPN_MH_ES2
```

## MLAG

### MLAG Summary

| Domain-id | Local-interface | Peer-address | Peer-link |
| --------- | --------------- | ------------ | --------- |
| sw1-sw2-mlag-domain | Vlan4094 | 172.16.0.1 | Port-Channel12 |

Heartbeat Interval is 5000 milliseconds.
Dual primary detection is enabled. The detection delay is 5 seconds.
Dual primary recovery delay for MLAG interfaces is 90 seconds.
Dual primary recovery delay for NON-MLAG interfaces is 30 seconds.

### MLAG Device Configuration

```eos
!
mlag configuration
   domain-id sw1-sw2-mlag-domain
   heartbeat-interval 5000
   local-interface Vlan4094
   peer-address 172.16.0.1
   peer-link Port-Channel12
   dual-primary detection delay 5 action errdisable all-interfaces
   dual-primary recovery delay mlag 90 non-mlag 30
   reload-delay mlag 400
   reload-delay non-mlag 450
```

## LACP

### LACP Summary

| Port-id range | Rate-limit default | System-priority |
| ------------- | ------------------ | --------------- |
| 1 - 128 | False | - |

### LACP Device Configuration

```eos
!
lacp port-id range 1 128
no lacp rate-limit default
```

## Internal VLAN Allocation Policy

### Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 10 | 40 |

### Internal VLAN Allocation Policy Device Configuration

```eos
!
vlan internal order ascending range 10 40
```

## VLANs

### VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 110 | PR01-DMZ | - |
| 111 | PRIVATE_VLAN_COMMUNITY | - |
| 112 | PRIVATE_VLAN_ISOLATED | - |
| 3010 | MLAG_iBGP_TENANT_A_PROJECT01 | LEAF_PEER_L3 |
| 3011 | MLAG_iBGP_TENANT_A_PROJECT02 | MY_TRUNK_GROUP |
| 3012 | MLAG_iBGP_TENANT_A_PROJECT03 | MY_TRUNK_GROUP |

#### Private VLANs

| Primary Vlan ID | Secondary VLAN ID | Private Vlan Type |
| --------------- | ----------------- | ----------------- |
| community | 111 | 110 |
| isolated | 112 | 110 |

### VLANs Device Configuration

```eos
!
vlan 110
   name PR01-DMZ
!
vlan 111
   name PRIVATE_VLAN_COMMUNITY
   private-vlan community primary vlan 110
!
vlan 112
   name PRIVATE_VLAN_ISOLATED
   private-vlan isolated primary vlan 110
!
vlan 3010
   name MLAG_iBGP_TENANT_A_PROJECT01
   trunk group LEAF_PEER_L3
!
vlan 3011
   name MLAG_iBGP_TENANT_A_PROJECT02
   state active
   trunk group MY_TRUNK_GROUP
!
vlan 3012
   name MLAG_iBGP_TENANT_A_PROJECT03
   state suspend
   trunk group MY_TRUNK_GROUP
```

## MAC Address Table

### MAC Address Table Summary

- MAC address table entry maximum age: 100 seconds

- Logging MAC address interface flapping is Enabled

- 2 MAC moves are considered as one flap

- Size of the flap detection time window: 10 seconds

### MAC Address Table Device Configuration

```eos
!
mac address-table aging-time 100
!
mac address-table notification host-flap logging
mac address-table notification host-flap detection window 10
mac address-table notification host-flap detection moves 2
```

## IP Security

- Hardware encryption is disabled

### IKE policies

| Policy name | IKE lifetime | Encryption | DH group | Local ID | Integrity |
| ----------- | ------------ | ---------- | -------- | -------- | --------- |
| IKE-1 | 24 | aes256 | 20 | 192.168.100.1 | md5 |
| IKE-2 | - | - | - | - | sha512 |
| IKE-FQDN | - | - | - | fqdn.local | - |
| IKE-UFQDN | - | - | - | my.awesome@fqdn.local | - |

### Security Association policies

| Policy name | ESP Integrity | ESP Encryption | Lifetime | PFS DH Group |
| ----------- | ------------- | -------------- | -------- | ------------ |
| SA-1 | - | aes128 | - | 14 |
| SA-2 | - | aes128 | 42 gigabytes | 14 |
| SA-3 | disabled | disabled | 8 hours | 17 |
| SA-4 | md5 | 3des | - | - |
| SA-5 | sha512 | - | - | - |
| SA-6 | sha384 | - | - | - |
| SA-7 | - | - | - | - |

### IPSec profiles

| Profile name | IKE policy | SA policy | Connection | DPD Interval | DPD Time | DPD action | Mode | Flow Parallelization |
| ------------ | ---------- | ----------| ---------- | ------------ | -------- | ---------- | ---- | -------------------- |
| Profile-1 | IKE-1 | SA-1 | start | - | - | - | transport | - |
| Profile-2 | - | SA-2 | start | - | - | - | tunnel | False |
| Profile-3 | - | SA-3 | start | - | - | - | tunnel | True |
| Profile-4 | - | - | - | - | - | - | - | - |

### Key controller

| Profile name |
| ------------ |
| Profile-1 |

### IP Security Device Configuration

```eos
!
ip security
   ike policy IKE-1
      integrity md5
      ike-lifetime 24
      encryption aes256
      dh-group 20
      local-id 192.168.100.1
   !
   ike policy IKE-2
      integrity sha512
   !
   ike policy IKE-FQDN
      local-id fqdn fqdn.local
   !
   ike policy IKE-UFQDN
      local-id fqdn my.awesome@fqdn.local
   !
   sa policy SA-1
      esp encryption aes128
      pfs dh-group 14
   !
   sa policy SA-2
      esp encryption aes128
      sa lifetime 42 gigabytes
      pfs dh-group 14
   !
   sa policy SA-3
      esp encryption null
      esp integrity null
      sa lifetime 8 hours
      pfs dh-group 17
   !
   sa policy SA-4
      esp encryption 3des
      esp integrity md5
   !
   sa policy SA-5
      esp integrity sha512
   !
   sa policy SA-6
      esp integrity sha384
   !
   sa policy SA-7
   !
   profile Profile-1
      ike-policy IKE-1
      sa-policy SA-1
      connection start
      shared-key 7 <removed>
      dpd 42 666 clear
      mode transport
   !
   profile Profile-2
      sa-policy SA-2
      connection start
      shared-key 7 <removed>
      mode tunnel
   !
   profile Profile-3
      sa-policy SA-3
      connection start
      shared-key 7 <removed>
      flow parallelization encapsulation udp
      mode tunnel
   !
   profile Profile-4
   !
   key controller
      profile Profile-1
   hardware encryption disabled
```

## Interfaces

### Switchport Default

#### Switchport Defaults Summary

- Default Switchport Mode: access
- Default Switchport Phone COS: 0
- Default Switchport Phone Trunk: tagged
- Default Switchport Phone VLAN: 69

#### Switchport Default Device Configuration

```eos
!
switchport default mode access
!
switchport default phone cos 0
!
switchport default phone vlan 69
```

### Interface Profiles

#### Interface Profiles Summary

- TEST-PROFILE-1
- TEST-PROFILE-2

#### Interface Profiles Device Configuration

```eos
!
interface profile TEST-PROFILE-1
   command description Molecule
   command no switchport
   command no lldp transmit
!
interface profile TEST-PROFILE-2
   command mtu 9214
   command ptp enable
```

### DPS Interfaces

#### DPS Interfaces Summary

| Interface | IP address | Shutdown | MTU | Flow tracker(s) | TCP MSS Ceiling |
| --------- | ---------- | -------- | --- | --------------- | --------------- |
| Dps1 | 192.168.42.42/24 | True | 666 | Hardware: FT-HW<br>Sampled: FT-S | IPv4: 666<br>IPv6: 666<br>Direction: ingress |

#### DPS Interfaces Device Configuration

```eos
!
interface Dps1
   description Test DPS Interface
   shutdown
   mtu 666
   flow tracker hardware FT-HW
   flow tracker sampled FT-S
   ip address 192.168.42.42/24
   tcp mss ceiling ipv4 666 ipv6 666 ingress
   load-interval 42
```

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet1 | P2P_LINK_TO_DC1-SPINE1_Ethernet1 | dot1q-tunnel | 110-111,200,210-211 | tag | g1, g2 | - |
| Ethernet2 | SRV-POD02_Eth1 | trunk | 110-111,210-211 | - | - | - |
| Ethernet3 | P2P_LINK_TO_DC1-SPINE2_Ethernet2 | trunk | - | 5 | - | - |
| Ethernet5 | Molecule Routing | - | 220 | - | - | - |
| Ethernet6 | SRV-POD02_Eth1 | trunk | 110-111,210-211 | - | - | - |
| Ethernet7 | Molecule L2 | - | - | - | - | - |
| Ethernet11 | interface_in_mode_access_accepting_tagged_LACP | access | 200 | - | - | - |
| Ethernet12 | interface_with_dot1q_tunnel | dot1q-tunnel | 300 | - | - | - |
| Ethernet13 | interface_in_mode_access_with_voice | trunk phone | - | 100 | - | - |
| Ethernet14 | SRV-POD02_Eth1 | trunk | 110-111,210-211 | - | - | - |
| Ethernet15 | PVLAN Promiscuous Access - only one secondary | access | 110 | - | - | - |
| Ethernet16 | PVLAN Promiscuous Trunk - vlan translation out | trunk | 110-112 | - | - | - |
| Ethernet17 | PVLAN Secondary Trunk | trunk | 110-112 | - | - | - |
| Ethernet19 | Switched port with no LLDP rx/tx | access | 110 | - | - | - |
| Ethernet21 | 200MBit/s shape | - | - | - | - | - |
| Ethernet22 | 10% shape | - | - | - | - | - |
| Ethernet23 | Error-correction encoding | - | - | - | - | - |
| Ethernet24 | Disable error-correction encoding | - | - | - | - | - |
| Ethernet25 | Molecule MAC | - | - | - | - | - |
| Ethernet27 | EVPN-Vxlan single-active redundancy | - | - | - | - | - |
| Ethernet28 | EVPN-MPLS multihoming | - | - | - | - | - |
| Ethernet29 | DOT1X Testing - auto phone true | - | - | - | - | - |
| Ethernet30 | DOT1X Testing - force-authorized phone false | - | - | - | - | - |
| Ethernet31 | DOT1X Testing - force-unauthorized - no phone | - | - | - | - | - |
| Ethernet32 | DOT1X Testing - auto reauthentication | - | - | - | - | - |
| Ethernet33 | DOT1X Testing - pae mode authenticator | - | - | - | - | - |
| Ethernet34 | DOT1X Testing - authentication_failure allow | - | - | - | - | - |
| Ethernet35 | DOT1X Testing - authentication_failure drop | - | - | - | - | - |
| Ethernet36 | DOT1X Testing - host-mode single-host | - | - | - | - | - |
| Ethernet37 | DOT1X Testing - host-mode multi-host | - | - | - | - | - |
| Ethernet38 | DOT1X Testing - host-mode multi-host authenticated | - | - | - | - | - |
| Ethernet39 | DOT1X Testing - mac_based_authentication host-mode common true | - | - | - | - | - |
| Ethernet40 | DOT1X Testing - mac_based_authentication always | - | - | - | - | - |
| Ethernet41 | DOT1X Testing - mac_based_authentication always and host-mode common | - | - | - | - | - |
| Ethernet42 | DOT1X Testing - mac_based_authentication | - | - | - | - | - |
| Ethernet43 | DOT1X Testing - timeout values | - | - | - | - | - |
| Ethernet44 | DOT1X Testing - reauthorization_request_limit | - | - | - | - | - |
| Ethernet45 | DOT1X Testing - all features | - | - | - | - | - |
| Ethernet46 | native-vlan-tag-precedence | trunk | - | tag | - | - |
| Ethernet48 | Load Interval | - | - | - | - | - |
| Ethernet50 | SFlow Interface Testing - SFlow ingress enabled | - | - | - | - | - |
| Ethernet51 | SFlow Interface Testing - SFlow egress enabled | - | - | - | - | - |
| Ethernet52 | SFlow Interface Testing - SFlow ingress and egress unmodified enabled | - | - | - | - | - |
| Ethernet53 | SFlow Interface Testing - SFlow ingress and egress disabled | - | - | - | - | - |
| Ethernet54 | SFlow Interface Testing - SFlow ingress and egress unmodified disabled | - | - | - | - | - |
| Ethernet56 | Interface with poe commands and limit in class | - | - | - | - | - |
| Ethernet57 | Interface with poe commands and limit in watts | - | - | - | - | - |
| Ethernet58 | Interface with poe disabled and no other poe keys | - | - | - | - | - |
| Ethernet60 | IP NAT Testing | - | - | - | - | - |
| Ethernet61 | interface_in_mode_access_with_voice | trunk phone | - | 100 | - | - |
| Ethernet62 | interface_in_mode_access_with_voice | trunk phone | - | 100 | - | - |
| Ethernet67 | Custom_Transceiver_Frequency | - | - | - | - | - |
| Ethernet68 | Custom_Transceiver_Frequency | - | - | - | - | - |
| Ethernet69 | IP NAT service-profile | - | - | - | - | - |
| Ethernet73 | DC1-AGG01_Ethernet1 | *trunk | *110,201 | *- | *- | 5 |
| Ethernet74 | MLAG_PEER_DC1-LEAF1B_Ethernet3 | *trunk | *2-4094 | *- | *LEAF_PEER_L3, MLAG | 3 |
| Ethernet75 | MLAG_PEER_DC1-LEAF1B_Ethernet4 | *trunk | *2-4094 | *- | *LEAF_PEER_L3, MLAG | 3 |
| Ethernet76 | SRV-POD03_Eth1 | *trunk | *110,201 | *- | *- | 5 |
| Ethernet78 | DC1-AGG03_Ethernet1 | *trunk | *110,201 | *- | *- | 15 |
| Ethernet79 | DC1-AGG04_Ethernet1 | *trunk | *110,201 | *10 | *- | 16 |
| Ethernet80/1 | LAG Member | *access | *110 | *- | *- | 101 |
| Ethernet80/2 | LAG Member | *trunk | *110-112 | *- | *- | 102 |
| Ethernet80/3 | LAG Member | *trunk | *110-112 | *- | *- | 103 |
| Ethernet80/4 | LAG Member LACP fallback | *trunk | *112 | *- | *- | 104 |
| Ethernet81 | LAG Member | *access | *110 | *- | *- | 109 |
| Ethernet81/2 | LAG Member LACP fallback LLDP ZTP VLAN | *trunk | *112 | *- | *- | 112 |

*Inherited from Port-Channel Interface

##### Encapsulation Dot1q Interfaces

| Interface | Description | Vlan ID | Dot1q VLAN Tag | Dot1q Inner VLAN Tag |
| --------- | ----------- | ------- | -------------- | -------------------- |
| Ethernet8.101 | to WAN-ISP-01 Ethernet2.101 - VRF-C1 | - | 101 | - |
| Ethernet67.1 | Test_encapsulation_dot1q | - | 4 | 34 |

##### Flexible Encapsulation Interfaces

| Interface | Description | Vlan ID | Client Encapsulation | Client Inner Encapsulation | Client VLAN | Client Outer VLAN Tag | Client Inner VLAN Tag | Network Encapsulation | Network Inner Encapsulation | Network VLAN | Network Outer VLAN Tag | Network Inner VLAN Tag |
| --------- | ----------- | ------- | --------------- | --------------------- | ----------- | --------------------- | --------------------- | ---------------- | ---------------------- |------------ | ---------------------- | ---------------------- |
| Ethernet26.1 | TENANT_A pseudowire 1 interface | - | unmatched | - | - | - | - | - | - | - | - | - |
| Ethernet26.100 | TENANT_A pseudowire 1 interface | 10 | dot1q | - | 100 | - | - | client | - | - | - | - |
| Ethernet26.200 | TENANT_A pseudowire 2 interface | - | dot1q | - | 200 | - | - | - | - | - | - | - |
| Ethernet26.300 | TENANT_A pseudowire 3 interface | - | dot1q | - | 300 | - | - | dot1q | - | 400 | - | - |
| Ethernet26.400 | TENANT_A pseudowire 3 interface | - | dot1q | - | - | 400 | 20 | dot1q | - | - | 401 | 21 |
| Ethernet26.500 | TENANT_A pseudowire 3 interface | - | dot1q | - | - | 500 | 50 | client | - | - | - | - |
| Ethernet68.1 | Test_encapsulation_vlan1 | - | dot1q | dot1q | - | 23 | 45 | dot1ad | dot1ad | - | 32 | 54 |
| Ethernet68.2 | Test_encapsulation_vlan2 | - | dot1q | - | 10 | - | - | dot1q | - | - | 32 | 54 |
| Ethernet68.3 | Test_encapsulation_vlan3 | - | dot1ad | - | 12 | - | - | dot1q | - | 25 | - | - |
| Ethernet68.4 | Test_encapsulation_vlan4 | - | dot1ad | dot1q | - | 35 | 60 | dot1q | dot1ad | - | 53 | 6 |
| Ethernet68.5 | Test_encapsulation_vlan5 | - | dot1ad | - | - | 35 | 60 | dot1ad | - | - | 52 | 62 |
| Ethernet68.6 | Test_encapsulation_vlan6 | - | dot1ad | - | - | 35 | 60 | client | - | - | - | - |
| Ethernet68.7 | Test_encapsulation_vlan7 | - | untagged | - | - | - | - | dot1ad | - | - | 35 | 60 |
| Ethernet68.8 | Test_encapsulation_vlan8 | - | untagged | - | - | - | - | dot1q | - | - | 35 | 60 |
| Ethernet68.9 | Test_encapsulation_vlan9 | - | untagged | - | - | - | - | untagged | - | - | - | - |
| Ethernet68.10 | Test_encapsulation_vlan9 | - | dot1q | - | - | 14 | 11 | client inner | - | - | - | - |

##### Private VLAN

| Interface | PVLAN Mapping | Secondary Trunk |
| --------- | ------------- | ----------------|
| Ethernet1 | 20-30 | True |
| Ethernet2 | - | False |
| Ethernet15 | 111 | - |
| Ethernet17 | - | True |

##### VLAN Translations

| Interface | Direction | From VLAN ID(s) | To VLAN ID | From Inner VLAN ID | To Inner VLAN ID | Network | Dot1q-tunnel |
| --------- | --------- | --------------- | ---------- | ------------------ | ---------------- | ------- | ------------ |
| Ethernet1 | both | 12 | 20 | - | - | - | - |
| Ethernet1 | both | 24 | 46 | 78 | - | True | - |
| Ethernet1 | both | 24 | 46 | 78 | - | False | - |
| Ethernet1 | both | 43 | 30 | - | - | - | True |
| Ethernet1 | in | 10 | 24 | - | - | - | - |
| Ethernet1 | in | 23 | 45 | - | - | - | True |
| Ethernet1 | in | 37 | 49 | 56 | - | - | - |
| Ethernet1 | out | 10 | 45 | - | 34 | - | - |
| Ethernet1 | out | 34 | 50 | - | - | - | - |
| Ethernet1 | out | 45 | all | - | - | - | True |
| Ethernet1 | out | 55 | - | - | - | - | - |
| Ethernet3 | out | 23 | 50 | - | - | - | True |
| Ethernet16 | out | 111-112 | 110 | - | - | - | - |

##### TCP MSS Clamping

| Interface | Ipv4 Segment Size | Ipv6 Segment Size | Direction |
| --------- | ----------------- | ----------------- | --------- |
| Ethernet1 | 70 | 75 | egress |
| Ethernet2 | 70 | - | ingress |
| Ethernet3 | - | 65 | - |
| Ethernet4 | 65 | - | - |

##### Transceiver Settings

| Interface | Transceiver Frequency | Media Override |
| --------- | --------------------- | -------------- |
| Ethernet7 | - | 100gbase-ar4 |
| Ethernet67 | 190050.000 | - |
| Ethernet68 | 190080.000 ghz | 100gbase-ar4 |
| Ethernet73 | - | 100gbase-ar4 |

##### Link Tracking Groups

| Interface | Group Name | Direction |
| --------- | ---------- | --------- |
| Ethernet1 | EVPN_MH_ES1 | upstream |
| Ethernet1 | EVPN_MH_ES3, EVPN_MH_ES4 | upstream |
| Ethernet3 | EVPN_MH_ES2 | downstream |

##### Phone Interfaces

| Interface | Mode | Native VLAN | Phone VLAN | Phone VLAN Mode |
| --------- | ---- | ----------- | ---------- | --------------- |
| Ethernet1 | dot1q-tunnel | 5 | 110 | tagged |
| Ethernet13 | trunk phone | 100 | 70 | untagged |
| Ethernet61 | trunk phone | 100 | 70 | untagged phone |
| Ethernet62 | trunk phone | 100 | 70 | tagged phone |
| Port-Channel12 | trunk phone | 100 | 70 | untagged |
| Port-Channel100 | dot1q-tunnel | 5 | 110 | tagged |

##### Multicast Routing

| Interface | IP Version | Static Routes Allowed | Multicast Boundaries |
| --------- | ---------- | --------------------- | -------------------- |
| Ethernet2 | IPv4 | True | ACL_MULTICAST |
| Ethernet2 | IPv6 | - | ACL_V6_MULTICAST |
| Ethernet4 | IPv4 | True | 224.0.1.0/24, 224.0.2.0/24 |
| Ethernet4 | IPv6 | - | ff00::/16, ff01::/16 |
| Ethernet9 | IPv4 | - | ACL_MULTICAST |
| Ethernet9 | IPv6 | True | - |

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_LINK_TO_DC1-SPINE1_Ethernet1 | - | 172.31.255.1/31 | default | 1500 | - | - | - |
| Ethernet2 | SRV-POD02_Eth1 | - | 10.1.255.3/24 | default | - | - | - | - |
| Ethernet3 | P2P_LINK_TO_DC1-SPINE2_Ethernet2 | - | 172.31.128.1/31 | default | 1500 | - | - | - |
| Ethernet8.101 | to WAN-ISP-01 Ethernet2.101 - VRF-C1 | - | 172.31.128.1/31 | default | - | - | - | - |
| Ethernet9 | interface_with_mpls_enabled | - | 172.31.128.9/31 | default | - | - | - | - |
| Ethernet10 | interface_with_mpls_disabled | - | 172.31.128.10/31 | default | - | - | - | - |
| Ethernet18 | PBR Description | - | 192.0.2.1/31 | default | 1500 | - | - | - |
| Ethernet47 | IP Helper | - | 172.31.255.1/31 | default | - | - | - | - |
| Ethernet63 | DHCP client interface | - | dhcp | default | - | - | - | - |
| Ethernet64 | DHCP server interface | - | 192.168.42.42/24 | default | - | - | - | - |
| Ethernet65 | Multiple VRIDs | - | 192.0.2.2/25 | default | - | False | - | - |
| Ethernet66 | Multiple VRIDs and tracking | - | 192.0.2.2/25 | default | - | False | - | - |
| Ethernet80 | LAG Member | 17 | *192.0.2.3/31 | **default | **- | **- | **- | **- |

*Inherited from Port-Channel Interface

##### IP NAT: Source Static

| Interface | Direction | Original IP | Original Port | Access List | Translated IP | Translated Port | Protocol | Group | Priority | Comment |
| --------- | --------- | ----------- | ------------- | ----------- | ------------- | --------------- | -------- | ----- | -------- | ------- |
| Ethernet60 | - | 3.0.0.1 | - | - | 4.0.0.1 | - | - | - | 0 | - |
| Ethernet60 | - | 3.0.0.2 | 22 | - | 4.0.0.2 | - | - | - | 0 | - |
| Ethernet60 | - | 3.0.0.3 | 22 | - | 4.0.0.3 | 23 | - | - | 0 | - |
| Ethernet60 | - | 3.0.0.4 | 22 | - | 4.0.0.4 | 23 | UDP | - | 0 | - |
| Ethernet60 | - | 3.0.0.5 | 22 | - | 4.0.0.5 | 23 | TCP | 1 | 0 | - |
| Ethernet60 | - | 3.0.0.6 | 22 | - | 4.0.0.6 | 23 | TCP | 2 | 5 | Comment Test |
| Ethernet60 | - | 3.0.0.7 | - | ACL21 | 4.0.0.7 | - | - | - | 0 | - |
| Ethernet60 | ingress | 3.0.0.8 | - | - | 4.0.0.8 | - | - | - | 0 | - |

##### IP NAT: Source Dynamic

| Interface | Access List | NAT Type | Pool Name | Priority | Comment |
| --------- | ----------- | -------- | --------- | -------- | ------- |
| Ethernet60 | ACL11 | pool | POOL11 | 0 | - |
| Ethernet60 | ACL12 | pool | POOL11 | 0 | POOL11 shared with ACL11/12 |
| Ethernet60 | ACL13 | pool | POOL13 | 10 | - |
| Ethernet60 | ACL14 | pool | POOL14 | 1 | Priority low end |
| Ethernet60 | ACL15 | pool | POOL15 | 4294967295 | Priority high end |
| Ethernet60 | ACL16 | pool | POOL16 | 0 | Priority default |
| Ethernet60 | ACL17 | overload | - | 10 | Priority_10 |
| Ethernet60 | ACL18 | pool-address-only | POOL18 | 10 | Priority_10 |
| Ethernet60 | ACL19 | pool-full-cone | POOL19 | 10 | Priority_10 |

##### IP NAT: Destination Static

| Interface | Direction | Original IP | Original Port | Access List | Translated IP | Translated Port | Protocol | Group | Priority | Comment |
| --------- | --------- | ----------- | ------------- | ----------- | ------------- | --------------- | -------- | ----- | -------- | ------- |
| Ethernet60 | - | 1.0.0.1 | - | - | 2.0.0.1 | - | - | - | 0 | - |
| Ethernet60 | - | 1.0.0.2 | 22 | - | 2.0.0.2 | - | - | - | 0 | - |
| Ethernet60 | - | 1.0.0.3 | 22 | - | 2.0.0.3 | 23 | - | - | 0 | - |
| Ethernet60 | - | 1.0.0.4 | 22 | - | 2.0.0.4 | 23 | udp | - | 0 | - |
| Ethernet60 | - | 1.0.0.5 | 22 | - | 2.0.0.5 | 23 | tcp | 1 | 0 | - |
| Ethernet60 | - | 1.0.0.6 | 22 | - | 2.0.0.6 | 23 | tcp | 2 | 5 | Comment Test |
| Ethernet60 | - | 1.0.0.7 | - | ACL21 | 2.0.0.7 | - | - | - | 0 | - |
| Ethernet60 | egress | 239.0.0.1 | - | - | 239.0.0.2 | - | - | - | 0 | - |

##### IP NAT: Destination Dynamic

| Interface | Access List | Pool Name | Priority | Comment |
| --------- | ----------- | --------- | -------- | ------- |
| Ethernet60 | ACL1 | POOL1 | 0 | - |
| Ethernet60 | ACL2 | POOL1 | 0 | POOL1 shared with ACL1/2 |
| Ethernet60 | ACL3 | POOL3 | 10 | - |
| Ethernet60 | ACL4 | POOL4 | 1 | Priority low end |
| Ethernet60 | ACL5 | POOL5 | 4294967295 | Priority high end |
| Ethernet60 | ACL6 | POOL6 | 0 | Priority default |

##### IP NAT: Interfaces configured via profile

| Interface | Profile |
| --------- |-------- |
| Ethernet69 | TEST-NAT-PROFILE |

##### IPv6

| Interface | Description | Channel Group | IPv6 Address | VRF | MTU | Shutdown | ND RA Disabled | Managed Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | ----------- | --------------| ------------ | --- | --- | -------- | -------------- | -------------------| ----------- | ------------ |
| Ethernet3 | P2P_LINK_TO_DC1-SPINE2_Ethernet2 | - | 2002:ABDC::1/64 | default | 1500 | - | - | - | - | - |
| Ethernet4 | Molecule IPv6 | - | 2020::2020/64 | default | 9100 | True | True | True | IPv6_ACL_IN | IPv6_ACL_OUT |
| Ethernet8.101 | to WAN-ISP-01 Ethernet2.101 - VRF-C1 | - | 2002:ABDC::1/64 | default | - | - | - | - | - | - |
| Ethernet55 | DHCPv6 Relay Testing | - | a0::1/64 | default | - | False | - | - | - | - |
| Ethernet65 | Multiple VRIDs | - | 2001:db8::2/64 | default | - | False | - | - | - | - |
| Ethernet66 | Multiple VRIDs and tracking | - | 2001:db8::2/64 | default | - | False | - | - | - | - |

##### VRRP Details

| Interface | VRRP-ID | Priority | Advertisement Interval | Preempt | Tracked Object Name(s) | Tracked Object Action(s) | IPv4 Virtual IP | IPv4 VRRP Version | IPv6 Virtual IP |
| --------- | ------- | -------- | ---------------------- | --------| ---------------------- | ------------------------ | --------------- | ----------------- | --------------- |
| Ethernet65 | 1 | 105 | 2 | Enabled | - | - | 192.0.2.1 | 2 | - |
| Ethernet65 | 2 | - | - | Enabled | - | - | - | 2 | 2001:db8::1 |
| Ethernet66 | 1 | 105 | 2 | Enabled | ID1TrackedObjectDecrement, ID1TrackedObjectShutdown | Decrement 5, Shutdown | 192.0.2.1 | 2 | - |
| Ethernet66 | 2 | - | - | Enabled | ID2TrackedObjectDecrement, ID2TrackedObjectShutdown | Decrement 10, Shutdown | - | 2 | 2001:db8::1 |
| Ethernet66 | 3 | - | - | Disabled | - | - | 100.64.0.1 | 3 | - |

##### ISIS

| Interface | Channel Group | ISIS Instance | ISIS BFD | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | ISIS Authentication Mode |
| --------- | ------------- | ------------- | -------- | ----------- | ---- | ----------------- | ------------- | ------------------------ |
| Ethernet5 | - | ISIS_TEST | True | 99 | point-to-point | level-2 | False | - |
| Ethernet8 | - | - | - | - | - | - | - | md5 |
| Ethernet8.101 | - | - | - | - | - | - | - | md5 |
| Ethernet9 | - | - | - | - | - | - | - | sha |
| Ethernet10 | - | - | - | - | - | - | - | sha |
| Ethernet11 | - | - | - | - | - | - | - | shared-secret |
| Ethernet12 | - | - | - | - | - | - | - | shared-secret |
| Ethernet13 | - | - | - | - | - | - | - | Level-1: md5<br>Level-2: text |
| Ethernet14 | - | - | - | - | - | - | - | Level-1: md5<br>Level-2: sha |
| Ethernet15 | - | - | - | - | - | - | - | Level-1: shared-secret<br>Level-2: shared-secret |
| Ethernet16 | - | - | - | - | - | - | - | Level-1: shared-secret<br>Level-2: shared-secret |
| Ethernet17 | - | - | - | - | - | - | - | Level-1: sha<br>Level-2: sha |
| Ethernet18 | - | - | - | - | - | - | - | Level-1: sha<br>Level-2: sha |
| Ethernet20 | - | - | - | - | - | - | - | Level-1: shared-secret<br>Level-2: md5 |
| Ethernet21 | - | - | - | - | - | - | - | Level-1: md5 |
| Ethernet22 | - | - | - | - | - | - | - | Level-2: sha |
| Ethernet23 | - | - | - | - | - | - | - | Level-2: shared-secret |
| Ethernet74 | 3 | *EVPN_UNDERLAY | - | *- | *- | *- | *- | *sha |
| Ethernet75 | 3 | *EVPN_UNDERLAY | - | *- | *- | *- | *- | *sha |
| Ethernet77 | 8 | *EVPN_UNDERLAY | - | *- | *- | *- | *- | *Level-1: md5<br>Level-2: md5 |
| Ethernet78 | 15 | *- | - | *- | *- | *- | *- | *md5 |
| Ethernet79 | 16 | *EVPN_UNDERLAY | - | *- | *- | *- | *- | *md5 |
| Ethernet81/10 | 110 | *ISIS_TEST | True | *99 | *point-to-point | *level-2 | *True | *- |

*Inherited from Port-Channel Interface

##### EVPN Multihoming

####### EVPN Multihoming Summary

| Interface | Ethernet Segment Identifier | Multihoming Redundancy Mode | Route Target |
| --------- | --------------------------- | --------------------------- | ------------ |
| Ethernet27 | 0000:0000:0000:0102:0304 | single-active | 00:00:01:02:03:04 |
| Ethernet28 | 0000:0000:0000:0102:0305 | all-active | 00:00:01:02:03:05 |

####### Designated Forwarder Election Summary

| Interface | Algorithm | Preference Value | Dont Preempt | Hold time | Subsequent Hold Time | Candidate Reachability Required |
| --------- | --------- | ---------------- | ------------ | --------- | -------------------- | ------------------------------- |
| Ethernet27 | preference | 100 | True | 10 | - | True |

####### EVPN-MPLS summary

| Interface | Shared Index | Tunnel Flood Filter Time |
| --------- | ------------ | ------------------------ |
| Ethernet28 | 100 | 100 |

##### Error Correction Encoding Interfaces

| Interface | Enabled |
| --------- | ------- |
| Ethernet23 | fire-code<br>reed-solomon |
| Ethernet24 | Disabled |
| Ethernet81/1 | fire-code<br>reed-solomon |

#### Priority Flow Control

| Interface | PFC | Priority | Drop/No_drop |
| Ethernet1 | True | 5 | False |
| Ethernet2 | True | 5 | True |
| Ethernet3 | False | - | - |
| Ethernet4 | True | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_DC1-SPINE1_Ethernet1
   mtu 1500
   bgp session tracker ST1
   l2 mtu 8000
   l2 mru 8000
   speed forced 100gfull
   switchport access vlan 200
   switchport trunk native vlan tag
   switchport phone vlan 110
   switchport phone trunk tagged
   switchport vlan translation in required
   switchport dot1q vlan tag required
   switchport trunk allowed vlan 110-111,210-211
   switchport mode dot1q-tunnel
   switchport dot1q ethertype 1536
   switchport vlan forwarding accept all
   switchport trunk group g1
   switchport trunk group g2
   no switchport
   switchport source-interface tx
   switchport vlan translation 12 20
   switchport vlan translation 24 inner 78 network 46
   switchport vlan translation 24 inner 78 46
   switchport vlan translation 43 dot1q-tunnel 30
   switchport vlan translation in 10 24
   switchport vlan translation in 37 inner 56 49
   switchport vlan translation in 23 dot1q-tunnel 45
   switchport vlan translation out 34 50
   switchport vlan translation out 10 45 inner 34
   switchport vlan translation out 45 dot1q-tunnel all
   switchport trunk private-vlan secondary
   switchport pvlan mapping 20-30
   ip address 172.31.255.1/31
   ip verify unicast source reachable-via rx
   bfd interval 500 min-rx 500 multiplier 5
   bfd echo
   ip igmp host-proxy
   ip igmp host-proxy 239.0.0.1
   ip igmp host-proxy 239.0.0.2 exclude 10.0.2.1
   ip igmp host-proxy 239.0.0.3 include 10.0.3.1
   ip igmp host-proxy 239.0.0.4 include 10.0.4.3
   ip igmp host-proxy 239.0.0.4 include 10.0.4.4
   ip igmp host-proxy 239.0.0.4 exclude 10.0.4.1
   ip igmp host-proxy 239.0.0.4 exclude 10.0.4.2
   ip igmp host-proxy access-list ACL1
   ip igmp host-proxy access-list ACL2
   ip igmp host-proxy report-interval 2
   ip igmp host-proxy version 2
   tcp mss ceiling ipv4 70 ipv6 75 egress
   switchport port-security
   switchport port-security mac-address maximum disabled
   priority-flow-control on
   priority-flow-control priority 5 drop
   switchport backup-link Ethernet5 prefer vlan 10
   switchport backup preemption-delay 35
   switchport backup mac-move-burst 20
   switchport backup mac-move-burst-interval 30
   switchport backup initial-mac-move-delay 10
   switchport backup dest-macaddr 01:00:00:00:00:00
   link tracking group EVPN_MH_ES1 upstream
   link tracking group EVPN_MH_ES3 upstream
   link tracking group EVPN_MH_ES4 upstream
   comment
   Comment created from eos_cli under ethernet_interfaces.Ethernet1
   EOF

!
interface Ethernet2
   description SRV-POD02_Eth1
   switchport dot1q vlan tag disallowed
   switchport trunk allowed vlan 110-111,210-211
   switchport mode trunk
   switchport
   ip address 10.1.255.3/24
   ip address 1.1.1.3/24 secondary
   ip address 1.1.1.4/24 secondary
   ip address 10.0.0.254/24 secondary
   ip address 192.168.1.1/24 secondary
   tcp mss ceiling ipv4 70 ingress
   multicast ipv4 boundary ACL_MULTICAST
   multicast ipv6 boundary ACL_V6_MULTICAST out
   multicast ipv4 static
   switchport port-security violation protect log
   switchport port-security mac-address maximum 100
   priority-flow-control on
   priority-flow-control priority 5 no-drop
   storm-control broadcast level pps 500
   storm-control unknown-unicast level 1
   storm-control all level 10
   spanning-tree bpduguard disable
   spanning-tree bpdufilter disable
!
interface Ethernet3
   description P2P_LINK_TO_DC1-SPINE2_Ethernet2
   mtu 1500
   switchport trunk native vlan 5
   switchport mode trunk
   no switchport
   switchport vlan translation out 23 dot1q-tunnel 50
   no snmp trap link-change
   ip address 172.31.128.1/31
   ipv6 enable
   ipv6 address 2002:ABDC::1/64
   ipv6 nd prefix 2345:ABCD:3FE0::1/96 infinite 50 no-autoconfig
   ipv6 nd prefix 2345:ABCD:3FE0::2/96 50 infinite
   ipv6 nd prefix 2345:ABCD:3FE0::3/96 100000 no-autoconfig
   tcp mss ceiling ipv6 65
   switchport port-security
   no switchport port-security mac-address maximum disabled
   switchport port-security vlan 1 mac-address maximum 3
   switchport port-security vlan 2 mac-address maximum 3
   switchport port-security vlan 2 mac-address maximum 4
   switchport port-security vlan 3 mac-address maximum 3
   switchport port-security vlan 22 mac-address maximum 4
   switchport port-security vlan 41 mac-address maximum 4
   switchport port-security vlan default mac-address maximum 2
   no priority-flow-control
   spanning-tree guard root
   switchport backup-link Ethernet4
   link tracking group EVPN_MH_ES2 downstream
!
interface Ethernet4
   description Molecule IPv6
   shutdown
   mtu 9100
   no switchport
   snmp trap link-change
   ipv6 enable
   ipv6 address 2020::2020/64
   ipv6 address FE80:FEA::AB65/64 link-local
   ipv6 nd ra disabled
   ipv6 nd managed-config-flag
   tcp mss ceiling ipv4 65
   ipv6 access-group IPv6_ACL_IN in
   ipv6 access-group IPv6_ACL_OUT out
   multicast ipv4 boundary 224.0.1.0/24 out
   multicast ipv4 boundary 224.0.2.0/24
   multicast ipv6 boundary ff00::/16 out
   multicast ipv6 boundary ff01::/16 out
   multicast ipv4 static
   switchport port-security violation protect
   priority-flow-control on
   spanning-tree guard none
!
interface Ethernet5
   description Molecule Routing
   no shutdown
   mtu 9100
   switchport access vlan 220
   no switchport
   ip ospf cost 99
   ip ospf network point-to-point
   ip ospf authentication message-digest
   ip ospf authentication-key 7 <removed>
   ip ospf area 100
   ip ospf message-digest-key 1 sha512 7 <removed>
   pim ipv4 sparse-mode
   pim ipv4 bidirectional
   pim ipv4 border-router
   pim ipv4 hello interval 10
   pim ipv4 hello count 2.5
   pim ipv4 dr-priority 200
   pim ipv4 bfd
   isis enable ISIS_TEST
   isis bfd
   isis circuit-type level-2
   isis metric 99
   no isis hello padding
   isis network point-to-point
   spanning-tree guard loop
!
interface Ethernet6
   description SRV-POD02_Eth1
   logging event link-status
   logging event congestion-drops
   switchport trunk allowed vlan 110-111,210-211
   switchport mode trunk
   switchport
   logging event storm-control discards
   spanning-tree bpduguard enable
   spanning-tree bpdufilter enable
   logging event spanning-tree
!
interface Ethernet7
   description Molecule L2
   no shutdown
   mtu 7000
   switchport
   ptp enable
   ptp announce interval 10
   ptp announce timeout 30
   ptp delay-mechanism p2p
   ptp delay-req interval 20
   ptp role master
   ptp sync-message interval 5
   ptp transport layer2
   ptp vlan all
   service-profile QoS
   qos trust cos
   qos cos 5
   storm-control broadcast level pps 10
   storm-control multicast level 50
   storm-control unknown-unicast level 10
   storm-control all level 75
   spanning-tree portfast
   spanning-tree bpduguard enable
   spanning-tree bpdufilter enable
   vmtracer vmware-esx
   transceiver media override 100gbase-ar4
!
interface Ethernet8
   description to WAN-ISP1-01 Ethernet2
   no switchport
   no lldp transmit
   no lldp receive
   isis authentication mode md5 rx-disabled
   isis authentication key 0 <removed>
!
interface Ethernet8.101
   description to WAN-ISP-01 Ethernet2.101 - VRF-C1
   encapsulation dot1q vlan 101
   ip address 172.31.128.1/31
   ipv6 enable
   ipv6 address 2002:ABDC::1/64
   isis authentication mode md5
   isis authentication key 0 <removed>
!
interface Ethernet9
   description interface_with_mpls_enabled
   no switchport
   ip address 172.31.128.9/31
   mpls ldp interface
   multicast ipv4 boundary ACL_MULTICAST out
   multicast ipv6 static
   mpls ip
   isis authentication mode sha key-id 2 rx-disabled
   isis authentication key 0 <removed>
!
interface Ethernet10
   description interface_with_mpls_disabled
   no switchport
   ip address 172.31.128.10/31
   no mpls ldp interface
   no mpls ip
   isis authentication mode sha key-id 2
   isis authentication key 0 <removed>
!
interface Ethernet11
   description interface_in_mode_access_accepting_tagged_LACP
   switchport access vlan 200
   switchport mode access
   switchport
   l2-protocol encapsulation dot1q vlan 200
   isis authentication mode shared-secret profile profile1 algorithm sha-1 rx-disabled
!
interface Ethernet12
   description interface_with_dot1q_tunnel
   switchport access vlan 300
   switchport mode dot1q-tunnel
   switchport
   isis authentication mode shared-secret profile profile1 algorithm sha-1
!
interface Ethernet13
   description interface_in_mode_access_with_voice
   no logging event link-status
   no logging event congestion-drops
   switchport trunk native vlan 100
   switchport phone vlan 70
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   isis authentication mode md5 rx-disabled level-1
   isis authentication mode text rx-disabled level-2
   isis authentication key 0 <removed> level-1
   isis authentication key 0 <removed> level-2
   no logging event storm-control discards
   no logging event spanning-tree
!
interface Ethernet14
   description SRV-POD02_Eth1
   logging event link-status
   switchport trunk allowed vlan 110-111,210-211
   switchport mode trunk
   switchport
   isis authentication mode md5 level-1
   isis authentication mode sha key-id 10 level-2
   isis authentication key 0 <removed> level-1
   isis authentication key 0 <removed> level-2
!
interface Ethernet15
   description PVLAN Promiscuous Access - only one secondary
   switchport access vlan 110
   switchport mode access
   switchport
   switchport pvlan mapping 111
   isis authentication mode shared-secret profile profile1 algorithm sha-256 level-1
   isis authentication mode shared-secret profile profile2 algorithm sha-1 level-2
!
interface Ethernet16
   description PVLAN Promiscuous Trunk - vlan translation out
   switchport vlan translation out required
   switchport trunk allowed vlan 110-112
   switchport mode trunk
   switchport
   switchport vlan translation out 111-112 110
   isis authentication mode shared-secret profile profile1 algorithm sha-256 rx-disabled level-1
   isis authentication mode shared-secret profile profile2 algorithm sha-1 rx-disabled level-2
!
interface Ethernet17
   description PVLAN Secondary Trunk
   switchport trunk allowed vlan 110-112
   switchport mode trunk
   switchport
   switchport trunk private-vlan secondary
   isis authentication mode sha key-id 5 rx-disabled level-1
   isis authentication mode sha key-id 10 rx-disabled level-2
!
interface Ethernet18
   description PBR Description
   mtu 1500
   no switchport
   ip address 192.0.2.1/31
   service-policy type pbr input MyLANServicePolicy
   isis authentication mode sha key-id 5 level-1
   isis authentication mode sha key-id 10 level-2
!
interface Ethernet19
   description Switched port with no LLDP rx/tx
   switchport access vlan 110
   switchport mode access
   switchport
   no lldp transmit
   no lldp receive
   lldp tlv transmit ztp vlan 666
   isis authentication key-id 2 algorithm sha-512 key 0 <removed>
   isis authentication key-id 3 algorithm sha-512 rfc-5310 key 0 <removed>
   isis authentication key-id 1 algorithm sha-1 key 0 <removed> level-1
   isis authentication key-id 4 algorithm sha-1 rfc-5310 key 0 <removed> level-1
   isis authentication key-id 1 algorithm sha-1 key 0 <removed> level-2
   isis authentication key-id 5 algorithm sha-1 rfc-5310 key 0 <removed> level-2
!
interface Ethernet20
   description Port patched through patch-panel to pseudowire
   no switchport
   no lldp transmit
   no lldp receive
   isis authentication mode shared-secret profile profile1 algorithm sha-256 level-1
   isis authentication mode md5 level-2
   isis authentication key 0 <removed> level-2
!
interface Ethernet21
   description 200MBit/s shape
   switchport
   no qos trust
   shape rate 200000 kbps
   isis authentication mode md5 rx-disabled level-1
   isis authentication key 0 <removed> level-1
!
interface Ethernet22
   description 10% shape
   switchport
   shape rate 10 percent
   isis authentication mode sha key-id 100 level-2
   isis authentication key 0 <removed> level-2
!
interface Ethernet23
   description Error-correction encoding
   error-correction encoding fire-code
   error-correction encoding reed-solomon
   switchport
   isis authentication mode shared-secret profile profile2 algorithm sha-1 level-2
!
interface Ethernet24
   description Disable error-correction encoding
   no error-correction encoding
   switchport
!
interface Ethernet25
   description Molecule MAC
   switchport
   mac access-group MAC_ACL_IN in
   mac access-group MAC_ACL_OUT out
!
interface Ethernet26
   no switchport
!
interface Ethernet26.1
   description TENANT_A pseudowire 1 interface
   encapsulation vlan
      client unmatched
!
interface Ethernet26.100
   description TENANT_A pseudowire 1 interface
   vlan id 10
   encapsulation vlan
      client dot1q 100 network client
!
interface Ethernet26.200
   description TENANT_A pseudowire 2 interface
   encapsulation vlan
      client dot1q 200
!
interface Ethernet26.300
   description TENANT_A pseudowire 3 interface
   encapsulation vlan
      client dot1q 300 network dot1q 400
!
interface Ethernet26.400
   description TENANT_A pseudowire 3 interface
   encapsulation vlan
      client dot1q outer 400 inner 20 network dot1q outer 401 inner 21
!
interface Ethernet26.500
   description TENANT_A pseudowire 3 interface
   encapsulation vlan
      client dot1q outer 500 inner 50 network client
!
interface Ethernet27
   description EVPN-Vxlan single-active redundancy
   switchport
   !
   evpn ethernet-segment
      identifier 0000:0000:0000:0102:0304
      redundancy single-active
      designated-forwarder election algorithm preference 100 dont-preempt
      designated-forwarder election hold-time 10
      designated-forwarder election candidate reachability required
      route-target import 00:00:01:02:03:04
!
interface Ethernet28
   description EVPN-MPLS multihoming
   switchport
   !
   evpn ethernet-segment
      identifier 0000:0000:0000:0102:0305
      mpls tunnel flood filter time 100
      mpls shared index 100
      route-target import 00:00:01:02:03:05
!
interface Ethernet29
   description DOT1X Testing - auto phone true
   switchport
   dot1x port-control auto
   dot1x port-control force-authorized phone
!
interface Ethernet30
   description DOT1X Testing - force-authorized phone false
   switchport
   dot1x port-control force-authorized
   no dot1x port-control force-authorized phone
!
interface Ethernet31
   description DOT1X Testing - force-unauthorized - no phone
   switchport
   dot1x port-control force-unauthorized
!
interface Ethernet32
   description DOT1X Testing - auto reauthentication
   switchport
   dot1x reauthentication
   dot1x port-control auto
!
interface Ethernet33
   description DOT1X Testing - pae mode authenticator
   switchport
   dot1x pae authenticator
!
interface Ethernet34
   description DOT1X Testing - authentication_failure allow
   switchport
   dot1x authentication failure action traffic allow vlan 800
!
interface Ethernet35
   description DOT1X Testing - authentication_failure drop
   switchport
   dot1x authentication failure action traffic drop
!
interface Ethernet36
   description DOT1X Testing - host-mode single-host
   switchport
   dot1x host-mode single-host
!
interface Ethernet37
   description DOT1X Testing - host-mode multi-host
   switchport
   dot1x host-mode multi-host
!
interface Ethernet38
   description DOT1X Testing - host-mode multi-host authenticated
   switchport
   dot1x host-mode multi-host authenticated
!
interface Ethernet39
   description DOT1X Testing - mac_based_authentication host-mode common true
   switchport
   dot1x mac based authentication host-mode common
!
interface Ethernet40
   description DOT1X Testing - mac_based_authentication always
   switchport
   dot1x mac based authentication always
!
interface Ethernet41
   description DOT1X Testing - mac_based_authentication always and host-mode common
   switchport
   dot1x mac based authentication host-mode common
   dot1x mac based authentication always
!
interface Ethernet42
   description DOT1X Testing - mac_based_authentication
   switchport
   dot1x mac based authentication
!
interface Ethernet43
   description DOT1X Testing - timeout values
   switchport
   dot1x timeout quiet-period 10
   dot1x timeout reauth-timeout-ignore always
   dot1x timeout tx-period 6
   dot1x timeout reauth-period server
   dot1x timeout idle-host 15 seconds
!
interface Ethernet44
   description DOT1X Testing - reauthorization_request_limit
   switchport
   dot1x eapol disabled
   dot1x reauthorization request limit 3
!
interface Ethernet45
   description DOT1X Testing - all features
   switchport
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 800
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout quiet-period 10
   dot1x timeout reauth-timeout-ignore always
   dot1x timeout tx-period 10
   dot1x timeout reauth-period server
   dot1x timeout idle-host 10 seconds
   dot1x reauthorization request limit 2
   dot1x unauthorized access vlan membership egress
   dot1x unauthorized native vlan membership egress
   dot1x eapol authentication failure fallback mba timeout 600
!
interface Ethernet46
   description native-vlan-tag-precedence
   switchport trunk native vlan tag
   switchport mode trunk
   switchport
!
interface Ethernet47
   description IP Helper
   no switchport
   ip address 172.31.255.1/31
   ip helper-address 10.10.64.151
   ip helper-address 10.10.96.101 source-interface Loopback0
   ip helper-address 10.10.96.150 vrf MGMT source-interface Loopback0
   ip helper-address 10.10.96.151 vrf MGMT
!
interface Ethernet48
   description Load Interval
   load-interval 5
   switchport
!
interface Ethernet50
   description SFlow Interface Testing - SFlow ingress enabled
   switchport
   sflow enable
!
interface Ethernet51
   description SFlow Interface Testing - SFlow egress enabled
   switchport
   sflow egress enable
!
interface Ethernet52
   description SFlow Interface Testing - SFlow ingress and egress unmodified enabled
   switchport
   sflow enable
   sflow egress unmodified enable
!
interface Ethernet53
   description SFlow Interface Testing - SFlow ingress and egress disabled
   switchport
   no sflow enable
   no sflow egress enable
!
interface Ethernet54
   description SFlow Interface Testing - SFlow ingress and egress unmodified disabled
   switchport
   no sflow enable
   no sflow egress unmodified enable
!
interface Ethernet55
   description DHCPv6 Relay Testing
   no shutdown
   no switchport
   ipv6 dhcp relay destination a0::2 link-address a0::3
   ipv6 dhcp relay destination a0::4 vrf TEST local-interface Loopback55 link-address a0::5
   ipv6 address a0::1/64
!
interface Ethernet56
   description Interface with poe commands and limit in class
   switchport
   poe priority low
   poe reboot action power-off
   poe link down action power-off 10 seconds
   poe shutdown action maintain
   poe limit 30.00 watts
   poe negotiation lldp disabled
!
interface Ethernet57
   description Interface with poe commands and limit in watts
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 45.00 watts fixed
   poe legacy detect
!
interface Ethernet58
   description Interface with poe disabled and no other poe keys
   switchport
   poe disabled
!
interface Ethernet60
   description IP NAT Testing
   switchport
   ip nat destination static 1.0.0.1 2.0.0.1
   ip nat destination static 1.0.0.2 22 2.0.0.2
   ip nat destination static 1.0.0.3 22 2.0.0.3 23
   ip nat destination static 1.0.0.4 22 2.0.0.4 23 protocol udp
   ip nat destination static 1.0.0.7 access-list ACL21 2.0.0.7
   ip nat source static 3.0.0.1 4.0.0.1
   ip nat source static 3.0.0.2 22 4.0.0.2
   ip nat source static 3.0.0.3 22 4.0.0.3 23
   ip nat source static 3.0.0.4 22 4.0.0.4 23 protocol udp
   ip nat source static 3.0.0.7 access-list ACL21 4.0.0.7
   ip nat source ingress static 3.0.0.8 4.0.0.8
   ip nat destination egress static 239.0.0.1 239.0.0.2
   ip nat source static 3.0.0.5 22 4.0.0.5 23 protocol tcp group 1
   ip nat destination static 1.0.0.5 22 2.0.0.5 23 protocol tcp group 1
   ip nat source static 3.0.0.6 22 4.0.0.6 23 protocol tcp group 2 comment Comment Test
   ip nat destination static 1.0.0.6 22 2.0.0.6 23 protocol tcp group 2 comment Comment Test
   ip nat destination dynamic access-list ACL1 pool POOL1
   ip nat source dynamic access-list ACL11 pool POOL11
   ip nat source dynamic access-list ACL12 pool POOL11 comment POOL11 shared with ACL11/12
   ip nat source dynamic access-list ACL13 pool POOL13 priority 10
   ip nat source dynamic access-list ACL14 pool POOL14 priority 1 comment Priority low end
   ip nat source dynamic access-list ACL15 pool POOL15 priority 4294967295 comment Priority high end
   ip nat source dynamic access-list ACL16 pool POOL16 comment Priority default
   ip nat source dynamic access-list ACL17 overload priority 10 comment Priority_10
   ip nat source dynamic access-list ACL18 pool POOL18 address-only priority 10 comment Priority_10
   ip nat source dynamic access-list ACL19 pool POOL19 full-cone priority 10 comment Priority_10
   ip nat destination dynamic access-list ACL2 pool POOL1 comment POOL1 shared with ACL1/2
   ip nat destination dynamic access-list ACL3 pool POOL3 priority 10
   ip nat destination dynamic access-list ACL4 pool POOL4 priority 1 comment Priority low end
   ip nat destination dynamic access-list ACL5 pool POOL5 priority 4294967295 comment Priority high end
   ip nat destination dynamic access-list ACL6 pool POOL6 comment Priority default
!
interface Ethernet61
   description interface_in_mode_access_with_voice
   no logging event link-status
   no logging event congestion-drops
   switchport trunk native vlan 100
   switchport phone vlan 70
   switchport phone trunk untagged phone
   switchport mode trunk phone
   switchport
   no logging event storm-control discards
   no logging event spanning-tree
!
interface Ethernet62
   description interface_in_mode_access_with_voice
   no logging event link-status
   no logging event congestion-drops
   switchport trunk native vlan 100
   switchport phone vlan 70
   switchport phone trunk tagged phone
   switchport mode trunk phone
   switchport
   no logging event storm-control discards
   no logging event spanning-tree
!
interface Ethernet63
   description DHCP client interface
   no switchport
   ip address dhcp
   dhcp client accept default-route
!
interface Ethernet64
   description DHCP server interface
   no switchport
   mac timestamp replace-fcs
   ip address 192.168.42.42/24
   dhcp server ipv4
   dhcp server ipv6
!
interface Ethernet65
   description Multiple VRIDs
   no shutdown
   no switchport
   mac timestamp header
   ip address 192.0.2.2/25
   ipv6 enable
   ipv6 address 2001:db8::2/64
   ipv6 address fe80::2/64 link-local
   vrrp 1 priority-level 105
   vrrp 1 advertisement interval 2
   vrrp 1 preempt delay minimum 30 reload 800
   vrrp 1 ipv4 192.0.2.1
   vrrp 2 ipv6 2001:db8::1
!
interface Ethernet66
   description Multiple VRIDs and tracking
   no shutdown
   no switchport
   ip address 192.0.2.2/25
   ipv6 enable
   ipv6 address 2001:db8::2/64
   ipv6 address fe80::2/64 link-local
   vrrp 1 priority-level 105
   vrrp 1 advertisement interval 2
   vrrp 1 preempt delay minimum 30 reload 800
   vrrp 1 ipv4 192.0.2.1
   vrrp 1 tracked-object ID1TrackedObjectDecrement decrement 5
   vrrp 1 tracked-object ID1TrackedObjectShutdown shutdown
   vrrp 2 ipv6 2001:db8::1
   vrrp 2 tracked-object ID2TrackedObjectDecrement decrement 10
   vrrp 2 tracked-object ID2TrackedObjectShutdown shutdown
   no vrrp 3 preempt
   vrrp 3 timers delay reload 900
   vrrp 3 ipv4 100.64.0.1
   vrrp 3 ipv4 version 3
!
interface Ethernet67
   description Custom_Transceiver_Frequency
   no shutdown
   switchport
   mac timestamp before-fcs
   transceiver frequency 190050.000
!
interface Ethernet67.1
   description Test_encapsulation_dot1q
   encapsulation dot1q vlan 4 inner 34
!
interface Ethernet68
   description Custom_Transceiver_Frequency
   no shutdown
   switchport
   transceiver media override 100gbase-ar4
   transceiver frequency 190080.000 ghz
!
interface Ethernet68.1
   description Test_encapsulation_vlan1
   encapsulation vlan
      client dot1q outer 23 inner dot1q 45 network dot1ad outer 32 inner dot1ad 54
!
interface Ethernet68.2
   description Test_encapsulation_vlan2
   encapsulation vlan
      client dot1q 10 network dot1q outer 32 inner 54
!
interface Ethernet68.3
   description Test_encapsulation_vlan3
   encapsulation vlan
      client dot1ad 12 network dot1q 25
!
interface Ethernet68.4
   description Test_encapsulation_vlan4
   encapsulation vlan
      client dot1ad outer 35 inner dot1q 60 network dot1q outer 53 inner dot1ad 6
!
interface Ethernet68.5
   description Test_encapsulation_vlan5
   encapsulation vlan
      client dot1ad outer 35 inner 60 network dot1ad outer 52 inner 62
!
interface Ethernet68.6
   description Test_encapsulation_vlan6
   encapsulation vlan
      client dot1ad outer 35 inner 60 network client
!
interface Ethernet68.7
   description Test_encapsulation_vlan7
   encapsulation vlan
      client untagged network dot1ad outer 35 inner 60
!
interface Ethernet68.8
   description Test_encapsulation_vlan8
   encapsulation vlan
      client untagged network dot1q outer 35 inner 60
!
interface Ethernet68.9
   description Test_encapsulation_vlan9
   encapsulation vlan
      client untagged network untagged
!
interface Ethernet68.10
   description Test_encapsulation_vlan9
   encapsulation vlan
      client dot1q outer 14 inner 11 network client inner
!
interface Ethernet69
   description IP NAT service-profile
   switchport
   ip nat service-profile TEST-NAT-PROFILE
!
interface Ethernet70
   description dot1x_aaa_unresponsive
   no shutdown
   dot1x aaa unresponsive phone action apply cached-results timeout 10 hours else traffic allow
   dot1x aaa unresponsive action traffic allow vlan 10 access-list acl1
   dot1x aaa unresponsive eap response success
   dot1x mac based access-list
!
interface Ethernet71
   description dot1x_aaa_unresponsive1
   no shutdown
   dot1x aaa unresponsive phone action apply cached-results timeout 10 hours
   dot1x aaa unresponsive action traffic allow vlan 10 access-list acl1
   dot1x aaa unresponsive eap response success
   dot1x mac based access-list
!
interface Ethernet72
   description dot1x_aaa_unresponsive2
   no shutdown
   dot1x aaa unresponsive action traffic allow vlan 10 access-list acl1
   dot1x aaa unresponsive eap response success
   dot1x mac based access-list
!
interface Ethernet73
   description DC1-AGG01_Ethernet1
   channel-group 5 mode active
   transceiver media override 100gbase-ar4
!
interface Ethernet74
   description MLAG_PEER_DC1-LEAF1B_Ethernet3
   channel-group 3 mode active
!
interface Ethernet75
   description MLAG_PEER_DC1-LEAF1B_Ethernet4
   channel-group 3 mode active
!
interface Ethernet76
   description SRV-POD03_Eth1
   channel-group 5 mode active
   no lldp transmit
   no lldp receive
!
interface Ethernet77
   description MLAG_PEER_DC1-LEAF1B_Ethernet8
   channel-group 8 mode active
!
interface Ethernet78
   description DC1-AGG03_Ethernet1
   channel-group 15 mode active
   lacp timer fast
   lacp timer multiplier 30
!
interface Ethernet79
   description DC1-AGG04_Ethernet1
   channel-group 16 mode active
   lacp timer normal
!
interface Ethernet80
   description LAG Member
   channel-group 17 mode active
!
interface Ethernet80/1
   description LAG Member
   channel-group 101 mode active
!
interface Ethernet80/2
   description LAG Member
   channel-group 102 mode active
!
interface Ethernet80/3
   description LAG Member
   channel-group 103 mode active
!
interface Ethernet80/4
   description LAG Member LACP fallback
   switchport trunk allowed vlan 100
   switchport mode trunk
   switchport
   channel-group 104 mode active
   spanning-tree portfast
!
interface Ethernet81
   description LAG Member
   channel-group 109 mode active
!
interface Ethernet81/1
   description LAG Member with error_correction
   error-correction encoding fire-code
   error-correction encoding reed-solomon
   channel-group 111 mode active
!
interface Ethernet81/2
   description LAG Member LACP fallback LLDP ZTP VLAN
   switchport trunk allowed vlan 112
   switchport mode trunk
   switchport
   channel-group 112 mode active
   lldp tlv transmit ztp vlan 112
   spanning-tree portfast
!
interface Ethernet81/10
   description isis_port_channel_member
   channel-group 110 mode active
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel3 | MLAG_PEER_DC1-LEAF1B_Po3 | trunk | 2-4094 | - | LEAF_PEER_L3, MLAG | - | - | - | - |
| Port-Channel5 | DC1_L2LEAF1_Po1 | trunk | 110,201 | - | - | - | - | 5 | - |
| Port-Channel10 | SRV01_bond0 | trunk | 2-3000 | - | - | - | - | - | 0000:0000:0404:0404:0303 |
| Port-Channel12 | interface_in_mode_access_with_voice | trunk phone | - | 100 | - | - | - | - | - |
| Port-Channel13 | EVPN-Vxlan single-active redundancy | - | - | - | - | - | - | - | 0000:0000:0000:0102:0304 |
| Port-Channel14 | EVPN-MPLS multihoming | - | - | - | - | - | - | - | 0000:0000:0000:0102:0305 |
| Port-Channel15 | DC1_L2LEAF3_Po1 | trunk | 110,201 | - | - | - | - | 15 | - |
| Port-Channel16 | DC1_L2LEAF4_Po1 | trunk | 110,201 | 10 | - | - | - | 16 | - |
| Port-Channel20 | Po_in_mode_access_accepting_tagged_LACP_frames | access | 200 | - | - | - | - | - | - |
| Port-Channel50 | SRV-POD03_PortChanne1 | trunk | 1-4000 | - | - | - | - | - | 0000:0000:0303:0202:0101 |
| Port-Channel51 | ipv6_prefix | trunk | 1-500 | - | - | - | - | - | - |
| Port-Channel100 | - | dot1q-tunnel | 10-11,200 | tag | g1, g2 | - | - | - | - |
| Port-Channel101 | PVLAN Promiscuous Access - only one secondary | access | 110 | - | - | - | - | - | - |
| Port-Channel102 | PVLAN Promiscuous Trunk - vlan translation out | trunk | 110-112 | - | - | - | - | - | - |
| Port-Channel103 | PVLAN Secondary Trunk | trunk | 110-112 | - | - | - | - | - | - |
| Port-Channel104 | LACP fallback individual | trunk | 112 | - | - | 300 | individual | - | - |
| Port-Channel105 | bpdu disabled | - | - | - | - | - | - | - | - |
| Port-Channel106 | bpdu enabled | - | - | - | - | - | - | - | - |
| Port-Channel107 | bpdu true | - | - | - | - | - | - | - | - |
| Port-Channel108 | bpdu false | - | - | - | - | - | - | - | - |
| Port-Channel109 | Molecule ACLs | access | 110 | - | - | - | - | - | - |
| Port-Channel112 | LACP fallback individual | trunk | 112 | - | - | 5 | individual | - | - |
| Port-Channel115 | native-vlan-tag-precedence | trunk | - | tag | - | - | - | - | - |
| Port-Channel121 | access_port_with_no_vlans | access | - | - | - | - | - | - | - |
| Port-Channel122 | trunk_port_with_no_vlans | trunk | - | - | - | - | - | - | - |
| Port-Channel130 | IP NAT Testing | - | - | - | - | - | - | - | - |
| Port-Channel131 | dot1q-tunnel mode | dot1q-tunnel | 115 | - | - | - | - | - | - |

##### Encapsulation Dot1q

| Interface | Description | Vlan ID | Dot1q VLAN Tag | Dot1q Inner VLAN Tag |
| --------- | ----------- | ------- | -------------- | -------------------- |
| Port-Channel8.101 | to Dev02 Port-Channel8.101 - VRF-C1 | - | 101 | - |
| Port-Channel100.101 | IFL for TENANT01 | - | 101 | - |
| Port-Channel100.102 | IFL for TENANT02 | - | 102 | 110 |

##### Flexible Encapsulation Interfaces

| Interface | Description | Vlan ID | Client Encapsulation | Client Inner Encapsulation | Client VLAN | Client Outer VLAN Tag | Client Inner VLAN Tag | Network Encapsulation | Network Inner Encapsulation | Network VLAN | Network Outer VLAN Tag | Network Inner VLAN Tag |
| --------- | ----------- | ------- | --------------- | --------------------- | ----------- | --------------------- | --------------------- | ---------------- | ---------------------- | ------------ | ---------------------- | ---------------------- |
| Port-Channel111.1 | TENANT_A pseudowire 1 interface | - | unmatched | - | - | - | - | - | - | - | - | - |
| Port-Channel111.100 | TENANT_A pseudowire 2 interface | - | dot1q | - | 100 | - | - | client | - | - | - | - |
| Port-Channel111.200 | TENANT_A pseudowire 3 interface | - | dot1q | - | 200 | - | - | - | - | - | - | - |
| Port-Channel111.300 | TENANT_A pseudowire 4 interface | - | dot1q | - | 300 | - | - | dot1q | - | 400 | - | - |
| Port-Channel111.400 | TENANT_A pseudowire 3 interface | - | dot1q | - | - | 400 | 20 | dot1q | - | - | 401 | 21 |
| Port-Channel111.1000 | L2 Subinterface | 1000 | dot1q | - | 100 | - | - | client | - | - | - | - |
| Port-Channel131.1 | Test_encapsulation_vlan1 | - | dot1q | dot1q | - | 23 | 45 | dot1ad | dot1ad | - | 32 | 54 |
| Port-Channel131.2 | Test_encapsulation_vlan2 | - | dot1q | - | 10 | - | - | dot1q | - | - | 32 | 54 |
| Port-Channel131.3 | Test_encapsulation_vlan3 | - | dot1ad | - | 12 | - | - | dot1q | - | 25 | - | - |
| Port-Channel131.4 | Test_encapsulation_vlan4 | - | dot1ad | dot1q | - | 35 | 60 | dot1q | dot1ad | - | 53 | 6 |
| Port-Channel131.5 | Test_encapsulation_vlan5 | - | dot1ad | - | - | 35 | 60 | dot1ad | - | - | 52 | 62 |
| Port-Channel131.6 | Test_encapsulation_vlan6 | - | dot1ad | - | - | 35 | 60 | client | - | - | - | - |
| Port-Channel131.7 | Test_encapsulation_vlan7 | - | untagged | - | - | - | - | dot1ad | - | - | 35 | 60 |
| Port-Channel131.8 | Test_encapsulation_vlan8 | - | untagged | - | - | - | - | dot1q | - | - | 35 | 60 |
| Port-Channel131.9 | Test_encapsulation_vlan9 | - | untagged | - | - | - | - | untagged | - | - | - | - |
| Port-Channel131.10 | Test_encapsulation_vlan9 | - | dot1q | - | - | 14 | 11 | client inner | - | - | - | - |

##### Private VLAN

| Interface | PVLAN Mapping | Secondary Trunk |
| --------- | ------------- | ----------------|
| Port-Channel15 | - | False |
| Port-Channel100 | 20-30 | True |
| Port-Channel101 | 111 | - |
| Port-Channel103 | - | True |

##### VLAN Translations

| Interface |  Direction | From VLAN ID(s) | To VLAN ID | From Inner VLAN ID | To Inner VLAN ID | Network | Dot1q-tunnel |
| --------- |  --------- | --------------- | ---------- | ------------------ | ---------------- | ------- | ------------ |
| Port-Channel16 | out | 23 | 22 | - | - | - | True |
| Port-Channel100 | both | 12 | 20 | - | - | - | - |
| Port-Channel100 | both | 23 | 42 | 74 | - | False | - |
| Port-Channel100 | both | 24 | 46 | 78 | - | True | - |
| Port-Channel100 | both | 43 | 30 | - | - | - | True |
| Port-Channel100 | in | 23 | 45 | - | - | - | True |
| Port-Channel100 | in | 34 | 23 | - | - | - | - |
| Port-Channel100 | in | 37 | 49 | - | 56 | - | - |
| Port-Channel100 | out | 10 | 45 | - | 34 | - | - |
| Port-Channel100 | out | 34 | 50 | - | - | - | - |
| Port-Channel100 | out | 45 | all | - | - | - | True |
| Port-Channel100 | out | 55 | - | - | - | - | - |
| Port-Channel102 | out | 111-112 | 110 | - | - | - | - |

##### EVPN Multihoming

####### EVPN Multihoming Summary

| Interface | Ethernet Segment Identifier | Multihoming Redundancy Mode | Route Target |
| --------- | --------------------------- | --------------------------- | ------------ |
| Port-Channel10 | 0000:0000:0404:0404:0303 | all-active | 04:04:03:03:02:02 |
| Port-Channel13 | 0000:0000:0000:0102:0304 | single-active | 00:00:01:02:03:04 |
| Port-Channel14 | 0000:0000:0000:0102:0305 | all-active | 00:00:01:02:03:05 |
| Port-Channel50 | 0000:0000:0303:0202:0101 | all-active | 03:03:02:02:01:01 |
| Port-Channel111.1000 | 0000:0000:0303:0202:0101 | all-active | 03:03:02:02:01:01 |

####### Designated Forwarder Election Summary

| Interface | Algorithm | Preference Value | Dont Preempt | Hold time | Subsequent Hold Time | Candidate Reachability Required |
| --------- | --------- | ---------------- | ------------ | --------- | -------------------- | ------------------------------- |
| Port-Channel13 | preference | 100 | True | 10 | - | True |

####### EVPN-MPLS summary

| Interface | Shared Index | Tunnel Flood Filter Time |
| --------- | ------------ | ------------------------ |
| Port-Channel14 | 100 | 100 |

##### Link Tracking Groups

| Interface | Group Name | Direction |
| --------- | ---------- | --------- |
| Port-Channel5 | EVPN_MH_ES1 | downstream |
| Port-Channel5 | EVPN_MH_ES3, EVPN_MH_ES4 | downstream |
| Port-Channel15 | EVPN_MH_ES2 | upstream |

##### IPv4

| Interface | Description | MLAG ID | IP Address | VRF | MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------- | ---------- | --- | --- | -------- | ------ | ------- |
| Port-Channel8.101 | to Dev02 Port-Channel8.101 - VRF-C1 | - | 10.1.2.3/31 | default | - | - | - | - |
| Port-Channel9 | - | - | 10.9.2.3/31 | default | - | - | - | - |
| Port-Channel17 | PBR Description | - | 192.0.2.3/31 | default | - | - | - | - |
| Port-Channel99 | MCAST | - | 192.0.2.10/31 | default | - | - | - | - |
| Port-Channel100.101 | IFL for TENANT01 | - | 10.1.1.3/31 | default | 1500 | - | - | - |
| Port-Channel100.102 | IFL for TENANT02 | - | 10.1.2.3/31 | C2 | 1500 | - | - | - |
| Port-Channel113 | interface_with_mpls_enabled | - | 172.31.128.9/31 | default | - | - | - | - |
| Port-Channel114 | interface_with_mpls_disabled | - | 172.31.128.10/31 | default | - | - | - | - |

##### IP NAT: Source Static

| Interface | Direction | Original IP | Original Port | Access List | Translated IP | Translated Port | Protocol | Group | Priority | Comment |
| --------- | --------- | ----------- | ------------- | ----------- | ------------- | --------------- | -------- | ----- | -------- | ------- |
| Port-Channel130 | - | 3.0.0.1 | - | - | 4.0.0.1 | - | - | - | 0 | - |

##### IP NAT: Source Dynamic

| Interface | Access List | NAT Type | Pool Name | Priority | Comment |
| --------- | ----------- | -------- | --------- | -------- | ------- |
| Port-Channel130 | ACL2 | pool | POOL2 | 0 | - |

##### IP NAT: Destination Static

| Interface | Direction | Original IP | Original Port | Access List | Translated IP | Translated Port | Protocol | Group | Priority | Comment |
| --------- | --------- | ----------- | ------------- | ----------- | ------------- | --------------- | -------- | ----- | -------- | ------- |
| Port-Channel130 | - | 1.0.0.1 | - | - | 2.0.0.1 | - | - | - | 0 | - |

##### IP NAT: Destination Dynamic

| Interface | Access List | Pool Name | Priority | Comment |
| --------- | ----------- | --------- | -------- | ------- |
| Port-Channel130 | ACL1 | POOL1 | 0 | - |

##### ISIS

| Interface | ISIS Instance | ISIS BFD | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | ISIS Authentication Mode |
| --------- | ------------- | -------- | ----------- | ---- | ----------------- | ------------- | ------------------------ |
| Port-Channel3 | EVPN_UNDERLAY | - | - | - | - | - | sha |
| Port-Channel8 | EVPN_UNDERLAY | - | - | - | - | - | Level-1: md5<br>Level-2: md5 |
| Port-Channel9 | - | - | - | - | - | - | Level-2: text |
| Port-Channel10 | EVPN_UNDERLAY | - | - | - | - | - | sha |
| Port-Channel12 | EVPN_UNDERLAY | - | - | - | - | - | Level-1: sha |
| Port-Channel13 | - | - | - | - | - | - | - |
| Port-Channel15 | - | - | - | - | - | - | md5 |
| Port-Channel16 | EVPN_UNDERLAY | - | - | - | - | - | md5 |
| Port-Channel20 | EVPN_UNDERLAY | - | - | - | - | - | Level-1: shared-secret<br>Level-2: shared-secret |
| Port-Channel50 | EVPN_UNDERLAY | - | - | - | - | - | shared-secret |
| Port-Channel51 | EVPN_UNDERLAY | - | - | - | - | - | shared-secret |
| Port-Channel100 | EVPN_UNDERLAY | - | - | - | - | - | Level-1: md5<br>Level-2: text |
| Port-Channel110 | ISIS_TEST | True | 99 | point-to-point | level-2 | True | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel3
   description MLAG_PEER_DC1-LEAF1B_Po3
   switchport trunk allowed vlan 2-4094
   switchport mode trunk
   switchport trunk group LEAF_PEER_L3
   switchport trunk group MLAG
   switchport
   no snmp trap link-change
   shape rate 200000 kbps
   isis enable EVPN_UNDERLAY
   isis authentication mode sha key-id 2 rx-disabled
   isis authentication key 0 <removed>
!
interface Port-Channel5
   description DC1_L2LEAF1_Po1
   bgp session tracker ST2
   switchport trunk allowed vlan 110,201
   switchport mode trunk
   switchport
   ip verify unicast source reachable-via rx
   ip igmp host-proxy
   ip igmp host-proxy 239.0.0.1
   ip igmp host-proxy 239.0.0.2 exclude 10.0.2.1
   ip igmp host-proxy 239.0.0.3 include 10.0.3.1
   ip igmp host-proxy 239.0.0.4 include 10.0.4.3
   ip igmp host-proxy 239.0.0.4 include 10.0.4.4
   ip igmp host-proxy 239.0.0.4 exclude 10.0.4.1
   ip igmp host-proxy 239.0.0.4 exclude 10.0.4.2
   ip igmp host-proxy access-list ACL1
   ip igmp host-proxy access-list ACL2
   ip igmp host-proxy report-interval 2
   ip igmp host-proxy version 2
   l2 mtu 8000
   l2 mru 8000
   mlag 5
   storm-control broadcast level 1
   storm-control multicast level 1
   storm-control unknown-unicast level 1
   link tracking group EVPN_MH_ES1 downstream
   link tracking group EVPN_MH_ES3 downstream
   link tracking group EVPN_MH_ES4 downstream
   comment
   Comment created from eos_cli under port_channel_interfaces.Port-Channel5
   EOF

!
interface Port-Channel8
   description to Dev02 Port-channel 8
   no switchport
   switchport port-security violation protect
   isis enable EVPN_UNDERLAY
   isis authentication mode md5 level-1
   isis authentication mode md5 level-2
   isis authentication key 0 <removed> level-1
   isis authentication key 0 <removed> level-2
!
interface Port-Channel8.101
   description to Dev02 Port-Channel8.101 - VRF-C1
   encapsulation dot1q vlan 101
   ip address 10.1.2.3/31
!
interface Port-Channel9
   no switchport
   ip address 10.9.2.3/31
   bfd interval 500 min-rx 500 multiplier 5
   bfd echo
   bfd neighbor 10.1.2.4
   bfd per-link rfc-7130
   isis authentication mode text rx-disabled level-2
   isis authentication key 0 <removed> level-2
   spanning-tree guard root
!
interface Port-Channel10
   description SRV01_bond0
   switchport trunk allowed vlan 2-3000
   switchport mode trunk
   switchport
   !
   evpn ethernet-segment
      identifier 0000:0000:0404:0404:0303
      route-target import 04:04:03:03:02:02
   shape rate 50 percent
   isis enable EVPN_UNDERLAY
   isis authentication mode sha key-id 2
   isis authentication key 0 <removed>
!
interface Port-Channel12
   description interface_in_mode_access_with_voice
   switchport trunk native vlan 100
   switchport phone vlan 70
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   isis enable EVPN_UNDERLAY
   isis authentication mode sha key-id 5 level-1
!
interface Port-Channel13
   description EVPN-Vxlan single-active redundancy
   switchport
   !
   evpn ethernet-segment
      identifier 0000:0000:0000:0102:0304
      redundancy single-active
      designated-forwarder election algorithm preference 100 dont-preempt
      designated-forwarder election hold-time 10
      designated-forwarder election candidate reachability required
      route-target import 00:00:01:02:03:04
   isis authentication key-id 2 algorithm sha-512 key 0 <removed>
   isis authentication key-id 3 algorithm sha-512 rfc-5310 key 0 <removed>
   isis authentication key-id 1 algorithm sha-1 key 0 <removed> level-1
   isis authentication key-id 4 algorithm sha-1 rfc-5310 key 0 <removed> level-1
   isis authentication key-id 5 algorithm sha-1 key 0 <removed> level-1
   isis authentication key-id 1 algorithm sha-1 key 0 <removed> level-2
   isis authentication key-id 5 algorithm sha-1 rfc-5310 key 0 <removed> level-2
!
interface Port-Channel14
   description EVPN-MPLS multihoming
   switchport
   !
   evpn ethernet-segment
      identifier 0000:0000:0000:0102:0305
      mpls tunnel flood filter time 100
      mpls shared index 100
      route-target import 00:00:01:02:03:05
!
interface Port-Channel15
   description DC1_L2LEAF3_Po1
   switchport trunk allowed vlan 110,201
   switchport mode trunk
   switchport
   mlag 15
   isis authentication mode md5 rx-disabled
   isis authentication key 0 <removed>
   spanning-tree guard loop
   link tracking group EVPN_MH_ES2 upstream
!
interface Port-Channel16
   description DC1_L2LEAF4_Po1
   switchport trunk native vlan 10
   switchport dot1q vlan tag disallowed
   switchport trunk allowed vlan 110,201
   switchport mode trunk
   switchport
   switchport vlan translation out 23 dot1q-tunnel 22
   snmp trap link-change
   mlag 16
   switchport port-security violation protect log
   switchport port-security mac-address maximum 100
   isis enable EVPN_UNDERLAY
   isis authentication mode md5
   isis authentication key 0 <removed>
   spanning-tree guard none
   switchport backup-link Port-Channel100.102 prefer vlan 20
!
interface Port-Channel17
   description PBR Description
   no switchport
   ip address 192.0.2.3/31
   service-policy type pbr input MyPolicy
!
interface Port-Channel20
   description Po_in_mode_access_accepting_tagged_LACP_frames
   switchport access vlan 200
   switchport mode access
   switchport
   l2-protocol encapsulation dot1q vlan 200
   isis enable EVPN_UNDERLAY
   isis authentication mode shared-secret profile profile1 algorithm sha-256 rx-disabled level-1
   isis authentication mode shared-secret profile profile2 algorithm sha-1 rx-disabled level-2
!
interface Port-Channel50
   description SRV-POD03_PortChanne1
   switchport trunk allowed vlan 1-4000
   switchport mode trunk
   switchport
   !
   evpn ethernet-segment
      identifier 0000:0000:0303:0202:0101
      route-target import 03:03:02:02:01:01
   lacp system-id 0303.0202.0101
   isis enable EVPN_UNDERLAY
   isis authentication mode shared-secret profile profile1 algorithm sha-1 rx-disabled
!
interface Port-Channel51
   description ipv6_prefix
   switchport trunk allowed vlan 1-500
   switchport mode trunk
   switchport
   ipv6 nd prefix a1::/64 infinite infinite no-autoconfig
   switchport port-security
   no switchport port-security mac-address maximum disabled
   switchport port-security vlan 1 mac-address maximum 3
   switchport port-security vlan 2 mac-address maximum 3
   switchport port-security vlan 3 mac-address maximum 3
   switchport port-security vlan default mac-address maximum 2
   isis enable EVPN_UNDERLAY
   isis authentication mode shared-secret profile profile1 algorithm sha-1
!
interface Port-Channel99
   description MCAST
   no switchport
   ip address 192.0.2.10/31
   pim ipv4 sparse-mode
   pim ipv4 bidirectional
   pim ipv4 hello interval 15
   pim ipv4 hello count 4.5
   pim ipv4 dr-priority 200
   pim ipv4 bfd
!
interface Port-Channel100
   logging event link-status
   switchport access vlan 200
   switchport trunk native vlan tag
   switchport phone vlan 110
   switchport phone trunk tagged
   switchport vlan translation in required
   switchport dot1q vlan tag required
   switchport trunk allowed vlan 10-11
   switchport mode dot1q-tunnel
   switchport dot1q ethertype 1536
   switchport vlan forwarding accept all
   switchport trunk group g1
   switchport trunk group g2
   no switchport
   switchport source-interface tx multicast
   switchport vlan translation 12 20
   switchport vlan translation 23 inner 74 42
   switchport vlan translation 24 inner 78 network 46
   switchport vlan translation 43 dot1q-tunnel 30
   switchport vlan translation in 34 23
   switchport vlan translation in 37 inner 56 49
   switchport vlan translation in 23 dot1q-tunnel 45
   switchport vlan translation out 34 50
   switchport vlan translation out 10 45 inner 34
   switchport vlan translation out 45 dot1q-tunnel all
   switchport trunk private-vlan secondary
   switchport pvlan mapping 20-30
   switchport port-security
   switchport port-security mac-address maximum disabled
   isis enable EVPN_UNDERLAY
   isis authentication mode md5 rx-disabled level-1
   isis authentication mode text rx-disabled level-2
   isis authentication key 0 <removed> level-1
   isis authentication key 0 <removed> level-2
   switchport backup-link Port-channel51
   switchport backup preemption-delay 35
   switchport backup mac-move-burst 20
   switchport backup mac-move-burst-interval 30
   switchport backup initial-mac-move-delay 10
   switchport backup dest-macaddr 01:00:00:00:00:00
!
interface Port-Channel100.101
   description IFL for TENANT01
   mtu 1500
   logging event link-status
   encapsulation dot1q vlan 101
   ip address 10.1.1.3/31
!
interface Port-Channel100.102
   description IFL for TENANT02
   mtu 1500
   no logging event link-status
   encapsulation dot1q vlan 102 inner 110
   vrf C2
   ip address 10.1.2.3/31
   logging event storm-control discards
!
interface Port-Channel101
   description PVLAN Promiscuous Access - only one secondary
   switchport access vlan 110
   switchport mode access
   switchport
   switchport pvlan mapping 111
   no qos trust
!
interface Port-Channel102
   description PVLAN Promiscuous Trunk - vlan translation out
   switchport vlan translation out required
   switchport trunk allowed vlan 110-112
   switchport mode trunk
   switchport
   switchport vlan translation out 111-112 110
!
interface Port-Channel103
   description PVLAN Secondary Trunk
   switchport trunk allowed vlan 110-112
   switchport mode trunk
   switchport
   switchport trunk private-vlan secondary
!
interface Port-Channel104
   description LACP fallback individual
   switchport trunk allowed vlan 112
   switchport mode trunk
   switchport
   port-channel lacp fallback individual
   port-channel lacp fallback timeout 300
!
interface Port-Channel105
   description bpdu disabled
   switchport
   spanning-tree bpduguard disable
   spanning-tree bpdufilter disable
!
interface Port-Channel106
   description bpdu enabled
   switchport
   spanning-tree bpduguard enable
   spanning-tree bpdufilter enable
!
interface Port-Channel107
   description bpdu true
   switchport
   spanning-tree bpduguard enable
   spanning-tree bpdufilter enable
!
interface Port-Channel108
   description bpdu false
   switchport
!
interface Port-Channel109
   description Molecule ACLs
   switchport access vlan 110
   switchport mode access
   switchport
   ip access-group IPV4_ACL_IN in
   ip access-group IPV4_ACL_OUT out
   ipv6 access-group IPV6_ACL_IN in
   ipv6 access-group IPV6_ACL_OUT out
   mac access-group MAC_ACL_IN in
   mac access-group MAC_ACL_OUT out
!
interface Port-Channel110
   description isis_interface_knobs
   no switchport
   isis enable ISIS_TEST
   isis bfd
   isis circuit-type level-2
   isis metric 99
   isis hello padding
   isis network point-to-point
!
interface Port-Channel111
   description Flexencap Port-Channel
   no switchport
!
interface Port-Channel111.1
   description TENANT_A pseudowire 1 interface
   !
   encapsulation vlan
      client unmatched
!
interface Port-Channel111.100
   description TENANT_A pseudowire 2 interface
   !
   encapsulation vlan
      client dot1q 100 network client
!
interface Port-Channel111.200
   description TENANT_A pseudowire 3 interface
   !
   encapsulation vlan
      client dot1q 200
!
interface Port-Channel111.300
   description TENANT_A pseudowire 4 interface
   !
   encapsulation vlan
      client dot1q 300 network dot1q 400
!
interface Port-Channel111.400
   description TENANT_A pseudowire 3 interface
   !
   encapsulation vlan
      client dot1q outer 400 inner 20 network dot1q outer 401 inner 21
!
interface Port-Channel111.1000
   description L2 Subinterface
   vlan id 1000
   !
   encapsulation vlan
      client dot1q 100 network client
   !
   evpn ethernet-segment
      identifier 0000:0000:0303:0202:0101
      route-target import 03:03:02:02:01:01
   lacp system-id 0303.0202.0101
!
interface Port-Channel112
   description LACP fallback individual
   switchport trunk allowed vlan 112
   switchport mode trunk
   switchport
   port-channel lacp fallback individual
   port-channel lacp fallback timeout 5
!
interface Port-Channel113
   description interface_with_mpls_enabled
   no switchport
   ip address 172.31.128.9/31
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
!
interface Port-Channel114
   description interface_with_mpls_disabled
   no switchport
   ip address 172.31.128.10/31
   no mpls ldp interface
   no mpls ip
!
interface Port-Channel115
   description native-vlan-tag-precedence
   switchport trunk native vlan tag
   switchport mode trunk
   switchport
!
interface Port-Channel117
   description interface_with_sflow_ingress_egress_enabled
   no switchport
   sflow enable
   sflow egress enable
!
interface Port-Channel118
   description interface_with_sflow_ingress_egress_unmodified_enabled
   no switchport
   sflow enable
   sflow egress unmodified enable
!
interface Port-Channel119
   description interface_with_sflow_ingress_egress_disabled
   no switchport
   no sflow enable
   no sflow egress enable
!
interface Port-Channel120
   description interface_with_sflow_ingress_egress_unmodified_disabled
   no switchport
   no sflow enable
   no sflow egress unmodified enable
!
interface Port-Channel121
   description access_port_with_no_vlans
   switchport mode access
   switchport
!
interface Port-Channel122
   description trunk_port_with_no_vlans
   switchport mode trunk
   switchport
!
interface Port-Channel130
   description IP NAT Testing
   switchport
   ip nat destination static 1.0.0.1 2.0.0.1
   ip nat source static 3.0.0.1 4.0.0.1
   ip nat destination dynamic access-list ACL1 pool POOL1
   ip nat source dynamic access-list ACL2 pool POOL2
!
interface Port-Channel131
   description dot1q-tunnel mode
   switchport access vlan 115
   switchport mode dot1q-tunnel
   switchport
!
interface Port-Channel131.1
   description Test_encapsulation_vlan1
   !
   encapsulation vlan
      client dot1q outer 23 inner dot1q 45 network dot1ad outer 32 inner dot1ad 54
!
interface Port-Channel131.2
   description Test_encapsulation_vlan2
   !
   encapsulation vlan
      client dot1q 10 network dot1q outer 32 inner 54
!
interface Port-Channel131.3
   description Test_encapsulation_vlan3
   !
   encapsulation vlan
      client dot1ad 12 network dot1q 25
!
interface Port-Channel131.4
   description Test_encapsulation_vlan4
   !
   encapsulation vlan
      client dot1ad outer 35 inner dot1q 60 network dot1q outer 53 inner dot1ad 6
!
interface Port-Channel131.5
   description Test_encapsulation_vlan5
   !
   encapsulation vlan
      client dot1ad outer 35 inner 60 network dot1ad outer 52 inner 62
!
interface Port-Channel131.6
   description Test_encapsulation_vlan6
   !
   encapsulation vlan
      client dot1ad outer 35 inner 60 network client
!
interface Port-Channel131.7
   description Test_encapsulation_vlan7
   !
   encapsulation vlan
      client untagged network dot1ad outer 35 inner 60
!
interface Port-Channel131.8
   description Test_encapsulation_vlan8
   !
   encapsulation vlan
      client untagged network dot1q outer 35 inner 60
!
interface Port-Channel131.9
   description Test_encapsulation_vlan9
   !
   encapsulation vlan
      client untagged network untagged
!
interface Port-Channel131.10
   description Test_encapsulation_vlan9
   !
   encapsulation vlan
      client dot1q outer 14 inner 11 network client inner
!
interface Port-Channel132
   profile test-interface-profile
   description Test_port-channel_interface-profile
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 192.168.255.3/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 192.168.254.3/32 |
| Loopback99 | TENANT_A_PROJECT02_VTEP_DIAGNOSTICS | TENANT_A_PROJECT02 | 10.1.255.3/32 <br> 192.168.1.1/32 secondary <br> 10.0.0.254/32 secondary |
| Loopback100 | TENANT_A_PROJECT02_VTEP_DIAGNOSTICS | TENANT_A_PROJECT02 | 10.1.255.3/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | - |
| Loopback99 | TENANT_A_PROJECT02_VTEP_DIAGNOSTICS | TENANT_A_PROJECT02 | 2002::CAFE/64 |
| Loopback100 | TENANT_A_PROJECT02_VTEP_DIAGNOSTICS | TENANT_A_PROJECT02 | - |

##### ISIS

| Interface | ISIS instance | ISIS metric | Interface mode |
| --------- | ------------- | ----------- | -------------- |
| Loopback99 | ISIS_TEST | 100 | point-to-point |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   ip address 192.168.255.3/32
   comment
   Comment created from eos_cli under loopback_interfaces.Loopback0
   EOF

!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   ip address 192.168.254.3/32
!
interface Loopback99
   description TENANT_A_PROJECT02_VTEP_DIAGNOSTICS
   no shutdown
   vrf TENANT_A_PROJECT02
   ip proxy-arp
   ip address 10.1.255.3/32
   ip address 10.0.0.254/32 secondary
   ip address 192.168.1.1/32 secondary
   ipv6 enable
   ipv6 address 2002::CAFE/64
   mpls ldp interface
   isis enable ISIS_TEST
   isis bfd
   isis metric 100
   isis passive
   isis network point-to-point
!
interface Loopback100
   description TENANT_A_PROJECT02_VTEP_DIAGNOSTICS
   vrf TENANT_A_PROJECT02
   ip address 10.1.255.3/32
```

### Tunnel Interfaces

#### Tunnel Interfaces Summary

| Interface | Description | VRF | Underlay VRF | MTU | Shutdown | NAT Profile | Mode | Source Interface | Destination | PMTU-Discovery | IPsec Profile |
| --------- | ----------- | --- | ------------ | --- | -------- | ----------- | ---- | ---------------- | ----------- | -------------- | ------------- |
| Tunnel1 | test ipv4 only | Tunnel-VRF | Underlay-VRF | 1500 | False | - | ipsec | Ethernet42 | 6.6.6.6 | True | - |
| Tunnel2 | test ipv6 only | default | default | - | True | NAT-PROFILE-NO-VRF-2 | gre | Ethernet42 | dead:beef::1 | False | Profile-2 |
| Tunnel3 | test dual stack | default | default | 1500 | - | - | ipsec | Ethernet42 | 1.1.1.1 | - | Profile-3 |
| Tunnel4 | test no tcp_mss | default | default | 1500 | - | NAT-PROFILE-NO-VRF-1 | - | Ethernet42 | 1.1.1.1 | - | - |

##### IPv4

| Interface | VRF | IP Address | TCP MSS | TCP MSS Direction | ACL In | ACL Out |
| --------- | --- | ---------- | ------- | ----------------- | ------ | ------- |
| Tunnel1 | Tunnel-VRF | 42.42.42.42/24 | 666 | ingress | test-in | test-out |
| Tunnel3 | default | 64.64.64.64/24 | 666 | - | - | - |
| Tunnel4 | default | 64.64.64.64/24 | - | - | - | - |

##### IPv6

| Interface | VRF | IPv6 Address | TCP MSS | TCP MSS Direction | IPv6 ACL In | IPv6 ACL Out |
| --------- | --- | ------------ | ------- | ----------------- | ----------- | ------------ |
| Tunnel2 | default | cafe::1/64 | 666 | egress | test-in | test-out |
| Tunnel3 | default | beef::64/64 | 666 | - | - | - |
| Tunnel4 | default | beef::64/64 | - | - | - | - |

#### Tunnel Interfaces Device Configuration

```eos
!
interface Tunnel1
   description test ipv4 only
   no shutdown
   mtu 1500
   vrf Tunnel-VRF
   ip address 42.42.42.42/24
   tcp mss ceiling ipv4 666 ingress
   ip access-group test-in in
   ip access-group test-out out
   tunnel mode ipsec
   tunnel source interface Ethernet42
   tunnel destination 6.6.6.6
   tunnel path-mtu-discovery
   tunnel underlay vrf Underlay-VRF
   comment
   Comment created from eos_cli under tunnel_interfaces.Tunnel1
   EOF

!
interface Tunnel2
   description test ipv6 only
   shutdown
   ipv6 enable
   ipv6 address cafe::1/64
   tcp mss ceiling ipv6 666 egress
   ipv6 access-group test-in in
   ipv6 access-group test-out out
   ip nat service-profile NAT-PROFILE-NO-VRF-2
   tunnel mode gre
   tunnel source interface Ethernet42
   tunnel destination dead:beef::1
   tunnel ipsec profile Profile-2
!
interface Tunnel3
   description test dual stack
   mtu 1500
   ip address 64.64.64.64/24
   ipv6 enable
   ipv6 address beef::64/64
   tcp mss ceiling ipv4 666 ipv6 666
   tunnel mode ipsec
   tunnel source interface Ethernet42
   tunnel destination 1.1.1.1
   tunnel ipsec profile Profile-3
!
interface Tunnel4
   description test no tcp_mss
   mtu 1500
   ip address 64.64.64.64/24
   ipv6 enable
   ipv6 address beef::64/64
   ip nat service-profile NAT-PROFILE-NO-VRF-1
   tunnel source interface Ethernet42
   tunnel destination 1.1.1.1
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan24 | SVI Description | default | - | False |
| Vlan25 | SVI Description | default | - | False |
| Vlan41 | SVI Description | default | - | False |
| Vlan42 | SVI Description | default | - | False |
| Vlan43 | SVI Description | default | - | False |
| Vlan44 | SVI Description | default | - | False |
| Vlan50 | IP NAT Testing | default | - | - |
| Vlan75 | SVI Description | default | - | False |
| Vlan81 | IPv6 Virtual Address | Tenant_C | - | - |
| Vlan83 | SVI Description | default | - | False |
| Vlan84 | SVI Description | default | - | - |
| Vlan85 | SVI Description | default | - | - |
| Vlan86 | SVI Description | default | - | - |
| Vlan87 | SVI Description | default | - | True |
| Vlan88 | SVI Description | default | - | True |
| Vlan89 | SVI Description | default | - | False |
| Vlan90 | SVI Description | default | - | - |
| Vlan91 | PBR Description | default | - | True |
| Vlan92 | SVI Description | default | - | - |
| Vlan110 | PVLAN Primary with vlan mapping | Tenant_A | - | False |
| Vlan333 | Multiple VRIDs and tracking | default | - | False |
| Vlan334 | v6 attached host exports | default | - | - |
| Vlan335 | v6 attached host exports | default | - | - |
| Vlan336 | v6 attached host exports | default | - | - |
| Vlan337 | v4 dhcp relay all-subnets | default | - | - |
| Vlan338 | v6 dhcp relay all-subnets | default | - | - |
| Vlan339 | v6 nd options | default | - | - |
| Vlan501 | SVI Description | default | - | False |
| Vlan667 | Multiple VRIDs | default | - | False |
| Vlan1001 | SVI Description | Tenant_A | - | False |
| Vlan1002 | SVI Description | Tenant_A | - | False |
| Vlan2001 | SVI Description | Tenant_B | - | - |
| Vlan2002 | SVI Description | Tenant_B | - | - |
| Vlan4094 | SVI Description | default | 9214 | - |

##### Private VLAN

| Interface | PVLAN Mapping |
| --------- | ------------- |
| Vlan110 | 111-112 |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| Vlan24 |  default  |  -  |  10.10.24.1/24  |  -  |  -  |  -  |
| Vlan25 |  default  |  -  |  -  |  -  |  -  |  -  |
| Vlan41 |  default  |  -  |  10.10.41.1/24  |  -  |  -  |  -  |
| Vlan42 |  default  |  -  |  10.10.42.1/24  |  -  |  -  |  -  |
| Vlan43 |  default  |  -  |  -  |  -  |  -  |  -  |
| Vlan44 |  default  |  -  |  -  |  -  |  -  |  -  |
| Vlan50 |  default  |  -  |  -  |  -  |  -  |  -  |
| Vlan75 |  default  |  -  |  10.10.75.1/24  |  -  |  -  |  -  |
| Vlan81 |  Tenant_C  |  -  |  10.10.81.1/24  |  -  |  -  |  -  |
| Vlan83 |  default  |  -  |  10.10.83.1/24  |  -  |  -  |  -  |
| Vlan84 |  default  |  10.10.84.1/24  |  -  |  10.10.84.254, 10.11.84.254/24  |  -  |  -  |
| Vlan85 |  default  |  10.10.84.1/24  |  -  |  -  |  -  |  -  |
| Vlan86 |  default  |  10.10.83.1/24  |  -  |  -  |  -  |  -  |
| Vlan87 |  default  |  10.10.87.1/24  |  -  |  -  |  ACL_IN  |  ACL_OUT  |
| Vlan88 |  default  |  -  |  10.10.87.1/23  |  -  |  -  |  -  |
| Vlan89 |  default  |  -  |  10.10.144.3/20  |  -  |  -  |  -  |
| Vlan90 |  default  |  10.10.83.1/24  |  -  |  -  |  -  |  -  |
| Vlan91 |  default  |  -  |  -  |  -  |  -  |  -  |
| Vlan92 |  default  |  10.10.92.1/24  |  -  |  -  |  -  |  -  |
| Vlan110 |  Tenant_A  |  10.0.101.1/24  |  -  |  -  |  -  |  -  |
| Vlan333 |  default  |  192.0.2.2/25  |  -  |  -  |  -  |  -  |
| Vlan334 |  default  |  -  |  -  |  -  |  -  |  -  |
| Vlan335 |  default  |  -  |  -  |  -  |  -  |  -  |
| Vlan336 |  default  |  -  |  -  |  -  |  -  |  -  |
| Vlan337 |  default  |  10.0.2.2/25  |  -  |  -  |  -  |  -  |
| Vlan338 |  default  |  -  |  -  |  -  |  -  |  -  |
| Vlan339 |  default  |  -  |  -  |  -  |  -  |  -  |
| Vlan501 |  default  |  10.50.26.29/27  |  -  |  -  |  -  |  -  |
| Vlan667 |  default  |  192.0.2.2/25  |  -  |  -  |  -  |  -  |
| Vlan1001 |  Tenant_A  |  -  |  10.1.1.1/24  |  -  |  -  |  -  |
| Vlan1002 |  Tenant_A  |  -  |  10.1.2.1/24  |  -  |  -  |  -  |
| Vlan2001 |  Tenant_B  |  -  |  10.2.1.1/24  |  -  |  -  |  -  |
| Vlan2002 |  Tenant_B  |  -  |  10.2.2.1/24  |  -  |  -  |  -  |
| Vlan4094 |  default  |  169.254.252.0/31  |  -  |  -  |  -  |  -  |

##### IP NAT: Source Static

| Interface | Direction | Original IP | Original Port | Access List | Translated IP | Translated Port | Protocol | Group | Priority | Comment |
| --------- | --------- | ----------- | ------------- | ----------- | ------------- | --------------- | -------- | ----- | -------- | ------- |
| Vlan50 | - | 3.0.0.1 | - | - | 4.0.0.1 | - | - | - | 0 | - |

##### IP NAT: Source Dynamic

| Interface | Access List | NAT Type | Pool Name | Priority | Comment |
| --------- | ----------- | -------- | --------- | -------- | ------- |
| Vlan50 | ACL2 | pool | POOL2 | 0 | - |

##### IP NAT: Destination Static

| Interface | Direction | Original IP | Original Port | Access List | Translated IP | Translated Port | Protocol | Group | Priority | Comment |
| --------- | --------- | ----------- | ------------- | ----------- | ------------- | --------------- | -------- | ----- | -------- | ------- |
| Vlan50 | - | 1.0.0.1 | - | - | 2.0.0.1 | - | - | - | 0 | - |

##### IP NAT: Destination Dynamic

| Interface | Access List | Pool Name | Priority | Comment |
| --------- | ----------- | --------- | -------- | ------- |
| Vlan50 | ACL1 | POOL1 | 0 | - |

##### IPv6

| Interface | VRF | IPv6 Address | IPv6 Virtual Addresses | Virtual Router Addresses | ND RA Disabled | Managed Config Flag | Other Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | --- | ------------ | ---------------------- | ------------------------ | -------------- | ------------------- | ----------------- | ----------- | ------------ |
| Vlan24 | default | 1b11:3a00:22b0:6::15/64 | - | 1b11:3a00:22b0:6::1 | - | True | - | - | - |
| Vlan25 | default | 1b11:3a00:22b0:16::16/64 | - | 1b11:3a00:22b0:16::15, 1b11:3a00:22b0:16::14 | - | - | - | - | - |
| Vlan43 | default | a0::1/64 | - | - | - | - | - | - | - |
| Vlan44 | default | a0::4/64 | - | - | - | - | - | - | - |
| Vlan75 | default | 1b11:3a00:22b0:1000::15/64 | - | 1b11:3a00:22b0:1000::1 | - | True | - | - | - |
| Vlan81 | Tenant_C | - | fc00:10:10:81::1/64, fc00:10:11:81::1/64, fc00:10:12:81::1/64 | - | - | - | - | - | - |
| Vlan89 | default | 1b11:3a00:22b0:5200::15/64 | - | 1b11:3a00:22b0:5200::3 | - | True | - | - | - |
| Vlan333 | default | 2001:db8:333::2/64 | - | - | - | - | - | - | - |
| Vlan334 | default | 2001:db8:334::1/64 | - | - | - | - | - | - | - |
| Vlan335 | default | 2001:db8:335::1/64 | - | - | - | - | - | - | - |
| Vlan336 | default | 2001:db8:336::1/64 | - | - | - | - | - | - | - |
| Vlan338 | default | 2001:db8:338::1/64 | - | - | - | - | - | - | - |
| Vlan339 | default | 2001:db8:339::1/64 | - | - | - | - | True | - | - |
| Vlan501 | default | 1b11:3a00:22b0:0088::207/127 | - | - | True | - | - | - | - |
| Vlan667 | default | 2001:db8:667::2/64 | - | - | - | - | - | - | - |
| Vlan1001 | Tenant_A | a1::1/64 | - | - | - | True | - | - | - |
| Vlan1002 | Tenant_A | a2::1/64 | - | - | True | True | - | - | - |

##### VRRP Details

| Interface | VRRP-ID | Priority | Advertisement Interval | Preempt | Tracked Object Name(s) | Tracked Object Action(s) | IPv4 Virtual IP | IPv4 VRRP Version | IPv6 Virtual IP |
| --------- | ------- | -------- | ---------------------- | --------| ---------------------- | ------------------------ | --------------- | ----------------- | --------------- |
| Vlan333 | 1 | 105 | 2 | Enabled | ID1TrackedObjectDecrement, ID1TrackedObjectShutdown | Decrement 5, Shutdown | 192.0.2.1 | 2 | - |
| Vlan333 | 2 | - | - | Enabled | ID2TrackedObjectDecrement, ID2TrackedObjectShutdown | Decrement 10, Shutdown | - | 2 | 2001:db8:333::1 |
| Vlan333 | 3 | - | - | Disabled | - | - | 100.64.0.1 | 3 | - |
| Vlan667 | 1 | 105 | 2 | Enabled | - | - | 192.0.2.1 | 2 | - |
| Vlan667 | 2 | - | - | Enabled | - | - | - | 2 | 2001:db8:667::1 |

##### ISIS

| Interface | ISIS Instance | ISIS BFD | ISIS Metric | Mode | ISIS Authentication Mode |
| --------- | ------------- | -------- | ----------- | ---- | ------------------------ |
| Vlan42 | EVPN_UNDERLAY | - | - | - | Level-1: sha |
| Vlan83 | EVPN_UNDERLAY | - | - | - | md5 |
| Vlan84 | EVPN_UNDERLAY | - | - | - | sha |
| Vlan85 | EVPN_UNDERLAY | - | - | - | sha |
| Vlan86 | EVPN_UNDERLAY | - | - | - | shared-secret |
| Vlan87 | EVPN_UNDERLAY | - | - | - | shared-secret |
| Vlan88 | EVPN_UNDERLAY | - | - | - | Level-1: md5<br>Level-2: text |
| Vlan90 | EVPN_UNDERLAY | - | - | - | Level-1: shared-secret<br>Level-2: shared-secret |
| Vlan91 | EVPN_UNDERLAY | - | - | - | Level-1: md5<br>Level-2: text |
| Vlan92 | EVPN_UNDERLAY | - | - | - | Level-1: shared-secret<br>Level-2: shared-secret |
| Vlan2002 | EVPN_UNDERLAY | True | - | - | md5 |
| Vlan4094 | EVPN_UNDERLAY | - | - | - | Level-1: sha<br>Level-2: sha |

##### Multicast Routing

| Interface | IP Version | Static Routes Allowed | Multicast Boundaries | Export Host Routes For Multicast Sources |
| --------- | ---------- | --------------------- | -------------------- | ---------------------------------------- |
| Vlan75 | IPv4 | True | 224.0.1.0/24, 224.0.2.0/24 | - |
| Vlan75 | IPv6 | - | ff00::/16, ff01::/16 | - |
| Vlan89 | IPv4 | - | ACL_MULTICAST | True |
| Vlan89 | IPv6 | True | ACL_V6_MULTICAST_WITH_OUT | - |
| Vlan110 | IPv4 | True | ACL_MULTICAST | - |
| Vlan110 | IPv6 | - | - | True |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan24
   description SVI Description
   no shutdown
   ipv6 address 1b11:3a00:22b0:6::15/64
   ipv6 nd managed-config-flag
   ipv6 nd prefix 1b11:3a00:22b0:6::/64 infinite infinite no-autoconfig
   ip address virtual 10.10.24.1/24
   ipv6 virtual-router address 1b11:3a00:22b0:6::1
!
interface Vlan25
   description SVI Description
   no shutdown
   ipv6 address 1b11:3a00:22b0:16::16/64
   ipv6 virtual-router address 1b11:3a00:22b0:16::14
   ipv6 virtual-router address 1b11:3a00:22b0:16::15
!
interface Vlan41
   description SVI Description
   no shutdown
   ip helper-address 10.10.64.150 source-interface Loopback0
   ip helper-address 10.10.96.150 source-interface Loopback0
   ip helper-address 10.10.96.151 source-interface Loopback0
   ip igmp host-proxy
   ip igmp host-proxy 239.0.0.1
   ip igmp host-proxy 239.0.0.2 exclude 10.0.2.1
   ip igmp host-proxy 239.0.0.3 include 10.0.3.1
   ip igmp host-proxy 239.0.0.4 include 10.0.4.3
   ip igmp host-proxy 239.0.0.4 include 10.0.4.4
   ip igmp host-proxy 239.0.0.4 exclude 10.0.4.1
   ip igmp host-proxy 239.0.0.4 exclude 10.0.4.2
   ip igmp host-proxy access-list ACL1
   ip igmp host-proxy access-list ACL2
   ip igmp host-proxy report-interval 2
   ip igmp host-proxy version 2
   ip address virtual 10.10.41.1/24
!
interface Vlan42
   description SVI Description
   no shutdown
   ip helper-address 10.10.64.150 source-interface Loopback0
   ip helper-address 10.10.96.150 source-interface Loopback0
   ip helper-address 10.10.96.151 source-interface Loopback0
   isis enable EVPN_UNDERLAY
   isis authentication mode sha key-id 5 level-1
   ip address virtual 10.10.42.1/24
!
interface Vlan43
   description SVI Description
   no shutdown
   ipv6 dhcp relay destination a0::2 vrf TEST local-interface Loopback44 link-address a0::4
   ipv6 address a0::1/64
   isis authentication key-id 2 algorithm sha-512 key 0 password
   isis authentication key-id 3 algorithm sha-512 rfc-5310 key 0 password1
   isis authentication key-id 1 algorithm sha-1 key 0 password level-1
   isis authentication key-id 4 algorithm sha-1 rfc-5310 key 0 password level-1
   isis authentication key-id 5 algorithm sha-1 key 0 password3 level-1
   isis authentication key-id 1 algorithm sha-1 key 0 password level-2
   isis authentication key-id 5 algorithm sha-1 rfc-5310 key 0 password level-2
!
interface Vlan44
   description SVI Description
   no shutdown
   ipv6 dhcp relay destination a0::8
   ipv6 dhcp relay destination a0::5 vrf TEST source-address a0::6 link-address a0::7
   ipv6 address a0::4/64
!
interface Vlan50
   description IP NAT Testing
   ip nat destination static 1.0.0.1 2.0.0.1
   ip nat source static 3.0.0.1 4.0.0.1
   ip nat destination dynamic access-list ACL1 pool POOL1
   ip nat source dynamic access-list ACL2 pool POOL2
   isis authentication mode text rx-disabled level-2
   isis authentication key 0 password level-2
!
interface Vlan75
   description SVI Description
   no shutdown
   ipv6 address 1b11:3a00:22b0:1000::15/64
   ipv6 nd managed-config-flag
   ipv6 nd prefix 1b11:3a00:22b0:1000::/64 infinite infinite no-autoconfig
   multicast ipv4 boundary 224.0.1.0/24 out
   multicast ipv4 boundary 224.0.2.0/24
   multicast ipv6 boundary ff00::/16 out
   multicast ipv6 boundary ff01::/16 out
   multicast ipv4 static
   ip address virtual 10.10.75.1/24
   ipv6 virtual-router address 1b11:3a00:22b0:1000::1
!
interface Vlan81
   description IPv6 Virtual Address
   vrf Tenant_C
   ipv6 enable
   ip address virtual 10.10.81.1/24
   ipv6 address virtual fc00:10:10:81::1/64
   ipv6 address virtual fc00:10:11:81::1/64
   ipv6 address virtual fc00:10:12:81::1/64
!
interface Vlan83
   description SVI Description
   no shutdown
   isis enable EVPN_UNDERLAY
   isis authentication mode md5
   isis authentication key 0 password
   ip address virtual 10.10.83.1/24
   ip address virtual 10.11.83.1/24 secondary
   ip address virtual 10.11.84.1/24 secondary
!
interface Vlan84
   description SVI Description
   arp gratuitous accept
   ip address 10.10.84.1/24
   arp monitor mac-address
   isis enable EVPN_UNDERLAY
   isis authentication mode sha key-id 2 rx-disabled
   isis authentication key 0 password
   ip virtual-router address 10.10.84.254
   ip virtual-router address 10.11.84.254/24
!
interface Vlan85
   description SVI Description
   ip address 10.10.84.1/24
   arp cache dynamic capacity 50000
   bfd interval 500 min-rx 500 multiplier 5
   bfd echo
   isis enable EVPN_UNDERLAY
   isis authentication mode sha key-id 2
   isis authentication key 0 password
!
interface Vlan86
   description SVI Description
   ip address 10.10.83.1/24
   ip attached-host route export 10
   isis enable EVPN_UNDERLAY
   isis authentication mode shared-secret profile profile1 algorithm sha-1 rx-disabled
!
interface Vlan87
   description SVI Description
   shutdown
   ip address 10.10.87.1/24
   ip access-group ACL_IN in
   ip access-group ACL_OUT out
   isis enable EVPN_UNDERLAY
   isis authentication mode shared-secret profile profile1 algorithm sha-1
!
interface Vlan88
   description SVI Description
   shutdown
   isis enable EVPN_UNDERLAY
   isis authentication mode md5 rx-disabled level-1
   isis authentication mode text rx-disabled level-2
   isis authentication key 0 password level-1
   isis authentication key 0 password level-2
   ip address virtual 10.10.87.1/23
!
interface Vlan89
   description SVI Description
   no shutdown
   ip helper-address 10.10.64.150 source-interface Loopback0
   ip helper-address 10.10.96.101 source-interface Loopback0
   ip helper-address 10.10.96.150 source-interface Loopback0
   ip helper-address 10.10.96.151 source-interface Loopback0
   ip igmp
   ip igmp version 2
   ipv6 address 1b11:3a00:22b0:5200::15/64
   ipv6 nd managed-config-flag
   ipv6 nd prefix 1b11:3a00:22b0:5200::/64 infinite infinite no-autoconfig
   multicast ipv4 boundary ACL_MULTICAST
   multicast ipv6 boundary ACL_V6_MULTICAST_WITH_OUT out
   multicast ipv4 source route export
   multicast ipv6 static
   pim ipv4 sparse-mode
   pim ipv4 local-interface Loopback0
   ip address virtual 10.10.144.3/20
   ipv6 virtual-router address 1b11:3a00:22b0:5200::3
!
interface Vlan90
   description SVI Description
   ip address 10.10.83.1/24
   ip attached-host route export
   isis enable EVPN_UNDERLAY
   isis authentication mode shared-secret profile profile2 algorithm sha-1 level-1
   isis authentication mode shared-secret profile profile1 algorithm sha-256 level-2
!
interface Vlan91
   description PBR Description
   shutdown
   service-policy type pbr input MyServicePolicy
   isis enable EVPN_UNDERLAY
   isis authentication mode md5 level-1
   isis authentication mode text level-2
   isis authentication key 0 password level-1
   isis authentication key 0 password level-2
!
interface Vlan92
   description SVI Description
   ip proxy-arp
   ip address 10.10.92.1/24
   ip directed-broadcast
   isis enable EVPN_UNDERLAY
   isis authentication mode shared-secret profile profile2 algorithm sha-1 rx-disabled level-1
   isis authentication mode shared-secret profile profile1 algorithm sha-256 rx-disabled level-2
!
interface Vlan110
   description PVLAN Primary with vlan mapping
   no shutdown
   pvlan mapping 111-112
   vrf Tenant_A
   ip address 10.0.101.1/24
   multicast ipv4 boundary ACL_MULTICAST out
   multicast ipv6 source route export 20
   multicast ipv4 static
!
interface Vlan333
   description Multiple VRIDs and tracking
   no shutdown
   ip address 192.0.2.2/25
   arp aging timeout 180
   ipv6 enable
   ipv6 address 2001:db8:333::2/64
   ipv6 address fe80::2/64 link-local
   vrrp 1 priority-level 105
   vrrp 1 advertisement interval 2
   vrrp 1 preempt delay minimum 30 reload 800
   vrrp 1 ipv4 192.0.2.1
   vrrp 1 tracked-object ID1TrackedObjectDecrement decrement 5
   vrrp 1 tracked-object ID1TrackedObjectShutdown shutdown
   vrrp 2 ipv6 2001:db8:333::1
   vrrp 2 tracked-object ID2TrackedObjectDecrement decrement 10
   vrrp 2 tracked-object ID2TrackedObjectShutdown shutdown
   no vrrp 3 preempt
   vrrp 3 timers delay reload 900
   vrrp 3 ipv4 100.64.0.1
   vrrp 3 ipv4 version 3
!
interface Vlan334
   description v6 attached host exports
   ipv6 attached-host route export 19
   ipv6 enable
   ipv6 address 2001:db8:334::1/64
!
interface Vlan335
   description v6 attached host exports
   ipv6 attached-host route export prefix-length 64
   ipv6 enable
   ipv6 address 2001:db8:335::1/64
!
interface Vlan336
   description v6 attached host exports
   ipv6 attached-host route export 18 prefix-length 64
   ipv6 enable
   ipv6 address 2001:db8:336::1/64
!
interface Vlan337
   description v4 dhcp relay all-subnets
   ip address 10.0.2.2/25
   ip dhcp relay all-subnets
!
interface Vlan338
   description v6 dhcp relay all-subnets
   ipv6 dhcp relay all-subnets
   ipv6 address 2001:db8:338::1/64
!
interface Vlan339
   description v6 nd options
   ipv6 nd cache expire 250
   ipv6 nd cache dynamic capacity 900
   ipv6 nd cache refresh always
   ipv6 enable
   ipv6 address 2001:db8:339::1/64
   ipv6 nd other-config-flag
!
interface Vlan501
   description SVI Description
   no shutdown
   ip address 10.50.26.29/27
   ipv6 address 1b11:3a00:22b0:0088::207/127
   ipv6 nd ra disabled
!
interface Vlan667
   description Multiple VRIDs
   no shutdown
   ip address 192.0.2.2/25
   arp aging timeout 180
   ipv6 enable
   ipv6 address 2001:db8:667::2/64
   ipv6 address fe80::2/64 link-local
   vrrp 1 priority-level 105
   vrrp 1 advertisement interval 2
   vrrp 1 preempt delay minimum 30 reload 800
   vrrp 1 ipv4 192.0.2.1
   vrrp 2 ipv6 2001:db8:667::1
!
interface Vlan1001
   description SVI Description
   no shutdown
   vrf Tenant_A
   ipv6 address a1::1/64
   ipv6 nd managed-config-flag
   ipv6 nd prefix a1::/64 infinite infinite no-autoconfig
   ip address virtual 10.1.1.1/24
!
interface Vlan1002
   description SVI Description
   no shutdown
   vrf Tenant_A
   ipv6 address a2::1/64
   ipv6 nd ra disabled
   ipv6 nd managed-config-flag
   ipv6 nd prefix a2::/64 infinite infinite no-autoconfig
   ip address virtual 10.1.2.1/24
!
interface Vlan2001
   description SVI Description
   logging event link-status
   vrf Tenant_B
   ip address virtual 10.2.1.1/24
   comment
   Comment created from eos_cli under vlan_interfaces.Vlan2001
   EOF

!
interface Vlan2002
   description SVI Description
   no autostate
   vrf Tenant_B
   ip verify unicast source reachable-via rx
   isis enable EVPN_UNDERLAY
   isis bfd
   isis authentication mode md5 rx-disabled
   isis authentication key 0 password
   ip address virtual 10.2.2.1/24
!
interface Vlan4094
   description SVI Description
   mtu 9214
   ip address 169.254.252.0/31
   ipv6 address fe80::a/64 link-local
   pim ipv4 sparse-mode
   pim ipv4 bidirectional
   pim ipv4 hello interval 10
   pim ipv4 hello count 3.5
   pim ipv4 dr-priority 200
   pim ipv4 bfd
   isis enable EVPN_UNDERLAY
   isis authentication mode sha key-id 5 rx-disabled level-1
   isis authentication mode sha key-id 10 rx-disabled level-2
```

### VXLAN Interface

#### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| Source Interface | Loopback0 |
| Controller Client | True |
| MLAG Source Interface | Loopback1 |
| UDP port | 4789 |
| Vtep-to-Vtep Bridging | True |
| EVPN MLAG Shared Router MAC | mlag-system-id |
| VXLAN flood-lists learning from data-plane | Enabled |
| Qos dscp propagation encapsulation | Enabled |
| Qos ECN propagation | Enabled |
| Qos map dscp to traffic-class decapsulation | Enabled |
| Remote VTEPs EVPN BFD transmission rate | 300ms |
| Remote VTEPs EVPN BFD expected minimum incoming rate (min-rx) | 300ms |
| Remote VTEPs EVPN BFD multiplier | 3 |
| Remote VTEPs EVPN BFD prefix-list | PL-TEST |
| Multicast headend-replication | Enabled |

##### VLAN to VNI, Flood List and Multicast Group Mappings

| VLAN | VNI | Flood List | Multicast Group |
| ---- | --- | ---------- | --------------- |
| 110 | 10110 | - | 239.9.1.4 |
| 111 | 10111 | 10.1.1.10<br/>10.1.1.11 | - |
| 112 | - | - | 239.9.1.6 |

##### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| Tenant_A_OP_Zone | 10 | 232.0.0.10 |
| Tenant_A_WEB_Zone | 11 | - |

##### Default Flood List

| Default Flood List |
| ------------------ |
| 10.1.0.10<br/>10.1.0.11 |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description DC1-LEAF2A_VTEP
   vxlan source-interface Loopback0
   vxlan controller-client
   vxlan virtual-router encapsulation mac-address mlag-system-id
   vxlan udp-port 4789
   vxlan bridging vtep-to-vtep
   vxlan flood vtep learned data-plane
   vxlan vlan 110 vni 10110
   vxlan vlan 111 vni 10111
   vxlan vrf Tenant_A_OP_Zone vni 10
   vxlan vrf Tenant_A_WEB_Zone vni 11
   vxlan mlag source-interface Loopback1
   bfd vtep evpn interval 300 min-rx 300 multiplier 3
   bfd vtep evpn prefix-list PL-TEST
   vxlan flood vtep 10.1.0.10 10.1.0.11
   vxlan vlan 111 flood vtep 10.1.1.10 10.1.1.11
   vxlan vlan 110 multicast group 239.9.1.4
   vxlan vlan 112 multicast group 239.9.1.6
   vxlan vrf Tenant_A_OP_Zone multicast group 232.0.0.10
   vxlan multicast headend-replication
   vxlan qos ecn propagation
   vxlan qos dscp propagation encapsulation
   vxlan qos map dscp to traffic-class decapsulation
   vxlan encapsulation ipv4

```

## Switchport Port-security

### Switchport Port-security Summary

| Settings | Value |
| -------- | ----- |
| Mac-address Aging | True |
| Mac-address Moveable | True |
| Disable Persistence | True |
| Violation Protect Chip-based | True |

### Switchport Port-security Device Configuration

```eos
!
switchport port-security mac-address aging
switchport port-security mac-address moveable
switchport port-security persistence disabled
switchport port-security violation protect chip-based
```

## Routing

### Service Routing Configuration BGP

BGP no equals default enabled

```eos
!
service routing configuration bgp no-equals-default
```

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
| default | False |
| BLAH | - |
| defauls | - |
| defaulu | - |
| MGMT | False |
| TENANT_A_PROJECT01 | True |
| TENANT_A_PROJECT02 | True |

#### IP Routing Device Configuration

```eos
no ip routing vrf MGMT
ip routing vrf TENANT_A_PROJECT01
ip routing vrf TENANT_A_PROJECT02
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| BLAH | false |
| defauls | false |
| defaulu | false |
| MGMT | false |
| TENANT_A_PROJECT01 | false |
| TENANT_A_PROJECT02 | false |

### Static Routes

#### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP | Exit interface | Administrative Distance | Tag | Route Name | Metric |
| --- | ------------------ | ----------- | -------------- | ----------------------- | --- | ---------- | ------ |
| BLUE-C1 | 193.1.0.0/24 | - | Null0 | 1 | - | - | - |
| BLUE-C1 | 193.1.1.0/24 | - | Null0 | 1 | - | - | - |
| BLUE-C1 | 193.1.2.0/24 | - | Null0 | 1 | - | - | - |
| default | 1.1.1.0/24 | 10.1.1.1 | vlan1001 | 1 | - | - | - |
| default | 1.1.2.0/24 | 10.1.1.1 | vlan1001 | 200 | 666 | RT-TO-FAKE-DMZ | - |
| TENANT_A_PROJECT01 | 1.2.1.0/24 | 10.1.2.1 | vlan202 | 1 | - | - | - |
| TENANT_A_PROJECT01 | 1.2.2.0/24 | 10.1.2.1 | vlan1001 | 201 | 667 | RT-TO-FAKE-DMZ | - |
| TENANT_A_PROJECT02 | 10.3.4.0/24 | 1.2.3.4 | - | 1 | - | - | - |
| TENANT_A_PROJECT02 | 10.3.5.0/24 | - | Null0 | 1 | - | - | - |
| TENANT_A_PROJECT01 | 10.3.6.0/24 | 11.2.1.1 (tracked with BFD) | Ethernet40 | 100 | 1000 | Track-BFD | 300 |
| TENANT_A_PROJECT01 | 10.3.7.0/24 | - | Ethernet41 | 100 | 1000 | No-Track-BFD | 300 |

#### Static Routes Device Configuration

```eos
!
ip route 1.1.1.0/24 Vlan1001 10.1.1.1
ip route 1.1.2.0/24 Vlan1001 10.1.1.1 200 tag 666 name RT-TO-FAKE-DMZ
ip route vrf BLUE-C1 193.1.0.0/24 Null0
ip route vrf BLUE-C1 193.1.1.0/24 Null0
ip route vrf BLUE-C1 193.1.2.0/24 Null0
ip route vrf TENANT_A_PROJECT01 1.2.1.0/24 Vlan202 10.1.2.1
ip route vrf TENANT_A_PROJECT01 1.2.2.0/24 Vlan1001 10.1.2.1 201 tag 667 name RT-TO-FAKE-DMZ
ip route vrf TENANT_A_PROJECT01 10.3.6.0/24 Ethernet40 11.2.1.1 track bfd 100 tag 1000 name Track-BFD metric 300
ip route vrf TENANT_A_PROJECT01 10.3.7.0/24 Ethernet41 100 tag 1000 name No-Track-BFD metric 300
ip route vrf TENANT_A_PROJECT02 10.3.4.0/24 1.2.3.4
ip route vrf TENANT_A_PROJECT02 10.3.5.0/24 Null0
```

### IPv6 Static Routes

#### IPv6 Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| default | 2a01:cb04:4e6:d300::/64 | 2a01:cb04:4e6:d100::1 | vlan1001 | 1 | - | - | - |
| default | 2a01:cb04:4e6:d400::/64 | 2a01:cb04:4e6:d100::1 | vlan1001 | 200 | 666 | RT-TO-FAKE-DMZ | - |
| default | 2a01:cb04:4e6:d400::/64 | 2a01:cb04:4e6:d100::1 | vlan1001 | 200 | 666 | RT-TO-FAKE-DB-ZONE | 100 |
| TENANT_A_PROJECT01 | 2a01:cb04:4e6:a300::/64 | 2a01:cb04:4e6:100::1 | vlan1001 | 1 | - | - | - |
| TENANT_A_PROJECT01 | 2a01:cb04:4e6:a400::/64 | 2a01:cb04:4e6:100::1 | vlan1001 | 201 | 667 | RT-TO-FAKE-DMZ | - |
| TENANT_A_PROJECT01 | 2b01:cb04:4e6:a400::/64 | 2a01:cb04:4e6:102::1 (tracked with BFD) | vlan102 | 201 | 102 | Track-BFD | 100 |
| TENANT_A_PROJECT01 | 2c01:cb04:4e6:a400::/64 | - | vlan102 | 201 | 102 | No-Track-BFD | - |

#### Static Routes Device Configuration

```eos
!
ipv6 route 2a01:cb04:4e6:d300::/64 Vlan1001 2a01:cb04:4e6:d100::1
ipv6 route 2a01:cb04:4e6:d400::/64 Vlan1001 2a01:cb04:4e6:d100::1 200 tag 666 name RT-TO-FAKE-DMZ
ipv6 route 2a01:cb04:4e6:d400::/64 Vlan1001 2a01:cb04:4e6:d100::1 200 tag 666 name RT-TO-FAKE-DB-ZONE metric 100
ipv6 route vrf TENANT_A_PROJECT01 2a01:cb04:4e6:a300::/64 Vlan1001 2a01:cb04:4e6:100::1
ipv6 route vrf TENANT_A_PROJECT01 2a01:cb04:4e6:a400::/64 Vlan1001 2a01:cb04:4e6:100::1 201 tag 667 name RT-TO-FAKE-DMZ
ipv6 route vrf TENANT_A_PROJECT01 2b01:cb04:4e6:a400::/64 Vlan102 2a01:cb04:4e6:102::1 track bfd 201 tag 102 name Track-BFD metric 100
ipv6 route vrf TENANT_A_PROJECT01 2c01:cb04:4e6:a400::/64 Vlan102 201 tag 102 name No-Track-BFD
```

### IPv6 Neighbors

IPv6 neighbor cache persistency is enabled. The refresh-delay is 1000 seconds after reboot.

#### IPv6 Static Neighbors

| VRF | IPv6 Address | Exit Interface | MAC Address |
| --- | ------------ | -------------- | ----------- |
| MGMT | 11:22:33:44:55:66:77:88 | Ethernet1 | 11:22:33:44:55:66 |
| - | ::ffff:192.1.56.10 | Loopback99 | aa:af:12:34:bc:bf |

#### IPv6 Neighbor Configuration

```eos
!
ipv6 neighbor persistent refresh-delay 1000
ipv6 neighbor vrf MGMT 11:22:33:44:55:66:77:88 Ethernet1 11:22:33:44:55:66
ipv6 neighbor ::ffff:192.1.56.10 Loopback99 aa:af:12:34:bc:bf
```

### ARP

ARP cache persistency is enabled. The refresh-delay is 700 seconds after reboot.

Global ARP timeout: 300

#### ARP Static Entries

| VRF | IPv4 address | MAC address |
| --- | ------------ | ----------- |
| BLAH | 42.42.42.42 | DEAD.BEEF.CAFE |
| defauls | 42.42.42.42 | DEAD.BEEF.CAFE |
| default | 41.42.42.42 | DEAD.BEEF.CAFE |
| default | 42.42.42.42 | DEAD.BEEF.CAFE |
| default | 43.42.42.42 | DEAD.BEEF.CAFE |
| defaulu | 42.42.42.42 | DEAD.BEEF.CAFE |

#### ARP Device Configuration

```eos
!
arp persistent refresh-delay 700
arp aging timeout default 300
arp vrf BLAH 42.42.42.42 DEAD.BEEF.CAFE arpa
arp vrf defauls 42.42.42.42 DEAD.BEEF.CAFE arpa
arp 41.42.42.42 DEAD.BEEF.CAFE arpa
arp 42.42.42.42 DEAD.BEEF.CAFE arpa
arp 43.42.42.42 DEAD.BEEF.CAFE arpa
arp vrf defaulu 42.42.42.42 DEAD.BEEF.CAFE arpa
```

### Router Adaptive Virtual Topology

#### Router Adaptive Virtual Topology Summary

Topology role: pathfinder

| Hierarchy | Name | ID |
| --------- | ---- | -- |
| Region | North_America | 1 |
| Zone | Canada | 2 |
| Site | Ottawa | 99 |

#### AVT Profiles

| Profile name | Load balance policy | Internet exit policy |
| ------------ | ------------------- | -------------------- |
| office365 | - | - |
| scavenger | scavenger-lb | scavenger-ie |
| video | - | video-ie |
| voice | voice-lb | - |

#### AVT Policies

##### AVT policy production

| Application profile | AVT Profile | Traffic Class | DSCP |
| ------------------- | ----------- | ------------- | ---- |
| videoApps | - | - | - |
| criticalApps | crit | 7 | 45 |
| audioApps | audio | 6 | - |
| mfgApp | crit | - | 54 |
| hrApp | hr | - | - |

#### VRFs configuration

##### VRF blue

| AVT Profile | AVT ID |
| ----------- | ------ |
| video | 1 |

##### VRF red

| AVT policy |
| ---------- |
| production |

| AVT Profile | AVT ID |
| ----------- | ------ |
| video | 1 |
| voice | 2 |

#### Router Adaptive Virtual Topology Configuration

```eos
!
router adaptive-virtual-topology
   topology role pathfinder
   region North_America id 1
   zone Canada id 2
   site Ottawa id 99
   !
   policy production
      !
      match application-profile videoApps
      !
      match application-profile criticalApps
         avt profile crit
         traffic-class 7
         dscp 45
      !
      match application-profile audioApps
         avt profile audio
         traffic-class 6
      !
      match application-profile mfgApp
         avt profile crit
         dscp 54
      !
      match application-profile hrApp
         avt profile hr
   !
   profile office365
   !
   profile scavenger
      internet-exit policy scavenger-ie
      path-selection load-balance scavenger-lb
   !
   profile video
      internet-exit policy video-ie
   !
   profile voice
      path-selection load-balance voice-lb
   !
   vrf blue
      avt profile video id 1
   !
   vrf red
      avt policy production
      avt profile video id 1
      avt profile voice id 2
```

### Router General

- Global IPv4 Router ID: 10.1.2.3

- Global IPv6 Router ID: 2001:beef:cafe::1

- Nexthop fast fail-over is enabled.

#### VRF Route leaking

| VRF | Source VRF | Route Map Policy |
|-----|------------|------------------|
| BLUE-C2 | BLUE-C1 | RM-BLUE-LEAKING |
| BLUE-C2 | BLUE-C3 | RM-BLUE-LEAKING |

#### VRF Routes Dynamic Prefix-lists

| VRF | Dynamic Prefix-list |
|-----|---------------------|
| BLUE-C2 | DYNAMIC_TEST_PREFIX_LIST_1 |
| BLUE-C2 | DYNAMIC_TEST_PREFIX_LIST_2 |

#### Router General Device Configuration

```eos
!
router general
   router-id ipv4 10.1.2.3
   router-id ipv6 2001:beef:cafe::1
   hardware next-hop fast-failover
   !
   vrf BLUE-C2
      leak routes source-vrf BLUE-C1 subscribe-policy RM-BLUE-LEAKING
      leak routes source-vrf BLUE-C3 subscribe-policy RM-BLUE-LEAKING
      routes dynamic prefix-list DYNAMIC_TEST_PREFIX_LIST_1
      routes dynamic prefix-list DYNAMIC_TEST_PREFIX_LIST_2
      exit
   !
   control-functions
      code unit code1
         function ACCEPT_ALL() {
           return true;
           }
         EOF
      code unit code2
         function DENY_ALL() {
           return true;
           }
         EOF
   !
   exit
```

## Router Service Insertion

Router service-insertion is enabled.

### Connections

#### Connections Through Ethernet Interface

| Name | Interface | Next Hop | Monitor Connectivity Host |
| ---- | --------- | -------- | ------------------------- |
| aconnection | Ethernet4/1 | 10.10.10.10 | host4 |
| connection1 | Ethernet2/2.2 | 10.10.10.10 | host1 |
| connection6 | Ethernet2 | 10.10.10.10 | - |
| connection7 | Ethernet3/1 | 10.10.10.10 | host4 |

#### Connections Through Tunnel Interface

| Name | Primary Interface | Secondary Interface | Monitor Connectivity Host |
| ---- | ----------------- | ------------------- | ------------------------- |
| connection2 | Tunnel1 | Tunnel2 | host2 |
| connection3 | - | Tunnel3 | host3 |
| connection4 | Tunnel4 | - | - |
| connection5 | Tunnel5 | Tunnel6 | - |

### Router Service Insertion Configuration

```eos
!
router service-insertion
   connection aconnection
      interface Ethernet4/1 next-hop 10.10.10.10
      monitor connectivity host host4
   connection connection1
      interface Ethernet2/2.2 next-hop 10.10.10.10
      monitor connectivity host host1
   connection connection2
      interface Tunnel1 primary
      interface Tunnel2 secondary
      monitor connectivity host host2
   connection connection3
      interface Tunnel3 secondary
      monitor connectivity host host3
   connection connection4
      interface Tunnel4 primary
   connection connection5
      interface Tunnel5 primary
      interface Tunnel6 secondary
   connection connection6
      interface Ethernet2 next-hop 10.10.10.10
   connection connection7
      interface Ethernet3/1 next-hop 10.10.10.10
      monitor connectivity host host4
```

### Router Traffic-Engineering

- Traffic Engineering is enabled.

#### Segment Routing Summary

- SRTE is enabled.

- system-colored-tunnel-rib is enabled

##### SRTE Policies

| Endpoint | Color | Preference | Name | Description | SBFD Remote Discriminator | Label Stack | Index  | Weight | Explicit Null |
| -------- | ----- | ---------- | ---- | ----------- | ------------------------- | ----------- | ------ | ------ | ------------- |
| 1.2.3.4 | 70810 | 180 | SRTE-1.2.3.4-70810 | SRTE POLICY FOR 1.2.3.4 COLOR 70810 | 155.2.1.1 | 900002 900003 900005 900006 | 200 | - | ipv4 ipv6 |
| 1.2.3.4 | 80810 | 100 | SRTE-1.2.3.4-80810 | SRTE POLICY FOR 1.2.3.4 COLOR 80810 | - | 900002 900008 900007 900006 | 100 | 20 | none |
| 5.6.7.8 | 20320 | 80 | - | - | 2600599809 | 900002 900003 900005 900006 | 300 | 120 | ipv4 |
| 5.6.7.8 | 20320 | 80 | - | - | 2600599809 | 900002 900004 900007 900006 | 400 | 220 | ipv4 |
| 5.6.7.8 | 20320 | 120 | - | - | 2600599809 | 900002 900008 900009 900006 | - | - | ipv6 |
| 5.6.7.8 | 20320 | 120 | - | - | 2600599809 | 900002 900010 900011 900012 | - | - | ipv6 |

#### Router Traffic Engineering Device Configuration

```eos
!
router traffic-engineering
   segment-routing
      rib system-colored-tunnel-rib
      !
      policy endpoint 1.2.3.4 color 70810
         binding-sid 970810
         name SRTE-1.2.3.4-70810
         description SRTE POLICY FOR 1.2.3.4 COLOR 70810
         sbfd remote-discriminator 155.2.1.1
         !
         path-group preference 180
            explicit-null ipv4 ipv6
            segment-list label-stack 900002 900003 900005 900006 index 200
      !
      policy endpoint 1.2.3.4 color 80810
         name SRTE-1.2.3.4-80810
         description SRTE POLICY FOR 1.2.3.4 COLOR 80810
         !
         path-group preference 100
            explicit-null none
            segment-list label-stack 900002 900008 900007 900006 weight 20 index 100
      !
      policy endpoint 5.6.7.8 color 20320
         binding-sid 978320
         sbfd remote-discriminator 2600599809
         !
         path-group preference 80
            explicit-null ipv4
            segment-list label-stack 900002 900003 900005 900006 weight 120 index 300
            segment-list label-stack 900002 900004 900007 900006 weight 220 index 400
         !
         path-group preference 120
            explicit-null ipv6
            segment-list label-stack 900002 900008 900009 900006
            segment-list label-stack 900002 900010 900011 900012
   router-id ipv4 10.0.0.1
   router-id ipv6 2001:beef:cafe::1
```

### Router BGP

ASN Notation: asdot

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65101 | 192.168.255.3 |

| BGP Tuning |
| ---------- |
| graceful-restart restart-time 555 |
| graceful-restart stalepath-time 666 |
| graceful-restart |
| graceful-restart-helper restart-time 888 |
| bgp bestpath d-path |
| bgp additional-paths receive |
| bgp additional-paths send ecmp limit 30 |
| update wait-for-convergence |
| update wait-install |
| bgp default ipv4-unicast |
| bgp default ipv4-unicast transport ipv6 |
| no bgp redistribute-internal |
| distance bgp 20 200 200 |
| maximum-paths 32 ecmp 32 |
| bgp route-reflector preserve-attributes always |

#### Router BGP Listen Ranges

| Prefix | Peer-ID Include Router ID | Peer Group | Peer-Filter | Remote-AS | VRF |
| ------ | ------------------------- | ---------- | ----------- | --------- | --- |
| 10.10.10.0/24 | - | my-peer-group1 | my-peer-filter | - | default |
| 12.10.10.0/24 | True | my-peer-group3 | - | 65444 | default |
| 13.10.10.0/24 | - | my-peer-group4 | my-peer-filter | - | default |
| 10.10.10.0/24 | - | my-peer-group1 | my-peer-filter | - | YELLOW-C1 |
| 12.10.10.0/24 | True | my-peer-group3 | - | 65444 | YELLOW-C1 |
| 13.10.10.0/24 | - | my-peer-group4 | my-peer-filter | - | YELLOW-C1 |

#### Router BGP Peer Groups

##### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Allowas-in | Allowed, allowed 3 (default) times |
| Remote AS | 65001 |
| Source | Loopback0 |
| RIB Pre-Policy Retain | True (All) |
| BFD | True |
| BFD Timers | interval: 2000, min_rx: 2000, multiplier: 3 |
| Ebgp multihop | 3 |
| Default originate | True |
| Send community | all |
| Maximum routes | 0 (no limit) |

##### EVPN-OVERLAY-RS-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Remote AS | 65001 |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 3 |
| Send community | all |
| Maximum routes | 0 (no limit) |

##### EXTENDED-COMMUNITY

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | extended |

##### IPv4-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65001 |
| RIB Pre-Policy Retain | False |
| Send community | all |
| Maximum routes | 12000 |

##### IPV6-UNDERLAY

| Settings | Value |
| -------- | ----- |
| Remote AS | 65000 |
| Send community | all |
| Maximum routes | 12000 |

##### IPV6-UNDERLAY-MLAG

| Settings | Value |
| -------- | ----- |
| Remove Private AS Outbound | False |
| Remove Private AS Inbound | False |
| Remote AS | 65100 |
| Next-hop self | True |
| Send community | all |
| Maximum routes | 12000 |

##### LARGE-COMMUNITY

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | large |

##### LOCAL-AS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Local AS | 65000 |

##### MLAG-IPv4-UNDERLAY-PEER

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remove Private AS Outbound | True (All) (Replace AS) |
| Remove Private AS Inbound | True (Replace AS) |
| Remote AS | 65101 |
| Next-hop self | True |
| Send community | all |
| Maximum routes | 12000 (warning-limit 80 percent, warning-only) |

##### MPLS-IBGP-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | vpn-ipv4, vpn-ipv6 |
| Remote AS | 65000 |
| Local AS | 65000 |
| Send community | all |
| Maximum routes | 0 (no limit) |

##### MULTIPLE-COMMUNITY

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | standard large |

##### NO-COMMUNITY

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |

##### OBS_WAN

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65000 |
| BFD | True |
| BFD Timers | interval: 2000, min_rx: 2000, multiplier: 3 |

##### PATH-SELECTION-PG-1

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65001 |

##### PATH-SELECTION-PG-2

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65001 |

##### PATH-SELECTION-PG-3

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65001 |

##### PATH-SELECTION-PG-4

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65001 |

##### PATH-SELECTION-PG-5

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65001 |

##### PG-1

| Settings | Value |
| -------- | ----- |
| Remote AS | 65001.0002 |

##### PG-2

| Settings | Value |
| -------- | ----- |
| Remote AS | 65001.0003 |

##### SEDI

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65003 |
| Source | Loopback101 |
| Ebgp multihop | 10 |

##### SEDI-shut

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Shutdown | True |

##### SR-TE-PG-1

| Settings | Value |
| -------- | ----- |
| Remote AS | 65000 |

##### SR-TE-PG-2

| Settings | Value |
| -------- | ----- |
| Remote AS | 65000 |

##### STARDARD-COMMUNITY

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | standard |

##### TEST

| Settings | Value |
| -------- | ----- |
| TTL Max Hops | 42 |

##### test-link-bandwidth1

| Settings | Value |
| -------- | ----- |
| TTL Max Hops | 1 |
| Link-Bandwidth | default 100G |

##### test-link-bandwidth2

| Settings | Value |
| -------- | ----- |
| Link-Bandwidth | enabled |

##### test-passive

| Settings | Value |
| -------- | ----- |
| Passive | True |

##### TEST-PASSIVE

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65003 |
| Passive | True |

##### test-session-tracker

| Settings | Value |
| -------- | ----- |
| Session tracker | ST2 |

##### WELCOME_ROUTERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65001 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 1.1.1.1 | 1 | default | False | - | - | - | - | - | - | - | - |
| 1b11:3a00:22b0:0088::1 | Inherited from peer group IPV6-UNDERLAY | default | - | Inherited from peer group IPV6-UNDERLAY | Inherited from peer group IPV6-UNDERLAY | - | - | - | - | - | - |
| 1b11:3a00:22b0:0088::3 | Inherited from peer group IPV6-UNDERLAY | default | - | Inherited from peer group IPV6-UNDERLAY | Inherited from peer group IPV6-UNDERLAY | - | - | - | - | - | - |
| 1b11:3a00:22b0:0088::5 | Inherited from peer group IPV6-UNDERLAY | default | - | Inherited from peer group IPV6-UNDERLAY | Inherited from peer group IPV6-UNDERLAY | - | - | - | - | - | - |
| 10.50.2.1 | - | default | - | - | - | - | - | - | - | - | - |
| 10.50.2.3 | - | default | - | - | - | - | - | - | - | - | - |
| 10.50.2.5 | - | default | - | - | - | - | - | - | - | - | - |
| 10.50.64.11 | - | default | - | - | - | - | - | - | - | - | - |
| 10.50.64.12 | - | default | - | - | - | - | - | - | - | - | - |
| 10.50.64.13 | - | default | - | - | - | - | - | - | - | - | - |
| 169.254.252.1 | - | default | - | - | - | - | - | - | - | - | - |
| 172.31.255.0 | Inherited from peer group IPv4-UNDERLAY-PEERS | default | - | Inherited from peer group IPv4-UNDERLAY-PEERS | Inherited from peer group IPv4-UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.31.255.2 | - | default | - | - | - | - | - | - | - | - | - |
| 172.31.255.3 | - | default | - | - | - | - | - | - | - | - | - |
| 172.31.255.4 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | Allowed, allowed 5 times | Inherited from peer group EVPN-OVERLAY-PEERS(interval: 2000, min_rx: 2000, multiplier: 3) | True (All) | - | - | - |
| 192.0.3.1 | 65432 | default | - | all | - | - | True(interval: 2000, min_rx: 2000, multiplier: 3) | True | - | True | - |
| 192.0.3.2 | 65433 | default | - | extended | 10000 | - | False | True (All) | - | - | - |
| 192.0.3.3 | 65434 | default | - | standard | - | - | - | True | - | - | - |
| 192.0.3.4 | 65435 | default | - | large | - | - | - | False | - | - | 1 |
| 192.0.3.5 | 65436 | default | - | standard | 12000 | - | - | - | - | - | - |
| 192.0.3.6 | 65437 | default | - | - | - | - | - | - | False | - | - |
| 192.0.3.7 | 65438 | default | - | - | - | - | - | - | True | - | - |
| 192.0.3.8 | 65438 | default | - | - | - | - | True | - | - | - | Inherited from peer group TEST |
| 192.0.3.9 | 65438 | default | - | - | - | - | False | - | - | - | Inherited from peer group TEST |
| 192.168.42.42 | 65004 | default | - | - | - | - | - | - | - | - | - |
| 192.168.251.1 | - | default | True | - | - | - | - | - | - | - | - |
| 192.168.251.2 | - | default | - | - | - | - | - | - | - | - | - |
| 192.168.252.1 | - | default | - | - | - | - | - | - | - | - | - |
| 192.168.255.1 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS(interval: 2000, min_rx: 2000, multiplier: 3) | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.255.2 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS(interval: 2000, min_rx: 2000, multiplier: 3) | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.255.3 | - | default | - | - | 52000 (warning-limit 2000, warning-only) | Allowed, allowed 5 times | - | - | - | - | - |
| 192.168.255.4 | 65004 | default | - | all | - | - | - | - | - | - | - |
| 192.168.255.11 | - | default | - | - | - | - | - | - | - | - | - |
| 192.168.255.21 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS(interval: 2000, min_rx: 2000, multiplier: 3) | False | - | - | - |
| 192.168.255.101 | Inherited from peer group MPLS-IBGP-PEERS | default | - | Inherited from peer group MPLS-IBGP-PEERS | Inherited from peer group MPLS-IBGP-PEERS | - | - | - | - | - | - |
| 192.168.255.201 | Inherited from peer group MPLS-IBGP-PEERS | default | - | Inherited from peer group MPLS-IBGP-PEERS | Inherited from peer group MPLS-IBGP-PEERS | - | - | - | - | - | - |
| 2001:cafe:192:168::4 | 65004 | default | - | all | - | - | - | - | - | - | - |
| 2001:db8::dead:beef:cafe | 65004 | default | - | - | - | - | - | - | - | - | - |
| fe80::b%Vl4094 | Inherited from peer group IPV6-UNDERLAY-MLAG | default | - | Inherited from peer group IPV6-UNDERLAY-MLAG | Inherited from peer group IPV6-UNDERLAY-MLAG | - | - | - | - | - | - |
| 10.1.1.0 | Inherited from peer group OBS_WAN | BLUE-C1 | - | - | - | - | Inherited from peer group OBS_WAN(interval: 2000, min_rx: 2000, multiplier: 3) | - | False | - | - |
| 10.255.1.1 | Inherited from peer group WELCOME_ROUTERS | BLUE-C1 | - | - | - | - | - | - | True | - | - |
| 101.0.3.1 | Inherited from peer group SEDI | BLUE-C1 | - | - | - | - | - | - | - | - | - |
| 101.0.3.2 | Inherited from peer group SEDI | BLUE-C1 | True | - | - | Allowed, allowed 3 (default) times | - | - | - | - | - |
| 101.0.3.3 | - | BLUE-C1 | Inherited from peer group SEDI-shut | - | - | Allowed, allowed 5 times | - | - | - | - | - |
| 101.0.3.4 | Inherited from peer group TEST-PASSIVE | BLUE-C1 | - | - | - | - | - | - | - | Inherited from peer group TEST-PASSIVE | - |
| 101.0.3.5 | Inherited from peer group WELCOME_ROUTERS | BLUE-C1 | - | - | - | - | False | - | - | True | - |
| 101.0.3.6 | Inherited from peer group WELCOME_ROUTERS | BLUE-C1 | - | - | - | - | True(interval: 2500, min_rx: 2000, multiplier: 3) | - | - | - | - |
| 101.0.3.7 | - | BLUE-C1 | - | - | - | - | True | - | - | - | - |
| 101.0.3.8 | - | BLUE-C1 | - | - | - | - | False | - | - | - | - |
| 10.1.1.0 | Inherited from peer group OBS_WAN | RED-C1 | - | - | - | - | Inherited from peer group OBS_WAN(interval: 2000, min_rx: 2000, multiplier: 3) | - | - | - | - |
| 10.255.251.1 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | TENANT_A_PROJECT01 | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |
| 10.2.3.4 | 1234 | TENANT_A_PROJECT01 | - | all | 0 (no limit) (warning-limit 100, warning-only) | - | - | - | - | - | - |
| 10.255.251.1 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | TENANT_A_PROJECT02 | - | standard | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |
| 10.255.251.2 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | TENANT_A_PROJECT02 | - | extended | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |
| 10.255.251.3 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | TENANT_A_PROJECT02 | - | large | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |
| 10.255.251.4 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | TENANT_A_PROJECT02 | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | True | - | - | - | - |
| 1.1.1.1 | - | VRF02 | - | - | - | - | - | - | - | - | - |
| 10.1.1.0 | Inherited from peer group OBS_WAN | YELLOW-C1 | - | - | - | - | Inherited from peer group OBS_WAN(interval: 2000, min_rx: 2000, multiplier: 3) | - | - | - | - |

#### BGP Neighbor Interfaces

| Neighbor Interface | VRF | Peer Group | Remote AS | Peer Filter |
| ------------------ | --- | ---------- | --------- | ----------- |
| Ethernet2 | default | PG-FOO-v4 | 65102 | - |
| Ethernet3 | default | PG-FOO-v4 | - | PF-BAR-v4 |

#### BGP Route Aggregation

| Prefix | AS Set | Summary Only | Attribute Map | Match Map | Advertise Only |
| ------ | ------ | ------------ | ------------- | --------- | -------------- |
| 1.1.1.0/24 | False | False | - | - | True |
| 1.12.1.0/24 | True | True | RM-ATTRIBUTE | RM-MATCH | True |
| 2.2.1.0/24 | False | False | - | - | False |

#### Router BGP EVPN Address Family

- VPN import pruning is **enabled**

- Next-hop resolution is **disabled**
- Next-hop-unchanged is explicitly configured (default behaviour)

- Next-hop MPLS resolution Primary-RIB : tunnel-rib colored system-colored-tunnel-rib
- Next-hop MPLS resolution Secondary-RIB : tunnel-rib test-rib
- Next-hop MPLS resolution Tertiary-RIB : system-connected
- Layer-2 In-place FEC update tracking timeout: 100 seconds

##### EVPN Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | Encapsulation |
| ---------- | -------- | ------------ | ------------- | ------------- |
| ADDITIONAL-PATH-PG-1 | True |  - | - | default |
| ADDITIONAL-PATH-PG-2 | True |  - | - | default |
| ADDITIONAL-PATH-PG-3 | True |  - | - | default |
| ADDITIONAL-PATH-PG-4 | True |  - | - | default |
| ADDITIONAL-PATH-PG-5 | True |  - | - | default |
| ADDITIONAL-PATH-PG-6 | True |  - | - | default |
| EVPN-OVERLAY | True |  RM-HIDE-AS-PATH | RM-HIDE-AS-PATH | default |
| EVPN-OVERLAY-PEERS | True |  - | - | vxlan |
| IPv4-UNDERLAY-PEERS | False |  - | - | default |
| MLAG-IPv4-UNDERLAY-PEER | False |  - | - | default |
| RCF_TEST | False |  - | - | default |
| TEST-ENCAPSULATION | True |  - | - | mpls |
| TEST-ENCAPSULATION-2 | True |  - | - | path-selection |

##### EVPN Neighbors

| Neighbor | Activate | Route-map In | Route-map Out | Encapsulation |
| -------- | -------- | ------------ | ------------- | ------------- |
| 10.100.100.1 | True | - | - | default |
| 10.100.100.2 | True | - | - | default |
| 10.100.100.3 | True | - | - | default |
| 10.100.100.4 | True | RM1 | RM2 | path-selection |
| 10.100.100.5 | True | - | - | mpls |
| 192.168.255.3 | False | - | - | default |
| 192.168.255.4 | False | - | - | mpls |

##### EVPN Neighbor Default Encapsulation

| Neighbor Default Encapsulation | Next-hop-self Source Interface |
| ------------------------------ | ------------------------------ |
| mpls | Loopback0 |

##### EVPN Host Flapping Settings

| State | Window | Threshold | Expiry Timeout |
| ----- | ------ | --------- | -------------- |
| Enabled | 10 Seconds | 1 | 3 Seconds |

##### EVPN DCI Gateway Summary

| Settings | Value |
| -------- | ----- |
| Local Domain | 65101:0 |
| Remote Domain | 65101:1 |
| Remote Domain Peer Groups | EVPN-OVERLAY-PEERS |
| Local Domain: Ethernet-Segment Identifier | 0011:1111:1111:1111:1111 |
| Local Domain: Ethernet-Segment import Route-Target | 11:11:11:11:11:11 |
| Remote Domain: Ethernet-Segment Identifier | 0022:2222:2222:2222:2222 |
| Remote Domain: Ethernet-Segment import Route-Target | 22:22:22:22:22:22 |

#### Router BGP IPv4 Labeled Unicast

##### General Settings

| Settings | Value |
| -------- | ----- |
| Update wait-for-convergence | Enabled |
| Next-hop Unchanged | True |
| LFIB entry installation skipped | True |
| Label local-termination | implicit-null |

##### IPv4 BGP-LU Peer-groups

| Peer-group | Activate | Route-map In | Route-map Out | RCF In | RCF Out |
| ---------- | -------- | ------------ | ------------- | ------ | ------- |
| PG-BGP-LU | True | RM_BGP_LU_IN | RM_BGP_LU_OUT | - | - |
| PG-BGP-LU1 | False | - | - | RCF_BGP_LU_IN() | RCF_BGP_LU_OUT() |
| PG-BGP-LU2 | False | - | - | - | - |
| PG-BGP-LU3 | False | - | - | - | - |

##### IPv4 BGP-LU Neighbors

| Neighbor | Activate | Route-map In | Route-map Out | RCF In | RCF Out |
| -------- | -------- | ------------ | ------------- | ------ | ------- |
| 192.168.66.21 | False | - | - | - | - |
| 192.168.66.22 | False | - | - | - | - |
| 198.51.100.1 | True | - | - | RCF_TEST() | RCF_TEST_OUT() |
| 198.51.100.2 | False | RM_IN_TEST | RM_OUT_TEST | - | - |

#### Router BGP IPv4 SR-TE Address Family

##### IPv4 SR-TE Neighbors

| Neighbor | Activate | Route-map In | Route-map Out |
| -------- | -------- | ------------ | ------------- |
| 192.168.42.42 | True | RM-SR-TE-PEER-IN4 | RM-SR-TE-PEER-OUT4 |
| 192.168.42.43 | False | - | - |

##### IPv4 SR-TE Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out |
| ---------- | -------- | ------------ | ------------- |
| SR-TE-PG-1 | True | RM-SR-TE-PEER-IN4 | RM-SR-TE-PEER-OUT4 |
| SR-TE-PG-2 | False | - | - |

#### Router BGP IPv6 SR-TE Address Family

##### IPv6 SR-TE Neighbors

| Neighbor | Activate | Route-map In | Route-map Out |
| -------- | -------- | ------------ | ------------- |
| 2001:db8::dead:beef:cafe | True | RM-SR-TE-PEER-IN6 | RM-SR-TE-PEER-OUT6 |
| 2002:db8::dead:beef:cafe | False | - | - |

##### IPv6 SR-TE Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out |
| ---------- | -------- | ------------ | ------------- |
| SR-TE-PG-2 | True | RM-SR-TE-PEER-IN6 | RM-SR-TE-PEER-OUT6 |
| SR-TE-PG-3 | False | - | - |

#### Router BGP Link-State Address Family

##### Link-State Neighbors

| Neighbor | Activate | Missing policy In action | Missing policy Out action |
| -------- | -------- | ------------------------ | ------------------------- |
| 192.168.255.1 | True | deny | deny |
| 192.168.255.2 | True | - | - |

##### Link-State Peer Groups

| Peer Group | Activate | Missing policy In action | Missing policy Out action |
| ---------- | -------- | ------------------------ | ------------------------- |
| PG-1 | True | deny-in-out | permit |
| PG-2 | False | - | - |

##### Link-State Path Selection Configuration

| Settings | Value |
| -------- | ----- |
| Role(s) | producer<br>consumer<br>propagator |

#### Router BGP VPN-IPv4 Address Family

- VPN import pruning is **enabled**

##### VPN-IPv4 Neighbors

| Neighbor | Activate | Route-map In | Route-map Out | RCF In | RCF Out |
| -------- | -------- | ------------ | ------------- | ------ | ------- |
| 192.168.255.4 | True | RM-NEIGHBOR-PEER-IN4 | RM-NEIGHBOR-PEER-OUT4 | - | - |
| 192.168.255.5 | False | - | - | Address_Family_VPN_IPV4_In() | Address_Family_VPN_IPV4_Out() |

##### VPN-IPv4 Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | RCF In | RCF Out |
| ---------- | -------- | ------------ | ------------- | ------ | ------- |
| MPLS-IBGP-PEERS | True | RM-IBGP-PEER-IN4 | RM-IBGP-PEER-OUT4 | - | - |
| Test_RCF | False | - | - | Address_Family_VPN_IPV4_In() | Address_Family_VPN_IPV4_Out() |

#### Router BGP VPN-IPv6 Address Family

- VPN import pruning is **enabled**

##### VPN-IPv6 Neighbors

| Neighbor | Activate | Route-map In | Route-map Out | RCF In | RCF Out |
| -------- | -------- | ------------ | ------------- | ------ | ------- |
| 2001:cafe:192:168::4 | True | RM-NEIGHBOR-PEER-IN6 | RM-NEIGHBOR-PEER-OUT6 | - | - |
| 2001:cafe:192:168::5 | False | - | - | Address_Family_VPN_IPV6_In() | Address_Family_VPN_IPV6_Out() |

##### VPN-IPv6 Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | RCF In | RCF Out |
| ---------- | -------- | ------------ | ------------- | ------ | ------- |
| MPLS-IBGP-PEERS | True | RM-IBGP-PEER-IN6 | RM-IBGP-PEER-OUT6 | - | - |
| Test_RCF | False | - | - | Address_Family_VPN_IPV6_In() | Address_Family_VPN_IPV6_Out() |

#### Router BGP Path-Selection Address Family

##### Path-Selection Neighbors

| Neighbor | Activate |
| -------- | -------- |
| 172.31.255.0 | True |
| 172.31.255.1 | True |
| 172.31.255.2 | True |
| 172.31.255.3 | True |
| 172.31.255.4 | False |

##### Path-Selection Peer Groups

| Peer Group | Activate |
| ---------- | -------- |
| PATH-SELECTION-PG-1 | True |
| PATH-SELECTION-PG-2 | True |
| PATH-SELECTION-PG-3 | True |
| PATH-SELECTION-PG-4 | True |
| PATH-SELECTION-PG-5 | False |

#### Router BGP VLAN Aware Bundles

| VLAN Aware Bundle | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute | VLANs |
| ----------------- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ | ----- |
| B-ELAN-201 | 192.168.255.3:20201 | - | - | 20201:20201 | learned<br>no host-route | 201 |
| TENANT_A_PROJECT01 | 192.168.255.3:11 | 11:11<br>remote 2:11 | - | - | learned<br>igmp<br>no static | 110 |
| TENANT_A_PROJECT02 | 192.168.255.3:12 | - | 12:12<br>remote 2:12 | remote 2:12 | learned | 112 |

#### Router BGP VLANs

| VLAN | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute |
| ---- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ |
| 24 | 10.50.64.15:10024 | 1:10024 | - | - | learned |
| 41 | 10.50.64.15:10041 | 1:10041 | - | - | learned |
| 42 | 10.50.64.15:10042 | 1:10042 | - | - | learned |
| 65 | 10.50.64.15:10065 | 1:10065 | - | - | learned |
| 66 | 145.245.21.0:66 | - | - | all 145.245.21.0:66 | no learned |
| 67 | 145.245.21.0:67 | - | 145.245.21.0:67 | - | no learned |
| 600 | 145.245.21.0:600 | - | all 145.245.21.0:600 | - | no learned |
| 666 | 145.245.21.0:666 | - | - | 145.245.21.0:666 | no learned |
| 2488 | 145.245.21.0:1 | 145.245.21.0:1 | - | - | no learned |

#### Router BGP VPWS Instances

| Instance | Route-Distinguisher | Both Route-Target | MPLS Control Word | Label Flow | MTU | Pseudowire | Local ID | Remote ID |
| -------- | ------------------- | ----------------- | ----------------- | -----------| --- | ---------- | -------- | --------- |
| TENANT_A | 100.70.0.2:1000 | 65000:1000 | True | True | 1600 | TEN_A_site1_site3_pw | 15 | 35 |
| TENANT_A | 100.70.0.2:1000 | 65000:1000 | True | True | 1600 | TEN_A_site2_site5_pw | 25 | 57 |
| TENANT_B | 100.70.0.2:2000 | 65000:2000 | False | False | - | TEN_B_site2_site5_pw | 26 | 58 |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute | EVPN Multicast |
| --- | ------------------- | ------------ | -------------- |
| BLUE-C1 | 1.0.1.1:101 | static<br>ospf | IPv4: False<br>Transit: False |
| RED-C1 | 1.0.1.1:102 | - | IPv4: False<br>Transit: False |
| Tenant_A | 10.50.64.15:30001 | ospf<br>ospfv3<br>connected | IPv4: False<br>Transit: False |
| TENANT_A_PROJECT01 | 192.168.255.3:11 | connected<br>static | IPv4: False<br>Transit: False |
| TENANT_A_PROJECT02 | 192.168.255.3:12 | connected<br>static | IPv4: False<br>Transit: False |
| TENANT_A_PROJECT03 | 192.168.255.3:13 | - | IPv4: True<br>Transit: True |
| TENANT_A_PROJECT04 | 192.168.255.3:14 | - | IPv4: True<br>Transit: False |
| Tenant_B | 10.50.64.15:30002 | - | IPv4: False<br>Transit: False |
| VRF01 | - | user<br>static<br>rip<br>ospf<br>ospfv3<br>isis<br>connected<br>bgp<br>attached_host | IPv4: False<br>Transit: False |
| VRF02 | - | dynamic<br>user<br>static<br>rip<br>ospf<br>ospfv3<br>isis<br>connected<br>bgp<br>attached_host | IPv4: False<br>Transit: False |
| VRF03 | - | dynamic | IPv4: False<br>Transit: False |
| YELLOW-C1 | 1.0.1.1:103 | - | IPv4: False<br>Transit: False |

#### Router BGP Session Trackers

| Session Tracker Name | Recovery Delay (in seconds) |
| -------------------- | --------------------------- |
| ST1 | 666 |
| ST2 | 42 |

#### Router BGP Device Configuration

```eos
!
router bgp 65101
   bgp asn notation asdot
   router-id 192.168.255.3
   update wait-for-convergence
   update wait-install
   bgp default ipv4-unicast
   bgp default ipv4-unicast transport ipv6
   distance bgp 20 200 200
   graceful-restart restart-time 555
   graceful-restart stalepath-time 666
   graceful-restart
   graceful-restart-helper restart-time 888
   bgp route-reflector preserve-attributes always
   maximum-paths 32 ecmp 32
   bgp additional-paths receive
   bgp additional-paths send ecmp limit 30
   bgp listen range 10.10.10.0/24 peer-group my-peer-group1 peer-filter my-peer-filter
   bgp listen range 12.10.10.0/24 peer-id include router-id peer-group my-peer-group3 remote-as 65444
   bgp listen range 13.10.10.0/24 peer-group my-peer-group4 peer-filter my-peer-filter
   bgp bestpath d-path
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS remote-as 65001
   neighbor EVPN-OVERLAY-PEERS weight 100
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS bfd interval 2000 min-rx 2000 multiplier 3
   neighbor EVPN-OVERLAY-PEERS allowas-in
   neighbor EVPN-OVERLAY-PEERS rib-in pre-policy retain all
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS timers 1600 1600
   neighbor EVPN-OVERLAY-PEERS password 7 <removed>
   neighbor EVPN-OVERLAY-PEERS password shared-secret profile profile2 algorithm aes-128-cmac-96
   neighbor EVPN-OVERLAY-PEERS default-originate route-map RM-FOO always
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor EVPN-OVERLAY-PEERS missing-policy address-family all direction out action permit
   neighbor EVPN-OVERLAY-RS-PEERS peer group
   neighbor EVPN-OVERLAY-RS-PEERS remote-as 65001
   neighbor EVPN-OVERLAY-RS-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-RS-PEERS bfd
   neighbor EVPN-OVERLAY-RS-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-RS-PEERS password 7 <removed>
   neighbor EVPN-OVERLAY-RS-PEERS send-community
   neighbor EVPN-OVERLAY-RS-PEERS maximum-routes 0
   neighbor EXTENDED-COMMUNITY peer group
   neighbor EXTENDED-COMMUNITY send-community extended
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS remote-as 65001
   no neighbor IPv4-UNDERLAY-PEERS rib-in pre-policy retain
   neighbor IPv4-UNDERLAY-PEERS password 7 <removed>
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor IPV6-UNDERLAY peer group
   neighbor IPV6-UNDERLAY remote-as 65000
   neighbor IPV6-UNDERLAY password 7 <removed>
   neighbor IPV6-UNDERLAY send-community
   neighbor IPV6-UNDERLAY maximum-routes 12000
   neighbor IPV6-UNDERLAY-MLAG peer group
   neighbor IPV6-UNDERLAY-MLAG remote-as 65100
   neighbor IPV6-UNDERLAY-MLAG next-hop-self
   no neighbor IPV6-UNDERLAY-MLAG remove-private-as
   neighbor IPV6-UNDERLAY-MLAG password 7 <removed>
   neighbor IPV6-UNDERLAY-MLAG send-community
   neighbor IPV6-UNDERLAY-MLAG maximum-routes 12000
   neighbor IPV6-UNDERLAY-MLAG missing-policy address-family all include sub-route-map direction in action deny
   no neighbor IPV6-UNDERLAY-MLAG remove-private-as ingress
   neighbor LARGE-COMMUNITY peer group
   neighbor LARGE-COMMUNITY send-community large
   neighbor LOCAL-AS peer group
   neighbor LOCAL-AS local-as 65000 no-prepend replace-as
   neighbor MLAG-IPv4-UNDERLAY-PEER peer group
   neighbor MLAG-IPv4-UNDERLAY-PEER remote-as 65101
   neighbor MLAG-IPv4-UNDERLAY-PEER next-hop-self
   neighbor MLAG-IPv4-UNDERLAY-PEER remove-private-as all replace-as
   neighbor MLAG-IPv4-UNDERLAY-PEER route-map RM-MLAG-PEER-IN in
   neighbor MLAG-IPv4-UNDERLAY-PEER route-map RM-MLAG-PEER-OUT out
   neighbor MLAG-IPv4-UNDERLAY-PEER password 7 <removed>
   neighbor MLAG-IPv4-UNDERLAY-PEER send-community
   neighbor MLAG-IPv4-UNDERLAY-PEER maximum-routes 12000 warning-limit 80 percent warning-only
   neighbor MLAG-IPv4-UNDERLAY-PEER missing-policy address-family all direction in action deny
   neighbor MLAG-IPv4-UNDERLAY-PEER remove-private-as ingress replace-as
   neighbor MPLS-IBGP-PEERS peer group
   neighbor MPLS-IBGP-PEERS remote-as 65000
   neighbor MPLS-IBGP-PEERS local-as 65000 no-prepend replace-as
   neighbor MPLS-IBGP-PEERS password 7 <removed>
   neighbor MPLS-IBGP-PEERS send-community
   neighbor MPLS-IBGP-PEERS maximum-routes 0
   neighbor MULTIPLE-COMMUNITY peer group
   neighbor MULTIPLE-COMMUNITY send-community standard large
   neighbor NO-COMMUNITY peer group
   neighbor OBS_WAN peer group
   neighbor OBS_WAN remote-as 65000
   neighbor OBS_WAN as-path prepend-own disabled
   neighbor OBS_WAN as-path remote-as replace out
   neighbor OBS_WAN bfd
   neighbor OBS_WAN bfd interval 2000 min-rx 2000 multiplier 3
   neighbor OBS_WAN description BGP Connection to OBS WAN CPE
   neighbor PATH-SELECTION-PG-1 peer group
   neighbor PATH-SELECTION-PG-1 remote-as 65001
   neighbor PATH-SELECTION-PG-2 peer group
   neighbor PATH-SELECTION-PG-2 remote-as 65001
   neighbor PATH-SELECTION-PG-3 peer group
   neighbor PATH-SELECTION-PG-3 remote-as 65001
   neighbor PATH-SELECTION-PG-4 peer group
   neighbor PATH-SELECTION-PG-4 remote-as 65001
   neighbor PATH-SELECTION-PG-5 peer group
   neighbor PATH-SELECTION-PG-5 remote-as 65001
   neighbor PG-1 peer group
   neighbor PG-1 remote-as 65001.0002
   neighbor PG-2 peer group
   neighbor PG-2 remote-as 65001.0003
   neighbor SEDI peer group
   neighbor SEDI remote-as 65003
   neighbor SEDI update-source Loopback101
   neighbor SEDI description BGP Connection to OBS WAN CPE
   neighbor SEDI ebgp-multihop 10
   neighbor SEDI-shut peer group
   neighbor SEDI-shut shutdown
   neighbor SEDI-shut description BGP Peer Shutdown
   neighbor SR-TE-PG-1 peer group
   neighbor SR-TE-PG-1 remote-as 65000
   neighbor SR-TE-PG-2 peer group
   neighbor SR-TE-PG-2 remote-as 65000
   neighbor STARDARD-COMMUNITY peer group
   neighbor STARDARD-COMMUNITY send-community standard
   neighbor TEST peer group
   neighbor TEST ttl maximum-hops 42
   neighbor test-link-bandwidth1 peer group
   neighbor test-link-bandwidth1 ttl maximum-hops 1
   neighbor test-link-bandwidth1 missing-policy address-family all include community-list prefix-list direction in action deny
   neighbor test-link-bandwidth1 missing-policy address-family all include community-list direction out action permit
   neighbor test-link-bandwidth1 link-bandwidth default 100G
   neighbor test-link-bandwidth2 peer group
   neighbor test-link-bandwidth2 link-bandwidth
   neighbor test-passive peer group
   neighbor test-passive passive
   neighbor TEST-PASSIVE peer group
   neighbor TEST-PASSIVE remote-as 65003
   neighbor TEST-PASSIVE passive
   neighbor TEST-PASSIVE description BGP Connection in passive mode
   neighbor test-session-tracker peer group
   neighbor test-session-tracker session tracker ST2
   neighbor WELCOME_ROUTERS peer group
   neighbor WELCOME_ROUTERS remote-as 65001
   neighbor WELCOME_ROUTERS description BGP Connection to WELCOME ROUTER 02
   neighbor 1.1.1.1 remote-as 1
   neighbor 1.1.1.1 description TEST
   neighbor 1b11:3a00:22b0:0088::1 peer group IPV6-UNDERLAY
   neighbor 1b11:3a00:22b0:0088::3 peer group IPV6-UNDERLAY
   neighbor 1b11:3a00:22b0:0088::5 peer group IPV6-UNDERLAY
   neighbor 10.50.2.1 peer group IPV4-UNDERLAY
   neighbor 10.50.2.3 peer group IPV4-UNDERLAY
   neighbor 10.50.2.5 peer group IPV4-UNDERLAY
   neighbor 10.50.64.11 peer group EVPN-OVERLAY
   neighbor 10.50.64.12 peer group EVPN-OVERLAY
   neighbor 10.50.64.13 peer group EVPN-OVERLAY
   neighbor 169.254.252.1 peer group IPV4-UNDERLAY-MLAG
   neighbor 172.31.255.0 peer group IPv4-UNDERLAY-PEERS
   no neighbor 172.31.255.0 remove-private-as
   neighbor 172.31.255.0 weight 101
   neighbor 172.31.255.0 timers 1500 1500
   neighbor 172.31.255.0 password 7 <removed>
   no neighbor 172.31.255.0 remove-private-as ingress
   neighbor 172.31.255.4 peer group EVPN-OVERLAY-PEERS
   neighbor 172.31.255.4 allowas-in 5
   neighbor 172.31.255.4 rib-in pre-policy retain all
   neighbor 172.31.255.4 password shared-secret profile profile1 algorithm aes-128-cmac-96
   neighbor 192.0.3.1 remote-as 65432
   neighbor 192.0.3.1 as-path prepend-own disabled
   neighbor 192.0.3.1 as-path remote-as replace out
   neighbor 192.0.3.1 passive
   neighbor 192.0.3.1 bfd
   neighbor 192.0.3.1 bfd interval 2000 min-rx 2000 multiplier 3
   neighbor 192.0.3.1 rib-in pre-policy retain
   neighbor 192.0.3.1 session tracker ST1
   neighbor 192.0.3.1 default-originate always
   neighbor 192.0.3.1 send-community
   neighbor 192.0.3.1 link-bandwidth default 100G
   neighbor 192.0.3.2 remote-as 65433
   neighbor 192.0.3.2 rib-in pre-policy retain all
   neighbor 192.0.3.2 default-originate route-map RM-FOO-MATCH3
   neighbor 192.0.3.2 send-community extended
   neighbor 192.0.3.2 maximum-routes 10000
   neighbor 192.0.3.2 missing-policy address-family all include community-list prefix-list direction in action deny
   neighbor 192.0.3.2 missing-policy address-family all include community-list direction out action permit
   neighbor 192.0.3.2 link-bandwidth
   neighbor 192.0.3.3 remote-as 65434
   neighbor 192.0.3.3 rib-in pre-policy retain
   neighbor 192.0.3.3 send-community standard
   neighbor 192.0.3.3 missing-policy address-family all include community-list prefix-list sub-route-map direction in action deny
   neighbor 192.0.3.4 remote-as 65435
   no neighbor 192.0.3.4 rib-in pre-policy retain
   neighbor 192.0.3.4 ttl maximum-hops 1
   neighbor 192.0.3.4 send-community large
   neighbor 192.0.3.5 remote-as 65436
   neighbor 192.0.3.5 description test_ebgp_multihop
   neighbor 192.0.3.5 ebgp-multihop 2
   neighbor 192.0.3.5 send-community standard
   neighbor 192.0.3.5 maximum-routes 12000
   neighbor 192.0.3.6 remote-as 65437
   neighbor 192.0.3.6 remove-private-as
   neighbor 192.0.3.6 description test_remove_private_as
   no neighbor 192.0.3.6 route-reflector-client
   neighbor 192.0.3.6 remove-private-as ingress
   neighbor 192.0.3.7 remote-as 65438
   neighbor 192.0.3.7 remove-private-as all replace-as
   neighbor 192.0.3.7 description test_remove_private_as_all
   neighbor 192.0.3.7 route-reflector-client
   neighbor 192.0.3.7 remove-private-as ingress replace-as
   neighbor 192.0.3.8 peer group TEST
   neighbor 192.0.3.8 remote-as 65438
   neighbor 192.0.3.8 bfd
   neighbor 192.0.3.9 peer group TEST
   neighbor 192.0.3.9 remote-as 65438
   no neighbor 192.0.3.9 bfd
   neighbor 192.168.42.42 remote-as 65004
   neighbor 192.168.42.42 next-hop-self
   neighbor 192.168.251.1 shutdown
   neighbor 192.168.255.1 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.2 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.3 allowas-in 5
   neighbor 192.168.255.3 maximum-routes 52000 warning-limit 2000 warning-only
   neighbor 192.168.255.3 missing-policy address-family all direction in action deny
   neighbor 192.168.255.4 remote-as 65004
   neighbor 192.168.255.4 send-community
   neighbor 192.168.255.21 peer group EVPN-OVERLAY-PEERS
   no neighbor 192.168.255.21 rib-in pre-policy retain
   neighbor 192.168.255.21 missing-policy address-family all direction out action deny-in-out
   neighbor 192.168.255.101 peer group MPLS-IBGP-PEERS
   neighbor 192.168.255.201 peer group MPLS-IBGP-PEERS
   neighbor 2001:cafe:192:168::4 remote-as 65004
   neighbor 2001:cafe:192:168::4 send-community
   neighbor 2001:db8::dead:beef:cafe remote-as 65004
   neighbor fe80::b%Vl4094 peer group IPV6-UNDERLAY-MLAG
   no bgp redistribute-internal
   aggregate-address 1.1.1.0/24 advertise-only
   aggregate-address 1.12.1.0/24 as-set summary-only attribute-map RM-ATTRIBUTE match-map RM-MATCH advertise-only
   aggregate-address 2.2.1.0/24
   redistribute connected rcf Router_BGP_Connected()
   redistribute isis level-2 include leaked route-map RM_BGP_EVPN
   redistribute ospf match internal
   redistribute ospf match external
   redistribute ospf match nssa-external 1 include leaked route-map RM-REDISTRIBUTE-OSPF-NSSA-1
   redistribute ospfv3 include leaked route-map RM_BGP_EVPN
   redistribute ospfv3 match external include leaked route-map RM_BGP_EVPN
   redistribute ospfv3 match nssa-external 1 include leaked route-map RM_BGP_EVPN
   redistribute static include leaked rcf Router_BGP_Static()
   redistribute rip route-map RM_BGP_EVPN
   redistribute attached-host route-map RM_BGP_EVPN
   redistribute dynamic route-map RM_BGP_EVPN
   redistribute bgp leaked route-map RM-REDISTRIBUTE-BGP
   redistribute user rcf RCF_BGP_EVPN()
   neighbor interface Ethernet2 peer-group PG-FOO-v4 remote-as 65102
   neighbor interface Ethernet3 peer-group PG-FOO-v4 peer-filter PF-BAR-v4
   !
   vlan 24
      rd 10.50.64.15:10024
      route-target both 1:10024
      redistribute learned
   !
   vlan 41
      rd 10.50.64.15:10041
      route-target both 1:10041
      redistribute learned
   !
   vlan 42
      rd 10.50.64.15:10042
      route-target both 1:10042
      redistribute learned
   !
   vlan 65
      rd 10.50.64.15:10065
      route-target both 1:10065
      redistribute learned
   !
   vlan 66
      rd 145.245.21.0:66
      route-target export evpn domain all 145.245.21.0:66
      no redistribute learned
   !
   vlan 67
      rd 145.245.21.0:67
      route-target import 145.245.21.0:67
      no redistribute learned
   !
   vlan 600
      rd 145.245.21.0:600
      route-target import evpn domain all 145.245.21.0:600
      no redistribute learned
   !
   vlan 666
      rd 145.245.21.0:666
      route-target export 145.245.21.0:666
      no redistribute learned
   !
   vlan 2488
      rd 145.245.21.0:1
      route-target both 145.245.21.0:1
      no redistribute learned
   !
   vpws TENANT_A
      rd 100.70.0.2:1000
      route-target import export evpn 65000:1000
      mpls control-word
      label flow
      mtu 1600
      !
      pseudowire TEN_A_site1_site3_pw
         evpn vpws id local 15 remote 35
      !
      pseudowire TEN_A_site2_site5_pw
         evpn vpws id local 25 remote 57
   !
   vpws TENANT_B
      rd 100.70.0.2:2000
      route-target import export evpn 65000:2000
      !
      pseudowire TEN_B_site2_site5_pw
         evpn vpws id local 26 remote 58
   !
   vlan-aware-bundle B-ELAN-201
      rd 192.168.255.3:20201
      route-target export 20201:20201
      redistribute learned
      no redistribute host-route
      vlan 201
   !
   vlan-aware-bundle TENANT_A_PROJECT01
      rd 192.168.255.3:11
      route-target both 11:11
      route-target import export evpn domain remote 2:11
      redistribute igmp
      redistribute learned
      no redistribute static
      vlan 110
   !
   vlan-aware-bundle TENANT_A_PROJECT02
      rd 192.168.255.3:12
      rd evpn domain remote 192.168.255.3:12
      route-target import 12:12
      route-target import evpn domain remote 2:12
      route-target export evpn domain remote 2:12
      redistribute learned
      vlan 112
   !
   address-family evpn
      route export ethernet-segment ip mass-withdraw
      route import ethernet-segment ip mass-withdraw
      bgp additional-paths receive
      bgp additional-paths send limit 10
      bgp next-hop-unchanged
      neighbor default encapsulation mpls next-hop-self source-interface Loopback0
      next-hop mpls resolution ribs tunnel-rib colored system-colored-tunnel-rib tunnel-rib test-rib system-connected
      neighbor ADDITIONAL-PATH-PG-1 activate
      neighbor ADDITIONAL-PATH-PG-1 additional-paths receive
      neighbor ADDITIONAL-PATH-PG-1 default-route rcf DEFAULT_ROUTE_RCF()
      neighbor ADDITIONAL-PATH-PG-1 additional-paths send any
      neighbor ADDITIONAL-PATH-PG-2 activate
      neighbor ADDITIONAL-PATH-PG-2 default-route route-map DEFAULT_ROUTE_RM
      neighbor ADDITIONAL-PATH-PG-2 additional-paths send backup
      neighbor ADDITIONAL-PATH-PG-3 activate
      neighbor ADDITIONAL-PATH-PG-3 additional-paths send ecmp
      neighbor ADDITIONAL-PATH-PG-4 activate
      neighbor ADDITIONAL-PATH-PG-4 additional-paths send ecmp limit 42
      neighbor ADDITIONAL-PATH-PG-5 activate
      neighbor ADDITIONAL-PATH-PG-5 additional-paths send limit 42
      neighbor ADDITIONAL-PATH-PG-6 activate
      no neighbor ADDITIONAL-PATH-PG-6 additional-paths send
      neighbor EVPN-OVERLAY activate
      neighbor EVPN-OVERLAY route-map RM-HIDE-AS-PATH in
      neighbor EVPN-OVERLAY route-map RM-HIDE-AS-PATH out
      neighbor EVPN-OVERLAY-PEERS activate
      neighbor EVPN-OVERLAY-PEERS default-route
      neighbor EVPN-OVERLAY-PEERS encapsulation vxlan
      neighbor EVPN-OVERLAY-PEERS domain remote
      no neighbor IPv4-UNDERLAY-PEERS activate
      no neighbor MLAG-IPv4-UNDERLAY-PEER activate
      neighbor RCF_TEST rcf in Address_Family_EVPN_In()
      neighbor RCF_TEST rcf out Address_Family_EVPN_Out()
      neighbor TEST-ENCAPSULATION activate
      neighbor TEST-ENCAPSULATION encapsulation mpls
      neighbor TEST-ENCAPSULATION-2 activate
      neighbor TEST-ENCAPSULATION-2 encapsulation path-selection
      neighbor 10.100.100.1 activate
      neighbor 10.100.100.1 additional-paths receive
      neighbor 10.100.100.1 default-route
      neighbor 10.100.100.1 additional-paths send any
      neighbor 10.100.100.2 activate
      neighbor 10.100.100.2 default-route route-map RM_DEFAULT_ROUTE
      no neighbor 10.100.100.2 additional-paths send
      neighbor 10.100.100.3 activate
      neighbor 10.100.100.3 default-route rcf RCF_DEFAULT_ROUTE()
      neighbor 10.100.100.3 additional-paths send ecmp limit 11
      neighbor 10.100.100.4 activate
      neighbor 10.100.100.4 route-map RM1 in
      neighbor 10.100.100.4 route-map RM2 out
      neighbor 10.100.100.4 additional-paths send limit 9
      neighbor 10.100.100.4 encapsulation path-selection
      neighbor 10.100.100.5 activate
      neighbor 10.100.100.5 encapsulation mpls
      no neighbor 192.168.255.3 activate
      neighbor 192.168.255.4 rcf in Address_Family_EVPN_In()
      neighbor 192.168.255.4 rcf out Address_Family_EVPN_Out()
      neighbor 192.168.255.4 encapsulation mpls next-hop-self source-interface Ethernet1
      domain identifier 65101:0
      domain identifier 65101:1 remote
      next-hop resolution disabled
      route import match-failure action discard
      host-flap detection window 10 threshold 1 expiry timeout 3 seconds
      layer-2 fec in-place update timeout 100 seconds
      route import overlay-index gateway
      !
      evpn ethernet-segment domain local
         identifier 0011:1111:1111:1111:1111
         route-target import 11:11:11:11:11:11
      !
      evpn ethernet-segment domain remote
         identifier 0022:2222:2222:2222:2222
         route-target import 22:22:22:22:22:22
   !
   address-family flow-spec ipv4
      bgp missing-policy direction in action deny-in-out
      bgp missing-policy direction out action deny
      neighbor FOOBAR activate
      no neighbor IPv4_SEC activate
      neighbor 192.168.66.22 activate
   !
   address-family flow-spec ipv6
      bgp missing-policy direction in action deny
      bgp missing-policy direction out action permit
      no neighbor FOOBAR activate
      neighbor IPv6_SEC activate
      neighbor 192.168.66.21 activate
   !
   address-family ipv4
      bgp additional-paths install
      bgp additional-paths receive
      bgp additional-paths send ecmp limit 20
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor foo additional-paths receive
      neighbor foo prefix-list PL-BAR-v4-IN in
      neighbor foo prefix-list PL-BAR-v4-OUT out
      neighbor foo default-originate route-map RM-FOO-MATCH always
      neighbor foo additional-paths send ecmp limit 20 prefix-list PL1
      neighbor FOOBAR activate
      neighbor FOOBAR next-hop address-family ipv6 originate
      neighbor IPV4-UNDERLAY activate
      neighbor IPV4-UNDERLAY route-map RM-HIDE-AS-PATH in
      neighbor IPV4-UNDERLAY route-map RM-HIDE-AS-PATH out
      no neighbor IPV4-UNDERLAY additional-paths send
      neighbor IPv4-UNDERLAY-PEERS activate
      neighbor MLAG-IPv4-UNDERLAY-PEER activate
      neighbor OBS_WAN activate
      neighbor OBS_WAN additional-paths send limit 8
      neighbor SEDI activate
      neighbor SEDI route-map RM-BGP-EXPORT-DEFAULT-BLUE-C1 out
      neighbor SEDI-shut activate
      neighbor SEDI-shut route-map RM-BGP-EXPORT-DEFAULT-BLUE-C1 out
      neighbor TEST_PEER_GRP activate
      neighbor TEST_PEER_GRP next-hop address-family ipv6 originate
      neighbor TEST_RCF rcf in Address_Family_IPV4_In()
      neighbor TEST_RCF rcf out Address_Family_IPV4_Out()
      neighbor WELCOME_ROUTERS activate
      neighbor WELCOME_ROUTERS additional-paths send any
      neighbor 10.2.3.8 rcf in Address_Family_IPV4_In()
      no neighbor 10.2.3.8 additional-paths send
      neighbor 10.2.3.9 rcf out Address_Family_IPV4_Out()
      neighbor 10.2.3.9 default-originate route-map Address_Family_IPV4 always
      neighbor 10.2.3.9 additional-paths send ecmp limit 4
      neighbor 192.0.2.1 additional-paths receive
      neighbor 192.0.2.1 route-map Address_Family_IPV4_In in
      neighbor 192.0.2.1 route-map Address_Family_IPV4_Out out
      neighbor 192.0.2.1 prefix-list PL-FOO-v4-IN in
      neighbor 192.0.2.1 prefix-list PL-FOO-v4-OUT out
      neighbor 192.0.2.1 additional-paths send limit 20 prefix-list PL1
      no neighbor 192.168.66.21 activate
      neighbor 192.168.66.21 additional-paths send any
      network 10.0.0.0/8
      network 172.16.0.0/12
      network 192.168.0.0/16 route-map RM-FOO-MATCH
      redistribute attached-host route-map RM_BGP_EVPN_IPV4
      redistribute bgp leaked route-map RM_BGP_EVPN_IPV4
      redistribute connected include leaked rcf Address_Family_IPV4_Connected()
      redistribute dynamic route-map Address_Family_IPV4_Dynamic_RM
      redistribute user rcf RCF_BGP_EVPN_IPV4()
      redistribute isis level-1 include leaked route-map RM_BGP_EVPN_IPV4
      redistribute ospf match internal include leaked route-map RM_BGP_EVPN_IPV4
      redistribute ospfv3 include leaked route-map RM_BGP_EVPN_IPV4
      redistribute ospfv3 match external include leaked route-map RM_BGP_EVPN_IPV4
      redistribute ospfv3 match nssa-external 2 include leaked route-map RM_BGP_EVPN_IPV4
      redistribute ospf match external include leaked route-map RM-REDISTRIBUTE-OSPF-EXTERNAL
      redistribute ospf match nssa-external
      redistribute rip route-map RM_BGP_EVPN_IPV4
      redistribute static rcf Address_Family_IPV4_Static()
   !
   address-family ipv4 labeled-unicast
      update wait-for-convergence
      bgp missing-policy include community-list prefix-list sub-route-map direction in action deny
      bgp additional-paths receive
      bgp additional-paths send ecmp limit 20
      bgp next-hop-unchanged
      next-hop resolution ribs tunnel-rib colored system-colored-tunnel-rib tunnel-rib test-rib system-connected
      neighbor PG-BGP-LU activate
      neighbor PG-BGP-LU route-map RM_BGP_LU_IN in
      neighbor PG-BGP-LU route-map RM_BGP_LU_OUT out
      neighbor PG-BGP-LU additional-paths send ecmp limit 10
      neighbor PG-BGP-LU next-hop-unchanged
      neighbor PG-BGP-LU maximum-advertised-routes 120000 warning-limit 1000
      neighbor PG-BGP-LU missing-policy include community-list prefix-list sub-route-map direction in action deny
      neighbor PG-BGP-LU aigp-session
      neighbor PG-BGP-LU multi-path
      no neighbor PG-BGP-LU1 activate
      neighbor PG-BGP-LU1 additional-paths receive
      neighbor PG-BGP-LU1 graceful-restart-helper stale-route route-map RM_BGP_LU_TEST
      neighbor PG-BGP-LU1 rcf in RCF_BGP_LU_IN()
      neighbor PG-BGP-LU1 rcf out RCF_BGP_LU_OUT()
      no neighbor PG-BGP-LU1 additional-paths send
      neighbor PG-BGP-LU1 next-hop-self
      no neighbor PG-BGP-LU2 activate
      neighbor PG-BGP-LU2 additional-paths send any
      neighbor PG-BGP-LU2 next-hop-self v4-mapped-v6 source-interface Ethernet1
      no neighbor PG-BGP-LU3 activate
      neighbor PG-BGP-LU3 next-hop-self source-interface Ethernet2
      no neighbor 192.168.66.21 activate
      neighbor 192.168.66.21 additional-paths send limit 11
      no neighbor 192.168.66.22 activate
      no neighbor 192.168.66.22 additional-paths send
      neighbor 198.51.100.1 activate
      neighbor 198.51.100.1 additional-paths receive
      neighbor 198.51.100.1 rcf in RCF_TEST()
      neighbor 198.51.100.1 rcf out RCF_TEST_OUT()
      neighbor 198.51.100.1 additional-paths send ecmp limit 11
      neighbor 198.51.100.1 next-hop-self
      neighbor 198.51.100.1 next-hop-self v4-mapped-v6 source-interface Ethernet1
      neighbor 198.51.100.1 maximum-advertised-routes 120000 warning-limit 1000
      no neighbor 198.51.100.2 activate
      neighbor 198.51.100.2 graceful-restart-helper stale-route route-map RM_STALE
      neighbor 198.51.100.2 route-map RM_IN_TEST in
      neighbor 198.51.100.2 route-map RM_OUT_TEST out
      neighbor 198.51.100.2 additional-paths send any
      neighbor 198.51.100.2 next-hop-unchanged
      neighbor 198.51.100.2 next-hop-self source-interface Ethernet2
      neighbor 198.51.100.2 missing-policy  include community-list prefix-list sub-route-map direction in action deny
      neighbor 198.51.100.2 aigp-session
      neighbor 198.51.100.2 multi-path
      network 203.0.113.0/25 route-map RM-TEST
      network 203.0.113.128/25
      next-hop 192.51.100.1 originate lfib-backup ip-forwarding
      lfib entry installation skipped
      label local-termination implicit-null
      tunnel source-protocol isis segment-routing
      tunnel source-protocol ldp rcf TEST()
      aigp-session confederation
      aigp-session ebgp
   !
   address-family ipv4 multicast
      bgp additional-paths receive
      neighbor FOOBAR activate
      neighbor FOOBAR additional-paths receive
      no neighbor IPV4-MULTICAST-INACTIVE activate
      neighbor IPV4-UNDERLAY activate
      neighbor IPV4-UNDERLAY route-map IPV4-MULTICAST-RM-IN in
      neighbor IPV4-UNDERLAY route-map IPV4-MULTICAST-RM-OUT out
      neighbor IPV4-UNDERLAY-MLAG activate
      neighbor 10.1.1.1 activate
      neighbor 10.1.1.1 additional-paths receive
      neighbor 10.1.1.1 route-map IPV4-MULTICAST-RM-IN in
      neighbor 10.1.1.1 route-map IPV4-MULTICAST-RM-OUT out
      no neighbor 10.1.1.2 activate
      redistribute attached-host route-map AFIPV4M_ATTACHED_HOST
      redistribute connected route-map AFIPV4M_CONNECTED
      redistribute isis level-1-2 include leaked route-map AFIPV4M_ISIS
      redistribute ospf route-map RM_BGP_EVPN_IPV4M
      redistribute ospfv3 match internal route-map RM_BGP_EVPN_IPV4M
      redistribute ospfv3 match external route-map RM_BGP_EVPN_IPV4M
      redistribute ospfv3 match nssa-external 1 route-map RM_BGP_EVPN_IPV4M
      redistribute ospf match nssa-external route-map AFIPV4M_OSPF_NSSA
      redistribute static route-map AFIPV4M_STATIC
   !
   address-family ipv4 sr-te
      neighbor SR-TE-PG-1 activate
      neighbor SR-TE-PG-1 route-map RM-SR-TE-PEER-IN4 in
      neighbor SR-TE-PG-1 route-map RM-SR-TE-PEER-OUT4 out
      no neighbor SR-TE-PG-2 activate
      neighbor 192.168.42.42 activate
      neighbor 192.168.42.42 route-map RM-SR-TE-PEER-IN4 in
      neighbor 192.168.42.42 route-map RM-SR-TE-PEER-OUT4 out
      no neighbor 192.168.42.43 activate
   !
   address-family ipv6
      bgp additional-paths install ecmp-primary
      bgp additional-paths receive
      bgp additional-paths send any
      neighbor baz additional-paths receive
      neighbor baz prefix-list PL-BAR-v6-IN in
      neighbor baz prefix-list PL-BAR-v6-OUT out
      neighbor baz additional-paths send ecmp limit 20
      no neighbor FOOBAR activate
      neighbor IPV6-UNDERLAY activate
      neighbor IPV6-UNDERLAY route-map RM-HIDE-AS-PATH in
      neighbor IPV6-UNDERLAY route-map RM-HIDE-AS-PATH out
      neighbor IPV6-UNDERLAY additional-paths send any
      neighbor IPV6-UNDERLAY-MLAG activate
      no neighbor IPV6-UNDERLAY-MLAG additional-paths send
      neighbor TEST_RCF rcf in Address_Family_IPV6_In()
      neighbor TEST_RCF rcf out Address_Family_IPV6_Out()
      neighbor TEST_RCF additional-paths send limit 11
      neighbor 2001:db8::1 additional-paths receive
      neighbor 2001:db8::1 route-map Address_Family_IPV6_In in
      neighbor 2001:db8::1 route-map Address_Family_IPV6_Out out
      neighbor 2001:db8::1 prefix-list PL-FOO-v6-IN in
      neighbor 2001:db8::1 prefix-list PL-FOO-v6-OUT out
      neighbor 2001:db8::1 additional-paths send ecmp limit 20
      neighbor 2001:db8::2 activate
      neighbor 2001:db8::2 rcf in Address_Family_IPV6_In()
      neighbor 2001:db8::2 rcf out Address_Family_IPV6_Out()
      neighbor 2001:db8::2 additional-paths send any
      no neighbor 2001:db8::21 activate
      no neighbor 2001:db8::21 additional-paths send
      neighbor 2001:db8::22 additional-paths send limit 5
      network 2001:db8:100::/40
      network 2001:db8:200::/40 route-map RM-BAR-MATCH
      redistribute attached-host
      redistribute bgp leaked route-map RM-REDISTRIBUTE-BGP
      redistribute dhcp
      redistribute connected include leaked rcf Address_Family_IPV6_Connected()
      redistribute dynamic route-map RM-REDISTRIBUTE-DYNAMIC
      redistribute user
      redistribute isis level-1-2 rcf RCF_Address_Family_IPV6_ISIS()
      redistribute ospfv3
      redistribute ospfv3 match external include leaked
      redistribute ospfv3 match nssa-external 1
      redistribute static route-map RM-IPV6-STATIC-TO-BGP
   !
   address-family ipv6 multicast
      bgp missing-policy direction in action permit
      bgp missing-policy direction out action permit
      bgp additional-paths receive
      no neighbor FOOBAR activate
      neighbor FOOBAR additional-paths receive
      neighbor FOOBAR1 activate
      neighbor aa::1 activate
      neighbor aa::1 additional-paths receive
      neighbor aa::1 route-map IPv6_MULTICAST_RM_IN in
      neighbor aa::1 route-map IPv6_MULTICAST_RM_OUT out
      network aa::1/126 route-map IPv6_MULTICAST_RM
      redistribute connected route-map RM-address_family_ipv6_multicast-Connected
      redistribute isis level-1 include leaked route-map RM-address_family_ipv6_multicast-ISIS
      redistribute ospf route-map RM-address_family_ipv6_multicast-OSPF
      redistribute ospfv3 route-map RM-address_family_ipv6_multicast-OSPFv3
      redistribute ospfv3 match external route-map RM-address_family_ipv6_multicast-OSPFv3-External
      redistribute ospfv3 match nssa-external 2 route-map RM-address_family_ipv6_multicast-OSPFv3-External
      redistribute ospf match external route-map RM-address_family_ipv6_multicast-OSPF-External
      redistribute ospf match nssa-external 2 route-map RM-address_family_ipv6_multicast-OSPF-External
      redistribute static route-map RM-address_family_ipv6_multicast-Static
   !
   address-family ipv6 sr-te
      neighbor SR-TE-PG-2 activate
      neighbor SR-TE-PG-2 route-map RM-SR-TE-PEER-IN6 in
      neighbor SR-TE-PG-2 route-map RM-SR-TE-PEER-OUT6 out
      no neighbor SR-TE-PG-3 activate
      neighbor 2001:db8::dead:beef:cafe activate
      neighbor 2001:db8::dead:beef:cafe route-map RM-SR-TE-PEER-IN6 in
      neighbor 2001:db8::dead:beef:cafe route-map RM-SR-TE-PEER-OUT6 out
      no neighbor 2002:db8::dead:beef:cafe activate
   !
   address-family link-state
      bgp missing-policy direction in action permit
      bgp missing-policy direction out action deny
      neighbor PG-1 activate
      neighbor PG-1 missing-policy direction in action deny-in-out
      neighbor PG-1 missing-policy direction out action permit
      no neighbor PG-2 activate
      neighbor 192.168.255.1 activate
      neighbor 192.168.255.1 missing-policy direction in action deny
      neighbor 192.168.255.1 missing-policy direction out action deny
      neighbor 192.168.255.2 activate
      path-selection
      path-selection role consumer propagator
   !
   address-family path-selection
      bgp additional-paths receive
      bgp additional-paths send ecmp limit 42
      neighbor PATH-SELECTION-PG-1 activate
      neighbor PATH-SELECTION-PG-1 additional-paths receive
      no neighbor PATH-SELECTION-PG-1 send
      neighbor PATH-SELECTION-PG-2 activate
      neighbor PATH-SELECTION-PG-2 additional-paths send backup
      neighbor PATH-SELECTION-PG-3 activate
      neighbor PATH-SELECTION-PG-3 additional-paths send ecmp
      neighbor PATH-SELECTION-PG-4 activate
      neighbor PATH-SELECTION-PG-4 additional-paths send ecmp limit 42
      no neighbor PATH-SELECTION-PG-5 activate
      neighbor PATH-SELECTION-PG-5 additional-paths send limit 42
      neighbor 172.31.255.0 activate
      neighbor 172.31.255.0 additional-paths receive
      neighbor 172.31.255.0 additional-paths send any
      neighbor 172.31.255.1 activate
      no neighbor 172.31.255.1 additional-paths send
      neighbor 172.31.255.2 activate
      neighbor 172.31.255.2 additional-paths send ecmp
      neighbor 172.31.255.3 activate
      neighbor 172.31.255.3 additional-paths send ecmp limit 42
      no neighbor 172.31.255.4 activate
      neighbor 172.31.255.4 additional-paths send limit 42
   !
   address-family rt-membership
      neighbor EVPN-OVERLAY-PEERS activate
      neighbor EVPN-OVERLAY-PEERS default-route-target
      neighbor EVPN-OVERLAY-RS-PEERS activate
      neighbor EVPN-OVERLAY-RS-PEERS default-route-target only
      neighbor EVPN-OVERLAY-RS-PEERS default-route-target encoding origin-as omit
      no neighbor RTC-INACTIVE-PEERS activate
   !
   address-family vpn-ipv4
      neighbor MPLS-IBGP-PEERS activate
      neighbor MPLS-IBGP-PEERS route-map RM-IBGP-PEER-IN4 in
      neighbor MPLS-IBGP-PEERS route-map RM-IBGP-PEER-OUT4 out
      neighbor MPLS-IBGP-PEERS default-route route-map RM-IBGP-PEER-IN4
      no neighbor Test_RCF activate
      neighbor Test_RCF rcf in Address_Family_VPN_IPV4_In()
      neighbor Test_RCF rcf out Address_Family_VPN_IPV4_Out()
      neighbor Test_RCF default-route rcf Address_Family_VPN_IPV4_In()
      neighbor 192.168.255.4 activate
      neighbor 192.168.255.4 route-map RM-NEIGHBOR-PEER-IN4 in
      neighbor 192.168.255.4 route-map RM-NEIGHBOR-PEER-OUT4 out
      neighbor 192.168.255.4 default-route route-map RM-NEIGHBOR-PEER-IN4
      no neighbor 192.168.255.5 activate
      neighbor 192.168.255.5 rcf in Address_Family_VPN_IPV4_In()
      neighbor 192.168.255.5 rcf out Address_Family_VPN_IPV4_Out()
      neighbor 192.168.255.5 default-route rcf Address_Family_VPN_IPV4_In()
      neighbor default encapsulation mpls next-hop-self source-interface Loopback0
      domain identifier 65000:0
      route import match-failure action discard
   !
   address-family vpn-ipv6
      neighbor MPLS-IBGP-PEERS activate
      neighbor MPLS-IBGP-PEERS route-map RM-IBGP-PEER-IN6 in
      neighbor MPLS-IBGP-PEERS route-map RM-IBGP-PEER-OUT6 out
      neighbor MPLS-IBGP-PEERS default-route route-map RM-IBGP-PEER-OUT6
      no neighbor Test_RCF activate
      neighbor Test_RCF rcf in Address_Family_VPN_IPV6_In()
      neighbor Test_RCF rcf out Address_Family_VPN_IPV6_Out()
      neighbor Test_RCF default-route rcf Address_Family_VPN_IPV6_Out()
      neighbor 2001:cafe:192:168::4 activate
      neighbor 2001:cafe:192:168::4 route-map RM-NEIGHBOR-PEER-IN6 in
      neighbor 2001:cafe:192:168::4 route-map RM-NEIGHBOR-PEER-OUT6 out
      neighbor 2001:cafe:192:168::4 default-route route-map RM-NEIGHBOR-PEER-IN6
      no neighbor 2001:cafe:192:168::5 activate
      neighbor 2001:cafe:192:168::5 rcf in Address_Family_VPN_IPV6_In()
      neighbor 2001:cafe:192:168::5 rcf out Address_Family_VPN_IPV6_Out()
      neighbor 2001:cafe:192:168::5 default-route rcf Address_Family_VPN_IPV6_In()
      neighbor default encapsulation mpls next-hop-self source-interface Loopback0
      domain identifier 65000:0
      route import match-failure action discard
   !
   vrf BLUE-C1
      rd 1.0.1.1:101
      no bgp additional-paths send
      neighbor 10.1.1.0 peer group OBS_WAN
      neighbor 10.1.1.0 as-path prepend-own disabled
      no neighbor 10.1.1.0 route-reflector-client
      neighbor 10.255.1.1 peer group WELCOME_ROUTERS
      neighbor 10.255.1.1 as-path remote-as replace out
      neighbor 10.255.1.1 weight 65535
      neighbor 10.255.1.1 route-reflector-client
      neighbor 101.0.3.1 peer group SEDI
      neighbor 101.0.3.1 weight 100
      neighbor 101.0.3.2 peer group SEDI
      neighbor 101.0.3.2 shutdown
      neighbor 101.0.3.2 allowas-in
      neighbor 101.0.3.3 peer group SEDI-shut
      neighbor 101.0.3.3 allowas-in 5
      neighbor 101.0.3.4 peer group TEST-PASSIVE
      neighbor 101.0.3.5 peer group WELCOME_ROUTERS
      neighbor 101.0.3.5 passive
      no neighbor 101.0.3.5 bfd
      neighbor 101.0.3.6 peer group WELCOME_ROUTERS
      neighbor 101.0.3.6 bfd
      neighbor 101.0.3.6 bfd interval 2500 min-rx 2000 multiplier 3
      neighbor 101.0.3.7 bfd
      aggregate-address 0.0.0.0/0 as-set summary-only attribute-map RM-BGP-AGG-APPLY-SET advertise-only
      aggregate-address 193.1.0.0/16 as-set summary-only attribute-map RM-BGP-AGG-APPLY-SET match-map VRF-MATCH-MAP
      redistribute ospf include leaked
      redistribute static rcf VRF_STATIC_RCF()
      !
      comment
      Comment created from eos_cli under router_bgp.vrfs.BLUE-C1
      EOF

   !
   vrf RED-C1
      rd 1.0.1.1:102
      neighbor 10.1.1.0 peer group OBS_WAN
      no neighbor 10.1.1.0 remove-private-as
      !
      address-family ipv4
         neighbor 10.1.1.0 prefix-list PL-BGP-DEFAULT-RED-IN-C1 in
         neighbor 10.1.1.0 prefix-list PL-BGP-DEFAULT-RED-OUT-C1 out
      !
      address-family ipv6
         neighbor 2001:cafe:192:168::4 prefix-list PL-BGP-V6-RED-IN-C1 in
         neighbor 2001:cafe:192:168::4 prefix-list PL-BGP-V6-RED-OUT-C1 out
   !
   vrf Tenant_A
      rd 10.50.64.15:30001
      route-target import evpn 1:30001
      route-target import evpn route-map RM-DENY-DEFAULT
      route-target import vpn-ipv4 1:30011
      route-target import vpn-ipv4 rcf RT_IMPORT_AF_RCF() vpn-route filter-rcf RT_IMPORT_AF_RCF_FILTER()
      route-target import vpn-ipv4 route-map RT_IMPORT_AF_RM
      route-target import vpn-ipv6 1:30011
      route-target import vpn-ipv6 rcf RT_IMPORT_AF_RCF()
      route-target import vpn-ipv6 route-map RT_IMPORT_AF_RM
      route-target export evpn 1:30001
      route-target export evpn rcf RT_EXPORT_AF_RCF()
      route-target export vpn-ipv6 1:30011
      route-target export vpn-ipv6 rcf RT_IMPORT_AF_RCF() vpn-route filter-rcf RT_IMPORT_AF_RCF_FILTER()
      route-target export vpn-ipv6 route-map RT_IMPORT_AF_RM
      redistribute connected
      redistribute ospf match external include leaked
      redistribute ospfv3
      redistribute ospfv3 match nssa-external
   !
   vrf TENANT_A_PROJECT01
      rd 192.168.255.3:11
      route-target import evpn 11:11
      route-target import evpn rcf RT_IMPORT_AF_RCF()
      route-target export evpn 11:11
      route-target export evpn rcf RT_EXPORT_AF_RCF()
      router-id 192.168.255.3
      update wait-for-convergence
      update wait-install
      neighbor 10.2.3.4 remote-as 1234
      neighbor 10.2.3.4 remove-private-as all replace-as
      neighbor 10.2.3.4 local-as 123 no-prepend replace-as
      neighbor 10.2.3.4 description Tenant A BGP Peer
      neighbor 10.2.3.4 ebgp-multihop 3
      neighbor 10.2.3.4 route-map RM-10.2.3.4-SET-NEXT-HOP-OUT out
      neighbor 10.2.3.4 default-originate route-map RM-10.2.3.4-SET-NEXT-HOP-OUT always
      neighbor 10.2.3.4 send-community
      neighbor 10.2.3.4 maximum-routes 0 warning-limit 100 warning-only
      neighbor 10.255.251.1 peer group MLAG-IPv4-UNDERLAY-PEER
      neighbor 10.255.251.1 remove-private-as ingress replace-as
      network 10.0.0.0/8 route-map VRF-RM
      network 100.64.0.0/10
      redistribute connected
      redistribute static
      !
      address-family ipv4
         bgp additional-paths install
         bgp missing-policy direction in action permit
         bgp missing-policy direction out action deny
         bgp additional-paths receive
         bgp additional-paths send ecmp
         neighbor 10.2.3.4 activate
         neighbor 10.2.3.5 activate
         neighbor 10.2.3.5 route-map RM-10.2.3.5-SET-NEXT-HOP-IN in
         neighbor 10.2.3.6 next-hop address-family ipv6
         neighbor 10.2.3.7 next-hop address-family ipv6 originate
         no neighbor 10.2.3.8 next-hop address-family ipv6
         neighbor 10.2.3.9 activate
         neighbor 10.2.3.9 rcf in VRF_AFIPV4_RCF_IN()
         neighbor 10.2.3.10 activate
         neighbor 10.2.3.10 rcf out VRF_AFIPV4_RCF_OUT()
         network 10.0.0.0/8
         network 100.64.0.0/10 route-map RM-10.2.3.4
         redistribute connected rcf VRF_AFIPV4_RCF_CONNECTED()
         redistribute static route-map VRF_AFIPV4_RM_STATIC
   !
   vrf TENANT_A_PROJECT02
      rd 192.168.255.3:12
      route-target import evpn 12:12
      route-target export evpn 12:12
      router-id 192.168.255.3
      timers bgp 5 15
      neighbor 10.255.251.1 peer group MLAG-IPv4-UNDERLAY-PEER
      neighbor 10.255.251.1 next-hop-self
      neighbor 10.255.251.1 description ABCDEFG
      neighbor 10.255.251.1 timers 1 3
      neighbor 10.255.251.1 send-community standard
      neighbor 10.255.251.2 peer group MLAG-IPv4-UNDERLAY-PEER
      neighbor 10.255.251.2 description ABCDEFGfg
      neighbor 10.255.251.2 timers 1 3
      neighbor 10.255.251.2 send-community extended
      neighbor 10.255.251.3 peer group MLAG-IPv4-UNDERLAY-PEER
      neighbor 10.255.251.3 next-hop-self
      neighbor 10.255.251.3 description ABCDEFGfgLCLCLCLC
      neighbor 10.255.251.3 timers 1 3
      neighbor 10.255.251.3 default-originate always
      neighbor 10.255.251.3 send-community large
      neighbor 10.255.251.4 peer group MLAG-IPv4-UNDERLAY-PEER
      neighbor 10.255.251.4 bfd
      neighbor 10.255.251.4 description Test_Bfd
      redistribute connected
      redistribute static route-map RM-CONN-2-BGP
   !
   vrf TENANT_A_PROJECT03
      rd 192.168.255.3:13
      default-route export evpn always route-map TENANT_A_PROJECT03_RM_DEFAULT
      route-target import evpn 13:13
      route-target export evpn 13:13
      router-id 192.168.255.3
      evpn multicast
         address-family ipv4
            transit
   !
   vrf TENANT_A_PROJECT04
      rd 192.168.255.3:14
      default-route export evpn rcf TENANT_A_PROJECT03_RCF_DEFAULT()
      route-target import evpn 14:14
      route-target export evpn 14:14
      router-id 192.168.255.3
      evpn multicast
   !
   vrf Tenant_B
      rd 10.50.64.15:30002
      route-target import evpn 1:30002
      route-target export evpn 1:30002
      route-target export evpn route-map RM-DEFAULT-EXTRA-COMM
   !
   vrf VRF01
      bgp additional-paths install
      bgp additional-paths receive
      bgp additional-paths send any
      redistribute connected include leaked rcf RCF_VRF_CONNECTED()
      redistribute isis level-2 rcf RCF_VRF_ISIS()
      redistribute ospf match internal include leaked route-map RM_VRF_OSPF
      redistribute ospf match external include leaked route-map RM_VRF_OSPF
      redistribute ospf match nssa-external 1 include leaked route-map RM_VRF_OSPF
      redistribute ospfv3 match internal include leaked route-map RM_VRF_OSPF
      redistribute static route-map RM_VRF_STATIC
      redistribute rip route-map RM_VRF_RIP
      redistribute attached-host route-map RM_VRF_ATTACHED-HOST
      redistribute bgp leaked route-map RM_VRF_BGP
      redistribute user rcf RCF_VRF_USER()
      !
      address-family flow-spec ipv4
         bgp missing-policy direction in action permit
         bgp missing-policy direction out action permit
         neighbor 1.2.3.4 activate
      !
      address-family flow-spec ipv6
         bgp missing-policy direction in action permit
         bgp missing-policy direction out action deny
         neighbor aa::1 activate
      !
      address-family ipv4
         bgp additional-paths install ecmp-primary
         bgp missing-policy direction in action deny
         bgp missing-policy direction out action permit
         bgp additional-paths receive
         bgp additional-paths send ecmp limit 4
         neighbor 1.2.3.4 activate
         neighbor 1.2.3.4 additional-paths receive
         neighbor 1.2.3.4 route-map FOO in
         neighbor 1.2.3.4 route-map BAR out
         neighbor 1.2.3.4 additional-paths send any
         network 2.3.4.0/24 route-map BARFOO
         redistribute attached-host route-map VRF_AFIPV4_RM_HOST
         redistribute bgp leaked route-map VRF_AFIPV4_RM_BGP
         redistribute connected include leaked rcf VRF_AFIPV4_RCF_CONNECTED_1()
         redistribute dynamic route-map VRF_AFIPV4_RM_DYNAMIC
         redistribute user rcf VRF_AFIPV4_RCF_USER()
         redistribute isis level-1 include leaked rcf VRF_AFIPV4_RCF_ISIS()
         redistribute ospf include leaked route-map VRF_AFIPV4_RM_OSPF
         redistribute ospfv3 match internal include leaked route-map VRF_AFIPV4_RM_OSPF
         redistribute ospfv3 match external include leaked route-map VRF_AFIPV4_RM_OSPF
         redistribute ospfv3 match nssa-external 2 include leaked route-map VRF_AFIPV4_RM_OSPF
         redistribute ospf match external include leaked route-map VRF_AFIPV4_RM_OSPF
         redistribute ospf match nssa-external 1 include leaked route-map VRF_AFIPV4_RM_OSPF
         redistribute rip route-map VRF_AFIPV4_RM_RIP
         redistribute static include leaked route-map VRF_AFIPV4_RM_STATIC_1
      !
      address-family ipv4 multicast
         bgp missing-policy direction in action permit
         bgp missing-policy direction out action permit
         bgp additional-paths receive
         neighbor 1.2.3.4 additional-paths receive
         neighbor 1.2.3.4 route-map FOO in
         neighbor 1.2.3.4 route-map BAR out
         network 239.0.0.0/24 route-map BARFOO
         redistribute attached-host route-map VRF_AFIPV4MULTI_RM_HOST
         redistribute connected route-map VRF_AFIPV4MULTI_RM_CONNECTED
         redistribute isis level-1 include leaked route-map VRF_AFIPV4MULTI_RM_ISIS
         redistribute ospf match internal route-map VRF_AFIPV4MULTI_RM_OSPF
         redistribute ospfv3 match internal route-map VRF_AFIPV4MULTI_RM_OSPFv3
         redistribute ospfv3 match external route-map VRF_AFIPV4MULTI_RM_OSPFv3
         redistribute ospfv3 match nssa-external 1 route-map VRF_AFIPV4MULTI_RM_OSPFv3
         redistribute ospf match external route-map VRF_AFIPV4MULTI_RM_OSPF
         redistribute ospf match nssa-external 2 route-map VRF_AFIPV4MULTI_RM_OSPF
         redistribute static route-map VRF_AFIPV4MULTI_RM_STATIC
      !
      address-family ipv6
         bgp additional-paths install
         bgp missing-policy direction in action deny-in-out
         bgp missing-policy direction out action deny-in-out
         bgp additional-paths receive
         bgp additional-paths send any
         neighbor aa::1 activate
         neighbor aa::1 additional-paths receive
         neighbor aa::1 route-map FOO in
         neighbor aa::1 route-map BAR out
         neighbor aa::1 additional-paths send any
         neighbor aa::2 activate
         neighbor aa::2 rcf in VRF_AFIPV6_RCF_IN()
         neighbor aa::2 rcf out VRF_AFIPV6_RCF_OUT()
         network aa::/64
         redistribute connected rcf VRF_AFIPV6_RCF_CONNECTED()
         redistribute isis include leaked
         redistribute ospfv3 match internal include leaked
         redistribute ospfv3 match external
         redistribute ospfv3 match nssa-external
         redistribute static route-map VRF_AFIPV6_RM_STATIC
      !
      address-family ipv6 multicast
         bgp missing-policy direction in action deny
         bgp missing-policy direction out action deny
         bgp additional-paths receive
         neighbor aa::1 additional-paths receive
         network ff08:1::/64
         redistribute connected route-map VRF_AFIPV6MULTI_RM_CONNECTED
         redistribute isis level-1-2 include leaked route-map VRF_AFIPV6MULTI_RM_ISIS
         redistribute ospf route-map VRF_AFIPV6MULTI_RM_OSPF
         redistribute ospfv3 match internal route-map VRF_AFIPV6MULTI_RM_OSPFv3
         redistribute ospfv3 match external route-map VRF_AFIPV6MULTI_RM_OSPFv3
         redistribute ospfv3 match nssa-external 1 route-map VRF_AFIPV6MULTI_RM_OSPFv3
         redistribute ospf match external route-map VRF_AFIPV6MULTI_RM_OSPF
         redistribute ospf match nssa-external 1 route-map VRF_AFIPV6MULTI_RM_OSPF
         redistribute static route-map VRF_AFIPV6MULTI_RM_STATIC
   !
   vrf VRF02
      neighbor 1.1.1.1 additional-paths receive
      neighbor 1.1.1.1 additional-paths send ecmp limit 24
      redistribute connected include leaked route-map RM_VRF_CONNECTED
      redistribute isis level-2 include leaked route-map RM_VRF_ISIS
      redistribute ospf include leaked route-map RM_VRF_OSPF
      redistribute ospfv3 include leaked route-map RM_VRF_OSPFv3
      redistribute ospfv3 match external include leaked route-map RM_VRF_OSPFv3
      redistribute ospfv3 match nssa-external 1 include leaked route-map RM_VRF_OSPFv3
      redistribute static include leaked
      redistribute rip
      redistribute attached-host route-map RM_VRF_HOST
      redistribute dynamic route-map RM_VRF_DYNAMIC
      redistribute bgp leaked route-map RM_VRF_BGP
      redistribute user
      !
      address-family ipv4
         bgp additional-paths send backup
      !
      address-family ipv6
         bgp additional-paths send limit 3
   !
   vrf VRF03
      maximum-paths 10 ecmp 10
      bgp additional-paths send ecmp limit 4
      redistribute dynamic rcf VRF_RCF_DYNAMIC()
      !
      address-family ipv4
         bgp additional-paths install ecmp-primary
         bgp additional-paths send ecmp
   !
   vrf YELLOW-C1
      rd 1.0.1.1:103
      bgp listen range 10.10.10.0/24 peer-group my-peer-group1 peer-filter my-peer-filter
      bgp listen range 12.10.10.0/24 peer-id include router-id peer-group my-peer-group3 remote-as 65444
      bgp listen range 13.10.10.0/24 peer-group my-peer-group4 peer-filter my-peer-filter
      neighbor 10.1.1.0 peer group OBS_WAN
      no neighbor 10.1.1.0 remove-private-as ingress
   session tracker ST1
      recovery delay 666 seconds
   session tracker ST2
      recovery delay 42 seconds
   !
   address-family evpn
      evpn ethernet-segment domain all
         identifier 0011:1111:1111:1111:1111
         route-target import 00:01:00:01:00:01
            !
            layer-2 fec in-place update
```

### PBR Policy Maps

#### PBR Policy Maps Summary

##### PM_PBR_BREAKOUT

| Class | Index | Drop | Nexthop | Recursive |
| ----- | ----- | ---- | ------- | --------- |
| CM_PBR_EXCLUDE | - | - | - | - |
| CM_PBR_INCLUDE | - | - | 192.168.4.2 | True |

#### PBR Policy Maps Device Configuration

```eos
!
policy-map type pbr PM_PBR_BREAKOUT
   class CM_PBR_EXCLUDE
   !
   class CM_PBR_INCLUDE
      set nexthop recursive 192.168.4.2
```

## BFD

### Router BFD

| BFD Tuning |
| ---------- |
| Slow-Timer 5000 |

#### Router BFD Singlehop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 900 | 900 | 50 |

#### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 300 | 300 | 3 |

#### Router BFD SBFD Summary

| Initiator Interval | Initiator Multiplier | Initiator Round-Trip | Reflector Minimum RX | Reflector Local-Discriminator |
| ------------------ | -------------------- | -------------------- | ----------------------------- |
| 500 | 3 | True | 600 | 155.1.3.1 |

#### Router BFD Device Configuration

```eos
!
router bfd
   interval 900 min-rx 900 multiplier 50 default
   multihop interval 300 min-rx 300 multiplier 3
   slow-timer 5000
   local-address 192.168.255.1
   session stats snapshot interval 51
   !
   sbfd
      local-interface Loopback0 ipv4 ipv6
      initiator interval 500 multiplier 3
      initiator measurement delay round-trip
      reflector min-rx 600
      reflector local-discriminator 155.1.3.1
```

### BFD Interfaces

| Interface | Interval | Minimum RX | Multiplier | Echo |
| --------- | -------- | ---------- | ---------- | ---- |
| Ethernet1 | 500 | 500 | 5 | True |
| Port-Channel9 | 500 | 500 | 5 | True |
| Vlan85 | 500 | 500 | 5 | True |

## MPLS

### MPLS Interfaces

| Interface | MPLS IP Enabled | LDP Enabled | IGP Sync |
| --------- | --------------- | ----------- | -------- |
| Ethernet9 | True | True | - |
| Ethernet10 | False | False | - |
| Loopback99 | - | True | - |
| Port-Channel113 | True | True | True |
| Port-Channel114 | False | False | - |

## Patch Panel

### Patch Panel Summary

Patch Panel Connector Interface Recovery Review Delay Min: 10s - Max: 900s

Patch Panel Connector Interface Path BGP VPWS Remote Failure Errdisable is enabled.

#### Patch Panel Connections

| Patch Name | Enabled | Connector A Type | Connector A Endpoint | Connector B Type | Connector B Endpoint |
| ---------- | ------- | ---------------- | -------------------- | ---------------- | -------------------- |
| TEN_B_site2_site5_eline | True | Interface | Ethernet5 | Pseudowire | bgp vpws TENANT_A pseudowire TEN_B_site2_site5_eline |
| TEN_A_site2_site5_eline | False | Interface | Ethernet6 dot1q vlan 123 | Pseudowire | ldp LDP_PW_1 |

### Patch Panel Device Configuration

```eos
!
patch panel
   connector interface recovery review delay 10 900
   connector interface patch bgp vpws remote-failure errdisable
   !
   patch TEN_A_site2_site5_eline
      shutdown
      connector 1 interface Ethernet6 dot1q vlan 123
      connector 2 pseudowire ldp LDP_PW_1
   !
   patch TEN_B_site2_site5_eline
      connector 1 interface Ethernet5
      connector 2 pseudowire bgp vpws TENANT_A pseudowire TEN_B_site2_site5_eline
   !
```

## Queue Monitor

### Queue Monitor Length

| Enabled | Logging Interval | Default Thresholds High | Default Thresholds Low | Notifying | TX Latency | CPU Thresholds High | CPU Thresholds Low |
| ------- | ---------------- | ----------------------- | ---------------------- | --------- | ---------- | ------------------- | ------------------ |
| True | 100 | 100 | 10 | enabled | enabled | 200000 | 100000 |

### Queue Monitor Streaming

| Enabled | IP Access Group | IPv6 Access Group | Max Connections | VRF |
| ------- | --------------- | ----------------- | --------------- | --- |
| True | ACL-QMS | ACLv6-QMS | 5 | test |

### Queue Monitor Configuration

```eos
!
queue-monitor length
queue-monitor length notifying
queue-monitor length tx-latency
queue-monitor length default thresholds 100 10
queue-monitor length cpu thresholds 200000 100000
!
queue-monitor length log 100
!
queue-monitor streaming
   max-connections 5
   ip access-group ACL-QMS
   ipv6 access-group ACLv6-QMS
   vrf test
   no shutdown
```

## Multicast

### IP IGMP Snooping

#### IP IGMP Snooping Summary

| IGMP Snooping | Fast Leave | Interface Restart Query | Proxy | Restart Query Interval | Robustness Variable |
| ------------- | ---------- | ----------------------- | ----- | ---------------------- | ------------------- |
| Enabled | True | 500 | True | 30 | 2 |

| Querier Enabled | IP Address | Query Interval | Max Response Time | Last Member Query Interval | Last Member Query Count | Startup Query Interval | Startup Query Count | Version |
| --------------- | ---------- | -------------- | ----------------- | -------------------------- | ----------------------- | ---------------------- | ------------------- | ------- |
| True | 10.10.10.1 | 40 | 10 | 5 | 2 | 20 | 2 | 3 |

##### IP IGMP Snooping Vlan Summary

| Vlan | IGMP Snooping | Fast Leave | Max Groups | Proxy |
| ---- | ------------- | ---------- | ---------- | ----- |
| 23 | True | True | 20 | True |
| 24 | True | - | - | - |
| 25 | False | False | - | False |
| 26 | - | - | - | - |

| Vlan | Querier Enabled | IP Address | Query Interval | Max Response Time | Last Member Query Interval | Last Member Query Count | Startup Query Interval | Startup Query Count | Version |
| ---- | --------------- | ---------- | -------------- | ----------------- | -------------------------- | ----------------------- | ---------------------- | ------------------- | ------- |
| 23 | True | 10.10.23.1 | 40 | 10 | 5 | 2 | 20 | 2 | 3 |

#### IP IGMP Snooping Device Configuration

```eos
!
ip igmp snooping robustness-variable 2
ip igmp snooping restart query-interval 30
ip igmp snooping interface-restart-query 500
ip igmp snooping fast-leave
ip igmp snooping vlan 23
ip igmp snooping vlan 23 querier
ip igmp snooping vlan 23 querier address 10.10.23.1
ip igmp snooping vlan 23 querier query-interval 40
ip igmp snooping vlan 23 querier max-response-time 10
ip igmp snooping vlan 23 querier last-member-query-interval 5
ip igmp snooping vlan 23 querier last-member-query-count 2
ip igmp snooping vlan 23 querier startup-query-interval 20
ip igmp snooping vlan 23 querier startup-query-count 2
ip igmp snooping vlan 23 querier version 3
ip igmp snooping vlan 23 max-groups 20
ip igmp snooping vlan 23 fast-leave
ip igmp snooping vlan 24
no ip igmp snooping vlan 25
no ip igmp snooping vlan 25 fast-leave
ip igmp snooping querier
ip igmp snooping querier address 10.10.10.1
ip igmp snooping querier query-interval 40
ip igmp snooping querier max-response-time 10
ip igmp snooping querier last-member-query-interval 5
ip igmp snooping querier last-member-query-count 2
ip igmp snooping querier startup-query-interval 20
ip igmp snooping querier startup-query-count 2
ip igmp snooping querier version 3
!
ip igmp snooping proxy
ip igmp snooping vlan 23 proxy
no ip igmp snooping vlan 25 proxy
```

### Router Multicast

#### IP Router Multicast Summary

- Counters rate period decay is set for 300 seconds
- Routing for IPv4 multicast is enabled.
- Multipathing deterministically by selecting the same upstream router.
- Software forwarding by the Software Forwarding Engine (SFE)

#### IP Router Multicast RPF Routes

| Source Prefix | Next Hop | Administrative Distance |
| ------------- | -------- | ----------------------- |
| 10.10.10.1/32 | 10.9.9.9 | 2 |
| 10.10.10.1/32 | Ethernet1 | 1 |
| 10.10.10.2/32 | Ethernet2 | - |

#### IP Router Multicast VRFs

| VRF Name | Multicast Routing |
| -------- | ----------------- |
| MCAST_VRF1 | enabled |
| MCAST_VRF2 | enabled |

#### Router Multicast Device Configuration

```eos
!
router multicast
   ipv4
      rpf route 10.10.10.1/32 10.9.9.9 2
      rpf route 10.10.10.1/32 Ethernet1 1
      rpf route 10.10.10.2/32 Ethernet2
      counters rate period decay 300 seconds
      activity polling-interval 10
      routing
      multipath deterministic router-id
      software-forwarding sfe
   !
   ipv6
      activity polling-interval 20
   !
   vrf MCAST_VRF1
      ipv4
         routing
   !
   vrf MCAST_VRF2
      ipv4
         routing
```

### PIM Sparse Mode

#### Router PIM Sparse Mode

##### IP Sparse Mode Information

BFD enabled: True

##### IP Rendezvous Information

| Rendezvous Point Address | Group Address | Access Lists | Priority | Hashmask | Override |
| ------------------------ | ------------- | ------------ | -------- | -------- | -------- |
| 10.238.1.161 | 239.12.12.12/32, 239.12.12.13/32, 239.12.12.14/32, 239.12.12.16/32, 239.12.12.20/32, 239.12.12.21/32 | RP_ACL, RP_ACL2 | 20 | - | - |
| 10.238.1.161 | 239.12.12.17/32 | RP_ACL3 | - | - | - |

##### IP Anycast Information

| IP Anycast Address | Other Rendezvous Point Address | Register Count |
| ------------------ | ------------------------------ | -------------- |
| 10.38.1.161 | 10.50.64.16 | 15 |

##### IP Sparse Mode VRFs

| VRF Name | BFD Enabled |
| -------- | ----------- |
| MCAST_VRF1 | True |
| MCAST_VRF2_ALL_GROUPS | False |
| Test_RP_ACL | False |

| VRF Name | Rendezvous Point Address | Group Address | Access Lists | Priority | Hashmask | Override |
| -------- | ------------------------ | ------------- | ------------ | -------- | -------- | -------- |
| MCAST_VRF1 | 10.238.2.161 | 239.12.22.12/32, 239.12.22.13/32, 239.12.22.14/32 | - | - | - | - |
| MCAST_VRF2_ALL_GROUPS | 10.238.3.161 | - | - | - | 30 | - |
| Test_RP_ACL | 10.238.4.161 | - | RP_ACL | - | - | - |
| Test_RP_ACL | 10.238.4.161 | - | RP_ACL2 | 20 | 30 | True |

##### Router Multicast Device Configuration

```eos
!
router pim sparse-mode
   ipv4
      ssm range standard
      bfd
      rp address 10.238.1.161 239.12.12.12/32 priority 20
      rp address 10.238.1.161 239.12.12.13/32 priority 20
      rp address 10.238.1.161 239.12.12.14/32 priority 20
      rp address 10.238.1.161 239.12.12.16/32 priority 20
      rp address 10.238.1.161 239.12.12.20/32 priority 20
      rp address 10.238.1.161 239.12.12.21/32 priority 20
      rp address 10.238.1.161 access-list RP_ACL priority 20
      rp address 10.238.1.161 access-list RP_ACL2 priority 20
      rp address 10.238.1.161 239.12.12.17/32
      rp address 10.238.1.161 access-list RP_ACL3
      anycast-rp 10.38.1.161 10.50.64.16 register-count 15
   !
   vrf MCAST_VRF1
      ipv4
         bfd
         rp address 10.238.2.161 239.12.22.12/32
         rp address 10.238.2.161 239.12.22.13/32
         rp address 10.238.2.161 239.12.22.14/32
   !
   vrf MCAST_VRF2_ALL_GROUPS
      ipv4
         rp address 10.238.3.161 hashmask 30
   !
   vrf Test_RP_ACL
      ipv4
         rp address 10.238.4.161 access-list RP_ACL
         rp address 10.238.4.161 access-list RP_ACL2 priority 20 hashmask 30 override
```

#### PIM Sparse Mode Enabled Interfaces

| Interface Name | VRF Name | IP Version | Border Router | DR Priority | Local Interface |
| -------------- | -------- | ---------- | ------------- | ----------- | --------------- |
| Ethernet5 | - | IPv4 | True | 200 | - |
| Port-Channel99 | - | IPv4 | - | 200 | - |
| Vlan89 | - | IPv4 | - | - | Loopback0 |
| Vlan4094 | - | IPv4 | - | 200 | - |

### Router MSDP

#### Router MSDP Peers

| Peer Address | Disabled | VRF | Default-peer | Default-peer Prefix List | Mesh Groups | Local Interface | Description | Inbound SA Filter | Outbound SA Filter |
| ------------ | -------- | --- | ------------ | ------------------------ | ----------- | --------------- | ----------- | ----------------- | ------------------ |
| 1.2.3.4 | True | default | True | PLIST1 | MG1, MG2 | Loopback11 | Some kind of MSDP Peer | ACL1 | ACL2 |
| 4.3.2.1 | False | default | False | PLIST2 | - | Loopback21 | - | - | - |
| 2.3.4.5 | False | RED | True | - | - | Loopback13 | Some other kind of MSDP Peer | ACL3 | ACL4 |

#### Router MSDP Device Configuration

```eos
!
router msdp
   group-limit 100 source 10.0.1.0/24
   group-limit 123 source 10.0.123.0/24
   originator-id local-interface Loopback10
   rejected-limit 123
   forward register-packets
   connection retry interval 5
   !
   peer 1.2.3.4
      default-peer prefix-list PLIST1
      mesh-group MG1
      mesh-group MG2
      local-interface Loopback11
      keepalive 10 30
      sa-filter in list ACL1
      sa-filter out list ACL2
      description Some kind of MSDP Peer
      disabled
      sa-limit 1000
   !
   peer 4.3.2.1
      local-interface Loopback21
   !
   vrf RED
      group-limit 22 source 10.0.22.0/24
      originator-id local-interface Loopback12
      rejected-limit 10
      connection retry interval 10
      !
      peer 2.3.4.5
         default-peer
         local-interface Loopback13
         keepalive 5 15
         sa-filter in list ACL3
         sa-filter out list ACL4
         description Some other kind of MSDP Peer
         sa-limit 100
```

### Router IGMP

#### Router IGMP Summary

| VRF | SSM Aware | Host Proxy |
| --- | --------- | ---------- |
| - | Enabled | - |
| default | - | all |
| BLUE | - | iif |

#### Router IGMP Device Configuration

```eos
!
router igmp
   host-proxy match mroute all
   ssm aware
   !
   vrf BLUE
     host-proxy match mroute iif
```

## Filters

### IP Community-lists

#### IP Community-lists Summary

| Name | Action | Communities / Regexp |
| ---- | ------ | -------------------- |
| IP_CL_TEST1 | permit | 1001:1001, 1002:1002 |
| IP_CL_TEST1 | deny | 1010:1010 |
| IP_CL_TEST1 | permit | 20:* |
| IP_CL_TEST2 | deny | 1003:1003 |
| IP_RE_TEST1 | permit | ^$ |
| IP_RE_TEST2 | deny | ^100 |

#### IP Community-lists Device Configuration

```eos
!
ip community-list IP_CL_TEST1 permit 1001:1001 1002:1002
ip community-list IP_CL_TEST1 deny 1010:1010
ip community-list regexp IP_CL_TEST1 permit 20:*
ip community-list IP_CL_TEST2 deny 1003:1003
ip community-list regexp IP_RE_TEST1 permit ^$
ip community-list regexp IP_RE_TEST2 deny ^100
```

### Peer Filters

#### Peer Filters Summary

##### PF1

| Sequence | Match |
| -------- | ----- |
| 10 | as-range 1-2 result reject |
| 20 | as-range 1-100 result accept |

##### PF2

| Sequence | Match |
| -------- | ----- |
| 30 | as-range 65000 result accept |

#### Peer Filters Device Configuration

```eos
!
peer-filter PF1
   10 match as-range 1-2 result reject
   20 match as-range 1-100 result accept
!
peer-filter PF2
   30 match as-range 65000 result accept
```

### Route-maps

#### Route-maps Summary

##### RM-10.2.3.4-SET-NEXT-HOP-OUT

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | - | ip next-hop 10.2.3.4 | - | - |

##### RM-BGP-AGG-APPLY-SET

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | - | local-preference 50 | - | - |

##### RM-BGP-EXPORT-DEFAULT-BLUE-C1

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | ip address prefix-list PL-BGP-DEFAULT-BLUE-C1 | - | - | - |

##### RM-CONN-BL-BGP

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | deny | ip address prefix-list PL-MLAG | - | - | - |
| 20 | permit | ip address prefix-list PL-SUBRM | - | RM-HIDE-ASPATH-IN | - |
| 30 | permit | ip address prefix-list PL-CONTINUE | - | - | 40 |
| 40 | permit | ip address prefix-list PL-CONTINUE | - | - | Next Sequence |
| 50 | permit | - | - | - | - |

##### RM-HIDE-ASPATH-IN

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | - | as-path match all replacement auto<br>community 65000:1 additive | - | - |

##### RM-HIDE-ASPATH-OUT

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | deny | community LIST-COM | - | - | - |
| 20 | permit | - | as-path match all replacement auto | - | - |

##### RM-MLAG-PEER-IN

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | - | origin incomplete | - | - |

##### RM-STATIC-2-BGP

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | - | tag 65100 | - | - |

#### Route-maps Device Configuration

```eos
!
route-map RM-10.2.3.4-SET-NEXT-HOP-OUT permit 10
   set ip next-hop 10.2.3.4
!
route-map RM-BGP-AGG-APPLY-SET permit 10
   description RM for BGP AGG Set
   set local-preference 50
!
route-map RM-BGP-EXPORT-DEFAULT-BLUE-C1 permit 10
   description RM for BGP default route in BLUE-C1
   match ip address prefix-list PL-BGP-DEFAULT-BLUE-C1
!
route-map RM-CONN-BL-BGP deny 10
   match ip address prefix-list PL-MLAG
!
route-map RM-CONN-BL-BGP permit 20
   description sub-route-map test
   match ip address prefix-list PL-SUBRM
   sub-route-map RM-HIDE-ASPATH-IN
!
route-map RM-CONN-BL-BGP permit 30
   match ip address prefix-list PL-CONTINUE
   continue 40
!
route-map RM-CONN-BL-BGP permit 40
   match ip address prefix-list PL-CONTINUE
   continue
!
route-map RM-CONN-BL-BGP permit 50
!
route-map RM-HIDE-ASPATH-IN permit 10
   set as-path match all replacement auto
   set community 65000:1 additive
!
route-map RM-HIDE-ASPATH-OUT deny 10
   match community LIST-COM
!
route-map RM-HIDE-ASPATH-OUT permit 20
   set as-path match all replacement auto
!
route-map RM-MLAG-PEER-IN permit 10
   set origin incomplete
!
route-map RM-STATIC-2-BGP permit 10
   description tag for static routes
   set tag 65100
```

### IP Extended Community Lists

#### IP Extended Community Lists Summary

| List Name | Type | Extended Communities |
| --------- | ---- | -------------------- |
| TEST1 | permit | 65000:65000 |
| TEST1 | deny | 65002:65002 |
| TEST2 | deny | 65001:65001 |

#### IP Extended Community Lists Device Configuration

```eos
!
ip extcommunity-list TEST1 permit 65000:65000
ip extcommunity-list TEST1 deny 65002:65002
!
ip extcommunity-list TEST2 deny 65001:65001
```

### IP Extended Community RegExp Lists

#### IP Extended Community RegExp Lists Summary

| List Name | Type | Regular Expression |
| --------- | ---- | ------------------ |
| TEST1 | permit | `65[0-9]{3}:[0-9]+` |
| TEST1 | deny | `.*` |
| TEST2 | deny | `6500[0-1]:650[0-9][0-9]` |

#### IP Extended Community RegExp Lists Device Configuration

```eos
!
ip extcommunity-list regexp TEST1 permit 65[0-9]{3}:[0-9]+
ip extcommunity-list regexp TEST1 deny .*
!
ip extcommunity-list regexp TEST2 deny 6500[0-1]:650[0-9][0-9]
```

### Match-lists

#### Match-list Input IPv4-prefix Summary

| Prefix List Name | Prefixes |
| ---------------- | -------- |
| molecule_v4 | 10.10.10.0/24, 10.10.20.0/24 |

#### Match-list Input IPv6-prefix Summary

| Prefix List Name | Prefixes |
| ---------------- | -------- |
| molecule_v6 | 2001:0DB8::/32 |

#### Match-list Input String Summary

##### molecule

| Sequence | Match Regex |
| -------- | ------ |
| 10 | ^.*MOLECULE.*$ |
| 20 | ^.*TESTING.*$ |

#### Match-lists Device Configuration

```eos
!
match-list input string molecule
   10 match regex ^.*MOLECULE.*$
   20 match regex ^.*TESTING.*$
!
match-list input prefix-ipv4 molecule_v4
   match prefix-ipv4 10.10.10.0/24
   match prefix-ipv4 10.10.20.0/24
!
match-list input prefix-ipv6 molecule_v6
   match prefix-ipv6 2001:0DB8::/32
```

### AS Path Lists

#### AS Path Lists Summary

AS Path Regex Mode is **asn**.

| List Name | Type | Match | Origin |
| --------- | ---- | ----- | ------ |
| mylist1 | permit | ^(64512\|645115) | egp |
| mylist1 | deny | (64513\|64515)$ | any |
| mylist2 | deny | _64517$ | igp |

#### AS Path Lists Device Configuration

```eos
!
ip as-path regex-mode asn
ip as-path access-list mylist1 permit ^(64512|645115) egp
ip as-path access-list mylist1 deny (64513|64515)$ any
ip as-path access-list mylist2 deny _64517$ igp
```

## 802.1X Port Security

### 802.1X Summary

#### 802.1X Global

| System Auth Control | Protocol LLDP Bypass | Dynamic Authorization |
| ------------------- | -------------------- | ----------------------|
| True | True | True |

#### 802.1X MAC based authentication

| Delay | Hold period |
| ----- | ----------- |
| 300 | 300 |

#### 802.1X Radius AV pair

| Service type | Framed MTU |
| ------------ | ---------- |
| True | 1500 |

#### 802.1X Captive-portal authentication

| Authentication Attribute | Value |
| ------------------------ | ----- |
| URL | http://portal-nacm08/captiveredirect/ |
| SSL profile | Profile1 |
| IPv4 Access-list | ACL |
| Start limit | Infinite |

#### 802.1X Supplicant

| Attribute | Value |
| --------- | ----- |
| Logging | True |
| Disconnect cached-results timeout | 79 seconds |

##### 802.1X Supplicant profiles

| Profile | EAP Method | Identity | SSL Profile |
| ------- | ---------- | -------- | ----------- |
| Profile1 | tls | user_id1 | PF1 |
| Profile2 | - | user_id2 | - |
| Profile3 | - | - | PF2 |

#### 802.1X Interfaces

| Interface | PAE Mode | State | Phone Force Authorized | Reauthentication | Auth Failure Action | Host Mode | Mac Based Auth | Eapol |
| --------- | -------- | ------| ---------------------- | ---------------- | ------------------- | --------- | -------------- | ------ |
| Ethernet29 | - | auto | True | - | - | - | - | - |
| Ethernet30 | - | force-authorized | False | - | - | - | - | - |
| Ethernet31 | - | force-unauthorized | - | - | - | - | - | - |
| Ethernet32 | - | auto | - | True | - | - | - | - |
| Ethernet33 | authenticator | - | - | - | - | - | - | - |
| Ethernet34 | - | - | - | - | allow vlan 800 | - | - | - |
| Ethernet35 | - | - | - | - | drop | - | - | - |
| Ethernet36 | - | - | - | - | - | single-host | - | - |
| Ethernet37 | - | - | - | - | - | multi-host | - | - |
| Ethernet38 | - | - | - | - | - | multi-host | - | - |
| Ethernet39 | - | - | - | - | - | - | True | - |
| Ethernet40 | - | - | - | - | - | - | True | - |
| Ethernet41 | - | - | - | - | - | - | True | - |
| Ethernet42 | - | - | - | - | - | - | True | - |
| Ethernet43 | - | - | - | - | - | - | - | - |
| Ethernet44 | - | - | - | - | - | - | - | - |
| Ethernet45 | authenticator | auto | - | True | allow vlan 800 | multi-host | True | True |
| Ethernet70 | - | - | - | - | - | - | - | - |
| Ethernet71 | - | - | - | - | - | - | - | - |
| Ethernet72 | - | - | - | - | - | - | - | - |

## Power Over Ethernet (PoE)

### PoE Summary

#### PoE Interfaces

| Interface | PoE Enabled | Priority | Limit | Reboot Action | Link Down Action | Shutdown Action | LLDP Negotiation | Legacy Detection |
| --------- | --------- | --------- | ----------- | ----------- | ----------- | ----------- | --------- | --------- |
| Ethernet56 | True | low | 30.00 watts | power-off | power-off (delayed 10 seconds) | maintain | False | - |
| Ethernet57 | True | critical | 45.00 watts (fixed) | maintain | maintain | power-off | True | True |
| Ethernet58 | False | - | - | - | - | - | - | - |

## ACL

### Standard Access-lists

#### Standard Access-lists Summary

##### 99

| Sequence | Action |
| -------- | ------ |
| 10 | remark ACL to restrict access RFC1918 addresses |
| 20 | permit 10.0.0.0/8 |
| 30 | permit 172.16.0.0/12 |
| 40 | permit 192.168.0.0/16 |

##### ACL-API

| Sequence | Action |
| -------- | ------ |
| 10 | remark ACL to restrict access to switch API to CVP and Ansible |
| 20 | permit host 10.10.10.10 |
| 30 | permit host 10.10.10.11 |
| 40 | permit host 10.10.10.12 |

##### ACL-SSH

ACL has counting mode `counters per-entry` enabled!

| Sequence | Action |
| -------- | ------ |
| 10 | remark ACL to restrict access RFC1918 addresses |
| 20 | permit 10.0.0.0/8 |
| 30 | permit 172.16.0.0/12 |
| 40 | permit 192.168.0.0/16 |

##### ACL-SSH-VRF

| Sequence | Action |
| -------- | ------ |
| 10 | remark ACL to restrict access RFC1918 addresses |
| 20 | permit 10.0.0.0/8 |
| 30 | permit 172.16.0.0/12 |
| 40 | permit 192.168.0.0/16 |

#### Standard Access-lists Device Configuration

```eos
!
ip access-list standard 99
   10 remark ACL to restrict access RFC1918 addresses
   20 permit 10.0.0.0/8
   30 permit 172.16.0.0/12
   40 permit 192.168.0.0/16
!
ip access-list standard ACL-API
   10 remark ACL to restrict access to switch API to CVP and Ansible
   20 permit host 10.10.10.10
   30 permit host 10.10.10.11
   40 permit host 10.10.10.12
!
ip access-list standard ACL-SSH
   counters per-entry
   10 remark ACL to restrict access RFC1918 addresses
   20 permit 10.0.0.0/8
   30 permit 172.16.0.0/12
   40 permit 192.168.0.0/16
!
ip access-list standard ACL-SSH-VRF
   10 remark ACL to restrict access RFC1918 addresses
   20 permit 10.0.0.0/8
   30 permit 172.16.0.0/12
   40 permit 192.168.0.0/16
```

### Extended Access-lists

#### Extended Access-lists Summary

##### 4

| Sequence | Action |
| -------- | ------ |
| 10 | remark ACL to restrict access RFC1918 addresses |
| 20 | deny ip 10.0.0.0/8 any |
| 30 | permit ip 192.0.2.0/24 any |

##### ACL-01

| Sequence | Action |
| -------- | ------ |
| 10 | remark ACL to restrict access to switch API to CVP and Ansible |
| 20 | deny ip host 192.0.2.1 any |
| 30 | permit ip 192.0.2.0/24 any |

##### ACL-02

ACL has counting mode `counters per-entry` enabled!

| Sequence | Action |
| -------- | ------ |
| 10 | remark ACL to restrict access RFC1918 addresses |
| 20 | permit ip 10.0.0.0/8 any |
| 30 | permit ip 192.0.2.0/24 any |
| - | permit response traffic nat |

##### ACL-03

| Sequence | Action |
| -------- | ------ |
| 10 | remark ACL to restrict access RFC1918 addresses |
| 20 | deny ip 10.0.0.0/8 any |
| 30 | permit ip 192.0.2.0/24 any |

##### ACL-04

ACL has counting mode `counters per-entry` enabled!

| Sequence | Action |
| -------- | ------ |
| 20 | deny ip 12.0.0.0/8 any |
| 30 | permit ip 194.0.2.0/24 any |
| - | permit response traffic nat |

#### Extended Access-lists Device Configuration

```eos
!
ip access-list 4
   10 remark ACL to restrict access RFC1918 addresses
   20 deny ip 10.0.0.0/8 any
   30 permit ip 192.0.2.0/24 any
!
ip access-list ACL-01
   10 remark ACL to restrict access to switch API to CVP and Ansible
   20 deny ip host 192.0.2.1 any
   30 permit ip 192.0.2.0/24 any
!
ip access-list ACL-02
   counters per-entry
   10 remark ACL to restrict access RFC1918 addresses
   20 permit ip 10.0.0.0/8 any
   30 permit ip 192.0.2.0/24 any
   permit response traffic nat
!
ip access-list ACL-03
   10 remark ACL to restrict access RFC1918 addresses
   20 deny ip 10.0.0.0/8 any
   30 permit ip 192.0.2.0/24 any
!
ip access-list ACL-04
   counters per-entry
   20 deny ip 12.0.0.0/8 any
   30 permit ip 194.0.2.0/24 any
   permit response traffic nat
```

### IP Access-lists

#### IP Access-lists Summary

- The maximum number of ACL entries allowed to be provisioned per switch: 10000

#### IP Access-lists Device Configuration

```eos
!
ip access-list ACL_NO_SEQUENCE
   remark test acl without sequence numbers
   deny udp any any log
   permit icmp any any 3 4 ttl eq 40
   permit icmp any any unreachable ttl gt 3
   permit ip any any fragments dscp 46
   permit ip any any tracked dscp ef
   permit ip any any nexthop-group NH_TEST
   permit vlan inner 123 0x000 ip any any
   permit vlan 234 0xFFF ip any any
   permit icmp any any
!
ip access-list ACL_SEQUENCE_AND_COUNTERS
   counters per-entry
   10 remark test acl with sequence numbers
   20 permit ip 10.0.0.0/8 any
   30 permit tcp host 192.168.122.22 any established
   40 permit tcp any gt 1023 host 172.16.16.16 eq 22
   50 permit tcp any range 1000 1100 any range 10 20
   4294967295 deny ip any any
   permit response traffic nat
```

### IPv6 Standard Access-lists

#### IPv6 Standard Access-lists Summary

##### TEST4

| Sequence | Action |
| -------- | ------ |
| 5 | deny fe80::/64 |
| 10 | permit fe90::/64 |

##### TEST5

ACL has counting mode `counters per-entry` enabled!

| Sequence | Action |
| -------- | ------ |
| 5 | permit 2001:db8::/64 |
| 10 | deny 2001:db8::/32 |

##### TEST6

| Sequence | Action |
| -------- | ------ |
| 5 | deny 2001:db8:1000::/64 |
| 10 | permit 2001:db8::/32 |

#### IPv6 Standard Access-lists Device Configuration

```eos
!
ipv6 access-list standard TEST4
   5 deny fe80::/64
   10 permit fe90::/64
!
ipv6 access-list standard TEST5
   counters per-entry
   5 permit 2001:db8::/64
   10 deny 2001:db8::/32
!
ipv6 access-list standard TEST6
   5 deny 2001:db8:1000::/64
   10 permit 2001:db8::/32
```

### IPv6 Extended Access-lists

#### IPv6 Extended Access-lists Summary

##### TEST1

| Sequence | Action |
| -------- | ------ |
| 5 | deny ipv6 fe80::/64 any |
| 10 | permit ipv6 fe90::/64 any |

##### TEST2

ACL has counting mode `counters per-entry` enabled!

| Sequence | Action |
| -------- | ------ |
| 5 | permit ipv6 2001:db8::/64 any |
| 10 | deny ipv6 2001:db8::/32 any |

##### TEST3

| Sequence | Action |
| -------- | ------ |
| 5 | deny ipv6 2001:db8:1000::/64 any |
| 10 | permit ipv6 2001:db8::/32 any |

#### IPv6 Extended Access-lists Device Configuration

```eos
!
ipv6 access-list TEST1
   5 deny ipv6 fe80::/64 any
   10 permit ipv6 fe90::/64 any
!
ipv6 access-list TEST2
   counters per-entry
   5 permit ipv6 2001:db8::/64 any
   10 deny ipv6 2001:db8::/32 any
!
ipv6 access-list TEST3
   5 deny ipv6 2001:db8:1000::/64 any
   10 permit ipv6 2001:db8::/32 any
```

### MAC Access-lists

#### MAC Access-lists Summary

##### TEST1

| Sequence | Action |
| -------- | ------ |
| 10 | deny any 01:80:c2:00:00:00 00:00:00:00:00:00 |
| 5 | permit any 01:00:0c:cc:cc:cd 00:00:00:00:00:00 |

##### TEST2

- ACL has counting mode `counters per-entry` enabled!

| Sequence | Action |
| -------- | ------ |
| 5 | permit any 01:00:0c:cc:cc:cd 00:00:00:00:00:00 |
| 10 | deny any 01:80:c2:00:00:00 00:00:00:00:00:00 |

##### TEST3

| Sequence | Action |
| -------- | ------ |
| 5 | permit any 01:00:0c:cc:cc:cd 00:00:00:00:00:00 |
| 10 | deny any 01:80:c2:00:00:00 00:00:00:00:00:00 |

##### TEST4

| Sequence | Action |
| -------- | ------ |
| - | permit any 01:00:0c:cc:cc:cd 00:00:00:00:00:00 |
| - | deny any 01:80:c2:00:00:00 00:00:00:00:00:00 |
| - | remark A comment in the middle |
| - | permit any 02:00:00:12:34:56 00:00:00:00:00:00 |
| - | deny any 02:00:00:ab:cd:ef 00:00:00:00:00:00 |

#### MAC Access-lists Device Configuration

```eos
!
mac access-list TEST1
   10 deny any 01:80:c2:00:00:00 00:00:00:00:00:00
   5 permit any 01:00:0c:cc:cc:cd 00:00:00:00:00:00
!
mac access-list TEST2
   counters per-entry
   5 permit any 01:00:0c:cc:cc:cd 00:00:00:00:00:00
   10 deny any 01:80:c2:00:00:00 00:00:00:00:00:00
!
mac access-list TEST3
   5 permit any 01:00:0c:cc:cc:cd 00:00:00:00:00:00
   10 deny any 01:80:c2:00:00:00 00:00:00:00:00:00
!
mac access-list TEST4
   permit any 01:00:0c:cc:cc:cd 00:00:00:00:00:00
   deny any 01:80:c2:00:00:00 00:00:00:00:00:00
   remark A comment in the middle
   permit any 02:00:00:12:34:56 00:00:00:00:00:00
   deny any 02:00:00:ab:cd:ef 00:00:00:00:00:00
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| BLAH | disabled |
| defauls | disabled |
| defaulu | disabled |
| MGMT | disabled |
| TENANT_A_PROJECT01 | enabled |
| TENANT_A_PROJECT02 | enabled |

### VRF Instances Device Configuration

```eos
!
vrf instance BLAH
!
vrf instance defauls
!
vrf instance defaulu
!
vrf instance MGMT
!
vrf instance TENANT_A_PROJECT01
!
vrf instance TENANT_A_PROJECT02
```

## Virtual Source NAT

### Virtual Source NAT Summary

| Source NAT VRF | Source NAT IPv4 Address | Source NAT IPv6 Address |
| -------------- | ----------------------- | ----------------------- |
| TEST_01 | 1.1.1.1 | - |
| TEST_02 | 1.1.1.2 | - |
| TEST_03 | - | 2001:db8:85a3::8a2e:370:7334 |
| TEST_04 | 1.1.1.3 | 2001:db8:85a3::8a2e:370:7335 |

### Virtual Source NAT Configuration

```eos
!
ip address virtual source-nat vrf TEST_01 address 1.1.1.1
ip address virtual source-nat vrf TEST_02 address 1.1.1.2
ip address virtual source-nat vrf TEST_04 address 1.1.1.3
ipv6 address virtual source-nat vrf TEST_03 address 2001:db8:85a3::8a2e:370:7334
ipv6 address virtual source-nat vrf TEST_04 address 2001:db8:85a3::8a2e:370:7335
```

## System L1

### Unsupported Interface Configurations

| Unsupported Configuration | action |
| ---------------- | -------|
| Speed | warn |
| Error correction | error |

### System L1 Device Configuration

```eos
!
system l1
   unsupported speed action warn
   unsupported error-correction action error
```

## Application Traffic Recognition

### Applications

#### IPv4 Applications

| Name | Source Prefix | Destination Prefix | Protocols | Protocol Ranges | TCP Source Port Set | TCP Destination Port Set | UDP Source Port Set | UDP Destination Port Set | DSCP |
| ---- | ------------- | ------------------ | --------- | --------------- | ------------------- | ------------------------ | ------------------- | ------------------------ | ---- |
| empty-application | - | - | - | - | - | - | - | - | - |
| empty-protocols | - | - | - | 21 | - | - | - | - | - |
| user_defined_app1 | src_prefix_set1 | dest_prefix_set1 | udp, tcp | 25 | src_port_set1 | dest_port_set1 | src_port_set2 | dest_port_set2 | 12-19 af43 af41 ef 1-4,6 32-33,34-35 11 56-57, 58 59-60, 61-62 |
| user_defined_app2 | src_prefix_set2 | dest_prefix_set2 | pim, icmp, tcp | 21, 7-11 | - | - | - | - | ef 1-42 cs1 |

#### Layer 4 Applications

| Name | Protocols | Protocol Ranges | TCP Source Port Set | TCP Destination Port Set | UDP Source Port Set | UDP Destination Port Set |
| ---- | --------- | --------------- | ------------------- | ------------------------ | ------------------- | ------------------------ |
| l4-app-1 | tcp, udp | - | src_port_set1 | dest_port_set1 | src_port_set1 | dest_port_set1 |
| l4-app-2 | tcp | 27, 41-44 | - | - | - | - |

### Application Profiles

#### Application Profile Name app_profile_1

| Type | Name | Service |
| ---- | ---- | ------- |
| application | aim | audio-video |
| application | aim | chat |
| application | user_defined_app1 | - |
| category | best-effort | - |
| category | category1 | audio-video |
| transport | http | - |
| transport | udp | - |

#### Application Profile Name app_profile_2

| Type | Name | Service |
| ---- | ---- | ------- |
| application | aim | audio-video |
| application | user_defined_app2 | - |
| category | category1 | chat |
| transport | https | - |
| transport | quic | - |

### Categories

| Category | Application(Service) |
| -------- | -------------------- |
| best-effort | aimini(peer-to-peer)<br>apple_update(software-update) |
| category1 | aim(audio-video)<br>aim(chat)<br>anydesk |
| empty |  |

### Field Sets

#### L4 Port Sets

| Name | Ports |
| ---- | ----- |
| dest_port_set1 | 2300-2350 |
| dest_port_set2 | 3300-3350 |
| empty-l4-ports | - |
| ordering-test | 101-103, 650, 666 |
| src_port_set1 | 2400-2500, 2900-3000 |
| src_port_set2 | 5700-5800, 6500-6600 |

#### IPv4 Prefix Sets

| Name | Prefixes |
| ---- | -------- |
| dest_prefix_set1 | 2.3.4.0/24 |
| dest_prefix_set2 | 4.4.4.0/24 |
| empty-ipv4-prefixes | - |
| order-test | 192.168.42.0/24<br>192.168.43.0/24<br>6.6.6.6/32 |
| src_prefix_set1 | 1.2.3.0/24<br>1.2.5.0/24 |
| src_prefix_set2 | 2.2.2.0/24<br>3.3.3.0/24 |

### Router Application-Traffic-Recognition Device Configuration

```eos
!
application traffic recognition
   !
   application ipv4 empty-application
   !
   application ipv4 empty-protocols
      protocol 21
   !
   application ipv4 user_defined_app1
      source prefix field-set src_prefix_set1
      destination prefix field-set dest_prefix_set1
      protocol tcp source port field-set src_port_set1 destination port field-set dest_port_set1
      protocol udp source port field-set src_port_set2 destination port field-set dest_port_set2
      protocol 25
      dscp 12-19 af43 af41 ef 1-4,6 32-33,34-35 11 56-57, 58 59-60, 61-62
   !
   application ipv4 user_defined_app2
      source prefix field-set src_prefix_set2
      destination prefix field-set dest_prefix_set2
      protocol icmp
      protocol pim
      protocol tcp
      protocol 7-11, 21
      dscp ef 1-42 cs1
   !
   application l4 l4-app-1
      protocol tcp source port field-set src_port_set1 destination port field-set dest_port_set1
      protocol udp source port field-set src_port_set1 destination port field-set dest_port_set1
   !
   application l4 l4-app-2
      protocol tcp
      protocol 27, 41-44
   !
   category best-effort
      application aimini service peer-to-peer
      application apple_update service software-update
   !
   category category1
      application aim service audio-video
      application aim service chat
      application anydesk
   !
   category empty
   !
   application-profile app_profile_1
      application aim service audio-video
      application aim service chat
      application user_defined_app1
      application http transport
      application udp transport
      category best-effort
      category category1 service audio-video
   !
   application-profile app_profile_2
      application aim service audio-video
      application user_defined_app2
      application https transport
      application quic transport
      category category1 service chat
   !
   field-set ipv4 prefix dest_prefix_set1
      2.3.4.0/24
   !
   field-set ipv4 prefix dest_prefix_set2
      4.4.4.0/24
   !
   field-set ipv4 prefix empty-ipv4-prefixes
   !
   field-set ipv4 prefix order-test
      192.168.42.0/24 192.168.43.0/24 6.6.6.6/32
   !
   field-set ipv4 prefix src_prefix_set1
      1.2.3.0/24 1.2.5.0/24
   !
   field-set ipv4 prefix src_prefix_set2
      2.2.2.0/24 3.3.3.0/24
   !
   field-set l4-port dest_port_set1
      2300-2350
   !
   field-set l4-port dest_port_set2
      3300-3350
   !
   field-set l4-port empty-l4-ports
   !
   field-set l4-port ordering-test
      101-103, 650, 666
   !
   field-set l4-port src_port_set1
      2400-2500, 2900-3000
   !
   field-set l4-port src_port_set2
      5700-5800, 6500-6600
```

## Group-Based Multi-domain Segmentation Services (MSS-Group)

MSS-G is enabled.

### Segmentation Policies

#### POLICY-TEST1

| Sequence Number | Application Name | Action | Next-Hop | Log | Stateless |
| --------------- | ---------------- | ------ | -------- | --- | --------- |
| 10 | APP-TEST-1 | forward | - | - | False |
| 20 | APP-TEST-2 | drop | - | True | - |
| 25 | APP-TEST-3 | redirect | 198.51.100.1 | - | - |

### Segment Definitions

#### VRF default Segmentation

##### Segment SEGMENT-TEST1 Definitions

| Interface | Match-List Name | Covered Prefix-List Name | Address Family |
| --------- |---------------- | ------------------------ | -------------- |
| - | MATCH-LIST10 | - | ipv4 |
| - | MATCH-LIST11 | - | ipv6 |

##### Segment SEGMENT-TEST1 Policies

| Source Segment | Policy Applied |
| -------------- | -------------- |
| MATCH-LIST22 | POLICY-TEST1 |

##### Segment SEGMENT-TEST2 Definitions

| Interface | Match-List Name | Covered Prefix-List Name | Address Family |
| --------- |---------------- | ------------------------ | -------------- |
| - | MATCH-LIST4 | - | ipv4 |
| - | MATCH-LIST3 | - | ipv6 |

##### Segment SEGMENT-TEST2 Policies

| Source Segment | Policy Applied |
| -------------- | -------------- |
| MATCH-LIST20 | policy-forward-all |
| MATCH-LIST21 | POLICY-TEST1 |
| MATCH-LIST30 | policy-drop-all |

#### VRF SECURE Segmentation

##### Segment SEGMENT-TEST1 Definitions

| Interface | Match-List Name | Covered Prefix-List Name | Address Family |
| --------- |---------------- | ------------------------ | -------------- |
| Ethernet1 | - | - | - |
| Ethernet2 | - | - | - |
| - | - | PREFIX-LIST10 | ipv4 |
| - | - | PREFIX-LIST1 | ipv6 |

##### Segment SEGMENT-TEST1 Policies

| Source Segment | Policy Applied |
| -------------- | -------------- |
| MATCH-LIST20 | policy-forward-all |
| MATCH-LIST30 | policy-drop-all |

Configured Fallback Policy: policy-custom

### Router MSS-G Device Configuration

```eos
!
router segment-security
   no shutdown
   !
   policy POLICY-TEST1
      10 application APP-TEST-1 action forward
      20 application APP-TEST-2 action drop stateless log
      25 application APP-TEST-3 action redirect next-hop 198.51.100.1 stateless
   !
   vrf default
      segment SEGMENT-TEST1
         definition
            match prefix-ipv4 MATCH-LIST10
            match prefix-ipv6 MATCH-LIST11
         !
         policies
            from MATCH-LIST22 policy POLICY-TEST1
      !
      segment SEGMENT-TEST2
         definition
            match prefix-ipv4 MATCH-LIST4
            match prefix-ipv6 MATCH-LIST3
         !
         policies
            from MATCH-LIST20 policy policy-forward-all
            from MATCH-LIST21 policy POLICY-TEST1
            from MATCH-LIST30 policy policy-drop-all
   !
   vrf SECURE
      segment SEGMENT-TEST1
         definition
            match interface Ethernet1
            match interface Ethernet2
            match covered prefix-list ipv4 PREFIX-LIST10
            match covered prefix-list ipv6 PREFIX-LIST1
         !
         policies
            from MATCH-LIST20 policy policy-forward-all
            from MATCH-LIST30 policy policy-drop-all
            fallback policy policy-custom
   !
```

### Router Path-selection

#### Router Path-selection Summary

| Setting | Value |
| ------  | ----- |
| Dynamic peers source | STUN |

#### TCP MSS Ceiling Configuration

| IPV4 segment size | Direction |
| ----------------- | --------- |
| 200 | ingress |

#### Path Groups

##### Path Group PG-1

| Setting | Value |
| ------  | ----- |
| Path Group ID | 666 |
| Keepalive interval(failure threshold) | 200(3) |

###### Dynamic Peers Settings

| Setting | Value |
| ------  | ----- |
| IP Local | True |
| IPSec | True |

###### Static Peers

| Router IP | Name | IPv4 address(es) |
| --------- | ---- | ---------------- |
| 172.16.1.42 | - | - |
| 172.16.2.42 | - | 192.168.2.42 |
| 172.16.42.42 | TEST-STATIC-PEER-WITH-NAME | 192.168.42.42<br>192.168.1.42 |

##### Path Group PG-2

| Setting | Value |
| ------  | ----- |
| Path Group ID | 42 |
| IPSec profile | IPSEC-P-1 |
| Keepalive interval | auto |
| Flow assignment | LAN |

###### Local Interfaces

| Interface name | Public address | STUN server profile(s) |
| -------------- | -------------- | ---------------------- |
| Ethernet1/1 | - |  |
| Ethernet1/1/3 | - |  |
| Ethernet2 | 192.168.42.42 | STUN-P-1<br>STUN-P-2 |
| Ethernet2/4.666 | - |  |
| Ethernet3 | - | STUN-P-1 |
| Ethernet4.666 | - |  |
| Port-Channel1 | 192.168.42.43 | STUN-P-1<br>STUN-P-2 |
| Port-Channel4.666 | - |  |

###### Local IPs

| IP address | Public address | STUN server profile(s) |
| ---------- | -------------- | ---------------------- |
| 192.168.1.100 | 192.168.42.42 | STUN-P-1<br>STUN-P-2 |
| 192.168.100.1 | - | STUN-P-1 |

###### Dynamic Peers Settings

| Setting | Value |
| ------  | ----- |
| IP Local | - |
| IPSec | False |

##### Path Group PG-3

| Setting | Value |
| ------  | ----- |
| Path Group ID | 888 |

##### Path Group PG-4

| Setting | Value |
| ------  | ----- |
| Path Group ID | - |

#### Load-balance Policies

| Policy Name | Jitter (ms) | Latency (ms) | Loss Rate (%) | Path Groups (priority) | Lowest Hop Count |
| ----------- | ----------- | ------------ | ------------- | ---------------------- | ---------------- |
| LB-EMPTY | - | - | - |  | False |
| LB-P-1 | - | - | 17 | PG-5 (1)<br>PG-2 (42)<br>PG-4 (42)<br>PG-3 (666) | True |
| LB-P-2 | 666 | 42 | 42.42 | PG-1 (1)<br>PG-3 (1) | False |

#### DPS Policies

##### DPS Policy DPS-P-1

| Rule ID | Application profile | Load-balance policy |
| ------- | ------------------- | ------------------- |
| Default Match | - | LB-P-1 |
| 42 | AP-3 | LB-P-1 |

##### DPS Policy DPS-P-2

| Rule ID | Application profile | Load-balance policy |
| ------- | ------------------- | ------------------- |
| Default Match | - | LB-P-2 |

##### DPS Policy DPS-P-3

| Rule ID | Application profile | Load-balance policy |
| ------- | ------------------- | ------------------- |
| 42 | AP-2 | - |
| 66 | AP-1 | LB-P-1 |

#### VRFs Configuration

| VRF name | DPS policy |
| -------- | ---------- |
| VRF-1 | DPS-P-1 |
| VRF-2 | DPS-P-2 |
| VRF-3 | - |

#### Router Path-selection Device Configuration

```eos
!
router path-selection
   peer dynamic source stun
   tcp mss ceiling ipv4 200 ingress
   !
   path-group PG-1 id 666
      keepalive interval 200 milliseconds failure-threshold 3 intervals
      !
      peer dynamic
         ip local
         ipsec
      !
      peer static router-ip 172.16.1.42
      !
      peer static router-ip 172.16.2.42
         ipv4 address 192.168.2.42
      !
      peer static router-ip 172.16.42.42
         name TEST-STATIC-PEER-WITH-NAME
         ipv4 address 192.168.42.42
         ipv4 address 192.168.1.42
   !
   path-group PG-2 id 42
      ipsec profile IPSEC-P-1
      keepalive interval auto
      flow assignment lan
      !
      local interface Ethernet1/1
      !
      local interface Ethernet1/1/3
      !
      local interface Ethernet2 public address 192.168.42.42
         stun server-profile STUN-P-1 STUN-P-2
      !
      local interface Ethernet2/4.666
      !
      local interface Ethernet3
         stun server-profile STUN-P-1
      !
      local interface Ethernet4.666
      !
      local interface Port-Channel1 public address 192.168.42.43
         stun server-profile STUN-P-1 STUN-P-2
      !
      local interface Port-Channel4.666
      !
      local ip 192.168.1.100 public address 192.168.42.42
         stun server-profile STUN-P-1 STUN-P-2
      !
      local ip 192.168.100.1
         stun server-profile STUN-P-1
      !
      peer dynamic
         ipsec disabled
   !
   path-group PG-3 id 888
   !
   path-group PG-4
   !
   load-balance policy LB-EMPTY
   !
   load-balance policy LB-P-1
      loss-rate 17
      hop count lowest
      path-group PG-5
      path-group PG-2 priority 42
      path-group PG-4 priority 42
      path-group PG-3 priority 666
   !
   load-balance policy LB-P-2
      latency 42
      jitter 666
      loss-rate 42.42
      path-group PG-1 priority 1
      path-group PG-3
   !
   policy DPS-P-1
      default-match
         load-balance LB-P-1
      !
      42 application-profile AP-3
         load-balance LB-P-1
   !
   policy DPS-P-2
      default-match
         load-balance LB-P-2
   !
   policy DPS-P-3
      42 application-profile AP-2
      !
      66 application-profile AP-1
         load-balance LB-P-1
   !
   vrf VRF-1
      path-selection-policy DPS-P-1
   !
   vrf VRF-2
      path-selection-policy DPS-P-2
   !
   vrf VRF-3
```

### Router Internet Exit

#### Exit Groups

| Exit Group Name | Local Connections | Fib Default |
| --------------- | ----------------- | ----------- |
| eg_01 | - | - |
| eg_02 | - | True |
| eg_03 | eg_03_lo_01<br>eg_03_lo_02 | True |
| eg_04 | eg_04_lo_01<br>eg_04_lo_02<br>eg_04_lo_03 | - |

#### Internet Exit Policies

| Policy Name | Exit Groups |
| ----------- | ----------- |
| po_01 | po_eg_01_02<br>po_eg_01_04<br>po_eg_01_01<br>po_eg_01_03<br>system-default-exit-group |
| po_02 | - |
| po_03 | po_eg_03_01 |

#### Router Internet Exit Device Configuration

```eos
!
router internet-exit
   exit-group eg_01
   !
   exit-group eg_02
      fib-default
   !
   exit-group eg_03
      local connection eg_03_lo_01
      local connection eg_03_lo_02
      fib-default
   !
   exit-group eg_04
      local connection eg_04_lo_01
      local connection eg_04_lo_02
      local connection eg_04_lo_03
   !
   policy po_01
      exit-group po_eg_01_02
      exit-group po_eg_01_04
      exit-group po_eg_01_01
      exit-group po_eg_01_03
      exit-group system-default-exit-group
   !
   policy po_02
   !
   policy po_03
      exit-group po_eg_03_01
```

## Router L2 VPN

### Router L2 VPN Summary

- ARP learning bridged is enabled.

- VXLAN ARP Proxying is disabled for IPv4 addresses defined in the prefix-list pl-router-l2-vpn.

- Selective ARP is enabled.

- ND learning bridged is enabled.

- VXLAN ND Proxying is disabled for IPv6 addresses defined in the prefix-list pl-router-l2-vpn.

- Neighbor discovery router solicitation VTEP flooding is disabled.

- Virtual router neighbor advertisement VTEP flooding is disabled.

### Router L2 VPN Device Configuration

```eos
!
router l2-vpn
   arp learning bridged
   arp proxy prefix-list pl-router-l2-vpn
   arp selective-install
   nd learning bridged
   nd proxy prefix-list pl-router-l2-vpn
   nd rs flooding disabled
   virtual-router neighbor advertisement flooding disabled
```

## IP DHCP Relay

### IP DHCP Relay Summary

IP DHCP Relay Option 82 is enabled.

DhcpRelay Agent is in always-on mode.

Forwarding requests with secondary IP addresses in the "giaddr" field is allowed.

### IP DHCP Relay Device Configuration

```eos
!
ip dhcp relay information option
ip dhcp relay always-on
ip dhcp relay all-subnets default
```

## IPv6 DHCP Relay

### IPv6 DHCP Relay Summary

DhcpRelay Agent is in always-on mode.

Forwarding requests with additional IPv6 addresses in the "giaddr" field is allowed.

Add Option 79 - Link Layer Address Option.

Add RemoteID option 37 in format MAC address and interface ID.

### IPv6 DHCP Relay Device Configuration

```eos
!
ipv6 dhcp relay always-on
ipv6 dhcp relay all-subnets default
ipv6 dhcp relay option link-layer address
ipv6 dhcp relay option remote-id format %m:%i
```

## IP DHCP Snooping

IP DHCP Snooping is enabled

IP DHCP Snooping Bridging is enabled

IP DHCP Snooping Insertion of Option 82 is enabled

IP DHCP Snooping Circuit-ID Suboption: 10

IP DHCP Snooping Circuit-ID Format: %h:%p

IP DHCP Snooping enabled VLAN: 10,20,500,1000-2000

### IP DHCP Snooping Device Configuration

```eos
!
ip dhcp snooping bridging
ip dhcp snooping information option
ip dhcp snooping information option circuit-id type 10 format %h:%p
ip dhcp snooping vlan 10,20,500,1000-2000
```

## IP NAT

| Setting | Value |
| -------- | ----- |
| Kernel Buffer Size | 64 MB |

### NAT Profiles

#### Profile: NAT-PROFILE-NO-VRF-1

#### Profile: NAT-PROFILE-NO-VRF-2

##### IP NAT: Source Static

| Direction | Original IP | Original Port | Access List | Translated IP | Translated Port | Protocol | Group | Priority | Comment |
| --------- | ----------- | ------------- | ----------- | ------------- | --------------- | -------- | ----- | -------- | ------- |
| - | 3.0.0.1 | - | - | 4.0.0.1 | - | - | - | 0 | - |
| - | 3.0.0.2 | 22 | - | 4.0.0.2 | - | - | - | 0 | - |
| - | 3.0.0.3 | 22 | - | 4.0.0.3 | 23 | - | - | 0 | - |
| - | 3.0.0.4 | 22 | - | 4.0.0.4 | 23 | UDP | - | 0 | - |
| - | 3.0.0.5 | 22 | - | 4.0.0.5 | 23 | TCP | 1 | 0 | - |
| - | 3.0.0.6 | 22 | - | 4.0.0.6 | 23 | TCP | 2 | 5 | Comment Test |
| - | 3.0.0.7 | - | ACL21 | 4.0.0.7 | - | - | - | 0 | - |
| ingress | 3.0.0.8 | - | - | 4.0.0.8 | - | - | - | 0 | - |

##### IP NAT: Source Dynamic

| Access List | NAT Type | Pool Name | Priority | Comment |
| ----------- | -------- | --------- | -------- | ------- |
| ACL11 | pool | POOL11 | 0 | - |
| ACL12 | pool | POOL11 | 0 | POOL11 shared with ACL11/12 |
| ACL13 | pool | POOL13 | 10 | - |
| ACL14 | pool | POOL14 | 1 | Priority low end |
| ACL15 | pool | POOL15 | 4294967295 | Priority high end |
| ACL16 | pool | POOL16 | 0 | Priority default |
| ACL17 | overload | - | 10 | Priority_10 |
| ACL18 | pool-address-only | POOL18 | 10 | Priority_10 |
| ACL19 | pool-full-cone | POOL19 | 10 | Priority_10 |

##### IP NAT: Destination Static

| Direction | Original IP | Original Port | Access List | Translated IP | Translated Port | Protocol | Group | Priority | Comment |
| --------- | ----------- | ------------- | ----------- | ------------- | --------------- | -------- | ----- | -------- | ------- |
| - | 1.0.0.1 | - | - | 2.0.0.1 | - | - | - | 0 | - |
| - | 1.0.0.2 | 22 | - | 2.0.0.2 | - | - | - | 0 | - |
| - | 1.0.0.2 | 23 | - | 2.0.0.3 | 23 | - | - | 0 | - |
| - | 1.0.0.4 | 22 | - | 2.0.0.4 | 23 | udp | - | 0 | - |
| - | 1.0.0.5 | 22 | - | 2.0.0.5 | 23 | tcp | 1 | 0 | - |
| - | 1.0.0.6 | 22 | - | 2.0.0.6 | 23 | tcp | 2 | 5 | Comment Test |
| - | 1.0.0.7 | - | ACL21 | 2.0.0.7 | - | - | - | 0 | - |
| egress | 239.0.0.1 | - | - | 239.0.0.2 | - | - | - | 0 | - |

##### IP NAT: Destination Dynamic

| Access List | Pool Name | Priority | Comment |
| ----------- | --------- | -------- | ------- |
| ACL1 | POOL1 | 0 | - |
| ACL2 | POOL1 | 0 | POOL1 shared with ACL1/2 |
| ACL3 | POOL3 | 10 | - |
| ACL4 | POOL4 | 1 | Priority low end |
| ACL5 | POOL5 | 4294967295 | Priority high end |
| ACL6 | POOL6 | 0 | Priority default |

#### Profile: NAT-PROFILE-TEST-VRF

NAT profile VRF is: TEST

### NAT Pools

| Pool Name | Pool Type | Prefix Length | Utilization Log Threshold | First-Last IP Addresses | First-Last Ports |
| --------- | --------- | ------------- | ------------------------- | ----------------------- | ---------------- |
| port_only_1 | port-only | - | - | - | - |
| port_only_2 | port-only | - | - | - | 1024-65535 |
| prefix_16 | ip-port | 16 | 91 | 10.0.0.1-10.0.255.254<br>10.1.0.0-10.1.255.255 | -<br>1024-65535 |
| prefix_21 | ip-port | 21 | - | - | - |
| prefix_24 | ip-port | 24 | 100 | - | - |
| prefix_32 | ip-port | 32 | - | 10.2.0.1-10.2.0.1<br>10.2.0.2-10.2.0.2 | 1024-65535<br>- |
| prefix_32_without_ip | ip-port | 32 | - | - | 1024-65535 |

### NAT Synchronization

| Setting | Value |
| -------- | ----- |
| State | Disabled |
| Expiry Interval | 60 Seconds |
| Interface | Ethernet1 |
| Peer IP Address | 1.1.1.1 |
| Port Range | 1024 - 65535 |
| Port Range Split | Disabled |

### NAT Translation Settings

| Setting | Value |
| -------- | ----- |
| Address Selection | Any |
| Address Selection | Hash Source IP Field |
| Counters | Enabled |
| Global Connection Limit | max. 100000 Connections |
| per Host Connection Limit | max. 1000 Connections |
| IP Host 10.0.0.1 Connection Limit | max. 100 Connections |
| IP Host 10.0.0.2 Connection Limit | max. 200 Connections |
| Global Connection Limit Low Mark | 50 % |
| per Host Connection Limit Low Mark | 50 % |
| UDP Connection Timeout | 3600 Seconds |
| TCP Connection Timeout | 7200 Seconds |

### IP NAT Device Configuration

```eos
!
ip nat translation address selection hash field source-ip
ip nat translation address selection any
ip nat translation tcp-timeout 7200
ip nat translation udp-timeout 3600
ip nat translation max-entries 100000
ip nat translation low-mark 50
ip nat translation max-entries 1000 host
ip nat translation low-mark 50 host
ip nat translation max-entries 100 10.0.0.1
ip nat translation max-entries 200 10.0.0.2
ip nat kernel buffer size 64
!
ip nat profile NAT-PROFILE-NO-VRF-1
!
ip nat profile NAT-PROFILE-NO-VRF-2
   ip nat destination static 1.0.0.1 2.0.0.1
   ip nat destination static 1.0.0.2 22 2.0.0.2
   ip nat destination static 1.0.0.2 23 2.0.0.3 23
   ip nat destination static 1.0.0.4 22 2.0.0.4 23 protocol udp
   ip nat destination static 1.0.0.7 access-list ACL21 2.0.0.7
   ip nat source static 3.0.0.1 4.0.0.1
   ip nat source static 3.0.0.2 22 4.0.0.2
   ip nat source static 3.0.0.3 22 4.0.0.3 23
   ip nat source static 3.0.0.4 22 4.0.0.4 23 protocol udp
   ip nat source static 3.0.0.7 access-list ACL21 4.0.0.7
   ip nat source ingress static 3.0.0.8 4.0.0.8
   ip nat destination egress static 239.0.0.1 239.0.0.2
   ip nat source static 3.0.0.5 22 4.0.0.5 23 protocol tcp group 1
   ip nat destination static 1.0.0.5 22 2.0.0.5 23 protocol tcp group 1
   ip nat source static 3.0.0.6 22 4.0.0.6 23 protocol tcp group 2 comment Comment Test
   ip nat destination static 1.0.0.6 22 2.0.0.6 23 protocol tcp group 2 comment Comment Test
   ip nat destination dynamic access-list ACL1 pool POOL1
   ip nat source dynamic access-list ACL11 pool POOL11
   ip nat source dynamic access-list ACL12 pool POOL11 comment POOL11 shared with ACL11/12
   ip nat source dynamic access-list ACL13 pool POOL13 priority 10
   ip nat source dynamic access-list ACL14 pool POOL14 priority 1 comment Priority low end
   ip nat source dynamic access-list ACL15 pool POOL15 priority 4294967295 comment Priority high end
   ip nat source dynamic access-list ACL16 pool POOL16 comment Priority default
   ip nat source dynamic access-list ACL17 overload priority 10 comment Priority_10
   ip nat source dynamic access-list ACL18 pool POOL18 address-only priority 10 comment Priority_10
   ip nat source dynamic access-list ACL19 pool POOL19 full-cone priority 10 comment Priority_10
   ip nat destination dynamic access-list ACL2 pool POOL1 comment POOL1 shared with ACL1/2
   ip nat destination dynamic access-list ACL3 pool POOL3 priority 10
   ip nat destination dynamic access-list ACL4 pool POOL4 priority 1 comment Priority low end
   ip nat destination dynamic access-list ACL5 pool POOL5 priority 4294967295 comment Priority high end
   ip nat destination dynamic access-list ACL6 pool POOL6 comment Priority default
!
ip nat profile NAT-PROFILE-TEST-VRF vrf TEST
!
ip nat pool prefix_16 prefix-length 16
   range 10.0.0.1 10.0.255.254
   range 10.1.0.0 10.1.255.255 1024 65535
   utilization threshold 91 action log
ip nat pool prefix_21 prefix-length 21
ip nat pool prefix_24 prefix-length 24
   utilization threshold 100 action log
ip nat pool prefix_32 prefix-length 32
   range 10.2.0.1 10.2.0.1 1024 65535
   range 10.2.0.2 10.2.0.2
ip nat pool prefix_32_without_ip prefix-length 32
ip nat pool port_only_1 port-only
ip nat pool port_only_2 port-only
   port range 1024 65535
ip nat synchronization
   description test sync config
   expiry-interval 60
   shutdown
   peer-address 1.1.1.1
   local-interface Ethernet1
   port-range 1024 65535
   port-range split disabled
```

## Errdisable

### Errdisable Summary

|  Detect Cause | Enabled |
| ------------- | ------- |
| acl | True |
| arp-inspection | True |
| dot1x | True |
| link-change | True |
| tapagg | True |
| xcvr-misconfigured | True |
| xcvr-overheat | True |
| xcvr-power-unsupported | True |

|  Detect Cause | Enabled | Interval |
| ------------- | ------- | -------- |
| arp-inspection | True | 300 |
| bpduguard | True | 300 |
| dot1x | True | 300 |
| hitless-reload-down | True | 300 |
| lacp-rate-limit | True | 300 |
| link-flap | True | 300 |
| no-internal-vlan | True | 300 |
| portchannelguard | True | 300 |
| portsec | True | 300 |
| speed-misconfigured | True | 300 |
| tapagg | True | 300 |
| uplink-failure-detection | True | 300 |
| xcvr-misconfigured | True | 300 |
| xcvr-overheat | True | 300 |
| xcvr-power-unsupported | True | 300 |
| xcvr-unsupported | True | 300 |

```eos
!
errdisable detect cause acl
errdisable detect cause arp-inspection
errdisable detect cause dot1x
errdisable detect cause link-change
errdisable detect cause tapagg
errdisable detect cause xcvr-misconfigured
errdisable detect cause xcvr-overheat
errdisable detect cause xcvr-power-unsupported
errdisable recovery cause arp-inspection
errdisable recovery cause bpduguard
errdisable recovery cause dot1x
errdisable recovery cause hitless-reload-down
errdisable recovery cause lacp-rate-limit
errdisable recovery cause link-flap
errdisable recovery cause no-internal-vlan
errdisable recovery cause portchannelguard
errdisable recovery cause portsec
errdisable recovery cause speed-misconfigured
errdisable recovery cause tapagg
errdisable recovery cause uplink-failure-detection
errdisable recovery cause xcvr-misconfigured
errdisable recovery cause xcvr-overheat
errdisable recovery cause xcvr-power-unsupported
errdisable recovery cause xcvr-unsupported
errdisable recovery interval 300
```

## Quality Of Service

### QOS Class Maps

#### QOS Class Maps Summary

| Name | Field | Value |
| ---- | ----- | ----- |
| CM_IPv6_ACCESS_GROUP | - | - |
| CM_REPLICATION_LD | acl | ACL_REPLICATION_LD |
| CM_REPLICATION_LD2 | vlan | 200 |
| CM_REPLICATION_LD3 | cos | 3 |
| COS_RANGE | vlan | 1-3 |
| VLAN_RANGE | vlan | 200-400 |

#### Class-maps Device Configuration

```eos
!
class-map type qos match-any CM_IPv6_ACCESS_GROUP
   match ipv6 access-group ACL_REPLICATION_LD
!
class-map type qos match-any CM_REPLICATION_LD
   match ip access-group ACL_REPLICATION_LD
!
class-map type qos match-any CM_REPLICATION_LD2
   match vlan 200
!
class-map type qos match-any CM_REPLICATION_LD3
   match cos 3
!
class-map type qos match-any COS_RANGE
   match vlan 1-3
!
class-map type qos match-any VLAN_RANGE
   match vlan 200-400
!
class-map type pbr match-any CM_PBR_EXCLUDE
   match ip access-group ACL_PBR_EXCLUDE
!
class-map type pbr match-any CM_PBR_INCLUDE
   match ip access-group ACL_PBR_INCLUDE
!
class-map type pbr match-any CM_PBR_WITHOUT_ACCESS_GROUP
```

### QOS Policy Maps

#### QOS Policy Maps Summary

##### PM_REPLICATION_LD

| Class Name | COS | DSCP | Traffic Class | Drop Precedence | Police Rate (Burst) -> Action |
| ---------- | --- | -----| ------------- | --------------- | ----------------------------- |
| CM_REPLICATION_LD | - | af11 | 2 | 1 | 10 kbps (260 kbytes) -> drop-precedence<br> 30 kbps(270 kbytes) -> drop |
| CM_REPLICATION_LD_2 | - | af11 | 2 | - | - |

##### PM_REPLICATION_LD2

| Class Name | COS | DSCP | Traffic Class | Drop Precedence | Police Rate (Burst) -> Action |
| ---------- | --- | -----| ------------- | --------------- | ----------------------------- |
| CM_REPLICATION_LD | 4 | af11 | - | - | 30 kbps (280 bytes) -> dscp<br> 1 mbps(270 bytes) -> drop |

##### PM_REPLICATION_LD3

| Class Name | COS | DSCP | Traffic Class | Drop Precedence | Police Rate (Burst) -> Action |
| ---------- | --- | -----| ------------- | --------------- | ----------------------------- |
| CM_REPLICATION_LD | 6 | af11 | - | - | 10000 bps (260 kbytes) -> drop |

#### QOS Policy Maps Device Configuration

```eos
!
policy-map type quality-of-service PM_REPLICATION_LD
   class CM_REPLICATION_LD
      set dscp af11
      set traffic-class 2
      set drop-precedence 1
      police rate 10 kbps burst-size 260 kbytes action set drop-precedence rate 30 kbps burst-size 270 kbytes
   !
   class CM_REPLICATION_LD_2
      set dscp af11
      set traffic-class 2
!
policy-map type quality-of-service PM_REPLICATION_LD2
   class CM_REPLICATION_LD
      set dscp af11
      set cos 4
      police rate 30 kbps burst-size 280 bytes action set dscp af11 rate 1 mbps burst-size 270 bytes
!
policy-map type quality-of-service PM_REPLICATION_LD3
   class CM_REPLICATION_LD
      set dscp af11
      set cos 6
      police rate 10000 bps burst-size 260 kbytes
```

### QOS Interfaces

| Interface | Trust | Default DSCP | Default COS | Shape rate |
| --------- | ----- | ------------ | ----------- | ---------- |
| Ethernet7 | cos | - | 5 | - |
| Ethernet21 | disabled | - | - | 200000 kbps |
| Ethernet22 | - | - | - | 10 percent |
| Port-Channel3 | - | - | - | 200000 kbps |
| Port-Channel10 | - | - | - | 50 percent |
| Port-Channel101 | disabled | - | - | - |

### Control-plane Policy Map

#### Control-plane Policy Map Summary

##### copp-system-policy

| Class | Shape | Bandwidth | Rate Unit |
| ----- | ----- | --------- | --------- |
| copp-system-cvx | 2000 | 2000 | pps |
| copp-system-OspfIsis | 1000 | 1000 | kbps |
| copp-system-rsvp | - | - | - |

#### COPP Policy Maps Device Configuration

```eos
!
policy-map type copp copp-system-policy
   class copp-system-OspfIsis
      shape kbps 1000
      bandwidth kbps 1000
   !
   class copp-system-cvx
      shape pps 2000
      bandwidth pps 2000
   !
   class copp-system-rsvp
```

## InfluxDB Telemetry

### InfluxDB Telemetry Summary

Source Group Standard Disabled : True

#### InfluxDB Telemetry Destinations

| Destination | Database | URL | VRF | Username |
| ----------- | -------- | --- | --- | -------- |
| test | test | https://influx_test.localhost | test | test |
| test1 | test1 | https://influx_test1.localhost | test | test1 |

#### InfluxDB Telemetry Sources

| Source Name | URL | Connection Limit |
| ----------- | --- | ---------------- |
| socket1 | unix:///var/run/example2.sock | 100 |
| socket2 | unix:///var/run/example3.sock | 22222 |

#### InfluxDB Telemetry Tags

| Tag | Value |
| --- | ----- |
| tag1 | value1 |
| tag2 | value2 |

### InfluxDB Telemetry Device Configuration

```eos
!
monitor telemetry influx
   destination influxdb test
      url https://influx_test.localhost
      database name test
      retention policy test
      vrf test
      username test password 7 <removed>
   !
   destination influxdb test1
      url https://influx_test1.localhost
      database name test1
      retention policy test1
      vrf test
      username test1 password 7 <removed>
   !
   source socket socket1
      url unix:///var/run/example2.sock
      connection limit 100
   !
   source socket socket2
      url unix:///var/run/example3.sock
      connection limit 22222
   tag global tag1 value1
   tag global tag2 value2
   source group standard disabled
```

## STUN

### STUN Client

#### Server Profiles

| Server Profile | IP address | SSL Profile | Port |
| -------------- | ---------- | ----------- | ---- |
| server1 | 1.2.3.4 | pathfinder | 3478 |
| server2 | 2.3.4.5 | - | 4100 |

### STUN Server

| Server Local Interfaces | Bindings Timeout (s) | SSL Profile | SSL Connection Lifetime | Port |
| ----------------------- | -------------------- | ----------- | ----------------------- | ---- |
| Ethernet1<br>Ethernet13<br>Vlan42<br>Vlan666 | 600 | pathfinder | 1300 minutes | 4100 |

### STUN Device Configuration

```eos
!
stun
   client
      server-profile server1
         ip address 1.2.3.4
         ssl profile pathfinder
      server-profile server2
         ip address 2.3.4.5
         port 4100
   server
      local-interface Ethernet1
      local-interface Ethernet13
      local-interface Vlan42
      local-interface Vlan666
      port 4100
      ssl profile pathfinder
      binding timeout 600 seconds
      ssl connection lifetime 1300 minutes
```

## Maintenance Mode

### BGP Groups

#### BGP Groups Summary

| BGP group | VRF Name | Neighbors | BGP maintenance profiles |
| --------- | -------- | --------- | ------------------------ |
| bar | red | peer-group-baz | downlink-neighbors |
| foo | - | 169.254.1.1<br>fe80::1 | ixp<br>uplink-neighbors |
| without-neighbors-key | red | - | BP1 |

#### BGP Groups Device Configuration

```eos
!
group bgp bar
   vrf red
   neighbor peer-group-baz
   maintenance profile bgp downlink-neighbors
!
group bgp foo
   neighbor 169.254.1.1
   neighbor fe80::1
   maintenance profile bgp ixp
   maintenance profile bgp uplink-neighbors
!
group bgp without-neighbors-key
   vrf red
```

### Interface Groups

#### Interface Groups Summary

| Interface Group | Interfaces | Interface maintenance profile | BGP maintenance profiles |
| --------------- | ---------- | ----------------------------- | ------------------------ |
| QSFP_Interface_Group | Ethernet1,5 | uplink-interfaces | BP1 |
| QSFP_Interface_Group1 | Ethernet1,5 | IP1 | BP1 |
| SFP_Interface_Group | Ethernet10-20<br>Ethernet30-48 | downlink-interfaces<br>ix-interfaces | downlink-neighbors<br>local-ix |

#### Interface Groups Device Configuration

```eos
!
group interface QSFP_Interface_Group
   interface Ethernet1,5
   maintenance profile interface uplink-interfaces
!
group interface QSFP_Interface_Group1
   interface Ethernet1,5
!
group interface SFP_Interface_Group
   interface Ethernet10-20
   interface Ethernet30-48
   maintenance profile bgp downlink-neighbors
   maintenance profile bgp local-ix
   maintenance profile interface downlink-interfaces
   maintenance profile interface ix-interfaces
```

### Maintenance

#### Maintenance defaults

Default maintenance bgp profile: **BP1**

Default maintenance interface profile: **IP1**

Default maintenance unit profile: **UP1**

#### Maintenance profiles

| BGP profile | Initiator route-map |
| ----------- | ------------------- |
| BP1 | RM-MAINTENANCE |
| BP2 | RM-MAINTENANCE2 |
| BP3 | RM-MAINTENANCE3 |

| Interface profile | Rate monitoring load interval (s) | Rate monitoring threshold in/out (kbps) | Shutdown Max Delay |
|-------------------|-----------------------------------|-----------------------------------------|--------------------|
| IP1 | 10 | 500 | 300 |

| Unit profile | on-boot duration (s) |
| ------------ | -------------------- |
| UP1 | 900 |
| UP2 | 600 |

#### Maintenance units

| Unit | Interface groups | BGP groups | Unit profile | Quiesce |
| ---- | ---------------- | ---------- | ------------ | ------- |
| System | - | - | UP1 | No |
| UNIT1 | INTERFACE_GROUP_1 | BGP_GROUP_1<br/>BGP_GROUP_2 | UP1 | No |

#### Maintenance Device Configuration

```eos
!
maintenance
   profile bgp BP1
      initiator route-map RM-MAINTENANCE inout
   !
   profile bgp BP2
      initiator route-map RM-MAINTENANCE2 inout
   !
   profile bgp BP3
      initiator route-map RM-MAINTENANCE3 inout
   profile bgp BP1 default
   profile interface IP1 default
   profile unit UP1 default
   !
   profile interface IP1
      rate-monitoring load-interval 10
      rate-monitoring threshold 500
      shutdown max-delay 300
   !
   profile unit UP1
      on-boot duration 900
   !
   profile unit UP2
      on-boot duration 600
   !
   unit System
   !
   unit UNIT1
      group bgp BGP_GROUP_1
      group bgp BGP_GROUP_2
      group interface INTERFACE_GROUP_1
      profile unit UP1
```
