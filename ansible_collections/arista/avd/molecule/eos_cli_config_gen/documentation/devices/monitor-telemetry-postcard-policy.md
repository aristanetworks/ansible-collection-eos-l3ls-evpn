# monitor-telemetry-postcard-policy

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitoring](#monitoring)
  - [Monitor Telemetry Postcard Policy](#monitor-telemetry-postcard-policy-1)

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

### Monitor Telemetry Postcard Policy

#### Sample Policy Summary

##### samplepo1

###### Match rules

| Rule Name | Rule Type | Source Prefix | Destination Prefix | Protocol | Source Ports | Destination Ports |
| --------- | --------- | ------------- | ------------------ | -------- | ------------ | ----------------- |
| rule1 | ipv4 | 3.4.5.0/24 | 10.3.3.0/24 | tcp<br>udp | -<br>98 | 77, 78-80, 82<br>99 |
| rule2 | ipv6 | 5::0/128 | 4::0/128 | udp | - | 747, 748-800 |
| rule3 | ipv4 | - | - | - | - | - |

##### samplepo2

###### Match rules

| Rule Name | Rule Type | Source Prefix | Destination Prefix | Protocol | Source Ports | Destination Ports |
| --------- | --------- | ------------- | ------------------ | -------- | ------------ | ----------------- |
| rule1 | ipv4 | 3.4.5.0/24 | 10.3.3.0/24 | udp | bgp | https |

#### Telemetry Postcard Policy Profiles

| Profile Name | Ingress Sample Policy |
| ------------ | --------------------- |
| profile1 | samplepo1 |
| profile2 | samplepo2 |

#### Monitor Telemetry Postcard Policy Configuration

```eos
!
monitor telemetry postcard policy
   no disabled
   ingress sample rate 16384
   marker vxlan header word 0 bit 30
   ingress collection gre source 10.3.3.3 destination 10.3.3.4 version 2
   !
   sample policy samplepo1
      match rule1 ipv4
         source prefix 3.4.5.0/24
         destination prefix 10.3.3.0/24
         protocol tcp destination port 77, 78-80, 82
         protocol udp source port 98 destination port 99
      !
      match rule2 ipv6
         source prefix 5::0/128
         destination prefix 4::0/128
         protocol udp destination port 747, 748-800
      !
      match rule3 ipv4
   !
   sample policy samplepo2
      match rule1 ipv4
         source prefix 3.4.5.0/24
         destination prefix 10.3.3.0/24
         protocol udp source port bgp destination port https
   !
   profile profile1
      ingress sample policy samplepo1
   !
   profile profile2
      ingress sample policy samplepo2
```
