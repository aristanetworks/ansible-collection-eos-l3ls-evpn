# ethernet-interfaces

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [DHCP Server](#dhcp-server)
  - [DHCP Server Interfaces](#dhcp-server-interfaces)
- [Monitoring](#monitoring)
  - [SFlow](#sflow)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces-1)
- [BFD](#bfd)
  - [BFD Interfaces](#bfd-interfaces)
- [MPLS](#mpls)
  - [MPLS Interfaces](#mpls-interfaces)
- [Multicast](#multicast)
  - [PIM Sparse Mode](#pim-sparse-mode)
- [802.1X Port Security](#8021x-port-security)
  - [802.1X Summary](#8021x-summary)
- [Power Over Ethernet (PoE)](#power-over-ethernet-poe)
  - [PoE Summary](#poe-summary)
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

## DHCP Server

### DHCP Server Interfaces

| Interface name | DHCP IPv4 | DHCP IPv6 |
| -------------- | --------- | --------- |
| Ethernet64 | True | True |

## Monitoring

### SFlow

#### SFlow Summary

sFlow is disabled.

#### SFlow Interfaces

| Interface | Ingress Enabled | Egress Enabled |
| --------- | --------------- | -------------- |
| Ethernet50 | True | - |
| Ethernet51 | - | True |
| Ethernet52 | True | True (unmodified) |
| Ethernet53 | False | False |
| Ethernet54 | False | False (unmodified) |

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet1 | P2P_LINK_TO_DC1-SPINE1_Ethernet1 | dot1q-tunnel | 110-111,200,210-211 | tag | g1, g2 | - |
| Ethernet2 | SRV-POD02_Eth1 | trunk | 110-111,210-211 | - | - | - |
| Ethernet3 | P2P_LINK_TO_DC1-SPINE2_Ethernet2 | trunk | - | 5 | - | - |
| Ethernet5 | Molecule Routing | - | 220 | - | - | - |
| Ethernet6 | SRV-POD02_Eth1 | trunk | 110-111,210-211 | - | - | - |
| Ethernet7 | Molecule L2 | - | - | - | - | - |
| Ethernet11 | interface_in_mode_access_accepting_tagged_LACP | access | 200 | - | - | - |
| Ethernet12 | interface_with_dot1q_tunnel | dot1q-tunnel | 300 | - | - | - |
| Ethernet13 | interface_in_mode_access_with_voice | trunk phone | - | 100 | - | - |
| Ethernet14 | SRV-POD02_Eth1 | trunk | 110-111,210-211 | - | - | - |
| Ethernet15 | PVLAN Promiscuous Access - only one secondary | access | 110 | - | - | - |
| Ethernet16 | PVLAN Promiscuous Trunk - vlan translation out | trunk | 110-112 | - | - | - |
| Ethernet17 | PVLAN Secondary Trunk | trunk | 110-112 | - | - | - |
| Ethernet19 | Switched port with no LLDP rx/tx | access | 110 | - | - | - |
| Ethernet21 | 200MBit/s shape | - | - | - | - | - |
| Ethernet22 | 10% shape | - | - | - | - | - |
| Ethernet23 | Error-correction encoding | - | - | - | - | - |
| Ethernet24 | Disable error-correction encoding | - | - | - | - | - |
| Ethernet25 | Molecule MAC | - | - | - | - | - |
| Ethernet27 | EVPN-Vxlan single-active redundancy | - | - | - | - | - |
| Ethernet28 | EVPN-MPLS multihoming | - | - | - | - | - |
| Ethernet29 | DOT1X Testing - auto phone true | - | - | - | - | - |
| Ethernet30 | DOT1X Testing - force-authorized phone false | - | - | - | - | - |
| Ethernet31 | DOT1X Testing - force-unauthorized - no phone | - | - | - | - | - |
| Ethernet32 | DOT1X Testing - auto reauthentication | - | - | - | - | - |
| Ethernet33 | DOT1X Testing - pae mode authenticator | - | - | - | - | - |
| Ethernet34 | DOT1X Testing - authentication_failure allow | - | - | - | - | - |
| Ethernet35 | DOT1X Testing - authentication_failure drop | - | - | - | - | - |
| Ethernet36 | DOT1X Testing - host-mode single-host | - | - | - | - | - |
| Ethernet37 | DOT1X Testing - host-mode multi-host | - | - | - | - | - |
| Ethernet38 | DOT1X Testing - host-mode multi-host authenticated | - | - | - | - | - |
| Ethernet39 | DOT1X Testing - mac_based_authentication host-mode common true | - | - | - | - | - |
| Ethernet40 | DOT1X Testing - mac_based_authentication always | - | - | - | - | - |
| Ethernet41 | DOT1X Testing - mac_based_authentication always and host-mode common | - | - | - | - | - |
| Ethernet42 | DOT1X Testing - mac_based_authentication | - | - | - | - | - |
| Ethernet43 | DOT1X Testing - timeout values | - | - | - | - | - |
| Ethernet44 | DOT1X Testing - reauthorization_request_limit | - | - | - | - | - |
| Ethernet45 | DOT1X Testing - all features | - | - | - | - | - |
| Ethernet46 | native-vlan-tag-precedence | trunk | - | tag | - | - |
| Ethernet48 | Load Interval | - | - | - | - | - |
| Ethernet50 | SFlow Interface Testing - SFlow ingress enabled | - | - | - | - | - |
| Ethernet51 | SFlow Interface Testing - SFlow egress enabled | - | - | - | - | - |
| Ethernet52 | SFlow Interface Testing - SFlow ingress and egress unmodified enabled | - | - | - | - | - |
| Ethernet53 | SFlow Interface Testing - SFlow ingress and egress disabled | - | - | - | - | - |
| Ethernet54 | SFlow Interface Testing - SFlow ingress and egress unmodified disabled | - | - | - | - | - |
| Ethernet56 | Interface with poe commands and limit in class | - | - | - | - | - |
| Ethernet57 | Interface with poe commands and limit in watts | - | - | - | - | - |
| Ethernet58 | Interface with poe disabled and no other poe keys | - | - | - | - | - |
| Ethernet60 | IP NAT Testing | - | - | - | - | - |
| Ethernet61 | interface_in_mode_access_with_voice | trunk phone | - | 100 | - | - |
| Ethernet62 | interface_in_mode_access_with_voice | trunk phone | - | 100 | - | - |
| Ethernet67 | Custom_Transceiver_Frequency | - | - | - | - | - |
| Ethernet68 | Custom_Transceiver_Frequency | - | - | - | - | - |
| Ethernet69 | IP NAT service-profile | - | - | - | - | - |

*Inherited from Port-Channel Interface

##### Encapsulation Dot1q Interfaces

| Interface | Description | Vlan ID | Dot1q VLAN Tag | Dot1q Inner VLAN Tag |
| --------- | ----------- | ------- | -------------- | -------------------- |
| Ethernet8.101 | to WAN-ISP-01 Ethernet2.101 - VRF-C1 | - | 101 | - |
| Ethernet67.1 | Test_encapsulation_dot1q | - | 4 | 34 |

##### Flexible Encapsulation Interfaces

| Interface | Description | Vlan ID | Client Encapsulation | Client Inner Encapsulation | Client VLAN | Client Outer VLAN Tag | Client Inner VLAN Tag | Network Encapsulation | Network Inner Encapsulation | Network VLAN | Network Outer VLAN Tag | Network Inner VLAN Tag |
| --------- | ----------- | ------- | --------------- | --------------------- | ----------- | --------------------- | --------------------- | ---------------- | ---------------------- |------------ | ---------------------- | ---------------------- |
| Ethernet26.1 | TENANT_A pseudowire 1 interface | - | unmatched | - | - | - | - | - | - | - | - | - |
| Ethernet26.100 | TENANT_A pseudowire 1 interface | 10 | dot1q | - | 100 | - | - | client | - | - | - | - |
| Ethernet26.200 | TENANT_A pseudowire 2 interface | - | dot1q | - | 200 | - | - | - | - | - | - | - |
| Ethernet26.300 | TENANT_A pseudowire 3 interface | - | dot1q | - | 300 | - | - | dot1q | - | 400 | - | - |
| Ethernet26.400 | TENANT_A pseudowire 3 interface | - | dot1q | - | - | 400 | 20 | dot1q | - | - | 401 | 21 |
| Ethernet26.500 | TENANT_A pseudowire 3 interface | - | dot1q | - | - | 500 | 50 | client | - | - | - | - |
| Ethernet68.1 | Test_encapsulation_vlan1 | - | dot1q | dot1q | - | 23 | 45 | dot1ad | dot1ad | - | 32 | 54 |
| Ethernet68.2 | Test_encapsulation_vlan2 | - | dot1q | - | 10 | - | - | dot1q | - | - | 32 | 54 |
| Ethernet68.3 | Test_encapsulation_vlan3 | - | dot1ad | - | 12 | - | - | dot1q | - | 25 | - | - |
| Ethernet68.4 | Test_encapsulation_vlan4 | - | dot1ad | dot1q | - | 35 | 60 | dot1q | dot1ad | - | 53 | 6 |
| Ethernet68.5 | Test_encapsulation_vlan5 | - | dot1ad | - | - | 35 | 60 | dot1ad | - | - | 52 | 62 |
| Ethernet68.6 | Test_encapsulation_vlan6 | - | dot1ad | - | - | 35 | 60 | client | - | - | - | - |
| Ethernet68.7 | Test_encapsulation_vlan7 | - | untagged | - | - | - | - | dot1ad | - | - | 35 | 60 |
| Ethernet68.8 | Test_encapsulation_vlan8 | - | untagged | - | - | - | - | dot1q | - | - | 35 | 60 |
| Ethernet68.9 | Test_encapsulation_vlan9 | - | untagged | - | - | - | - | untagged | - | - | - | - |
| Ethernet68.10 | Test_encapsulation_vlan9 | - | dot1q | - | - | 14 | 11 | client inner | - | - | - | - |

##### Private VLAN

| Interface | PVLAN Mapping | Secondary Trunk |
| --------- | ------------- | ----------------|
| Ethernet1 | 20-30 | True |
| Ethernet2 | - | False |
| Ethernet15 | 111 | - |
| Ethernet17 | - | True |

##### VLAN Translations

| Interface | Direction | From VLAN ID(s) | To VLAN ID | From Inner VLAN ID | To Inner VLAN ID | Network | Dot1q-tunnel |
| --------- | --------- | --------------- | ---------- | ------------------ | ---------------- | ------- | ------------ |
| Ethernet1 | both | 12 | 20 | - | - | - | - |
| Ethernet1 | both | 24 | 46 | 78 | - | True | - |
| Ethernet1 | both | 24 | 46 | 78 | - | False | - |
| Ethernet1 | both | 43 | 30 | - | - | - | True |
| Ethernet1 | in | 10 | 24 | - | - | - | - |
| Ethernet1 | in | 23 | 45 | - | - | - | True |
| Ethernet1 | in | 37 | 49 | 56 | - | - | - |
| Ethernet1 | out | 10 | 45 | - | 34 | - | - |
| Ethernet1 | out | 34 | 50 | - | - | - | - |
| Ethernet1 | out | 45 | all | - | - | - | True |
| Ethernet1 | out | 55 | - | - | - | - | - |
| Ethernet3 | out | 23 | 50 | - | - | - | True |
| Ethernet16 | out | 111-112 | 110 | - | - | - | - |

##### TCP MSS Clamping

| Interface | Ipv4 Segment Size | Ipv6 Segment Size | Direction |
| --------- | ----------------- | ----------------- | --------- |
| Ethernet1 | 70 | 75 | egress |
| Ethernet2 | 70 | - | ingress |
| Ethernet3 | - | 65 | - |
| Ethernet4 | 65 | - | - |

##### Transceiver Settings

| Interface | Transceiver Frequency | Media Override |
| --------- | --------------------- | -------------- |
| Ethernet7 | - | 100gbase-ar4 |
| Ethernet67 | 190050.000 | - |
| Ethernet68 | 190080.000 ghz | 100gbase-ar4 |

##### Link Tracking Groups

| Interface | Group Name | Direction |
| --------- | ---------- | --------- |
| Ethernet1 | EVPN_MH_ES1 | upstream |
| Ethernet3 | EVPN_MH_ES2 | downstream |

##### Phone Interfaces

| Interface | Mode | Native VLAN | Phone VLAN | Phone VLAN Mode |
| --------- | ---- | ----------- | ---------- | --------------- |
| Ethernet1 | dot1q-tunnel | 5 | 110 | tagged |
| Ethernet13 | trunk phone | 100 | 70 | untagged |
| Ethernet61 | trunk phone | 100 | 70 | untagged phone |
| Ethernet62 | trunk phone | 100 | 70 | tagged phone |

##### Multicast Routing

| Interface | IP Version | Static Routes Allowed | Multicast Boundaries |
| --------- | ---------- | --------------------- | -------------------- |
| Ethernet2 | IPv4 | True | ACL_MULTICAST |
| Ethernet2 | IPv6 | - | ACL_V6_MULTICAST |
| Ethernet4 | IPv4 | True | 224.0.1.0/24, 224.0.2.0/24 |
| Ethernet4 | IPv6 | - | ff00::/16, ff01::/16 |
| Ethernet9 | IPv4 | - | ACL_MULTICAST |
| Ethernet9 | IPv6 | True | - |

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_LINK_TO_DC1-SPINE1_Ethernet1 | - | 172.31.255.1/31 | default | 1500 | - | - | - |
| Ethernet2 | SRV-POD02_Eth1 | - | 10.1.255.3/24 | default | - | - | - | - |
| Ethernet3 | P2P_LINK_TO_DC1-SPINE2_Ethernet2 | - | 172.31.128.1/31 | default | 1500 | - | - | - |
| Ethernet8.101 | to WAN-ISP-01 Ethernet2.101 - VRF-C1 | - | 172.31.128.1/31 | default | - | - | - | - |
| Ethernet9 | interface_with_mpls_enabled | - | 172.31.128.9/31 | default | - | - | - | - |
| Ethernet10 | interface_with_mpls_disabled | - | 172.31.128.10/31 | default | - | - | - | - |
| Ethernet18 | PBR Description | - | 192.0.2.1/31 | default | 1500 | - | - | - |
| Ethernet47 | IP Helper | - | 172.31.255.1/31 | default | - | - | - | - |
| Ethernet63 | DHCP client interface | - | dhcp | default | - | - | - | - |
| Ethernet64 | DHCP server interface | - | 192.168.42.42/24 | default | - | - | - | - |
| Ethernet65 | Multiple VRIDs | - | 192.0.2.2/25 | default | - | False | - | - |
| Ethernet66 | Multiple VRIDs and tracking | - | 192.0.2.2/25 | default | - | False | - | - |

##### IP NAT: Source Static

| Interface | Direction | Original IP | Original Port | Access List | Translated IP | Translated Port | Protocol | Group | Priority | Comment |
| --------- | --------- | ----------- | ------------- | ----------- | ------------- | --------------- | -------- | ----- | -------- | ------- |
| Ethernet60 | - | 3.0.0.1 | - | - | 4.0.0.1 | - | - | - | 0 | - |
| Ethernet60 | - | 3.0.0.2 | 22 | - | 4.0.0.2 | - | - | - | 0 | - |
| Ethernet60 | - | 3.0.0.3 | 22 | - | 4.0.0.3 | 23 | - | - | 0 | - |
| Ethernet60 | - | 3.0.0.4 | 22 | - | 4.0.0.4 | 23 | UDP | - | 0 | - |
| Ethernet60 | - | 3.0.0.5 | 22 | - | 4.0.0.5 | 23 | TCP | 1 | 0 | - |
| Ethernet60 | - | 3.0.0.6 | 22 | - | 4.0.0.6 | 23 | TCP | 2 | 5 | Comment Test |
| Ethernet60 | - | 3.0.0.7 | - | ACL21 | 4.0.0.7 | - | - | - | 0 | - |
| Ethernet60 | ingress | 3.0.0.8 | - | - | 4.0.0.8 | - | - | - | 0 | - |

##### IP NAT: Source Dynamic

| Interface | Access List | NAT Type | Pool Name | Priority | Comment |
| --------- | ----------- | -------- | --------- | -------- | ------- |
| Ethernet60 | ACL11 | pool | POOL11 | 0 | - |
| Ethernet60 | ACL12 | pool | POOL11 | 0 | POOL11 shared with ACL11/12 |
| Ethernet60 | ACL13 | pool | POOL13 | 10 | - |
| Ethernet60 | ACL14 | pool | POOL14 | 1 | Priority low end |
| Ethernet60 | ACL15 | pool | POOL15 | 4294967295 | Priority high end |
| Ethernet60 | ACL16 | pool | POOL16 | 0 | Priority default |
| Ethernet60 | ACL17 | overload | - | 10 | Priority_10 |
| Ethernet60 | ACL18 | pool-address-only | POOL18 | 10 | Priority_10 |
| Ethernet60 | ACL19 | pool-full-cone | POOL19 | 10 | Priority_10 |

##### IP NAT: Destination Static

| Interface | Direction | Original IP | Original Port | Access List | Translated IP | Translated Port | Protocol | Group | Priority | Comment |
| --------- | --------- | ----------- | ------------- | ----------- | ------------- | --------------- | -------- | ----- | -------- | ------- |
| Ethernet60 | - | 1.0.0.1 | - | - | 2.0.0.1 | - | - | - | 0 | - |
| Ethernet60 | - | 1.0.0.2 | 22 | - | 2.0.0.2 | - | - | - | 0 | - |
| Ethernet60 | - | 1.0.0.3 | 22 | - | 2.0.0.3 | 23 | - | - | 0 | - |
| Ethernet60 | - | 1.0.0.4 | 22 | - | 2.0.0.4 | 23 | udp | - | 0 | - |
| Ethernet60 | - | 1.0.0.5 | 22 | - | 2.0.0.5 | 23 | tcp | 1 | 0 | - |
| Ethernet60 | - | 1.0.0.6 | 22 | - | 2.0.0.6 | 23 | tcp | 2 | 5 | Comment Test |
| Ethernet60 | - | 1.0.0.7 | - | ACL21 | 2.0.0.7 | - | - | - | 0 | - |
| Ethernet60 | egress | 239.0.0.1 | - | - | 239.0.0.2 | - | - | - | 0 | - |

##### IP NAT: Destination Dynamic

| Interface | Access List | Pool Name | Priority | Comment |
| --------- | ----------- | --------- | -------- | ------- |
| Ethernet60 | ACL1 | POOL1 | 0 | - |
| Ethernet60 | ACL2 | POOL1 | 0 | POOL1 shared with ACL1/2 |
| Ethernet60 | ACL3 | POOL3 | 10 | - |
| Ethernet60 | ACL4 | POOL4 | 1 | Priority low end |
| Ethernet60 | ACL5 | POOL5 | 4294967295 | Priority high end |
| Ethernet60 | ACL6 | POOL6 | 0 | Priority default |

##### IP NAT: Interfaces configured via profile

| Interface | Profile |
| --------- |-------- |
| Ethernet69 | TEST-NAT-PROFILE |

##### IPv6

| Interface | Description | Channel Group | IPv6 Address | VRF | MTU | Shutdown | ND RA Disabled | Managed Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | ----------- | --------------| ------------ | --- | --- | -------- | -------------- | -------------------| ----------- | ------------ |
| Ethernet3 | P2P_LINK_TO_DC1-SPINE2_Ethernet2 | - | 2002:ABDC::1/64 | default | 1500 | - | - | - | - | - |
| Ethernet4 | Molecule IPv6 | - | 2020::2020/64 | default | 9100 | True | True | True | IPv6_ACL_IN | IPv6_ACL_OUT |
| Ethernet8.101 | to WAN-ISP-01 Ethernet2.101 - VRF-C1 | - | 2002:ABDC::1/64 | default | - | - | - | - | - | - |
| Ethernet55 | DHCPv6 Relay Testing | - | a0::1/64 | default | - | False | - | - | - | - |
| Ethernet65 | Multiple VRIDs | - | 2001:db8::2/64 | default | - | False | - | - | - | - |
| Ethernet66 | Multiple VRIDs and tracking | - | 2001:db8::2/64 | default | - | False | - | - | - | - |

##### VRRP Details

| Interface | VRRP-ID | Priority | Advertisement Interval | Preempt | Tracked Object Name(s) | Tracked Object Action(s) | IPv4 Virtual IP | IPv4 VRRP Version | IPv6 Virtual IP |
| --------- | ------- | -------- | ---------------------- | --------| ---------------------- | ------------------------ | --------------- | ----------------- | --------------- |
| Ethernet65 | 1 | 105 | 2 | Enabled | - | - | 192.0.2.1 | 2 | - |
| Ethernet65 | 2 | - | - | Enabled | - | - | - | 2 | 2001:db8::1 |
| Ethernet66 | 1 | 105 | 2 | Enabled | ID1-TrackedObjectDecrement, ID1-TrackedObjectShutdown | Decrement 5, Shutdown | 192.0.2.1 | 2 | - |
| Ethernet66 | 2 | - | - | Enabled | ID2-TrackedObjectDecrement, ID2-TrackedObjectShutdown | Decrement 10, Shutdown | - | 2 | 2001:db8::1 |
| Ethernet66 | 3 | - | - | Disabled | - | - | 100.64.0.1 | 3 | - |

##### ISIS

| Interface | Channel Group | ISIS Instance | ISIS BFD | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | Authentication Mode |
| --------- | ------------- | ------------- | -------- | ----------- | ---- | ----------------- | ------------- | ------------------- |
| Ethernet5 | - | ISIS_TEST | True | 99 | point-to-point | level-2 | False | md5 |

##### EVPN Multihoming

####### EVPN Multihoming Summary

| Interface | Ethernet Segment Identifier | Multihoming Redundancy Mode | Route Target |
| --------- | --------------------------- | --------------------------- | ------------ |
| Ethernet27 | 0000:0000:0000:0102:0304 | single-active | 00:00:01:02:03:04 |
| Ethernet28 | 0000:0000:0000:0102:0305 | all-active | 00:00:01:02:03:05 |

####### Designated Forwarder Election Summary

| Interface | Algorithm | Preference Value | Dont Preempt | Hold time | Subsequent Hold Time | Candidate Reachability Required |
| --------- | --------- | ---------------- | ------------ | --------- | -------------------- | ------------------------------- |
| Ethernet27 | preference | 100 | True | 10 | - | True |

####### EVPN-MPLS summary

| Interface | Shared Index | Tunnel Flood Filter Time |
| --------- | ------------ | ------------------------ |
| Ethernet28 | 100 | 100 |

##### Error Correction Encoding Interfaces

| Interface | Enabled |
| --------- | ------- |
| Ethernet23 | fire-code<br>reed-solomon |
| Ethernet24 | Disabled |

#### Priority Flow Control

| Interface | PFC | Priority | Drop/No_drop |
| Ethernet1 | True | 5 | False |
| Ethernet2 | True | 5 | True |
| Ethernet3 | False | - | - |
| Ethernet4 | True | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_LINK_TO_DC1-SPINE1_Ethernet1
   mtu 1500
   bgp session tracker ST1
   l2 mtu 8000
   l2 mru 8000
   speed forced 100gfull
   switchport access vlan 200
   switchport trunk native vlan tag
   switchport phone vlan 110
   switchport phone trunk tagged
   switchport vlan translation in required
   switchport dot1q vlan tag required
   switchport trunk allowed vlan 110-111,210-211
   switchport mode dot1q-tunnel
   switchport dot1q ethertype 1536
   switchport vlan forwarding accept all
   switchport trunk group g1
   switchport trunk group g2
   no switchport
   switchport source-interface tx
   switchport vlan translation 12 20
   switchport vlan translation 24 inner 78 network 46
   switchport vlan translation 24 inner 78 46
   switchport vlan translation 43 dot1q-tunnel 30
   switchport vlan translation in 10 24
   switchport vlan translation in 37 inner 56 49
   switchport vlan translation in 23 dot1q-tunnel 45
   switchport vlan translation out 34 50
   switchport vlan translation out 10 45 inner 34
   switchport vlan translation out 45 dot1q-tunnel all
   switchport trunk private-vlan secondary
   switchport pvlan mapping 20-30
   ip address 172.31.255.1/31
   ip verify unicast source reachable-via rx
   bfd interval 500 min-rx 500 multiplier 5
   bfd echo
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
   tcp mss ceiling ipv4 70 ipv6 75 egress
   switchport port-security
   switchport port-security mac-address maximum disabled
   priority-flow-control on
   priority-flow-control priority 5 drop
   switchport backup-link Ethernet5 prefer vlan 10
   switchport backup preemption-delay 35
   switchport backup mac-move-burst 20
   switchport backup mac-move-burst-interval 30
   switchport backup initial-mac-move-delay 10
   switchport backup dest-macaddr 01:00:00:00:00:00
   link tracking group EVPN_MH_ES1 upstream
   comment
   Comment created from eos_cli under ethernet_interfaces.Ethernet1
   EOF

!
interface Ethernet2
   description SRV-POD02_Eth1
   switchport dot1q vlan tag disallowed
   switchport trunk allowed vlan 110-111,210-211
   switchport mode trunk
   switchport
   ip address 10.1.255.3/24
   ip address 1.1.1.3/24 secondary
   ip address 1.1.1.4/24 secondary
   ip address 10.0.0.254/24 secondary
   ip address 192.168.1.1/24 secondary
   tcp mss ceiling ipv4 70 ingress
   multicast ipv4 boundary ACL_MULTICAST
   multicast ipv6 boundary ACL_V6_MULTICAST out
   multicast ipv4 static
   switchport port-security violation protect log
   switchport port-security mac-address maximum 100
   priority-flow-control on
   priority-flow-control priority 5 no-drop
   storm-control broadcast level pps 500
   storm-control unknown-unicast level 1
   storm-control all level 10
   spanning-tree bpduguard disable
   spanning-tree bpdufilter disable
!
interface Ethernet3
   description P2P_LINK_TO_DC1-SPINE2_Ethernet2
   mtu 1500
   switchport trunk native vlan 5
   switchport mode trunk
   no switchport
   switchport vlan translation out 23 dot1q-tunnel 50
   no snmp trap link-change
   ip address 172.31.128.1/31
   ipv6 enable
   ipv6 address 2002:ABDC::1/64
   ipv6 nd prefix 2345:ABCD:3FE0::1/96 infinite 50 no-autoconfig
   ipv6 nd prefix 2345:ABCD:3FE0::2/96 50 infinite
   ipv6 nd prefix 2345:ABCD:3FE0::3/96 100000 no-autoconfig
   tcp mss ceiling ipv6 65
   switchport port-security
   no switchport port-security mac-address maximum disabled
   switchport port-security vlan 1 mac-address maximum 3
   switchport port-security vlan 2 mac-address maximum 3
   switchport port-security vlan 2 mac-address maximum 4
   switchport port-security vlan 3 mac-address maximum 3
   switchport port-security vlan 22 mac-address maximum 4
   switchport port-security vlan 41 mac-address maximum 4
   switchport port-security vlan default mac-address maximum 2
   no priority-flow-control
   spanning-tree guard root
   switchport backup-link Ethernet4
   link tracking group EVPN_MH_ES2 downstream
!
interface Ethernet4
   description Molecule IPv6
   shutdown
   mtu 9100
   no switchport
   snmp trap link-change
   ipv6 enable
   ipv6 address 2020::2020/64
   ipv6 address FE80:FEA::AB65/64 link-local
   ipv6 nd ra disabled
   ipv6 nd managed-config-flag
   tcp mss ceiling ipv4 65
   ipv6 access-group IPv6_ACL_IN in
   ipv6 access-group IPv6_ACL_OUT out
   multicast ipv4 boundary 224.0.1.0/24 out
   multicast ipv4 boundary 224.0.2.0/24
   multicast ipv6 boundary ff00::/16 out
   multicast ipv6 boundary ff01::/16 out
   multicast ipv4 static
   switchport port-security violation protect
   priority-flow-control on
   spanning-tree guard none
!
interface Ethernet5
   description Molecule Routing
   no shutdown
   mtu 9100
   switchport access vlan 220
   no switchport
   ip ospf cost 99
   ip ospf network point-to-point
   ip ospf authentication message-digest
   ip ospf authentication-key 7 <removed>
   ip ospf area 100
   ip ospf message-digest-key 1 sha512 7 <removed>
   pim ipv4 sparse-mode
   pim ipv4 bidirectional
   pim ipv4 border-router
   pim ipv4 hello interval 10
   pim ipv4 hello count 2.5
   pim ipv4 dr-priority 200
   pim ipv4 bfd
   isis enable ISIS_TEST
   isis bfd
   isis circuit-type level-2
   isis metric 99
   no isis hello padding
   isis network point-to-point
   isis authentication mode md5
   isis authentication key 7 <removed>
   spanning-tree guard loop
!
interface Ethernet6
   description SRV-POD02_Eth1
   logging event link-status
   logging event congestion-drops
   switchport trunk allowed vlan 110-111,210-211
   switchport mode trunk
   switchport
   logging event storm-control discards
   spanning-tree bpduguard enable
   spanning-tree bpdufilter enable
   logging event spanning-tree
!
interface Ethernet7
   description Molecule L2
   no shutdown
   mtu 7000
   switchport
   ptp enable
   ptp announce interval 10
   ptp announce timeout 30
   ptp delay-mechanism p2p
   ptp delay-req interval 20
   ptp role master
   ptp sync-message interval 5
   ptp transport layer2
   ptp vlan all
   service-profile QoS
   qos trust cos
   qos cos 5
   storm-control broadcast level pps 10
   storm-control multicast level 50
   storm-control unknown-unicast level 10
   storm-control all level 75
   spanning-tree portfast
   spanning-tree bpduguard enable
   spanning-tree bpdufilter enable
   vmtracer vmware-esx
   transceiver media override 100gbase-ar4
!
interface Ethernet8
   description to WAN-ISP1-01 Ethernet2
   no switchport
   no lldp transmit
   no lldp receive
!
interface Ethernet8.101
   description to WAN-ISP-01 Ethernet2.101 - VRF-C1
   encapsulation dot1q vlan 101
   ip address 172.31.128.1/31
   ipv6 enable
   ipv6 address 2002:ABDC::1/64
!
interface Ethernet9
   description interface_with_mpls_enabled
   no switchport
   ip address 172.31.128.9/31
   mpls ldp interface
   multicast ipv4 boundary ACL_MULTICAST out
   multicast ipv6 static
   mpls ip
!
interface Ethernet10
   description interface_with_mpls_disabled
   no switchport
   ip address 172.31.128.10/31
   no mpls ldp interface
   no mpls ip
!
interface Ethernet11
   description interface_in_mode_access_accepting_tagged_LACP
   switchport access vlan 200
   switchport mode access
   switchport
   l2-protocol encapsulation dot1q vlan 200
!
interface Ethernet12
   description interface_with_dot1q_tunnel
   switchport access vlan 300
   switchport mode dot1q-tunnel
   switchport
!
interface Ethernet13
   description interface_in_mode_access_with_voice
   no logging event link-status
   no logging event congestion-drops
   switchport trunk native vlan 100
   switchport phone vlan 70
   switchport phone trunk untagged
   switchport mode trunk phone
   switchport
   no logging event storm-control discards
   no logging event spanning-tree
!
interface Ethernet14
   description SRV-POD02_Eth1
   logging event link-status
   switchport trunk allowed vlan 110-111,210-211
   switchport mode trunk
   switchport
!
interface Ethernet15
   description PVLAN Promiscuous Access - only one secondary
   switchport access vlan 110
   switchport mode access
   switchport
   switchport pvlan mapping 111
!
interface Ethernet16
   description PVLAN Promiscuous Trunk - vlan translation out
   switchport vlan translation out required
   switchport trunk allowed vlan 110-112
   switchport mode trunk
   switchport
   switchport vlan translation out 111-112 110
!
interface Ethernet17
   description PVLAN Secondary Trunk
   switchport trunk allowed vlan 110-112
   switchport mode trunk
   switchport
   switchport trunk private-vlan secondary
!
interface Ethernet18
   description PBR Description
   mtu 1500
   no switchport
   ip address 192.0.2.1/31
   service-policy type pbr input MyLANServicePolicy
!
interface Ethernet19
   description Switched port with no LLDP rx/tx
   switchport access vlan 110
   switchport mode access
   switchport
   no lldp transmit
   no lldp receive
   lldp tlv transmit ztp vlan 666
!
interface Ethernet20
   description Port patched through patch-panel to pseudowire
   no switchport
   no lldp transmit
   no lldp receive
!
interface Ethernet21
   description 200MBit/s shape
   switchport
   no qos trust
   shape rate 200000 kbps
!
interface Ethernet22
   description 10% shape
   switchport
   shape rate 10 percent
!
interface Ethernet23
   description Error-correction encoding
   error-correction encoding fire-code
   error-correction encoding reed-solomon
   switchport
!
interface Ethernet24
   description Disable error-correction encoding
   no error-correction encoding
   switchport
!
interface Ethernet25
   description Molecule MAC
   switchport
   mac access-group MAC_ACL_IN in
   mac access-group MAC_ACL_OUT out
!
interface Ethernet26
   no switchport
!
interface Ethernet26.1
   description TENANT_A pseudowire 1 interface
   encapsulation vlan
      client unmatched
!
interface Ethernet26.100
   description TENANT_A pseudowire 1 interface
   vlan id 10
   encapsulation vlan
      client dot1q 100 network client
!
interface Ethernet26.200
   description TENANT_A pseudowire 2 interface
   encapsulation vlan
      client dot1q 200
!
interface Ethernet26.300
   description TENANT_A pseudowire 3 interface
   encapsulation vlan
      client dot1q 300 network dot1q 400
!
interface Ethernet26.400
   description TENANT_A pseudowire 3 interface
   encapsulation vlan
      client dot1q outer 400 inner 20 network dot1q outer 401 inner 21
!
interface Ethernet26.500
   description TENANT_A pseudowire 3 interface
   encapsulation vlan
      client dot1q outer 500 inner 50 network client
!
interface Ethernet27
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
interface Ethernet28
   description EVPN-MPLS multihoming
   switchport
   !
   evpn ethernet-segment
      identifier 0000:0000:0000:0102:0305
      mpls tunnel flood filter time 100
      mpls shared index 100
      route-target import 00:00:01:02:03:05
!
interface Ethernet29
   description DOT1X Testing - auto phone true
   switchport
   dot1x port-control auto
   dot1x port-control force-authorized phone
!
interface Ethernet30
   description DOT1X Testing - force-authorized phone false
   switchport
   dot1x port-control force-authorized
   no dot1x port-control force-authorized phone
!
interface Ethernet31
   description DOT1X Testing - force-unauthorized - no phone
   switchport
   dot1x port-control force-unauthorized
!
interface Ethernet32
   description DOT1X Testing - auto reauthentication
   switchport
   dot1x reauthentication
   dot1x port-control auto
!
interface Ethernet33
   description DOT1X Testing - pae mode authenticator
   switchport
   dot1x pae authenticator
!
interface Ethernet34
   description DOT1X Testing - authentication_failure allow
   switchport
   dot1x authentication failure action traffic allow vlan 800
!
interface Ethernet35
   description DOT1X Testing - authentication_failure drop
   switchport
   dot1x authentication failure action traffic drop
!
interface Ethernet36
   description DOT1X Testing - host-mode single-host
   switchport
   dot1x host-mode single-host
!
interface Ethernet37
   description DOT1X Testing - host-mode multi-host
   switchport
   dot1x host-mode multi-host
!
interface Ethernet38
   description DOT1X Testing - host-mode multi-host authenticated
   switchport
   dot1x host-mode multi-host authenticated
!
interface Ethernet39
   description DOT1X Testing - mac_based_authentication host-mode common true
   switchport
   dot1x mac based authentication host-mode common
!
interface Ethernet40
   description DOT1X Testing - mac_based_authentication always
   switchport
   dot1x mac based authentication always
!
interface Ethernet41
   description DOT1X Testing - mac_based_authentication always and host-mode common
   switchport
   dot1x mac based authentication host-mode common
   dot1x mac based authentication always
!
interface Ethernet42
   description DOT1X Testing - mac_based_authentication
   switchport
   dot1x mac based authentication
!
interface Ethernet43
   description DOT1X Testing - timeout values
   switchport
   dot1x timeout quiet-period 10
   dot1x timeout reauth-timeout-ignore always
   dot1x timeout tx-period 6
   dot1x timeout reauth-period server
   dot1x timeout idle-host 15 seconds
!
interface Ethernet44
   description DOT1X Testing - reauthorization_request_limit
   switchport
   dot1x eapol disabled
   dot1x reauthorization request limit 3
!
interface Ethernet45
   description DOT1X Testing - all features
   switchport
   dot1x pae authenticator
   dot1x authentication failure action traffic allow vlan 800
   dot1x reauthentication
   dot1x port-control auto
   dot1x host-mode multi-host authenticated
   dot1x mac based authentication
   dot1x timeout quiet-period 10
   dot1x timeout reauth-timeout-ignore always
   dot1x timeout tx-period 10
   dot1x timeout reauth-period server
   dot1x timeout idle-host 10 seconds
   dot1x reauthorization request limit 2
   dot1x unauthorized access vlan membership egress
   dot1x unauthorized native vlan membership egress
   dot1x eapol authentication failure fallback mba timeout 600
!
interface Ethernet46
   description native-vlan-tag-precedence
   switchport trunk native vlan tag
   switchport mode trunk
   switchport
!
interface Ethernet47
   description IP Helper
   no switchport
   ip address 172.31.255.1/31
   ip helper-address 10.10.64.151
   ip helper-address 10.10.96.101 source-interface Loopback0
   ip helper-address 10.10.96.150 vrf MGMT source-interface Loopback0
   ip helper-address 10.10.96.151 vrf MGMT
!
interface Ethernet48
   description Load Interval
   load-interval 5
   switchport
!
interface Ethernet50
   description SFlow Interface Testing - SFlow ingress enabled
   switchport
   sflow enable
!
interface Ethernet51
   description SFlow Interface Testing - SFlow egress enabled
   switchport
   sflow egress enable
!
interface Ethernet52
   description SFlow Interface Testing - SFlow ingress and egress unmodified enabled
   switchport
   sflow enable
   sflow egress unmodified enable
!
interface Ethernet53
   description SFlow Interface Testing - SFlow ingress and egress disabled
   switchport
   no sflow enable
   no sflow egress enable
!
interface Ethernet54
   description SFlow Interface Testing - SFlow ingress and egress unmodified disabled
   switchport
   no sflow enable
   no sflow egress unmodified enable
!
interface Ethernet55
   description DHCPv6 Relay Testing
   no shutdown
   no switchport
   ipv6 dhcp relay destination a0::2 link-address a0::3
   ipv6 dhcp relay destination a0::4 vrf TEST local-interface Loopback55 link-address a0::5
   ipv6 address a0::1/64
!
interface Ethernet56
   description Interface with poe commands and limit in class
   switchport
   poe priority low
   poe reboot action power-off
   poe link down action power-off 10 seconds
   poe shutdown action maintain
   poe limit 30.00 watts
   poe negotiation lldp disabled
!
interface Ethernet57
   description Interface with poe commands and limit in watts
   switchport
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 45.00 watts fixed
   poe legacy detect
!
interface Ethernet58
   description Interface with poe disabled and no other poe keys
   switchport
   poe disabled
!
interface Ethernet60
   description IP NAT Testing
   switchport
   ip nat destination static 1.0.0.1 2.0.0.1
   ip nat destination static 1.0.0.2 22 2.0.0.2
   ip nat destination static 1.0.0.3 22 2.0.0.3 23
   ip nat destination static 1.0.0.4 22 2.0.0.4 23 protocol udp
   ip nat destination static 1.0.0.7 access-list ACL21 2.0.0.7
   ip nat source static 3.0.0.1 4.0.0.1
   ip nat source static 3.0.0.2 22 4.0.0.2
   ip nat source static 3.0.0.3 22 4.0.0.3 23
   ip nat source static 3.0.0.4 22 4.0.0.4 23 protocol udp
   ip nat source static 3.0.0.7 access-list ACL21 4.0.0.7
   ip nat source ingress static 3.0.0.8 4.0.0.8
   ip nat destination egress static 239.0.0.1 239.0.0.2
   ip nat source static 3.0.0.5 22 4.0.0.5 23 protocol tcp group 1
   ip nat destination static 1.0.0.5 22 2.0.0.5 23 protocol tcp group 1
   ip nat source static 3.0.0.6 22 4.0.0.6 23 protocol tcp group 2 comment Comment Test
   ip nat destination static 1.0.0.6 22 2.0.0.6 23 protocol tcp group 2 comment Comment Test
   ip nat destination dynamic access-list ACL1 pool POOL1
   ip nat source dynamic access-list ACL11 pool POOL11
   ip nat source dynamic access-list ACL12 pool POOL11 comment POOL11 shared with ACL11/12
   ip nat source dynamic access-list ACL13 pool POOL13 priority 10
   ip nat source dynamic access-list ACL14 pool POOL14 priority 1 comment Priority low end
   ip nat source dynamic access-list ACL15 pool POOL15 priority 4294967295 comment Priority high end
   ip nat source dynamic access-list ACL16 pool POOL16 comment Priority default
   ip nat source dynamic access-list ACL17 overload priority 10 comment Priority_10
   ip nat source dynamic access-list ACL18 pool POOL18 address-only priority 10 comment Priority_10
   ip nat source dynamic access-list ACL19 pool POOL19 full-cone priority 10 comment Priority_10
   ip nat destination dynamic access-list ACL2 pool POOL1 comment POOL1 shared with ACL1/2
   ip nat destination dynamic access-list ACL3 pool POOL3 priority 10
   ip nat destination dynamic access-list ACL4 pool POOL4 priority 1 comment Priority low end
   ip nat destination dynamic access-list ACL5 pool POOL5 priority 4294967295 comment Priority high end
   ip nat destination dynamic access-list ACL6 pool POOL6 comment Priority default
!
interface Ethernet61
   description interface_in_mode_access_with_voice
   no logging event link-status
   no logging event congestion-drops
   switchport trunk native vlan 100
   switchport phone vlan 70
   switchport phone trunk untagged phone
   switchport mode trunk phone
   switchport
   no logging event storm-control discards
   no logging event spanning-tree
!
interface Ethernet62
   description interface_in_mode_access_with_voice
   no logging event link-status
   no logging event congestion-drops
   switchport trunk native vlan 100
   switchport phone vlan 70
   switchport phone trunk tagged phone
   switchport mode trunk phone
   switchport
   no logging event storm-control discards
   no logging event spanning-tree
!
interface Ethernet63
   description DHCP client interface
   no switchport
   ip address dhcp
   dhcp client accept default-route
!
interface Ethernet64
   description DHCP server interface
   no switchport
   mac timestamp replace-fcs
   ip address 192.168.42.42/24
   dhcp server ipv4
   dhcp server ipv6
!
interface Ethernet65
   description Multiple VRIDs
   no shutdown
   no switchport
   mac timestamp header
   ip address 192.0.2.2/25
   ipv6 enable
   ipv6 address 2001:db8::2/64
   ipv6 address fe80::2/64 link-local
   vrrp 1 priority-level 105
   vrrp 1 advertisement interval 2
   vrrp 1 preempt delay minimum 30 reload 800
   vrrp 1 ipv4 192.0.2.1
   vrrp 2 ipv6 2001:db8::1
!
interface Ethernet66
   description Multiple VRIDs and tracking
   no shutdown
   no switchport
   ip address 192.0.2.2/25
   ipv6 enable
   ipv6 address 2001:db8::2/64
   ipv6 address fe80::2/64 link-local
   vrrp 1 priority-level 105
   vrrp 1 advertisement interval 2
   vrrp 1 preempt delay minimum 30 reload 800
   vrrp 1 ipv4 192.0.2.1
   vrrp 1 tracked-object ID1-TrackedObjectDecrement decrement 5
   vrrp 1 tracked-object ID1-TrackedObjectShutdown shutdown
   vrrp 2 ipv6 2001:db8::1
   vrrp 2 tracked-object ID2-TrackedObjectDecrement decrement 10
   vrrp 2 tracked-object ID2-TrackedObjectShutdown shutdown
   no vrrp 3 preempt
   vrrp 3 timers delay reload 900
   vrrp 3 ipv4 100.64.0.1
   vrrp 3 ipv4 version 3
!
interface Ethernet67
   description Custom_Transceiver_Frequency
   no shutdown
   switchport
   mac timestamp before-fcs
   transceiver frequency 190050.000
!
interface Ethernet67.1
   description Test_encapsulation_dot1q
   encapsulation dot1q vlan 4 inner 34
!
interface Ethernet68
   description Custom_Transceiver_Frequency
   no shutdown
   switchport
   transceiver media override 100gbase-ar4
   transceiver frequency 190080.000 ghz
!
interface Ethernet68.1
   description Test_encapsulation_vlan1
   encapsulation vlan
      client dot1q outer 23 inner dot1q 45 network dot1ad outer 32 inner dot1ad 54
!
interface Ethernet68.2
   description Test_encapsulation_vlan2
   encapsulation vlan
      client dot1q 10 network dot1q outer 32 inner 54
!
interface Ethernet68.3
   description Test_encapsulation_vlan3
   encapsulation vlan
      client dot1ad 12 network dot1q 25
!
interface Ethernet68.4
   description Test_encapsulation_vlan4
   encapsulation vlan
      client dot1ad outer 35 inner dot1q 60 network dot1q outer 53 inner dot1ad 6
!
interface Ethernet68.5
   description Test_encapsulation_vlan5
   encapsulation vlan
      client dot1ad outer 35 inner 60 network dot1ad outer 52 inner 62
!
interface Ethernet68.6
   description Test_encapsulation_vlan6
   encapsulation vlan
      client dot1ad outer 35 inner 60 network client
!
interface Ethernet68.7
   description Test_encapsulation_vlan7
   encapsulation vlan
      client untagged network dot1ad outer 35 inner 60
!
interface Ethernet68.8
   description Test_encapsulation_vlan8
   encapsulation vlan
      client untagged network dot1q outer 35 inner 60
!
interface Ethernet68.9
   description Test_encapsulation_vlan9
   encapsulation vlan
      client untagged network untagged
!
interface Ethernet68.10
   description Test_encapsulation_vlan9
   encapsulation vlan
      client dot1q outer 14 inner 11 network client inner
!
interface Ethernet69
   description IP NAT service-profile
   switchport
   ip nat service-profile TEST-NAT-PROFILE
!
interface Ethernet70
   description dot1x_aaa_unresponsive
   no shutdown
   dot1x aaa unresponsive phone action apply cached-results timeout 10 hours else traffic allow
   dot1x aaa unresponsive action traffic allow vlan 10 access-list acl1
   dot1x aaa unresponsive eap response success
   dot1x mac based access-list
!
interface Ethernet71
   description dot1x_aaa_unresponsive1
   no shutdown
   dot1x aaa unresponsive phone action apply cached-results timeout 10 hours
   dot1x aaa unresponsive action traffic allow vlan 10 access-list acl1
   dot1x aaa unresponsive eap response success
   dot1x mac based access-list
!
interface Ethernet72
   description dot1x_aaa_unresponsive2
   no shutdown
   dot1x aaa unresponsive action traffic allow vlan 10 access-list acl1
   dot1x aaa unresponsive eap response success
   dot1x mac based access-list
```

## BFD

### BFD Interfaces

| Interface | Interval | Minimum RX | Multiplier | Echo |
| --------- | -------- | ---------- | ---------- | ---- |
| Ethernet1 | 500 | 500 | 5 | True |

## MPLS

### MPLS Interfaces

| Interface | MPLS IP Enabled | LDP Enabled | IGP Sync |
| --------- | --------------- | ----------- | -------- |
| Ethernet9 | True | True | - |
| Ethernet10 | False | False | - |

## Multicast

### PIM Sparse Mode

#### PIM Sparse Mode Enabled Interfaces

| Interface Name | VRF Name | IP Version | Border Router | DR Priority | Local Interface |
| -------------- | -------- | ---------- | ------------- | ----------- | --------------- |
| Ethernet5 | - | IPv4 | True | 200 | - |

## 802.1X Port Security

### 802.1X Summary

#### 802.1X Interfaces

| Interface | PAE Mode | State | Phone Force Authorized | Reauthentication | Auth Failure Action | Host Mode | Mac Based Auth | Eapol |
| --------- | -------- | ------| ---------------------- | ---------------- | ------------------- | --------- | -------------- | ------ |
| Ethernet29 | - | auto | True | - | - | - | - | - |
| Ethernet30 | - | force-authorized | False | - | - | - | - | - |
| Ethernet31 | - | force-unauthorized | - | - | - | - | - | - |
| Ethernet32 | - | auto | - | True | - | - | - | - |
| Ethernet33 | authenticator | - | - | - | - | - | - | - |
| Ethernet34 | - | - | - | - | allow vlan 800 | - | - | - |
| Ethernet35 | - | - | - | - | drop | - | - | - |
| Ethernet36 | - | - | - | - | - | single-host | - | - |
| Ethernet37 | - | - | - | - | - | multi-host | - | - |
| Ethernet38 | - | - | - | - | - | multi-host | - | - |
| Ethernet39 | - | - | - | - | - | - | True | - |
| Ethernet40 | - | - | - | - | - | - | True | - |
| Ethernet41 | - | - | - | - | - | - | True | - |
| Ethernet42 | - | - | - | - | - | - | True | - |
| Ethernet43 | - | - | - | - | - | - | - | - |
| Ethernet44 | - | - | - | - | - | - | - | - |
| Ethernet45 | authenticator | auto | - | True | allow vlan 800 | multi-host | True | True |
| Ethernet70 | - | - | - | - | - | - | - | - |
| Ethernet71 | - | - | - | - | - | - | - | - |
| Ethernet72 | - | - | - | - | - | - | - | - |

## Power Over Ethernet (PoE)

### PoE Summary

#### PoE Interfaces

| Interface | PoE Enabled | Priority | Limit | Reboot Action | Link Down Action | Shutdown Action | LLDP Negotiation | Legacy Detection |
| --------- | --------- | --------- | ----------- | ----------- | ----------- | ----------- | --------- | --------- |
| Ethernet56 | True | low | 30.00 watts | power-off | power-off (delayed 10 seconds) | maintain | False | - |
| Ethernet57 | True | critical | 45.00 watts (fixed) | maintain | maintain | power-off | True | True |
| Ethernet58 | False | - | - | - | - | - | - | - |

## Quality Of Service

### QOS Interfaces

| Interface | Trust | Default DSCP | Default COS | Shape rate |
| --------- | ----- | ------------ | ----------- | ---------- |
| Ethernet7 | cos | - | 5 | - |
| Ethernet21 | disabled | - | - | 200000 kbps |
| Ethernet22 | - | - | - | 10 percent |
