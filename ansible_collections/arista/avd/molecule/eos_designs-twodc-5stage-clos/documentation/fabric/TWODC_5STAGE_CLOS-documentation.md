# TWODC_5STAGE_CLOS

## Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)
- [Connected Endpoints](#connected-endpoints)
  - [Connected Endpoint Keys](#connected-endpoint-keys)
  - [Servers](#servers)
  - [Port Profiles](#port-profiles)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| DC1_POD1 | l2leaf | DC1-POD1-L2LEAF1A | - | vEOS-LAB | Provisioned | - |
| DC1_POD1 | l2leaf | DC1-POD1-L2LEAF2A | - | vEOS-LAB | Provisioned | - |
| DC1_POD1 | l2leaf | DC1-POD1-L2LEAF2B | 192.168.1.12/24 | vEOS-LAB | Provisioned | - |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF1A | - | vEOS-LAB | Provisioned | - |
| DC1_POD1 | l3leaf | DC1-POD1-LEAF2B | 192.168.1.9/16 | vEOS-LAB | Provisioned | - |
| DC1_POD1 | spine | DC1-POD1-SPINE1 | - | vEOS-LAB | Provisioned | - |
| DC1_POD1 | spine | DC1-POD1-SPINE2 | 192.168.1.6/24 | vEOS-LAB | Provisioned | DEADBEEFC0FFEE |
| DC1_POD2 | l3leaf | DC1-POD2-LEAF1A | 192.168.1.15/24 | vEOS-LAB | Provisioned | - |
| DC1_POD2 | spine | DC1-POD2-SPINE1 | 192.168.1.13/24 | vEOS-LAB | Provisioned | - |
| DC1_POD2 | spine | DC1-POD2-SPINE2 | 192.168.1.14/24 | vEOS-LAB | Provisioned | - |
| DC1 | overlay-controller | DC1-RS1 | - | vEOS-LAB | Provisioned | - |
| DC1 | overlay-controller | DC1-RS2 | 192.168.1.4/24 | vEOS-LAB | Provisioned | - |
| DC1 | super-spine | DC1-SUPER-SPINE1 | - | vEOS-LAB | Provisioned | - |
| DC1 | super-spine | DC1-SUPER-SPINE2 | 192.168.1.2/24 | vEOS-LAB | Provisioned | - |
| DC1_POD1 | l3leaf | DC1.POD1.LEAF2A | - | vEOS-LAB | Provisioned | - |
| DC2_POD1 | l2leaf | DC2-POD1-L2LEAF1A | 192.168.1.23/24 | vEOS-LAB | Provisioned | - |
| DC2_POD1 | l2leaf | DC2-POD1-L2LEAF2A | 192.168.1.25/24 | vEOS-LAB | Provisioned | - |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF1A | 192.168.1.22/24 | vEOS-LAB | Provisioned | - |
| DC2_POD1 | l3leaf | DC2-POD1-LEAF2A | 192.168.1.24/24 | vEOS-LAB | Provisioned | - |
| DC2_POD1 | spine | DC2-POD1-SPINE1 | 192.168.1.20/24 | vEOS-LAB | Provisioned | - |
| DC2_POD1 | spine | DC2-POD1-SPINE2 | 192.168.1.21/24 | vEOS-LAB | Provisioned | - |
| DC2 | overlay-controller | DC2-RS1 | 192.168.1.18/24 | vEOS-LAB | Provisioned | - |
| DC2 | overlay-controller | DC2-RS2 | 192.168.1.19/24 | vEOS-LAB | Provisioned | - |
| DC2 | super-spine | DC2-SUPER-SPINE1 | 192.168.1.16/24 | vEOS-LAB | Provisioned | - |
| DC2 | super-spine | DC2-SUPER-SPINE2 | 192.168.1.17/24 | vEOS-LAB | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |
| DC1_POD1 | l2leaf | DC1-POD1-L2LEAF1A | 172.21.110.4/24 | Vlan4085 |
| DC1_POD1 | l2leaf | DC1-POD1-L2LEAF2A | 172.21.110.5/24 | Vlan4085 |
| DC1_POD1 | l2leaf | DC1-POD1-L2LEAF2B | 172.21.110.6/24 | Vlan4085 |
| DC2_POD1 | l2leaf | DC2-POD1-L2LEAF1A | 172.21.210.4/24 | Vlan4092 |
| DC2_POD1 | l2leaf | DC2-POD1-L2LEAF2A | 172.21.210.5/24 | Vlan4092 |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l2leaf | DC1-POD1-L2LEAF1A | Ethernet1 | l3leaf | DC1-POD1-LEAF1A | Ethernet3 |
| l2leaf | DC1-POD1-L2LEAF2A | Ethernet1 | l3leaf | DC1.POD1.LEAF2A | Ethernet3 |
| l2leaf | DC1-POD1-L2LEAF2A | Ethernet2 | l3leaf | DC1-POD1-LEAF2B | Ethernet3 |
| l2leaf | DC1-POD1-L2LEAF2A | Ethernet3 | mlag_peer | DC1-POD1-L2LEAF2B | Ethernet3 |
| l2leaf | DC1-POD1-L2LEAF2A | Ethernet4 | mlag_peer | DC1-POD1-L2LEAF2B | Ethernet4 |
| l2leaf | DC1-POD1-L2LEAF2B | Ethernet1 | l3leaf | DC1.POD1.LEAF2A | Ethernet4 |
| l2leaf | DC1-POD1-L2LEAF2B | Ethernet2 | l3leaf | DC1-POD1-LEAF2B | Ethernet4 |
| l3leaf | DC1-POD1-LEAF1A | Ethernet1 | spine | DC1-POD1-SPINE1 | Ethernet3 |
| l3leaf | DC1-POD1-LEAF1A | Ethernet2 | spine | DC1-POD1-SPINE2 | Ethernet3 |
| l3leaf | DC1-POD1-LEAF1A | Ethernet4 | overlay-controller | DC1-RS1 | Ethernet3 |
| l3leaf | DC1-POD1-LEAF2B | Ethernet1 | spine | DC1-POD1-SPINE1 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF2B | Ethernet2 | spine | DC1-POD1-SPINE2 | Ethernet5 |
| l3leaf | DC1-POD1-LEAF2B | Ethernet5 | mlag_peer | DC1.POD1.LEAF2A | Ethernet5 |
| l3leaf | DC1-POD1-LEAF2B | Ethernet6 | mlag_peer | DC1.POD1.LEAF2A | Ethernet6 |
| l3leaf | DC1-POD1-LEAF2B | Ethernet7 | l3leaf | DC2-POD1-LEAF1A | Ethernet7 |
| l3leaf | DC1-POD1-LEAF2B | Ethernet11 | spine | DC1-POD1-SPINE1 | Ethernet8 |
| l3leaf | DC1-POD1-LEAF2B | Ethernet12 | spine | DC1-POD1-SPINE2 | Ethernet8 |
| spine | DC1-POD1-SPINE1 | Ethernet1 | super-spine | DC1-SUPER-SPINE1 | Ethernet1 |
| spine | DC1-POD1-SPINE1 | Ethernet2 | super-spine | DC1-SUPER-SPINE2 | Ethernet1 |
| spine | DC1-POD1-SPINE1 | Ethernet4 | l3leaf | DC1.POD1.LEAF2A | Ethernet1 |
| spine | DC1-POD1-SPINE1 | Ethernet6 | overlay-controller | DC1-RS1 | Ethernet2 |
| spine | DC1-POD1-SPINE1 | Ethernet7 | l3leaf | DC1.POD1.LEAF2A | Ethernet11 |
| spine | DC1-POD1-SPINE2 | Ethernet1 | super-spine | DC1-SUPER-SPINE1 | Ethernet2 |
| spine | DC1-POD1-SPINE2 | Ethernet2 | super-spine | DC1-SUPER-SPINE2 | Ethernet2 |
| spine | DC1-POD1-SPINE2 | Ethernet4 | l3leaf | DC1.POD1.LEAF2A | Ethernet2 |
| spine | DC1-POD1-SPINE2 | Ethernet7 | l3leaf | DC1.POD1.LEAF2A | Ethernet12 |
| l3leaf | DC1-POD2-LEAF1A | Ethernet1 | spine | DC1-POD2-SPINE1 | Ethernet3 |
| l3leaf | DC1-POD2-LEAF1A | Ethernet2 | spine | DC1-POD2-SPINE2 | Ethernet3 |
| l3leaf | DC1-POD2-LEAF1A | Ethernet3 | overlay-controller | DC1-RS2 | Ethernet3 |
| spine | DC1-POD2-SPINE1 | Ethernet1 | super-spine | DC1-SUPER-SPINE1 | Ethernet3 |
| spine | DC1-POD2-SPINE1 | Ethernet2 | super-spine | DC1-SUPER-SPINE2 | Ethernet3 |
| spine | DC1-POD2-SPINE1 | Ethernet4 | overlay-controller | DC1-RS2 | Ethernet2 |
| spine | DC1-POD2-SPINE1 | Ethernet5 | spine | DC2-POD1-SPINE1 | Ethernet5 |
| spine | DC1-POD2-SPINE2 | Ethernet1 | super-spine | DC1-SUPER-SPINE1 | Ethernet4 |
| spine | DC1-POD2-SPINE2 | Ethernet2 | super-spine | DC1-SUPER-SPINE2 | Ethernet4 |
| spine | DC1-POD2-SPINE2 | Ethernet4 | spine | DC2-POD1-SPINE2 | Ethernet5 |
| overlay-controller | DC1-RS1 | Ethernet1 | super-spine | DC1-SUPER-SPINE1 | Ethernet5 |
| overlay-controller | DC1-RS2 | Ethernet1 | super-spine | DC1-SUPER-SPINE2 | Ethernet5 |
| super-spine | DC1-SUPER-SPINE1 | Ethernet6 | super-spine | DC2-SUPER-SPINE1 | Ethernet4 |
| super-spine | DC1-SUPER-SPINE2 | Ethernet6 | super-spine | DC2-SUPER-SPINE2 | Ethernet4 |
| l3leaf | DC1.POD1.LEAF2A | Ethernet7 | l3leaf | DC2-POD1-LEAF1A | Ethernet6 |
| l2leaf | DC2-POD1-L2LEAF1A | Ethernet1 | l3leaf | DC2-POD1-LEAF1A | Ethernet3 |
| l2leaf | DC2-POD1-L2LEAF2A | Ethernet1 | l3leaf | DC2-POD1-LEAF2A | Ethernet3 |
| l3leaf | DC2-POD1-LEAF1A | Ethernet1 | spine | DC2-POD1-SPINE1 | Ethernet3 |
| l3leaf | DC2-POD1-LEAF1A | Ethernet2 | spine | DC2-POD1-SPINE2 | Ethernet3 |
| l3leaf | DC2-POD1-LEAF2A | Ethernet1 | spine | DC2-POD1-SPINE1 | Ethernet4 |
| l3leaf | DC2-POD1-LEAF2A | Ethernet2 | spine | DC2-POD1-SPINE2 | Ethernet4 |
| spine | DC2-POD1-SPINE1 | Ethernet1 | super-spine | DC2-SUPER-SPINE1 | Ethernet1 |
| spine | DC2-POD1-SPINE1 | Ethernet2 | super-spine | DC2-SUPER-SPINE2 | Ethernet1 |
| spine | DC2-POD1-SPINE2 | Ethernet1 | super-spine | DC2-SUPER-SPINE1 | Ethernet2 |
| spine | DC2-POD1-SPINE2 | Ethernet2 | super-spine | DC2-SUPER-SPINE2 | Ethernet2 |
| overlay-controller | DC2-RS1 | Ethernet1 | super-spine | DC2-SUPER-SPINE1 | Ethernet3 |
| overlay-controller | DC2-RS1 | Ethernet2 | super-spine | DC2-SUPER-SPINE1 | Ethernet6 |
| overlay-controller | DC2-RS2 | Ethernet1 | super-spine | DC2-SUPER-SPINE1 | Ethernet5 |
| overlay-controller | DC2-RS2 | Ethernet2 | super-spine | DC2-SUPER-SPINE1 | Ethernet7 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 172.16.11.0/24 | 256 | 8 | 3.13 % |
| 172.16.12.0/24 | 256 | 8 | 3.13 % |
| 172.16.21.0/24 | 256 | 8 | 3.13 % |
| 172.17.10.0/24 | 256 | 12 | 4.69 % |
| 172.17.20.0/24 | 256 | 8 | 3.13 % |
| 172.17.110.0/24 | 256 | 20 | 7.82 % |
| 172.17.120.0/24 | 256 | 4 | 1.57 % |
| 172.17.210.0/24 | 256 | 8 | 3.13 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| DC1-POD1-LEAF1A | Ethernet1 | 172.17.110.1/31 | DC1-POD1-SPINE1 | Ethernet3 | 172.17.110.0/31 |
| DC1-POD1-LEAF1A | Ethernet2 | 172.17.110.3/31 | DC1-POD1-SPINE2 | Ethernet3 | 172.17.110.2/31 |
| DC1-POD1-LEAF1A | Ethernet4 | 172.17.10.4/31 | DC1-RS1 | Ethernet3 | 172.17.10.5/31 |
| DC1-POD1-LEAF2B | Ethernet1 | 172.17.110.17/31 | DC1-POD1-SPINE1 | Ethernet5 | 172.17.110.16/31 |
| DC1-POD1-LEAF2B | Ethernet2 | 172.17.110.19/31 | DC1-POD1-SPINE2 | Ethernet5 | 172.17.110.18/31 |
| DC1-POD1-LEAF2B | Ethernet7 | 11.1.0.38/31 | DC2-POD1-LEAF1A | Ethernet7 | 11.1.0.39/31 |
| DC1-POD1-LEAF2B | Ethernet11 | 172.17.110.21/31 | DC1-POD1-SPINE1 | Ethernet8 | 172.17.110.20/31 |
| DC1-POD1-LEAF2B | Ethernet12 | 172.17.110.23/31 | DC1-POD1-SPINE2 | Ethernet8 | 172.17.110.22/31 |
| DC1-POD1-SPINE1 | Ethernet1 | 172.16.11.1/31 | DC1-SUPER-SPINE1 | Ethernet1 | 172.16.11.0/31 |
| DC1-POD1-SPINE1 | Ethernet2 | 172.16.11.65/31 | DC1-SUPER-SPINE2 | Ethernet1 | 172.16.11.64/31 |
| DC1-POD1-SPINE1 | Ethernet4 | 172.17.110.8/31 | DC1.POD1.LEAF2A | Ethernet1 | 172.17.110.9/31 |
| DC1-POD1-SPINE1 | Ethernet6 | 172.17.10.2/31 | DC1-RS1 | Ethernet2 | 172.17.10.3/31 |
| DC1-POD1-SPINE1 | Ethernet7 | 172.17.110.12/31 | DC1.POD1.LEAF2A | Ethernet11 | 172.17.110.13/31 |
| DC1-POD1-SPINE2 | Ethernet1 | 172.16.11.3/31 | DC1-SUPER-SPINE1 | Ethernet2 | 172.16.11.2/31 |
| DC1-POD1-SPINE2 | Ethernet2 | 172.16.11.67/31 | DC1-SUPER-SPINE2 | Ethernet2 | 172.16.11.66/31 |
| DC1-POD1-SPINE2 | Ethernet4 | 172.17.110.10/31 | DC1.POD1.LEAF2A | Ethernet2 | 172.17.110.11/31 |
| DC1-POD1-SPINE2 | Ethernet7 | 172.17.110.14/31 | DC1.POD1.LEAF2A | Ethernet12 | 172.17.110.15/31 |
| DC1-POD2-LEAF1A | Ethernet1 | 172.17.120.1/31 | DC1-POD2-SPINE1 | Ethernet3 | 172.17.120.0/31 |
| DC1-POD2-LEAF1A | Ethernet2 | 172.17.120.3/31 | DC1-POD2-SPINE2 | Ethernet3 | 172.17.120.2/31 |
| DC1-POD2-LEAF1A | Ethernet3 | 172.17.10.12/31 | DC1-RS2 | Ethernet3 | 172.17.10.13/31 |
| DC1-POD2-SPINE1 | Ethernet1 | 172.16.12.1/31 | DC1-SUPER-SPINE1 | Ethernet3 | 172.16.12.0/31 |
| DC1-POD2-SPINE1 | Ethernet2 | 172.16.12.65/31 | DC1-SUPER-SPINE2 | Ethernet3 | 172.16.12.64/31 |
| DC1-POD2-SPINE1 | Ethernet4 | 172.17.10.10/31 | DC1-RS2 | Ethernet2 | 172.17.10.11/31 |
| DC1-POD2-SPINE1 | Ethernet5 | 11.1.1.18/31 | DC2-POD1-SPINE1 | Ethernet5 | 11.1.1.19/31 |
| DC1-POD2-SPINE2 | Ethernet1 | 172.16.12.3/31 | DC1-SUPER-SPINE1 | Ethernet4 | 172.16.12.2/31 |
| DC1-POD2-SPINE2 | Ethernet2 | 172.16.12.67/31 | DC1-SUPER-SPINE2 | Ethernet4 | 172.16.12.66/31 |
| DC1-POD2-SPINE2 | Ethernet4 | 200.200.200.101/24 | DC2-POD1-SPINE2 | Ethernet5 | 200.200.200.201/24 |
| DC1-RS1 | Ethernet1 | 172.17.10.1/31 | DC1-SUPER-SPINE1 | Ethernet5 | 172.17.10.0/31 |
| DC1-RS2 | Ethernet1 | 172.17.10.9/31 | DC1-SUPER-SPINE2 | Ethernet5 | 172.17.10.8/31 |
| DC1-SUPER-SPINE1 | Ethernet6 | 11.1.2.0/31 | DC2-SUPER-SPINE1 | Ethernet4 | 11.1.2.1/31 |
| DC1-SUPER-SPINE2 | Ethernet6 | 11.1.2.2/31 | DC2-SUPER-SPINE2 | Ethernet4 | 11.1.2.3/31 |
| DC1.POD1.LEAF2A | Ethernet7 | 100.100.100.101/24 | DC2-POD1-LEAF1A | Ethernet6 | 100.100.100.201/24 |
| DC2-POD1-LEAF1A | Ethernet1 | 172.17.210.1/31 | DC2-POD1-SPINE1 | Ethernet3 | 172.17.210.0/31 |
| DC2-POD1-LEAF1A | Ethernet2 | 172.17.210.3/31 | DC2-POD1-SPINE2 | Ethernet3 | 172.17.210.2/31 |
| DC2-POD1-LEAF2A | Ethernet1 | 172.17.210.5/31 | DC2-POD1-SPINE1 | Ethernet4 | 172.17.210.4/31 |
| DC2-POD1-LEAF2A | Ethernet2 | 172.17.210.7/31 | DC2-POD1-SPINE2 | Ethernet4 | 172.17.210.6/31 |
| DC2-POD1-SPINE1 | Ethernet1 | 172.16.21.1/31 | DC2-SUPER-SPINE1 | Ethernet1 | 172.16.21.0/31 |
| DC2-POD1-SPINE1 | Ethernet2 | 172.16.21.65/31 | DC2-SUPER-SPINE2 | Ethernet1 | 172.16.21.64/31 |
| DC2-POD1-SPINE2 | Ethernet1 | 172.16.21.3/31 | DC2-SUPER-SPINE1 | Ethernet2 | 172.16.21.2/31 |
| DC2-POD1-SPINE2 | Ethernet2 | 172.16.21.67/31 | DC2-SUPER-SPINE2 | Ethernet2 | 172.16.21.66/31 |
| DC2-RS1 | Ethernet1 | 172.17.20.1/31 | DC2-SUPER-SPINE1 | Ethernet3 | 172.17.20.0/31 |
| DC2-RS1 | Ethernet2 | 172.17.20.3/31 | DC2-SUPER-SPINE1 | Ethernet6 | 172.17.20.2/31 |
| DC2-RS2 | Ethernet1 | 172.17.20.9/31 | DC2-SUPER-SPINE1 | Ethernet5 | 172.17.20.8/31 |
| DC2-RS2 | Ethernet2 | 172.17.20.11/31 | DC2-SUPER-SPINE1 | Ethernet7 | 172.17.20.10/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 172.16.10.0/24 | 256 | 2 | 0.79 % |
| 172.16.20.0/24 | 256 | 2 | 0.79 % |
| 172.16.100.0/24 | 256 | 2 | 0.79 % |
| 172.16.110.0/24 | 256 | 5 | 1.96 % |
| 172.16.120.0/24 | 256 | 3 | 1.18 % |
| 172.16.200.0/24 | 256 | 2 | 0.79 % |
| 172.16.210.0/24 | 256 | 4 | 1.57 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| DC1_POD1 | DC1-POD1-LEAF1A | 172.16.110.3/32 |
| DC1_POD1 | DC1-POD1-LEAF2B | 172.16.110.5/32 |
| DC1_POD1 | DC1-POD1-SPINE1 | 172.16.110.1/32 |
| DC1_POD1 | DC1-POD1-SPINE2 | 172.16.110.2/32 |
| DC1_POD2 | DC1-POD2-LEAF1A | 172.16.120.3/32 |
| DC1_POD2 | DC1-POD2-SPINE1 | 172.16.120.1/32 |
| DC1_POD2 | DC1-POD2-SPINE2 | 172.16.120.2/32 |
| DC1 | DC1-RS1 | 172.16.10.1/32 |
| DC1 | DC1-RS2 | 172.16.10.2/32 |
| DC1 | DC1-SUPER-SPINE1 | 172.16.100.1/32 |
| DC1 | DC1-SUPER-SPINE2 | 172.16.100.2/32 |
| DC1_POD1 | DC1.POD1.LEAF2A | 172.16.110.4/32 |
| DC2_POD1 | DC2-POD1-LEAF1A | 172.16.210.3/32 |
| DC2_POD1 | DC2-POD1-LEAF2A | 172.16.210.4/32 |
| DC2_POD1 | DC2-POD1-SPINE1 | 172.16.210.1/32 |
| DC2_POD1 | DC2-POD1-SPINE2 | 172.16.210.2/32 |
| DC2 | DC2-RS1 | 172.16.20.1/32 |
| DC2 | DC2-RS2 | 172.16.20.2/32 |
| DC2 | DC2-SUPER-SPINE1 | 172.16.200.1/32 |
| DC2 | DC2-SUPER-SPINE2 | 172.16.200.2/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------ | ------------------- | ------------------ | ------------------ |
| 172.18.110.0/24 | 256 | 3 | 1.18 % |
| 172.18.120.0/24 | 256 | 1 | 0.4 % |
| 172.18.210.0/24 | 256 | 2 | 0.79 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| DC1_POD1 | DC1-POD1-LEAF1A | 172.18.110.3/32 |
| DC1_POD1 | DC1-POD1-LEAF2B | 172.18.110.4/32 |
| DC1_POD2 | DC1-POD2-LEAF1A | 172.18.120.3/32 |
| DC1_POD1 | DC1.POD1.LEAF2A | 172.18.110.4/32 |
| DC2_POD1 | DC2-POD1-LEAF1A | 172.18.210.3/32 |
| DC2_POD1 | DC2-POD1-LEAF2A | 172.18.210.4/32 |

## Connected Endpoints

### Connected Endpoint Keys

| Key | Type | Description |
| --- | ---- | ----------- |
| servers | server | Server |

### Servers

| Name | Port | Fabric Device | Fabric Port | Description | Shutdown | Mode | Access VLAN | Trunk Allowed VLANs | Profile |
| ---- | ---- | ------------- | ------------| ----------- | -------- | ---- | ----------- | ------------------- | ------- |
| server-1 | Eth1 | DC1.POD1.LEAF2A | Ethernet16 | SERVER_server-1_Eth1 | False | access | 110 | - | TENANT_A |
| server-1 | Eth3 | DC1.POD1.LEAF2A | Ethernet17 | Set using structured_config on server adapter | False | access | 110 | - | TENANT_A |
| server-1 | Eth5 | DC1.POD1.LEAF2A | Ethernet18 | SERVER_server-1_Eth5 | False | access | 110 | - | NESTED_TENANT_A |
| server-1 | Eth7 | DC1.POD1.LEAF2A | Ethernet19 | SERVER_server-1_Eth7 | False | access | 110 | - | NESTED_TENANT_A |
| server-1 | Eth2 | DC1-POD1-LEAF2B | Ethernet16 | SERVER_server-1_Eth2 | False | access | 110 | - | TENANT_A |
| server-1 | Eth4 | DC1-POD1-LEAF2B | Ethernet17 | Set using structured_config on server adapter | False | access | 110 | - | TENANT_A |
| server-1 | Eth6 | DC1-POD1-LEAF2B | Ethernet18 | SERVER_server-1_Eth6 | False | access | 110 | - | NESTED_TENANT_A |
| server-1 | Eth8 | DC1-POD1-LEAF2B | Ethernet19 | SERVER_server-1_Eth8 | False | access | 110 | - | NESTED_TENANT_A |

### Port Profiles

| Profile Name | Parent Profile |
| ------------ | -------------- |
| NESTED_TENANT_A | TENANT_A |
| TENANT_A | - |
