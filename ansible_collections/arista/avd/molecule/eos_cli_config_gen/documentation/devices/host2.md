# host2

## Table of Contents

- [Management](#management)
  - [Banner](#banner)
  - [Management Interfaces](#management-interfaces)
  - [NTP](#ntp)
  - [PTP](#ptp)
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
  - [MCS Client Summary](#mcs-client-summary)
  - [SNMP](#snmp)
  - [Tap Aggregation](#tap-aggregation)
  - [SFlow](#sflow)
  - [Flow Tracking](#flow-tracking)
  - [Monitor Telemetry Postcard Policy](#monitor-telemetry-postcard-policy)
  - [Monitor Server Radius Summary](#monitor-server-radius-summary)
- [Monitor Connectivity](#monitor-connectivity)
  - [Global Configuration](#global-configuration)
  - [Monitor Connectivity Device Configuration](#monitor-connectivity-device-configuration)
- [Monitor Layer 1 Logging](#monitor-layer-1-logging)
  - [Monitor Layer 1 Device Configuration](#monitor-layer-1-device-configuration)
- [Hardware TCAM Profile](#hardware-tcam-profile)
  - [Custom TCAM Profiles](#custom-tcam-profiles)
  - [Hardware TCAM Device Configuration](#hardware-tcam-device-configuration)
- [LLDP](#lldp)
  - [LLDP Summary](#lldp-summary)
  - [LLDP Device Configuration](#lldp-device-configuration)
- [LACP](#lacp)
  - [LACP Summary](#lacp-summary)
  - [LACP Device Configuration](#lacp-device-configuration)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [MAC Address Table](#mac-address-table)
  - [MAC Address Table Summary](#mac-address-table-summary)
  - [MAC Address Table Device Configuration](#mac-address-table-device-configuration)
- [Interfaces](#interfaces)
  - [Switchport Default](#switchport-default)
  - [Interface Defaults](#interface-defaults)
  - [DPS Interfaces](#dps-interfaces)
  - [VXLAN Interface](#vxlan-interface)
- [Switchport Port-security](#switchport-port-security)
  - [Switchport Port-security Summary](#switchport-port-security-summary)
  - [Switchport Port-security Device Configuration](#switchport-port-security-device-configuration)
- [Routing](#routing)
  - [Service Routing Configuration BGP](#service-routing-configuration-bgp)
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
  - [Queue Monitor Streaming](#queue-monitor-streaming)
  - [Queue Monitor Configuration](#queue-monitor-configuration)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
  - [Router Multicast](#router-multicast)
  - [PIM Sparse Mode](#pim-sparse-mode)
- [Filters](#filters)
  - [AS Path Lists](#as-path-lists)
- [802.1X Port Security](#8021x-port-security)
  - [802.1X Summary](#8021x-summary)
- [Application Traffic Recognition](#application-traffic-recognition)
  - [Applications](#applications)
  - [Router Application-Traffic-Recognition Device Configuration](#router-application-traffic-recognition-device-configuration)
- [Router L2 VPN](#router-l2-vpn)
  - [Router L2 VPN Summary](#router-l2-vpn-summary)
  - [Router L2 VPN Device Configuration](#router-l2-vpn-device-configuration)
- [IP DHCP Relay](#ip-dhcp-relay)
  - [IP DHCP Relay Summary](#ip-dhcp-relay-summary)
  - [IP DHCP Relay Device Configuration](#ip-dhcp-relay-device-configuration)
- [IPv6 DHCP Relay](#ipv6-dhcp-relay)
  - [IPv6 DHCP Relay Summary](#ipv6-dhcp-relay-summary)
  - [IPv6 DHCP Relay Device Configuration](#ipv6-dhcp-relay-device-configuration)
- [IP DHCP Snooping](#ip-dhcp-snooping)
  - [IP DHCP Snooping Device Configuration](#ip-dhcp-snooping-device-configuration)
- [IP NAT](#ip-nat)
  - [IP NAT Device Configuration](#ip-nat-device-configuration)
- [Errdisable](#errdisable)
  - [Errdisable Summary](#errdisable-summary)
- [MACsec](#macsec)
  - [MACsec Summary](#macsec-summary)
  - [MACsec Device Configuration](#macsec-device-configuration)
  - [Traffic Policies information](#traffic-policies-information)
- [Quality Of Service](#quality-of-service)
  - [QOS](#qos)
  - [Priority Flow Control](#priority-flow-control)
- [STUN](#stun)
  - [STUN Server](#stun-server)
  - [STUN Device Configuration](#stun-device-configuration)

## Management

### Banner

#### Login Banner

```text
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!***!!!Unauthorized access prohibited!!!***!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
EOF
```

#### MOTD Banner

```text
.         Switch       : $(hostname)                            .
.         Site         : DC1                      .
.         Type info for information about the device            .
.         Type help for information about the aliases           .
EOF
```

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

### NTP

#### NTP Summary

##### NTP Authentication

- Authentication enabled

#### NTP Device Configuration

```eos
!
ntp authenticate
```

### PTP

#### PTP Summary

| Clock ID | Source IP | Priority 1 | Priority 2 | TTL | Domain | Mode | Forward Unicast |
| -------- | --------- | ---------- | ---------- | --- | ------ | ---- | --------------- |
| - | - | - | - | - | - | - | - |

#### PTP Device Configuration

```eos
!
no ptp monitor sequence-id
```

### Management SSH

#### Authentication Settings

| Authentication protocols | Empty passwords |
| ------------------------ | --------------- |
| keyboard-interactive, public-key | permit |

#### IPv4 ACL

| IPv4 ACL | VRF |
| -------- | --- |
| ACL-SSH | - |
| ACL-SSH-VRF | mgt |

#### SSH Timeout and Management

| Idle Timeout | SSH Management |
| ------------ | -------------- |
| 15 | Disabled |

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
   authentication empty-passwords permit
   shutdown
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

| HTTP | HTTPS | UNIX-Socket | Default Services |
| ---- | ----- | ----------- | ---------------- |
| True | False | - | False |

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

| SSL Profile Name | TLS protocol accepted | Certificate filename | Key filename | Ciphers | CRLs | FIPS restrictions enabled |
| ---------------- | --------------------- | -------------------- | ------------ | ------- | ---- | ------------------------- |
| cipher-v1.0-v1.3 | - | - | - | v1.0 to v1.2: SHA256:SHA384<br>v1.3: TLS_AES_256_GCM_SHA384:TLS_CHACHA20_POLY1305_SHA256 | - | - |

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
| gzip | 10.20.20.1:9910 | mgt | certs,/persist/secure/ssl/terminattr/DC1/certs/client.crt,/persist/secure/ssl/terminattr/DC1/keys/client.key,/persist/secure/ssl/terminattr/DC1/certs/ca.crt | - | - | False |
| gzip | 10.30.30.1:9910 | mgt | key,<removed> | - | - | False |
| gzip | 10.40.40.1:9910 | mgt | token,/tmp/tokenDC3 | - | - | False |
| gzip | 10.40.40.1:9910 | mgt | token-secure,/tmp/tokenDC4 | - | - | False |
| gzip | 10.20.20.2:9910 | mgt | certs,/persist/secure/ssl/terminattr/DC1/certs/client.crt,/persist/secure/ssl/terminattr/DC1/keys/client.key | - | - | False |
| gzip | 10.20.20.3:9910 | - | - | - | - | False |
| gzip | apiserver.arista.io:443 | - | key,<removed> | - | - | False |

#### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvopt DC1.addr=10.20.20.1:9910 -cvopt DC1.auth=certs,/persist/secure/ssl/terminattr/DC1/certs/client.crt,/persist/secure/ssl/terminattr/DC1/keys/client.key,/persist/secure/ssl/terminattr/DC1/certs/ca.crt -cvopt DC1.vrf=mgt -cvopt DC1.sourceintf=Loopback10 -cvopt DC2.addr=10.30.30.1:9910 -cvopt DC2.auth=key,<removed> -cvopt DC2.vrf=mgt -cvopt DC2.sourceintf=Vlan500 -cvopt DC3.addr=10.40.40.1:9910 -cvopt DC3.auth=token,/tmp/tokenDC3 -cvopt DC3.vrf=mgt -cvopt DC3.sourceintf=Vlan500 -cvopt DC4.addr=10.40.40.1:9910 -cvopt DC4.auth=token-secure,/tmp/tokenDC4 -cvopt DC4.vrf=mgt -cvopt DC4.sourceip=10.10.10.10 -cvopt DC4.proxy=http://arista:arista@10.10.10.1:3128 -cvopt DC4.obscurekeyfile=True -cvopt DC4.sourceintf=Vlan500 -cvopt DC5.addr=10.20.20.2:9910 -cvopt DC5.auth=certs,/persist/secure/ssl/terminattr/DC1/certs/client.crt,/persist/secure/ssl/terminattr/DC1/keys/client.key -cvopt DC5.vrf=mgt -cvopt DC5.sourceintf=Loopback11 -cvopt DC6.addr=10.20.20.3:9910 -cvaddr=apiserver.arista.io:443 -cvauth=key,<removed> -taillogs -ipfix=false -sflow=false
   no shutdown
```

### Logging

#### Logging Servers and Features Summary

| Type | Level |
| -----| ----- |
| Console | disabled |
| Monitor | debugging |
| Buffer | disabled |
| Trap | alerts |
| Synchronous | disabled |

| Format Type | Setting |
| ----------- | ------- |
| Hostname | ipv4 |
| Sequence-numbers | false |
| RFC5424 | False |

**Syslog facility value:** syslog

#### Logging Servers and Features Device Configuration

```eos
!
no logging repeat-messages
no logging buffered
logging trap alerts
no logging console
logging monitor debugging
no logging synchronous
logging format hostname ipv4
logging facility syslog
!
logging event link-status global
```

### MCS Client Summary

MCS client is shutdown

| Secondary CVX cluster | Server Hosts | Enabled |
| --------------------- | ------------ | ------- |
| default | - | False |

#### MCS Client Device Configuration

```eos
!
mcs client
   shutdown
   !
   cvx secondary default
      shutdown
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

### Tap Aggregation

#### Tap Aggregation Summary

| Settings | Values |
| -------- | ------ |
| Mode Exclusive | True |
| Mode Exclusive No-Errdisable | Ethernet1/1, Ethetnet 42/1, Port-Channel200 |
| Mac Timestamp | Replace Source-Mac |
| Mac FCS Append | True |

#### Tap Aggregation Device Configuration

```eos
!
tap aggregation
   mode exclusive
   mode exclusive no-errdisable Ethernet1/1
   mode exclusive no-errdisable Ethetnet 42/1
   mode exclusive no-errdisable Port-Channel200
   mac timestamp replace source-mac
   mac fcs append
```

### SFlow

#### SFlow Summary

sFlow is disabled.

Egress sFlow is enabled on all interfaces by default.

#### SFlow Device Configuration

```eos
!
sflow source 1.1.1.1
sflow interface egress enable default
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

### Monitor Telemetry Postcard Policy

#### Monitor Telemetry Postcard Policy Configuration

```eos
!
monitor telemetry postcard policy
   disabled
   ingress sample tcp-udp-checksum value 65000 mask 0xffff
   marker vxlan
   ingress collection gre source 10.3.3.3 destination 10.3.3.4
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

## Monitor Layer 1 Logging

| Layer 1 Event | Logging |
| ------------- | ------- |

### Monitor Layer 1 Device Configuration

```eos
!
monitor layer1
```

## Hardware TCAM Profile

TCAM profile **`default`** is active

### Custom TCAM Profiles

Following TCAM profiles are configured on device:

- Profile Name: `MY_TCAM_PROFILE`

### Hardware TCAM Device Configuration

```eos
!
hardware tcam
   profile MY_TCAM_PROFILE
Thisisnotaidealinput
   !
```

## LLDP

### LLDP Summary

#### LLDP Global Settings

| Enabled | Management Address | Management VRF | Timer | Hold-Time | Re-initialization Timer | Drop Received Tagged Packets |
| ------- | ------------------ | -------------- | ----- | --------- | ----------------------- | ---------------------------- |
| False | - | Default | 30 | 120 | 2 | - |

### LLDP Device Configuration

```eos
!
no lldp run
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

## MAC Address Table

### MAC Address Table Summary

- Logging MAC address interface flapping is Disabled

### MAC Address Table Device Configuration

```eos
!
no mac address-table notification host-flap logging
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

### Interface Defaults

#### Interface Defaults Summary

- Default Ethernet Interface Shutdown: False

#### Interface Defaults Device Configuration

```eos
!
interface defaults
   ethernet
      no shutdown
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

##### VLAN to VNI, Flood List and Multicast Group Mappings

| VLAN | VNI | Flood List | Multicast Group |
| ---- | --- | ---------- | --------------- |
| 111,113,115-118 | 10111,10113,10115-10118 | - | - |
| 110 | 10110 | - | 239.9.1.4 |
| 111 | - | 10.1.1.10<br/>10.1.1.11 | - |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   vxlan vlan 110 vni 10110
   vxlan vlan 111,113,115-118 vni 10111,10113,10115-10118
   vxlan vlan 111 flood vtep 10.1.1.10 10.1.1.11
   vxlan vlan 110 multicast group 239.9.1.4
   no vxlan qos ecn propagation
   no vxlan qos dscp propagation encapsulation
   no vxlan qos map dscp to traffic-class decapsulation
```

## Switchport Port-security

### Switchport Port-security Summary

| Settings | Value |
| -------- | ----- |
| Mac-address Aging | True |

### Switchport Port-security Device Configuration

```eos
!
switchport port-security mac-address aging
```

## Routing

### Service Routing Configuration BGP

BGP no equals default disabled

```eos
```

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

| Peer Group | Activate | Route-map In | Route-map Out | Encapsulation | Next-hop-self Source Interface |
| ---------- | -------- | ------------ | ------------- | ------------- | ------------------------------ |
| EVPN-OVERLAY-PEERS | True |  - | - | default | - |
| MLAG-IPv4-UNDERLAY-PEER | False |  - | - | default | - |

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
| Graceful-restart | Enabled |

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
   neighbor default send-community large
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
      graceful-restart
   !
   address-family ipv4 multicast
      redistribute ospf match internal route-map AFIPV4M_OSPF_INTERNAL
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

### Queue Monitor Streaming

| Enabled | IP Access Group | IPv6 Access Group | Max Connections | VRF |
| ------- | --------------- | ----------------- | --------------- | --- |
| False | - | - | - | - |

### Queue Monitor Configuration

```eos
!
queue-monitor length
no queue-monitor length notifying
queue-monitor length default threshold 100
!
queue-monitor streaming
   shutdown
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

### Router Multicast

#### IP Router Multicast Summary

- Multipathing deterministically by selecting the same-colored upstream routers.
- Software forwarding by the Linux kernel

#### Router Multicast Device Configuration

```eos
!
router multicast
   ipv4
      multipath deterministic color
      software-forwarding kernel
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

## Router L2 VPN

### Router L2 VPN Summary

- VXLAN ARP Proxying is disabled for IPv4 addresses defined in the prefix-list pl-router-l2-vpn.

### Router L2 VPN Device Configuration

```eos
!
router l2-vpn
   arp proxy prefix-list pl-router-l2-vpn
```

## IP DHCP Relay

### IP DHCP Relay Summary

IP DHCP Relay Option 82 is enabled.

### IP DHCP Relay Device Configuration

```eos
!
ip dhcp relay information option
```

## IPv6 DHCP Relay

### IPv6 DHCP Relay Summary

Add RemoteID option 37 in format MAC address and interface name.

### IPv6 DHCP Relay Device Configuration

```eos
!
ipv6 dhcp relay option remote-id format %m:%p
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

## Errdisable

### Errdisable Summary

|  Cause | Detection Enabled | Recovery Enabled |
| ------ | ----------------- | ---------------- |
| arp-inspection | - | True |
| bpduguard | - | True |
| hitless-reload-down | - | True |
| lacp-rate-limit | - | True |
| link-flap | - | True |
| no-internal-vlan | - | True |
| portchannelguard | - | True |
| portsec | - | True |
| tapagg | - | True |
| uplink-failure-detection | - | True |

```eos
!
errdisable recovery cause arp-inspection
errdisable recovery cause bpduguard
errdisable recovery cause hitless-reload-down
errdisable recovery cause lacp-rate-limit
errdisable recovery cause link-flap
errdisable recovery cause no-internal-vlan
errdisable recovery cause portchannelguard
errdisable recovery cause portsec
errdisable recovery cause tapagg
errdisable recovery cause uplink-failure-detection
```

## MACsec

### MACsec Summary

License is not installed.

FIPS restrictions enabled.

### MACsec Device Configuration

```eos
!
mac security
   fips restrictions
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

## Quality Of Service

### QOS

#### QOS Summary

QOS rewrite DSCP: **disabled**

##### QOS Mappings

| COS to Traffic Class mappings |
| ----------------------------- |
| 1 2 3 4 to traffic-class 2 |
| 3 to traffic-class 3 |

#### QOS Device Configuration

```eos
!
qos map cos 1 2 3 4 to traffic-class 2
qos map cos 3 to traffic-class 3
```

### Priority Flow Control

#### Global Settings

##### Priority Flow Control Watchdog Settings

| Action | Timeout | Recovery | Polling | Override Action Drop |
| ------ | ------- | -------- | ------- |
| errdisable | - | - | - | True |

```eos
!
priority-flow-control pause watchdog override action drop
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
