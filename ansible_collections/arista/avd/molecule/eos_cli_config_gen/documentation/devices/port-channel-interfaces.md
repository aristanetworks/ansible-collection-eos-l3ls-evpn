# port-channel-interfaces

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitoring](#monitoring)
  - [SFlow](#sflow)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces-1)
- [BFD](#bfd)
  - [BFD Interfaces](#bfd-interfaces)
- [MPLS](#mpls)
  - [MPLS Interfaces](#mpls-interfaces)
- [Multicast](#multicast)
  - [PIM Sparse Mode](#pim-sparse-mode)
- [Quality Of Service](#quality-of-service)
  - [QOS Interfaces](#qos-interfaces)

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

## Monitoring

### SFlow

#### SFlow Summary

sFlow is disabled.

#### SFlow Interfaces

| Interface | Ingress Enabled | Egress Enabled |
| --------- | --------------- | -------------- |
| Port-Channel117 | True | True |
| Port-Channel118 | True | True (unmodified) |
| Port-Channel119 | False | False |
| Port-Channel120 | False | False (unmodified) |

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet3 | MLAG_PEER_DC1-LEAF1B_Ethernet3 | *trunk | *2-4094 | *- | *LEAF_PEER_L3, MLAG | 3 |
| Ethernet4 | MLAG_PEER_DC1-LEAF1B_Ethernet4 | *trunk | *2-4094 | *- | *LEAF_PEER_L3, MLAG | 3 |
| Ethernet5 | DC1-AGG01_Ethernet1 | *trunk | *110,201 | *- | *- | 5 |
| Ethernet10/1 | LAG Member | *access | *110 | *- | *- | 101 |
| Ethernet10/2 | LAG Member | *trunk | *110-112 | *- | *- | 102 |
| Ethernet10/3 | LAG Member | *trunk | *110-112 | *- | *- | 103 |
| Ethernet10/4 | LAG Member LACP fallback | *trunk | *112 | *- | *- | 104 |
| Ethernet11/2 | LAG Member LACP fallback LLDP ZTP VLAN | *trunk | *112 | *- | *- | 112 |
| Ethernet15 | DC1-AGG03_Ethernet1 | *trunk | *110,201 | *- | *- | 15 |
| Ethernet16 | DC1-AGG04_Ethernet1 | *trunk | *110,201 | *10 | *- | 16 |
| Ethernet18 | LAG Member | *access | *110 | *- | *- | 109 |
| Ethernet50 | SRV-POD03_Eth1 | *trunk | *110,201 | *- | *- | 5 |

*Inherited from Port-Channel Interface

##### Transceiver Settings

| Interface | Transceiver Frequency | Media Override |
| --------- | --------------------- | -------------- |
| Ethernet5 | - | 100gbase-ar4 |

##### Phone Interfaces

| Interface | Mode | Native VLAN | Phone VLAN | Phone VLAN Mode |
| --------- | ---- | ----------- | ---------- | --------------- |
| Port-Channel12 | trunk phone | 100 | 70 | untagged |
| Port-Channel100 | dot1q-tunnel | 5 | 110 | tagged |

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet17 | LAG Member | 17 | *192.0.2.3/31 | **default | **- | **- | **- | **- |

*Inherited from Port-Channel Interface

##### ISIS

| Interface | Channel Group | ISIS Instance | ISIS BFD | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | Authentication Mode |
| --------- | ------------- | ------------- | -------- | ----------- | ---- | ----------------- | ------------- | ------------------- |
| Ethernet10/10 | 110 | *ISIS_TEST | True | *99 | *point-to-point | *level-2 | *True | *text |

*Inherited from Port-Channel Interface

##### Error Correction Encoding Interfaces

| Interface | Enabled |
| --------- | ------- |
| Ethernet11/1 | fire-code<br>reed-solomon |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet3
   description MLAG_PEER_DC1-LEAF1B_Ethernet3
   channel-group 3 mode active
!
interface Ethernet4
   description MLAG_PEER_DC1-LEAF1B_Ethernet4
   channel-group 3 mode active
!
interface Ethernet5
   description DC1-AGG01_Ethernet1
   channel-group 5 mode active
   transceiver media override 100gbase-ar4
!
interface Ethernet8
   description MLAG_PEER_DC1-LEAF1B_Ethernet8
   channel-group 8 mode active
!
interface Ethernet10/1
   description LAG Member
   channel-group 101 mode active
!
interface Ethernet10/2
   description LAG Member
   channel-group 102 mode active
!
interface Ethernet10/3
   description LAG Member
   channel-group 103 mode active
!
interface Ethernet10/4
   description LAG Member LACP fallback
   switchport trunk allowed vlan 100
   switchport mode trunk
   switchport
   channel-group 104 mode active
   spanning-tree portfast
!
interface Ethernet10/10
   description isis_port_channel_member
   channel-group 110 mode active
!
interface Ethernet11/1
   description LAG Member with error_correction
   error-correction encoding fire-code
   error-correction encoding reed-solomon
   channel-group 111 mode active
!
interface Ethernet11/2
   description LAG Member LACP fallback LLDP ZTP VLAN
   switchport trunk allowed vlan 112
   switchport mode trunk
   switchport
   channel-group 112 mode active
   lldp tlv transmit ztp vlan 112
   spanning-tree portfast
!
interface Ethernet15
   description DC1-AGG03_Ethernet1
   channel-group 15 mode active
   lacp timer fast
   lacp timer multiplier 30
!
interface Ethernet16
   description DC1-AGG04_Ethernet1
   channel-group 16 mode active
   lacp timer normal
!
interface Ethernet17
   description LAG Member
   channel-group 17 mode active
!
interface Ethernet18
   description LAG Member
   channel-group 109 mode active
!
interface Ethernet50
   description SRV-POD03_Eth1
   channel-group 5 mode active
   no lldp transmit
   no lldp receive
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel3 | MLAG_PEER_DC1-LEAF1B_Po3 | trunk | 2-4094 | - | LEAF_PEER_L3, MLAG | - | - | - | - |
| Port-Channel5 | DC1_L2LEAF1_Po1 | trunk | 110,201 | - | - | - | - | 5 | - |
| Port-Channel10 | SRV01_bond0 | trunk | 2-3000 | - | - | - | - | - | 0000:0000:0404:0404:0303 |
| Port-Channel12 | interface_in_mode_access_with_voice | trunk phone | - | 100 | - | - | - | - | - |
| Port-Channel13 | EVPN-Vxlan single-active redundancy | - | - | - | - | - | - | - | 0000:0000:0000:0102:0304 |
| Port-Channel14 | EVPN-MPLS multihoming | - | - | - | - | - | - | - | 0000:0000:0000:0102:0305 |
| Port-Channel15 | DC1_L2LEAF3_Po1 | trunk | 110,201 | - | - | - | - | 15 | - |
| Port-Channel16 | DC1_L2LEAF4_Po1 | trunk | 110,201 | 10 | - | - | - | 16 | - |
| Port-Channel20 | Po_in_mode_access_accepting_tagged_LACP_frames | access | 200 | - | - | - | - | - | - |
| Port-Channel50 | SRV-POD03_PortChanne1 | trunk | 1-4000 | - | - | - | - | - | 0000:0000:0303:0202:0101 |
| Port-Channel51 | ipv6_prefix | trunk | 1-500 | - | - | - | - | - | - |
| Port-Channel100 | - | dot1q-tunnel | 10-11,200 | tag | g1, g2 | - | - | - | - |
| Port-Channel101 | PVLAN Promiscuous Access - only one secondary | access | 110 | - | - | - | - | - | - |
| Port-Channel102 | PVLAN Promiscuous Trunk - vlan translation out | trunk | 110-112 | - | - | - | - | - | - |
| Port-Channel103 | PVLAN Secondary Trunk | trunk | 110-112 | - | - | - | - | - | - |
| Port-Channel104 | LACP fallback individual | trunk | 112 | - | - | 300 | individual | - | - |
| Port-Channel105 | bpdu disabled | - | - | - | - | - | - | - | - |
| Port-Channel106 | bpdu enabled | - | - | - | - | - | - | - | - |
| Port-Channel107 | bpdu true | - | - | - | - | - | - | - | - |
| Port-Channel108 | bpdu false | - | - | - | - | - | - | - | - |
| Port-Channel109 | Molecule ACLs | access | 110 | - | - | - | - | - | - |
| Port-Channel112 | LACP fallback individual | trunk | 112 | - | - | 5 | individual | - | - |
| Port-Channel115 | native-vlan-tag-precedence | trunk | - | tag | - | - | - | - | - |
| Port-Channel121 | access_port_with_no_vlans | access | - | - | - | - | - | - | - |
| Port-Channel122 | trunk_port_with_no_vlans | trunk | - | - | - | - | - | - | - |
| Port-Channel130 | IP NAT Testing | - | - | - | - | - | - | - | - |
| Port-Channel131 | dot1q-tunnel mode | dot1q-tunnel | 115 | - | - | - | - | - | - |

##### Encapsulation Dot1q

| Interface | Description | Vlan ID | Dot1q VLAN Tag | Dot1q Inner VLAN Tag |
| --------- | ----------- | ------- | -------------- | -------------------- |
| Port-Channel8.101 | to Dev02 Port-Channel8.101 - VRF-C1 | - | 101 | - |
| Port-Channel100.101 | IFL for TENANT01 | - | 101 | - |
| Port-Channel100.102 | IFL for TENANT02 | - | 102 | 110 |

##### Flexible Encapsulation Interfaces

| Interface | Description | Vlan ID | Client Encapsulation | Client Inner Encapsulation | Client VLAN | Client Outer VLAN Tag | Client Inner VLAN Tag | Network Encapsulation | Network Inner Encapsulation | Network VLAN | Network Outer VLAN Tag | Network Inner VLAN Tag |
| --------- | ----------- | ------- | --------------- | --------------------- | ----------- | --------------------- | --------------------- | ---------------- | ---------------------- | ------------ | ---------------------- | ---------------------- |
| Port-Channel111.1 | TENANT_A pseudowire 1 interface | - | unmatched | - | - | - | - | - | - | - | - | - |
| Port-Channel111.100 | TENANT_A pseudowire 2 interface | - | dot1q | - | 100 | - | - | client | - | - | - | - |
| Port-Channel111.200 | TENANT_A pseudowire 3 interface | - | dot1q | - | 200 | - | - | - | - | - | - | - |
| Port-Channel111.300 | TENANT_A pseudowire 4 interface | - | dot1q | - | 300 | - | - | dot1q | - | 400 | - | - |
| Port-Channel111.400 | TENANT_A pseudowire 3 interface | - | dot1q | - | - | 400 | 20 | dot1q | - | - | 401 | 21 |
| Port-Channel111.1000 | L2 Subinterface | 1000 | dot1q | - | 100 | - | - | client | - | - | - | - |
| Port-Channel131.1 | Test_encapsulation_vlan1 | - | dot1q | dot1q | - | 23 | 45 | dot1ad | dot1ad | - | 32 | 54 |
| Port-Channel131.2 | Test_encapsulation_vlan2 | - | dot1q | - | 10 | - | - | dot1q | - | - | 32 | 54 |
| Port-Channel131.3 | Test_encapsulation_vlan3 | - | dot1ad | - | 12 | - | - | dot1q | - | 25 | - | - |
| Port-Channel131.4 | Test_encapsulation_vlan4 | - | dot1ad | dot1q | - | 35 | 60 | dot1q | dot1ad | - | 53 | 6 |
| Port-Channel131.5 | Test_encapsulation_vlan5 | - | dot1ad | - | - | 35 | 60 | dot1ad | - | - | 52 | 62 |
| Port-Channel131.6 | Test_encapsulation_vlan6 | - | dot1ad | - | - | 35 | 60 | client | - | - | - | - |
| Port-Channel131.7 | Test_encapsulation_vlan7 | - | untagged | - | - | - | - | dot1ad | - | - | 35 | 60 |
| Port-Channel131.8 | Test_encapsulation_vlan8 | - | untagged | - | - | - | - | dot1q | - | - | 35 | 60 |
| Port-Channel131.9 | Test_encapsulation_vlan9 | - | untagged | - | - | - | - | untagged | - | - | - | - |
| Port-Channel131.10 | Test_encapsulation_vlan9 | - | dot1q | - | - | 14 | 11 | client inner | - | - | - | - |

##### Private VLAN

| Interface | PVLAN Mapping | Secondary Trunk |
| --------- | ------------- | ----------------|
| Port-Channel15 | - | False |
| Port-Channel100 | 20-30 | True |
| Port-Channel101 | 111 | - |
| Port-Channel103 | - | True |

##### VLAN Translations

| Interface |  Direction | From VLAN ID(s) | To VLAN ID | From Inner VLAN ID | To Inner VLAN ID | Network | Dot1q-tunnel |
| --------- |  --------- | --------------- | ---------- | ------------------ | ---------------- | ------- | ------------ |
| Port-Channel16 | out | 23 | 22 | - | - | - | True |
| Port-Channel100 | both | 12 | 20 | - | - | - | - |
| Port-Channel100 | both | 23 | 42 | 74 | - | False | - |
| Port-Channel100 | both | 24 | 46 | 78 | - | True | - |
| Port-Channel100 | both | 43 | 30 | - | - | - | True |
| Port-Channel100 | in | 23 | 45 | - | - | - | True |
| Port-Channel100 | in | 34 | 23 | - | - | - | - |
| Port-Channel100 | in | 37 | 49 | - | 56 | - | - |
| Port-Channel100 | out | 10 | 45 | - | 34 | - | - |
| Port-Channel100 | out | 34 | 50 | - | - | - | - |
| Port-Channel100 | out | 45 | all | - | - | - | True |
| Port-Channel100 | out | 55 | - | - | - | - | - |
| Port-Channel102 | out | 111-112 | 110 | - | - | - | - |

##### EVPN Multihoming

####### EVPN Multihoming Summary

| Interface | Ethernet Segment Identifier | Multihoming Redundancy Mode | Route Target |
| --------- | --------------------------- | --------------------------- | ------------ |
| Port-Channel10 | 0000:0000:0404:0404:0303 | all-active | 04:04:03:03:02:02 |
| Port-Channel13 | 0000:0000:0000:0102:0304 | single-active | 00:00:01:02:03:04 |
| Port-Channel14 | 0000:0000:0000:0102:0305 | all-active | 00:00:01:02:03:05 |
| Port-Channel50 | 0000:0000:0303:0202:0101 | all-active | 03:03:02:02:01:01 |
| Port-Channel111.1000 | 0000:0000:0303:0202:0101 | all-active | 03:03:02:02:01:01 |

####### Designated Forwarder Election Summary

| Interface | Algorithm | Preference Value | Dont Preempt | Hold time | Subsequent Hold Time | Candidate Reachability Required |
| --------- | --------- | ---------------- | ------------ | --------- | -------------------- | ------------------------------- |
| Port-Channel13 | preference | 100 | True | 10 | - | True |

####### EVPN-MPLS summary

| Interface | Shared Index | Tunnel Flood Filter Time |
| --------- | ------------ | ------------------------ |
| Port-Channel14 | 100 | 100 |

##### Link Tracking Groups

| Interface | Group Name | Direction |
| --------- | ---------- | --------- |
| Port-Channel5 | EVPN_MH_ES1 | downstream |
| Port-Channel15 | EVPN_MH_ES2 | upstream |

##### IPv4

| Interface | Description | MLAG ID | IP Address | VRF | MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------- | ---------- | --- | --- | -------- | ------ | ------- |
| Port-Channel8.101 | to Dev02 Port-Channel8.101 - VRF-C1 | - | 10.1.2.3/31 | default | - | - | - | - |
| Port-Channel9 | - | - | 10.9.2.3/31 | default | - | - | - | - |
| Port-Channel17 | PBR Description | - | 192.0.2.3/31 | default | - | - | - | - |
| Port-Channel99 | MCAST | - | 192.0.2.10/31 | default | - | - | - | - |
| Port-Channel100.101 | IFL for TENANT01 | - | 10.1.1.3/31 | default | 1500 | - | - | - |
| Port-Channel100.102 | IFL for TENANT02 | - | 10.1.2.3/31 | C2 | 1500 | - | - | - |
| Port-Channel113 | interface_with_mpls_enabled | - | 172.31.128.9/31 | default | - | - | - | - |
| Port-Channel114 | interface_with_mpls_disabled | - | 172.31.128.10/31 | default | - | - | - | - |

##### IP NAT: Source Static

| Interface | Direction | Original IP | Original Port | Access List | Translated IP | Translated Port | Protocol | Group | Priority | Comment |
| --------- | --------- | ----------- | ------------- | ----------- | ------------- | --------------- | -------- | ----- | -------- | ------- |
| Port-Channel130 | - | 3.0.0.1 | - | - | 4.0.0.1 | - | - | - | 0 | - |

##### IP NAT: Source Dynamic

| Interface | Access List | NAT Type | Pool Name | Priority | Comment |
| --------- | ----------- | -------- | --------- | -------- | ------- |
| Port-Channel130 | ACL2 | pool | POOL2 | 0 | - |

##### IP NAT: Destination Static

| Interface | Direction | Original IP | Original Port | Access List | Translated IP | Translated Port | Protocol | Group | Priority | Comment |
| --------- | --------- | ----------- | ------------- | ----------- | ------------- | --------------- | -------- | ----- | -------- | ------- |
| Port-Channel130 | - | 1.0.0.1 | - | - | 2.0.0.1 | - | - | - | 0 | - |

##### IP NAT: Destination Dynamic

| Interface | Access List | Pool Name | Priority | Comment |
| --------- | ----------- | --------- | -------- | ------- |
| Port-Channel130 | ACL1 | POOL1 | 0 | - |

##### ISIS

| Interface | ISIS Instance | ISIS BFD | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | Authentication Mode |
| --------- | ------------- | -------- | ----------- | ---- | ----------------- | ------------- | ------------------- |
| Port-Channel110 | ISIS_TEST | True | 99 | point-to-point | level-2 | True | text |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel3
   description MLAG_PEER_DC1-LEAF1B_Po3
   switchport trunk allowed vlan 2-4094
   switchport mode trunk
   switchport trunk group LEAF_PEER_L3
   switchport trunk group MLAG
   switchport
   no snmp trap link-change
   shape rate 200000 kbps
!
interface Port-Channel5
   description DC1_L2LEAF1_Po1
   bgp session tracker ST2
   switchport trunk allowed vlan 110,201
   switchport mode trunk
   switchport
   ip verify unicast source reachable-via rx
   ip igmp host-proxy
   ip igmp host-proxy 239.0.0.1
   ip igmp host-proxy 239.0.0.2 exclude 10.0.2.1
   ip igmp host-proxy 239.0.0.3 include 10.0.3.1
   ip igmp host-proxy 239.0.0.4 include 10.0.4.3
   ip igmp host-proxy 239.0.0.4 include 10.0.4.4
   ip igmp host-proxy 239.0.0.4 exclude 10.0.4.1
   ip igmp host-proxy 239.0.0.4 exclude 10.0.4.2
   ip igmp host-proxy access-list ACL1
   ip igmp host-proxy access-list ACL2
   ip igmp host-proxy report-interval 2
   ip igmp host-proxy version 2
   l2 mtu 8000
   l2 mru 8000
   mlag 5
   storm-control broadcast level 1
   storm-control multicast level 1
   storm-control unknown-unicast level 1
   link tracking group EVPN_MH_ES1 downstream
   comment
   Comment created from eos_cli under port_channel_interfaces.Port-Channel5
   EOF

!
interface Port-Channel8
   description to Dev02 Port-channel 8
   no switchport
   switchport port-security violation protect
!
interface Port-Channel8.101
   description to Dev02 Port-Channel8.101 - VRF-C1
   encapsulation dot1q vlan 101
   ip address 10.1.2.3/31
!
interface Port-Channel9
   no switchport
   ip address 10.9.2.3/31
   bfd interval 500 min-rx 500 multiplier 5
   bfd echo
   bfd neighbor 10.1.2.4
   bfd per-link rfc-7130
   spanning-tree guard root
!
interface Port-Channel10
   description SRV01_bond0
   switchport trunk allowed vlan 2-3000
   switchport mode trunk
   switchport
   !
   evpn ethernet-segment
      identifier 0000:0000:0404:0404:0303
      route-target import 04:04:03:03:02:02
   shape rate 50 percent
!
interface Port-Channel12
   description interface_in_mode_access_with_voice
   switchport trunk native vlan 100
   switchport phone vlan 70
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
!
interface Port-Channel13
   description EVPN-Vxlan single-active redundancy
   switchport
   !
   evpn ethernet-segment
      identifier 0000:0000:0000:0102:0304
      redundancy single-active
      designated-forwarder election algorithm preference 100 dont-preempt
      designated-forwarder election hold-time 10
      designated-forwarder election candidate reachability required
      route-target import 00:00:01:02:03:04
!
interface Port-Channel14
   description EVPN-MPLS multihoming
   switchport
   !
   evpn ethernet-segment
      identifier 0000:0000:0000:0102:0305
      mpls tunnel flood filter time 100
      mpls shared index 100
      route-target import 00:00:01:02:03:05
!
interface Port-Channel15
   description DC1_L2LEAF3_Po1
   switchport trunk allowed vlan 110,201
   switchport mode trunk
   switchport
   mlag 15
   spanning-tree guard loop
   link tracking group EVPN_MH_ES2 upstream
!
interface Port-Channel16
   description DC1_L2LEAF4_Po1
   switchport trunk native vlan 10
   switchport dot1q vlan tag disallowed
   switchport trunk allowed vlan 110,201
   switchport mode trunk
   switchport
   switchport vlan translation out 23 dot1q-tunnel 22
   snmp trap link-change
   mlag 16
   switchport port-security violation protect log
   switchport port-security mac-address maximum 100
   spanning-tree guard none
   switchport backup-link Port-Channel100.102 prefer vlan 20
!
interface Port-Channel17
   description PBR Description
   no switchport
   ip address 192.0.2.3/31
   service-policy type pbr input MyPolicy
!
interface Port-Channel20
   description Po_in_mode_access_accepting_tagged_LACP_frames
   switchport access vlan 200
   switchport mode access
   switchport
   l2-protocol encapsulation dot1q vlan 200
!
interface Port-Channel50
   description SRV-POD03_PortChanne1
   switchport trunk allowed vlan 1-4000
   switchport mode trunk
   switchport
   !
   evpn ethernet-segment
      identifier 0000:0000:0303:0202:0101
      route-target import 03:03:02:02:01:01
   lacp system-id 0303.0202.0101
!
interface Port-Channel51
   description ipv6_prefix
   switchport trunk allowed vlan 1-500
   switchport mode trunk
   switchport
   ipv6 nd prefix a1::/64 infinite infinite no-autoconfig
   switchport port-security
   no switchport port-security mac-address maximum disabled
   switchport port-security vlan 1 mac-address maximum 3
   switchport port-security vlan 2 mac-address maximum 3
   switchport port-security vlan 3 mac-address maximum 3
   switchport port-security vlan default mac-address maximum 2
!
interface Port-Channel99
   description MCAST
   no switchport
   ip address 192.0.2.10/31
   pim ipv4 sparse-mode
   pim ipv4 bidirectional
   pim ipv4 hello interval 15
   pim ipv4 hello count 4.5
   pim ipv4 dr-priority 200
   pim ipv4 bfd
!
interface Port-Channel100
   logging event link-status
   switchport access vlan 200
   switchport trunk native vlan tag
   switchport phone vlan 110
   switchport phone trunk tagged
   switchport vlan translation in required
   switchport dot1q vlan tag required
   switchport trunk allowed vlan 10-11
   switchport mode dot1q-tunnel
   switchport dot1q ethertype 1536
   switchport vlan forwarding accept all
   switchport trunk group g1
   switchport trunk group g2
   no switchport
   switchport source-interface tx multicast
   switchport vlan translation 12 20
   switchport vlan translation 23 inner 74 42
   switchport vlan translation 24 inner 78 network 46
   switchport vlan translation 43 dot1q-tunnel 30
   switchport vlan translation in 34 23
   switchport vlan translation in 37 inner 56 49
   switchport vlan translation in 23 dot1q-tunnel 45
   switchport vlan translation out 34 50
   switchport vlan translation out 10 45 inner 34
   switchport vlan translation out 45 dot1q-tunnel all
   switchport trunk private-vlan secondary
   switchport pvlan mapping 20-30
   switchport port-security
   switchport port-security mac-address maximum disabled
   switchport backup-link Port-channel51
   switchport backup preemption-delay 35
   switchport backup mac-move-burst 20
   switchport backup mac-move-burst-interval 30
   switchport backup initial-mac-move-delay 10
   switchport backup dest-macaddr 01:00:00:00:00:00
!
interface Port-Channel100.101
   description IFL for TENANT01
   mtu 1500
   logging event link-status
   encapsulation dot1q vlan 101
   ip address 10.1.1.3/31
!
interface Port-Channel100.102
   description IFL for TENANT02
   mtu 1500
   no logging event link-status
   encapsulation dot1q vlan 102 inner 110
   vrf C2
   ip address 10.1.2.3/31
   logging event storm-control discards
!
interface Port-Channel101
   description PVLAN Promiscuous Access - only one secondary
   switchport access vlan 110
   switchport mode access
   switchport
   switchport pvlan mapping 111
   no qos trust
!
interface Port-Channel102
   description PVLAN Promiscuous Trunk - vlan translation out
   switchport vlan translation out required
   switchport trunk allowed vlan 110-112
   switchport mode trunk
   switchport
   switchport vlan translation out 111-112 110
!
interface Port-Channel103
   description PVLAN Secondary Trunk
   switchport trunk allowed vlan 110-112
   switchport mode trunk
   switchport
   switchport trunk private-vlan secondary
!
interface Port-Channel104
   description LACP fallback individual
   switchport trunk allowed vlan 112
   switchport mode trunk
   switchport
   port-channel lacp fallback individual
   port-channel lacp fallback timeout 300
!
interface Port-Channel105
   description bpdu disabled
   switchport
   spanning-tree bpduguard disable
   spanning-tree bpdufilter disable
!
interface Port-Channel106
   description bpdu enabled
   switchport
   spanning-tree bpduguard enable
   spanning-tree bpdufilter enable
!
interface Port-Channel107
   description bpdu true
   switchport
   spanning-tree bpduguard enable
   spanning-tree bpdufilter enable
!
interface Port-Channel108
   description bpdu false
   switchport
!
interface Port-Channel109
   description Molecule ACLs
   switchport access vlan 110
   switchport mode access
   switchport
   ip access-group IPV4_ACL_IN in
   ip access-group IPV4_ACL_OUT out
   ipv6 access-group IPV6_ACL_IN in
   ipv6 access-group IPV6_ACL_OUT out
   mac access-group MAC_ACL_IN in
   mac access-group MAC_ACL_OUT out
!
interface Port-Channel110
   description isis_interface_knobs
   no switchport
   isis enable ISIS_TEST
   isis bfd
   isis circuit-type level-2
   isis metric 99
   isis hello padding
   isis network point-to-point
   isis authentication mode text
   isis authentication key 7 <removed>
!
interface Port-Channel111
   description Flexencap Port-Channel
   no switchport
!
interface Port-Channel111.1
   description TENANT_A pseudowire 1 interface
   !
   encapsulation vlan
      client unmatched
!
interface Port-Channel111.100
   description TENANT_A pseudowire 2 interface
   !
   encapsulation vlan
      client dot1q 100 network client
!
interface Port-Channel111.200
   description TENANT_A pseudowire 3 interface
   !
   encapsulation vlan
      client dot1q 200
!
interface Port-Channel111.300
   description TENANT_A pseudowire 4 interface
   !
   encapsulation vlan
      client dot1q 300 network dot1q 400
!
interface Port-Channel111.400
   description TENANT_A pseudowire 3 interface
   !
   encapsulation vlan
      client dot1q outer 400 inner 20 network dot1q outer 401 inner 21
!
interface Port-Channel111.1000
   description L2 Subinterface
   vlan id 1000
   !
   encapsulation vlan
      client dot1q 100 network client
   !
   evpn ethernet-segment
      identifier 0000:0000:0303:0202:0101
      route-target import 03:03:02:02:01:01
   lacp system-id 0303.0202.0101
!
interface Port-Channel112
   description LACP fallback individual
   switchport trunk allowed vlan 112
   switchport mode trunk
   switchport
   port-channel lacp fallback individual
   port-channel lacp fallback timeout 5
!
interface Port-Channel113
   description interface_with_mpls_enabled
   no switchport
   ip address 172.31.128.9/31
   mpls ldp igp sync
   mpls ldp interface
   mpls ip
!
interface Port-Channel114
   description interface_with_mpls_disabled
   no switchport
   ip address 172.31.128.10/31
   no mpls ldp interface
   no mpls ip
!
interface Port-Channel115
   description native-vlan-tag-precedence
   switchport trunk native vlan tag
   switchport mode trunk
   switchport
!
interface Port-Channel117
   description interface_with_sflow_ingress_egress_enabled
   no switchport
   sflow enable
   sflow egress enable
!
interface Port-Channel118
   description interface_with_sflow_ingress_egress_unmodified_enabled
   no switchport
   sflow enable
   sflow egress unmodified enable
!
interface Port-Channel119
   description interface_with_sflow_ingress_egress_disabled
   no switchport
   no sflow enable
   no sflow egress enable
!
interface Port-Channel120
   description interface_with_sflow_ingress_egress_unmodified_disabled
   no switchport
   no sflow enable
   no sflow egress unmodified enable
!
interface Port-Channel121
   description access_port_with_no_vlans
   switchport mode access
   switchport
!
interface Port-Channel122
   description trunk_port_with_no_vlans
   switchport mode trunk
   switchport
!
interface Port-Channel130
   description IP NAT Testing
   switchport
   ip nat destination static 1.0.0.1 2.0.0.1
   ip nat source static 3.0.0.1 4.0.0.1
   ip nat destination dynamic access-list ACL1 pool POOL1
   ip nat source dynamic access-list ACL2 pool POOL2
!
interface Port-Channel131
   description dot1q-tunnel mode
   switchport access vlan 115
   switchport mode dot1q-tunnel
   switchport
!
interface Port-Channel131.1
   description Test_encapsulation_vlan1
   !
   encapsulation vlan
      client dot1q outer 23 inner dot1q 45 network dot1ad outer 32 inner dot1ad 54
!
interface Port-Channel131.2
   description Test_encapsulation_vlan2
   !
   encapsulation vlan
      client dot1q 10 network dot1q outer 32 inner 54
!
interface Port-Channel131.3
   description Test_encapsulation_vlan3
   !
   encapsulation vlan
      client dot1ad 12 network dot1q 25
!
interface Port-Channel131.4
   description Test_encapsulation_vlan4
   !
   encapsulation vlan
      client dot1ad outer 35 inner dot1q 60 network dot1q outer 53 inner dot1ad 6
!
interface Port-Channel131.5
   description Test_encapsulation_vlan5
   !
   encapsulation vlan
      client dot1ad outer 35 inner 60 network dot1ad outer 52 inner 62
!
interface Port-Channel131.6
   description Test_encapsulation_vlan6
   !
   encapsulation vlan
      client dot1ad outer 35 inner 60 network client
!
interface Port-Channel131.7
   description Test_encapsulation_vlan7
   !
   encapsulation vlan
      client untagged network dot1ad outer 35 inner 60
!
interface Port-Channel131.8
   description Test_encapsulation_vlan8
   !
   encapsulation vlan
      client untagged network dot1q outer 35 inner 60
!
interface Port-Channel131.9
   description Test_encapsulation_vlan9
   !
   encapsulation vlan
      client untagged network untagged
!
interface Port-Channel131.10
   description Test_encapsulation_vlan9
   !
   encapsulation vlan
      client dot1q outer 14 inner 11 network client inner
!
interface Port-Channel132
   profile test-interface-profile
   description Test_port-channel_interface-profile
```

## BFD

### BFD Interfaces

| Interface | Interval | Minimum RX | Multiplier | Echo |
| --------- | -------- | ---------- | ---------- | ---- |
| Port-Channel9 | 500 | 500 | 5 | True |

## MPLS

### MPLS Interfaces

| Interface | MPLS IP Enabled | LDP Enabled | IGP Sync |
| --------- | --------------- | ----------- | -------- |
| Port-Channel113 | True | True | True |
| Port-Channel114 | False | False | - |

## Multicast

### PIM Sparse Mode

#### PIM Sparse Mode Enabled Interfaces

| Interface Name | VRF Name | IP Version | Border Router | DR Priority | Local Interface |
| -------------- | -------- | ---------- | ------------- | ----------- | --------------- |
| Port-Channel99 | - | IPv4 | - | 200 | - |

## Quality Of Service

### QOS Interfaces

| Interface | Trust | Default DSCP | Default COS | Shape rate |
| --------- | ----- | ------------ | ----------- | ---------- |
| Port-Channel3 | - | - | - | 200000 kbps |
| Port-Channel10 | - | - | - | 50 percent |
| Port-Channel101 | disabled | - | - | - |
