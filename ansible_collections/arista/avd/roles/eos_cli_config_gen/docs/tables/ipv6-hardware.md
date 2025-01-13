<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ipv6_hardware</samp>](## "ipv6_hardware") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;fib</samp>](## "ipv6_hardware.fib") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;optimize</samp>](## "ipv6_hardware.fib.optimize") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefixes</samp>](## "ipv6_hardware.fib.optimize.prefixes") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profile</samp>](## "ipv6_hardware.fib.optimize.prefixes.profile") | String |  |  |  | Pre-defined profile 'internet' or user-defined profile name. |

=== "YAML"

    ```yaml
    ipv6_hardware:
      fib:
        optimize:
          prefixes:

            # Pre-defined profile 'internet' or user-defined profile name.
            profile: <str>
    ```
