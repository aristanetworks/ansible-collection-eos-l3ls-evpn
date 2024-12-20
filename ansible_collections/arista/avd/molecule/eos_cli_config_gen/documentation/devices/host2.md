# host2

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Management SSH](#management-ssh)
  - [Management API gNMI](#management-api-gnmi)
  - [Management CVX Summary](#management-cvx-summary)
  - [Management API HTTP](#management-api-http)
- [CVX](#cvx)
  - [CVX Device Configuration](#cvx-device-configuration)
- [Authentication](#authentication)
  - [Enable Password](#enable-password)
  - [TACACS Servers](#tacacs-servers)
  - [RADIUS Server](#radius-server)
  - [AAA Authentication](#aaa-authentication)
  - [AAA Authorization](#aaa-authorization)
  - [AAA Accounting](#aaa-accounting)
- [Management Security](#management-security)
  - [Management Security Summary](#management-security-summary)
  - [Management Security SSL Profiles](#management-security-ssl-profiles)
  - [Management Security Device Configuration](#management-security-device-configuration)
- [Prompt Device Configuration](#prompt-device-configuration)
- [DHCP Relay](#dhcp-relay)
  - [DHCP Relay Summary](#dhcp-relay-summary)
  - [DHCP Relay Device Configuration](#dhcp-relay-device-configuration)
- [System Boot Settings](#system-boot-settings)
  - [System Boot Device Configuration](#system-boot-device-configuration)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
  - [Logging](#logging)
  - [SNMP](#snmp)
  - [Flow Tracking](#flow-tracking)
  - [Monitor Server Radius Summary](#monitor-server-radius-summary)
- [Monitor Connectivity](#monitor-connectivity)
  - [Global Configuration](#global-configuration)
  - [Monitor Connectivity Device Configuration](#monitor-connectivity-device-configuration)
- [LACP](#lacp)
  - [LACP Summary](#lacp-summary)
  - [LACP Device Configuration](#lacp-device-configuration)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Interfaces](#interfaces)
  - [Switchport Default](#switchport-default)
  - [DPS Interfaces](#dps-interfaces)
  - [VXLAN Interface](#vxlan-interface)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [ARP](#arp)
  - [Router Adaptive Virtual Topology](#router-adaptive-virtual-topology)
  - [Router ISIS](#router-isis)
  - [Router BGP](#router-bgp)
  - [PBR Policy Maps](#pbr-policy-maps)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [MPLS](#mpls)
  - [MPLS and LDP](#mpls-and-ldp)
  - [MPLS RSVP](#mpls-rsvp)
  - [MPLS Device Configuration](#mpls-device-configuration)
- [Queue Monitor](#queue-monitor)
  - [Queue Monitor Length](#queue-monitor-length)
  - [Queue Monitor Configuration](#queue-monitor-configuration)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
  - [PIM Sparse Mode](#pim-sparse-mode)
- [Filters](#filters)
  - [AS Path Lists](#as-path-lists)
- [802.1X Port Security](#8021x-port-security)
  - [802.1X Summary](#8021x-summary)
- [Application Traffic Recognition](#application-traffic-recognition)
  - [Applications](#applications)
  - [Router Application-Traffic-Recognition Device Configuration](#router-application-traffic-recognition-device-configuration)
- [IP DHCP Relay](#ip-dhcp-relay)
  - [IP DHCP Relay Summary](#ip-dhcp-relay-summary)
  - [IP DHCP Relay Device Configuration](#ip-dhcp-relay-device-configuration)
- [IP DHCP Snooping](#ip-dhcp-snooping)
  - [IP DHCP Snooping Device Configuration](#ip-dhcp-snooping-device-configuration)
- [IP NAT](#ip-nat)
  - [IP NAT Device Configuration](#ip-nat-device-configuration)
  - [Traffic Policies information](#traffic-policies-information)
- [STUN](#stun)
  - [STUN Server](#stun-server)
  - [STUN Device Configuration](#stun-device-configuration)

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

### Management SSH

#### IPv4 ACL

| IPv4 ACL | VRF |
| -------- | --- |
| ACL-SSH | - |
| ACL-SSH-VRF | mgt |

#### SSH Timeout and Management

| Idle Timeout | SSH Management |
| ------------ | -------------- |
| 15 | Enabled |

#### Max number of SSH sessions limit and per-host limit

| Connection Limit | Max from a single Host |
| ---------------- | ---------------------- |
| 55 | - |

#### Ciphers and Algorithms

| Ciphers | Key-exchange methods | MAC algorithms | Hostkey server algorithms |
|---------|----------------------|----------------|---------------------------|
| aes256-cbc, aes256-ctr, aes256-gcm@openssh.com | ecdh-sha2-nistp521 | hmac-sha2-512, hmac-sha2-512-etm@openssh.com | ecdsa-nistp256, ecdsa-nistp521 |

#### VRFs

| VRF | Status |
| --- | ------ |
| mgt | Enabled |

#### Management SSH Device Configuration

```eos
!
management ssh
   ip access-group ACL-SSH in
   ip access-group ACL-SSH-VRF vrf mgt in
   idle-timeout 15
   cipher aes256-cbc aes256-ctr aes256-gcm@openssh.com
   key-exchange ecdh-sha2-nistp521
   mac hmac-sha2-512 hmac-sha2-512-etm@openssh.com
   hostkey server ecdsa-nistp256 ecdsa-nistp521
   connection limit 55
   no shutdown
   hostkey server cert sshkey.cert
   !
   vrf mgt
      no shutdown
```

### Management API gNMI

#### Management API gNMI Summary

| Transport | SSL Profile | VRF | Notification Timestamp | ACL | Port |
| --------- | ----------- | --- | ---------------------- | --- | ---- |
| MGMT | - | MGMT | last-change-time | ACL-GNMI | 6030 |
| MONITORING | - | MONITORING | last-change-time | - | 6031 |

#### Management API gNMI Device Configuration

```eos
!
management api gnmi
   transport grpc MGMT
      vrf MGMT
      ip access-group ACL-GNMI
   !
   transport grpc MONITORING
      port 6031
      vrf MONITORING
```

### Management CVX Summary

| Shutdown | CVX Servers |
| -------- | ----------- |
| True | - |

#### Management CVX Device Configuration

```eos
!
management cvx
   shutdown
```

### Management API HTTP

#### Management API HTTP Summary

| HTTP | HTTPS | Default Services |
| ---- | ----- | ---------------- |
| True | False | False |

#### Management API HTTP Device Configuration

```eos
!
management api http-commands
   no protocol https
   protocol http
   no default-services
   no shutdown
```

## CVX

CVX is disabled

### CVX Device Configuration

```eos
!
cvx
   shutdown
   !
   service mcs
      shutdown
   !
   service vxlan
      shutdown
```

## Authentication

### Enable Password

md5 encrypted enable password is configured

#### Enable Password Device Configuration

```eos
!
enable password 5 <removed>
!
```

### TACACS Servers

#### TACACS Servers

| VRF | TACACS Servers | Single-Connection | Timeout |
| --- | -------------- | ----------------- | ------- |
| default | 10.10.10.159 | False | - |

#### TACACS Servers Device Configuration

```eos
!
tacacs-server host 10.10.10.159 key 8a <removed>
```

### RADIUS Server

- Attribute 32 is included in access requests using format 'myformat'

#### RADIUS Server Device Configuration

```eos
!
radius-server attribute 32 include-in-access-req format myformat
```

### AAA Authentication

#### AAA Authentication Summary

| Type | Sub-type | User Stores |
| ---- | -------- | ---------- |

#### AAA Authentication Device Configuration

```eos
!
```

### AAA Authorization

#### AAA Authorization Summary

| Type | User Stores |
| ---- | ----------- |

Authorization for configuration commands is disabled.

#### AAA Authorization Device Configuration

```eos
no aaa authorization config-commands
!
```

### AAA Accounting

#### AAA Accounting Summary

| Type | Commands | Record type | Group | Logging |
| ---- | -------- | ----------- | ----- | ------- |
| Exec - Console | - | none | - | True |
| Exec - Default | - | none | - | - |

#### AAA Accounting Device Configuration

```eos
aaa accounting exec console none
aaa accounting exec default none
```

## Management Security

### Management Security Summary

| Settings | Value |
| -------- | ----- |
| Reversible password encryption | aes-256-gcm |

### Management Security SSL Profiles

| SSL Profile Name | TLS protocol accepted | Certificate filename | Key filename | Ciphers | CRLs |
| ---------------- | --------------------- | -------------------- | ------------ | ------- | ---- |
| cipher-v1.0-v1.3 | - | - | - | v1.0 to v1.2: SHA256:SHA384<br>v1.3: TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256 | - |

### Management Security Device Configuration

```eos
!
management security
   password encryption reversible aes-256-gcm
   !
   ssl profile cipher-v1.0-v1.3
      cipher v1.0 SHA256:SHA384
      cipher v1.3 TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256
```

## Prompt Device Configuration

```eos
!
prompt Test
```

## DHCP Relay

### DHCP Relay Summary

- DHCP Relay is enabled for tunnelled requests
- DHCP Relay is enabled for MLAG peer-link requests

| DHCP Relay Servers |
| ------------------ |
| dhcp-relay-server1 |
| dhcp-relay-server2 |

### DHCP Relay Device Configuration

```eos
!
dhcp relay
   server dhcp-relay-server1
   server dhcp-relay-server2
```

## System Boot Settings

### System Boot Device Configuration

```eos
!
```

## Monitoring

### TerminAttr Daemon

#### TerminAttr Daemon Summary

| CV Compression | CloudVision Servers | VRF | Authentication | Smash Excludes | Ingest Exclude | Bypass AAA |
| -------------- | ------------------- | --- | -------------- | -------------- | -------------- | ---------- |
| gzip | 10.20.20.1:9910 | mgt | certs,/persist/secure/ssl/terminattr/DC1/certs/client.crt,/persist/secure/ssl/terminattr/DC1/keys/client.key,/persist/secure/ssl/terminattr/DC1/certs/ca.crt | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | False |
| gzip | 10.30.30.1:9910 | mgt | key,<removed> | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | False |
| gzip | 10.40.40.1:9910 | mgt | token,/tmp/tokenDC3 | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | False |
| gzip | apiserver.arista.io:443 | - | key,<removed> | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | False |

#### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvopt DC1.addr=10.20.20.1:9910 -cvopt DC1.auth=certs,/persist/secure/ssl/terminattr/DC1/certs/client.crt,/persist/secure/ssl/terminattr/DC1/keys/client.key,/persist/secure/ssl/terminattr/DC1/certs/ca.crt -cvopt DC1.vrf=mgt -cvopt DC1.sourceintf=Loopback10 -cvopt DC2.addr=10.30.30.1:9910 -cvopt DC2.auth=key,<removed> -cvopt DC2.vrf=mgt -cvopt DC2.sourceintf=Vlan500 -cvopt DC3.addr=10.40.40.1:9910 -cvopt DC3.auth=token,/tmp/tokenDC3 -cvopt DC3.vrf=mgt -cvopt DC3.sourceintf=Vlan500 -cvaddr=apiserver.arista.io:443 -cvauth=key,<removed> -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -taillogs
   no shutdown
```

### Logging

#### Logging Servers and Features Summary

| Type | Level |
| -----| ----- |
| Console | informational |
| Monitor | debugging |
| Buffer | - |

**Syslog facility value:** syslog

#### Logging Servers and Features Device Configuration

```eos
!
no logging repeat-messages
logging buffered 64000
logging console informational
logging monitor debugging
logging facility syslog
!
logging event link-status global
```

### SNMP

#### SNMP Configuration Summary

| Contact | Location | SNMP Traps | State |
| ------- | -------- | ---------- | ----- |
| - | - | All | Disabled |

#### SNMP Device Configuration

```eos
!
no snmp-server enable traps
```

### Flow Tracking

#### Flow Tracking Sampled

| Sample Size | Minimum Sample Size | Hardware Offload for IPv4 | Hardware Offload for IPv6 | Encapsulations |
| ----------- | ------------------- | ------------------------- | ------------------------- | -------------- |
| 666 | default | enabled | enabled | - |

##### Trackers Summary

| Tracker Name | Record Export On Inactive Timeout | Record Export On Interval | MPLS | Number of Exporters | Applied On | Table Size |
| ------------ | --------------------------------- | ------------------------- | ---- | ------------------- | ---------- | ---------- |
| T21 | 3666 | 5666 | True | 0 |  | - |

##### Exporters Summary

| Tracker Name | Exporter Name | Collector IP/Host | Collector Port | Local Interface |
| ------------ | ------------- | ----------------- | -------------- | --------------- |

#### Flow Tracking Device Configuration

```eos
!
flow tracking sampled
   sample 666
   hardware offload ipv4 ipv6
   tracker T21
      record export on inactive timeout 3666
      record export on interval 5666
      record export mpls
```

### Monitor Server Radius Summary

#### Server Probe Settings

| Setting | Value |
| ------- | ----- |
| Probe method | status-server |

#### Monitor Server Radius Device Configuration

```eos
!
monitor server radius
   probe method status-server
```

## Monitor Connectivity

### Global Configuration

#### Interface Sets

| Name | Interfaces |
| ---- | ---------- |
| HOST_SET2 | Loopback2-4, Loopback10-12 |

#### Probing Configuration

| Enabled | Interval | Default Interface Set | Address Only |
| ------- | -------- | --------------------- | ------------ |
| False | 5 | HOST_SET2 | False |

### Monitor Connectivity Device Configuration

```eos
!
monitor connectivity
   interval 5
   shutdown
   interface set HOST_SET2 Loopback2-4, Loopback10-12
   local-interfaces HOST_SET2 default
```

## LACP

### LACP Summary

| Port-id range | Rate-limit default | System-priority |
| ------------- | ------------------ | --------------- |
| - | - | 0 |

### LACP Device Configuration

```eos
!
lacp system-priority 0
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **rstp**

#### Global Spanning-Tree Settings

- Global RSTP priority: 8192
- Global BPDU Guard for Edge ports is enabled.
- Global BPDU Filter for Edge ports is enabled.

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode rstp
spanning-tree edge-port bpduguard default
spanning-tree edge-port bpdufilter default
no spanning-tree bpduguard rate-limit default
spanning-tree priority 8192
```

## Interfaces

### Switchport Default

#### Switchport Defaults Summary

- Default Switchport Mode: routed

#### Switchport Default Device Configuration

```eos
!
switchport default mode routed
```

### DPS Interfaces

#### DPS Interfaces Summary

| Interface | IP address | Shutdown | MTU | Flow tracker(s) | TCP MSS Ceiling |
| --------- | ---------- | -------- | --- | --------------- | --------------- |
| Dps1 | 192.168.42.42/24 | False | 666 | Sampled: FT-S |  |

#### DPS Interfaces Device Configuration

```eos
!
interface Dps1
   description Test DPS Interface
   no shutdown
   mtu 666
   flow tracker sampled FT-S
   ip address 192.168.42.42/24
```

### VXLAN Interface

#### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| UDP port | 4789 |
| Qos dscp propagation encapsulation | Disabled |
| Qos ECN propagation | Disabled |
| Qos map dscp to traffic-class decapsulation | Disabled |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   no vxlan qos ecn propagation
   no vxlan qos dscp propagation encapsulation
   no vxlan qos map dscp to traffic-class decapsulation
```

## Routing

### Service Routing Protocols Model

Single agent routing protocol model enabled

```eos
!
service routing protocols model ribd
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |

#### IP Routing Device Configuration

```eos
!
no ip routing
no ip icmp redirect
```

### ARP

ARP cache persistency is enabled.

#### ARP Device Configuration

```eos
!
arp persistent
```

### Router Adaptive Virtual Topology

#### Router Adaptive Virtual Topology Summary

Topology role: edge

VXLAN gateway: Enabled

#### Router Adaptive Virtual Topology Configuration

```eos
!
router adaptive-virtual-topology
   topology role edge gateway vxlan
```

### Router ISIS

#### Router ISIS Summary

| Settings | Value |
| -------- | ----- |
| Instance | EVPN_UNDERLAY |
| Net-ID | 49.0001.0001.0001.0001.00 |
| Type | level-2 |
| Router-ID | 192.168.255.3 |
| Log Adjacency Changes | True |
| SR MPLS Enabled | False |
| SPF Interval | 250 seconds |

#### ISIS Route Timers

| Settings | Value |
| -------- | ----- |
| Local Convergence Delay | 10000 milliseconds |

#### ISIS Interfaces Summary

| Interface | ISIS Instance | ISIS Metric | Interface Mode |
| --------- | ------------- | ----------- | -------------- |

#### ISIS IPv4 Address Family Summary

| Settings | Value |
| -------- | ----- |
| IPv4 Address-family Enabled | True |

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
   timers local-convergence-delay protected-prefixes
   set-overload-bit on-startup wait-for-bgp
   spf-interval 250
   authentication mode sha key-id 5 rx-disabled level-1
   authentication mode shared-secret profile test2 algorithm md5 rx-disabled level-2
   authentication key 0 password
   !
   address-family ipv4 unicast
      tunnel source-protocol bgp ipv4 labeled-unicast
   !
   address-family ipv6 unicast
      bfd all-interfaces
      fast-reroute ti-lfa srlg
   !
   segment-routing mpls
      shutdown
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65101 | - |

| BGP Tuning |
| ---------- |
| graceful-restart |
| no graceful-restart-helper |
| no bgp additional-paths receive |
| no bgp additional-paths send |
| no bgp default ipv4-unicast |
| no bgp default ipv4-unicast transport ipv6 |
| bgp route-reflector preserve-attributes |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | Encapsulation |
| ---------- | -------- | ------------ | ------------- | ------------- |
| EVPN-OVERLAY-PEERS | True |  - | - | default |
| MLAG-IPv4-UNDERLAY-PEER | False |  - | - | default |

##### EVPN Neighbor Default Encapsulation

| Neighbor Default Encapsulation | Next-hop-self Source Interface |
| ------------------------------ | ------------------------------ |
| path-selection | - |

##### EVPN Host Flapping Settings

| State | Window | Threshold | Expiry Timeout |
| ----- | ------ | --------- | -------------- |
| Enabled | - | - | 20 Seconds |

##### EVPN DCI Gateway Summary

| Settings | Value |
| -------- | ----- |
| L3 Gateway Configured | True |
| L3 Gateway Inter-domain | True |

#### Router BGP IPv4 Labeled Unicast

##### General Settings

| Settings | Value |
| -------- | ----- |

#### Router BGP Path-Selection Address Family

#### Router BGP Device Configuration

```eos
!
router bgp 65101
   no bgp default ipv4-unicast
   no bgp default ipv4-unicast transport ipv6
   graceful-restart
   no graceful-restart-helper
   bgp route-reflector preserve-attributes
   no bgp additional-paths receive
   no bgp additional-paths send
   bgp redistribute-internal
   redistribute connected include leaked route-map RM-CONN-2-BGP
   redistribute isis level-2 include leaked rcf RCF_CONN_2_BGP()
   redistribute ospf match internal include leaked route-map RM_BGP_EVPN
   redistribute ospf match external include leaked route-map RM_BGP_EVPN
   redistribute ospfv3 match internal include leaked route-map RM-CONN-2-BGP
   redistribute static route-map RM-STATIC-2-BGP
   redistribute dynamic rcf RCF_CONN_2_BGP()
   !
   address-family evpn
      no bgp additional-paths send
      neighbor default encapsulation path-selection
      neighbor EVPN-OVERLAY-PEERS activate
      no neighbor MLAG-IPv4-UNDERLAY-PEER activate
      neighbor default next-hop-self received-evpn-routes route-type ip-prefix inter-domain
      host-flap detection expiry timeout 20 seconds
   !
   address-family ipv4
      bgp additional-paths install ecmp-primary
      no bgp additional-paths send
      bgp redistribute-internal
      redistribute bgp leaked
      redistribute connected route-map RM_BGP_EVPN_IPV4
      redistribute dynamic rcf RCF_BGP_EVPN_IPV4()
      redistribute isis level-1 include leaked rcf Address_Family_IPV4_ISIS()
      redistribute ospf include leaked route-map RM_BGP_EVPN_IPV4
      redistribute ospfv3 match internal include leaked route-map RM_BGP_EVPN_IPV4
      redistribute ospf match external include leaked route-map RM_BGP_EVPN_IPV4
      redistribute ospf match nssa-external 1 include leaked route-map RM_BGP_EVPN_IPV4
      redistribute static include leaked route-map RM_BGP_EVPN_IPV4
   !
   address-family ipv4 labeled-unicast
      bgp additional-paths send any
   !
   address-family ipv4 multicast
      redistribute ospfv3 route-map AFIPV4M_OSPFV3
      redistribute ospf match external route-map AFIPV4M_OSPF_EXTERNAL
   !
   address-family ipv6
      bgp additional-paths install
      bgp additional-paths send ecmp limit 8
      no bgp redistribute-internal
      redistribute attached-host route-map RM-Address_Family_IPV6_Attached-Host
      redistribute dhcp route-map RM-Address_Family_IPV6_DHCP
      redistribute connected route-map RM-Address_Family_IPV6_Connected
      redistribute dynamic rcf RCF_Address_Family_IPV6_Dynamic()
      redistribute user rcf RCF_Address_Family_IPV6_User()
      redistribute isis include leaked route-map RM-Address_Family_IPV6_ISIS
      redistribute ospfv3 match internal include leaked route-map RM-REDISTRIBUTE-OSPF-INTERNAL
      redistribute ospfv3 match external include leaked
      redistribute ospfv3 match nssa-external 1 include leaked route-map RM-REDISTRIBUTE-OSPF-NSSA-EXTERNAL
      redistribute static include leaked rcf RCF_IPV6_STATIC_TO_BGP()
   !
   address-family ipv6 multicast
      redistribute isis rcf Router_BGP_Isis()
      redistribute ospf match internal route-map RM-address_family_ipv6_multicast-OSPF
      redistribute ospfv3 match internal route-map RM-address_family_ipv6_multicast-OSPFv3
   !
   address-family path-selection
      no bgp additional-paths send
```

### PBR Policy Maps

#### PBR Policy Maps Summary

##### POLICY_DROP_THEN_NEXTHOP

| Class | Index | Drop | Nexthop | Recursive |
| ----- | ----- | ---- | ------- | --------- |
| CLASS_DROP | 10 | True | - | - |
| CLASS_NEXTHOP | 20 | - | 172.30.1.2 | True |
| NO_ACTION | - | - | - | - |

#### PBR Policy Maps Device Configuration

```eos
!
policy-map type pbr POLICY_DROP_THEN_NEXTHOP
   10 class CLASS_DROP
      drop
   !
   20 class CLASS_NEXTHOP
      set nexthop recursive 172.30.1.2
   !
   class NO_ACTION
```

## BFD

### Router BFD

#### Router BFD Device Configuration

```eos
!
router bfd
   session stats snapshot interval dangerous 8
```

## MPLS

### MPLS and LDP

#### MPLS and LDP Summary

| Setting | Value |
| -------- | ---- |
| MPLS IP Enabled | True |
| LDP Enabled | False |
| LDP Router ID | - |
| LDP Interface Disabled Default | False |
| LDP Transport-Address Interface | - |
| ICMP TTL-Exceeded Tunneling Enabled | True |

### MPLS RSVP

#### MPLS RSVP Summary

| Setting | Value |
| ------- | ----- |
| Refresh interval | 4 |
| Authentication type | - |
| Authentication sequence-number window | - |
| Authentication active index | 766 |
| SRLG | Enabled |
| Preemption method | hard |
| Fast reroute mode | node-protection |
| Fast reroute reversion | - |
| Fast reroute  bypass tunnel optimization interval | - |
| Hitless restart | Active |
| Hitless restart recovery timer | - |
| P2MP | True |
| Shutdown | False |

##### RSVP Graceful Restart

| Role | Recovery timer | Restart timer |
| ---- | -------------- | ------------- |
| Helper | - | - |
| Speaker | - | - |

### MPLS Device Configuration

```eos
!
mpls ip
!
mpls ldp
   shutdown
!
mpls icmp ttl-exceeded tunneling
!
mpls rsvp
   refresh interval 4
   authentication index 766 active
   fast-reroute mode node-protection
   srlg
   preemption method hard
   !
   hitless-restart
   !
   graceful-restart role helper
   !
   graceful-restart role speaker
   !
   p2mp
   no shutdown
```

## Queue Monitor

### Queue Monitor Length

| Enabled | Logging Interval | Default Thresholds High | Default Thresholds Low | Notifying | TX Latency | CPU Thresholds High | CPU Thresholds Low |
| ------- | ---------------- | ----------------------- | ---------------------- | --------- | ---------- | ------------------- | ------------------ |
| True | - | 100 | - | disabled | disabled | - | - |

### Queue Monitor Configuration

```eos
!
queue-monitor length
no queue-monitor length notifying
queue-monitor length default threshold 100
```

## Multicast

### IP IGMP Snooping

#### IP IGMP Snooping Summary

| IGMP Snooping | Fast Leave | Interface Restart Query | Proxy | Restart Query Interval | Robustness Variable |
| ------------- | ---------- | ----------------------- | ----- | ---------------------- | ------------------- |
| Disabled | False | - | False | - | - |

| Querier Enabled | IP Address | Query Interval | Max Response Time | Last Member Query Interval | Last Member Query Count | Startup Query Interval | Startup Query Count | Version |
| --------------- | ---------- | -------------- | ----------------- | -------------------------- | ----------------------- | ---------------------- | ------------------- | ------- |
| False | - | - | - | - | - | - | - | - |

##### IP IGMP Snooping Vlan Summary

| Vlan | IGMP Snooping | Fast Leave | Max Groups | Proxy |
| ---- | ------------- | ---------- | ---------- | ----- |
| 20 | False | - | - | - |
| 30 | False | - | - | - |

#### IP IGMP Snooping Device Configuration

```eos
!
no ip igmp snooping
no ip igmp snooping fast-leave
no ip igmp snooping vlan 20
no ip igmp snooping vlan 30
no ip igmp snooping querier
```

### PIM Sparse Mode

#### Router PIM Sparse Mode

##### IP Sparse Mode Information

BFD enabled: False

Make-before-break: True

##### IP Sparse Mode VRFs

| VRF Name | BFD Enabled | Make-before-break |
| -------- | ----------- | ----------------- |
| MCAST_VRF1 | False | True |

##### Router Multicast Device Configuration

```eos
!
router pim sparse-mode
   ipv4
      make-before-break
   !
   vrf MCAST_VRF1
      ipv4
         make-before-break
```

## Filters

### AS Path Lists

#### AS Path Lists Summary

| List Name | Type | Match | Origin |
| --------- | ---- | ----- | ------ |

#### AS Path Lists Device Configuration

```eos
!
```

## 802.1X Port Security

### 802.1X Summary

#### 802.1X Global

| System Auth Control | Protocol LLDP Bypass | Dynamic Authorization |
| ------------------- | -------------------- | ----------------------|
| True | True | True |

#### 802.1X Radius AV pair

| Service type | Framed MTU |
| ------------ | ---------- |
| True | 1500 |

## Application Traffic Recognition

### Applications

#### IPv4 Applications

| Name | Source Prefix | Destination Prefix | Protocols | Protocol Ranges | TCP Source Port Set | TCP Destination Port Set | UDP Source Port Set | UDP Destination Port Set | DSCP |
| ---- | ------------- | ------------------ | --------- | --------------- | ------------------- | ------------------------ | ------------------- | ------------------------ | ---- |
| user_defined_app1 | src_prefix_set1 | dest_prefix_set1 | udp, tcp | 25 | src_port_set1 | dest_port_set1 | - | - | 12-19 af43 af41 ef 1-4,6 32-33,34-35 11 56-57, 58 59-60, 61-62 |

#### Layer 4 Applications

| Name | Protocols | Protocol Ranges | TCP Source Port Set | TCP Destination Port Set | UDP Source Port Set | UDP Destination Port Set |
| ---- | --------- | --------------- | ------------------- | ------------------------ | ------------------- | ------------------------ |
| l4-app-1 | tcp, udp | - | src_port_set1 | dest_port_set1 | - | - |

### Router Application-Traffic-Recognition Device Configuration

```eos
!
application traffic recognition
   !
   application ipv4 user_defined_app1
      source prefix field-set src_prefix_set1
      destination prefix field-set dest_prefix_set1
      protocol tcp source port field-set src_port_set1 destination port field-set dest_port_set1
      protocol udp
      protocol 25
      dscp 12-19 af43 af41 ef 1-4,6 32-33,34-35 11 56-57, 58 59-60, 61-62
   !
   application l4 l4-app-1
      protocol tcp source port field-set src_port_set1 destination port field-set dest_port_set1
      protocol udp
```

## IP DHCP Relay

### IP DHCP Relay Summary

IP DHCP Relay Option 82 is enabled.

### IP DHCP Relay Device Configuration

```eos
!
ip dhcp relay information option
```

## IP DHCP Snooping

IP DHCP Snooping is enabled

### IP DHCP Snooping Device Configuration

```eos
!
ip dhcp snooping
```

## IP NAT

### IP NAT Device Configuration

```eos
!
!
ip nat synchronization
```

### Traffic Policies information

#### IPv6 Field Sets

| Field Set Name | IPv6 Prefixes |
| -------------- | ------------- |
| IPv6-DEMO-1 | 11:22:33:44:55:66:77:88 |
| IPv6-DEMO-2 | - |

#### Traffic Policies Device Configuration

```eos
!
traffic-policies
   field-set ipv6 prefix IPv6-DEMO-1
      11:22:33:44:55:66:77:88
   !
   field-set ipv6 prefix IPv6-DEMO-2
```

## STUN

### STUN Server

| Server Local Interfaces | Bindings Timeout (s) | SSL Profile | SSL Connection Lifetime | Port |
| ----------------------- | -------------------- | ----------- | ----------------------- | ---- |
| Ethernet1 | - | - | 3 hours | 3478 |

### STUN Device Configuration

```eos
!
stun
   server
      local-interface Ethernet1
      ssl connection lifetime 3 hours
```
