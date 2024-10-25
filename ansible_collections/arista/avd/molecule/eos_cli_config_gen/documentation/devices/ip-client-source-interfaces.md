# ip-client-source-interfaces

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [IP Client Source Interfaces](#ip-client-source-interfaces-1)

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

### IP Client Source Interfaces

| IP Client | VRF | Source Interface Name |
| --------- | --- | --------------------- |
| FTP | default | Ethernet10 |
| FTP | default | Loopback0 |
| FTP | MGMT | Management0 |
| HTTP | default | Loopback0 |
| HTTP | MGMT | Management0 |
| HTTP | default | Ethernet10 |
| SSH | default | Ethernet10 |
| SSH | default | Loopback0 |
| SSH | MGMT | Management0 |
| Telnet | default | Ethernet10 |
| Telnet | default | Loopback0 |
| Telnet | MGMT | Management0 |
| TFTP | default | Ethernet10 |
| TFTP | default | Loopback0 |
| TFTP | MGMT | Management0 |

#### IP Client Source Interfaces Device Configuration

```eos
!
ip ftp client source-interface Ethernet10
ip ftp client source-interface Loopback0 vrf default
ip ftp client source-interface Management0 vrf MGMT
ip http client local-interface Loopback0 vrf default
ip http client local-interface Management0 vrf MGMT
ip http client local-interface Ethernet10
ip ssh client source-interface Ethernet10
ip ssh client source-interface Loopback0 vrf default
ip ssh client source-interface Management0 vrf MGMT
ip telnet client source-interface Ethernet10
ip telnet client source-interface Loopback0 vrf default
ip telnet client source-interface Management0 vrf MGMT
ip tftp client source-interface Ethernet10
ip tftp client source-interface Loopback0 vrf default
ip tftp client source-interface Management0 vrf MGMT
 ```
