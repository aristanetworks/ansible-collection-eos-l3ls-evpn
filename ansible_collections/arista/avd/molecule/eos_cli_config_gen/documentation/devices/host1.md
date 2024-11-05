# hostname-set-via-hostname-var

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
- [Monitoring](#monitoring)
  - [Event Handler](#event-handler)
  - [Flow Tracking](#flow-tracking)
- [Interfaces](#interfaces)
  - [Interface Profiles](#interface-profiles)
  - [DPS Interfaces](#dps-interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
- [Filters](#filters)
  - [IP Community-lists](#ip-community-lists)
  - [IP Extended Community Lists](#ip-extended-community-lists)
  - [IP Extended Community RegExp Lists](#ip-extended-community-regexp-lists)
- [IP DHCP Relay](#ip-dhcp-relay)
  - [IP DHCP Relay Summary](#ip-dhcp-relay-summary)
  - [IP DHCP Relay Device Configuration](#ip-dhcp-relay-device-configuration)
- [IP DHCP Snooping](#ip-dhcp-snooping)
  - [IP DHCP Snooping Device Configuration](#ip-dhcp-snooping-device-configuration)
- [Errdisable](#errdisable)
  - [Errdisable Summary](#errdisable-summary)
- [Maintenance Mode](#maintenance-mode)
  - [BGP Groups](#bgp-groups)
  - [Interface Groups](#interface-groups)

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

## Monitoring

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

### Flow Tracking

#### Flow Tracking Sampled

| Sample Size | Minimum Sample Size | Hardware Offload for IPv4 | Hardware Offload for IPv6 | Encapsulations |
| ----------- | ------------------- | ------------------------- | ------------------------- | -------------- |
| 666 | 2 | enabled | disabled | ipv4, ipv6, mpls |

##### Trackers Summary

| Tracker Name | Record Export On Inactive Timeout | Record Export On Interval | MPLS | Number of Exporters | Applied On | Table Size |
| ------------ | --------------------------------- | ------------------------- | ---- | ------------------- | ---------- | ---------- |
| T1 | 3666 | 5666 | True | 0 |  | - |
| T2 | - | - | False | 1 | Ethernet40 | 614400 |
| T3 | - | - | - | 4 | Ethernet41<br>Ethernet42<br>Port-Channel42 | 100000 |

##### Exporters Summary

| Tracker Name | Exporter Name | Collector IP/Host | Collector Port | Local Interface |
| ------------ | ------------- | ----------------- | -------------- | --------------- |
| T2 | T2-E1 | - | - | No local interface |
| T3 | T3-E1 | - | - | No local interface |
| T3 | T3-E2 | - | - | No local interface |
| T3 | T3-E3 | - | - | Management1 |
| T3 | T3-E4 | - | - | No local interface |

#### Flow Tracking Hardware

Software export of IPFIX data records enabled.

##### Trackers Summary

| Tracker Name | Record Export On Inactive Timeout | Record Export On Interval | Number of Exporters | Applied On |
| ------------ | --------------------------------- | ------------------------- | ------------------- | ---------- |
| T1 | 3666 | 5666 | 0 |  |
| T2 | - | - | 1 | Ethernet40 |
| T3 | - | - | 4 | Dps1<br>Ethernet41<br>Port-Channel42 |
| T4 | 3666 | 5666 | 0 |  |

##### Exporters Summary

| Tracker Name | Exporter Name | Collector IP/Host | Collector Port | Local Interface |
| ------------ | ------------- | ----------------- | -------------- | --------------- |
| T2 | T2-E1 | - | - | No local interface |
| T3 | T3-E1 | - | - | No local interface |
| T3 | T3-E2 | - | - | No local interface |
| T3 | T3-E3 | - | - | Management1 |
| T3 | T3-E4 | - | - | No local interface |

#### Flow Tracking Device Configuration

```eos
!
flow tracking hardware
   tracker T1
      record export on inactive timeout 3666
      record export on interval 5666
   !
   tracker T2
      exporter T2-E1
         collector 42.42.42.42
   !
   tracker T3
      exporter T3-E1
      !
      exporter T3-E2
         collector 10.10.10.10 port 777
      !
      exporter T3-E3
         collector this.is.my.awesome.collector.dns.name port 888
         format ipfix version 10
         local interface Management1
         template interval 424242
      !
      exporter T3-E4
         collector dead:beef::cafe
   !
   tracker T4
      record export on inactive timeout 3666
      record export on interval 5666
   record format ipfix standard timestamps counters
   no shutdown
!
flow tracking sampled
   encapsulation ipv4 ipv6 mpls
   sample 666
   hardware offload ipv4
   hardware offload threshold minimum 2 samples
   tracker T1
      record export on inactive timeout 3666
      record export on interval 5666
      record export mpls
   !
   tracker T2
      flow table size 614400 entries
      exporter T2-E1
         collector 42.42.42.42
   !
   tracker T3
      flow table size 100000 entries
      exporter T3-E1
      !
      exporter T3-E2
         collector 10.10.10.10 port 777
      !
      exporter T3-E3
         collector this.is.my.awesome.collector.dns.name port 888
         format ipfix version 10
         local interface Management1
         template interval 424242
      !
      exporter T3-E4
         collector dead:beef::cafe
   no shutdown
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
| Dps1 | - | - | - | Hardware: T3 |  |

#### DPS Interfaces Device Configuration

```eos
!
interface Dps1
   flow tracker hardware T3
```

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet40 | - | - | - | - | - | - |
| Ethernet41 | - | - | - | - | - | - |
| Ethernet42 | - | - | - | - | - | - |

*Inherited from Port-Channel Interface

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet40
   switchport
   flow tracker hardware T2
   flow tracker sampled T2
!
interface Ethernet41
   switchport
   flow tracker hardware T3
   flow tracker sampled T3
!
interface Ethernet42
   switchport
   flow tracker sampled T3
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel42 | - | - | - | - | - | - | - | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel42
   switchport
   flow tracker hardware T3
   flow tracker sampled T3
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
| TEST1 | permit | 65[0-9]{3}:[0-9]+ |
| TEST1 | deny | .* |
| TEST2 | deny | 6500[0-1]:650[0-9][0-9] |

#### IP Extended Community RegExp Lists Device Configuration

```eos
!
ip extcommunity-list regexp TEST1 permit 65[0-9]{3}:[0-9]+
ip extcommunity-list regexp TEST1 deny .*
!
ip extcommunity-list regexp TEST2 deny 6500[0-1]:650[0-9][0-9]
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
