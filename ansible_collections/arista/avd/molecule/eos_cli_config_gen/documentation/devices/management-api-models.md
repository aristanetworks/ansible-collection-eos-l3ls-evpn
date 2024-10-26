# management-api-models

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Management API Models](#management-api-models-1)

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

### Management API Models

#### Management API Models Summary

| Provider | Path | Disabled |
| -------- | ---- | ------- |
| smash | flexCounters | False |
| smash | forwarding/srte/status/fec | False |
| smash | routing6/status | False |
| smash | routing/bgp/export/allPeerAdjRibIn | False |
| smash | routing/status | True |
| smash | tunnel/tunnelFib/entry | False |
| sysdb | /Sysdb/sys/logging/config/vrfLoggingHost/mgmt | True |
| sysdb | cell/1/agent | True |

#### Management API Models Device Configuration

```eos
!
management api models
   !
   provider smash
      path flexCounters
      path forwarding/srte/status/fec
      path routing6/status
      path routing/bgp/export/allPeerAdjRibIn
      path routing/status disabled
      path tunnel/tunnelFib/entry
   !
   provider sysdb
      path /Sysdb/sys/logging/config/vrfLoggingHost/mgmt disabled
      path cell/1/agent disabled
```
