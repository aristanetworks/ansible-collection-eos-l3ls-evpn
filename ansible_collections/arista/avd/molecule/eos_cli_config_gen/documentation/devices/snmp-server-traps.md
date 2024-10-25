# snmp-server-traps

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitoring](#monitoring)
  - [SNMP](#snmp)

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

### SNMP

#### SNMP Configuration Summary

| Contact | Location | SNMP Traps | State |
| ------- | -------- | ---------- | ----- |
| DC1_OPS | DC1 | All | Disabled |
| DC1_OPS | DC1 | bgp, bridge, lldp, mpls, msdp backward-transition, msdp established, snmp link-down, snmpConfigManEvent | Enabled |
| DC1_OPS | DC1 | bgp arista-backward-transition, bridge arista-mac-age | Disabled |

#### SNMP VRF Status

| VRF | Status |
| --- | ------ |
| default | Disabled |
| MGMT | Enabled |

#### SNMP Device Configuration

```eos
!
snmp-server contact DC1_OPS
snmp-server location DC1
snmp-server enable traps bgp
no snmp-server enable traps bgp arista-backward-transition
snmp-server enable traps bridge
no snmp-server enable traps bridge arista-mac-age
snmp-server enable traps lldp
snmp-server enable traps mpls
snmp-server enable traps msdp backward-transition
snmp-server enable traps msdp established
snmp-server enable traps snmp link-down
snmp-server enable traps snmpConfigManEvent
no snmp-server vrf default
snmp-server vrf MGMT
```
