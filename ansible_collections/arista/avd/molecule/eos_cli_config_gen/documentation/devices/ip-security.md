# ip-security

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [IP Security](#ip-security-1)
  - [IKE policies](#ike-policies)
  - [Security Association policies](#security-association-policies)
  - [IPSec profiles](#ipsec-profiles)
  - [Key controller](#key-controller)
  - [IP Security Device Configuration](#ip-security-device-configuration)

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

## IP Security

- Hardware encryption is disabled

### IKE policies

| Policy name | IKE lifetime | Encryption | DH group | Local ID | Integrity |
| ----------- | ------------ | ---------- | -------- | -------- | --------- |
| IKE-1 | 24 | aes256 | 20 | 192.168.100.1 | md5 |
| IKE-2 | - | - | - | - | sha512 |
| IKE-FQDN | - | - | - | fqdn.local | - |
| IKE-UFQDN | - | - | - | my.awesome@fqdn.local | - |

### Security Association policies

| Policy name | ESP Integrity | ESP Encryption | Lifetime | PFS DH Group |
| ----------- | ------------- | -------------- | -------- | ------------ |
| SA-1 | - | aes128 | - | 14 |
| SA-2 | - | aes128 | 42 gigabytes | 14 |
| SA-3 | disabled | disabled | 8 hours | 17 |
| SA-4 | md5 | 3des | - | - |
| SA-5 | sha512 | - | - | - |
| SA-6 | sha384 | - | - | - |
| SA-7 | - | - | - | - |

### IPSec profiles

| Profile name | IKE policy | SA policy | Connection | DPD Interval | DPD Time | DPD action | Mode | Flow Parallelization |
| ------------ | ---------- | ----------| ---------- | ------------ | -------- | ---------- | ---- | -------------------- |
| Profile-1 | IKE-1 | SA-1 | start | - | - | - | transport | - |
| Profile-2 | - | SA-2 | start | - | - | - | tunnel | False |
| Profile-3 | - | SA-3 | start | - | - | - | tunnel | True |
| Profile-4 | - | - | - | - | - | - | - | - |

### Key controller

| Profile name |
| ------------ |
| Profile-1 |

### IP Security Device Configuration

```eos
!
ip security
   ike policy IKE-1
      integrity md5
      ike-lifetime 24
      encryption aes256
      dh-group 20
      local-id 192.168.100.1
   !
   ike policy IKE-2
      integrity sha512
   !
   ike policy IKE-FQDN
      local-id fqdn fqdn.local
   !
   ike policy IKE-UFQDN
      local-id fqdn my.awesome@fqdn.local
   !
   sa policy SA-1
      esp encryption aes128
      pfs dh-group 14
   !
   sa policy SA-2
      esp encryption aes128
      sa lifetime 42 gigabytes
      pfs dh-group 14
   !
   sa policy SA-3
      esp encryption null
      esp integrity null
      sa lifetime 8 hours
      pfs dh-group 17
   !
   sa policy SA-4
      esp encryption 3des
      esp integrity md5
   !
   sa policy SA-5
      esp integrity sha512
   !
   sa policy SA-6
      esp integrity sha384
   !
   sa policy SA-7
   !
   profile Profile-1
      ike-policy IKE-1
      sa-policy SA-1
      connection start
      shared-key 7 <removed>
      dpd 42 666 clear
      mode transport
   !
   profile Profile-2
      sa-policy SA-2
      connection start
      shared-key 7 <removed>
      mode tunnel
   !
   profile Profile-3
      sa-policy SA-3
      connection start
      shared-key 7 <removed>
      flow parallelization encapsulation udp
      mode tunnel
   !
   profile Profile-4
   !
   key controller
      profile Profile-1
   hardware encryption disabled
```
