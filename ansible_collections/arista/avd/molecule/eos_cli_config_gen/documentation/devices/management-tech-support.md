# management-tech-support

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Management Tech-Support](#management-tech-support-1)

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

### Management Tech-Support

#### Policy

##### Exclude Commands

| Command | Type |
| ------- | ---- |
| show platform fap ip route | text |
| show platform fap ipv6 route | text |
| show ip bgp vrf all | text |
| show ipv6 bgp vrf all | text |
| show kernel ip route vrf all | text |
| show kernel ipv6 route vrf all | text |
| show ip route vrf all detail | text |
| show ipv6 route vrf all detail | text |
| show version detail | json |

##### Include Commands

| Command |
| ------- |
| show version detail \| grep TerminAttr |

#### Policy Device Configuration

```eos
!
management tech-support
   policy show tech-support
      exclude command show ip bgp vrf all
      exclude command show ip route vrf all detail
      exclude command show ipv6 bgp vrf all
      exclude command show ipv6 route vrf all detail
      exclude command show kernel ip route vrf all
      exclude command show kernel ipv6 route vrf all
      exclude command show platform fap ip route
      exclude command show platform fap ipv6 route
      exclude command json show version detail
      include command show version detail | grep TerminAttr
   exit
```
