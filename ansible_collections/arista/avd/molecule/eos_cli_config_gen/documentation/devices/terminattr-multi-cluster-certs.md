# terminattr-multi-cluster-certs

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)

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

### TerminAttr Daemon

#### TerminAttr Daemon Summary

| CV Compression | CloudVision Servers | VRF | Authentication | Smash Excludes | Ingest Exclude | Bypass AAA |
| -------------- | ------------------- | --- | -------------- | -------------- | -------------- | ---------- |
| gzip | 10.20.20.1:9910 | mgt | certs,/persist/secure/ssl/terminattr/DC1/certs/client.crt,/persist/secure/ssl/terminattr/DC1/keys/client.key,/persist/secure/ssl/terminattr/DC1/certs/ca.crt | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | False |
| gzip | 10.30.30.1:9910 | mgt | certs,/persist/secure/ssl/terminattr/DC2/certs/client.crt,/persist/secure/ssl/terminattr/DC2/keys/client.key,/persist/secure/ssl/terminattr/DC2/certs/ca.crt | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | False |

#### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvopt DC1.addr=10.20.20.1:9910 -cvopt DC1.auth=certs,/persist/secure/ssl/terminattr/DC1/certs/client.crt,/persist/secure/ssl/terminattr/DC1/keys/client.key,/persist/secure/ssl/terminattr/DC1/certs/ca.crt -cvopt DC1.vrf=mgt -cvopt DC1.sourceintf=Loopback10 -cvopt DC2.addr=10.30.30.1:9910 -cvopt DC2.auth=certs,/persist/secure/ssl/terminattr/DC2/certs/client.crt,/persist/secure/ssl/terminattr/DC2/keys/client.key,/persist/secure/ssl/terminattr/DC2/certs/ca.crt -cvopt DC2.vrf=mgt -cvopt DC2.sourceintf=Vlan500 -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -taillogs
   no shutdown
```
