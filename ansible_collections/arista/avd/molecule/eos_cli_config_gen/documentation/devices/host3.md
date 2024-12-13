# host3

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

### PTP

#### PTP Summary

| Clock ID | Source IP | Priority 1 | Priority 2 | TTL | Domain | Mode | Forward Unicast |
| -------- | --------- | ---------- | ---------- | --- | ------ | ---- | --------------- |
| - | - | - | - | - | - | - | - |

#### PTP Device Configuration

```eos
!
no ptp monitor
```

### Management SSH

#### SSH Timeout and Management

| Idle Timeout | SSH Management |
| ------------ | -------------- |
| default | Enabled |

#### Max number of SSH sessions limit and per-host limit

| Connection Limit | Max from a single Host |
| ---------------- | ---------------------- |
| - | - |

#### Ciphers and Algorithms

| Ciphers | Key-exchange methods | MAC algorithms | Hostkey server algorithms |
|---------|----------------------|----------------|---------------------------|
| default | default | default | default |

#### VRFs

| VRF | Status |
| --- | ------ |
| mgt | Disabled |

#### Management SSH Device Configuration

```eos
!
management ssh
   !
   vrf mgt
```

## CVX

CVX is enabled

### CVX Services

| Service | Enabled | Settings |
| ------- | ------- | -------- |
| MCS | - | Redis Password Set |
| VXLAN | - | VTEP MAC learning: control-plane |

### CVX Device Configuration

```eos
!
cvx
   no shutdown
   !
   service mcs
      redis password 7 <removed>
   !
   service vxlan
      vtep mac-learning control-plane
```

## Monitoring

### TerminAttr Daemon

#### TerminAttr Daemon Summary

| CV Compression | CloudVision Servers | VRF | Authentication | Smash Excludes | Ingest Exclude | Bypass AAA |
| -------------- | ------------------- | --- | -------------- | -------------- | -------------- | ---------- |
| gzip | apiserver.arista.io:443 | mgt | token-secure,/tmp/cv-onboarding-token | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | False |

#### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvaddr=apiserver.arista.io:443 -cvauth=token-secure,/tmp/cv-onboarding-token -cvvrf=mgt -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -taillogs -ipfix=false -sflow=false
   no shutdown
```

### Logging

#### Logging Servers and Features Summary

| Type | Level |
| -----| ----- |
| Console | disabled |

| Format Type | Setting |
| ----------- | ------- |
| Timestamp | traditional year timezone |
| Hostname | hostname |
| Sequence-numbers | false |
| RFC5424 | False |

#### Logging Servers and Features Device Configuration

```eos
!
no logging console
logging format timestamp traditional year timezone
```

### MCS Client Summary

MCS client is shutdown

| Secondary CVX cluster | Server Hosts | Enabled |
| --------------------- | ------------ | ------- |
| default | - | - |

#### MCS Client Device Configuration

```eos
!
mcs client
   shutdown
   !
   cvx secondary default
```

### Tap Aggregation

#### Tap Aggregation Summary

| Settings | Values |
| -------- | ------ |
| Mode Exclusive | True |
| Mac Timestamp | Replace Source-Mac |
| Mac FCS Error | pass-through |

#### Tap Aggregation Device Configuration

```eos
!
tap aggregation
   mode exclusive
   mac timestamp replace source-mac
   mac fcs-error pass-through
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **mstp**

#### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 4096 |
| 100-200 | 8192 |

#### MST Configuration

| Variable | Value |
| -------- | -------- |
| Name | test |
| Revision | 5 |
| Instance 2 | VLAN(s) 15,16,17,18 |
| Instance 3 | VLAN(s) 15 |
| Instance 4 | VLAN(s) 200-300 |

#### Global Spanning-Tree Settings

- MST PSVT Border is enabled.

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
spanning-tree mst pvst border
spanning-tree mst 0 priority 4096
spanning-tree mst 100-200 priority 8192
!
spanning-tree mst configuration
   name test
   revision 5
   instance 2 vlan 15,16,17,18
   instance 3 vlan 15
   instance 4 vlan 200-300
```

## Routing

### Router ISIS

#### Router ISIS Summary

| Settings | Value |
| -------- | ----- |
| Instance | EVPN_UNDERLAY |
| SPF Interval | 250 seconds |
| SPF Interval Wait Time| 30 milliseconds |

#### ISIS Interfaces Summary

| Interface | ISIS Instance | ISIS Metric | Interface Mode |
| --------- | ------------- | ----------- | -------------- |

#### Router ISIS Device Configuration

```eos
!
router isis EVPN_UNDERLAY
   set-overload-bit
   set-overload-bit on-startup 55
   spf-interval 250 30
   authentication mode shared-secret profile test1 algorithm md5 rx-disabled
   authentication key 0 password
   !
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65101.0001 | 192.168.255.3 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| update wait-install |
| distance bgp 20 200 200 |
| graceful-restart restart-time 300 |
| maximum-paths 2 ecmp 2 |
| graceful-restart-helper long-lived |
| bgp additional-paths send limit 5 |

#### Router BGP Device Configuration

```eos
!
router bgp 65101.0001
   router-id 192.168.255.3
   graceful-restart-helper long-lived
   no bgp default ipv4-unicast
   update wait-install
   distance bgp 20 200 200
   graceful-restart restart-time 300
   maximum-paths 2 ecmp 2
   bgp additional-paths send limit 5
   redistribute ospf include leaked route-map RM-OSPF-TO-BGP
   redistribute static
   !
   address-family ipv4 multicast
      redistribute attached-host
      redistribute connected
      redistribute isis rcf Router_BGP_Isis()
      redistribute ospf match internal
      redistribute ospfv3 match internal
      redistribute ospfv3 match external
      redistribute ospfv3 match nssa-external 2
      redistribute ospf match external
      redistribute ospf match nssa-external 2
   !
   address-family ipv6
      redistribute ospfv3 include leaked route-map RM-REDISTRIBUTE-OSPFV3
      redistribute ospfv3 match external include leaked route-map RM-REDISTRIBUTE-OSPFV3-EXTERNAL
```

## MPLS

### MPLS and LDP

#### MPLS and LDP Summary

| Setting | Value |
| -------- | ---- |
| MPLS IP Enabled | True |
| LDP Enabled | False |
| LDP Router ID | 192.168.1.2 |
| LDP Interface Disabled Default | True |
| LDP Transport-Address Interface | - |

### MPLS RSVP

#### MPLS RSVP Summary

| Setting | Value |
| ------- | ----- |

### MPLS Device Configuration

```eos
!
mpls ip
!
mpls ldp
   router-id 192.168.1.2
   interface disabled default
!
mpls rsvp
```

## Multicast

### Router Multicast

#### IP Router Multicast Summary

- Multipathing via ECMP.

#### Router Multicast Device Configuration

```eos
!
router multicast
   ipv4
      multipath deterministic
```

### Traffic Policies information

#### Traffic Policies Device Configuration

```eos
!
traffic-policies
```
