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

| Protocol | VRF | Access-list | Ingress-default |
| -------- | --- | ------------| --------------- |
| IPv4 | default | acl4_1 | False |
| IPv4 | - | acl4_2 | True |
| IPv4 | default | acl4_3 | False |
| IPv4 | red_2 | acl4_4 | False |
| IPv4 | red_5 | acl4_4 | False |
| IPv4 | red_3 | acl4_5 | False |
| IPv4 | red_4 | ingress | False |
| IPv6 | default | acl6_1 | False |
| IPv6 | blue | acl6_2 | False |
| IPv6 | blue_1 | acl6_2 | False |
| IPv6 | default | acl6_3 | False |
| IPv6 | - | acl6_4 | True |
| IPv6 | blue_2 | ingress | False |

#### System Control-Plane Device Configuration

```eos
!
system control-plane
   tcp mss ceiling ipv4 1344 ipv6 1366
   ip access-group ingress default acl4_2
   ip access-group acl4_3 in
   ip access-group acl4_4 vrf red_2 in
   ip access-group acl4_5 vrf red_3 in
   ip access-group ingress vrf red_4 in
   ip access-group acl4_4 vrf red_5 in
   ip access-group ingress default acl6_4
   ip access-group acl6_3 in
   ip access-group acl6_2 vrf blue in
   ip access-group acl6_2 vrf blue_1 in
   ip access-group ingress vrf blue_2 in
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
