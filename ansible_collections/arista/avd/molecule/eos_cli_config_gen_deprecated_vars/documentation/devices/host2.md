# host2

## Table of Contents

- [Interfaces](#interfaces)
  - [VXLAN Interface](#vxlan-interface)
- [Routing](#routing)
  - [Router BGP](#router-bgp)

## Interfaces

### VXLAN Interface

#### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| UDP port | 4789 |
| Qos dscp propagation encapsulation | Disabled |
| Qos ECN propagation | Disabled |
| Qos map dscp to traffic-class decapsulation | Disabled |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   no vxlan qos ecn propagation
   no vxlan qos dscp propagation encapsulation
   no vxlan qos map dscp to traffic-class decapsulation
```

## Routing

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65101 | 192.168.255.3 |

#### Router BGP EVPN Address Family

#### Router BGP Device Configuration

```eos
!
router bgp 65101
   router-id 192.168.255.3
   !
   address-family evpn
      bgp additional-paths receive
      bgp additional-paths send any
```
