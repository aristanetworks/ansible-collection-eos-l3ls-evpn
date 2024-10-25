# sflow

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitoring](#monitoring)
  - [SFlow](#sflow-1)

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

### SFlow

#### SFlow Summary

| VRF | SFlow Source | SFlow Destination | Port |
| --- | ------------ | ----------------- | ---- |
| AAA | - | 10.6.75.62 | 123 |
| AAA | - | 10.6.75.63 | 333 |
| AAA | Ethernet2 | - | - |
| BBB | - | 10.6.75.62 | 6343 |
| BBB | 1.1.1.1 | - | - |
| CCC | - | 10.6.75.62 | 6343 |
| CCC | Management1 | - | - |
| MGMT | - | 10.6.75.59 | 6343 |
| MGMT | - | 10.6.75.62 | 123 |
| MGMT | - | 10.6.75.63 | 333 |
| MGMT | Ethernet3 | - | - |
| default | - | 10.6.75.62 | 123 |
| default | - | 10.6.75.61 | 6343 |
| default | Management0 | - | - |

sFlow Sample Rate: 1000

sFlow Sample Input Subinterface is enabled.

sFlow Sample Output Subinterface is enabled.

sFlow Polling Interval: 10

sFlow is enabled.

sFlow is disabled on all interfaces by default.

Unmodified egress sFlow is enabled on all interfaces by default.

sFlow hardware acceleration is enabled.

sFlow hardware accelerated Sample Rate: 1024

#### SFlow Hardware Accelerated Modules

| Module | Acceleration Enabled |
| ------ | -------------------- |
| Linecard1 | True |
| Linecard2 | True |
| Linecard3 | False |

#### SFlow Extensions

| Extension | Enabled |
| --------- | ------- |
| bgp | True |
| router | True |
| switch | False |
| tunnel | False |

#### SFlow Device Configuration

```eos
!
sflow sample dangerous 1000
sflow polling-interval 10
sflow vrf AAA destination 10.6.75.62 123
sflow vrf AAA destination 10.6.75.63 333
sflow vrf AAA source-interface Ethernet2
sflow vrf BBB destination 10.6.75.62
sflow vrf BBB source 1.1.1.1
sflow vrf CCC destination 10.6.75.62
sflow vrf CCC source-interface Management1
sflow vrf MGMT destination 10.6.75.59
sflow vrf MGMT destination 10.6.75.62 123
sflow vrf MGMT destination 10.6.75.63 333
sflow vrf MGMT source-interface Ethernet3
sflow destination 10.6.75.61
sflow destination 10.6.75.62 123
sflow source-interface Management0
sflow sample input subinterface
sflow sample output subinterface
sflow extension bgp
sflow extension router
no sflow extension switch
no sflow extension tunnel
sflow interface disable default
sflow interface egress unmodified enable default
sflow run
sflow hardware acceleration
sflow hardware acceleration sample 1024
sflow hardware acceleration module Linecard1
sflow hardware acceleration module Linecard2
no sflow hardware acceleration module Linecard3
```
