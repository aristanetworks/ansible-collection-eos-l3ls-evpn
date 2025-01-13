<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>lacp</samp>](## "lacp") | Dictionary |  |  |  | Set Link Aggregation Control Protocol (LACP) parameters. |
    | [<samp>&nbsp;&nbsp;port_id</samp>](## "lacp.port_id") | Dictionary |  |  |  | LACP port-ID range configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;range</samp>](## "lacp.port_id.range") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;begin</samp>](## "lacp.port_id.range.begin") | Integer |  |  |  | Minimum LACP port-ID range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;end</samp>](## "lacp.port_id.range.end") | Integer |  |  |  | Maximum LACP port-ID range. |
    | [<samp>&nbsp;&nbsp;rate_limit</samp>](## "lacp.rate_limit") | Dictionary |  |  |  | Set LACPDU rate limit options. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "lacp.rate_limit.default") | Boolean |  |  |  | Enable LACPDU rate limiting by default on all ports. |
    | [<samp>&nbsp;&nbsp;system_priority</samp>](## "lacp.system_priority") | Integer |  |  | Min: 0<br>Max: 65535 | Set local system LACP priority. |

=== "YAML"

    ```yaml
    # Set Link Aggregation Control Protocol (LACP) parameters.
    lacp:

      # LACP port-ID range configuration.
      port_id:
        range:

          # Minimum LACP port-ID range.
          begin: <int>

          # Maximum LACP port-ID range.
          end: <int>

      # Set LACPDU rate limit options.
      rate_limit:

        # Enable LACPDU rate limiting by default on all ports.
        default: <bool>

      # Set local system LACP priority.
      system_priority: <int; 0-65535>
    ```
