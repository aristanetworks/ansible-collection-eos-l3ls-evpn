# vxlan-interface

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Interfaces](#interfaces)
  - [VXLAN Interface](#vxlan-interface-1)

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

## Interfaces

### VXLAN Interface

#### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| Source Interface | Loopback0 |
| Controller Client | True |
| MLAG Source Interface | Loopback1 |
| UDP port | 4789 |
| Vtep-to-Vtep Bridging | True |
| EVPN MLAG Shared Router MAC | mlag-system-id |
| VXLAN flood-lists learning from data-plane | Enabled |
| Qos dscp propagation encapsulation | Enabled |
| Qos ECN propagation | Enabled |
| Qos map dscp to traffic-class decapsulation | Enabled |
| Remote VTEPs EVPN BFD transmission rate | 300ms |
| Remote VTEPs EVPN BFD expected minimum incoming rate (min-rx) | 300ms |
| Remote VTEPs EVPN BFD multiplier | 3 |
| Remote VTEPs EVPN BFD prefix-list | PL-TEST |
| Multicast headend-replication | Enabled |

##### VLAN to VNI, Flood List and Multicast Group Mappings

| VLAN | VNI | Flood List | Multicast Group |
| ---- | --- | ---------- | --------------- |
| 110 | 10110 | - | 239.9.1.4 |
| 111 | 10111 | 10.1.1.10<br/>10.1.1.11 | - |
| 112 | - | - | 239.9.1.6 |

##### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| Tenant_A_OP_Zone | 10 | 232.0.0.10 |
| Tenant_A_WEB_Zone | 11 | - |

##### Default Flood List

| Default Flood List |
| ------------------ |
| 10.1.0.10<br/>10.1.0.11 |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description DC1-LEAF2A_VTEP
   vxlan source-interface Loopback0
   vxlan controller-client
   vxlan virtual-router encapsulation mac-address mlag-system-id
   vxlan udp-port 4789
   vxlan bridging vtep-to-vtep
   vxlan flood vtep learned data-plane
   vxlan vlan 110 vni 10110
   vxlan vlan 111 vni 10111
   vxlan vrf Tenant_A_OP_Zone vni 10
   vxlan vrf Tenant_A_WEB_Zone vni 11
   vxlan mlag source-interface Loopback1
   bfd vtep evpn interval 300 min-rx 300 multiplier 3
   bfd vtep evpn prefix-list PL-TEST
   vxlan flood vtep 10.1.0.10 10.1.0.11
   vxlan vlan 111 flood vtep 10.1.1.10 10.1.1.11
   vxlan vlan 110 multicast group 239.9.1.4
   vxlan vlan 112 multicast group 239.9.1.6
   vxlan vrf Tenant_A_OP_Zone multicast group 232.0.0.10
   vxlan multicast headend-replication
   vxlan qos ecn propagation
   vxlan qos dscp propagation encapsulation
   vxlan qos map dscp to traffic-class decapsulation
   vxlan encapsulation ipv4

```
