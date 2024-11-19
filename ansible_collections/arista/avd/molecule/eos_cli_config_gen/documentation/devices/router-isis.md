# router-isis

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
- [Routing](#routing)
  - [Router ISIS](#router-isis-1)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | OOB_MANAGEMENT | oob | MGMT | 10.73.254.11/24 | 10.73.254.253 |

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
   ip address 10.73.254.11/24
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_LINK_TO_EAPI-SPINE1_Ethernet1 | - | 172.31.255.1/31 | default | 1500 | - | - | - |
| Ethernet2 | P2P_LINK_TO_EAPI-SPINE2_Ethernet1 | - | 172.31.255.3/31 | default | 1500 | - | - | - |
| Ethernet4 | - | 4 | *10.9.2.3/31 | **default | **- | **- | **- | **- |
| Ethernet5 | - | 5 | *10.9.2.5/31 | **default | **- | **- | **- | **- |
| Ethernet6 | - | 6 | *10.9.2.7/31 | **default | **- | **- | **- | **- |

*Inherited from Port-Channel Interface

##### ISIS

| Interface | Channel Group | ISIS Instance | ISIS BFD | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | ISIS Authentication Mode |
| --------- | ------------- | ------------- | -------- | ----------- | ---- | ----------------- | ------------- | ------------------------ |
| Ethernet1 | - | EVPN_UNDERLAY | - | 50 | point-to-point | - | - | - |
| Ethernet2 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-1-2 | - | - |
| Ethernet4 | 4 | *EVPN_UNDERLAY | - | *50 | *point-to-point | *level-2 | *- | *- |
| Ethernet5 | 5 | *EVPN_UNDERLAY | - | *50 | *passive | *- | *- | *- |
| Ethernet6 | 6 | *EVPN_UNDERLAY | - | *100 | *- | *level-1-2 | *- | *- |

*Inherited from Port-Channel Interface

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_EAPI-SPINE1_Ethernet1
   mtu 1500
   no switchport
   ip address 172.31.255.1/31
   isis enable EVPN_UNDERLAY
   isis metric 50
   isis network point-to-point
!
interface Ethernet2
   description P2P_LINK_TO_EAPI-SPINE2_Ethernet1
   mtu 1500
   no switchport
   ip address 172.31.255.3/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-1-2
   isis metric 50
   isis network point-to-point
!
interface Ethernet3
   description MLAG_PEER_EAPI-LEAF1B_Ethernet3
   channel-group 3 mode active
!
interface Ethernet4
   channel-group 4 mode active
!
interface Ethernet5
   channel-group 5 mode active
!
interface Ethernet6
   channel-group 6 mode active
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |

##### IPv4

| Interface | Description | MLAG ID | IP Address | VRF | MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------- | ---------- | --- | --- | -------- | ------ | ------- |
| Port-Channel4 | - | - | 10.9.2.3/31 | default | - | - | - | - |
| Port-Channel5 | - | - | 10.9.2.5/31 | default | - | - | - | - |
| Port-Channel6 | - | - | 10.9.2.7/31 | default | - | - | - | - |

##### ISIS

| Interface | ISIS Instance | ISIS BFD | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | ISIS Authentication Mode |
| --------- | ------------- | -------- | ----------- | ---- | ----------------- | ------------- | ------------------------ |
| Port-Channel4 | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Port-Channel5 | EVPN_UNDERLAY | - | 50 | passive | - | - | - |
| Port-Channel6 | EVPN_UNDERLAY | - | 100 | - | level-1-2 | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel4
   no switchport
   ip address 10.9.2.3/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
!
interface Port-Channel5
   no switchport
   ip address 10.9.2.5/31
   isis enable EVPN_UNDERLAY
   isis metric 50
   isis passive
!
interface Port-Channel6
   no switchport
   ip address 10.9.2.7/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-1-2
   isis metric 100
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 192.168.255.3/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 192.168.254.3/32 |
| Loopback2 | ISIS-SR Node-SID | default | 10.1.255.3/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | - |
| Loopback2 | ISIS-SR Node-SID | default | - |

##### ISIS

| Interface | ISIS instance | ISIS metric | Interface mode |
| --------- | ------------- | ----------- | -------------- |
| Loopback0 | EVPN_UNDERLAY | - | passive |
| Loopback1 | EVPN_UNDERLAY | - | passive |
| Loopback2 | EVPN_UNDERLAY | 50 | passive |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description EVPN_Overlay_Peering
   ip address 192.168.255.3/32
   isis enable EVPN_UNDERLAY
   isis passive
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   ip address 192.168.254.3/32
   isis enable EVPN_UNDERLAY
   isis passive
!
interface Loopback2
   description ISIS-SR Node-SID
   ip address 10.1.255.3/32
   node-segment ipv4 index 10
   node-segment ipv6 index 1000
   isis enable EVPN_UNDERLAY
   isis metric 50
   isis passive
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan110 | PR01-DEMO | TENANT_A_PROJECT01 | - | False |
| Vlan4093 | MLAG_PEER_L3_PEERING | default | - | - |
| Vlan4094 | MLAG_PEER | default | 1500 | - |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| Vlan110 |  TENANT_A_PROJECT01  |  -  |  10.1.10.254/24  |  -  |  -  |  -  |
| Vlan4093 |  default  |  10.255.251.0/31  |  -  |  -  |  -  |  -  |
| Vlan4094 |  default  |  10.255.252.0/31  |  -  |  -  |  -  |  -  |

##### ISIS

| Interface | ISIS Instance | ISIS BFD | ISIS Metric | Mode | ISIS Authentication Mode |
| --------- | ------------- | -------- | ----------- | ---- | ------------------------ |
| Vlan4093 | EVPN_UNDERLAY | - | 50 | point-to-point | - |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan110
   description PR01-DEMO
   no shutdown
   vrf TENANT_A_PROJECT01
   ip address virtual 10.1.10.254/24
!
interface Vlan4093
   description MLAG_PEER_L3_PEERING
   ip address 10.255.251.0/31
   isis enable EVPN_UNDERLAY
   isis metric 50
   isis network point-to-point
!
interface Vlan4094
   description MLAG_PEER
   mtu 1500
   no autostate
   ip address 10.255.252.0/31
```

## Routing

### Router ISIS

#### Router ISIS Summary

| Settings | Value |
| -------- | ----- |
| Instance | EVPN_UNDERLAY |
| Net-ID | 49.0001.0001.0001.0001.00 |
| Type | level-2 |
| Router-ID | 192.168.255.3 |
| Log Adjacency Changes | True |
| Advertise Passive-only | True |
| SR MPLS Enabled | False |
| SPF Interval | 250 seconds |

#### ISIS Route Timers

| Settings | Value |
| -------- | ----- |
| Local Convergence Delay | 15000 milliseconds |
| CSN Packet Transmission Interval | 10 seconds |
| CSN Packet P2P Links Disabled | True |
| LSP Generation Maximum Interval | 30 seconds |
| LSP Generation Initial Wait-time | 40 milliseconds |
| LSP Generation Wait-time | 50 milliseconds |
| LSP Out-delay | 20 milliseconds |
| LSP Refresh Interval | 56 seconds |
| LSP Minimum Remaining Lifetime | 78 seconds |

#### ISIS Route Redistribution

| Route Type | Route-Map | Include Leaked |
| ---------- | --------- | -------------- |
| bgp | RM-BGP | - |

#### ISIS Interfaces Summary

| Interface | ISIS Instance | ISIS Metric | Interface Mode |
| --------- | ------------- | ----------- | -------------- |
| Ethernet1 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet2 | EVPN_UNDERLAY | 50 | point-to-point |
| Vlan4093 | EVPN_UNDERLAY | 50 | point-to-point |
| Loopback0 | EVPN_UNDERLAY | - | passive |
| Loopback1 | EVPN_UNDERLAY | - | passive |
| Loopback2 | EVPN_UNDERLAY | 50 | passive |

#### ISIS Segment-routing Node-SID

| Loopback | IPv4 Index | IPv6 Index |
| -------- | ---------- | ---------- |
| Loopback2 | 10 | 1000 |

#### Prefix Segments

| Prefix Segment | Index |
| -------------- | ----- |
| 155.2.1.19/32 | 2121 |

#### ISIS IPv4 Address Family Summary

| Settings | Value |
| -------- | ----- |
| IPv4 Address-family Enabled | True |
| TI-LFA Mode | node-protection |
| TI-LFA Level | level-2 |
| TI-LFA SRLG Enabled | True |

#### Tunnel Source

| Source Protocol | RCF |
| --------------- | --- |
| BGP Labeled-Unicast | - |

#### ISIS IPv6 Address Family Summary

| Settings | Value |
| -------- | ----- |
| IPv6 Address-family Enabled | True |
| BFD All-interfaces | True |
| TI-LFA SRLG Enabled | True |

#### Router ISIS Device Configuration

```eos
!
router isis EVPN_UNDERLAY
   net 49.0001.0001.0001.0001.00
   router-id ipv4 192.168.255.3
   is-type level-2
   log-adjacency-changes
   redistribute bgp route-map RM-BGP
   timers local-convergence-delay 15000 protected-prefixes
   set-overload-bit on-startup wait-for-bgp
   advertise passive-only
   spf-interval 250
   timers csnp generation interval 10 seconds
   timers csnp generation p2p disabled
   timers lsp out-delay 20
   timers lsp refresh 56
   timers lsp generation 30 40 50
   timers lsp min-remaining-lifetime 78
   authentication mode sha key-id 5 rx-disabled level-1
   authentication mode shared-secret profile test2 algorithm md5 rx-disabled level-2
   authentication key 0 password
   !
   address-family ipv4 unicast
      tunnel source-protocol bgp ipv4 labeled-unicast
      fast-reroute ti-lfa mode node-protection level-2
      fast-reroute ti-lfa srlg
   !
   address-family ipv6 unicast
      bfd all-interfaces
      fast-reroute ti-lfa srlg
   !
   segment-routing mpls
      shutdown
      prefix-segment 155.2.1.19/32 index 2121
   address-family ipv6 unicast
     multi-topology
   traffic-engineering
     no shutdown
     is-type level-2
```
