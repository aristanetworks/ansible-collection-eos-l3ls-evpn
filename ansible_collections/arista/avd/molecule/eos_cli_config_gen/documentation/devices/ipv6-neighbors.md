# ipv6-neighbors

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Routing](#routing)
  - [IPv6 Neighbors](#ipv6-neighbors-1)

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

### IPv6 Neighbors

IPv6 neighbor cache persistency is enabled. The refresh-delay is 1000 seconds after reboot.

#### IPv6 Static Neighbors

| VRF | IPv6 Address | Exit Interface | MAC Address |
| --- | ------------ | -------------- | ----------- |
| MGMT | 11:22:33:44:55:66:77:88 | Ethernet1 | 11:22:33:44:55:66 |
| - | ::ffff:192.1.56.10 | Loopback99 | aa:af:12:34:bc:bf |

#### IPv6 Neighbor Configuration

```eos
!
ipv6 neighbor persistent refresh-delay 1000
ipv6 neighbor vrf MGMT 11:22:33:44:55:66:77:88 Ethernet1 11:22:33:44:55:66
ipv6 neighbor ::ffff:192.1.56.10 Loopback99 aa:af:12:34:bc:bf
```
