# ip-dhcp-snooping

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [IP DHCP Snooping](#ip-dhcp-snooping-1)
  - [IP DHCP Snooping Device Configuration](#ip-dhcp-snooping-device-configuration)

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
