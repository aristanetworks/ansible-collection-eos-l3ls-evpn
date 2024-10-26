# system

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [System Control-Plane](#system-control-plane)
- [System L1](#system-l1)
  - [Unsupported Interface Configurations](#unsupported-interface-configurations)
  - [System L1 Device Configuration](#system-l1-device-configuration)

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

### System Control-Plane

#### TCP MSS Ceiling

| Protocol | Segment Size |
| -------- | -------------|
| IPv4 | 1344 |
| IPv6 | 1366 |

#### Control-Plane Access-Groups

| Protocol | VRF | Access-list |
| -------- | --- | ------------|
| IPv4 | default | acl4_1 |
| IPv4 | red | acl4_2 |
| IPv4 | red_1 | acl4_2 |
| IPv4 | default | acl4_3 |
| IPv6 | default | acl6_1 |
| IPv6 | blue | acl6_2 |
| IPv6 | blue_1 | acl6_2 |
| IPv6 | default | acl6_3 |

#### System Control-Plane Device Configuration

```eos
!
system control-plane
   tcp mss ceiling ipv4 1344 ipv6 1366
   ip access-group acl4_1 in
   ip access-group acl4_3 vrf default in
   ip access-group acl4_2 vrf red in
   ip access-group acl4_2 vrf red_1 in
   ipv6 access-group acl6_1 in
   ipv6 access-group acl6_3 vrf default in
   ipv6 access-group acl6_2 vrf blue in
   ipv6 access-group acl6_2 vrf blue_1 in
```

## System L1

### Unsupported Interface Configurations

| Unsupported Configuration | action |
| ---------------- | -------|
| Speed | warn |
| Error correction | error |

### System L1 Device Configuration

```eos
!
system l1
   unsupported speed action warn
   unsupported error-correction action error
```
