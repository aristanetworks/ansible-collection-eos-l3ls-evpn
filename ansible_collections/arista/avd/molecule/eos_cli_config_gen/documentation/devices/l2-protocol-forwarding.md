# l2-protocol-forwarding

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [L2 Protocol Forwarding](#l2-protocol-forwarding-1)
  - [Forwarding Profiles](#forwarding-profiles)
  - [L2 Protocol Forwarding Device Configuration](#l2-protocol-forwarding-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)

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

## L2 Protocol Forwarding

### Forwarding Profiles

#### TEST1

| Protocol | Forward | Tagged Forward | Untagged Forward |
| -------- | ------- | -------------- | ---------------- |
| bfd per-link rfc-7130 | True | True | True |
| e-lmi | True | True | True |
| isis | True | True | True |
| lacp | True | True | True |
| lldp | True | True | True |
| macsec | True | True | True |
| pause | True | True | True |
| stp | True | True | True |

#### TEST2

| Protocol | Forward | Tagged Forward | Untagged Forward |
| -------- | ------- | -------------- | ---------------- |
| bfd per-link rfc-7130 | False | True | - |
| e-lmi | True | - | - |
| isis | - | - | True |
| lacp | True | False | True |
| lldp | False | True | False |
| macsec | - | True | - |
| pause | False | - | True |
| stp | - | True | True |

### L2 Protocol Forwarding Device Configuration

```eos
!
l2-protocol
   forwarding profile TEST1
      bfd per-link rfc-7130 forward
      bfd per-link rfc-7130 tagged forward
      bfd per-link rfc-7130 untagged forward
      e-lmi forward
      e-lmi tagged forward
      e-lmi untagged forward
      isis forward
      isis tagged forward
      isis untagged forward
      lacp forward
      lacp tagged forward
      lacp untagged forward
      lldp forward
      lldp tagged forward
      lldp untagged forward
      macsec forward
      macsec tagged forward
      macsec untagged forward
      pause forward
      pause tagged forward
      pause untagged forward
      stp forward
      stp tagged forward
      stp untagged forward
   forwarding profile TEST2
      bfd per-link rfc-7130 tagged forward
      e-lmi forward
      isis untagged forward
      lacp forward
      lacp untagged forward
      lldp tagged forward
      macsec tagged forward
      pause untagged forward
      stp tagged forward
      stp untagged forward
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet1 | L2PF test | - | - | - | - | - |

*Inherited from Port-Channel Interface

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description L2PF test
   l2-protocol forwarding profile TEST1
   switchport
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel1 | L2PF test | - | - | - | - | - | - | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel1
   description L2PF test
   l2-protocol forwarding profile TEST2
   switchport
```
