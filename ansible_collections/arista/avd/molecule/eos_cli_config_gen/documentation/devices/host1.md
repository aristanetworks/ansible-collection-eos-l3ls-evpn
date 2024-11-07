# host1

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
- [System Boot Settings](#system-boot-settings)
  - [Boot Secret Summary](#boot-secret-summary)
  - [System Boot Device Configuration](#system-boot-device-configuration)
- [Monitoring](#monitoring)
  - [Custom daemons](#custom-daemons)
  - [SFlow](#sflow)
- [Interfaces](#interfaces)
  - [DPS Interfaces](#dps-interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
- [Routing](#routing)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [ARP](#arp)
- [BFD](#bfd)
  - [BFD Interfaces](#bfd-interfaces)
- [MPLS](#mpls)
  - [MPLS Interfaces](#mpls-interfaces)
- [Multicast](#multicast)
  - [PIM Sparse Mode](#pim-sparse-mode)
- [Filters](#filters)
  - [AS Path Lists](#as-path-lists)
- [802.1X Port Security](#8021x-port-security)
  - [802.1X Summary](#8021x-summary)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Application Traffic Recognition](#application-traffic-recognition)
  - [Applications](#applications)
  - [Application Profiles](#application-profiles)
  - [Categories](#categories)
  - [Field Sets](#field-sets)
  - [Router Application-Traffic-Recognition Device Configuration](#router-application-traffic-recognition-device-configuration)
- [Quality Of Service](#quality-of-service)
  - [QOS Class Maps](#qos-class-maps)
  - [QOS Interfaces](#qos-interfaces)

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
| Port-Channel117 | True | True |
| Port-Channel118 | True | True (unmodified) |
| Port-Channel119 | False | False |
| Port-Channel120 | False | False (unmodified) |

## Interfaces

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
| Ethernet3 | MLAG_PEER_DC1-LEAF1B_Ethernet3 | *trunk | *2-4094 | *- | *LEAF_PEER_L3, MLAG | 3 |
| Ethernet4 | MLAG_PEER_DC1-LEAF1B_Ethernet4 | *trunk | *2-4094 | *- | *LEAF_PEER_L3, MLAG | 3 |
| Ethernet5 | DC1-AGG01_Ethernet1 | *trunk | *110,201 | *- | *- | 5 |
| Ethernet10/1 | LAG Member | *access | *110 | *- | *- | 101 |
| Ethernet10/2 | LAG Member | *trunk | *110-112 | *- | *- | 102 |
| Ethernet10/3 | LAG Member | *trunk | *110-112 | *- | *- | 103 |
| Ethernet10/4 | LAG Member LACP fallback | *trunk | *112 | *- | *- | 104 |
| Ethernet11/2 | LAG Member LACP fallback LLDP ZTP VLAN | *trunk | *112 | *- | *- | 112 |
| Ethernet15 | DC1-AGG03_Ethernet1 | *trunk | *110,201 | *- | *- | 15 |
| Ethernet16 | DC1-AGG04_Ethernet1 | *trunk | *110,201 | *10 | *- | 16 |
| Ethernet18 | LAG Member | *access | *110 | *- | *- | 109 |
| Ethernet50 | SRV-POD03_Eth1 | *trunk | *110,201 | *- | *- | 5 |

*Inherited from Port-Channel Interface

##### Transceiver Settings

| Interface | Transceiver Frequency | Media Override |
| --------- | --------------------- | -------------- |
| Ethernet5 | - | 100gbase-ar4 |

##### Phone Interfaces

| Interface | Mode | Native VLAN | Phone VLAN | Phone VLAN Mode |
| --------- | ---- | ----------- | ---------- | --------------- |
| Port-Channel12 | trunk phone | 100 | 70 | untagged |
| Port-Channel100 | dot1q-tunnel | 5 | 110 | tagged |

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet17 | LAG Member | 17 | *192.0.2.3/31 | **default | **- | **- | **- | **- |

*Inherited from Port-Channel Interface

##### ISIS

| Interface | Channel Group | ISIS Instance | ISIS BFD | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | Authentication Mode |
| --------- | ------------- | ------------- | -------- | ----------- | ---- | ----------------- | ------------- | ------------------- |
| Ethernet10/10 | 110 | *ISIS_TEST | True | *99 | *point-to-point | *level-2 | *True | *text |

*Inherited from Port-Channel Interface

##### Error Correction Encoding Interfaces

| Interface | Enabled |
| --------- | ------- |
| Ethernet11/1 | fire-code<br>reed-solomon |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet3
   description MLAG_PEER_DC1-LEAF1B_Ethernet3
   channel-group 3 mode active
!
interface Ethernet4
   description MLAG_PEER_DC1-LEAF1B_Ethernet4
   channel-group 3 mode active
!
interface Ethernet5
   description DC1-AGG01_Ethernet1
   channel-group 5 mode active
   transceiver media override 100gbase-ar4
!
interface Ethernet8
   description MLAG_PEER_DC1-LEAF1B_Ethernet8
   channel-group 8 mode active
!
interface Ethernet10/1
   description LAG Member
   channel-group 101 mode active
!
interface Ethernet10/2
   description LAG Member
   channel-group 102 mode active
!
interface Ethernet10/3
   description LAG Member
   channel-group 103 mode active
!
interface Ethernet10/4
   description LAG Member LACP fallback
   switchport trunk allowed vlan 100
   switchport mode trunk
   switchport
   channel-group 104 mode active
   spanning-tree portfast
!
interface Ethernet10/10
   description isis_port_channel_member
   channel-group 110 mode active
!
interface Ethernet11/1
   description LAG Member with error_correction
   error-correction encoding fire-code
   error-correction encoding reed-solomon
   channel-group 111 mode active
!
interface Ethernet11/2
   description LAG Member LACP fallback LLDP ZTP VLAN
   switchport trunk allowed vlan 112
   switchport mode trunk
   switchport
   channel-group 112 mode active
   lldp tlv transmit ztp vlan 112
   spanning-tree portfast
!
interface Ethernet15
   description DC1-AGG03_Ethernet1
   channel-group 15 mode active
   lacp timer fast
   lacp timer multiplier 30
!
interface Ethernet16
   description DC1-AGG04_Ethernet1
   channel-group 16 mode active
   lacp timer normal
!
interface Ethernet17
   description LAG Member
   channel-group 17 mode active
!
interface Ethernet18
   description LAG Member
   channel-group 109 mode active
!
interface Ethernet50
   description SRV-POD03_Eth1
   channel-group 5 mode active
   no lldp transmit
   no lldp receive
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
   switchport backup-link Port-Channel100 prefer vlan 20
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
   switchport tap identity 3 inner 10
   switchport tap mac-address dest 01:00:00:00:00:00
   switchport tap encapsulation vxlan strip
   switchport tool identity dot1q
   switchport tool identity dot1q source dzgre policy
   switchport tap truncation 120
   switchport tool truncation
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
!
interface Port-Channel133
   description Test_switchport_tap_tool
   switchport tap native vlan 10
   switchport tap identity 3
   switchport tap mac-address dest 01:00:00:00:00:00 src 01:23:45:67:89:ab
   switchport tap mpls pop all
   switchport tap encapsulation gre strip
   switchport tap encapsulation gre destination 1.1.1.1 source 1.1.1.2 protocol 0x0000 strip
   switchport tap encapsulation gre protocol 0x0010 strip
   switchport tap encapsulation gre destination 2.1.1.2 protocol 0x0001 strip
   switchport tap encapsulation gre destination 1.1.1.3 source 1.1.1.4 strip
   switchport tap encapsulation gre protocol 0x0002 feature header length 3 strip
   switchport tap encapsulation gre protocol 0x0003 feature header length 2 strip re-encapsulation ethernet
   switchport tool mpls pop all
   switchport tool encapsulation vn-tag strip
   switchport tool encapsulation dot1br strip
   switchport tap allowed vlan 25
   switchport tool allowed vlan 23
   switchport tool identity qinq
   switchport tool identity qinq source dzgre port inner policy
   switchport tap truncation
   switchport tool truncation 160
   switchport tap default group g1 group g2 group g3
   switchport tap default nexthop-group nexthop_g1 nexthop_g2 nexthop_g3
   switchport tap default interface ethernet4
   switchport tap default interface port-channel10
   switchport tool group set group1 group2 group3
   switchport tool dot1q remove outer 1-2
   switchport tool dzgre preserve
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
| Port-Channel9 | 500 | 500 | 5 | True |

## MPLS

### MPLS Interfaces

| Interface | MPLS IP Enabled | LDP Enabled | IGP Sync |
| --------- | --------------- | ----------- | -------- |
| Port-Channel113 | True | True | True |
| Port-Channel114 | False | False | - |

## Multicast

### PIM Sparse Mode

#### PIM Sparse Mode Enabled Interfaces

| Interface Name | VRF Name | IP Version | Border Router | DR Priority | Local Interface |
| -------------- | -------- | ---------- | ------------- | ----------- | --------------- |
| Port-Channel99 | - | IPv4 | - | 200 | - |

## Filters

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
| Port-Channel3 | - | - | - | 200000 kbps |
| Port-Channel10 | - | - | - | 50 percent |
| Port-Channel101 | disabled | - | - | - |
