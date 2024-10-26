# patch-panel

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Patch Panel](#patch-panel-1)
  - [Patch Panel Summary](#patch-panel-summary)
  - [Patch Panel Device Configuration](#patch-panel-device-configuration)

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

## Patch Panel

### Patch Panel Summary

Patch Panel Connector Interface Recovery Review Delay Min: 10s - Max: 900s

Patch Panel Connector Interface Path BGP VPWS Remote Failure Errdisable is enabled.

#### Patch Panel Connections

| Patch Name | Enabled | Connector A Type | Connector A Endpoint | Connector B Type | Connector B Endpoint |
| ---------- | ------- | ---------------- | -------------------- | ---------------- | -------------------- |
| TEN_B_site2_site5_eline | True | Interface | Ethernet5 | Pseudowire | bgp vpws TENANT_A pseudowire TEN_B_site2_site5_eline |
| TEN_A_site2_site5_eline | False | Interface | Ethernet6 dot1q vlan 123 | Pseudowire | ldp LDP_PW_1 |

### Patch Panel Device Configuration

```eos
!
patch panel
   connector interface recovery review delay 10 900
   connector interface patch bgp vpws remote-failure errdisable
   !
   patch TEN_A_site2_site5_eline
      shutdown
      connector 1 interface Ethernet6 dot1q vlan 123
      connector 2 pseudowire ldp LDP_PW_1
   !
   patch TEN_B_site2_site5_eline
      connector 1 interface Ethernet5
      connector 2 pseudowire bgp vpws TENANT_A pseudowire TEN_B_site2_site5_eline
   !
```
