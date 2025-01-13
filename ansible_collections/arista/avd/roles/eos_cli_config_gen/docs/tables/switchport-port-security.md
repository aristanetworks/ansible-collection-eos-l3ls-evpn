<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>switchport_port_security</samp>](## "switchport_port_security") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;mac_address</samp>](## "switchport_port_security.mac_address") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;aging</samp>](## "switchport_port_security.mac_address.aging") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;moveable</samp>](## "switchport_port_security.mac_address.moveable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;persistence_disabled</samp>](## "switchport_port_security.persistence_disabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;violation_protect_chip_based</samp>](## "switchport_port_security.violation_protect_chip_based") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    switchport_port_security:
      mac_address:
        aging: <bool>
        moveable: <bool>
      persistence_disabled: <bool>
      violation_protect_chip_based: <bool>
    ```
