# vlans

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [VLANs](#vlans-1)
  - [VLANs Summary](#vlans-summary)
  - [VLANs Device Configuration](#vlans-device-configuration)

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

## VLANs

### VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 110 | PR01-DMZ | - |
| 111 | PRIVATE_VLAN_COMMUNITY | - |
| 112 | PRIVATE_VLAN_ISOLATED | - |
| 3010 | MLAG_iBGP_TENANT_A_PROJECT01 | LEAF_PEER_L3 |
| 3011 | MLAG_iBGP_TENANT_A_PROJECT02 | MY_TRUNK_GROUP |
| 3012 | MLAG_iBGP_TENANT_A_PROJECT03 | MY_TRUNK_GROUP |

#### Private VLANs

| Primary Vlan ID | Secondary VLAN ID | Private Vlan Type |
| --------------- | ----------------- | ----------------- |
| community | 111 | 110 |
| isolated | 112 | 110 |

### VLANs Device Configuration

```eos
!
vlan 110
   name PR01-DMZ
!
vlan 111
   name PRIVATE_VLAN_COMMUNITY
   private-vlan community primary vlan 110
!
vlan 112
   name PRIVATE_VLAN_ISOLATED
   private-vlan isolated primary vlan 110
!
vlan 3010
   name MLAG_iBGP_TENANT_A_PROJECT01
   trunk group LEAF_PEER_L3
!
vlan 3011
   name MLAG_iBGP_TENANT_A_PROJECT02
   state active
   trunk group MY_TRUNK_GROUP
!
vlan 3012
   name MLAG_iBGP_TENANT_A_PROJECT03
   state suspend
   trunk group MY_TRUNK_GROUP
```
