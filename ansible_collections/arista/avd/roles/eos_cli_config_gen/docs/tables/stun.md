<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>stun</samp>](## "stun") | Dictionary |  |  |  | STUN configuration. |
    | [<samp>&nbsp;&nbsp;client</samp>](## "stun.client") | Dictionary |  |  |  | STUN client settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;server_profiles</samp>](## "stun.client.server_profiles") | List, items: Dictionary |  |  |  | List of server profiles for the client. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "stun.client.server_profiles.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "stun.client.server_profiles.[].ip_address") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ssl_profile</samp>](## "stun.client.server_profiles.[].ssl_profile") | String |  |  |  | SSL profile name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "stun.client.server_profiles.[].port") | Integer |  |  | Min: 1<br>Max: 65535 | Destination port for the request STUN server (default - 3478). |
    | [<samp>&nbsp;&nbsp;server</samp>](## "stun.server") | Dictionary |  |  |  | STUN server settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;local_interfaces</samp>](## "stun.server.local_interfaces") | List, items: String |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "stun.server.local_interfaces.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bindings_timeout</samp>](## "stun.server.bindings_timeout") | Integer |  |  | Min: 10<br>Max: 7200 | Timeout for bindings stored on STUN server in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ssl_profile</samp>](## "stun.server.ssl_profile") | String |  |  |  | SSL profile name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ssl_connection_lifetime</samp>](## "stun.server.ssl_connection_lifetime") | Dictionary |  |  |  | SSL connection lifetime in minutes or hours.<br>If both are specified, minutes is given higher precedence. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minutes</samp>](## "stun.server.ssl_connection_lifetime.minutes") | Integer |  |  | Min: 1<br>Max: 1440 | SSL connection lifetime in minutes (default - 120). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hours</samp>](## "stun.server.ssl_connection_lifetime.hours") | Integer |  |  | Min: 1<br>Max: 24 | SSL connection lifetime in hours (default - 2). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;port</samp>](## "stun.server.port") | Integer |  |  | Min: 1<br>Max: 65535 | Listening port for STUN server (default - 3478). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "stun.server.local_interface") <span style="color:red">removed</span> | String |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version v5.0.0. Use <samp>local_interfaces</samp> instead.</span> |

=== "YAML"

    ```yaml
    # STUN configuration.
    stun:

      # STUN client settings.
      client:

        # List of server profiles for the client.
        server_profiles:
          - name: <str; required; unique>
            ip_address: <str>

            # SSL profile name.
            ssl_profile: <str>

            # Destination port for the request STUN server (default - 3478).
            port: <int; 1-65535>

      # STUN server settings.
      server:
        local_interfaces: # >=1 items
          - <str>

        # Timeout for bindings stored on STUN server in seconds.
        bindings_timeout: <int; 10-7200>

        # SSL profile name.
        ssl_profile: <str>

        # SSL connection lifetime in minutes or hours.
        # If both are specified, minutes is given higher precedence.
        ssl_connection_lifetime:

          # SSL connection lifetime in minutes (default - 120).
          minutes: <int; 1-1440>

          # SSL connection lifetime in hours (default - 2).
          hours: <int; 1-24>

        # Listening port for STUN server (default - 3478).
        port: <int; 1-65535>
    ```
