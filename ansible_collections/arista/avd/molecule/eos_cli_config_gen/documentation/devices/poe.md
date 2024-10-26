# poe

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [LLDP](#lldp)
  - [LLDP Summary](#lldp-summary)
  - [LLDP Device Configuration](#lldp-device-configuration)
- [Power Over Ethernet (PoE)](#power-over-ethernet-poe)
  - [PoE Summary](#poe-summary)
  - [PoE Device Configuration](#poe-device-configuration)

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

## LLDP

### LLDP Summary

#### LLDP Global Settings

| Enabled | Management Address | Management VRF | Timer | Hold-Time | Re-initialization Timer | Drop Received Tagged Packets |
| ------- | ------------------ | -------------- | ----- | --------- | ----------------------- | ---------------------------- |
| True | - | Default | 30 | 120 | 2 | - |

#### LLDP Explicit TLV Transmit Settings

| TLV | Transmit |
| --- | -------- |
| power-via-mdi | False |
| system-capabilities | True |

### LLDP Device Configuration

```eos
!
no lldp tlv transmit power-via-mdi
lldp tlv transmit system-capabilities
```

## Power Over Ethernet (PoE)

### PoE Summary

#### PoE Global

| Reboot Action | Shutdown Action | LLDP Negotiation |
| ------------------- | -------------------- | ----------------------|
| maintain | power-off | False |

### PoE Device Configuration

```eos
!
poe
   reboot action maintain
   interface shutdown action power-off
```
