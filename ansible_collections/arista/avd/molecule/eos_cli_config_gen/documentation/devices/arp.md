# arp

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Routing](#routing)
  - [ARP](#arp-1)

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

### ARP

ARP cache persistency is enabled. The refresh-delay is 700 seconds after reboot.

Global ARP timeout: 300

#### ARP Static Entries

| VRF | IPv4 address | MAC address |
| --- | ------------ | ----------- |
| BLAH | 42.42.42.42 | DEAD.BEEF.CAFE |
| defauls | 42.42.42.42 | DEAD.BEEF.CAFE |
| default | 41.42.42.42 | DEAD.BEEF.CAFE |
| default | 42.42.42.42 | DEAD.BEEF.CAFE |
| default | 43.42.42.42 | DEAD.BEEF.CAFE |
| defaulu | 42.42.42.42 | DEAD.BEEF.CAFE |

#### ARP Device Configuration

```eos
!
arp persistent refresh-delay 700
arp aging timeout default 300
arp vrf BLAH 42.42.42.42 DEAD.BEEF.CAFE arpa
arp vrf defauls 42.42.42.42 DEAD.BEEF.CAFE arpa
arp 41.42.42.42 DEAD.BEEF.CAFE arpa
arp 42.42.42.42 DEAD.BEEF.CAFE arpa
arp 43.42.42.42 DEAD.BEEF.CAFE arpa
arp vrf defaulu 42.42.42.42 DEAD.BEEF.CAFE arpa
```
