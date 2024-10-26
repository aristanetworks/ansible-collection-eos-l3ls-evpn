# router-bgp-path-selection

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
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

## Routing

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65101 | 192.168.255.42 |

#### Router BGP Peer Groups

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

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 172.31.255.0 | - | default | - | - | - | - | - | - | - | - | - |
| 172.31.255.2 | - | default | - | - | - | - | - | - | - | - | - |
| 172.31.255.3 | - | default | - | - | - | - | - | - | - | - | - |
| 172.31.255.4 | - | default | - | - | - | - | - | - | - | - | - |
| 192.168.255.1 | - | default | - | - | - | - | - | - | - | - | - |

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

#### Router BGP Device Configuration

```eos
!
router bgp 65101
   router-id 192.168.255.42
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
```
