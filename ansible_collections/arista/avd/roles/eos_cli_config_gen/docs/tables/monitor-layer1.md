<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>monitor_layer1</samp>](## "monitor_layer1") | Dictionary |  |  |  | Enable SYSLOG messages on transceiver SMBus communication failures. |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "monitor_layer1.enabled") | Boolean | Required |  |  | Enable monitor layer1. |
    | [<samp>&nbsp;&nbsp;logging_mac_fault</samp>](## "monitor_layer1.logging_mac_fault") | Boolean |  |  |  | Enable MAC fault logging. |
    | [<samp>&nbsp;&nbsp;logging_transceiver</samp>](## "monitor_layer1.logging_transceiver") | Dictionary |  |  |  | Configure transceiver monitoring logging. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dom</samp>](## "monitor_layer1.logging_transceiver.dom") | Boolean |  |  |  | Enable transceiver Digital Optical Monitoring (DOM) logging. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;communication</samp>](## "monitor_layer1.logging_transceiver.communication") | Boolean |  |  |  | Enable transceiver SMBus fail and reset logging. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "monitor_layer1.logging_transceiver.enabled") | Boolean |  |  |  | Some platforms support only the `logging transceiver` command. `enabled` key configures this command. |

=== "YAML"

    ```yaml
    # Enable SYSLOG messages on transceiver SMBus communication failures.
    monitor_layer1:

      # Enable monitor layer1.
      enabled: <bool; required>

      # Enable MAC fault logging.
      logging_mac_fault: <bool>

      # Configure transceiver monitoring logging.
      logging_transceiver:

        # Enable transceiver Digital Optical Monitoring (DOM) logging.
        dom: <bool>

        # Enable transceiver SMBus fail and reset logging.
        communication: <bool>

        # Some platforms support only the `logging transceiver` command. `enabled` key configures this command.
        enabled: <bool>
    ```
