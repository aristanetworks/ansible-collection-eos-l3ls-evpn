# tunnel-interfaces

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Interfaces](#interfaces)
  - [Tunnel Interfaces](#tunnel-interfaces-1)

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

## Interfaces

### Tunnel Interfaces

#### Tunnel Interfaces Summary

| Interface | Description | VRF | Underlay VRF | MTU | Shutdown | NAT Profile | Mode | Source Interface | Destination | PMTU-Discovery | IPsec Profile |
| --------- | ----------- | --- | ------------ | --- | -------- | ----------- | ---- | ---------------- | ----------- | -------------- | ------------- |
| Tunnel1 | test ipv4 only | Tunnel-VRF | Underlay-VRF | 1500 | False | - | ipsec | Ethernet42 | 6.6.6.6 | True | - |
| Tunnel2 | test ipv6 only | default | default | - | True | NAT-PROFILE-NO-VRF-2 | gre | Ethernet42 | dead:beef::1 | False | Profile-2 |
| Tunnel3 | test dual stack | default | default | 1500 | - | - | ipsec | Ethernet42 | 1.1.1.1 | - | Profile-3 |
| Tunnel4 | test no tcp_mss | default | default | 1500 | - | NAT-PROFILE-NO-VRF-1 | - | Ethernet42 | 1.1.1.1 | - | - |

##### IPv4

| Interface | VRF | IP Address | TCP MSS | TCP MSS Direction | ACL In | ACL Out |
| --------- | --- | ---------- | ------- | ----------------- | ------ | ------- |
| Tunnel1 | Tunnel-VRF | 42.42.42.42/24 | 666 | ingress | test-in | test-out |
| Tunnel3 | default | 64.64.64.64/24 | 666 | - | - | - |
| Tunnel4 | default | 64.64.64.64/24 | - | - | - | - |

##### IPv6

| Interface | VRF | IPv6 Address | TCP MSS | TCP MSS Direction | IPv6 ACL In | IPv6 ACL Out |
| --------- | --- | ------------ | ------- | ----------------- | ----------- | ------------ |
| Tunnel2 | default | cafe::1/64 | 666 | egress | test-in | test-out |
| Tunnel3 | default | beef::64/64 | 666 | - | - | - |
| Tunnel4 | default | beef::64/64 | - | - | - | - |

#### Tunnel Interfaces Device Configuration

```eos
!
interface Tunnel1
   description test ipv4 only
   no shutdown
   mtu 1500
   vrf Tunnel-VRF
   ip address 42.42.42.42/24
   tcp mss ceiling ipv4 666 ingress
   ip access-group test-in in
   ip access-group test-out out
   tunnel mode ipsec
   tunnel source interface Ethernet42
   tunnel destination 6.6.6.6
   tunnel path-mtu-discovery
   tunnel underlay vrf Underlay-VRF
   comment
   Comment created from eos_cli under tunnel_interfaces.Tunnel1
   EOF

!
interface Tunnel2
   description test ipv6 only
   shutdown
   ipv6 enable
   ipv6 address cafe::1/64
   tcp mss ceiling ipv6 666 egress
   ipv6 access-group test-in in
   ipv6 access-group test-out out
   ip nat service-profile NAT-PROFILE-NO-VRF-2
   tunnel mode gre
   tunnel source interface Ethernet42
   tunnel destination dead:beef::1
   tunnel ipsec profile Profile-2
!
interface Tunnel3
   description test dual stack
   mtu 1500
   ip address 64.64.64.64/24
   ipv6 enable
   ipv6 address beef::64/64
   tcp mss ceiling ipv4 666 ipv6 666
   tunnel mode ipsec
   tunnel source interface Ethernet42
   tunnel destination 1.1.1.1
   tunnel ipsec profile Profile-3
!
interface Tunnel4
   description test no tcp_mss
   mtu 1500
   ip address 64.64.64.64/24
   ipv6 enable
   ipv6 address beef::64/64
   ip nat service-profile NAT-PROFILE-NO-VRF-1
   tunnel source interface Ethernet42
   tunnel destination 1.1.1.1
```
