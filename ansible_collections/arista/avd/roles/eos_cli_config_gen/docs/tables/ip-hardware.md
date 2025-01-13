<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_hardware</samp>](## "ip_hardware") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;fib</samp>](## "ip_hardware.fib") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;optimize</samp>](## "ip_hardware.fib.optimize") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefixes</samp>](## "ip_hardware.fib.optimize.prefixes") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "ip_hardware.fib.optimize.prefixes.profile") | String |  |  | Valid Values:<br>- <code>internet</code><br>- <code>urpf-internet</code> |  |

=== "YAML"

    ```yaml
    ip_hardware:
      fib:
        optimize:
          prefixes:
            profile: <str; "internet" | "urpf-internet">
    ```
