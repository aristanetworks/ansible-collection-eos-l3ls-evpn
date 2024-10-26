# router-bgp-v4-v6-sr-te

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
| 65103 | 192.168.255.3 |

#### Router BGP Peer Groups

##### SR-TE-PG-1

| Settings | Value |
| -------- | ----- |
| Remote AS | 65000 |

##### SR-TE-PG-2

| Settings | Value |
| -------- | ----- |
| Remote AS | 65000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 192.168.42.42 | 65004 | default | - | - | - | - | - | - | - | - | - |
| 2001:db8::dead:beef:cafe | 65004 | default | - | - | - | - | - | - | - | - | - |

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

#### Router BGP Device Configuration

```eos
!
router bgp 65103
   router-id 192.168.255.3
   neighbor SR-TE-PG-1 peer group
   neighbor SR-TE-PG-1 remote-as 65000
   neighbor SR-TE-PG-2 peer group
   neighbor SR-TE-PG-2 remote-as 65000
   neighbor 192.168.42.42 remote-as 65004
   neighbor 2001:db8::dead:beef:cafe remote-as 65004
   !
   address-family ipv4 sr-te
      neighbor SR-TE-PG-1 activate
      neighbor SR-TE-PG-1 route-map RM-SR-TE-PEER-IN4 in
      neighbor SR-TE-PG-1 route-map RM-SR-TE-PEER-OUT4 out
      neighbor 192.168.42.42 activate
      neighbor 192.168.42.42 route-map RM-SR-TE-PEER-IN4 in
      neighbor 192.168.42.42 route-map RM-SR-TE-PEER-OUT4 out
   !
   address-family ipv6 sr-te
      neighbor SR-TE-PG-2 activate
      neighbor SR-TE-PG-2 route-map RM-SR-TE-PEER-IN6 in
      neighbor SR-TE-PG-2 route-map RM-SR-TE-PEER-OUT6 out
      neighbor 2001:db8::dead:beef:cafe activate
      neighbor 2001:db8::dead:beef:cafe route-map RM-SR-TE-PEER-IN6 in
      neighbor 2001:db8::dead:beef:cafe route-map RM-SR-TE-PEER-OUT6 out
```
