# ip-dhcp-relay

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [IP DHCP Relay](#ip-dhcp-relay-1)
  - [IP DHCP Relay Summary](#ip-dhcp-relay-summary)
  - [IP DHCP Relay Device Configuration](#ip-dhcp-relay-device-configuration)

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

## IP DHCP Relay

### IP DHCP Relay Summary

IP DHCP Relay Option 82 is enabled.

DhcpRelay Agent is in always-on mode.

Forwarding requests with secondary IP addresses in the "giaddr" field is allowed.

### IP DHCP Relay Device Configuration

```eos
!
ip dhcp relay information option
ip dhcp relay always-on
ip dhcp relay all-subnets default
```
