# router-l2-vpn

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
- [Router L2 VPN](#router-l2-vpn-1)
  - [Router L2 VPN Summary](#router-l2-vpn-summary)
  - [Router L2 VPN Device Configuration](#router-l2-vpn-device-configuration)

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

## Router L2 VPN

### Router L2 VPN Summary

- ARP learning bridged is enabled.

- VXLAN ARP Proxying is disabled for IPv4 addresses defined in the prefix-list pl-router-l2-vpn.

- Selective ARP is enabled.

- ND learning bridged is enabled.

- VXLAN ND Proxying is disabled for IPv6 addresses defined in the prefix-list pl-router-l2-vpn.

- Neighbor discovery router solicitation VTEP flooding is disabled.

- Virtual router neighbor advertisement VTEP flooding is disabled.

### Router L2 VPN Device Configuration

```eos
!
router l2-vpn
   arp learning bridged
   arp proxy prefix-list pl-router-l2-vpn
   arp selective-install
   nd learning bridged
   nd proxy prefix-list pl-router-l2-vpn
   nd rs flooding disabled
   virtual-router neighbor advertisement flooding disabled
```
