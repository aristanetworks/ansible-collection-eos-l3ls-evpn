# hardware-counter

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitoring](#monitoring)
  - [Hardware](#hardware)

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

## Monitoring

### Hardware

#### Hardware Counters

##### Hardware Counters Summary

###### Hardware Counter Features

**NOTE:** Not all options (columns) in the table below are compatible with every available feature, it is the user responsibility to configure valid options for each feature.

| Feature | Flow Direction | Address Type | Layer3 | VRF | Prefix | Units Packets |
| ------- | -------------- | ------------ | ------ | --- | ------ | ------------- |
| acl | out | mac | - | - | - | - |
| gre tunnel interface | out | - | - | - | - | - |
| ip | in | - | - | False | - | False |
| ip | out | - | - | True | - | True |
| mpls lfib | - | - | - | - | - | True |
| route | - | ipv4 | test | - | 192.168.0.0/24 | - |
| route | - | ipv6 | - | - | 2001:db8:cafe::/64 | - |
| segment-security | in | - | - | - | - | - |

#### Hardware Device Configuration

```eos
!
hardware counter feature acl out mac
hardware counter feature gre tunnel interface out
hardware counter feature ip in
hardware counter feature ip out layer3 units packets
hardware counter feature mpls lfib units packets
hardware counter feature route ipv4 vrf test 192.168.0.0/24
hardware counter feature route ipv6 2001:db8:cafe::/64
hardware counter feature segment-security in
```
