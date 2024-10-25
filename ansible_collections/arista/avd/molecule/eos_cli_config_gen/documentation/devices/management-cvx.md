# management-cvx

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Management CVX Summary](#management-cvx-summary)

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

### Management CVX Summary

| Shutdown | CVX Servers |
| -------- | ----------- |
| False | 10.90.224.188, 10.90.224.189, leaf1.atd.lab |

#### Management CVX Source Interface

| Interface | VRF |
| --------- | --- |
| Loopback0 | MGMT |

#### Management CVX Device Configuration

```eos
!
management cvx
   no shutdown
   server host 10.90.224.188
   server host 10.90.224.189
   server host leaf1.atd.lab
   source-interface Loopback0
   vrf MGMT
```
