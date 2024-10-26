# errdisable

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Errdisable](#errdisable-1)
  - [Errdisable Summary](#errdisable-summary)

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

## Errdisable

### Errdisable Summary

|  Detect Cause | Enabled |
| ------------- | ------- |
| arp-inspection | True |
| dot1x | True |
| link-change | True |
| tapagg | True |
| xcvr-misconfigured | True |
| xcvr-overheat | True |
| xcvr-power-unsupported | True |

|  Detect Cause | Enabled | Interval |
| ------------- | ------- | -------- |
| bpduguard | True | 300 |
| dot1x | True | 300 |
| hitless-reload-down | True | 300 |
| lacp-rate-limit | True | 300 |
| link-flap | True | 300 |
| no-internal-vlan | True | 300 |
| portchannelguard | True | 300 |
| portsec | True | 300 |
| speed-misconfigured | True | 300 |
| tapagg | True | 300 |
| uplink-failure-detection | True | 300 |
| xcvr-misconfigured | True | 300 |
| xcvr-overheat | True | 300 |
| xcvr-power-unsupported | True | 300 |
| xcvr-unsupported | True | 300 |

```eos
!
errdisable detect cause arp-inspection
errdisable detect cause dot1x
errdisable detect cause link-change
errdisable detect cause tapagg
errdisable detect cause xcvr-misconfigured
errdisable detect cause xcvr-overheat
errdisable detect cause xcvr-power-unsupported
errdisable recovery cause bpduguard
errdisable recovery cause dot1x
errdisable recovery cause hitless-reload-down
errdisable recovery cause lacp-rate-limit
errdisable recovery cause link-flap
errdisable recovery cause no-internal-vlan
errdisable recovery cause portchannelguard
errdisable recovery cause portsec
errdisable recovery cause speed-misconfigured
errdisable recovery cause tapagg
errdisable recovery cause uplink-failure-detection
errdisable recovery cause xcvr-misconfigured
errdisable recovery cause xcvr-overheat
errdisable recovery cause xcvr-power-unsupported
errdisable recovery cause xcvr-unsupported
errdisable recovery interval 300
```
