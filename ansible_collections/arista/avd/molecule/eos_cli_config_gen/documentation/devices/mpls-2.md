# mpls-2

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [MPLS](#mpls)
  - [MPLS and LDP](#mpls-and-ldp)
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

## MPLS

### MPLS and LDP

#### MPLS and LDP Summary

| Setting | Value |
| -------- | ---- |
| MPLS IP Enabled | True |
| LDP Enabled | False |
| LDP Router ID | - |
| LDP Interface Disabled Default | False |
| LDP Transport-Address Interface | - |
| ICMP TTL-Exceeded Tunneling Enabled | True |

### MPLS RSVP

#### MPLS RSVP Summary

| Setting | Value |
| ------- | ----- |
| Refresh method  | explicit |
| Authentication type | md5 |
| Authentication sequence-number window | 234 |
| Authentication active index | 766 |
| SRLG | enabled |
| Preemption method | hard |
| Fast reroute mode | link-protection |
| Fast reroute reversion | - |
| Fast reroute  bypass tunnel optimization interval | - |
| Hitless restart | Active |
| Hitless restart recovery timer | - |

##### RSVP Graceful Restart

| Role | Recovery timer | Restart timer |
| ---- | -------------- | ------------- |
| Helper | 32 | 33 |

#### MPLS Device Configuration

```eos
!
mpls ip
!
mpls ldp
   shutdown
!
mpls icmp ttl-exceeded tunneling
!
mpls rsvp
   refresh method explicit
   authentication type md5
   authentication sequence-number window 234
   authentication index 766 active
   fast-reroute mode link-protection
   srlg
   preemption method hard
   !
   hitless-restart
   !
   graceful-restart role helper
      timer restart maximum 32 seconds
      timer recovery maximum 33 seconds
   !
   p2mp
```
