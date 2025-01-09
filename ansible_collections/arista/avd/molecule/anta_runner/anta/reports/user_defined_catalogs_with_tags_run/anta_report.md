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
| 15 | 0 | 0 | 0 | 0 |

### Summary Totals Device Under Test

| Device Under Test | Total Tests | Tests Success | Tests Skipped | Tests Failure | Tests Error | Categories Skipped | Categories Failed |
| ------------------| ----------- | ------------- | ------------- | ------------- | ----------- | -------------------| ------------------|
| dc1-leaf2a | 5 | 0 | 0 | 0 | 0 | - | - |
| dc2-leaf2a | 5 | 0 | 0 | 0 | 0 | - | - |
| dc2-leaf2b | 5 | 0 | 0 | 0 | 0 | - | - |

### Summary Totals Per Category

| Test Category | Total Tests | Tests Success | Tests Skipped | Tests Failure | Tests Error |
| ------------- | ----------- | ------------- | ------------- | ------------- | ----------- |
| VXLAN | 15 | 0 | 0 | 0 | 0 |

## Test Results

| Device Under Test | Categories | Test | Description | Custom Field | Result | Messages |
| ----------------- | ---------- | ---- | ----------- | ------------ | ------ | -------- |
| dc1-leaf2a | VXLAN | VerifyVxlan1ConnSettings | Verifies the interface vxlan1 source interface and UDP port. | - | unset | - |
| dc1-leaf2a | VXLAN | VerifyVxlan1Interface | Verifies the Vxlan1 interface status. | - | unset | - |
| dc1-leaf2a | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | - | unset | - |
| dc1-leaf2a | VXLAN | VerifyVxlanVniBinding | Verifies the VNI-VLAN bindings of the Vxlan1 interface. | - | unset | - |
| dc1-leaf2a | VXLAN | VerifyVxlanVtep | Verifies the VTEP peers of the Vxlan1 interface. | - | unset | - |
| dc2-leaf2a | VXLAN | VerifyVxlan1ConnSettings | Verifies the interface vxlan1 source interface and UDP port. | - | unset | - |
| dc2-leaf2a | VXLAN | VerifyVxlan1Interface | Verifies the Vxlan1 interface status. | - | unset | - |
| dc2-leaf2a | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | - | unset | - |
| dc2-leaf2a | VXLAN | VerifyVxlanVniBinding | Verifies the VNI-VLAN bindings of the Vxlan1 interface. | - | unset | - |
| dc2-leaf2a | VXLAN | VerifyVxlanVtep | Verifies the VTEP peers of the Vxlan1 interface. | - | unset | - |
| dc2-leaf2b | VXLAN | VerifyVxlan1ConnSettings | Verifies the interface vxlan1 source interface and UDP port. | - | unset | - |
| dc2-leaf2b | VXLAN | VerifyVxlan1Interface | Verifies the Vxlan1 interface status. | - | unset | - |
| dc2-leaf2b | VXLAN | VerifyVxlanConfigSanity | Verifies there are no VXLAN config-sanity inconsistencies. | - | unset | - |
| dc2-leaf2b | VXLAN | VerifyVxlanVniBinding | Verifies the VNI-VLAN bindings of the Vxlan1 interface. | - | unset | - |
| dc2-leaf2b | VXLAN | VerifyVxlanVtep | Verifies the VTEP peers of the Vxlan1 interface. | - | unset | - |
