# host1

## Table of Contents

- [Management](#management)
  - [Agents](#agents)
  - [Management Interfaces](#management-interfaces)
  - [IP Domain-list](#ip-domain-list)
  - [Clock Settings](#clock-settings)
  - [NTP](#ntp)
  - [Management SSH](#management-ssh)
  - [Management Tech-Support](#management-tech-support)
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
- [System Boot Settings](#system-boot-settings)
  - [Boot Secret Summary](#boot-secret-summary)
  - [System Boot Device Configuration](#system-boot-device-configuration)
- [Monitoring](#monitoring)
  - [Custom daemons](#custom-daemons)
  - [MCS Client Summary](#mcs-client-summary)
  - [Monitor Sessions](#monitor-sessions)
  - [Tap Aggregation](#tap-aggregation)
  - [SFlow](#sflow)
  - [VM Tracer Sessions](#vm-tracer-sessions)
  - [Object Tracking](#object-tracking)
  - [Monitor Telemetry Postcard Policy](#monitor-telemetry-postcard-policy)
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
  - [DPS Interfaces](#dps-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [Tunnel Interfaces](#tunnel-interfaces)
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
  - [PBR Policy Maps](#pbr-policy-maps)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
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
  - [Router Multicast](#router-multicast)
  - [PIM Sparse Mode](#pim-sparse-mode)
  - [Router MSDP](#router-msdp)
  - [Router IGMP](#router-igmp)
- [Filters](#filters)
  - [Peer Filters](#peer-filters)
  - [Route-maps](#route-maps)
  - [Match-lists](#match-lists)
  - [AS Path Lists](#as-path-lists)
- [802.1X Port Security](#8021x-port-security)
  - [802.1X Summary](#8021x-summary)
- [ACL](#acl)
  - [MAC Access-lists](#mac-access-lists)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
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
- [IPv6 DHCP Relay](#ipv6-dhcp-relay)
  - [IPv6 DHCP Relay Summary](#ipv6-dhcp-relay-summary)
  - [IPv6 DHCP Relay Device Configuration](#ipv6-dhcp-relay-device-configuration)
- [Quality Of Service](#quality-of-service)
  - [QOS Class Maps](#qos-class-maps)
  - [QOS Policy Maps](#qos-policy-maps)
  - [Control-plane Policy Map](#control-plane-policy-map)
- [InfluxDB Telemetry](#influxdb-telemetry)
  - [InfluxDB Telemetry Summary](#influxdb-telemetry-summary)
  - [InfluxDB Telemetry Device Configuration](#influxdb-telemetry-device-configuration)
- [STUN](#stun)
  - [STUN Client](#stun-client)
  - [STUN Server](#stun-server)
  - [STUN Device Configuration](#stun-device-configuration)
- [Maintenance Mode](#maintenance-mode)
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
| Ethernet0 | both | ipv6 | ipv6ACL | - |
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
monitor session myMonitoringSession1 source Ethernet0 ipv6 access-group ipv6ACL
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
   password 7 encrypted_password
   autovlan disable
   vrf MGMT
   source-interface Management1
!
vmtracer session session_2
   url https://192.168.0.10
   username user1
   password 7 encrypted_password
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
| 1 - 128 | False | 0 |

### LACP Device Configuration

```eos
!
lacp system-priority 0
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
| default | 1.1.1.0/24 | 10.1.1.1 | vlan101 | 1 | - | - | - |
| default | 1.1.2.0/24 | 10.1.1.1 | vlan101 | 200 | 666 | RT-TO-FAKE-DMZ | - |
| customer01 | 1.2.1.0/24 | 10.1.2.1 | vlan202 | 1 | - | - | - |
| customer01 | 1.2.2.0/24 | 10.1.2.1 | vlan101 | 201 | 667 | RT-TO-FAKE-DMZ | - |
| APP | 10.3.4.0/24 | 1.2.3.4 | - | 1 | - | - | - |
| APP | 10.3.5.0/24 | - | Null0 | 1 | - | - | - |
| customer01 | 10.3.6.0/24 | 11.2.1.1 (tracked with BFD) | Ethernet40 | 100 | 1000 | Track-BFD | 300 |
| customer01 | 10.3.7.0/24 | - | Ethernet41 | 100 | 1000 | No-Track-BFD | 300 |

#### Static Routes Device Configuration

```eos
!
ip route 1.1.1.0/24 Vlan101 10.1.1.1
ip route 1.1.2.0/24 Vlan101 10.1.1.1 200 tag 666 name RT-TO-FAKE-DMZ
ip route vrf APP 10.3.4.0/24 1.2.3.4
ip route vrf APP 10.3.5.0/24 Null0
ip route vrf customer01 1.2.1.0/24 Vlan202 10.1.2.1
ip route vrf customer01 1.2.2.0/24 Vlan101 10.1.2.1 201 tag 667 name RT-TO-FAKE-DMZ
ip route vrf customer01 10.3.6.0/24 Ethernet40 11.2.1.1 track bfd 100 tag 1000 name Track-BFD metric 300
ip route vrf customer01 10.3.7.0/24 Ethernet41 100 tag 1000 name No-Track-BFD metric 300
```

### IPv6 Static Routes

#### IPv6 Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| default | 2a01:cb04:4e6:d300::/64 | 2a01:cb04:4e6:d100::1 | vlan101 | 1 | - | - | - |
| default | 2a01:cb04:4e6:d400::/64 | 2a01:cb04:4e6:d100::1 | vlan101 | 200 | 666 | RT-TO-FAKE-DMZ | - |
| default | 2a01:cb04:4e6:d400::/64 | 2a01:cb04:4e6:d100::1 | vlan101 | 200 | 666 | RT-TO-FAKE-DB-ZONE | 100 |
| customer01 | 2a01:cb04:4e6:a300::/64 | 2a01:cb04:4e6:100::1 | vlan101 | 1 | - | - | - |
| customer01 | 2a01:cb04:4e6:a400::/64 | 2a01:cb04:4e6:100::1 | vlan101 | 201 | 667 | RT-TO-FAKE-DMZ | - |
| customer01 | 2b01:cb04:4e6:a400::/64 | 2a01:cb04:4e6:102::1 (tracked with BFD) | vlan102 | 201 | 102 | Track-BFD | 100 |
| customer01 | 2c01:cb04:4e6:a400::/64 | - | vlan102 | 201 | 102 | No-Track-BFD | - |

#### Static Routes Device Configuration

```eos
!
ipv6 route 2a01:cb04:4e6:d300::/64 Vlan101 2a01:cb04:4e6:d100::1
ipv6 route 2a01:cb04:4e6:d400::/64 Vlan101 2a01:cb04:4e6:d100::1 200 tag 666 name RT-TO-FAKE-DMZ
ipv6 route 2a01:cb04:4e6:d400::/64 Vlan101 2a01:cb04:4e6:d100::1 200 tag 666 name RT-TO-FAKE-DB-ZONE metric 100
ipv6 route vrf customer01 2a01:cb04:4e6:a300::/64 Vlan101 2a01:cb04:4e6:100::1
ipv6 route vrf customer01 2a01:cb04:4e6:a400::/64 Vlan101 2a01:cb04:4e6:100::1 201 tag 667 name RT-TO-FAKE-DMZ
ipv6 route vrf customer01 2b01:cb04:4e6:a400::/64 Vlan102 2a01:cb04:4e6:102::1 track bfd 201 tag 102 name Track-BFD metric 100
ipv6 route vrf customer01 2c01:cb04:4e6:a400::/64 Vlan102 201 tag 102 name No-Track-BFD
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

## MPLS

### MPLS Interfaces

| Interface | MPLS IP Enabled | LDP Enabled | IGP Sync |
| --------- | --------------- | ----------- | -------- |
| Loopback99 | - | True | - |

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

## ACL

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

### Control-plane Policy Map

#### Control-plane Policy Map Summary

##### copp-system-policy

| Class | Shape | Bandwidth | Rate Unit |
| ----- | ----- | --------- | --------- |
| copp-system-aaa | - | - | - |
| copp-system-cvx | 2000 | 2000 | pps |
| copp-system-OspfIsis | 1000 | 1000 | kbps |

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
   class copp-system-aaa
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
