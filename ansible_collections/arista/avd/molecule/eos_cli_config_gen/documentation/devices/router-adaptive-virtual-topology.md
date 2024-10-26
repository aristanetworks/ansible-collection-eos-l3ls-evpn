# router-adaptive-virtual-topology

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Routing](#routing)
  - [Router Adaptive Virtual Topology](#router-adaptive-virtual-topology-1)

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

### Router Adaptive Virtual Topology

#### Router Adaptive Virtual Topology Summary

Topology role: pathfinder

| Hierarchy | Name | ID |
| --------- | ---- | -- |
| Region | North_America | 1 |
| Zone | Canada | 2 |
| Site | Ottawa | 99 |

#### AVT Profiles

| Profile name | Load balance policy | Internet exit policy |
| ------------ | ------------------- | -------------------- |
| office365 | - | - |
| scavenger | scavenger-lb | scavenger-ie |
| video | - | video-ie |
| voice | voice-lb | - |

#### AVT Policies

##### AVT policy production

| Application profile | AVT Profile | Traffic Class | DSCP |
| ------------------- | ----------- | ------------- | ---- |
| videoApps | - | - | - |
| criticalApps | crit | 7 | 45 |
| audioApps | audio | 6 | - |
| mfgApp | crit | - | 54 |
| hrApp | hr | - | - |

#### VRFs configuration

##### VRF blue

| AVT Profile | AVT ID |
| ----------- | ------ |
| video | 1 |

##### VRF red

| AVT policy |
| ---------- |
| production |

| AVT Profile | AVT ID |
| ----------- | ------ |
| video | 1 |
| voice | 2 |

#### Router Adaptive Virtual Topology Configuration

```eos
!
router adaptive-virtual-topology
   topology role pathfinder
   region North_America id 1
   zone Canada id 2
   site Ottawa id 99
   !
   policy production
      !
      match application-profile videoApps
      !
      match application-profile criticalApps
         avt profile crit
         traffic-class 7
         dscp 45
      !
      match application-profile audioApps
         avt profile audio
         traffic-class 6
      !
      match application-profile mfgApp
         avt profile crit
         dscp 54
      !
      match application-profile hrApp
         avt profile hr
   !
   profile office365
   !
   profile scavenger
      internet-exit policy scavenger-ie
      path-selection load-balance scavenger-lb
   !
   profile video
      internet-exit policy video-ie
   !
   profile voice
      path-selection load-balance voice-lb
   !
   vrf blue
      avt profile video id 1
   !
   vrf red
      avt policy production
      avt profile video id 1
      avt profile voice id 2
```
