# lldp

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [LLDP](#lldp-1)
  - [LLDP Summary](#lldp-summary)
  - [LLDP Device Configuration](#lldp-device-configuration)
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

## LLDP

### LLDP Summary

#### LLDP Global Settings

| Enabled | Management Address | Management VRF | Timer | Hold-Time | Re-initialization Timer | Drop Received Tagged Packets |
| ------- | ------------------ | -------------- | ----- | --------- | ----------------------- | ---------------------------- |
| False | 192.168.1.1/24 | Management | 30 | 90 | 2 | - |

#### LLDP Explicit TLV Transmit Settings

| TLV | Transmit |
| --- | -------- |
| system-capabilities | False |
| system-description | True |

#### LLDP Interface Settings

LLDP is **disabled** globally. Local interface configs will not apply.

| Interface | Transmit | Receive |
| --------- | -------- | ------- |
| Ethernet1 | False | False |
| Ethernet2 | False | True |
| Ethernet4 | True | False |

### LLDP Device Configuration

```eos
!
lldp timer 30
lldp hold-time 90
no lldp tlv transmit system-capabilities
lldp tlv transmit system-description
no lldp run
lldp management-address 192.168.1.1/24
lldp management-address vrf Management
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet2 | Switched port with no LLDP rx/tx | access | 110 | - | - | - |
| Ethernet3 | No special LLDP settings | access | 110 | - | - | - |

*Inherited from Port-Channel Interface

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description to WAN-ISP1-01 Ethernet2
   no switchport
   no lldp transmit
   no lldp receive
!
interface Ethernet2
   description Switched port with no LLDP rx/tx
   switchport access vlan 110
   switchport mode access
   switchport
   no lldp transmit
!
interface Ethernet3
   description No special LLDP settings
   switchport access vlan 110
   switchport mode access
   switchport
!
interface Ethernet4
   description test
   no switchport
   no lldp receive
```
