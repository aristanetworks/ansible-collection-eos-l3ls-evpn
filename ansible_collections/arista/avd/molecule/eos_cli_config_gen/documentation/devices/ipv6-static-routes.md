# ipv6-static-routes

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Routing](#routing)
  - [IPv6 Static Routes](#ipv6-static-routes-1)

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

### IPv6 Static Routes

#### IPv6 Static Routes Summary

| VRF | Destination Prefix | Next Hop IP             | Exit interface      | Administrative Distance       | Tag               | Route Name                    | Metric         |
| --- | ------------------ | ----------------------- | ------------------- | ----------------------------- | ----------------- | ----------------------------- | -------------- |
| default | 2a01:cb04:4e6:d300::/64 | 2a01:cb04:4e6:d100::1 | vlan101 | 1 | - | - | - |
| default | 2a01:cb04:4e6:d400::/64 | 2a01:cb04:4e6:d100::1 | vlan101 | 200 | 666 | RT-TO-FAKE-DMZ | - |
| default | 2a01:cb04:4e6:d400::/64 | 2a01:cb04:4e6:d100::1 | vlan101 | 200 | 666 | RT-TO-FAKE-DB-ZONE | 100 |
| customer01 | 2a01:cb04:4e6:a300::/64 | 2a01:cb04:4e6:100::1 | vlan101 | 1 | - | - | - |
| customer01 | 2a01:cb04:4e6:a400::/64 | 2a01:cb04:4e6:100::1 | vlan101 | 201 | 667 | RT-TO-FAKE-DMZ | - |
| customer01 | 2b01:cb04:4e6:a400::/64 | 2a01:cb04:4e6:102::1 (tracked with BFD) | vlan102 | 201 | 102 | Track-BFD | 100 |
| customer01 | 2c01:cb04:4e6:a400::/64 | - | vlan102 | 201 | 102 | No-Track-BFD | - |

#### Static Routes Device Configuration

```eos
!
ipv6 route 2a01:cb04:4e6:d300::/64 Vlan101 2a01:cb04:4e6:d100::1
ipv6 route 2a01:cb04:4e6:d400::/64 Vlan101 2a01:cb04:4e6:d100::1 200 tag 666 name RT-TO-FAKE-DMZ
ipv6 route 2a01:cb04:4e6:d400::/64 Vlan101 2a01:cb04:4e6:d100::1 200 tag 666 name RT-TO-FAKE-DB-ZONE metric 100
ipv6 route vrf customer01 2a01:cb04:4e6:a300::/64 Vlan101 2a01:cb04:4e6:100::1
ipv6 route vrf customer01 2a01:cb04:4e6:a400::/64 Vlan101 2a01:cb04:4e6:100::1 201 tag 667 name RT-TO-FAKE-DMZ
ipv6 route vrf customer01 2b01:cb04:4e6:a400::/64 Vlan102 2a01:cb04:4e6:102::1 track bfd 201 tag 102 name Track-BFD metric 100
ipv6 route vrf customer01 2c01:cb04:4e6:a400::/64 Vlan102 201 tag 102 name No-Track-BFD
```
