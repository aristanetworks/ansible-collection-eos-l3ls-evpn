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
- [Interfaces](#interfaces)
  - [DPS Interfaces](#dps-interfaces)
- [Routing](#routing)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [ARP](#arp)
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
