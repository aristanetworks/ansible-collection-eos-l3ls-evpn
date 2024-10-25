# ptp

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [PTP](#ptp-1)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)

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

### PTP

PTP Profile: g8275.1

#### PTP Summary

| Clock ID | Source IP | Priority 1 | Priority 2 | TTL | Domain | Mode | Forward Unicast |
| -------- | --------- | ---------- | ---------- | --- | ------ | ---- | --------------- |
| 11:11:11:11:11:11 | 1.1.2.3 | 101 | 102 | 12 | 17 | boundary | True |

#### PTP Device Configuration

```eos
!
ptp clock-identity 11:11:11:11:11:11
ptp domain 17
ptp message-type event dscp 46 default
ptp message-type general dscp 36 default
ptp mode boundary one-step
ptp priority1 101
ptp priority2 102
ptp profile g8275.1
ptp source ip 1.1.2.3
ptp ttl 12
ptp forward-unicast
ptp monitor threshold offset-from-master 11
ptp monitor threshold mean-path-delay 12
ptp monitor threshold mean-path-delay 14 nanoseconds drop
ptp monitor threshold offset-from-master 13 nanoseconds drop
ptp monitor threshold missing-message sync 103 intervals
ptp monitor threshold missing-message follow-up 102 intervals
ptp monitor threshold missing-message announce 101 intervals
ptp monitor sequence-id
ptp monitor threshold missing-message sync 204 sequence-ids
ptp monitor threshold missing-message follow-up 203 sequence-ids
ptp monitor threshold missing-message delay-resp 202 sequence-ids
ptp monitor threshold missing-message announce 201 sequence-ids
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet3 | P2P_LINK_TO_DC1-SPINE2_Ethernet5 | trunk | 2,14 | - | - | - |
| Ethernet5 | DC1-AGG01_Ethernet1 | *trunk | *110,201 | *- | *- | 5 |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet6 | P2P_LINK_TO_DC1-SPINE1_Ethernet6 | - | 172.31.255.15/31 | default | 1500 | - | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet3
   description P2P_LINK_TO_DC1-SPINE2_Ethernet5
   switchport trunk allowed vlan 2,14
   switchport mode trunk
   switchport
   ptp enable
   ptp delay-mechanism e2e
   ptp role dynamic
   ptp sync-message interval 1
   ptp transport layer2
   ptp vlan 2
!
interface Ethernet5
   description DC1-AGG01_Ethernet1
   channel-group 5 mode active
!
interface Ethernet6
   description P2P_LINK_TO_DC1-SPINE1_Ethernet6
   mtu 1500
   no switchport
   ip address 172.31.255.15/31
   ptp enable
   ptp announce interval 3
   ptp announce timeout 9
   ptp delay-mechanism e2e
   ptp delay-req interval -7
   ptp profile g8275.1 destination mac-address non-forwardable
   ptp role dynamic
   ptp sync-message interval 1
   ptp transport ipv4
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel5 | DC1_L2LEAF1_Po1 | trunk | 110,201 | - | - | - | - | 5 | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel5
   description DC1_L2LEAF1_Po1
   switchport trunk allowed vlan 110,201
   switchport mode trunk
   switchport
   mlag 5
   ptp enable
   ptp mpass
   ptp delay-mechanism e2e
   ptp profile g8275.1 destination mac-address forwardable
   ptp role dynamic
   ptp sync-message interval 1
   ptp transport layer2
   ptp vlan 2
```
