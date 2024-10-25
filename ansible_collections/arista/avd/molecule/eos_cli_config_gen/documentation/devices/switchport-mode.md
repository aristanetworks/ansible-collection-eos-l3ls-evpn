# switchport-mode

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Interfaces](#interfaces)
  - [Switchport Default](#switchport-default)

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

### Switchport Default

#### Switchport Defaults Summary

- Default Switchport Mode: access
- Default Switchport Phone COS: 0
- Default Switchport Phone Trunk: tagged
- Default Switchport Phone VLAN: 69

#### Switchport Default Device Configuration

```eos
!
switchport default mode access
!
switchport default phone cos 0
!
switchport default phone vlan 69
```
