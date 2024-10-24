# mpls

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
- [MPLS](#mpls-1)
  - [MPLS and LDP](#mpls-and-ldp)
  - [MPLS Interfaces](#mpls-interfaces)
  - [MPLS RSVP](#mpls-rsvp)

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
| Ethernet1 | - | - | 192.168.100.1/31 | default | - | - | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   no switchport
   ip address 192.168.100.1/31
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | - | default | 192.168.1.1/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | - | default | - |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   ip address 192.168.1.1/32
   mpls ldp interface
```

## MPLS

### MPLS and LDP

#### MPLS and LDP Summary

| Setting | Value |
| -------- | ---- |
| MPLS IP Enabled | True |
| LDP Enabled | True |
| LDP Router ID | 192.168.1.1 |
| LDP Interface Disabled Default | True |
| LDP Transport-Address Interface | Loopback0 |
| ICMP Fragmentation-Needed Tunneling Enabled | True |

#### MPLS and LDP Device Configuration

```eos
!
mpls ip
!
mpls ldp
   router-id 192.168.1.1
   transport-address interface Loopback0
   interface disabled default
   no shutdown
!
mpls icmp fragmentation-needed tunneling
!
mpls rsvp
   refresh interval 3
   refresh method explicit
   hello interval 30 multiplier 254
   authentication type md5
   authentication sequence-number window 234
   authentication index 55 password 7 <removed>
   authentication index 766 password 7 <removed>
   authentication index 766 active
   neighbor 1.1.1.1 authentication type md5
   neighbor 1.1.1.1 authentication index 3 active
   neighbor 1.1.12.2 authentication type none
   neighbor 1.1.12.2 authentication index 30 active
   neighbor 1.10.1.2 authentication type none
   neighbor 1.21.1.20 authentication type md5
   neighbor 10.1.1.2 authentication index 303 active
   ip access-group RSVP_access_group_ipv4
   ipv6 access-group RSVP_access_group_ipv6
   fast-reroute mode link-protection
   fast-reroute reversion local
   fast-reroute bypass tunnel optimization interval 65535 seconds
   srlg strict
   label local-termination explicit-null
   preemption method soft timer 444
   mtu signaling
   !
   hitless-restart
      timer recovery 222 seconds
   !
   graceful-restart role helper
      timer restart maximum 32 seconds
      timer recovery maximum 33 seconds
   !
   graceful-restart role speaker
      timer restart 35 seconds
      timer recovery 36 seconds
   !
   p2mp
      disabled
   shutdown
```

### MPLS Interfaces

| Interface | MPLS IP Enabled | LDP Enabled | IGP Sync |
| --------- | --------------- | ----------- | -------- |
| Ethernet1 | True | True | True |
| Loopback0 | - | True | - |

### MPLS RSVP

#### MPLS RSVP Summary

| Setting | Value |
| ------- | ----- |
| Refresh interval | 3 |
| Refresh method  | explicit |
| Hello interval | 30 |
| Timeout multiplier | 254 |
| Authentication type | md5 |
| Authentication sequence-number window | 234 |
| Authentication active index | 766 |
| IPv4 access-group | RSVP_access_group_ipv4 |
| IPv6 access-group | RSVP_access_group_ipv6 |
| SRLG strict | enabled |
| Label local-termination | explicit-null |
| Preemption method | soft |
| Preemption timer | 444 |
| MTU signaling | True |
| Fast reroute mode | link-protection |
| Fast reroute reversion | local |
| Fast reroute  bypass tunnel optimization interval | 65535 |
| Hitless restart | Active |
| Hitless restart recovery timer | 222 |
| Shutdown | Active |

##### Neighbor

| Neighbor IP | Index | Type |
| ----------- | ----- | ---- |
| 1.1.1.1 | 3 | md5 |
| 1.1.12.2 | 30 | none |
| 1.10.1.2 | - | none |
| 1.21.1.20 | - | md5 |
| 10.1.1.2 | 303 | - |

##### Graceful restart

| Role | Recovery timer | Restart timer |
| ---- | -------------- | ------------- |
| Helper | 32 | 33 |
| Speaker | 35 | 36 |
