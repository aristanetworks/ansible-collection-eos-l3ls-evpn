<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>monitor_server_radius</samp>](## "monitor_server_radius") | Dictionary |  |  |  | Settings to monitor radius servers. |
    | [<samp>&nbsp;&nbsp;service_dot1x</samp>](## "monitor_server_radius.service_dot1x") | Boolean |  |  |  | Monitor servers used for 802.1X authentication. |
    | [<samp>&nbsp;&nbsp;probe</samp>](## "monitor_server_radius.probe") | Dictionary |  |  |  | Settings for probe sent to the server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "monitor_server_radius.probe.interval") | Integer |  |  | Min: 1<br>Max: 1000 | Server probe period in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;method</samp>](## "monitor_server_radius.probe.method") | String |  |  | Valid Values:<br>- <code>status-server</code><br>- <code>access-request</code> | Method used to probe the server. `status-server` is the EOS default method. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_request</samp>](## "monitor_server_radius.probe.access_request") | Dictionary |  |  |  | Use RADIUS Access-Request packets as probes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;username</samp>](## "monitor_server_radius.probe.access_request.username") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "monitor_server_radius.probe.access_request.password") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password_type</samp>](## "monitor_server_radius.probe.access_request.password_type") | String |  | `7` | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> |  |

=== "YAML"

    ```yaml
    # Settings to monitor radius servers.
    monitor_server_radius:

      # Monitor servers used for 802.1X authentication.
      service_dot1x: <bool>

      # Settings for probe sent to the server.
      probe:

        # Server probe period in seconds.
        interval: <int; 1-1000>

        # Method used to probe the server. `status-server` is the EOS default method.
        method: <str; "status-server" | "access-request">

        # Use RADIUS Access-Request packets as probes.
        access_request:
          username: <str>
          password: <str>
          password_type: <str; "0" | "7" | "8a"; default="7">
    ```
