<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>errdisable</samp>](## "errdisable") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;detect</samp>](## "errdisable.detect") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;causes</samp>](## "errdisable.detect.causes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "errdisable.detect.causes.[]") | String |  |  | Valid Values:<br>- <code>acl</code><br>- <code>arp-inspection</code><br>- <code>dot1x</code><br>- <code>link-change</code><br>- <code>tapagg</code><br>- <code>xcvr-misconfigured</code><br>- <code>xcvr-overheat</code><br>- <code>xcvr-power-unsupported</code> |  |
    | [<samp>&nbsp;&nbsp;recovery</samp>](## "errdisable.recovery") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;causes</samp>](## "errdisable.recovery.causes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "errdisable.recovery.causes.[]") | String |  |  | Valid Values:<br>- <code>arp-inspection</code><br>- <code>bpduguard</code><br>- <code>dot1x</code><br>- <code>hitless-reload-down</code><br>- <code>lacp-rate-limit</code><br>- <code>link-flap</code><br>- <code>no-internal-vlan</code><br>- <code>portchannelguard</code><br>- <code>portsec</code><br>- <code>speed-misconfigured</code><br>- <code>tap-port-init</code><br>- <code>tapagg</code><br>- <code>uplink-failure-detection</code><br>- <code>xcvr-misconfigured</code><br>- <code>xcvr-overheat</code><br>- <code>xcvr-power-unsupported</code><br>- <code>xcvr-unsupported</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "errdisable.recovery.interval") | Integer |  | `300` | Min: 30<br>Max: 86400 | Interval in seconds. |

=== "YAML"

    ```yaml
    errdisable:
      detect:
        causes:
          - <str; "acl" | "arp-inspection" | "dot1x" | "link-change" | "tapagg" | "xcvr-misconfigured" | "xcvr-overheat" | "xcvr-power-unsupported">
      recovery:
        causes:
          - <str; "arp-inspection" | "bpduguard" | "dot1x" | "hitless-reload-down" | "lacp-rate-limit" | "link-flap" | "no-internal-vlan" | "portchannelguard" | "portsec" | "speed-misconfigured" | "tap-port-init" | "tapagg" | "uplink-failure-detection" | "xcvr-misconfigured" | "xcvr-overheat" | "xcvr-power-unsupported" | "xcvr-unsupported">

        # Interval in seconds.
        interval: <int; 30-86400; default=300>
    ```
