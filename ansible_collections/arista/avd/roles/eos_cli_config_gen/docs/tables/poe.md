<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>poe</samp>](## "poe") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;reboot</samp>](## "poe.reboot") | Dictionary |  |  |  | Set the global PoE power behavior for PoE ports when the system is rebooted. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "poe.reboot.action") | String |  |  | Valid Values:<br>- <code>power-off</code><br>- <code>maintain</code> | PoE action for interface. By default in EOS, reboot action is set to power-off. |
    | [<samp>&nbsp;&nbsp;interface_shutdown</samp>](## "poe.interface_shutdown") | Dictionary |  |  |  | Set the global PoE power behavior for PoE ports when ports are admin down. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "poe.interface_shutdown.action") | String |  |  | Valid Values:<br>- <code>power-off</code><br>- <code>maintain</code> | PoE action for interface. By default in EOS, interface shutdown action is set to maintain. |

=== "YAML"

    ```yaml
    poe:

      # Set the global PoE power behavior for PoE ports when the system is rebooted.
      reboot:

        # PoE action for interface. By default in EOS, reboot action is set to power-off.
        action: <str; "power-off" | "maintain">

      # Set the global PoE power behavior for PoE ports when ports are admin down.
      interface_shutdown:

        # PoE action for interface. By default in EOS, interface shutdown action is set to maintain.
        action: <str; "power-off" | "maintain">
    ```
