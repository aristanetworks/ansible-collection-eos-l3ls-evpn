# flow-tracking

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitoring](#monitoring)
  - [Flow Tracking](#flow-tracking-1)
- [Interfaces](#interfaces)
  - [DPS Interfaces](#dps-interfaces)
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

## Monitoring

### Flow Tracking

#### Flow Tracking Sampled

| Sample Size | Minimum Sample Size | Hardware Offload for IPv4 | Hardware Offload for IPv6 | Encapsulations |
| ----------- | ------------------- | ------------------------- | ------------------------- | -------------- |
| 666 | 2 | enabled | disabled | ipv4, ipv6, mpls |

##### Trackers Summary

| Tracker Name | Record Export On Inactive Timeout | Record Export On Interval | MPLS | Number of Exporters | Applied On | Table Size |
| ------------ | --------------------------------- | ------------------------- | ---- | ------------------- | ---------- | ---------- |
| T1 | 3666 | 5666 | True | 0 |  | - |
| T2 | - | - | False | 1 | Ethernet40 | 614400 |
| T3 | - | - | - | 4 | Ethernet41<br>Ethernet42<br>Port-Channel42 | 100000 |

##### Exporters Summary

| Tracker Name | Exporter Name | Collector IP/Host | Collector Port | Local Interface |
| ------------ | ------------- | ----------------- | -------------- | --------------- |
| T2 | T2-E1 | - | - | No local interface |
| T3 | T3-E1 | - | - | No local interface |
| T3 | T3-E2 | - | - | No local interface |
| T3 | T3-E3 | - | - | Management1 |
| T3 | T3-E4 | - | - | No local interface |

#### Flow Tracking Hardware

Software export of IPFIX data records enabled.

##### Trackers Summary

| Tracker Name | Record Export On Inactive Timeout | Record Export On Interval | Number of Exporters | Applied On |
| ------------ | --------------------------------- | ------------------------- | ------------------- | ---------- |
| T1 | 3666 | 5666 | 0 |  |
| T2 | - | - | 1 | Ethernet40 |
| T3 | - | - | 4 | Dps1<br>Ethernet41<br>Port-Channel42 |

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
!
flow tracking sampled
   encapsulation ipv4 ipv6 mpls
   sample 666
   hardware offload ipv4
   hardware offload threshold minimum 2 samples
   tracker T1
      record export on inactive timeout 3666
      record export on interval 5666
      record export mpls
   !
   tracker T2
      flow table size 614400 entries
      exporter T2-E1
         collector 42.42.42.42
   !
   tracker T3
      flow table size 100000 entries
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
   no shutdown
```

## Interfaces

### DPS Interfaces

#### DPS Interfaces Summary

| Interface | IP address | Shutdown | MTU | Flow tracker(s) | TCP MSS Ceiling |
| --------- | ---------- | -------- | --- | --------------- | --------------- |
| Dps1 | - | - | - | Hardware: T3 |  |

#### DPS Interfaces Device Configuration

```eos
!
interface Dps1
   flow tracker hardware T3
```

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet40 | - | - | - | - | - | - |
| Ethernet41 | - | - | - | - | - | - |
| Ethernet42 | - | - | - | - | - | - |

*Inherited from Port-Channel Interface

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet40
   switchport
   flow tracker hardware T2
   flow tracker sampled T2
!
interface Ethernet41
   switchport
   flow tracker hardware T3
   flow tracker sampled T3
!
interface Ethernet42
   switchport
   flow tracker sampled T3
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel42 | - | - | - | - | - | - | - | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel42
   switchport
   flow tracker hardware T3
   flow tracker sampled T3
```
