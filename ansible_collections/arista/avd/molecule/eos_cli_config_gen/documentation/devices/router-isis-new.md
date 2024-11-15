# router-isis-new

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
- [Routing](#routing)
  - [Router ISIS](#router-isis)

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

##### ISIS

| Interface | Channel Group | ISIS Instance | ISIS BFD | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | ISIS Authentication Mode |
| --------- | ------------- | ------------- | -------- | ----------- | ---- | ----------------- | ------------- | ------------------------ |
| Ethernet1 | - | EVPN_UNDERLAY | - | 50 | point-to-point | - | - | - |
| Ethernet2 | - | EVPN_UNDERLAY | - | 50 | point-to-point | - | - | - |

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
   isis metric 50
   isis network point-to-point
!
interface Ethernet3
   description MLAG_PEER_EAPI-LEAF1B_Ethernet3
   channel-group 3 mode active
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | default | 192.168.255.3/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | 192.168.254.3/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | EVPN_Overlay_Peering | default | - |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | default | - |

##### ISIS

| Interface | ISIS instance | ISIS metric | Interface mode |
| --------- | ------------- | ----------- | -------------- |
| Loopback0 | EVPN_UNDERLAY | - | passive |
| Loopback1 | EVPN_UNDERLAY | - | passive |

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
| Log Adjacency Changes | False |
| MPLS LDP Sync Default | True |
| Advertise Passive-only | True |
| SR MPLS Enabled | True |
| SPF Interval | 250 seconds |
| SPF Interval Wait Time| 10 milliseconds |
| SPF Interval Hold Time| 20 milliseconds |
| Graceful-restart Enabled | True |
| Graceful-restart t2 Level-1 | 10 |
| Graceful-restart t2 Level-2 | 20 |
| Graceful-restart Restart-hold-time | 10 |

#### ISIS Route Timers

| Settings | Value |
| -------- | ----- |
| Local Convergence Delay | 10000 milliseconds |
| LSP Generation Maximum Interval | 30 seconds |
| LSP Generation Initial Wait-time | 40 milliseconds |

#### ISIS Route Redistribution

| Route Type | Route-Map | Include Leaked |
| ---------- | --------- | -------------- |
| connected | - | - |
| isis instance | RM-REDIS-ISIS-INSTANCE | - |
| ospf internal | - | - |
| ospf external | RM-OSPF-EXTERNAL-TO-ISIS | - |
| ospf nssa-external | RM-OSPF-NSSA_EXT-TO-ISIS | True |
| ospf | - | - |
| ospfv3 external | - | - |
| ospfv3 | - | - |
| static | RM-STATIC-TO-ISIS | True |

#### ISIS Interfaces Summary

| Interface | ISIS Instance | ISIS Metric | Interface Mode |
| --------- | ------------- | ----------- | -------------- |
| Ethernet1 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet2 | EVPN_UNDERLAY | 50 | point-to-point |
| Vlan4093 | EVPN_UNDERLAY | 50 | point-to-point |
| Loopback0 | EVPN_UNDERLAY | - | passive |
| Loopback1 | EVPN_UNDERLAY | - | passive |

#### Prefix Segments

| Prefix Segment | Index |
| -------------- | ----- |
| 155.2.1.1/32 | 211 |
| 2001:cafe:155::/64 | 6211 |

#### ISIS IPv4 Address Family Summary

| Settings | Value |
| -------- | ----- |
| IPv4 Address-family Enabled | True |
| Maximum-paths | 4 |
| BFD All-interfaces | True |
| TI-LFA Mode | link-protection |
| TI-LFA Level | level-2 |
| TI-LFA SRLG Enabled | True |
| TI-LFA SRLG Strict Mode | True |

#### Tunnel Source

| Source Protocol | RCF |
| --------------- | --- |
| BGP Labeled-Unicast | lu_2_sr_pfx() |

#### ISIS IPv6 Address Family Summary

| Settings | Value |
| -------- | ----- |
| IPv6 Address-family Enabled | True |
| TI-LFA Mode | node-protection |
| TI-LFA Level | level-1 |
| TI-LFA SRLG Enabled | True |
| TI-LFA SRLG Strict Mode | True |

#### Router ISIS Device Configuration

```eos
!
router isis EVPN_UNDERLAY
   no log-adjacency-changes
   mpls ldp sync default
   redistribute connected
   redistribute isis instance route-map RM-REDIS-ISIS-INSTANCE
   redistribute ospf match internal
   redistribute ospf match external route-map RM-OSPF-EXTERNAL-TO-ISIS
   redistribute ospf include leaked match nssa-external route-map RM-OSPF-NSSA_EXT-TO-ISIS
   redistribute ospfv3 match external
   redistribute static include leaked route-map RM-STATIC-TO-ISIS
   timers local-convergence-delay protected-prefixes
   set-overload-bit
   advertise passive-only
   spf-interval 250 seconds 10 milliseconds 20 milliseconds
   timers lsp generation 30 40
   authentication mode shared-secret profile test1 algorithm md5 level-1
   authentication mode sha key-id 2 level-2
   graceful-restart
   graceful-restart t2 level-1 10
   graceful-restart t2 level-2 20
   graceful-restart restart-hold-time 10
   authentication key-id 2 algorithm sha-512 key 0 password
   authentication key-id 3 algorithm sha-512 rfc-5310 key 0 password1
   authentication key-id 1 algorithm sha-1 key 0 password level-1
   authentication key-id 4 algorithm sha-1 rfc-5310 key 0 password level-1
   authentication key-id 1 algorithm sha-1 key 0 password level-2
   authentication key-id 5 algorithm sha-1 rfc-5310 key 0 password level-2
   authentication key 0 password level-1
   authentication key 0 password level-2
   !
   address-family ipv4 unicast
      maximum-paths 4
      tunnel source-protocol bgp ipv4 labeled-unicast rcf lu_2_sr_pfx()
      bfd all-interfaces
      fast-reroute ti-lfa mode link-protection level-2
      fast-reroute ti-lfa srlg strict
   !
   address-family ipv6 unicast
      fast-reroute ti-lfa mode node-protection level-1
      fast-reroute ti-lfa srlg strict
   !
   segment-routing mpls
      no shutdown
      prefix-segment 155.2.1.1/32 index 211
      prefix-segment 2001:cafe:155::/64 index 6211
```
