# router-general

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Routing](#routing)
  - [Router General](#router-general-1)

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

## Routing

### Router General

- Global IPv4 Router ID: 10.1.2.3

- Global IPv6 Router ID: 2001:beef:cafe::1

- Nexthop fast fail-over is enabled.

#### VRF Route leaking

| VRF | Source VRF | Route Map Policy |
|-----|------------|------------------|
| BLUE-C2 | BLUE-C1 | RM-BLUE-LEAKING |
| BLUE-C2 | BLUE-C3 | RM-BLUE-LEAKING |

#### VRF Routes Dynamic Prefix-lists

| VRF | Dynamic Prefix-list |
|-----|---------------------|
| BLUE-C2 | DYNAMIC_TEST_PREFIX_LIST_1 |
| BLUE-C2 | DYNAMIC_TEST_PREFIX_LIST_2 |

#### Router General Device Configuration

```eos
!
router general
   router-id ipv4 10.1.2.3
   router-id ipv6 2001:beef:cafe::1
   hardware next-hop fast-failover
   !
   vrf BLUE-C2
      leak routes source-vrf BLUE-C1 subscribe-policy RM-BLUE-LEAKING
      leak routes source-vrf BLUE-C3 subscribe-policy RM-BLUE-LEAKING
      routes dynamic prefix-list DYNAMIC_TEST_PREFIX_LIST_1
      routes dynamic prefix-list DYNAMIC_TEST_PREFIX_LIST_2
      exit
   !
   control-functions
      code unit code1
         function ACCEPT_ALL() {
           return true;
           }
         EOF
      code unit code2
         function DENY_ALL() {
           return true;
           }
         EOF
   !
   exit
```
