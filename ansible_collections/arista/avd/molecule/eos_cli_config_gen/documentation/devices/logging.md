# logging

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitoring](#monitoring)
  - [Logging](#logging-1)

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

### Logging

#### Logging Servers and Features Summary

| Type | Level |
| -----| ----- |
| Console | errors |
| Buffer | warnings |
| Trap | disabled |
| Synchronous | critical |

| Format Type | Setting |
| ----------- | ------- |
| Timestamp | traditional year timezone |
| Hostname | hostname |
| Sequence-numbers | false |
| RFC5424 | True |

| VRF | Source Interface |
| --- | ---------------- |
| default | Loopback0 |
| mgt | Management0 |

| VRF | Hosts | Ports | Protocol |
| --- | ----- | ----- | -------- |
| default | 20.20.20.7 | Default | UDP |
| default | 50.50.50.7 | 100, 200 | TCP |
| default | 60.60.60.7 | 100, 200 | UDP |
| default | 2001:db8::20:7 | Default | UDP |
| default | 2001:db8::50:7 | 100, 200 | TCP |
| default | 2001:db8::60:7 | 100, 200 | UDP |
| mgt | 10.10.10.7 | Default | UDP |
| mgt | 30.30.30.7 | 100, 200 | TCP |
| mgt | 40.40.40.7 | 300, 400 | UDP |
| mgt | 2001:db8::10:7 | Default | UDP |
| mgt | 2001:db8::30:7 | 100, 200 | TCP |
| mgt | 2001:db8::40:7 | 300, 400 | UDP |
| vrf_with_no_source_interface | 1.2.3.4 | Default | UDP |
| vrf_with_no_source_interface | 2001:db8::1:2:3:4 | Default | UDP |

| Facility | Severity |
| -------- | -------- |
| AAA | warnings |
| ACL | critical |
| BGP | 0 |

#### Logging Servers and Features Device Configuration

```eos
!
logging event storm-control discards global
logging event storm-control discards interval 10
!
logging event congestion-drops interval 10
!
logging repeat-messages
logging buffered 1000000 warnings
no logging trap
logging console errors
logging synchronous level critical
logging host 20.20.20.7
logging host 50.50.50.7 100 200 protocol tcp
logging host 60.60.60.7 100 200
logging host 2001:db8::20:7
logging host 2001:db8::50:7 100 200 protocol tcp
logging host 2001:db8::60:7 100 200
logging vrf mgt host 10.10.10.7
logging vrf mgt host 30.30.30.7 100 200 protocol tcp
logging vrf mgt host 40.40.40.7 300 400
logging vrf mgt host 2001:db8::10:7
logging vrf mgt host 2001:db8::30:7 100 200 protocol tcp
logging vrf mgt host 2001:db8::40:7 300 400
logging vrf vrf_with_no_source_interface host 1.2.3.4
logging vrf vrf_with_no_source_interface host 2001:db8::1:2:3:4
logging format timestamp traditional year timezone
logging format rfc5424
logging source-interface Loopback0
logging vrf mgt source-interface Management0
!
logging level AAA warnings
logging level ACL critical
logging level BGP 0
!
no logging event link-status global
```
