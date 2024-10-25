# management-interfaces

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces-1)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management0 | - | oob | default | 10.0.0.0 | - |
| Management1 | OOB_MANAGEMENT | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |
| Management42 | - | oob | default | - | - |
| Vlan123 | inband_management | inband | default | 10.73.0.123/24 | 10.73.0.1 |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management0 | - | oob | default | - | - |
| Management1 | OOB_MANAGEMENT | oob | MGMT | - | - |
| Management42 | - | oob | default | - | - |
| Vlan123 | inband_management | inband | default | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management0
   mac-address 00:1c:73:00:00:aa
   ip address 10.0.0.0
!
interface Management1
   description OOB_MANAGEMENT
   vrf MGMT
   ip address 10.73.255.122/24
!
interface Management42
   shutdown
   speed forced 1000full
   no lldp transmit
   no lldp receive
   lldp tlv transmit ztp vlan 666
!
interface Vlan123
   description inband_management
   mtu 1500
   ip address 10.73.0.123/24
   ip virtual-router address 10.73.0.1
```
