# router-bgp-evpn-vpn-import-pruning

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

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65101 | 192.168.255.3 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| graceful-restart |
| maximum-paths 2 ecmp 2 |

#### Router BGP Peer Groups

##### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Remote AS | 65001 |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 3 |
| Send community | all |
| Maximum routes | 0 (no limit) |

##### MLAG-IPv4-UNDERLAY-PEER

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Remote AS | 65101 |
| Next-hop self | True |
| Send community | all |
| Maximum routes | 12000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 192.168.255.1 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 192.168.255.2 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 10.255.251.1 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | TENANT_A_PROJECT01 | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | True | - | - | - |
| 10.255.251.1 | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | TENANT_A_PROJECT02 | - | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | Inherited from peer group MLAG-IPv4-UNDERLAY-PEER | - | - | - | - | - | - |

#### Router BGP EVPN Address Family

- VPN import pruning is **enabled**

##### EVPN Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | Encapsulation |
| ---------- | -------- | ------------ | ------------- | ------------- |
| EVPN-OVERLAY-PEERS | True |  - | - | default |
| MLAG-IPv4-UNDERLAY-PEER | False |  - | - | default |

##### EVPN Host Flapping Settings

| State | Window | Threshold | Expiry Timeout |
| ----- | ------ | --------- | -------------- |
| Enabled | 10 Seconds | 1 | - |

#### Router BGP VLAN Aware Bundles

| VLAN Aware Bundle | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute | VLANs |
| ----------------- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ | ----- |
| B-ELAN-201 | 192.168.255.3:20201 | 20201:20201 | - | - | learned | 201 |
| TENANT_A_PROJECT01 | 192.168.255.3:11 | 11:11 | - | - | learned | 110 |
| TENANT_A_PROJECT02 | 192.168.255.3:12 | 12:12 | - | - | learned | 112 |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| TENANT_A_PROJECT01 | 192.168.255.3:11 | connected<br>static<br>isis |
| TENANT_A_PROJECT02 | 192.168.255.3:12 | connected |

#### Router BGP Device Configuration

```eos
!
router bgp 65101
   router-id 192.168.255.3
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 2 ecmp 2
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS remote-as 65001
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS password 7 <removed>
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor MLAG-IPv4-UNDERLAY-PEER peer group
   neighbor MLAG-IPv4-UNDERLAY-PEER remote-as 65101
   neighbor MLAG-IPv4-UNDERLAY-PEER next-hop-self
   neighbor MLAG-IPv4-UNDERLAY-PEER route-map RM-MLAG-PEER-IN in
   neighbor MLAG-IPv4-UNDERLAY-PEER route-map RM-MLAG-PEER-OUT out
   neighbor MLAG-IPv4-UNDERLAY-PEER password 7 <removed>
   neighbor MLAG-IPv4-UNDERLAY-PEER send-community
   neighbor MLAG-IPv4-UNDERLAY-PEER maximum-routes 12000
   neighbor 192.168.255.1 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.2 peer group EVPN-OVERLAY-PEERS
   !
   vlan-aware-bundle B-ELAN-201
      rd 192.168.255.3:20201
      route-target both 20201:20201
      redistribute learned
      vlan 201
   !
   vlan-aware-bundle TENANT_A_PROJECT01
      rd 192.168.255.3:11
      route-target both 11:11
      redistribute learned
      vlan 110
   !
   vlan-aware-bundle TENANT_A_PROJECT02
      rd 192.168.255.3:12
      route-target both 12:12
      redistribute learned
      vlan 112
   !
   address-family evpn
      bgp additional-paths send ecmp limit 20
      neighbor EVPN-OVERLAY-PEERS activate
      no neighbor MLAG-IPv4-UNDERLAY-PEER activate
      domain identifier 65101:0
      route import match-failure action discard
      host-flap detection window 10 threshold 1
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
   !
   vrf TENANT_A_PROJECT01
      rd 192.168.255.3:11
      route-target import evpn 11:11
      route-target import evpn rcf RT_IMPORT_AF_RCF()
      route-target export evpn 11:11
      route-target export evpn rcf RT_EXPORT_AF_RCF()
      router-id 192.168.255.3
      neighbor 10.255.251.1 peer group MLAG-IPv4-UNDERLAY-PEER
      neighbor 10.255.251.1 rib-in pre-policy retain
      redistribute connected
      redistribute isis route-map Router_BGP_Isis
      redistribute static rcf Router_BGP_Static()
   !
   vrf TENANT_A_PROJECT02
      rd 192.168.255.3:12
      route-target import evpn 12:12
      route-target export evpn 12:12
      router-id 192.168.255.3
      neighbor 10.255.251.1 peer group MLAG-IPv4-UNDERLAY-PEER
      redistribute connected
```
