# ip-igmp-snooping-enable

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)

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

## Multicast

### IP IGMP Snooping

#### IP IGMP Snooping Summary

| IGMP Snooping | Fast Leave | Interface Restart Query | Proxy | Restart Query Interval | Robustness Variable |
| ------------- | ---------- | ----------------------- | ----- | ---------------------- | ------------------- |
| Enabled | True | 500 | True | 30 | 2 |

| Querier Enabled | IP Address | Query Interval | Max Response Time | Last Member Query Interval | Last Member Query Count | Startup Query Interval | Startup Query Count | Version |
| --------------- | ---------- | -------------- | ----------------- | -------------------------- | ----------------------- | ---------------------- | ------------------- | ------- |
| True | 10.10.10.1 | 40 | 10 | 5 | 2 | 20 | 2 | 3 |

##### IP IGMP Snooping Vlan Summary

| Vlan | IGMP Snooping | Fast Leave | Max Groups | Proxy |
| ---- | ------------- | ---------- | ---------- | ----- |
| 23 | True | True | 20 | True |
| 24 | True | - | - | - |
| 25 | False | False | - | False |

| Vlan | Querier Enabled | IP Address | Query Interval | Max Response Time | Last Member Query Interval | Last Member Query Count | Startup Query Interval | Startup Query Count | Version |
| ---- | --------------- | ---------- | -------------- | ----------------- | -------------------------- | ----------------------- | ---------------------- | ------------------- | ------- |
| 23 | True | 10.10.23.1 | 40 | 10 | 5 | 2 | 20 | 2 | 3 |

#### IP IGMP Snooping Device Configuration

```eos
!
ip igmp snooping robustness-variable 2
ip igmp snooping restart query-interval 30
ip igmp snooping interface-restart-query 500
ip igmp snooping fast-leave
ip igmp snooping vlan 23
ip igmp snooping vlan 23 querier
ip igmp snooping vlan 23 querier address 10.10.23.1
ip igmp snooping vlan 23 querier query-interval 40
ip igmp snooping vlan 23 querier max-response-time 10
ip igmp snooping vlan 23 querier last-member-query-interval 5
ip igmp snooping vlan 23 querier last-member-query-count 2
ip igmp snooping vlan 23 querier startup-query-interval 20
ip igmp snooping vlan 23 querier startup-query-count 2
ip igmp snooping vlan 23 querier version 3
ip igmp snooping vlan 23 max-groups 20
ip igmp snooping vlan 23 fast-leave
ip igmp snooping vlan 24
no ip igmp snooping vlan 25
no ip igmp snooping vlan 25 fast-leave
ip igmp snooping querier
ip igmp snooping querier address 10.10.10.1
ip igmp snooping querier query-interval 40
ip igmp snooping querier max-response-time 10
ip igmp snooping querier last-member-query-interval 5
ip igmp snooping querier last-member-query-count 2
ip igmp snooping querier startup-query-interval 20
ip igmp snooping querier startup-query-count 2
ip igmp snooping querier version 3
!
ip igmp snooping proxy
ip igmp snooping vlan 23 proxy
no ip igmp snooping vlan 25 proxy
```
