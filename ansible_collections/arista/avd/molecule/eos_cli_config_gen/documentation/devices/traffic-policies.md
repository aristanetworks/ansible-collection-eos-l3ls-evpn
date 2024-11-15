# traffic-policies

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
  - [Traffic Policies information](#traffic-policies-information)

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

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   traffic-policy input BLUE-C1-POLICY
   traffic-policy output BLUE-C2-POLICY
   no switchport
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel2
   traffic-policy input BLUE-C1-POLICY
   traffic-policy output BLUE-C2-POLICY
   no switchport
```

### Traffic Policies information

#### IPv4 Field Sets

| Field Set Name | IPv4 Prefixes |
| -------------- | ------------- |
| DEMO-01 | 10.0.0.0/8<br/>192.168.0.0/16 |
| DEMO-02 | 172.16.0.0/12<br/>224.0.0.0/8 |
| DEMO-03 | - |

#### L4 Port Field Sets

| Field Set Name | L4 Ports |
| -------------- | -------- |
| SERVICE-DEMO | 10,20,80,440-450 |
| SERVICE-DEMO2 | - |

#### Traffic Policies

##### BLUE-C1-POLICY

| Match set | Type | Sources | Destinations | Protocol | Source Port(s) | Source Field(s) | Destination port(s) | Destination Field(s) | Action |
| --------- | ---- | ------- | ------------ | -------- | -------------- | --------------- | ------------------- | -------------------- | ------ |
| BLUE-C1-POLICY-01 | ipv4 | 10.0.0.0/8<br/>192.168.0.0/16 | DEMO-01 | tcp<br/>udp | 1,10-20<br/>any | -<br/>SERVICE-DEMO | any<br/>any | -<br/>- | action: PASS<br/>traffic-class: 5 |
| BLUE-C1-POLICY-02 | ipv4 | DEMO-01<br/>DEMO-02 | any | tcp<br/>icmp | any<br/>- | -<br/>- | any<br/>- | SERVICE-DEMO<br/>- | action: PASS<br/>counter: DEMO-TRAFFIC<br/>dscp marking: 60 |
| BLUE-C1-POLICY-03 | ipv4 | DEMO-01 | any | icmp | - | - | - | - | action: DROP<br/>counter: DROP-PACKETS<br/>logging |
| BLUE-C1-POLICY-04 | ipv4 | DEMO-02 | DEMO-01 | tcp<br/>icmp | 22<br/>- | -<br/>- | 80<br/>- | -<br/>- | action: PASS<br/>traffic-class: 5 |
| BLUE-C1-POLICY-05 | ipv4 | DEMO-02 | DEMO-01 | bgp | - | - | - | - | action: PASS<br/>traffic-class: 5 |
| BLUE-C1-POLICY-06 | ipv4 | any | any | neighbors<br/>udp<br/>tcp<br/>icmp | -<br/>22<br/>22<br/>- | -<br/>-<br/>-<br/>- | -<br/>1,10-20<br/>any<br/>- | -<br/>-<br/>-<br/>- | action: PASS |
| BLUE-C1-POLICY-07 | ipv4 | any | 10.0.0.0/8<br/>192.168.0.0/16 | - | - | - | - | - | default action: PASS |
| BLUE-C1-POLICY-08 | ipv4 | any | DEMO-01 | udp<br/>tcp | any<br/>any | -<br/>SERVICE-DEMO-SRC | 1,10-20<br/>any | -<br/>SERVICE-DEMO-DST | default action: PASS |

##### BLUE-C2-POLICY

| Match set | Type | Sources | Destinations | Protocol | Source Port(s) | Source Field(s) | Destination port(s) | Destination Field(s) | Action |
| --------- | ---- | ------- | ------------ | -------- | -------------- | --------------- | ------------------- | -------------------- | ------ |
| BLUE-C2-POLICY-01 | ipv4 | 10.0.0.0/8<br/>192.168.0.0/16 | any | tcp<br/>icmp | 1,10-20<br/>- | -<br/>- | any<br/>- | -<br/>- | action: PASS<br/>traffic-class: 5 |
| BLUE-C2-POLICY-02 | ipv4 | DEMO-01<br/>DEMO-02 | any | tcp<br/>icmp | any<br/>- | SERVICE-DEMO<br/>- | any<br/>- | -<br/>- | action: PASS<br/>counter: DEMO-TRAFFIC<br/>dscp marking: 60 |
| BLUE-C2-POLICY-03 | ipv4 | DEMO-01 | any | tcp | any | - | any | - | action: DROP |

##### BLUE-C3-POLICY

##### BLUE-C4-POLICY

##### BLUE-C5-POLICY

##### BLUE-C6-POLICY

##### BLUE-C7-POLICY

| Match set | Type | Sources | Destinations | Protocol | Source Port(s) | Source Field(s) | Destination port(s) | Destination Field(s) | Action |
| --------- | ---- | ------- | ------------ | -------- | -------------- | --------------- | ------------------- | -------------------- | ------ |
| BLUE-C7-POLICY-01 | ipv4 | any | any | neighbors | - | - | - | - | default action: PASS |

##### Traffic-Policy Interfaces

| Interface | Input Traffic-Policy | Output Traffic-Policy |
| --------- | -------------------- | --------------------- |
| Ethernet1 | BLUE-C1-POLICY | BLUE-C2-POLICY |
| Port-Channel2 | BLUE-C1-POLICY | BLUE-C2-POLICY |

#### Traffic Policies Device Configuration

```eos
!
traffic-policies
   field-set l4-port SERVICE-DEMO
      10,20,80,440-450
   !
   field-set l4-port SERVICE-DEMO2
   field-set ipv4 prefix DEMO-01
      10.0.0.0/8 192.168.0.0/16
   !
   field-set ipv4 prefix DEMO-02
      172.16.0.0/12 224.0.0.0/8
   !
   field-set ipv4 prefix DEMO-03
   counter interface per-interface ingress
   !
   traffic-policy BLUE-C1-POLICY
      counter DEMO-TRAFFIC DROP-PACKETS
      !
      match BLUE-C1-POLICY-01 ipv4
         source prefix 10.0.0.0/8 192.168.0.0/16
         destination prefix field-set DEMO-01
         protocol tcp source port 1,10-20
         protocol udp source port field-set SERVICE-DEMO
         ttl 10, 20-30
         !
         actions
            set traffic class 5
      !
      match BLUE-C1-POLICY-02 ipv4
         source prefix field-set DEMO-01 DEMO-02
         protocol tcp flags established
         protocol tcp destination port field-set SERVICE-DEMO
         protocol icmp
         !
         actions
            count DEMO-TRAFFIC
            set dscp 60
      !
      match BLUE-C1-POLICY-03 ipv4
         source prefix field-set DEMO-01
         protocol icmp type echo echo-reply code all
         fragment offset 1124, 2000-2010
         !
         actions
            count DROP-PACKETS
            drop
            log
      !
      match BLUE-C1-POLICY-04 ipv4
         source prefix field-set DEMO-02
         destination prefix field-set DEMO-01
         protocol tcp flags established
         protocol tcp source port 22 destination port 80
         protocol icmp
         !
         actions
            set traffic class 5
      !
      match BLUE-C1-POLICY-05 ipv4
         source prefix field-set DEMO-02
         destination prefix field-set DEMO-01
         protocol bgp
         fragment
         !
         actions
            set traffic class 5
      !
      match BLUE-C1-POLICY-06 ipv4
         protocol neighbors bgp
      !
      match BLUE-C1-POLICY-07 ipv4
         destination prefix 10.0.0.0/8 192.168.0.0/16
      !
      match BLUE-C1-POLICY-08 ipv4
         destination prefix 10.0.0.0/8 192.168.0.0/16
         protocol udp destination port 1,10-20
         protocol tcp source port field-set SERVICE-DEMO-SRC destination port field-set SERVICE-DEMO-DST
      !
      match ipv4-all-default ipv4
         actions
            drop
      !
      match ipv6-all-default ipv6
   !
   traffic-policy BLUE-C2-POLICY
      counter DEMO-TRAFFIC
      !
      match BLUE-C2-POLICY-01 ipv4
         source prefix 10.0.0.0/8 192.168.0.0/16
         protocol tcp source port 1,10-20
         protocol icmp
         !
         actions
            set traffic class 5
      !
      match BLUE-C2-POLICY-02 ipv4
         source prefix field-set DEMO-01 DEMO-02
         protocol tcp source port field-set SERVICE-DEMO
         protocol icmp
         !
         actions
            count DEMO-TRAFFIC
            set dscp 60
      !
      match BLUE-C2-POLICY-03 ipv4
         source prefix field-set DEMO-01
         protocol tcp
         !
         actions
            drop
      !
      match ipv4-all-default ipv4
         actions
            drop
            log
      !
      match ipv6-all-default ipv6
   !
   traffic-policy BLUE-C3-POLICY
      match ipv4-all-default ipv4
         actions
            count test
            set dscp 11
            set traffic class 10
      !
      match ipv6-all-default ipv6
   !
   traffic-policy BLUE-C4-POLICY
      match ipv4-all-default ipv4
      !
      match ipv6-all-default ipv6
         actions
            count test
            set dscp 11
            set traffic class 10
   !
   traffic-policy BLUE-C5-POLICY
      match ipv4-all-default ipv4
      !
      match ipv6-all-default ipv6
         actions
            drop
            log
   !
   traffic-policy BLUE-C6-POLICY
      match ipv4-all-default ipv4
      !
      match ipv6-all-default ipv6
         actions
            drop
   !
   traffic-policy BLUE-C7-POLICY
      match BLUE-C7-POLICY-01 ipv4
         protocol neighbors bgp enforce ttl maximum-hops
      !
      match ipv4-all-default ipv4
      !
      match ipv6-all-default ipv6
```
