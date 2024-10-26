# ipv6-dhcp-relay

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [IPv6 DHCP Relay](#ipv6-dhcp-relay-1)
  - [IPv6 DHCP Relay Summary](#ipv6-dhcp-relay-summary)
  - [IPv6 DHCP Relay Device Configuration](#ipv6-dhcp-relay-device-configuration)

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

## IPv6 DHCP Relay

### IPv6 DHCP Relay Summary

DhcpRelay Agent is in always-on mode.

Forwarding requests with additional IPv6 addresses in the "giaddr" field is allowed.

Add Option 79 - Link Layer Address Option.

Add RemoteID option 37 in format MAC address and interface ID.

### IPv6 DHCP Relay Device Configuration

```eos
!
ipv6 dhcp relay always-on
ipv6 dhcp relay all-subnets default
ipv6 dhcp relay option link-layer address
ipv6 dhcp relay option remote-id format %m:%i
```
