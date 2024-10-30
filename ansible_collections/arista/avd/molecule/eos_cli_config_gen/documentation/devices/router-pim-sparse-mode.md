# router-pim-sparse-mode

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Multicast](#multicast)
  - [PIM Sparse Mode](#pim-sparse-mode)

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

## Multicast

### PIM Sparse Mode

#### Router PIM Sparse Mode

##### IP Sparse Mode Information

BFD enabled: True

##### IP Rendezvous Information

| Rendezvous Point Address | Group Address | Access Lists | Priority | Hashmask | Override |
| ------------------------ | ------------- | ------------ | -------- | -------- | -------- |
| 10.238.1.161 | 239.12.12.12/32, 239.12.12.13/32, 239.12.12.14/32, 239.12.12.16/32, 239.12.12.20/32, 239.12.12.21/32 | RP_ACL, RP_ACL2 | 20 | - | - |
| 10.238.1.161 | 239.12.12.17/32 | RP_ACL3 | - | - | - |

##### IP Anycast Information

| IP Anycast Address | Other Rendezvous Point Address | Register Count |
| ------------------ | ------------------------------ | -------------- |
| 10.38.1.161 | 10.50.64.16 | 15 |

##### IP Sparse Mode VRFs

| VRF Name | BFD Enabled |
| -------- | ----------- |
| MCAST_VRF1 | True |
| MCAST_VRF2_ALL_GROUPS | False |
| Test_RP_ACL | False |

| VRF Name | Rendezvous Point Address | Group Address | Access Lists | Priority | Hashmask | Override |
| -------- | ------------------------ | ------------- | ------------ | -------- | -------- | -------- |
| MCAST_VRF1 | 10.238.2.161 | 239.12.22.12/32, 239.12.22.13/32, 239.12.22.14/32 | - | - | - | - |
| MCAST_VRF2_ALL_GROUPS | 10.238.3.161 | - | - | - | 30 | - |
| Test_RP_ACL | 10.238.4.161 | - | RP_ACL | - | - | - |
| Test_RP_ACL | 10.238.4.161 | - | RP_ACL2 | 20 | 30 | True |

##### Router Multicast Device Configuration

```eos
!
router pim sparse-mode
   ipv4
      ssm range standard
      bfd
      rp address 10.238.1.161 239.12.12.12/32 priority 20
      rp address 10.238.1.161 239.12.12.13/32 priority 20
      rp address 10.238.1.161 239.12.12.14/32 priority 20
      rp address 10.238.1.161 239.12.12.16/32 priority 20
      rp address 10.238.1.161 239.12.12.20/32 priority 20
      rp address 10.238.1.161 239.12.12.21/32 priority 20
      rp address 10.238.1.161 access-list RP_ACL priority 20
      rp address 10.238.1.161 access-list RP_ACL2 priority 20
      rp address 10.238.1.161 239.12.12.17/32
      rp address 10.238.1.161 access-list RP_ACL3
      anycast-rp 10.38.1.161 10.50.64.16 register-count 15
   !
   vrf MCAST_VRF1
      ipv4
         bfd
         rp address 10.238.2.161 239.12.22.12/32
         rp address 10.238.2.161 239.12.22.13/32
         rp address 10.238.2.161 239.12.22.14/32
   !
   vrf MCAST_VRF2_ALL_GROUPS
      ipv4
         rp address 10.238.3.161 hashmask 30
   !
   vrf Test_RP_ACL
      ipv4
         rp address 10.238.4.161 access-list RP_ACL
         rp address 10.238.4.161 access-list RP_ACL2 priority 20 hashmask 30 override
```
