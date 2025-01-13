# L2LS

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| L2LS_BGP | l2leaf | BGP-LEAF1 | - | - | Provisioned | - |
| L2LS_BGP | l2leaf | BGP-LEAF2 | - | - | Provisioned | - |
| L2LS_BGP | l3spine | BGP-SPINE1 | - | - | Provisioned | - |
| L2LS_BGP | l3spine | BGP-SPINE2 | - | - | Provisioned | - |
| L2LS_ISIS | l2leaf | ISIS-LEAF1 | 192.168.200.105/24 | vEOS-LAB | Provisioned | - |
| L2LS_ISIS | l3spine | ISIS-SPINE1 | 192.168.200.101/24 | vEOS-LAB | Provisioned | - |
| L2LS_L2ONLY | l2leaf | L2ONLY-LEAF1 | - | - | Provisioned | - |
| L2LS_L2ONLY | l2leaf | L2ONLY-LEAF2 | - | - | Provisioned | - |
| L2LS_L2ONLY | l2spine | L2ONLY-SPINE1 | - | - | Provisioned | - |
| L2LS_L2ONLY | l2spine | L2ONLY-SPINE2 | - | - | Provisioned | - |
| L2LS_OSPF | l2leaf | OSPF-LEAF1 | - | - | Provisioned | - |
| L2LS_OSPF | l2leaf | OSPF-LEAF2 | - | - | Provisioned | - |
| L2LS_OSPF | l3spine | OSPF-SPINE1 | - | - | Provisioned | - |
| L2LS_OSPF | l3spine | OSPF-SPINE2 | - | - | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |
| L2LS_BGP | l2leaf | BGP-LEAF1 | 172.23.254.4/24 | Vlan4092 |
| L2LS_BGP | l2leaf | BGP-LEAF2 | 172.23.254.5/24 | Vlan4092 |
| L2LS_ISIS | l2leaf | ISIS-LEAF1 | 172.23.254.4/24 | Vlan4092 |
| L2LS_L2ONLY | l2leaf | L2ONLY-LEAF1 | 172.23.254.4/24 | Vlan4092 |
| L2LS_L2ONLY | l2leaf | L2ONLY-LEAF2 | 172.23.254.5/24 | Vlan4092 |
| L2LS_OSPF | l2leaf | OSPF-LEAF1 | 172.23.254.4/24 | Vlan4092 |
| L2LS_OSPF | l2leaf | OSPF-LEAF2 | 172.23.254.5/24 | Vlan4092 |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l2leaf | BGP-LEAF1 | Ethernet1 | l3spine | BGP-SPINE1 | Ethernet1 |
| l2leaf | BGP-LEAF1 | Ethernet2 | l3spine | BGP-SPINE2 | Ethernet1 |
| l2leaf | BGP-LEAF2 | Ethernet1 | l3spine | BGP-SPINE1 | Ethernet2 |
| l2leaf | BGP-LEAF2 | Ethernet2 | l3spine | BGP-SPINE2 | Ethernet2 |
| l3spine | BGP-SPINE1 | Ethernet3 | mlag_peer | BGP-SPINE2 | Ethernet3 |
| l3spine | BGP-SPINE1 | Ethernet4 | mlag_peer | BGP-SPINE2 | Ethernet4 |
| l2leaf | ISIS-LEAF1 | Ethernet1 | l3spine | ISIS-SPINE1 | Ethernet1 |
| l2leaf | L2ONLY-LEAF1 | Ethernet1 | l2spine | L2ONLY-SPINE1 | Ethernet1 |
| l2leaf | L2ONLY-LEAF1 | Ethernet2 | l2spine | L2ONLY-SPINE2 | Ethernet1 |
| l2leaf | L2ONLY-LEAF2 | Ethernet1 | l2spine | L2ONLY-SPINE1 | Ethernet2 |
| l2leaf | L2ONLY-LEAF2 | Ethernet2 | l2spine | L2ONLY-SPINE2 | Ethernet2 |
| l2spine | L2ONLY-SPINE1 | Ethernet3 | mlag_peer | L2ONLY-SPINE2 | Ethernet3 |
| l2spine | L2ONLY-SPINE1 | Ethernet4 | mlag_peer | L2ONLY-SPINE2 | Ethernet4 |
| l2leaf | OSPF-LEAF1 | Ethernet1 | l3spine | OSPF-SPINE1 | Ethernet1 |
| l2leaf | OSPF-LEAF1 | Ethernet2 | l3spine | OSPF-SPINE2 | Ethernet1 |
| l2leaf | OSPF-LEAF2 | Ethernet1 | l3spine | OSPF-SPINE1 | Ethernet2 |
| l2leaf | OSPF-LEAF2 | Ethernet2 | l3spine | OSPF-SPINE2 | Ethernet2 |
| l3spine | OSPF-SPINE1 | Ethernet3 | mlag_peer | OSPF-SPINE2 | Ethernet3 |
| l3spine | OSPF-SPINE1 | Ethernet4 | mlag_peer | OSPF-SPINE2 | Ethernet4 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 192.168.255.0/24 | 256 | 5 | 1.96 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| L2LS_BGP | BGP-SPINE1 | 192.168.255.1/32 |
| L2LS_BGP | BGP-SPINE2 | 192.168.255.2/32 |
| L2LS_ISIS | ISIS-SPINE1 | 192.168.255.1/32 |
| L2LS_OSPF | OSPF-SPINE1 | 192.168.255.1/32 |
| L2LS_OSPF | OSPF-SPINE2 | 192.168.255.2/32 |

### ISIS CLNS interfaces

| POD | Node | CLNS Address |
| --- | ---- | ------------ |
| L2LS_ISIS | ISIS-SPINE1 | 49.0001.1921.6825.5001.00 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------ | ------------------- | ------------------ | ------------------ |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
