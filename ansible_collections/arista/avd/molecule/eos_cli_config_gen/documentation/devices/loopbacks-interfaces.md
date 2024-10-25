# loopbacks-interfaces

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Interfaces](#interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
- [MPLS](#mpls)
  - [MPLS Interfaces](#mpls-interfaces)

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

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 192.168.255.3/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 192.168.254.3/32 |
| Loopback99 | TENANT_A_PROJECT02_VTEP_DIAGNOSTICS | TENANT_A_PROJECT02 | 10.1.255.3/32 <br> 192.168.1.1/32 secondary <br> 10.0.0.254/32 secondary |
| Loopback100 | TENANT_A_PROJECT02_VTEP_DIAGNOSTICS | TENANT_A_PROJECT02 | 10.1.255.3/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | - |
| Loopback99 | TENANT_A_PROJECT02_VTEP_DIAGNOSTICS | TENANT_A_PROJECT02 | 2002::CAFE/64 |
| Loopback100 | TENANT_A_PROJECT02_VTEP_DIAGNOSTICS | TENANT_A_PROJECT02 | - |

##### ISIS

| Interface | ISIS instance | ISIS metric | Interface mode |
| --------- | ------------- | ----------- | -------------- |
| Loopback99 | ISIS_TEST | 100 | point-to-point |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   ip address 192.168.255.3/32
   comment
   Comment created from eos_cli under loopback_interfaces.Loopback0
   EOF

!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   ip address 192.168.254.3/32
!
interface Loopback99
   description TENANT_A_PROJECT02_VTEP_DIAGNOSTICS
   no shutdown
   vrf TENANT_A_PROJECT02
   ip proxy-arp
   ip address 10.1.255.3/32
   ip address 10.0.0.254/32 secondary
   ip address 192.168.1.1/32 secondary
   ipv6 enable
   ipv6 address 2002::CAFE/64
   mpls ldp interface
   isis enable ISIS_TEST
   isis bfd
   isis metric 100
   isis passive
   isis network point-to-point
!
interface Loopback100
   description TENANT_A_PROJECT02_VTEP_DIAGNOSTICS
   vrf TENANT_A_PROJECT02
   ip address 10.1.255.3/32
```

## MPLS

### MPLS Interfaces

| Interface | MPLS IP Enabled | LDP Enabled | IGP Sync |
| --------- | --------------- | ----------- | -------- |
| Loopback99 | - | True | - |
