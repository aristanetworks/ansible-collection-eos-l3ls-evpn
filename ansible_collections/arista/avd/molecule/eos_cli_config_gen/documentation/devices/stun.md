# stun

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [STUN](#stun-1)
  - [STUN Client](#stun-client)
  - [STUN Server](#stun-server)
  - [STUN Device Configuration](#stun-device-configuration)

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

## STUN

### STUN Client

#### Server Profiles

| Server Profile | IP address | SSL Profile | Port |
| -------------- | ---------- | ----------- | ---- |
| server1 | 1.2.3.4 | pathfinder | 3478 |
| server2 | 2.3.4.5 | - | 4100 |

### STUN Server

| Server Local Interfaces | Bindings Timeout (s) | SSL Profile | SSL Connection Lifetime | Port |
| ----------------------- | -------------------- | ----------- | ----------------------- | ---- |
| Ethernet1<br>Ethernet13<br>Vlan42<br>Vlan666 | 600 | pathfinder | 1300 minutes | 4100 |

### STUN Device Configuration

```eos
!
stun
   client
      server-profile server1
         ip address 1.2.3.4
         ssl profile pathfinder
      server-profile server2
         ip address 2.3.4.5
         port 4100
   server
      local-interface Ethernet1
      local-interface Ethernet13
      local-interface Vlan42
      local-interface Vlan666
      port 4100
      ssl profile pathfinder
      binding timeout 600 seconds
      ssl connection lifetime 1300 minutes
```
