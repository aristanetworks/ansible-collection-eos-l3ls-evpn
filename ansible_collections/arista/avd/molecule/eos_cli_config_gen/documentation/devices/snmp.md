# snmp

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitoring](#monitoring)
  - [SNMP](#snmp-1)

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
| DC1_OPS | DC1 | All | Enabled |

#### SNMP EngineID Configuration

| Type | EngineID (Hex) | IP | Port |
| ---- | -------------- | -- | ---- |
| local | 424242424242424242 | - | - |
| remote | 6172697374615F6970 | 1.1.1.1 | - |
| remote | DEADBEEFCAFE123456 | 2.2.2.2 | 1337 |

#### SNMP ACLs

| IP | ACL | VRF |
| -- | --- | --- |
| IPv4 | SNMP-MGMT | MGMT |
| IPv4 | onur | default |
| IPv6 | SNMP-MGMT | MGMT |
| IPv6 | onur_v6 | default |

#### SNMP Local Interfaces

| Local Interface | VRF |
| --------------- | --- |
| Management1 | MGMT |
| Loopback0 | default |
| Loopback12 | Tenant_A_APP_Zone |

#### SNMP VRF Status

| VRF | Status |
| --- | ------ |
| default | Disabled |
| MGMT | Enabled |

#### SNMP Hosts Configuration

| Host | VRF | Community | Username | Authentication level | SNMP Version |
| ---- |---- | --------- | -------- | -------------------- | ------------ |
| 10.6.75.121 | MGMT | <removed> | - | - | 1 |
| 10.6.75.121 | MGMT | <removed> | - | - | 2c |
| 10.6.75.122 | MGMT | <removed> | - | - | 2c |
| 10.6.75.99 | MGMT | - | USER-READ-AUTH-NO-PRIV | auth | 3 |
| 10.6.75.99 | MGMT | - | USER-WRITE | auth | 3 |
| 10.6.75.100 | MGMT | - | USER-READ-AUTH-PRIV | priv | 3 |

#### SNMP Views Configuration

| View | MIB Family Name | Status |
| ---- | --------------- | ------ |
| VW-WRITE | iso | Included |
| VW-READ | iso | Included |

#### SNMP Communities

| Community | Access | Access List IPv4 | Access List IPv6 | View |
| --------- | ------ | ---------------- | ---------------- | ---- |
| <removed> | ro | onur | - | - |
| <removed> | rw | SNMP-MGMT | SNMP-MGMT | VW-READ |
| <removed> | ro | - | - | - |

#### SNMP Groups Configuration

| Group | SNMP Version | Authentication | Read | Write | Notify |
| ----- | ------------ | -------------- | ---- | ----- | ------ |
| GRP-READ-ONLY | v3 | priv | v3read | - | - |
| GRP-READ-WRITE | v3 | auth | v3read | v3write | - |

#### SNMP Users Configuration

| User | Group | Version | Authentication | Privacy | Remote Address | Remote Port | Engine ID |
| ---- | ----- | ------- | -------------- | ------- | -------------- | ----------- | --------- |
| USER-READ-NO-AUTH-NO-PRIV | GRP-READ-ONLY | v3 | - | - | - | - | - |
| USER-READ-AUTH-NO-PRIV | GRP-READ-ONLY | v3 | sha | - | - | - | - |
| USER-READ-AUTH-PRIV | GRP-READ-ONLY | v3 | sha | aes | - | - | - |
| USER-READ-NO-AUTH-NO-PRIV-LOC | GRP-READ-ONLY | v3 | - | - | - | - | 424242424242424242 |
| USER-READ-AUTH-NO-PRIV-LOC | GRP-READ-ONLY | v3 | sha | - | - | - | 424242424242424242 |
| USER-READ-AUTH-PRIV-LOC | GRP-READ-ONLY | v3 | sha | aes | - | - | 424242424242424242 |
| USER-WRITE | GRP-READ-WRITE | v3 | sha | aes | - | - | - |
| REMOTE-USER-IP-ONLY | GRP-REMOTE | v3 | - | - | 42.42.42.42 | - | - |
| REMOTE-USER-IP-PORT | GRP-REMOTE | v3 | - | - | 42.42.42.42 | 666 | - |
| REMOTE-USER-IP-LOCALIZED | GRP-REMOTE | v3 | sha | - | 42.42.42.42 | - | DEADBEEFCAFE123456 |

#### SNMP Device Configuration

```eos
!
snmp-server ipv4 access-list SNMP-MGMT vrf MGMT
snmp-server ipv4 access-list onur
snmp-server ipv6 access-list SNMP-MGMT vrf MGMT
snmp-server ipv6 access-list onur_v6
snmp-server engineID local 424242424242424242
snmp-server contact DC1_OPS
snmp-server location DC1
snmp-server local-interface Loopback0
snmp-server vrf Tenant_A_APP_Zone local-interface Loopback12
snmp-server vrf MGMT local-interface Management1
snmp-server view VW-READ iso included
snmp-server view VW-WRITE iso included
snmp-server community <removed> ro onur
snmp-server community <removed> view VW-READ rw ipv6 SNMP-MGMT SNMP-MGMT
snmp-server community <removed> ro
snmp-server group GRP-READ-ONLY v3 priv read v3read
snmp-server group GRP-READ-WRITE v3 auth read v3read write v3write
snmp-server user REMOTE-USER-IP-LOCALIZED GRP-REMOTE remote 42.42.42.42 v3 localized DEADBEEFCAFE123456 auth sha <removed>
snmp-server user REMOTE-USER-IP-ONLY GRP-REMOTE remote 42.42.42.42 v3
snmp-server user REMOTE-USER-IP-PORT GRP-REMOTE remote 42.42.42.42 udp-port 666 v3
snmp-server user USER-READ-AUTH-NO-PRIV GRP-READ-ONLY v3 auth sha <removed>
snmp-server user USER-READ-AUTH-NO-PRIV-LOC GRP-READ-ONLY v3 localized 424242424242424242 auth sha <removed>
snmp-server user USER-READ-AUTH-PRIV GRP-READ-ONLY v3 auth sha <removed> priv aes <removed>
snmp-server user USER-READ-AUTH-PRIV-LOC GRP-READ-ONLY v3 localized 424242424242424242 auth sha <removed> priv aes <removed>
snmp-server user USER-READ-NO-AUTH-NO-PRIV GRP-READ-ONLY v3
snmp-server user USER-READ-NO-AUTH-NO-PRIV-LOC GRP-READ-ONLY v3
snmp-server user USER-WRITE GRP-READ-WRITE v3 auth sha <removed> priv aes <removed>
snmp-server engineID remote 1.1.1.1 6172697374615F6970
snmp-server engineID remote 2.2.2.2 udp-port 1337 DEADBEEFCAFE123456
snmp-server host 10.6.75.99 vrf MGMT version 3 auth USER-READ-AUTH-NO-PRIV
snmp-server host 10.6.75.99 vrf MGMT version 3 auth USER-WRITE
snmp-server host 10.6.75.100 vrf MGMT version 3 priv USER-READ-AUTH-PRIV
snmp-server host 10.6.75.121 vrf MGMT version 1 <removed>
snmp-server host 10.6.75.121 vrf MGMT version 2c <removed>
snmp-server host 10.6.75.122 vrf MGMT version 2c <removed>
snmp-server enable traps
no snmp-server vrf default
snmp-server vrf MGMT
snmp-server ifmib ifspeed shape-rate
```
