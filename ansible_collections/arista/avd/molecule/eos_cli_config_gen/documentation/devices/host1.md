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
- [System Boot Settings](#system-boot-settings)
  - [Boot Secret Summary](#boot-secret-summary)
  - [System Boot Device Configuration](#system-boot-device-configuration)
- [Monitoring](#monitoring)
  - [Custom daemons](#custom-daemons)
  - [Event Handler](#event-handler)
- [Interfaces](#interfaces)
  - [Interface Profiles](#interface-profiles)
  - [DPS Interfaces](#dps-interfaces)
- [Routing](#routing)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [ARP](#arp)
  - [Router BGP](#router-bgp)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
- [Filters](#filters)
  - [IP Community-lists](#ip-community-lists)
  - [IP Extended Community Lists](#ip-extended-community-lists)
  - [IP Extended Community RegExp Lists](#ip-extended-community-regexp-lists)
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
- [IP DHCP Relay](#ip-dhcp-relay)
  - [IP DHCP Relay Summary](#ip-dhcp-relay-summary)
  - [IP DHCP Relay Device Configuration](#ip-dhcp-relay-device-configuration)
- [IP DHCP Snooping](#ip-dhcp-snooping)
  - [IP DHCP Snooping Device Configuration](#ip-dhcp-snooping-device-configuration)
- [Errdisable](#errdisable)
  - [Errdisable Summary](#errdisable-summary)
- [Quality Of Service](#quality-of-service)
  - [QOS Class Maps](#qos-class-maps)
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

### Router BGP

ASN Notation: asdot

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65101 | 192.168.255.3 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| update wait-install |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| maximum-paths 2 ecmp 2 |
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
| 172.31.255.4 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | Allowed, allowed 5 times | Inherited from peer group EVPN-OVERLAY-PEERS(interval: 2000, min_rx: 2000, multiplier: 3) | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
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
| 192.168.255.21 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS(interval: 2000, min_rx: 2000, multiplier: 3) | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - |
| 192.168.255.101 | Inherited from peer group MPLS-IBGP-PEERS | default | - | Inherited from peer group MPLS-IBGP-PEERS | Inherited from peer group MPLS-IBGP-PEERS | - | - | - | - | - | - |
| 192.168.255.201 | Inherited from peer group MPLS-IBGP-PEERS | default | - | Inherited from peer group MPLS-IBGP-PEERS | Inherited from peer group MPLS-IBGP-PEERS | - | - | - | - | - | - |
| 2001:cafe:192:168::4 | 65004 | default | - | all | - | - | - | - | - | - | - |
| 2001:db8::dead:beef:cafe | 65004 | default | - | - | - | - | - | - | - | - | - |
| fe80::b%Vl4094 | Inherited from peer group IPV6-UNDERLAY-MLAG | default | - | Inherited from peer group IPV6-UNDERLAY-MLAG | Inherited from peer group IPV6-UNDERLAY-MLAG | - | - | - | - | - | - |
| 10.1.1.0 | Inherited from peer group OBS_WAN | BLUE-C1 | - | - | - | - | Inherited from peer group OBS_WAN(interval: 2000, min_rx: 2000, multiplier: 3) | - | - | - | - |
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
| 10.2.3.4 | 1234 | TENANT_A_PROJECT01 | - | all | 0 (no limit) | - | - | - | - | - | - |
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
| Label local-termination | implicit-null |

##### IPv4 BGP-LU Peer-groups

| Peer-group | Activate | Route-map In | Route-map Out | RCF In | RCF Out |
| ---------- | -------- | ------------ | ------------- | ------ | ------- |
| PG-BGP-LU | True | - | - | - | - |

##### IPv4 BGP-LU Neighbors

| Neighbor | Activate | Route-map In | Route-map Out | RCF In | RCF Out |
| -------- | -------- | ------------ | ------------- | ------ | ------- |
| 198.51.100.1 | True | - | - | RCF_TEST(ARGS) | - |
| 198.51.100.2 | False | - | RM_OUT_TEST | - | - |

#### Router BGP IPv4 SR-TE Address Family

##### IPv4 SR-TE Neighbors

| Neighbor | Activate | Route-map In | Route-map Out |
| -------- | -------- | ------------ | ------------- |
| 192.168.42.42 | True | RM-SR-TE-PEER-IN4 | RM-SR-TE-PEER-OUT4 |

##### IPv4 SR-TE Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out |
| ---------- | -------- | ------------ | ------------- |
| SR-TE-PG-1 | True | RM-SR-TE-PEER-IN4 | RM-SR-TE-PEER-OUT4 |

#### Router BGP IPv6 SR-TE Address Family

##### IPv6 SR-TE Neighbors

| Neighbor | Activate | Route-map In | Route-map Out |
| -------- | -------- | ------------ | ------------- |
| 2001:db8::dead:beef:cafe | True | RM-SR-TE-PEER-IN6 | RM-SR-TE-PEER-OUT6 |

##### IPv6 SR-TE Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out |
| ---------- | -------- | ------------ | ------------- |
| SR-TE-PG-2 | True | RM-SR-TE-PEER-IN6 | RM-SR-TE-PEER-OUT6 |

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
| 172.31.255.4 | True |

##### Path-Selection Peer Groups

| Peer Group | Activate |
| ---------- | -------- |
| PATH-SELECTION-PG-1 | True |
| PATH-SELECTION-PG-2 | True |
| PATH-SELECTION-PG-3 | True |
| PATH-SELECTION-PG-4 | True |
| PATH-SELECTION-PG-5 | True |

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
   no bgp default ipv4-unicast
   update wait-install
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 2 ecmp 2
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
      neighbor ADDITIONAL-PATH-PG-2 default-route rcf DEFAULT_ROUTE_RM
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
      neighbor 10.2.3.9 rcf out Address_Family_IPV4_Out()
      neighbor 192.0.2.1 additional-paths receive
      neighbor 192.0.2.1 route-map Address_Family_IPV4_In in
      neighbor 192.0.2.1 route-map Address_Family_IPV4_Out out
      neighbor 192.0.2.1 prefix-list PL-FOO-v4-IN in
      neighbor 192.0.2.1 prefix-list PL-FOO-v4-OUT out
      neighbor 192.0.2.1 additional-paths send limit 20 prefix-list PL1
      no neighbor 192.168.66.21 activate
      network 10.0.0.0/8
      network 172.16.0.0/12
      network 192.168.0.0/16 route-map RM-FOO-MATCH
      no bgp redistribute-internal
      redistribute attached-host route-map RM_BGP_EVPN_IPV4
      redistribute bgp leaked
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
      bgp missing-policy include community-list direction in action deny
      bgp additional-paths receive
      bgp additional-paths send ecmp limit 20
      bgp next-hop-unchanged
      next-hop resolution ribs tunnel-rib colored system-colored-tunnel-rib tunnel-rib test-rib system-connected
      neighbor PG-BGP-LU activate
      neighbor 198.51.100.1 activate
      neighbor 198.51.100.1 additional-paths receive
      neighbor 198.51.100.1 graceful-restart
      neighbor 198.51.100.1 rcf in RCF_TEST(ARGS)
      neighbor 198.51.100.1 additional-paths send ecmp
      neighbor 198.51.100.1 maximum-advertised-routes 0
      no neighbor 198.51.100.2 activate
      neighbor 198.51.100.2 graceful-restart-helper stale-route route-map RM_STALE
      neighbor 198.51.100.2 route-map RM_OUT_TEST out
      neighbor 198.51.100.2 next-hop-unchanged
      neighbor 198.51.100.2 aigp-session
      neighbor 198.51.100.2 multi-path
      network 203.0.113.0/25 route-map RM-TEST
      network 203.0.113.128/25
      label local-termination implicit-null
      tunnel source-protocol isis segment-routing
      tunnel source-protocol ldp rcf TEST(ARGS)
      aigp-session confederation
      aigp-session ebgp
   !
   address-family ipv4 multicast
      bgp additional-paths receive
      neighbor FOOBAR activate
      neighbor FOOBAR additional-paths receive
      neighbor IPV4-UNDERLAY activate
      neighbor IPV4-UNDERLAY-MLAG activate
      neighbor 10.1.1.1 activate
      neighbor 10.1.1.1 additional-paths receive
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
      neighbor 192.168.42.42 activate
      neighbor 192.168.42.42 route-map RM-SR-TE-PEER-IN4 in
      neighbor 192.168.42.42 route-map RM-SR-TE-PEER-OUT4 out
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
      neighbor IPV6-UNDERLAY-MLAG activate
      neighbor TEST_RCF rcf in Address_Family_IPV6_In()
      neighbor TEST_RCF rcf out Address_Family_IPV6_Out()
      neighbor 2001:db8::1 additional-paths receive
      neighbor 2001:db8::1 prefix-list PL-FOO-v6-IN in
      neighbor 2001:db8::1 prefix-list PL-FOO-v6-OUT out
      neighbor 2001:db8::1 additional-paths send ecmp limit 20
      neighbor 2001:db8::2 rcf in Address_Family_IPV6_In()
      neighbor 2001:db8::2 rcf out Address_Family_IPV6_Out()
      network 2001:db8:100::/40
      network 2001:db8:200::/40 route-map RM-BAR-MATCH
      bgp redistribute-internal
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
      bgp additional-paths receive
      no neighbor FOOBAR activate
      neighbor FOOBAR additional-paths receive
      neighbor aa::1 additional-paths receive
      redistribute connected route-map RM-address_family_ipv6_multicast-Connected
      redistribute isis include leaked route-map RM-address_family_ipv6_multicast-ISIS
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
      neighbor 2001:db8::dead:beef:cafe activate
      neighbor 2001:db8::dead:beef:cafe route-map RM-SR-TE-PEER-IN6 in
      neighbor 2001:db8::dead:beef:cafe route-map RM-SR-TE-PEER-OUT6 out
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
      neighbor PATH-SELECTION-PG-1 additional-paths send any
      neighbor PATH-SELECTION-PG-2 activate
      neighbor PATH-SELECTION-PG-2 additional-paths send backup
      neighbor PATH-SELECTION-PG-3 activate
      neighbor PATH-SELECTION-PG-3 additional-paths send ecmp
      neighbor PATH-SELECTION-PG-4 activate
      neighbor PATH-SELECTION-PG-4 additional-paths send ecmp limit 42
      neighbor PATH-SELECTION-PG-5 activate
      neighbor PATH-SELECTION-PG-5 additional-paths send limit 42
      neighbor 172.31.255.0 activate
      neighbor 172.31.255.0 additional-paths receive
      neighbor 172.31.255.0 additional-paths send any
      neighbor 172.31.255.1 activate
      neighbor 172.31.255.1 additional-paths send backup
      neighbor 172.31.255.2 activate
      neighbor 172.31.255.2 additional-paths send ecmp
      neighbor 172.31.255.3 activate
      neighbor 172.31.255.3 additional-paths send ecmp limit 42
      neighbor 172.31.255.4 activate
      neighbor 172.31.255.4 additional-paths send limit 42
   !
   address-family rt-membership
      neighbor EVPN-OVERLAY-PEERS activate
      neighbor EVPN-OVERLAY-PEERS default-route-target
      neighbor EVPN-OVERLAY-RS-PEERS activate
      neighbor EVPN-OVERLAY-RS-PEERS default-route-target only
      neighbor EVPN-OVERLAY-RS-PEERS default-route-target encoding origin-as omit
   !
   address-family vpn-ipv4
      neighbor MPLS-IBGP-PEERS activate
      neighbor MPLS-IBGP-PEERS route-map RM-IBGP-PEER-IN4 in
      neighbor MPLS-IBGP-PEERS route-map RM-IBGP-PEER-OUT4 out
      neighbor Test_RCF rcf in Address_Family_VPN_IPV4_In()
      neighbor Test_RCF rcf out Address_Family_VPN_IPV4_Out()
      neighbor 192.168.255.4 activate
      neighbor 192.168.255.4 route-map RM-NEIGHBOR-PEER-IN4 in
      neighbor 192.168.255.4 route-map RM-NEIGHBOR-PEER-OUT4 out
      neighbor 192.168.255.5 rcf in Address_Family_VPN_IPV4_In()
      neighbor 192.168.255.5 rcf out Address_Family_VPN_IPV4_Out()
      neighbor default encapsulation mpls next-hop-self source-interface Loopback0
      domain identifier 65000:0
      route import match-failure action discard
   !
   address-family vpn-ipv6
      neighbor MPLS-IBGP-PEERS activate
      neighbor MPLS-IBGP-PEERS route-map RM-IBGP-PEER-IN6 in
      neighbor MPLS-IBGP-PEERS route-map RM-IBGP-PEER-OUT6 out
      neighbor Test_RCF rcf in Address_Family_VPN_IPV6_In()
      neighbor Test_RCF rcf out Address_Family_VPN_IPV6_Out()
      neighbor 2001:cafe:192:168::4 activate
      neighbor 2001:cafe:192:168::4 route-map RM-NEIGHBOR-PEER-IN6 in
      neighbor 2001:cafe:192:168::4 route-map RM-NEIGHBOR-PEER-OUT6 out
      neighbor 2001:cafe:192:168::5 rcf in Address_Family_VPN_IPV6_In()
      neighbor 2001:cafe:192:168::5 rcf out Address_Family_VPN_IPV6_Out()
      neighbor default encapsulation mpls next-hop-self source-interface Loopback0
      domain identifier 65000:0
      route import match-failure action discard
   !
   vrf BLUE-C1
      rd 1.0.1.1:101
      neighbor 10.1.1.0 peer group OBS_WAN
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
      aggregate-address 0.0.0.0/0 as-set summary-only attribute-map RM-BGP-AGG-APPLY-SET
      aggregate-address 193.1.0.0/16 as-set summary-only attribute-map RM-BGP-AGG-APPLY-SET
      redistribute ospf include leaked
      redistribute static
      !
      comment
      Comment created from eos_cli under router_bgp.vrfs.BLUE-C1
      EOF

   !
   vrf RED-C1
      rd 1.0.1.1:102
      neighbor 10.1.1.0 peer group OBS_WAN
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
      route-target export evpn 1:30001
      route-target export evpn rcf RT_EXPORT_AF_RCF()
      redistribute connected
      redistribute ospf match external include leaked
      redistribute ospfv3
      redistribute ospfv3 match nssa-external
   !
   vrf TENANT_A_PROJECT01
      rd 192.168.255.3:11
      route-target import evpn 11:11
      route-target export evpn 11:11
      router-id 192.168.255.3
      update wait-for-convergence
      update wait-install
      neighbor 10.2.3.4 remote-as 1234
      neighbor 10.2.3.4 remove-private-as all
      neighbor 10.2.3.4 local-as 123 no-prepend replace-as
      neighbor 10.2.3.4 description Tenant A BGP Peer
      neighbor 10.2.3.4 ebgp-multihop 3
      neighbor 10.2.3.4 route-map RM-10.2.3.4-SET-NEXT-HOP-OUT out
      neighbor 10.2.3.4 default-originate route-map RM-10.2.3.4-SET-NEXT-HOP-OUT always
      neighbor 10.2.3.4 send-community
      neighbor 10.2.3.4 maximum-routes 0
      neighbor 10.255.251.1 peer group MLAG-IPv4-UNDERLAY-PEER
      network 10.0.0.0/8
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
         neighbor 10.2.3.4 route-map RM-10.2.3.4-SET-NEXT-HOP-OUT out
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
      no bgp redistribute-internal
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
         no bgp redistribute-internal
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
         no bgp redistribute-internal
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
      redistribute dynamic rcf VRF_RCF_DYNAMIC()
      !
      address-family ipv4
         bgp additional-paths send ecmp
   !
   vrf YELLOW-C1
      rd 1.0.1.1:103
      bgp listen range 10.10.10.0/24 peer-group my-peer-group1 peer-filter my-peer-filter
      bgp listen range 12.10.10.0/24 peer-id include router-id peer-group my-peer-group3 remote-as 65444
      bgp listen range 13.10.10.0/24 peer-group my-peer-group4 peer-filter my-peer-filter
      neighbor 10.1.1.0 peer group OBS_WAN
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
