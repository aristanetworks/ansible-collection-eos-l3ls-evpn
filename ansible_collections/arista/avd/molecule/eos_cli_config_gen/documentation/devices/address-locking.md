# address-locking

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Address Locking](#address-locking-1)
  - [Address Locking Summary](#address-locking-summary)
  - [DHCP Servers](#dhcp-servers)
  - [Leases](#leases)
- [Address Locking Interfaces](#address-locking-interfaces)
  - [Address Locking Device Configuration](#address-locking-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)

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

## Address Locking

### Address Locking Summary

| Setting | Value |
| -------- | ----- |
| Disable IP locking on configured ports | True |
| Local Interface | Loopback0 |
| Disable deauthorizing locked addresses upon MAC aging out | True |
| Disable enforcement for locked ipv4 addresses | True |
| Disable enforcement for locked ipv6 addresses | True |

### DHCP Servers

| Server IP |
| --------- |
| 1.1.1.1 |
| 4.4.4.4 |

### Leases

| Lease IP Address | Lease MAC Address |
| ---------------- | ----------------- |
| 2.2.2.2 | dead.beef.cafe |
| 3.3.3.3 | de:af:be:ef:ca:fe |

## Address Locking Interfaces

| Interface | IPv4 Address Locking | IPv6 Address Locking |
| --------- | -------------------- | -------------------- |
| Ethernet1 | True | False |
| Ethernet2 | True | True |
| Ethernet3 | False | True |

### Address Locking Device Configuration

```eos
!
address locking
   disabled
   local-interface Loopback0
   dhcp server ipv4 1.1.1.1
   dhcp server ipv4 4.4.4.4
   lease 2.2.2.2 mac dead.beef.cafe
   lease 3.3.3.3 mac de:af:be:ef:ca:fe
   locked-address expiration mac disabled
   locked-address ipv4 enforcement disabled
   locked-address ipv6 enforcement disabled
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet1 | Address Locking Interface Testing 1 | - | - | - | - | - |
| Ethernet2 | Address Locking Interface Testing 2 | - | - | - | - | - |
| Ethernet3 | Address Locking Interface Testing 3 | - | - | - | - | - |

*Inherited from Port-Channel Interface

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description Address Locking Interface Testing 1
   switchport
   address locking ipv4
!
interface Ethernet2
   description Address Locking Interface Testing 2
   switchport
   address locking ipv4 ipv6
!
interface Ethernet3
   description Address Locking Interface Testing 3
   switchport
   address locking ipv6
```
