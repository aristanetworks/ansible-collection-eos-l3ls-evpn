# router-internet-exit

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Router Internet Exit](#router-internet-exit-1)

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

### Router Internet Exit

#### Exit Groups

| Exit Group Name | Local Connections | Fib Default |
| --------------- | ----------------- | ----------- |
| eg_01 | - | - |
| eg_02 | - | True |
| eg_03 | eg_03_lo_01<br>eg_03_lo_02 | True |
| eg_04 | eg_04_lo_01<br>eg_04_lo_02<br>eg_04_lo_03 | - |

#### Internet Exit Policies

| Policy Name | Exit Groups |
| ----------- | ----------- |
| po_01 | po_eg_01_02<br>po_eg_01_04<br>po_eg_01_01<br>po_eg_01_03<br>system-default-exit-group |
| po_02 | - |
| po_03 | po_eg_03_01 |

#### Router Internet Exit Device Configuration

```eos
!
router internet-exit
   exit-group eg_01
   !
   exit-group eg_02
      fib-default
   !
   exit-group eg_03
      local connection eg_03_lo_01
      local connection eg_03_lo_02
      fib-default
   !
   exit-group eg_04
      local connection eg_04_lo_01
      local connection eg_04_lo_02
      local connection eg_04_lo_03
   !
   policy po_01
      exit-group po_eg_01_02
      exit-group po_eg_01_04
      exit-group po_eg_01_01
      exit-group po_eg_01_03
      exit-group system-default-exit-group
   !
   policy po_02
   !
   policy po_03
      exit-group po_eg_03_01
```
