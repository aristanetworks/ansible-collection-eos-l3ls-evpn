<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cvx</samp>](## "cvx") | Dictionary |  |  |  | CVX server features are not supported on physical switches. See `management_cvx` for client configurations. |
    | [<samp>&nbsp;&nbsp;shutdown</samp>](## "cvx.shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;peer_hosts</samp>](## "cvx.peer_hosts") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "cvx.peer_hosts.[]") | String |  |  |  | IP address or hostname. |
    | [<samp>&nbsp;&nbsp;services</samp>](## "cvx.services") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mcs</samp>](## "cvx.services.mcs") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;redis</samp>](## "cvx.services.mcs.redis") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "cvx.services.mcs.redis.password") | String |  |  |  | Hashed password using the password_type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password_type</samp>](## "cvx.services.mcs.redis.password_type") | String |  | `7` | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "cvx.services.mcs.shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "cvx.services.vxlan") | Dictionary |  |  |  | VXLAN Controller service. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "cvx.services.vxlan.shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vtep_mac_learning</samp>](## "cvx.services.vxlan.vtep_mac_learning") | String |  |  | Valid Values:<br>- <code>control-plane</code><br>- <code>data-plane</code> |  |

=== "YAML"

    ```yaml
    # CVX server features are not supported on physical switches. See `management_cvx` for client configurations.
    cvx:
      shutdown: <bool>
      peer_hosts:

          # IP address or hostname.
        - <str>
      services:
        mcs:
          redis:

            # Hashed password using the password_type.
            password: <str>
            password_type: <str; "0" | "7" | "8a"; default="7">
          shutdown: <bool>

        # VXLAN Controller service.
        vxlan:
          shutdown: <bool>
          vtep_mac_learning: <str; "control-plane" | "data-plane">
    ```
