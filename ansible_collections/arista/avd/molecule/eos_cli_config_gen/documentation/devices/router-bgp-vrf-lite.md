# router-bgp-vrf-lite

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Routing](#routing)
  - [Static Routes](#static-routes)
  - [Router BGP](#router-bgp)
- [Filters](#filters)
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)

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

### Static Routes

#### Static Routes Summary

| VRF | Destination Prefix | Next Hop IP | Exit interface | Administrative Distance | Tag | Route Name | Metric |
| --- | ------------------ | ----------- | -------------- | ----------------------- | --- | ---------- | ------ |
| BLUE-C1 | 193.1.0.0/24 | - | Null0 | 1 | - | - | - |
| BLUE-C1 | 193.1.1.0/24 | - | Null0 | 1 | - | - | - |
| BLUE-C1 | 193.1.2.0/24 | - | Null0 | 1 | - | - | - |

#### Static Routes Device Configuration

```eos
!
ip route vrf BLUE-C1 193.1.0.0/24 Null0
ip route vrf BLUE-C1 193.1.1.0/24 Null0
ip route vrf BLUE-C1 193.1.2.0/24 Null0
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65001 | 1.0.1.1 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |

#### Router BGP Listen Ranges

| Prefix | Peer-ID Include Router ID | Peer Group | Peer-Filter | Remote-AS | VRF |
| ------ | ------------------------- | ---------- | ----------- | --------- | --- |
| 10.10.10.0/24 | - | my-peer-group1 | my-peer-filter | - | YELLOW-C1 |
| 12.10.10.0/24 | True | my-peer-group3 | - | 65444 | YELLOW-C1 |
| 13.10.10.0/24 | - | my-peer-group4 | my-peer-filter | - | YELLOW-C1 |

#### Router BGP Peer Groups

##### OBS_WAN

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65000 |
| BFD | True |
| BFD Timers | interval: 2000, min_rx: 2000, multiplier: 3 |

##### SEDI

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65003 |
| Source | Loopback101 |
| Ebgp multihop | 10 |

##### SEDI-shut

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Shutdown | True |

##### TEST-PASSIVE

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65003 |
| Passive | True |

##### WELCOME_ROUTERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65001 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 10.1.1.0 | Inherited from peer group OBS_WAN | BLUE-C1 | - | - | - | - | Inherited from peer group OBS_WAN(interval: 2000, min_rx: 2000, multiplier: 3) | - | - | - | - |
| 10.255.1.1 | Inherited from peer group WELCOME_ROUTERS | BLUE-C1 | - | - | - | - | - | - | True | - | - |
| 101.0.3.1 | Inherited from peer group SEDI | BLUE-C1 | - | - | - | - | - | - | - | - | - |
| 101.0.3.2 | Inherited from peer group SEDI | BLUE-C1 | True | - | - | Allowed, allowed 3 (default) times | - | - | - | - | - |
| 101.0.3.3 | - | BLUE-C1 | Inherited from peer group SEDI-shut | - | - | Allowed, allowed 5 times | - | - | - | - | - |
| 101.0.3.4 | Inherited from peer group TEST-PASSIVE | BLUE-C1 | - | - | - | - | - | - | - | Inherited from peer group TEST-PASSIVE | - |
| 101.0.3.5 | Inherited from peer group WELCOME_ROUTERS | BLUE-C1 | - | - | - | - | False | - | - | True | - |
| 101.0.3.6 | Inherited from peer group WELCOME_ROUTERS | BLUE-C1 | - | - | - | - | True(interval: 2500, min_rx: 2000, multiplier: 3) | - | - | - | - |
| 101.0.3.7 | - | BLUE-C1 | - | - | - | - | True | - | - | - | - |
| 101.0.3.8 | - | BLUE-C1 | - | - | - | - | False | - | - | - | - |
| 10.1.1.0 | Inherited from peer group OBS_WAN | RED-C1 | - | - | - | - | Inherited from peer group OBS_WAN(interval: 2000, min_rx: 2000, multiplier: 3) | - | - | - | - |
| 10.1.1.0 | Inherited from peer group OBS_WAN | YELLOW-C1 | - | - | - | - | Inherited from peer group OBS_WAN(interval: 2000, min_rx: 2000, multiplier: 3) | - | - | - | - |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| BLUE-C1 | 1.0.1.1:101 | static<br>ospf |
| RED-C1 | 1.0.1.1:102 | - |
| YELLOW-C1 | 1.0.1.1:103 | - |

#### Router BGP Device Configuration

```eos
!
router bgp 65001
   router-id 1.0.1.1
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   neighbor OBS_WAN peer group
   neighbor OBS_WAN remote-as 65000
   neighbor OBS_WAN as-path prepend-own disabled
   neighbor OBS_WAN as-path remote-as replace out
   neighbor OBS_WAN bfd
   neighbor OBS_WAN bfd interval 2000 min-rx 2000 multiplier 3
   neighbor OBS_WAN description BGP Connection to OBS WAN CPE
   neighbor SEDI peer group
   neighbor SEDI remote-as 65003
   neighbor SEDI update-source Loopback101
   neighbor SEDI description BGP Connection to OBS WAN CPE
   neighbor SEDI ebgp-multihop 10
   neighbor SEDI-shut peer group
   neighbor SEDI-shut shutdown
   neighbor SEDI-shut description BGP Peer Shutdown
   neighbor TEST-PASSIVE peer group
   neighbor TEST-PASSIVE remote-as 65003
   neighbor TEST-PASSIVE passive
   neighbor TEST-PASSIVE description BGP Connection in passive mode
   neighbor WELCOME_ROUTERS peer group
   neighbor WELCOME_ROUTERS remote-as 65001
   neighbor WELCOME_ROUTERS description BGP Connection to WELCOME ROUTER 02
   redistribute ospf include leaked route-map RM-OSPF-TO-BGP
   redistribute static
   !
   address-family ipv4
      neighbor OBS_WAN activate
      neighbor SEDI activate
      neighbor SEDI route-map RM-BGP-EXPORT-DEFAULT-BLUE-C1 out
      neighbor SEDI-shut activate
      neighbor SEDI-shut route-map RM-BGP-EXPORT-DEFAULT-BLUE-C1 out
      neighbor WELCOME_ROUTERS activate
   !
   vrf BLUE-C1
      rd 1.0.1.1:101
      neighbor 10.1.1.0 peer group OBS_WAN
      neighbor 10.255.1.1 peer group WELCOME_ROUTERS
      neighbor 10.255.1.1 as-path remote-as replace out
      neighbor 10.255.1.1 weight 65535
      neighbor 10.255.1.1 route-reflector-client
      neighbor 101.0.3.1 peer group SEDI
      neighbor 101.0.3.1 weight 100
      neighbor 101.0.3.2 peer group SEDI
      neighbor 101.0.3.2 shutdown
      neighbor 101.0.3.2 allowas-in
      neighbor 101.0.3.3 peer group SEDI-shut
      neighbor 101.0.3.3 allowas-in 5
      neighbor 101.0.3.4 peer group TEST-PASSIVE
      neighbor 101.0.3.5 peer group WELCOME_ROUTERS
      neighbor 101.0.3.5 passive
      no neighbor 101.0.3.5 bfd
      neighbor 101.0.3.6 peer group WELCOME_ROUTERS
      neighbor 101.0.3.6 bfd
      neighbor 101.0.3.6 bfd interval 2500 min-rx 2000 multiplier 3
      neighbor 101.0.3.7 bfd
      aggregate-address 0.0.0.0/0 as-set summary-only attribute-map RM-BGP-AGG-APPLY-SET
      aggregate-address 193.1.0.0/16 as-set summary-only attribute-map RM-BGP-AGG-APPLY-SET
      redistribute ospf include leaked
      redistribute static
      !
      comment
      Comment created from eos_cli under router_bgp.vrfs.BLUE-C1
      EOF

   !
   vrf RED-C1
      rd 1.0.1.1:102
      neighbor 10.1.1.0 peer group OBS_WAN
      !
      address-family ipv4
         neighbor 10.1.1.0 prefix-list PL-BGP-DEFAULT-RED-IN-C1 in
         neighbor 10.1.1.0 prefix-list PL-BGP-DEFAULT-RED-OUT-C1 out
      !
      address-family ipv6
         neighbor 2001:cafe:192:168::4 prefix-list PL-BGP-V6-RED-IN-C1 in
         neighbor 2001:cafe:192:168::4 prefix-list PL-BGP-V6-RED-OUT-C1 out
   !
   vrf YELLOW-C1
      rd 1.0.1.1:103
      bgp listen range 10.10.10.0/24 peer-group my-peer-group1 peer-filter my-peer-filter
      bgp listen range 12.10.10.0/24 peer-id include router-id peer-group my-peer-group3 remote-as 65444
      bgp listen range 13.10.10.0/24 peer-group my-peer-group4 peer-filter my-peer-filter
      neighbor 10.1.1.0 peer group OBS_WAN
```

## Filters

### Prefix-lists

#### Prefix-lists Summary

##### PL-BGP-DEFAULT-BLUE-C1

| Sequence | Action |
| -------- | ------ |
| 10 | permit 0.0.0.0/0 le 1 |

##### PL-BGP-DEFAULT-RED-IN-C1

| Sequence | Action |
| -------- | ------ |
| 10 | permit 0.0.0.0/0 |

##### PL-BGP-DEFAULT-RED-OUT-C1

| Sequence | Action |
| -------- | ------ |
| 10 | permit 10.0.0.0/8 |

#### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-BGP-DEFAULT-BLUE-C1
   seq 10 permit 0.0.0.0/0 le 1
!
ip prefix-list PL-BGP-DEFAULT-RED-IN-C1
   seq 10 permit 0.0.0.0/0
!
ip prefix-list PL-BGP-DEFAULT-RED-OUT-C1
   seq 10 permit 10.0.0.0/8
```

### Route-maps

#### Route-maps Summary

##### RM-BGP-AGG-APPLY-SET

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | - | local-preference 50 | - | - |

##### RM-BGP-EXPORT-DEFAULT-BLUE-C1

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | ip address prefix-list PL-BGP-DEFAULT-BLUE-C1 | - | - | - |

#### Route-maps Device Configuration

```eos
!
route-map RM-BGP-AGG-APPLY-SET permit 10
   description RM for BGP AGG Set
   set local-preference 50
!
route-map RM-BGP-EXPORT-DEFAULT-BLUE-C1 permit 10
   description RM for BGP default route in BLUE-C1
   match ip address prefix-list PL-BGP-DEFAULT-BLUE-C1
```
