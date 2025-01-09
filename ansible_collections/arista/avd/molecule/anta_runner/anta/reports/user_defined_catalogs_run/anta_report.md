# ANTA Report

**Table of Contents:**

- [ANTA Report](#anta-report)
  - [Test Results Summary](#test-results-summary)
    - [Summary Totals](#summary-totals)
    - [Summary Totals Device Under Test](#summary-totals-device-under-test)
    - [Summary Totals Per Category](#summary-totals-per-category)
  - [Test Results](#test-results)

## Test Results Summary

### Summary Totals

| Total Tests | Total Tests Success | Total Tests Skipped | Total Tests Failure | Total Tests Error |
| ----------- | ------------------- | ------------------- | ------------------- | ------------------|
| 183 | 0 | 0 | 0 | 0 |

### Summary Totals Device Under Test

| Device Under Test | Total Tests | Tests Success | Tests Skipped | Tests Failure | Tests Error | Categories Skipped | Categories Failed |
| ------------------| ----------- | ------------- | ------------- | ------------- | ----------- | -------------------| ------------------|
| dc1-leaf1a | 8 | 0 | 0 | 0 | 0 | - | - |
| dc1-leaf1b | 8 | 0 | 0 | 0 | 0 | - | - |
| dc1-leaf1c | 8 | 0 | 0 | 0 | 0 | - | - |
| dc1-leaf2a | 13 | 0 | 0 | 0 | 0 | - | - |
| dc1-leaf2c | 8 | 0 | 0 | 0 | 0 | - | - |
| dc1-spine1 | 8 | 0 | 0 | 0 | 0 | - | - |
| dc1-spine2 | 8 | 0 | 0 | 0 | 0 | - | - |
| dc1-svc-leaf1a | 8 | 0 | 0 | 0 | 0 | - | - |
| dc1-svc-leaf1b | 8 | 0 | 0 | 0 | 0 | - | - |
| dc1-wan1 | 8 | 0 | 0 | 0 | 0 | - | - |
| dc1-wan2 | 8 | 0 | 0 | 0 | 0 | - | - |
| dc2-leaf1a | 8 | 0 | 0 | 0 | 0 | - | - |
| dc2-leaf1b | 8 | 0 | 0 | 0 | 0 | - | - |
| dc2-leaf1c | 8 | 0 | 0 | 0 | 0 | - | - |
| dc2-leaf2a | 13 | 0 | 0 | 0 | 0 | - | - |
| dc2-leaf2b | 13 | 0 | 0 | 0 | 0 | - | - |
| dc2-leaf2c | 8 | 0 | 0 | 0 | 0 | - | - |
| dc2-leaf3a.arista.com | 8 | 0 | 0 | 0 | 0 | - | - |
| dc2-leaf3b.arista.com | 8 | 0 | 0 | 0 | 0 | - | - |
| dc2-spine1 | 8 | 0 | 0 | 0 | 0 | - | - |
| dc2-spine2 | 8 | 0 | 0 | 0 | 0 | - | - |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Success | Tests Skipped | Tests Failure | Tests Error |
| ------------- | ----------- | ------------- | ------------- | ------------- | ----------- |
| Interfaces | 105 | 0 | 0 | 0 | 0 |
| Software | 63 | 0 | 0 | 0 | 0 |
| VXLAN | 15 | 0 | 0 | 0 | 0 |

## Test Results

| Device Under Test | Categories | Test | Description | Custom Field | Result | Messages |
| ----------------- | ---------- | ---- | ----------- | ------------ | ------ | -------- |
| dc1-leaf1a | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | - | unset | - |
| dc1-leaf1a | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | - | unset | - |
| dc1-leaf1a | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | - | unset | - |
| dc1-leaf1a | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | - | unset | - |
| dc1-leaf1a | Interfaces | VerifyStormControlDrops | Verifies there are no interface storm-control drop counters. | - | unset | - |
| dc1-leaf1a | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc1-leaf1a | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc1-leaf1a | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc1-leaf1b | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | - | unset | - |
| dc1-leaf1b | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | - | unset | - |
| dc1-leaf1b | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | - | unset | - |
| dc1-leaf1b | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | - | unset | - |
| dc1-leaf1b | Interfaces | VerifyStormControlDrops | Verifies there are no interface storm-control drop counters. | - | unset | - |
| dc1-leaf1b | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc1-leaf1b | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc1-leaf1b | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc1-leaf1c | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | - | unset | - |
| dc1-leaf1c | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | - | unset | - |
| dc1-leaf1c | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | - | unset | - |
| dc1-leaf1c | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | - | unset | - |
| dc1-leaf1c | Interfaces | VerifyStormControlDrops | Verifies there are no interface storm-control drop counters. | - | unset | - |
| dc1-leaf1c | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc1-leaf1c | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc1-leaf1c | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc1-leaf2a | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | - | unset | - |
| dc1-leaf2a | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | - | unset | - |
| dc1-leaf2a | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | - | unset | - |
| dc1-leaf2a | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | - | unset | - |
| dc1-leaf2a | Interfaces | VerifyStormControlDrops | Verifies there are no interface storm-control drop counters. | - | unset | - |
| dc1-leaf2a | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc1-leaf2a | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc1-leaf2a | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc1-leaf2a | VXLAN | VerifyVxlan1ConnSettings | Verifies the interface vxlan1 source interface and UDP port. | - | unset | - |
| dc1-leaf2a | VXLAN | VerifyVxlan1Interface | Verifies the Vxlan1 interface status. | - | unset | - |
| dc1-leaf2a | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | - | unset | - |
| dc1-leaf2a | VXLAN | VerifyVxlanVniBinding | Verifies the VNI-VLAN bindings of the Vxlan1 interface. | - | unset | - |
| dc1-leaf2a | VXLAN | VerifyVxlanVtep | Verifies the VTEP peers of the Vxlan1 interface. | - | unset | - |
| dc1-leaf2c | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | - | unset | - |
| dc1-leaf2c | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | - | unset | - |
| dc1-leaf2c | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | - | unset | - |
| dc1-leaf2c | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | - | unset | - |
| dc1-leaf2c | Interfaces | VerifyStormControlDrops | Verifies there are no interface storm-control drop counters. | - | unset | - |
| dc1-leaf2c | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc1-leaf2c | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc1-leaf2c | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc1-spine1 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | - | unset | - |
| dc1-spine1 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | - | unset | - |
| dc1-spine1 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | - | unset | - |
| dc1-spine1 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | - | unset | - |
| dc1-spine1 | Interfaces | VerifyStormControlDrops | Verifies there are no interface storm-control drop counters. | - | unset | - |
| dc1-spine1 | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc1-spine1 | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc1-spine1 | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc1-spine2 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | - | unset | - |
| dc1-spine2 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | - | unset | - |
| dc1-spine2 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | - | unset | - |
| dc1-spine2 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | - | unset | - |
| dc1-spine2 | Interfaces | VerifyStormControlDrops | Verifies there are no interface storm-control drop counters. | - | unset | - |
| dc1-spine2 | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc1-spine2 | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc1-spine2 | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc1-svc-leaf1a | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | - | unset | - |
| dc1-svc-leaf1a | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | - | unset | - |
| dc1-svc-leaf1a | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | - | unset | - |
| dc1-svc-leaf1a | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | - | unset | - |
| dc1-svc-leaf1a | Interfaces | VerifyStormControlDrops | Verifies there are no interface storm-control drop counters. | - | unset | - |
| dc1-svc-leaf1a | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc1-svc-leaf1a | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc1-svc-leaf1a | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc1-svc-leaf1b | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | - | unset | - |
| dc1-svc-leaf1b | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | - | unset | - |
| dc1-svc-leaf1b | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | - | unset | - |
| dc1-svc-leaf1b | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | - | unset | - |
| dc1-svc-leaf1b | Interfaces | VerifyStormControlDrops | Verifies there are no interface storm-control drop counters. | - | unset | - |
| dc1-svc-leaf1b | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc1-svc-leaf1b | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc1-svc-leaf1b | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc1-wan1 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | - | unset | - |
| dc1-wan1 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | - | unset | - |
| dc1-wan1 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | - | unset | - |
| dc1-wan1 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | - | unset | - |
| dc1-wan1 | Interfaces | VerifyStormControlDrops | Verifies there are no interface storm-control drop counters. | - | unset | - |
| dc1-wan1 | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc1-wan1 | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc1-wan1 | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc1-wan2 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | - | unset | - |
| dc1-wan2 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | - | unset | - |
| dc1-wan2 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | - | unset | - |
| dc1-wan2 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | - | unset | - |
| dc1-wan2 | Interfaces | VerifyStormControlDrops | Verifies there are no interface storm-control drop counters. | - | unset | - |
| dc1-wan2 | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc1-wan2 | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc1-wan2 | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc2-leaf1a | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | - | unset | - |
| dc2-leaf1a | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | - | unset | - |
| dc2-leaf1a | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | - | unset | - |
| dc2-leaf1a | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | - | unset | - |
| dc2-leaf1a | Interfaces | VerifyStormControlDrops | Verifies there are no interface storm-control drop counters. | - | unset | - |
| dc2-leaf1a | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc2-leaf1a | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc2-leaf1a | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc2-leaf1b | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | - | unset | - |
| dc2-leaf1b | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | - | unset | - |
| dc2-leaf1b | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | - | unset | - |
| dc2-leaf1b | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | - | unset | - |
| dc2-leaf1b | Interfaces | VerifyStormControlDrops | Verifies there are no interface storm-control drop counters. | - | unset | - |
| dc2-leaf1b | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc2-leaf1b | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc2-leaf1b | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc2-leaf1c | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | - | unset | - |
| dc2-leaf1c | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | - | unset | - |
| dc2-leaf1c | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | - | unset | - |
| dc2-leaf1c | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | - | unset | - |
| dc2-leaf1c | Interfaces | VerifyStormControlDrops | Verifies there are no interface storm-control drop counters. | - | unset | - |
| dc2-leaf1c | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc2-leaf1c | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc2-leaf1c | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc2-leaf2a | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | - | unset | - |
| dc2-leaf2a | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | - | unset | - |
| dc2-leaf2a | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | - | unset | - |
| dc2-leaf2a | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | - | unset | - |
| dc2-leaf2a | Interfaces | VerifyStormControlDrops | Verifies there are no interface storm-control drop counters. | - | unset | - |
| dc2-leaf2a | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc2-leaf2a | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc2-leaf2a | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc2-leaf2a | VXLAN | VerifyVxlan1ConnSettings | Verifies the interface vxlan1 source interface and UDP port. | - | unset | - |
| dc2-leaf2a | VXLAN | VerifyVxlan1Interface | Verifies the Vxlan1 interface status. | - | unset | - |
| dc2-leaf2a | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | - | unset | - |
| dc2-leaf2a | VXLAN | VerifyVxlanVniBinding | Verifies the VNI-VLAN bindings of the Vxlan1 interface. | - | unset | - |
| dc2-leaf2a | VXLAN | VerifyVxlanVtep | Verifies the VTEP peers of the Vxlan1 interface. | - | unset | - |
| dc2-leaf2b | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | - | unset | - |
| dc2-leaf2b | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | - | unset | - |
| dc2-leaf2b | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | - | unset | - |
| dc2-leaf2b | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | - | unset | - |
| dc2-leaf2b | Interfaces | VerifyStormControlDrops | Verifies there are no interface storm-control drop counters. | - | unset | - |
| dc2-leaf2b | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc2-leaf2b | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc2-leaf2b | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc2-leaf2b | VXLAN | VerifyVxlan1ConnSettings | Verifies the interface vxlan1 source interface and UDP port. | - | unset | - |
| dc2-leaf2b | VXLAN | VerifyVxlan1Interface | Verifies the Vxlan1 interface status. | - | unset | - |
| dc2-leaf2b | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | - | unset | - |
| dc2-leaf2b | VXLAN | VerifyVxlanVniBinding | Verifies the VNI-VLAN bindings of the Vxlan1 interface. | - | unset | - |
| dc2-leaf2b | VXLAN | VerifyVxlanVtep | Verifies the VTEP peers of the Vxlan1 interface. | - | unset | - |
| dc2-leaf2c | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | - | unset | - |
| dc2-leaf2c | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | - | unset | - |
| dc2-leaf2c | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | - | unset | - |
| dc2-leaf2c | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | - | unset | - |
| dc2-leaf2c | Interfaces | VerifyStormControlDrops | Verifies there are no interface storm-control drop counters. | - | unset | - |
| dc2-leaf2c | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc2-leaf2c | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc2-leaf2c | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc2-leaf3a.arista.com | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | - | unset | - |
| dc2-leaf3a.arista.com | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | - | unset | - |
| dc2-leaf3a.arista.com | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | - | unset | - |
| dc2-leaf3a.arista.com | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | - | unset | - |
| dc2-leaf3a.arista.com | Interfaces | VerifyStormControlDrops | Verifies there are no interface storm-control drop counters. | - | unset | - |
| dc2-leaf3a.arista.com | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc2-leaf3a.arista.com | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc2-leaf3a.arista.com | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc2-leaf3b.arista.com | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | - | unset | - |
| dc2-leaf3b.arista.com | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | - | unset | - |
| dc2-leaf3b.arista.com | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | - | unset | - |
| dc2-leaf3b.arista.com | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | - | unset | - |
| dc2-leaf3b.arista.com | Interfaces | VerifyStormControlDrops | Verifies there are no interface storm-control drop counters. | - | unset | - |
| dc2-leaf3b.arista.com | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc2-leaf3b.arista.com | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc2-leaf3b.arista.com | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc2-spine1 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | - | unset | - |
| dc2-spine1 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | - | unset | - |
| dc2-spine1 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | - | unset | - |
| dc2-spine1 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | - | unset | - |
| dc2-spine1 | Interfaces | VerifyStormControlDrops | Verifies there are no interface storm-control drop counters. | - | unset | - |
| dc2-spine1 | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc2-spine1 | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc2-spine1 | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
| dc2-spine2 | Interfaces | VerifyInterfaceDiscards | Verifies that the interfaces packet discard counters are equal to zero. | - | unset | - |
| dc2-spine2 | Interfaces | VerifyInterfaceErrDisabled | Verifies there are no interfaces in the errdisabled state. | - | unset | - |
| dc2-spine2 | Interfaces | VerifyInterfaceErrors | Verifies that the interfaces error counters are equal to zero. | - | unset | - |
| dc2-spine2 | Interfaces | VerifyInterfaceUtilization | Verifies that the utilization of interfaces is below a certain threshold. | - | unset | - |
| dc2-spine2 | Interfaces | VerifyStormControlDrops | Verifies there are no interface storm-control drop counters. | - | unset | - |
| dc2-spine2 | Software | VerifyEOSExtensions | Verifies that all EOS extensions installed on the device are enabled for boot persistence. | - | unset | - |
| dc2-spine2 | Software | VerifyEOSVersion | Verifies the EOS version of the device. | - | unset | - |
| dc2-spine2 | Software | VerifyTerminAttrVersion | Verifies the TerminAttr version of the device. | - | unset | - |
