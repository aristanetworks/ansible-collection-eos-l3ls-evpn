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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "monitor_server_radius.probe.interval") | Integer |  |  | Min: 1<br>Max: 1000 | Server probe interval in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;threshold_failure</samp>](## "monitor_server_radius.probe.threshold_failure") | Integer |  |  | Min: 1<br>Max: 255 | Number of consecutive failed probes before a server is marked as dead. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;method</samp>](## "monitor_server_radius.probe.method") | String |  |  | Valid Values:<br>- <code>status-server</code><br>- <code>access-request</code> | Method used to probe the server. `status-server` is the EOS default method. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;access_request</samp>](## "monitor_server_radius.probe.access_request") | Dictionary |  |  |  | This can only be set when `method` is `access_request`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;username</samp>](## "monitor_server_radius.probe.access_request.username") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "monitor_server_radius.probe.access_request.password") | String |  |  |  | Encrypted password using the `password_type`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;password_type</samp>](## "monitor_server_radius.probe.access_request.password_type") | String |  | `7` | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> |  |

=== "YAML"

    ```yaml
    # Settings to monitor radius servers.
    monitor_server_radius:

      # Monitor servers used for 802.1X authentication.
      service_dot1x: <bool>

      # Settings for probe sent to the server.
      probe:

        # Server probe interval in seconds.
        interval: <int; 1-1000>

        # Number of consecutive failed probes before a server is marked as dead.
        threshold_failure: <int; 1-255>

        # Method used to probe the server. `status-server` is the EOS default method.
        method: <str; "status-server" | "access-request">

        # This can only be set when `method` is `access_request`.
        access_request:
          username: <str>

          # Encrypted password using the `password_type`.
          password: <str>
          password_type: <str; "0" | "7" | "8a"; default="7">
    ```
