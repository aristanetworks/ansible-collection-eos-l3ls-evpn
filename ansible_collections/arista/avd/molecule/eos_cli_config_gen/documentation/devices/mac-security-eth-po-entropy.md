# mac-security-eth-po-entropy

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Management Security](#management-security)
  - [Management Security Summary](#management-security-summary)
  - [Management Security SSL Profiles](#management-security-ssl-profiles)
  - [Management Security Device Configuration](#management-security-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Port-Channel Interfaces](#port-channel-interfaces)
- [MACsec](#macsec)
  - [MACsec Summary](#macsec-summary)
  - [MACsec Device Configuration](#macsec-device-configuration)

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

## Management Security

### Management Security Summary

| Settings | Value |
| -------- | ----- |
| Entropy sources | hardware |
| Common password encryption key | True |

### Management Security SSL Profiles

| SSL Profile Name | TLS protocol accepted | Certificate filename | Key filename | Cipher List | CRLs |
| ---------------- | --------------------- | -------------------- | ------------ | ----------- | ---- |
| SSL_PROFILE | 1.1 1.2 | SSL_CERT | SSL_KEY | - | - |

### Management Security Device Configuration

```eos
!
management security
   entropy source hardware
   password encryption-key common
   !
   ssl profile SSL_PROFILE
      tls versions 1.1 1.2
      certificate SSL_CERT key SSL_KEY
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |
| Ethernet3 | DC1-AGG01_Ethernet1 | *trunk | *1-5 | *- | *- | 3 |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | - | - | 1.1.1.1/24 | default | - | - | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   no switchport
   ip address 1.1.1.1/24
   mac security profile A1
!
interface Ethernet3
   description DC1-AGG01_Ethernet1
   channel-group 3 mode active
   mac security profile A1
```

### Port-Channel Interfaces

#### Port-Channel Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | LACP Fallback Timeout | LACP Fallback Mode | MLAG ID | EVPN ESI |
| --------- | ----------- | ---- | ----- | ----------- | ------------| --------------------- | ------------------ | ------- | -------- |
| Port-Channel3 | L2-PORT | trunk | 1-5 | - | - | - | - | - | - |

#### Port-Channel Interfaces Device Configuration

```eos
!
interface Port-Channel3
   description L2-PORT
   switchport trunk allowed vlan 1-5
   switchport mode trunk
   switchport
```

## MACsec

### MACsec Summary

License is installed.

FIPS restrictions enabled.

#### MACsec Profiles Summary

##### Profile A1

###### Settings

| Cipher | Key-Server Priority | Rekey-Period | SCI | Traffic Unprotected Fallback |
| ------ | ------------------- | ------------ | --- | ---------------------------- |
| aes128-gcm | 100 | 30 | True | allow |

###### Keys

| Key ID | Fallback |
| ------ | -------- |
| 1234a | - |
| 1234c | True |

###### L2 Protocols

| L2 Protocol | Mode |
| ----------- | ---- |
| lldp | bypass unauthorized |

##### Profile A2

###### Settings

| Cipher | Key-Server Priority | Rekey-Period | SCI | Traffic Unprotected Fallback |
| ------ | ------------------- | ------------ | --- | ---------------------------- |
| - | - | - | - | allow active-sak |

###### Keys

| Key ID | Fallback |
| ------ | -------- |
| 1234b | - |

##### Profile A3

###### Settings

| Cipher | Key-Server Priority | Rekey-Period | SCI | Traffic Unprotected Fallback |
| ------ | ------------------- | ------------ | --- | ---------------------------- |
| aes256-gcm-xpn | - | - | - | drop |

###### Keys

| Key ID | Fallback |
| ------ | -------- |
| ab | False |

### MACsec Device Configuration

```eos
!
mac security
   license license1 123456
   fips restrictions
   !
   profile A1
      cipher aes128-gcm
      key 1234a 7 <removed>
      key 1234c 7 <removed> fallback
      mka key-server priority 100
      mka session rekey-period 30
      traffic unprotected allow
      sci
      l2-protocol lldp bypass unauthorized
   !
   profile A2
      key 1234b 7 <removed>
      traffic unprotected allow active-sak
   !
   profile A3
      cipher aes256-gcm-xpn
      key ab 7 <removed>
      traffic unprotected drop
```
