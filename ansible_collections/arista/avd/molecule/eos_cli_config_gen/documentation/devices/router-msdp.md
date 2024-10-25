# router-msdp

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Multicast](#multicast)
  - [Router MSDP](#router-msdp-1)

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

### Router MSDP

#### Router MSDP Peers

| Peer Address | Disabled | VRF | Default-peer | Default-peer Prefix List | Mesh Groups | Local Interface | Description | Inbound SA Filter | Outbound SA Filter |
| ------------ | -------- | --- | ------------ | ------------------------ | ----------- | --------------- | ----------- | ----------------- | ------------------ |
| 1.2.3.4 | True | default | True | PLIST1 | MG1, MG2 | Loopback11 | Some kind of MSDP Peer | ACL1 | ACL2 |
| 4.3.2.1 | False | default | False | PLIST2 | - | Loopback21 | - | - | - |
| 2.3.4.5 | False | RED | True | - | - | Loopback13 | Some other kind of MSDP Peer | ACL3 | ACL4 |

#### Router MSDP Device Configuration

```eos
!
router msdp
   group-limit 100 source 10.0.1.0/24
   group-limit 123 source 10.0.123.0/24
   originator-id local-interface Loopback10
   rejected-limit 123
   forward register-packets
   connection retry interval 5
   !
   peer 1.2.3.4
      default-peer prefix-list PLIST1
      mesh-group MG1
      mesh-group MG2
      local-interface Loopback11
      keepalive 10 30
      sa-filter in list ACL1
      sa-filter out list ACL2
      description Some kind of MSDP Peer
      disabled
      sa-limit 1000
   !
   peer 4.3.2.1
      local-interface Loopback21
   !
   vrf RED
      group-limit 22 source 10.0.22.0/24
      originator-id local-interface Loopback12
      rejected-limit 10
      connection retry interval 10
      !
      peer 2.3.4.5
         default-peer
         local-interface Loopback13
         keepalive 5 15
         sa-filter in list ACL3
         sa-filter out list ACL4
         description Some other kind of MSDP Peer
         sa-limit 100
```
