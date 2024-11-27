# FABRIC

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

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| FABRIC | l3leaf | leaf1 | 172.16.1.101/24 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf2 | 172.16.1.102/24 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf3 | 172.16.1.103/24 | vEOS-lab | Provisioned | - |
| FABRIC | l3leaf | leaf4 | 172.16.1.104/24 | vEOS-lab | Provisioned | - |
| FABRIC | spine | spine1 | 172.16.1.11/24 | vEOS-lab | Provisioned | - |
| FABRIC | spine | spine2 | 172.16.1.12/24 | vEOS-lab | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | leaf1 | Ethernet1 | spine | spine1 | Ethernet1 |
| l3leaf | leaf1 | Ethernet2 | spine | spine2 | Ethernet1 |
| l3leaf | leaf1 | Ethernet11 | mlag_peer | leaf2 | Ethernet11 |
| l3leaf | leaf1 | Ethernet12 | mlag_peer | leaf2 | Ethernet12 |
| l3leaf | leaf2 | Ethernet1 | spine | spine1 | Ethernet2 |
| l3leaf | leaf2 | Ethernet2 | spine | spine2 | Ethernet2 |
| l3leaf | leaf3 | Ethernet1 | spine | spine1 | Ethernet3 |
| l3leaf | leaf3 | Ethernet2 | spine | spine2 | Ethernet3 |
| l3leaf | leaf3 | Ethernet11 | mlag_peer | leaf4 | Ethernet11 |
| l3leaf | leaf3 | Ethernet12 | mlag_peer | leaf4 | Ethernet12 |
| l3leaf | leaf4 | Ethernet1 | spine | spine1 | Ethernet4 |
| l3leaf | leaf4 | Ethernet2 | spine | spine2 | Ethernet4 |

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

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
