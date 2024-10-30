# traffic-policies-2

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Interfaces](#interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Traffic Policies information](#traffic-policies-information)

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

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel2
   no switchport
```

### Traffic Policies information

#### IPv6 Field Sets

| Field Set Name | IPv6 Prefixes |
| -------------- | ------------- |
| IPv6-DEMO-1 | 11:22:33:44:55:66:77:88 |
| IPv6-DEMO-2 | - |

#### Traffic Policies Device Configuration

```eos
!
traffic-policies
   field-set ipv6 prefix IPv6-DEMO-1
      11:22:33:44:55:66:77:88
   !
   field-set ipv6 prefix IPv6-DEMO-2
```
