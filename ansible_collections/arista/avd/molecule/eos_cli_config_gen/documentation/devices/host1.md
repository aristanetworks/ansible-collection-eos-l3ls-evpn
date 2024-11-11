# hostname-set-via-hostname-var

## Table of Contents

- [Management](#management)
  - [Agents](#agents)
  - [Management Interfaces](#management-interfaces)
  - [IP Domain-list](#ip-domain-list)
  - [Clock Settings](#clock-settings)
- [CVX](#cvx)
  - [CVX Services](#cvx-services)
  - [CVX Device Configuration](#cvx-device-configuration)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [Enable Password](#enable-password)
  - [TACACS Servers](#tacacs-servers)
  - [RADIUS Server](#radius-server)
  - [AAA Server Groups](#aaa-server-groups)
  - [AAA Authentication](#aaa-authentication)
  - [AAA Authorization](#aaa-authorization)
  - [AAA Accounting](#aaa-accounting)
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
  - [SFlow](#sflow)
  - [Event Handler](#event-handler)
- [Interfaces](#interfaces)
  - [Interface Profiles](#interface-profiles)
  - [DPS Interfaces](#dps-interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
- [Routing](#routing)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [ARP](#arp)
- [BFD](#bfd)
  - [BFD Interfaces](#bfd-interfaces)
- [MPLS](#mpls)
  - [MPLS Interfaces](#mpls-interfaces)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
  - [PIM Sparse Mode](#pim-sparse-mode)
- [Filters](#filters)
  - [IP Community-lists](#ip-community-lists)
  - [IP Extended Community Lists](#ip-extended-community-lists)
  - [IP Extended Community RegExp Lists](#ip-extended-community-regexp-lists)
  - [AS Path Lists](#as-path-lists)
- [802.1X Port Security](#8021x-port-security)
  - [802.1X Summary](#8021x-summary)
- [Power Over Ethernet (PoE)](#power-over-ethernet-poe)
  - [PoE Summary](#poe-summary)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Application Traffic Recognition](#application-traffic-recognition)
  - [Applications](#applications)
  - [Application Profiles](#application-profiles)
  - [Categories](#categories)
  - [Field Sets](#field-sets)
  - [Router Application-Traffic-Recognition Device Configuration](#router-application-traffic-recognition-device-configuration)
- [IP DHCP Relay](#ip-dhcp-relay)
  - [IP DHCP Relay Summary](#ip-dhcp-relay-summary)
  - [IP DHCP Relay Device Configuration](#ip-dhcp-relay-device-configuration)
- [IP DHCP Snooping](#ip-dhcp-snooping)
  - [IP DHCP Snooping Device Configuration](#ip-dhcp-snooping-device-configuration)
- [Errdisable](#errdisable)
  - [Errdisable Summary](#errdisable-summary)
- [Quality Of Service](#quality-of-service)
  - [QOS Class Maps](#qos-class-maps)
  - [QOS Interfaces](#qos-interfaces)
- [Maintenance Mode](#maintenance-mode)
  - [BGP Groups](#bgp-groups)
  - [Interface Groups](#interface-groups)

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

### SFlow

#### SFlow Summary

sFlow is disabled.

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

## Interfaces

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

| Interface | Channel Group | ISIS Instance | ISIS BFD | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | Authentication Mode |
| --------- | ------------- | ------------- | -------- | ----------- | ---- | ----------------- | ------------- | ------------------- |
| Ethernet5 | - | ISIS_TEST | True | 99 | point-to-point | level-2 | False | md5 |
| Ethernet81/10 | 110 | *ISIS_TEST | True | *99 | *point-to-point | *level-2 | *True | *text |

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
   isis authentication mode md5
   isis authentication key 7 <removed>
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
!
interface Ethernet8.101
   description to WAN-ISP-01 Ethernet2.101 - VRF-C1
   encapsulation dot1q vlan 101
   ip address 172.31.128.1/31
   ipv6 enable
   ipv6 address 2002:ABDC::1/64
!
interface Ethernet9
   description interface_with_mpls_enabled
   no switchport
   ip address 172.31.128.9/31
   mpls ldp interface
   multicast ipv4 boundary ACL_MULTICAST out
   multicast ipv6 static
   mpls ip
!
interface Ethernet10
   description interface_with_mpls_disabled
   no switchport
   ip address 172.31.128.10/31
   no mpls ldp interface
   no mpls ip
!
interface Ethernet11
   description interface_in_mode_access_accepting_tagged_LACP
   switchport access vlan 200
   switchport mode access
   switchport
   l2-protocol encapsulation dot1q vlan 200
!
interface Ethernet12
   description interface_with_dot1q_tunnel
   switchport access vlan 300
   switchport mode dot1q-tunnel
   switchport
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
   no logging event storm-control discards
   no logging event spanning-tree
!
interface Ethernet14
   description SRV-POD02_Eth1
   logging event link-status
   switchport trunk allowed vlan 110-111,210-211
   switchport mode trunk
   switchport
!
interface Ethernet15
   description PVLAN Promiscuous Access - only one secondary
   switchport access vlan 110
   switchport mode access
   switchport
   switchport pvlan mapping 111
!
interface Ethernet16
   description PVLAN Promiscuous Trunk - vlan translation out
   switchport vlan translation out required
   switchport trunk allowed vlan 110-112
   switchport mode trunk
   switchport
   switchport vlan translation out 111-112 110
!
interface Ethernet17
   description PVLAN Secondary Trunk
   switchport trunk allowed vlan 110-112
   switchport mode trunk
   switchport
   switchport trunk private-vlan secondary
!
interface Ethernet18
   description PBR Description
   mtu 1500
   no switchport
   ip address 192.0.2.1/31
   service-policy type pbr input MyLANServicePolicy
!
interface Ethernet19
   description Switched port with no LLDP rx/tx
   switchport access vlan 110
   switchport mode access
   switchport
   no lldp transmit
   no lldp receive
   lldp tlv transmit ztp vlan 666
!
interface Ethernet20
   description Port patched through patch-panel to pseudowire
   no switchport
   no lldp transmit
   no lldp receive
!
interface Ethernet21
   description 200MBit/s shape
   switchport
   no qos trust
   shape rate 200000 kbps
!
interface Ethernet22
   description 10% shape
   switchport
   shape rate 10 percent
!
interface Ethernet23
   description Error-correction encoding
   error-correction encoding fire-code
   error-correction encoding reed-solomon
   switchport
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

| Interface | ISIS Instance | ISIS BFD | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | Authentication Mode |
| --------- | ------------- | -------- | ----------- | ---- | ----------------- | ------------- | ------------------- |
| Port-Channel110 | ISIS_TEST | True | 99 | point-to-point | level-2 | True | text |

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
!
interface Port-Channel12
   description interface_in_mode_access_with_voice
   switchport trunk native vlan 100
   switchport phone vlan 70
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
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
   isis authentication mode text
   isis authentication key 7 <removed>
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

## Routing

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

## BFD

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
| Port-Channel113 | True | True | True |
| Port-Channel114 | False | False | - |

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

### PIM Sparse Mode

#### PIM Sparse Mode Enabled Interfaces

| Interface Name | VRF Name | IP Version | Border Router | DR Priority | Local Interface |
| -------------- | -------- | ---------- | ------------- | ----------- | --------------- |
| Ethernet5 | - | IPv4 | True | 200 | - |
| Port-Channel99 | - | IPv4 | - | 200 | - |
| Vlan89 | - | IPv4 | - | - | Loopback0 |
| Vlan4094 | - | IPv4 | - | 200 | - |

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

### QOS Interfaces

| Interface | Trust | Default DSCP | Default COS | Shape rate |
| --------- | ----- | ------------ | ----------- | ---------- |
| Ethernet7 | cos | - | 5 | - |
| Ethernet21 | disabled | - | - | 200000 kbps |
| Ethernet22 | - | - | - | 10 percent |
| Port-Channel3 | - | - | - | 200000 kbps |
| Port-Channel10 | - | - | - | 50 percent |
| Port-Channel101 | disabled | - | - | - |

## Maintenance Mode

### BGP Groups

#### BGP Groups Summary

| BGP group | VRF Name | Neighbors | BGP maintenance profiles |
| --------- | -------- | --------- | ------------------------ |
| bar | red | peer-group-baz | downlink-neighbors |
| foo | - | 169.254.1.1<br>fe80::1 | ixp<br>uplink-neighbors |
| without-neighbors-key | red | - | Default |

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
| QSFP_Interface_Group | Ethernet1,5 | uplink-interfaces | Default |
| QSFP_Interface_Group1 | Ethernet1,5 | Default | Default |
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
