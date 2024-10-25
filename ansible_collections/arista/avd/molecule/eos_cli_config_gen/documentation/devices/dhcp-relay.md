# dhcp-relay

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [DHCP Relay](#dhcp-relay-1)
  - [DHCP Relay Summary](#dhcp-relay-summary)
  - [DHCP Relay Device Configuration](#dhcp-relay-device-configuration)

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

## DHCP Relay

### DHCP Relay Summary

- DHCP Relay is disabled for tunnelled requests
- DHCP Relay is disabled for MLAG peer-link requests

| DHCP Relay Servers |
| ------------------ |
| dhcp-relay-server1 |
| dhcp-relay-server2 |

### DHCP Relay Device Configuration

```eos
!
dhcp relay
   tunnel requests disabled
   mlag peer-link requests disabled
   server dhcp-relay-server1
   server dhcp-relay-server2
```
