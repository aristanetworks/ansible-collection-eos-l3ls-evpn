# monitor-connectivity

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitor Connectivity](#monitor-connectivity-1)
  - [Global Configuration](#global-configuration)
  - [VRF Configuration](#vrf-configuration)
  - [Monitor Connectivity Device Configuration](#monitor-connectivity-device-configuration)

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

## Monitor Connectivity

### Global Configuration

#### Interface Sets

| Name | Interfaces |
| ---- | ---------- |
| GLOBAL_SET | Ethernet1-4 |
| HOST_SET | Loopback2-4, Loopback10-12 |

#### Probing Configuration

| Enabled | Interval | Default Interface Set | Address Only |
| ------- | -------- | --------------------- | ------------ |
| True | 5 | GLOBAL_SET | True |

#### Host Parameters

| Host Name | Description | IPv4 Address | Probing Interface Set | Address Only | URL |
| --------- | ----------- | ------------ | --------------------- | ------------ | --- |
| server1 | server1_connectivity_monitor | 10.10.10.1 | HOST_SET | True | https://server1.local.com |
| server2 | server2_connectivity_monitor | 10.10.10.2 | HOST_SET | True | https://server2.local.com |
| server3 | server3_connectivity_monitor | 10.10.10.3 | HOST_SET | False | - |
| server4 | - | - | - | True | - |

### VRF Configuration

| Name | Description | Default Interface Set | Address Only |
| ---- | ----------- | --------------------- | ------------ |
| blue | - | VRF_GLOBAL_SET | False |
| red | vrf_connectivity_monitor | VRF_GLOBAL_SET | True |
| yellow | - | - | True |

#### Vrf blue Configuration

##### Interface Sets

| Name | Interfaces |
| ---- | ---------- |
| VRF_GLOBAL_SET | Vlan21-24, Vlan29-32 |

##### Host Parameters

| Host Name | Description | IPv4 Address | Probing Interface Set | Address Only | URL |
| --------- | ----------- | ------------ | --------------------- | ------------ | --- |
| server4 | server4_connectivity_monitor | 10.10.20.1 | VRF_GLOBAL_SET | False | https://server2.local.com |
| server5 | server5_connectivity_monitor | 10.10.20.11 | VRF_GLOBAL_SET | True | https://server5.local.com |
| server6 | - | - | - | True | - |

#### Vrf red Configuration

##### Interface Sets

| Name | Interfaces |
| ---- | ---------- |
| VRF_GLOBAL_SET | Vlan21-24, Vlan29-32 |
| VRF_HOST_SET | Loopback12-14, 19-23 |

##### Host Parameters

| Host Name | Description | IPv4 Address | Probing Interface Set | Address Only | URL |
| --------- | ----------- | ------------ | --------------------- | ------------ | --- |
| server2 | server2_connectivity_monitor | 10.10.20.1 | VRF_HOST_SET | True | https://server2.local.com |

#### Vrf yellow Configuration

##### Interface Sets

| Name | Interfaces |
| ---- | ---------- |

### Monitor Connectivity Device Configuration

```eos
!
monitor connectivity
   vrf blue
      interface set VRF_GLOBAL_SET Vlan21-24, Vlan29-32
      local-interfaces VRF_GLOBAL_SET default
      !
      host server4
         description
         server4_connectivity_monitor
         local-interfaces VRF_GLOBAL_SET
         ip 10.10.20.1
         url https://server2.local.com
      !
      host server5
         description
         server5_connectivity_monitor
         local-interfaces VRF_GLOBAL_SET address-only
         ip 10.10.20.11
         url https://server5.local.com
      !
      host server6
   !
   vrf red
      interface set VRF_GLOBAL_SET Vlan21-24, Vlan29-32
      interface set VRF_HOST_SET Loopback12-14, 19-23
      description
      vrf_connectivity_monitor
      local-interfaces VRF_GLOBAL_SET address-only default
      !
      host server2
         description
         server2_connectivity_monitor
         local-interfaces VRF_HOST_SET address-only
         ip 10.10.20.1
         url https://server2.local.com
   !
   vrf yellow
   interval 5
   no shutdown
   interface set GLOBAL_SET Ethernet1-4
   interface set HOST_SET Loopback2-4, Loopback10-12
   local-interfaces GLOBAL_SET address-only default
   !
   host server1
      description
      server1_connectivity_monitor
      local-interfaces HOST_SET address-only
      ip 10.10.10.1
      url https://server1.local.com
   !
   host server2
      description
      server2_connectivity_monitor
      local-interfaces HOST_SET address-only
      ip 10.10.10.2
      url https://server2.local.com
   !
   host server3
      description
      server3_connectivity_monitor
      local-interfaces HOST_SET
      ip 10.10.10.3
   !
   host server4
```
