# host7

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Address Locking](#address-locking)
  - [Address Locking Summary](#address-locking-summary)
- [Address Locking Interfaces](#address-locking-interfaces)
  - [Address Locking Device Configuration](#address-locking-device-configuration)
- [Management Security](#management-security)
  - [Management Security Summary](#management-security-summary)
  - [Management Security Device Configuration](#management-security-device-configuration)
- [Monitoring](#monitoring)
  - [Logging](#logging)
  - [Monitor Sessions](#monitor-sessions)
  - [Tap Aggregation](#tap-aggregation)
  - [SFlow](#sflow)
  - [Hardware](#hardware)
  - [Flow Tracking](#flow-tracking)
  - [Monitor Telemetry Postcard Policy](#monitor-telemetry-postcard-policy)
- [Hardware TCAM Profile](#hardware-tcam-profile)
  - [Custom TCAM Profiles](#custom-tcam-profiles)
  - [Hardware TCAM Device Configuration](#hardware-tcam-device-configuration)
- [L2 Protocol Forwarding](#l2-protocol-forwarding)
  - [Forwarding Profiles](#forwarding-profiles)
  - [L2 Protocol Forwarding Device Configuration](#l2-protocol-forwarding-device-configuration)
- [IP Security](#ip-security)
  - [IP Security Device Configuration](#ip-security-device-configuration)
- [Interfaces](#interfaces)
  - [DPS Interfaces](#dps-interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Tunnel Interfaces](#tunnel-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
  - [VXLAN Interface](#vxlan-interface)
- [Switchport Port-security](#switchport-port-security)
  - [Switchport Port-security Summary](#switchport-port-security-summary)
  - [Switchport Port-security Device Configuration](#switchport-port-security-device-configuration)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [Router General](#router-general)
  - [Router BGP](#router-bgp)
- [Queue Monitor](#queue-monitor)
  - [Queue Monitor Length](#queue-monitor-length)
  - [Queue Monitor Streaming](#queue-monitor-streaming)
  - [Queue Monitor Configuration](#queue-monitor-configuration)
- [Filters](#filters)
  - [Match-lists](#match-lists)
- [802.1X Port Security](#8021x-port-security)
  - [802.1X Summary](#8021x-summary)
- [Power Over Ethernet (PoE)](#power-over-ethernet-poe)
  - [PoE Summary](#poe-summary)
  - [PoE Device Configuration](#poe-device-configuration)
- [ACL](#acl)
  - [Extended Access-lists](#extended-access-lists)
  - [IP Access-lists](#ip-access-lists)
- [Platform](#platform)
  - [Platform Summary](#platform-summary)
  - [Platform Device Configuration](#platform-device-configuration)
- [Application Traffic Recognition](#application-traffic-recognition)
  - [Applications](#applications)
  - [Application Profiles](#application-profiles)
  - [Categories](#categories)
  - [Router Application-Traffic-Recognition Device Configuration](#router-application-traffic-recognition-device-configuration)
- [Group-Based Multi-domain Segmentation Services (MSS-Group)](#group-based-multi-domain-segmentation-services-mss-group)
  - [Segmentation Policies](#segmentation-policies)
  - [Segment Definitions](#segment-definitions)
  - [Router MSS-G Device Configuration](#router-mss-g-device-configuration)
  - [Router Path-selection](#router-path-selection)
- [IP NAT](#ip-nat)
  - [NAT Profiles](#nat-profiles)
  - [NAT Pools](#nat-pools)
  - [NAT Synchronization](#nat-synchronization)
  - [NAT Translation Settings](#nat-translation-settings)
  - [IP NAT Device Configuration](#ip-nat-device-configuration)
- [Errdisable](#errdisable)
  - [Errdisable Summary](#errdisable-summary)
  - [Traffic Policies information](#traffic-policies-information)
- [Quality Of Service](#quality-of-service)
  - [QOS](#qos)
  - [QOS Class Maps](#qos-class-maps)
  - [QOS Policy Maps](#qos-policy-maps)
  - [QOS Profiles](#qos-profiles)
  - [Control-plane Policy Map](#control-plane-policy-map)
  - [Priority Flow Control](#priority-flow-control-2)

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

## Address Locking

### Address Locking Summary

| Setting | Value |
| -------- | ----- |
| Disable IP locking on configured ports | False |
| Disable enforcement for locked ipv4 addresses | True |
| Disable enforcement for locked ipv6 addresses | True |

## Address Locking Interfaces

| Interface | IPv4 Address Locking | IPv6 Address Locking |
| --------- | -------------------- | -------------------- |
| Ethernet1 | True | True |
| Ethernet2 | False | True |

### Address Locking Device Configuration

```eos
!
address locking
   locked-address ipv4 enforcement disabled
   locked-address ipv6 enforcement disabled
```

## Management Security

### Management Security Summary

| Settings | Value |
| -------- | ----- |
| Entropy sources | hardware, hardware exclusive |

### Management Security Device Configuration

```eos
!
management security
   entropy source hardware
   entropy source hardware exclusive
```

## Monitoring

### Logging

#### Logging Servers and Features Summary

| Type | Level |
| -----| ----- |

#### Logging Servers and Features Device Configuration

```eos
!
logging event storm-control discards global
logging event storm-control discards interval 10
!
logging event congestion-drops interval 10
!
```

### Monitor Sessions

#### Monitor Sessions Summary

##### myMonitoringSession1

####### myMonitoringSession1 Sources

| Sources | Direction | Access Group Type | Access Group Name | Access Group Priority |
| ------- | --------- | ----------------- | ----------------- | --------------------- |
| Ethernet1 | both | ipv6 | ipv6ACL | - |
| Ethernet5 | both | ip | ipv4ACL | 10 |
| Ethernet18 | tx | mac | macACL | 100 |

####### myMonitoringSession1 Destinations and Session Settings

| Settings | Values |
| -------- | ------ |
| Destinations | - |
| Encapsulation Gre Metadata Tx | True |
| Header Remove Size | 32 |
| Truncate Enabled | True |

##### myMonitoringSession2

####### myMonitoringSession2 Sources

| Sources | Direction | Access Group Type | Access Group Name | Access Group Priority |
| ------- | --------- | ----------------- | ----------------- | --------------------- |

####### myMonitoringSession2 Destinations and Session Settings

| Settings | Values |
| -------- | ------ |
| Destinations | Cpu |
| Encapsulation Gre Metadata Tx | True |
| Access Group Type | ip |
| Access Group Name | ipv4ACL |
| Sample | 50 |

##### myMonitoringSession3

####### myMonitoringSession3 Sources

| Sources | Direction | Access Group Type | Access Group Name | Access Group Priority |
| ------- | --------- | ----------------- | ----------------- | --------------------- |
| Ethernet20 | both | ip | ipv4ACL | 10 |

####### myMonitoringSession3 Destinations and Session Settings

| Settings | Values |
| -------- | ------ |
| Destinations | - |

##### myMonitoringSession4

####### myMonitoringSession4 Sources

| Sources | Direction | Access Group Type | Access Group Name | Access Group Priority |
| ------- | --------- | ----------------- | ----------------- | --------------------- |
| Ethernet18 | tx | mac | macACL | 100 |

####### myMonitoringSession4 Destinations and Session Settings

| Settings | Values |
| -------- | ------ |
| Destinations | Cpu |
| Encapsulation Gre Metadata Tx | True |

##### Monitor Session Default Settings

| Settings | Values |
| -------- | ------ |
| Encapsulation GRE Payload | inner-packet |

#### Monitor Sessions Device Configuration

```eos
!
monitor session myMonitoringSession1 source Ethernet1 ipv6 access-group ipv6ACL
monitor session myMonitoringSession1 source Ethernet5 both ip access-group ipv4ACL priority 10
monitor session myMonitoringSession1 source Ethernet18 tx mac access-group macACL priority 100
monitor session myMonitoringSession1 truncate
monitor session myMonitoringSession1 header remove size 32
monitor session myMonitoringSession1 encapsulation gre metadata tx
monitor session myMonitoringSession2 ip access-group ipv4ACL
monitor session myMonitoringSession2 destination Cpu
monitor session myMonitoringSession2 sample 50
monitor session myMonitoringSession2 encapsulation gre metadata tx
monitor session myMonitoringSession3 source Ethernet20 both ip access-group ipv4ACL priority 10
monitor session myMonitoringSession4 source Ethernet18 tx mac access-group macACL priority 100
monitor session myMonitoringSession4 destination Cpu
monitor session myMonitoringSession4 encapsulation gre metadata tx
!
monitor session default encapsulation gre payload inner-packet
```

### Tap Aggregation

#### Tap Aggregation Summary

| Settings | Values |
| -------- | ------ |
| Mode Exclusive | True |
| Mode Exclusive Profile | tap-aggregation-extended |
| Mode Exclusive No-Errdisable | Ethernet1/1, Ethetnet 42/1, Port-Channel200 |
| Encapsulation Dot1br Strip | True |
| Encapsulation Vn Tag Strip | True |
| Protocol LLDP Trap | True |
| Truncation Size | 169 |
| Mac Timestamp | Header Format 64-bit |
| Mac Timestamp | Header eth-type 5 |
| Mac FCS Error | pass-through |

#### Tap Aggregation Device Configuration

```eos
!
tap aggregation
   mode exclusive profile tap-aggregation-extended
   encapsulation dot1br strip
   encapsulation vn-tag strip
   protocol lldp trap
   mode exclusive no-errdisable Ethernet1/1
   mode exclusive no-errdisable Ethetnet 42/1
   mode exclusive no-errdisable Port-Channel200
   truncation size 169
   mac timestamp header format 64-bit
   mac timestamp header eth-type 5
   mac fcs-error pass-through
```

### SFlow

#### SFlow Summary

sFlow Sample Output Subinterface is enabled.

sFlow is disabled.

Unmodified egress sFlow is enabled on all interfaces by default.

sFlow hardware acceleration is enabled.

sFlow hardware accelerated Sample Rate: 1024

#### SFlow Hardware Accelerated Modules

| Module | Acceleration Enabled |
| ------ | -------------------- |
| Linecard1 | True |
| Linecard2 | True |
| Linecard3 | False |

#### SFlow Extensions

| Extension | Enabled |
| --------- | ------- |
| tunnel | False |

#### SFlow Interfaces

| Interface | Ingress Enabled | Egress Enabled |
| --------- | --------------- | -------------- |
| Ethernet1 | - | True (unmodified) |
| Ethernet2 | - | False (unmodified) |
| Port-Channel5 | - | True (unmodified) |
| Port-Channel6 | - | False (unmodified) |

#### SFlow Device Configuration

```eos
!
sflow sample output subinterface
no sflow extension tunnel
sflow interface egress unmodified enable default
sflow hardware acceleration
sflow hardware acceleration sample 1024
sflow hardware acceleration module Linecard1
sflow hardware acceleration module Linecard2
no sflow hardware acceleration module Linecard3
```

### Hardware

#### Hardware Counters

##### Hardware Counters Summary

###### Hardware Counter Features

**NOTE:** Not all options (columns) in the table below are compatible with every available feature, it is the user responsibility to configure valid options for each feature.

| Feature | Flow Direction | Address Type | Layer3 | VRF | Prefix | Units Packets |
| ------- | -------------- | ------------ | ------ | --- | ------ | ------------- |
| gre tunnel interface | out | - | - | - | - | - |
| ip | in | - | - | False | - | False |
| ip | out | - | - | True | - | True |
| mpls lfib | - | - | - | - | - | True |
| route | - | ipv4 | test | - | 192.168.0.0/24 | - |
| route | - | ipv6 | - | - | 2001:db8:cafe::/64 | - |
| segment-security | in | - | - | - | - | - |

#### Hardware Device Configuration

```eos
!
hardware port-group 1 select Et32/1-4
hardware port-group 2 select Et32/1,Et32/3,Et34
!
hardware counter feature gre tunnel interface out
hardware counter feature ip in
hardware counter feature ip out layer3 units packets
hardware counter feature mpls lfib units packets
hardware counter feature route ipv4 vrf test 192.168.0.0/24
hardware counter feature route ipv6 2001:db8:cafe::/64
hardware counter feature segment-security in
!
hardware access-list mechanism tcam
!
hardware speed-group 3/1 serdes 25g
```

### Flow Tracking

#### Flow Tracking Hardware

Software export of IPFIX data records enabled.

##### Trackers Summary

| Tracker Name | Record Export On Inactive Timeout | Record Export On Interval | Number of Exporters | Applied On |
| ------------ | --------------------------------- | ------------------------- | ------------------- | ---------- |
| T1 | 3666 | 5666 | 0 |  |
| T2 | - | - | 1 | Ethernet1 |
| T3 | - | - | 4 | Dps1<br>Port-Channel5 |

##### Exporters Summary

| Tracker Name | Exporter Name | Collector IP/Host | Collector Port | Local Interface |
| ------------ | ------------- | ----------------- | -------------- | --------------- |
| T2 | T2-E1 | - | - | No local interface |
| T3 | T3-E1 | - | - | No local interface |
| T3 | T3-E2 | - | - | No local interface |
| T3 | T3-E3 | - | - | Management1 |
| T3 | T3-E4 | - | - | No local interface |

#### Flow Tracking Device Configuration

```eos
!
flow tracking hardware
   tracker T1
      record export on inactive timeout 3666
      record export on interval 5666
   !
   tracker T2
      exporter T2-E1
         collector 42.42.42.42
   !
   tracker T3
      exporter T3-E1
      !
      exporter T3-E2
         collector 10.10.10.10 port 777
      !
      exporter T3-E3
         collector this.is.my.awesome.collector.dns.name port 888
         format ipfix version 10
         local interface Management1
         template interval 424242
      !
      exporter T3-E4
         collector dead:beef::cafe
   record format ipfix standard timestamps counters
   no shutdown
```

### Monitor Telemetry Postcard Policy

#### Sample Policy Summary

##### samplepo1

###### Match rules

| Rule Name | Rule Type | Source Prefix | Destination Prefix | Protocol | Source Ports | Destination Ports |
| --------- | --------- | ------------- | ------------------ | -------- | ------------ | ----------------- |
| rule2 | ipv6 | 5::0/128 | 4::0/128 | udp | - | 747, 748-800 |

#### Monitor Telemetry Postcard Policy Configuration

```eos
!
monitor telemetry postcard policy
   marker vxlan header word 0 bit 30
   !
   sample policy samplepo1
      match rule2 ipv6
         source prefix 5::0/128
         destination prefix 4::0/128
         protocol udp destination port 747, 748-800
```

## Hardware TCAM Profile

TCAM profile **`traffic_policy`** is active

### Custom TCAM Profiles

Following TCAM profiles are configured on device:

- Profile Name: `MY_TCAM_PROFILE`

### Hardware TCAM Device Configuration

```eos
!
hardware tcam
   profile MY_TCAM_PROFILE
      source flash:/TCAM_PROFILES/MY_TCAM_PROFILE.conf
   !
   system profile traffic_policy
```

## L2 Protocol Forwarding

### Forwarding Profiles

#### TEST1

| Protocol | Forward | Tagged Forward | Untagged Forward |
| -------- | ------- | -------------- | ---------------- |
| bfd per-link rfc-7130 | True | True | True |
| e-lmi | True | True | True |
| isis | True | True | True |
| lacp | True | True | True |
| lldp | True | True | True |
| macsec | True | True | True |
| pause | True | True | True |
| stp | True | True | True |

#### TEST2

| Protocol | Forward | Tagged Forward | Untagged Forward |
| -------- | ------- | -------------- | ---------------- |
| bfd per-link rfc-7130 | False | True | - |
| e-lmi | True | - | - |
| isis | - | - | True |
| lacp | True | False | True |
| lldp | False | True | False |
| macsec | - | True | - |
| pause | False | - | True |
| stp | - | True | True |

### L2 Protocol Forwarding Device Configuration

```eos
!
l2-protocol
   forwarding profile TEST1
      bfd per-link rfc-7130 forward
      bfd per-link rfc-7130 tagged forward
      bfd per-link rfc-7130 untagged forward
      e-lmi forward
      e-lmi tagged forward
      e-lmi untagged forward
      isis forward
      isis tagged forward
      isis untagged forward
      lacp forward
      lacp tagged forward
      lacp untagged forward
      lldp forward
      lldp tagged forward
      lldp untagged forward
      macsec forward
      macsec tagged forward
      macsec untagged forward
      pause forward
      pause tagged forward
      pause untagged forward
      stp forward
      stp tagged forward
      stp untagged forward
   forwarding profile TEST2
      bfd per-link rfc-7130 tagged forward
      e-lmi forward
      isis untagged forward
      lacp forward
      lacp untagged forward
      lldp tagged forward
      macsec tagged forward
      pause untagged forward
      stp tagged forward
      stp untagged forward
```

## IP Security

- Hardware encryption is disabled

### IP Security Device Configuration

```eos
!
ip security
   hardware encryption disabled
```

## Interfaces

### DPS Interfaces

#### DPS Interfaces Summary

| Interface | IP address | Shutdown | MTU | Flow tracker(s) | TCP MSS Ceiling |
| --------- | ---------- | -------- | --- | --------------- | --------------- |
| Dps1 | 192.168.42.42/24 | True | 666 | Hardware: T3<br>Sampled: T2 | IPv4: 666<br>IPv6: 666<br>Direction: ingress |

#### DPS Interfaces Device Configuration

```eos
!
interface Dps1
   description Test DPS Interface
   shutdown
   mtu 666
   flow tracker hardware T3
   flow tracker sampled T2
   ip address 192.168.42.42/24
   tcp mss ceiling ipv4 666 ipv6 666 ingress
   load-interval 42
```

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

##### VLAN Translations

| Interface | Direction | From VLAN ID(s) | To VLAN ID | From Inner VLAN ID | To Inner VLAN ID | Network | Dot1q-tunnel |
| --------- | --------- | --------------- | ---------- | ------------------ | ---------------- | ------- | ------------ |
| Ethernet1 | both | 24 | 46 | 78 | - | True | - |
| Ethernet1 | both | 43 | 30 | - | - | - | True |
| Ethernet1 | in | 23 | 45 | - | - | - | True |
| Ethernet1 | out | 23 | 50 | - | - | - | True |
| Ethernet1 | out | 45 | all | - | - | - | True |
| Ethernet1 | out | 55 | - | - | - | - | - |

##### IP NAT: Source Static

| Interface | Direction | Original IP | Original Port | Access List | Translated IP | Translated Port | Protocol | Group | Priority | Comment |
| --------- | --------- | ----------- | ------------- | ----------- | ------------- | --------------- | -------- | ----- | -------- | ------- |
| Ethernet1 | ingress | 3.0.0.8 | - | - | 4.0.0.8 | - | - | - | 0 | - |

##### IP NAT: Destination Static

| Interface | Direction | Original IP | Original Port | Access List | Translated IP | Translated Port | Protocol | Group | Priority | Comment |
| --------- | --------- | ----------- | ------------- | ----------- | ------------- | --------------- | -------- | ----- | -------- | ------- |
| Ethernet1 | egress | 239.0.0.1 | - | - | 239.0.0.2 | - | - | - | 0 | - |

##### IP NAT: Interfaces configured via profile

| Interface | Profile |
| --------- |-------- |
| Ethernet3 | TEST-NAT-PROFILE |

#### Priority Flow Control

| Interface | PFC | Priority | Drop/No_drop |
| Ethernet1 | True | - | - |
| Ethernet2 | True | 5 | True |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   l2-protocol forwarding profile TEST1
   l2 mtu 8000
   l2 mru 8000
   logging event congestion-drops
   switchport vlan translation in required
   switchport dot1q vlan tag required
   switchport dot1q ethertype 1536
   switchport vlan forwarding accept all
   switchport source-interface tx
   switchport vlan translation 24 inner 78 network 46
   switchport vlan translation 43 dot1q-tunnel 30
   switchport vlan translation in 23 dot1q-tunnel 45
   switchport vlan translation out 45 dot1q-tunnel all
   switchport vlan translation out 23 dot1q-tunnel 50
   mac timestamp replace-fcs
   flow tracker hardware T2
   address locking ipv4 ipv6
   ip verify unicast source reachable-via rx
   mac security profile A1
   ip nat source ingress static 3.0.0.8 4.0.0.8
   ip nat destination egress static 239.0.0.1 239.0.0.2
   poe priority low
   poe reboot action power-off
   poe link down action power-off 10 seconds
   poe shutdown action maintain
   poe disabled
   poe limit 30.00 watts
   poe negotiation lldp disabled
   priority-flow-control on
   !
   tx-queue 2
      random-detect ecn count
   sflow egress unmodified enable
   storm-control broadcast level pps 500
   storm-control unknown-unicast level 1
   storm-control all level 10
   logging event storm-control discards
!
interface Ethernet2
   no logging event congestion-drops
   switchport dot1q vlan tag disallowed
   mac timestamp header
   address locking ipv6
   poe priority critical
   poe reboot action maintain
   poe link down action maintain
   poe shutdown action power-off
   poe limit 45.00 watts fixed
   poe legacy detect
   priority-flow-control on
   priority-flow-control priority 5 no-drop
   no sflow egress unmodified enable
   storm-control broadcast level pps 10
   storm-control multicast level 50
   storm-control unknown-unicast level 10
   storm-control all level 75
   no logging event storm-control discards
!
interface Ethernet3
   mac timestamp before-fcs
   ip nat service-profile TEST-NAT-PROFILE
   !
   uc-tx-queue 4
      random-detect ecn count
   dot1x aaa unresponsive action traffic allow vlan 10 access-list acl1
   dot1x mac based access-list
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |

##### VLAN Translations

| Interface |  Direction | From VLAN ID(s) | To VLAN ID | From Inner VLAN ID | To Inner VLAN ID | Network | Dot1q-tunnel |
| --------- |  --------- | --------------- | ---------- | ------------------ | ---------------- | ------- | ------------ |
| Port-Channel5 | both | 24 | 46 | 78 | - | True | - |
| Port-Channel5 | both | 43 | 30 | - | - | - | True |
| Port-Channel5 | in | 23 | 45 | - | - | - | True |
| Port-Channel5 | out | 23 | 22 | - | - | - | True |
| Port-Channel5 | out | 45 | all | - | - | - | True |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel5
   l2-protocol forwarding profile TEST2
   switchport vlan translation in required
   switchport dot1q vlan tag disallowed
   switchport vlan forwarding accept all
   switchport source-interface tx multicast
   switchport vlan translation 24 inner 78 network 46
   switchport vlan translation 43 dot1q-tunnel 30
   switchport vlan translation in 23 dot1q-tunnel 45
   switchport vlan translation out 23 dot1q-tunnel 22
   switchport vlan translation out 45 dot1q-tunnel all
   flow tracker hardware T3
   ip verify unicast source reachable-via rx
   l2 mtu 8000
   l2 mru 8000
   sflow egress unmodified enable
   storm-control broadcast level 1
   storm-control multicast level 1
   storm-control unknown-unicast level 1
   logging event storm-control discards
!
interface Port-Channel6
   switchport dot1q vlan tag required
   switchport dot1q ethertype 1536
   no sflow egress unmodified enable
```

### Tunnel Interfaces

#### Tunnel Interfaces Summary

| Interface | Description | VRF | Underlay VRF | MTU | Shutdown | NAT Profile | Mode | Source Interface | Destination | PMTU-Discovery | IPsec Profile |
| --------- | ----------- | --- | ------------ | --- | -------- | ----------- | ---- | ---------------- | ----------- | -------------- | ------------- |
| Tunnel1 | - | default | default | - | - | NAT-PROFILE-NO-VRF-2 | - | - | - | - | - |

#### Tunnel Interfaces Device Configuration

```eos
!
interface Tunnel1
   ip access-group test-in in
   ip access-group test-out out
   ipv6 access-group test-in in
   ipv6 access-group test-out out
   ip nat service-profile NAT-PROFILE-NO-VRF-2
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan2001 | - | default | - | - |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| Vlan2001 |  default  |  -  |  -  |  -  |  ACL_IN  |  ACL_OUT  |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan2001
   ip verify unicast source reachable-via rx
   ip access-group ACL_IN in
   ip access-group ACL_OUT out
```

### VXLAN Interface

#### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| UDP port | 4789 |
| Qos dscp propagation encapsulation | Enabled |
| Qos ECN propagation | Enabled |
| Qos map dscp to traffic-class decapsulation | Enabled |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description DC1-LEAF2A_VTEP
   vxlan qos ecn propagation
   vxlan qos dscp propagation encapsulation
   vxlan qos map dscp to traffic-class decapsulation
```

## Switchport Port-security

### Switchport Port-security Summary

| Settings | Value |
| -------- | ----- |
| Mac-address Aging | True |
| Mac-address Moveable | True |
| Violation Protect Chip-based | True |

### Switchport Port-security Device Configuration

```eos
!
switchport port-security mac-address aging
switchport port-security mac-address moveable
switchport port-security violation protect chip-based
```

## Routing

### Service Routing Protocols Model

Single agent routing protocol model enabled

```eos
!
service routing protocols model ribd
```

### Router General

- Nexthop fast fail-over is enabled.

#### Router General Device Configuration

```eos
!
router general
   hardware next-hop fast-failover
   exit
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| - | - |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | Encapsulation |
| ---------- | -------- | ------------ | ------------- | ------------- |
| TEST-ENCAPSULATION-2 | True |  - | - | path-selection |

##### EVPN Neighbors

| Neighbor | Activate | Route-map In | Route-map Out | Encapsulation |
| -------- | -------- | ------------ | ------------- | ------------- |
| 10.100.100.4 | True | - | - | path-selection |

#### Router BGP Device Configuration

```eos
```

## Queue Monitor

### Queue Monitor Length

| Enabled | Logging Interval | Default Thresholds High | Default Thresholds Low | Notifying | TX Latency | CPU Thresholds High | CPU Thresholds Low |
| ------- | ---------------- | ----------------------- | ---------------------- | --------- | ---------- | ------------------- | ------------------ |
| True | 100 | 100 | 10 | enabled | enabled | 200000 | 100000 |

### Queue Monitor Streaming

| Enabled | IP Access Group | IPv6 Access Group | Max Connections | VRF |
| ------- | --------------- | ----------------- | --------------- | --- |
| True | ACL-QMS | ACLv6-QMS | 5 | test |

### Queue Monitor Configuration

```eos
!
queue-monitor length
queue-monitor length notifying
queue-monitor length tx-latency
queue-monitor length default thresholds 100 10
queue-monitor length cpu thresholds 200000 100000
!
queue-monitor length log 100
!
queue-monitor streaming
   max-connections 5
   ip access-group ACL-QMS
   ipv6 access-group ACLv6-QMS
   vrf test
   no shutdown
```

## Filters

### Match-lists

#### Match-list Input IPv6-prefix Summary

| Prefix List Name | Prefixes |
| ---------------- | -------- |
| molecule_v6 | 2001:0DB8::/32 |

#### Match-lists Device Configuration

```eos
!
match-list input prefix-ipv6 molecule_v6
   match prefix-ipv6 2001:0DB8::/32
```

## 802.1X Port Security

### 802.1X Summary

#### 802.1X Interfaces

| Interface | PAE Mode | State | Phone Force Authorized | Reauthentication | Auth Failure Action | Host Mode | Mac Based Auth | Eapol |
| --------- | -------- | ------| ---------------------- | ---------------- | ------------------- | --------- | -------------- | ------ |
| Ethernet3 | - | - | - | - | - | - | - | - |

## Power Over Ethernet (PoE)

### PoE Summary

#### PoE Global

| Reboot Action | Shutdown Action | LLDP Negotiation |
| ------------------- | -------------------- | ----------------------|
| maintain | power-off | - |

#### PoE Interfaces

| Interface | PoE Enabled | Priority | Limit | Reboot Action | Link Down Action | Shutdown Action | LLDP Negotiation | Legacy Detection |
| --------- | --------- | --------- | ----------- | ----------- | ----------- | ----------- | --------- | --------- |
| Ethernet1 | False | low | 30.00 watts | power-off | power-off (delayed 10 seconds) | maintain | False | - |
| Ethernet2 | True | critical | 45.00 watts (fixed) | maintain | maintain | power-off | True | True |

### PoE Device Configuration

```eos
!
poe
   reboot action maintain
   interface shutdown action power-off
```

## ACL

### Extended Access-lists

#### Extended Access-lists Summary

##### ACL-03

| Sequence | Action |
| -------- | ------ |
| 10 | remark ACL to restrict access RFC1918 addresses |
| 20 | deny ip 10.0.0.0/8 any |
| 30 | permit ip 192.0.2.0/24 any |

#### Extended Access-lists Device Configuration

```eos
!
ip access-list ACL-03
   10 remark ACL to restrict access RFC1918 addresses
   20 deny ip 10.0.0.0/8 any
   30 permit ip 192.0.2.0/24 any
```

### IP Access-lists

#### IP Access-lists Device Configuration

```eos
```

## Platform

### Platform Summary

#### Platform Trident Summary

| Settings | Value |
| -------- | ----- |
| Routing MAC Address per VLAN | true |
| Forwarding Table Partition | 2 |
| MMU Applied Profile | mc_example_profile |

#### Trident MMU QUEUE PROFILES

##### mc_example_profile

| Type | Egress Queue | Threshold | Reserved | Drop-Precedence |
| ---- | ------------ | --------- | -------- | --------------- |
| Unicast | 1 | - | 0 bytes | - |
| Unicast | 2 | 1/8 | 0 cells | - |
| Multicast | 0 | - | 0 bytes | - |
| Multicast | 1 | 1/64 | 0 cells | - |
| Multicast | 7 | 1/64 | 0 cells | - |

##### unused_profile

| Type | Egress Queue | Threshold | Reserved | Drop-Precedence |
| ---- | ------------ | --------- | -------- | --------------- |
| Unicast | 1 | - | 0 bytes | - |
| Unicast | 2 | 1/8 | 0 cells | - |
| Unicast | 7 | - | - bytes | - |
| Multicast | 0 | - | 0 bytes | - |
| Multicast | 1 | 8 | 0 cells | - |

#### Platform Sand Summary

| Settings | Value |
| -------- | ----- |
| Forwarding Mode | arad |
| Hardware Only Lag | True |
| Lag Mode | 512x32 |
| Default Multicast Replication | ingress |

##### Internal Network QOS Mapping

| Traffic Class | To Network QOS |
| ------------- | -------------- |
| 0 | 0 |
| 1 | 7 |
| 2 | 15 |

#### Platform Software Forwarding Engine Summary

| Settings | Value |
| -------- | ----- |
| Maximum CPU Allocation | 42 |

### Platform Device Configuration

```eos
!
platform trident l3 routing mac-address per-vlan
platform trident forwarding-table partition 2
platform sand forwarding mode arad
platform sand lag mode 512x32
platform sand lag hardware-only
platform sand qos map traffic-class 0 to network-qos 0
platform sand qos map traffic-class 1 to network-qos 7
platform sand qos map traffic-class 2 to network-qos 15
platform sand multicast replication default ingress
platform sand mdb profile l3-xxl
platform sfe data-plane cpu allocation maximum 42
```

## Application Traffic Recognition

### Applications

#### IPv4 Applications

| Name | Source Prefix | Destination Prefix | Protocols | Protocol Ranges | TCP Source Port Set | TCP Destination Port Set | UDP Source Port Set | UDP Destination Port Set | DSCP |
| ---- | ------------- | ------------------ | --------- | --------------- | ------------------- | ------------------------ | ------------------- | ------------------------ | ---- |
| empty-application | - | - | - | - | - | - | - | - | - |
| empty-protocols | - | - | - | 21 | - | - | - | - | - |
| user_defined_app1 | src_prefix_set1 | dest_prefix_set1 | udp, tcp | 25 | src_port_set1 | dest_port_set1 | src_port_set2 | dest_port_set2 | 12-19 af43 af41 ef 1-4,6 32-33,34-35 11 56-57, 58 59-60, 61-62 |
| user_defined_app2 | src_prefix_set2 | dest_prefix_set2 | pim, icmp, tcp | 21, 7-11 | - | - | - | - | ef 1-42 cs1 |
| user_defined_app11 | src_prefix_set1 | dest_prefix_set1 | udp, tcp | 25 | src_port_set1 | dest_port_set1 | - | - | 12-19 af43 af41 ef 1-4,6 32-33,34-35 11 56-57, 58 59-60, 61-62 |

#### Layer 4 Applications

| Name | Protocols | Protocol Ranges | TCP Source Port Set | TCP Destination Port Set | UDP Source Port Set | UDP Destination Port Set |
| ---- | --------- | --------------- | ------------------- | ------------------------ | ------------------- | ------------------------ |
| l4-app-1 | tcp, udp | - | src_port_set1 | dest_port_set1 | src_port_set1 | dest_port_set1 |
| l4-app-2 | tcp | 27, 41-44 | - | - | - | - |
| l4-app-11 | tcp, udp | - | src_port_set1 | dest_port_set1 | - | - |

### Application Profiles

#### Application Profile Name app_profile_1

| Type | Name | Service |
| ---- | ---- | ------- |
| application | aim | audio-video |
| application | aim | chat |
| application | user_defined_app1 | - |
| category | best-effort | - |
| category | category1 | audio-video |
| transport | http | - |
| transport | udp | - |

#### Application Profile Name app_profile_2

| Type | Name | Service |
| ---- | ---- | ------- |
| application | aim | audio-video |
| application | user_defined_app2 | - |
| category | category1 | chat |
| transport | https | - |
| transport | quic | - |

### Categories

| Category | Application(Service) |
| -------- | -------------------- |
| best-effort | aimini(peer-to-peer)<br>apple_update(software-update) |
| category1 | aim(audio-video)<br>aim(chat)<br>anydesk |
| empty |  |

### Router Application-Traffic-Recognition Device Configuration

```eos
!
application traffic recognition
   !
   application ipv4 empty-application
   !
   application ipv4 empty-protocols
      protocol 21
   !
   application ipv4 user_defined_app1
      source prefix field-set src_prefix_set1
      destination prefix field-set dest_prefix_set1
      protocol tcp source port field-set src_port_set1 destination port field-set dest_port_set1
      protocol udp source port field-set src_port_set2 destination port field-set dest_port_set2
      protocol 25
      dscp 12-19 af43 af41 ef 1-4,6 32-33,34-35 11 56-57, 58 59-60, 61-62
   !
   application ipv4 user_defined_app2
      source prefix field-set src_prefix_set2
      destination prefix field-set dest_prefix_set2
      protocol icmp
      protocol pim
      protocol tcp
      protocol 7-11, 21
      dscp ef 1-42 cs1
   !
   application ipv4 user_defined_app11
      source prefix field-set src_prefix_set1
      destination prefix field-set dest_prefix_set1
      protocol tcp source port field-set src_port_set1 destination port field-set dest_port_set1
      protocol udp
      protocol 25
      dscp 12-19 af43 af41 ef 1-4,6 32-33,34-35 11 56-57, 58 59-60, 61-62
   !
   application l4 l4-app-1
      protocol tcp source port field-set src_port_set1 destination port field-set dest_port_set1
      protocol udp source port field-set src_port_set1 destination port field-set dest_port_set1
   !
   application l4 l4-app-2
      protocol tcp
      protocol 27, 41-44
   !
   application l4 l4-app-11
      protocol tcp source port field-set src_port_set1 destination port field-set dest_port_set1
      protocol udp
   !
   category best-effort
      application aimini service peer-to-peer
      application apple_update service software-update
   !
   category category1
      application aim service audio-video
      application aim service chat
      application anydesk
   !
   category empty
   !
   application-profile app_profile_1
      application aim service audio-video
      application aim service chat
      application user_defined_app1
      application http transport
      application udp transport
      category best-effort
      category category1 service audio-video
   !
   application-profile app_profile_2
      application aim service audio-video
      application user_defined_app2
      application https transport
      application quic transport
      category category1 service chat
```

## Group-Based Multi-domain Segmentation Services (MSS-Group)

MSS-G is enabled.

### Segmentation Policies

#### POLICY-TEST1

| Sequence Number | Application Name | Action | Next-Hop | Log | Stateless |
| --------------- | ---------------- | ------ | -------- | --- | --------- |
| 10 | APP-TEST-1 | forward | - | - | False |
| 20 | APP-TEST-2 | drop | - | True | - |
| 25 | APP-TEST-3 | redirect | 198.51.100.1 | - | - |

### Segment Definitions

#### VRF default Segmentation

##### Segment SEGMENT-TEST1 Definitions

| Interface | Match-List Name | Covered Prefix-List Name | Address Family |
| --------- |---------------- | ------------------------ | -------------- |
| - | MATCH-LIST10 | - | ipv4 |
| - | MATCH-LIST11 | - | ipv6 |

##### Segment SEGMENT-TEST1 Policies

| Source Segment | Policy Applied |
| -------------- | -------------- |
| MATCH-LIST22 | POLICY-TEST1 |

##### Segment SEGMENT-TEST2 Definitions

| Interface | Match-List Name | Covered Prefix-List Name | Address Family |
| --------- |---------------- | ------------------------ | -------------- |
| - | MATCH-LIST4 | - | ipv4 |
| - | MATCH-LIST3 | - | ipv6 |

##### Segment SEGMENT-TEST2 Policies

| Source Segment | Policy Applied |
| -------------- | -------------- |
| MATCH-LIST20 | policy-forward-all |
| MATCH-LIST21 | POLICY-TEST1 |
| MATCH-LIST30 | policy-drop-all |

#### VRF SECURE Segmentation

##### Segment SEGMENT-TEST1 Definitions

| Interface | Match-List Name | Covered Prefix-List Name | Address Family |
| --------- |---------------- | ------------------------ | -------------- |
| Ethernet1 | - | - | - |
| Ethernet2 | - | - | - |
| - | - | PREFIX-LIST10 | ipv4 |
| - | - | PREFIX-LIST1 | ipv6 |

##### Segment SEGMENT-TEST1 Policies

| Source Segment | Policy Applied |
| -------------- | -------------- |
| MATCH-LIST20 | policy-forward-all |
| MATCH-LIST30 | policy-drop-all |

Configured Fallback Policy: policy-custom

### Router MSS-G Device Configuration

```eos
!
router segment-security
   no shutdown
   !
   policy POLICY-TEST1
      10 application APP-TEST-1 action forward
      20 application APP-TEST-2 action drop stateless log
      25 application APP-TEST-3 action redirect next-hop 198.51.100.1 stateless
   !
   vrf default
      segment SEGMENT-TEST1
         definition
            match prefix-ipv4 MATCH-LIST10
            match prefix-ipv6 MATCH-LIST11
         !
         policies
            from MATCH-LIST22 policy POLICY-TEST1
      !
      segment SEGMENT-TEST2
         definition
            match prefix-ipv4 MATCH-LIST4
            match prefix-ipv6 MATCH-LIST3
         !
         policies
            from MATCH-LIST20 policy policy-forward-all
            from MATCH-LIST21 policy POLICY-TEST1
            from MATCH-LIST30 policy policy-drop-all
   !
   vrf SECURE
      segment SEGMENT-TEST1
         definition
            match interface Ethernet1
            match interface Ethernet2
            match covered prefix-list ipv4 PREFIX-LIST10
            match covered prefix-list ipv6 PREFIX-LIST1
         !
         policies
            from MATCH-LIST20 policy policy-forward-all
            from MATCH-LIST30 policy policy-drop-all
            fallback policy policy-custom
   !
```

### Router Path-selection

#### Router Path-selection Summary

| Setting | Value |
| ------  | ----- |
| Dynamic peers source | STUN |

#### TCP MSS Ceiling Configuration

| IPV4 segment size | Direction |
| ----------------- | --------- |
| 200 | ingress |

#### Path Groups

##### Path Group PG-1

| Setting | Value |
| ------  | ----- |
| Path Group ID | 666 |
| Keepalive interval(failure threshold) | 200(3) |

###### Dynamic Peers Settings

| Setting | Value |
| ------  | ----- |
| IP Local | True |
| IPSec | True |

###### Static Peers

| Router IP | Name | IPv4 address(es) |
| --------- | ---- | ---------------- |
| 172.16.1.42 | - | - |
| 172.16.2.42 | - | 192.168.2.42 |
| 172.16.42.42 | TEST-STATIC-PEER-WITH-NAME | 192.168.42.42<br>192.168.1.42 |

##### Path Group PG-2

| Setting | Value |
| ------  | ----- |
| Path Group ID | 42 |
| IPSec profile | IPSEC-P-1 |
| Keepalive interval | auto |
| Flow assignment | LAN |

###### Local Interfaces

| Interface name | Public address | STUN server profile(s) |
| -------------- | -------------- | ---------------------- |
| Ethernet1/1 | - |  |
| Ethernet1/1/3 | - |  |
| Ethernet2 | 192.168.42.42 | STUN-P-1<br>STUN-P-2 |
| Ethernet2/4.666 | - |  |
| Ethernet3 | - | STUN-P-1 |
| Ethernet4.666 | - |  |
| Port-Channel1 | 192.168.42.43 | STUN-P-1<br>STUN-P-2 |
| Port-Channel4.666 | - |  |

###### Local IPs

| IP address | Public address | STUN server profile(s) |
| ---------- | -------------- | ---------------------- |
| 192.168.1.100 | 192.168.42.42 | STUN-P-1<br>STUN-P-2 |
| 192.168.100.1 | - | STUN-P-1 |

###### Dynamic Peers Settings

| Setting | Value |
| ------  | ----- |
| IP Local | - |
| IPSec | False |

##### Path Group PG-3

| Setting | Value |
| ------  | ----- |
| Path Group ID | 888 |

##### Path Group PG-4

| Setting | Value |
| ------  | ----- |
| Path Group ID | - |

#### Load-balance Policies

| Policy Name | Jitter (ms) | Latency (ms) | Loss Rate (%) | Path Groups (priority) | Lowest Hop Count |
| ----------- | ----------- | ------------ | ------------- | ---------------------- | ---------------- |
| LB-EMPTY | - | - | - |  | False |
| LB-P-1 | - | - | 17 | PG-5 (1)<br>PG-2 (42)<br>PG-4 (42)<br>PG-3 (666) | True |
| LB-P-2 | 666 | 42 | 42.42 | PG-1 (1)<br>PG-3 (1) | False |

#### DPS Policies

##### DPS Policy DPS-P-1

| Rule ID | Application profile | Load-balance policy |
| ------- | ------------------- | ------------------- |
| Default Match | - | LB-P-1 |
| 42 | AP-3 | LB-P-1 |

##### DPS Policy DPS-P-2

| Rule ID | Application profile | Load-balance policy |
| ------- | ------------------- | ------------------- |
| Default Match | - | LB-P-2 |

##### DPS Policy DPS-P-3

| Rule ID | Application profile | Load-balance policy |
| ------- | ------------------- | ------------------- |
| 42 | AP-2 | - |
| 66 | AP-1 | LB-P-1 |

#### VRFs Configuration

| VRF name | DPS policy |
| -------- | ---------- |
| VRF-1 | DPS-P-1 |
| VRF-2 | DPS-P-2 |
| VRF-3 | - |

#### Router Path-selection Device Configuration

```eos
!
router path-selection
   peer dynamic source stun
   tcp mss ceiling ipv4 200 ingress
   !
   path-group PG-1 id 666
      keepalive interval 200 milliseconds failure-threshold 3 intervals
      !
      peer dynamic
         ip local
         ipsec
      !
      peer static router-ip 172.16.1.42
      !
      peer static router-ip 172.16.2.42
         ipv4 address 192.168.2.42
      !
      peer static router-ip 172.16.42.42
         name TEST-STATIC-PEER-WITH-NAME
         ipv4 address 192.168.42.42
         ipv4 address 192.168.1.42
   !
   path-group PG-2 id 42
      ipsec profile IPSEC-P-1
      keepalive interval auto
      flow assignment lan
      !
      local interface Ethernet1/1
      !
      local interface Ethernet1/1/3
      !
      local interface Ethernet2 public address 192.168.42.42
         stun server-profile STUN-P-1 STUN-P-2
      !
      local interface Ethernet2/4.666
      !
      local interface Ethernet3
         stun server-profile STUN-P-1
      !
      local interface Ethernet4.666
      !
      local interface Port-Channel1 public address 192.168.42.43
         stun server-profile STUN-P-1 STUN-P-2
      !
      local interface Port-Channel4.666
      !
      local ip 192.168.1.100 public address 192.168.42.42
         stun server-profile STUN-P-1 STUN-P-2
      !
      local ip 192.168.100.1
         stun server-profile STUN-P-1
      !
      peer dynamic
         ipsec disabled
   !
   path-group PG-3 id 888
   !
   path-group PG-4
   !
   load-balance policy LB-EMPTY
   !
   load-balance policy LB-P-1
      loss-rate 17
      hop count lowest
      path-group PG-5
      path-group PG-2 priority 42
      path-group PG-4 priority 42
      path-group PG-3 priority 666
   !
   load-balance policy LB-P-2
      latency 42
      jitter 666
      loss-rate 42.42
      path-group PG-1 priority 1
      path-group PG-3
   !
   policy DPS-P-1
      default-match
         load-balance LB-P-1
      !
      42 application-profile AP-3
         load-balance LB-P-1
   !
   policy DPS-P-2
      default-match
         load-balance LB-P-2
   !
   policy DPS-P-3
      42 application-profile AP-2
      !
      66 application-profile AP-1
         load-balance LB-P-1
   !
   vrf VRF-1
      path-selection-policy DPS-P-1
   !
   vrf VRF-2
      path-selection-policy DPS-P-2
   !
   vrf VRF-3
```

## IP NAT

### NAT Profiles

#### Profile: NAT-PROFILE-NO-VRF-1

#### Profile: NAT-PROFILE-NO-VRF-2

##### IP NAT: Source Static

| Direction | Original IP | Original Port | Access List | Translated IP | Translated Port | Protocol | Group | Priority | Comment |
| --------- | ----------- | ------------- | ----------- | ------------- | --------------- | -------- | ----- | -------- | ------- |
| - | 3.0.0.1 | - | - | 4.0.0.1 | - | - | - | 0 | - |
| - | 3.0.0.2 | 22 | - | 4.0.0.2 | - | - | - | 0 | - |
| - | 3.0.0.3 | 22 | - | 4.0.0.3 | 23 | - | - | 0 | - |
| - | 3.0.0.4 | 22 | - | 4.0.0.4 | 23 | UDP | - | 0 | - |
| - | 3.0.0.5 | 22 | - | 4.0.0.5 | 23 | TCP | 1 | 0 | - |
| - | 3.0.0.6 | 22 | - | 4.0.0.6 | 23 | TCP | 2 | 5 | Comment Test |
| - | 3.0.0.7 | - | ACL21 | 4.0.0.7 | - | - | - | 0 | - |
| ingress | 3.0.0.8 | - | - | 4.0.0.8 | - | - | - | 0 | - |

##### IP NAT: Source Dynamic

| Access List | NAT Type | Pool Name | Priority | Comment |
| ----------- | -------- | --------- | -------- | ------- |
| ACL11 | pool | POOL11 | 0 | - |
| ACL12 | pool | POOL11 | 0 | POOL11 shared with ACL11/12 |
| ACL13 | pool | POOL13 | 10 | - |
| ACL14 | pool | POOL14 | 1 | Priority low end |
| ACL15 | pool | POOL15 | 4294967295 | Priority high end |
| ACL16 | pool | POOL16 | 0 | Priority default |
| ACL17 | overload | - | 10 | Priority_10 |
| ACL18 | pool-address-only | POOL18 | 10 | Priority_10 |
| ACL19 | pool-full-cone | POOL19 | 10 | Priority_10 |

##### IP NAT: Destination Static

| Direction | Original IP | Original Port | Access List | Translated IP | Translated Port | Protocol | Group | Priority | Comment |
| --------- | ----------- | ------------- | ----------- | ------------- | --------------- | -------- | ----- | -------- | ------- |
| - | 1.0.0.1 | - | - | 2.0.0.1 | - | - | - | 0 | - |
| - | 1.0.0.2 | 22 | - | 2.0.0.2 | - | - | - | 0 | - |
| - | 1.0.0.2 | 23 | - | 2.0.0.3 | 23 | - | - | 0 | - |
| - | 1.0.0.4 | 22 | - | 2.0.0.4 | 23 | udp | - | 0 | - |
| - | 1.0.0.5 | 22 | - | 2.0.0.5 | 23 | tcp | 1 | 0 | - |
| - | 1.0.0.6 | 22 | - | 2.0.0.6 | 23 | tcp | 2 | 5 | Comment Test |
| - | 1.0.0.7 | - | ACL21 | 2.0.0.7 | - | - | - | 0 | - |
| egress | 239.0.0.1 | - | - | 239.0.0.2 | - | - | - | 0 | - |

##### IP NAT: Destination Dynamic

| Access List | Pool Name | Priority | Comment |
| ----------- | --------- | -------- | ------- |
| ACL1 | POOL1 | 0 | - |
| ACL2 | POOL1 | 0 | POOL1 shared with ACL1/2 |
| ACL3 | POOL3 | 10 | - |
| ACL4 | POOL4 | 1 | Priority low end |
| ACL5 | POOL5 | 4294967295 | Priority high end |
| ACL6 | POOL6 | 0 | Priority default |

#### Profile: NAT-PROFILE-TEST-VRF

NAT profile VRF is: TEST

### NAT Pools

| Pool Name | Pool Type | Prefix Length | Utilization Log Threshold | First-Last IP Addresses | First-Last Ports |
| --------- | --------- | ------------- | ------------------------- | ----------------------- | ---------------- |
| port_only_1 | port-only | - | - | - | - |
| port_only_2 | port-only | - | - | - | 1024-65535 |

### NAT Synchronization

| Setting | Value |
| -------- | ----- |
| State | Enabled |
| Port Range Split | Enabled |

### NAT Translation Settings

| Setting | Value |
| -------- | ----- |
| Address Selection | Any |

### IP NAT Device Configuration

```eos
!
ip nat translation address selection any
!
ip nat profile NAT-PROFILE-NO-VRF-1
!
ip nat profile NAT-PROFILE-NO-VRF-2
   ip nat destination static 1.0.0.1 2.0.0.1
   ip nat destination static 1.0.0.2 22 2.0.0.2
   ip nat destination static 1.0.0.2 23 2.0.0.3 23
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
ip nat profile NAT-PROFILE-TEST-VRF vrf TEST
!
ip nat pool port_only_1 port-only
ip nat pool port_only_2 port-only
   port range 1024 65535
```

## Errdisable

### Errdisable Summary

|  Detect Cause | Enabled |
| ------------- | ------- |
| dot1x | True |
| xcvr-misconfigured | True |
| xcvr-overheat | True |
| xcvr-power-unsupported | True |

|  Detect Cause | Enabled | Interval |
| ------------- | ------- | -------- |
| speed-misconfigured | True | 300 |
| xcvr-misconfigured | True | 300 |
| xcvr-overheat | True | 300 |
| xcvr-power-unsupported | True | 300 |
| xcvr-unsupported | True | 300 |

```eos
!
errdisable detect cause dot1x
errdisable detect cause xcvr-misconfigured
errdisable detect cause xcvr-overheat
errdisable detect cause xcvr-power-unsupported
errdisable recovery cause speed-misconfigured
errdisable recovery cause xcvr-misconfigured
errdisable recovery cause xcvr-overheat
errdisable recovery cause xcvr-power-unsupported
errdisable recovery cause xcvr-unsupported
errdisable recovery interval 300
```

### Traffic Policies information

#### Traffic Policies Device Configuration

```eos
!
traffic-policies
   counter interface per-interface ingress
   !
```

## Quality Of Service

### QOS

#### QOS Summary

QOS rewrite DSCP: **enabled**

QOS random-detect ECN is set to allow **non-ect** **chip-based**

##### QOS Mappings

| DSCP to Traffic Class mappings |
| ------------------------------ |
| 8 9 10 11 12 13 14 15 16 17 19 21 23 24 25 27 29 31 32 33 35 37 39 40 41 42 43 44 45 47 49 50 51 52 53 54 55 57 58 59 60 61 62 63 to traffic-class 1 |
| 18 20 22 26 28 30 34 36 38 to traffic-class 4 drop-precedence 2 |
| 46 to traffic-class 5 |

| EXP to Traffic Class mappings |
| ----------------------------- |
| 0 to traffic-class 0 |

| Traffic Class to DSCP or COS mappings |
| ------------------------------------- |
| 1 to dscp 56 |
| 2 4 5 to cos 7 |
| 6 to tx-queue 2 |

#### QOS Device Configuration

```eos
!
qos rewrite dscp
qos map dscp 8 9 10 11 12 13 14 15 16 17 19 21 23 24 25 27 29 31 32 33 35 37 39 40 41 42 43 44 45 47 49 50 51 52 53 54 55 57 58 59 60 61 62 63 to traffic-class 1
qos map dscp 18 20 22 26 28 30 34 36 38 to traffic-class 4 drop-precedence 2
qos map dscp 46 to traffic-class 5
qos map traffic-class 1 to dscp 56
qos map traffic-class 2 4 5 to cos 7
qos map traffic-class 6 to tx-queue 2
qos map exp 0 to traffic-class 0
!
qos random-detect ecn allow non-ect chip-based
```

### QOS Class Maps

#### QOS Class Maps Summary

| Name | Field | Value |
| ---- | ----- | ----- |
| CM_IPv6_ACCESS_GROUP | - | - |
| CM_REPLICATION_LD | acl | ACL_REPLICATION_LD |
| CM_REPLICATION_LD2 | vlan | 200 |
| CM_REPLICATION_LD3 | cos | 3 |
| cmap_tc0_v4 | acl | acl_qos_tc0_v4 |
| cmap_tc0_v6 | - | - |
| cmap_tc5_v4 | acl | acl_qos_tc5_v4 |
| cmap_tc5_v6 | - | - |
| COS_RANGE | vlan | 1-3 |
| VLAN_RANGE | vlan | 200-400 |

#### Class-maps Device Configuration

```eos
!
class-map type qos match-any CM_IPv6_ACCESS_GROUP
   match ipv6 access-group ACL_REPLICATION_LD
!
class-map type qos match-any CM_REPLICATION_LD
   match ip access-group ACL_REPLICATION_LD
!
class-map type qos match-any CM_REPLICATION_LD2
   match vlan 200
!
class-map type qos match-any CM_REPLICATION_LD3
   match cos 3
!
class-map type qos match-any cmap_tc0_v4
   match ip access-group acl_qos_tc0_v4
!
class-map type qos match-any cmap_tc0_v6
   match ipv6 access-group acl_qos_tc0_v6
!
class-map type qos match-any cmap_tc5_v4
   match ip access-group acl_qos_tc5_v4
!
class-map type qos match-any cmap_tc5_v6
   match ipv6 access-group acl_qos_tc5_v6
!
class-map type qos match-any COS_RANGE
   match vlan 1-3
!
class-map type qos match-any VLAN_RANGE
   match vlan 200-400
```

### QOS Policy Maps

#### QOS Policy Maps Summary

##### PM_REPLICATION_LD

| Class Name | COS | DSCP | Traffic Class | Drop Precedence | Police Rate (Burst) -> Action |
| ---------- | --- | -----| ------------- | --------------- | ----------------------------- |
| CM_REPLICATION_LD | - | - | - | 1 | 10 kbps (260 kbytes) -> drop-precedence<br> 30 kbps(270 kbytes) -> drop |

##### PM_REPLICATION_LD2

| Class Name | COS | DSCP | Traffic Class | Drop Precedence | Police Rate (Burst) -> Action |
| ---------- | --- | -----| ------------- | --------------- | ----------------------------- |
| CM_REPLICATION_LD | - | - | - | - | 30 kbps (280 bytes) -> dscp<br> 1 mbps(270 bytes) -> drop |

##### PM_REPLICATION_LD3

| Class Name | COS | DSCP | Traffic Class | Drop Precedence | Police Rate (Burst) -> Action |
| ---------- | --- | -----| ------------- | --------------- | ----------------------------- |
| CM_REPLICATION_LD | - | - | - | - | 10000 bps (260 kbytes) -> drop |

#### QOS Policy Maps Device Configuration

```eos
!
policy-map type quality-of-service PM_REPLICATION_LD
   class CM_REPLICATION_LD
      set drop-precedence 1
      police rate 10 kbps burst-size 260 kbytes action set drop-precedence rate 30 kbps burst-size 270 kbytes
!
policy-map type quality-of-service PM_REPLICATION_LD2
   class CM_REPLICATION_LD
      police rate 30 kbps burst-size 280 bytes action set dscp af11 rate 1 mbps burst-size 270 bytes
!
policy-map type quality-of-service PM_REPLICATION_LD3
   class CM_REPLICATION_LD
      police rate 10000 bps burst-size 260 kbytes
```

### QOS Profiles

#### QOS Profiles Summary

##### QOS Profile: **experiment**

###### Settings

| Default COS | Default DSCP | Trust | Shape Rate | QOS Service Policy |
| ----------- | ------------ | ----- | ---------- | ------------------ |
| - | - | - | - | - |

###### TX Queues

| TX queue | Type | Bandwidth | Priority | Shape Rate | Comment |
| -------- | ---- | --------- | -------- | ---------- | ------- |
| 3 | All | 30 | no priority | - | - |
| 4 | All | 10 | - | - | - |
| 5 | All | 40 | - | - | - |
| 7 | All | 30 | - | 40 percent | - |

##### QOS Profile: **qprof_testwithpolicy**

###### Settings

| Default COS | Default DSCP | Trust | Shape Rate | QOS Service Policy |
| ----------- | ------------ | ----- | ---------- | ------------------ |
| - | - | - | - | - |

###### TX Queues

| TX queue | Type | Bandwidth | Priority | Shape Rate | Comment |
| -------- | ---- | --------- | -------- | ---------- | ------- |
| 0 | All | 1 | - | - | - |
| 1 | All | 80 | - | - | - |
| 5 | All | 19 | no priority | - | Multi-line comment<br>here. |

##### QOS Profile: **test**

###### Settings

| Default COS | Default DSCP | Trust | Shape Rate | QOS Service Policy |
| ----------- | ------------ | ----- | ---------- | ------------------ |
| - | - | - | - | - |

###### TX Queues

| TX queue | Type | Bandwidth | Priority | Shape Rate | Comment |
| -------- | ---- | --------- | -------- | ---------- | ------- |
| 1 | All | 50 | no priority | - | - |
| 2 | All | 10 | priority strict | - | - |
| 4 | All | 10 | - | - | - |

###### ECN Configuration

| TX queue | Type | Min Threshold | Max Threshold | Max Mark Probability |
| -------- | ---- | ------------- | ------------- | -------------------- |
| 1 | All | -  | -  | - |
| 2 | All | 320 kbytes | 320 kbytes | 90 |
| 4 | All | 320 segments | 320 segments | - |

##### QOS Profile: **test_with_pfc**

###### Settings

| Default COS | Default DSCP | Trust | Shape Rate | QOS Service Policy |
| ----------- | ------------ | ----- | ---------- | ------------------ |
| - | - | - | - | - |

###### TX Queues

| TX queue | Type | Bandwidth | Priority | Shape Rate | Comment |
| -------- | ---- | --------- | -------- | ---------- | ------- |
| 0 | All | 1 | - | - | - |
| 1 | All | 80 | - | - | - |
| 5 | All | 19 | no priority | - | - |

###### Priority Flow Control

Priority Flow Control is **enabled**.

| Priority | Action |
| -------- | ------ |
| 0 | no-drop |
| 1 | drop |

###### Priority Flow Control Watchdog Settings

| Enabled | Action | Timeout | Recovery | Polling |
| ------- | ------ | ------- | -------- | ------- |
| True | drop | 0.05 | 1.11 | auto |

##### QOS Profile: **uc_mc_queues_test**

###### Settings

| Default COS | Default DSCP | Trust | Shape Rate | QOS Service Policy |
| ----------- | ------------ | ----- | ---------- | ------------------ |
| - | - | - | - | - |

###### TX Queues

| TX queue | Type | Bandwidth | Priority | Shape Rate | Comment |
| -------- | ---- | --------- | -------- | ---------- | ------- |
| 1 | Unicast | 50 | no priority | - | Test no priority |
| 2 | Unicast | 10 | priority strict | - | - |
| 4 | Unicast | 10 | - | - | Test guaranteed percent |
| 1 | Multicast | 50 | no priority | - | - |
| 2 | Multicast | 10 | priority strict | - | Test strict priority |
| 4 | Multicast | 10 | - | - | Test guaranteed percent |

###### ECN Configuration

| TX queue | Type | Min Threshold | Max Threshold | Max Mark Probability |
| -------- | ---- | ------------- | ------------- | -------------------- |
| 1 | Unicast | 3 milliseconds | 9 milliseconds | 90 |
| 2 | Unicast | 320 kbytes | 320 kbytes | 90 |
| 4 | Unicast | 320 segments | 320 segments | - |
| 1 | Multicast | - | - | - |
| 2 | Multicast | - | - | - |
| 4 | Multicast | - | - | - |

##### QOS Profile: **wred_queues_test**

###### Settings

| Default COS | Default DSCP | Trust | Shape Rate | QOS Service Policy |
| ----------- | ------------ | ----- | ---------- | ------------------ |
| - | - | - | - | - |

###### TX Queues

| TX queue | Type | Bandwidth | Priority | Shape Rate | Comment |
| -------- | ---- | --------- | -------- | ---------- | ------- |
| 1 | All | 50 | no priority | - | Test no priority |
| 2 | All | 10 | priority strict | - | - |
| 3 | All | 10 | priority strict | - | - |
| 4 | All | 10 | - | - | Test guaranteed percent |
| 1 | Multicast | 50 | no priority | - | - |
| 2 | Multicast | 10 | priority strict | - | Test strict priority |
| 4 | Multicast | 10 | - | - | Test guaranteed percent |

###### ECN Configuration

| TX queue | Type | Min Threshold | Max Threshold | Max Mark Probability |
| -------- | ---- | ------------- | ------------- | -------------------- |
| 1 | All | -  | -  | - |
| 2 | All | -  | -  | - |
| 3 | All | 320 kbytes | 320 kbytes | - |
| 4 | All | -  | -  | - |
| 1 | Multicast | - | - | - |
| 2 | Multicast | - | - | - |
| 4 | Multicast | - | - | - |

###### WRED Configuration

| TX queue | Type | Drop Precedence | Min Threshold | Max Threshold | Drop Probability | Weight |
| -------- | ---- | --------------- | ------------- | ------------- | ---------------- | ------ |
| 1 | All | - | 1 kbytes | 10 kbytes | 100 | - |
| 2 | All | 2 | 2 kbytes | 200 kbytes | 50 | 10 |
| 3 | All | - | -  | -  | - | - |
| 4 | All | - | 1 kbytes | 10 kbytes | 90 | - |
| 1 | Multicast | - | - | - | - | - |
| 2 | Multicast | - | - | - | - | - |
| 4 | Multicast | - | - | - | - | - |

##### QOS Profile: **wred_uc_queues_test**

###### Settings

| Default COS | Default DSCP | Trust | Shape Rate | QOS Service Policy |
| ----------- | ------------ | ----- | ---------- | ------------------ |
| - | - | - | - | - |

###### TX Queues

| TX queue | Type | Bandwidth | Priority | Shape Rate | Comment |
| -------- | ---- | --------- | -------- | ---------- | ------- |
| 1 | Unicast | 50 | no priority | - | Test no priority |
| 2 | Unicast | 10 | priority strict | - | - |
| 4 | Unicast | 10 | - | - | Test guaranteed percent |

###### WRED Configuration

| TX queue | Type | Drop Precedence | Min Threshold | Max Threshold | Drop Probability | Weight |
| -------- | ---- | --------------- | ------------- | ------------- | ---------------- | ------ |
| 1 | Unicast | - |1 microseconds | 10 microseconds | 90 | 15 |
| 2 | Unicast | 1 |2 milliseconds | 20 milliseconds | 80 | - |
| 4 | Unicast | - |1 microseconds | 10 microseconds | 90 | - |

#### QOS Profile Device Configuration

```eos
!
qos profile experiment
   !
   tx-queue 3
      no priority
      bandwidth percent 30
   !
   tx-queue 4
      bandwidth guaranteed percent 10
   !
   tx-queue 5
      bandwidth percent 40
   !
   tx-queue 7
      bandwidth percent 30
      shape rate 40 percent
!
qos profile qprof_testwithpolicy
   !
   tx-queue 0
      bandwidth percent 1
   !
   tx-queue 1
      bandwidth percent 80
   !
   tx-queue 5
      !! Multi-line comment
      !! here.
      no priority
      bandwidth percent 19
!
qos profile test
   !
   tx-queue 1
      no priority
      bandwidth percent 50
   !
   tx-queue 2
      priority strict
      bandwidth percent 10
      random-detect ecn minimum-threshold 320 kbytes maximum-threshold 320 kbytes max-mark-probability 90
   !
   tx-queue 4
      bandwidth guaranteed percent 10
      random-detect ecn minimum-threshold 320 segments maximum-threshold 320 segments weight 10
!
qos profile test_with_pfc
   !
   tx-queue 0
      bandwidth percent 1
   !
   tx-queue 1
      bandwidth percent 80
   !
   tx-queue 5
      no priority
      bandwidth percent 19
   !
   priority-flow-control on
   priority-flow-control priority 0 no-drop
   priority-flow-control priority 1 drop
   priority-flow-control pause watchdog
   priority-flow-control pause watchdog port action drop
   priority-flow-control pause watchdog port timer timeout 0.05 polling-interval auto recovery-time 1.11 forced
!
qos profile uc_mc_queues_test
   !
   uc-tx-queue 1
      !! Test no priority
      no priority
      bandwidth percent 50
      random-detect ecn minimum-threshold 3 milliseconds maximum-threshold 9 milliseconds max-mark-probability 90
   !
   uc-tx-queue 2
      priority strict
      bandwidth percent 10
      random-detect ecn minimum-threshold 320 kbytes maximum-threshold 320 kbytes max-mark-probability 90
   !
   uc-tx-queue 4
      !! Test guaranteed percent
      bandwidth guaranteed percent 10
      random-detect ecn minimum-threshold 320 segments maximum-threshold 320 segments weight 10
   !
   mc-tx-queue 1
      no priority
      bandwidth percent 50
   !
   mc-tx-queue 2
      !! Test strict priority
      priority strict
      bandwidth percent 10
   !
   mc-tx-queue 4
      !! Test guaranteed percent
      bandwidth guaranteed percent 10
!
qos profile wred_queues_test
   !
   tx-queue 1
      !! Test no priority
      no priority
      bandwidth percent 50
      random-detect drop minimum-threshold 1 kbytes maximum-threshold 10 kbytes drop-probability 100
   !
   tx-queue 2
      priority strict
      bandwidth percent 10
      random-detect drop drop-precedence 2 minimum-threshold 2 kbytes maximum-threshold 200 kbytes drop-probability 50 weight 10
   !
   tx-queue 3
      priority strict
      bandwidth percent 10
      random-detect ecn minimum-threshold 320 kbytes maximum-threshold 320 kbytes weight 10
   !
   tx-queue 4
      !! Test guaranteed percent
      bandwidth guaranteed percent 10
      random-detect drop minimum-threshold 1 kbytes maximum-threshold 10 kbytes drop-probability 90
   !
   mc-tx-queue 1
      no priority
      bandwidth percent 50
   !
   mc-tx-queue 2
      !! Test strict priority
      priority strict
      bandwidth percent 10
   !
   mc-tx-queue 4
      !! Test guaranteed percent
      bandwidth guaranteed percent 10
!
qos profile wred_uc_queues_test
   !
   uc-tx-queue 1
      !! Test no priority
      no priority
      bandwidth percent 50
      random-detect drop minimum-threshold 1 microseconds maximum-threshold 10 microseconds drop-probability 90 weight 15
   !
   uc-tx-queue 2
      priority strict
      bandwidth percent 10
      random-detect drop drop-precedence 1 minimum-threshold 2 milliseconds maximum-threshold 20 milliseconds drop-probability 80
   !
   uc-tx-queue 4
      !! Test guaranteed percent
      bandwidth guaranteed percent 10
      random-detect drop minimum-threshold 1 microseconds maximum-threshold 10 microseconds drop-probability 90
```

### Control-plane Policy Map

#### Control-plane Policy Map Summary

##### copp-system-policy

| Class | Shape | Bandwidth | Rate Unit |
| ----- | ----- | --------- | --------- |
| copp-system-cvx | 2000 | 2000 | pps |
| copp-system-OspfIsis | 1000 | 1000 | kbps |
| copp-system-rsvp | - | - | - |

#### COPP Policy Maps Device Configuration

```eos
!
policy-map type copp copp-system-policy
   class copp-system-OspfIsis
      shape kbps 1000
      bandwidth kbps 1000
   !
   class copp-system-cvx
      shape pps 2000
      bandwidth pps 2000
   !
   class copp-system-rsvp
```

### Priority Flow Control

#### Global Settings

Priority Flow Control is **Off** on all interfaces.

##### Priority Flow Control Watchdog Settings

| Action | Timeout | Recovery | Polling | Override Action Drop |
| ------ | ------- | -------- | ------- |
| no-drop | 0.05 | 1.22 | 10.001 | False |

```eos
!
priority-flow-control all off
priority-flow-control pause watchdog default timeout 0.05
priority-flow-control pause watchdog default recovery-time 1.22
priority-flow-control pause watchdog default polling-interval 10.001
priority-flow-control pause watchdog action no-drop
```
