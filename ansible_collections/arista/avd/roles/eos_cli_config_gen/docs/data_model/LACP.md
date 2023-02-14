---
search:
  boost: 2
---

# LACP

## LACP

Set Link Aggregation Control Protocol (LACP) parameters.

=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>lacp</samp>](## "lacp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;port_id</samp>](## "lacp.port_id") | Dictionary |  |  |  | LACP port-ID range configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;range</samp>](## "lacp.port_id.range") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;begin</samp>](## "lacp.port_id.range.begin") | Integer |  |  |  | Minimum LACP port-ID range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;end</samp>](## "lacp.port_id.range.end") | Integer |  |  |  | Maximum LACP port-ID range. |
    | [<samp>&nbsp;&nbsp;rate_limit</samp>](## "lacp.rate_limit") | Dictionary |  |  |  | Set LACPDU rate limit options. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "lacp.rate_limit.default") | Boolean |  |  |  | Enable LACPDU rate limiting by default on all ports. |
    | [<samp>&nbsp;&nbsp;system_priority</samp>](## "lacp.system_priority") | Integer |  |  | Min: 0<br>Max: 65535 | Set local system LACP priority. |

=== "YAML"

    ```yaml
    lacp:
      port_id:
        range:
          begin: <int>
          end: <int>
      rate_limit:
        default: <bool>
      system_priority: <int>
    ```
