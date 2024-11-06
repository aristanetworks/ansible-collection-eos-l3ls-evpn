# host1

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [TACACS Servers](#tacacs-servers)
  - [RADIUS Server](#radius-server)
  - [AAA Server Groups](#aaa-server-groups)
  - [AAA Authentication](#aaa-authentication)
  - [AAA Authorization](#aaa-authorization)
  - [AAA Accounting](#aaa-accounting)

## Management

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
