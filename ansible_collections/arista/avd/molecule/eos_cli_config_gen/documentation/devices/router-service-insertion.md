# router-service-insertion

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Routing](#routing)
- [Router Service Insertion](#router-service-insertion-1)
  - [Connections](#connections)
  - [Router Service Insertion Configuration](#router-service-insertion-configuration)

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

## Router Service Insertion

Router service-insertion is enabled.

### Connections

#### Connections Through Ethernet Interface

| Name | Interface | Next Hop | Monitor Connectivity Host |
| ---- | --------- | -------- | ------------------------- |
| aconnection | Ethernet4/1 | 10.10.10.10 | host4 |
| connection1 | Ethernet2/2.2 | 10.10.10.10 | host1 |
| connection6 | Ethernet2 | 10.10.10.10 | - |
| connection7 | Ethernet3/1 | 10.10.10.10 | host4 |

#### Connections Through Tunnel Interface

| Name | Primary Interface | Secondary Interface | Monitor Connectivity Host |
| ---- | ----------------- | ------------------- | ------------------------- |
| connection2 | Tunnel1 | Tunnel2 | host2 |
| connection3 | - | Tunnel3 | host3 |
| connection4 | Tunnel4 | - | - |
| connection5 | Tunnel5 | Tunnel6 | - |

### Router Service Insertion Configuration

```eos
!
router service-insertion
   connection aconnection
      interface Ethernet4/1 next-hop 10.10.10.10
      monitor connectivity host host4
   connection connection1
      interface Ethernet2/2.2 next-hop 10.10.10.10
      monitor connectivity host host1
   connection connection2
      interface Tunnel1 primary
      interface Tunnel2 secondary
      monitor connectivity host host2
   connection connection3
      interface Tunnel3 secondary
      monitor connectivity host host3
   connection connection4
      interface Tunnel4 primary
   connection connection5
      interface Tunnel5 primary
      interface Tunnel6 secondary
   connection connection6
      interface Ethernet2 next-hop 10.10.10.10
   connection connection7
      interface Ethernet3/1 next-hop 10.10.10.10
      monitor connectivity host host4
```
