# router-bgp-asdot

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Routing](#routing)
  - [Router BGP](#router-bgp)

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

### Router BGP

ASN Notation: asdot

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65101.1234 | 192.168.255.3 |

| BGP Tuning |
| ---------- |
| graceful-restart restart-time 555 |
| graceful-restart stalepath-time 666 |
| graceful-restart |
| graceful-restart-helper restart-time 888 |
| bgp bestpath d-path |
| update wait-for-convergence |
| update wait-install |
| no bgp default ipv4-unicast |
| no bgp default ipv4-unicast transport ipv6 |
| distance bgp 20 200 200 |
| maximum-paths 32 ecmp 32 |
| bgp route-reflector preserve-attributes always |

#### Router BGP Listen Ranges

| Prefix | Peer-ID Include Router ID | Peer Group | Peer-Filter | Remote-AS | VRF |
| ------ | ------------------------- | ---------- | ----------- | --------- | --- |
| 10.10.10.0/24 | - | my-peer-group1 | my-peer-filter | - | default |
| 12.10.10.0/24 | True | my-peer-group3 | - | 65444.12 | default |
| 13.10.10.0/24 | - | my-peer-group4 | my-peer-filter | - | default |

#### Router BGP Peer Groups

##### TEST

| Settings | Value |
| -------- | ----- |
| TTL Max Hops | 42 |

##### test-link-bandwidth1

| Settings | Value |
| -------- | ----- |
| TTL Max Hops | 1 |
| Link-Bandwidth | default 100G |

##### test-link-bandwidth2

| Settings | Value |
| -------- | ----- |
| Link-Bandwidth | enabled |

##### test-passive

| Settings | Value |
| -------- | ----- |
| Passive | True |

##### test-session-tracker

| Settings | Value |
| -------- | ----- |
| Session tracker | ST2 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 192.0.3.1 | 65432.12 | default | - | all | - | - | True(interval: 2000, min_rx: 2000, multiplier: 3) | True | - | True | - |
| 192.0.3.2 | 65433.12 | default | - | extended | 10000 | - | False | True (All) | - | - | - |
| 192.0.3.3 | 65434.12 | default | - | standard | - | - | - | True | - | - | - |
| 192.0.3.4 | 65435.12 | default | - | large | - | - | - | False | - | - | 1 |
| 192.0.3.5 | 65436.12 | default | - | standard | 12000 | - | - | - | - | - | - |
| 192.0.3.6 | 65437.12 | default | - | - | - | - | - | - | False | - | - |
| 192.0.3.7 | 65438.12 | default | - | - | - | - | - | - | True | - | - |
| 192.0.3.8 | 65438.12 | default | - | - | - | - | True | - | - | - | Inherited from peer group TEST |
| 192.0.3.9 | 65438.12 | default | - | - | - | - | False | - | - | - | Inherited from peer group TEST |

#### BGP Neighbor Interfaces

| Neighbor Interface | VRF | Peer Group | Remote AS | Peer Filter |
| ------------------ | --- | ---------- | --------- | ----------- |
| Ethernet2 | default | PG-FOO-v4 | 65102.12 | - |
| Ethernet3 | default | PG-FOO-v4 | - | PF-BAR-v4 |

#### BGP Route Aggregation

| Prefix | AS Set | Advertise Map | Supress Map | Summary Only | Attribute Map | Match Map | Advertise Only |
| ------ | ------ | ------------- | ----------- | ------------ | ------------- | --------- | -------------- |
| 1.1.1.0/24 | False | - | - | False | - | - | True |
| 1.12.1.0/24 | True | ADV-MAP | SUP-MAP | True | RM-ATTRIBUTE | RM-MATCH | True |
| 2.2.1.0/24 | False | - | - | False | - | - | False |

#### Router BGP Session Trackers

| Session Tracker Name | Recovery Delay (in seconds) |
| -------------------- | --------------------------- |
| ST1 | 666 |
| ST2 | 42 |

#### Router BGP Device Configuration

```eos
!
router bgp 65101.1234
   bgp asn notation asdot
   router-id 192.168.255.3
   distance bgp 20 200 200
   graceful-restart restart-time 555
   graceful-restart stalepath-time 666
   graceful-restart
   graceful-restart-helper restart-time 888
   bgp route-reflector preserve-attributes always
   maximum-paths 32 ecmp 32
   update wait-for-convergence
   update wait-install
   no bgp default ipv4-unicast
   no bgp default ipv4-unicast transport ipv6
   bgp bestpath d-path
   bgp listen range 10.10.10.0/24 peer-group my-peer-group1 peer-filter my-peer-filter
   bgp listen range 12.10.10.0/24 peer-id include router-id peer-group my-peer-group3 remote-as 65444.12
   bgp listen range 13.10.10.0/24 peer-group my-peer-group4 peer-filter my-peer-filter
   neighbor TEST peer group
   neighbor TEST ttl maximum-hops 42
   neighbor test-link-bandwidth1 peer group
   neighbor test-link-bandwidth1 ttl maximum-hops 1
   neighbor test-link-bandwidth1 link-bandwidth default 100G
   neighbor test-link-bandwidth2 peer group
   neighbor test-link-bandwidth2 link-bandwidth
   neighbor test-passive peer group
   neighbor test-passive passive
   neighbor test-session-tracker peer group
   neighbor test-session-tracker session tracker ST2
   neighbor interface Ethernet2 peer-group PG-FOO-v4 remote-as 65102.12
   neighbor interface Ethernet3 peer-group PG-FOO-v4 peer-filter PF-BAR-v4
   neighbor 192.0.3.1 remote-as 65432.12
   neighbor 192.0.3.1 as-path remote-as replace out
   neighbor 192.0.3.1 as-path prepend-own disabled
   neighbor 192.0.3.1 bfd
   neighbor 192.0.3.1 bfd interval 2000 min-rx 2000 multiplier 3
   neighbor 192.0.3.1 rib-in pre-policy retain
   neighbor 192.0.3.1 passive
   neighbor 192.0.3.1 session tracker ST1
   neighbor 192.0.3.1 default-originate always
   neighbor 192.0.3.1 send-community
   neighbor 192.0.3.1 link-bandwidth default 100G
   neighbor 192.0.3.2 remote-as 65433.12
   neighbor 192.0.3.2 rib-in pre-policy retain all
   neighbor 192.0.3.2 default-originate route-map RM-FOO-MATCH3
   neighbor 192.0.3.2 send-community extended
   neighbor 192.0.3.2 maximum-routes 10000
   neighbor 192.0.3.2 link-bandwidth
   neighbor 192.0.3.3 remote-as 65434.12
   neighbor 192.0.3.3 rib-in pre-policy retain
   neighbor 192.0.3.3 send-community standard
   neighbor 192.0.3.4 remote-as 65435.12
   neighbor 192.0.3.4 ttl maximum-hops 1
   no neighbor 192.0.3.4 rib-in pre-policy retain
   neighbor 192.0.3.4 send-community large
   neighbor 192.0.3.5 remote-as 65436.12
   neighbor 192.0.3.5 description test_ebgp_multihop
   neighbor 192.0.3.5 ebgp-multihop 2
   neighbor 192.0.3.5 send-community standard
   neighbor 192.0.3.5 maximum-routes 12000
   neighbor 192.0.3.6 remote-as 65437.12
   neighbor 192.0.3.6 remove-private-as
   neighbor 192.0.3.6 remove-private-as ingress
   neighbor 192.0.3.6 description test_remove_private_as
   no neighbor 192.0.3.6 route-reflector-client
   neighbor 192.0.3.7 remote-as 65438.12
   neighbor 192.0.3.7 remove-private-as all replace-as
   neighbor 192.0.3.7 remove-private-as ingress replace-as
   neighbor 192.0.3.7 description test_remove_private_as_all
   neighbor 192.0.3.7 route-reflector-client
   neighbor 192.0.3.8 peer group TEST
   neighbor 192.0.3.8 remote-as 65438.12
   neighbor 192.0.3.8 bfd
   neighbor 192.0.3.9 peer group TEST
   neighbor 192.0.3.9 remote-as 65438.12
   no neighbor 192.0.3.9 bfd
   aggregate-address 1.1.1.0/24 advertise-only
   aggregate-address 1.12.1.0/24 as-set advertise-map ADV-MAP supress-map SUP-MAP summary-only attribute-map RM-ATTRIBUTE match-map RM-MATCH advertise-only
   aggregate-address 2.2.1.0/24
   redistribute bgp leaked route-map RM-REDISTRIBUTE-BGP
   redistribute ospf include leaked
   !
   address-family ipv4
      neighbor foo prefix-list PL-BAR-v4-IN in
      neighbor foo prefix-list PL-BAR-v4-OUT out
      neighbor foo default-originate route-map RM-FOO-MATCH always
      neighbor 192.0.2.1 prefix-list PL-FOO-v4-IN in
      neighbor 192.0.2.1 prefix-list PL-FOO-v4-OUT out
      network 10.0.0.0/8
      network 172.16.0.0/12
      network 192.168.0.0/16 route-map RM-FOO-MATCH
   !
   address-family ipv6
      neighbor baz prefix-list PL-BAR-v6-IN in
      neighbor baz prefix-list PL-BAR-v6-OUT out
      neighbor 2001:db8::1 prefix-list PL-FOO-v6-IN in
      neighbor 2001:db8::1 prefix-list PL-FOO-v6-OUT out
      network 2001:db8:100::/40
      network 2001:db8:200::/40 route-map RM-BAR-MATCH
      redistribute bgp leaked route-map RM-REDISTRIBUTE-BGP
      redistribute ospf include leaked
      redistribute static route-map RM-IPV6-STATIC-TO-BGP
   session tracker ST1
      recovery delay 666 seconds
   session tracker ST2
      recovery delay 42 seconds
```
