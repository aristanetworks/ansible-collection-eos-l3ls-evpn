# virtual-source-nat

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Virtual Source NAT](#virtual-source-nat-1)
  - [Virtual Source NAT Summary](#virtual-source-nat-summary)
  - [Virtual Source NAT Configuration](#virtual-source-nat-configuration)

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

## Virtual Source NAT

### Virtual Source NAT Summary

| Source NAT VRF | Source NAT IP Address |
| -------------- | --------------------- |
| TEST_01 | 1.1.1.1 |
| TEST_02 | 1.1.1.2 |

### Virtual Source NAT Configuration

```eos
!
ip address virtual source-nat vrf TEST_01 address 1.1.1.1
ip address virtual source-nat vrf TEST_02 address 1.1.1.2
```
