# hide-passwords

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [Enable Password](#enable-password)
  - [TACACS Servers](#tacacs-servers)
  - [RADIUS Server](#radius-server)
- [IP Security](#ip-security)
  - [IPSec profiles](#ipsec-profiles)
  - [IP Security Device Configuration](#ip-security-device-configuration)
- [Routing](#routing)
  - [Router BGP](#router-bgp)

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
| ansible | - | - | False | - |

#### Local Users Device Configuration

```eos
!
username ansible secret sha512 <removed>
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
| default | 10.10.10.157 | False | - |

#### TACACS Servers Device Configuration

```eos
!
tacacs-server host 10.10.10.157 key 7 <removed>
```

### RADIUS Server

#### RADIUS Server Hosts

| VRF | RADIUS Servers | TLS | SSL Profile | Timeout | Retransmit |
| --- | -------------- | --- | ----------- | ------- | ---------- |
| default | 10.10.10.158 | - | - | - | - |

#### RADIUS Server Device Configuration

```eos
!
radius-server host 10.10.10.158 key 7 <removed>
```

## IP Security

### IPSec profiles

| Profile name | IKE policy | SA policy | Connection | DPD Interval | DPD Time | DPD action | Mode | Flow Parallelization |
| ------------ | ---------- | ----------| ---------- | ------------ | -------- | ---------- | ---- | -------------------- |
| Profile-1 | - | - | - | - | - | - | - | - |

### IP Security Device Configuration

```eos
!
ip security
   !
   profile Profile-1
      shared-key 7 <removed>
```

## Routing

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65100 | 10.50.64.15 |

#### Router BGP Peer Groups

##### IPV4-UNDERLAY

| Settings | Value |
| -------- | ----- |
| Remote AS | 65000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 10.50.2.1 | 65000 | BLAH | - | - | - | - | - | - | - | - | - |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| BLAH | - | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65100
   router-id 10.50.64.15
   neighbor IPV4-UNDERLAY peer group
   neighbor IPV4-UNDERLAY remote-as 65000
   neighbor IPV4-UNDERLAY password 7 <removed>
   !
   vrf BLAH
      neighbor 10.50.2.1 remote-as 65000
      neighbor 10.50.2.1 password 7 <removed>
```
