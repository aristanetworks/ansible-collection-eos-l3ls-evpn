<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>platform_sfe_interface</samp>](## "platform_sfe_interface") | Dictionary |  |  |  | Configure interface related settings for Sfe platform. |
    | [<samp>&nbsp;&nbsp;profile</samp>](## "platform_sfe_interface.profile") | List, items: Dictionary |  |  |  | Configure one or more Receive Side Scaling (RSS) interface profiles.<br>This is supported on select platforms. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "platform_sfe_interface.profile.[].name") | String | Required, Unique |  |  | RSS interface profile-name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "platform_sfe_interface.profile.[].interfaces") | List, items: Dictionary |  |  |  | Interfaces within RSS profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "platform_sfe_interface.profile.[].interfaces.[].name") | String | Required, Unique |  |  | Interface name such as 'Ethernet2'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rx_queue</samp>](## "platform_sfe_interface.profile.[].interfaces.[].rx_queue") | Dictionary |  |  |  | Receive queue parameters for the selected interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;count</samp>](## "platform_sfe_interface.profile.[].interfaces.[].rx_queue.count") | Integer |  |  | Min: 1 | Number of receive queues.<br>The maximum value is platform dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;worker</samp>](## "platform_sfe_interface.profile.[].interfaces.[].rx_queue.worker") | String |  |  |  | Worker ids specified as combination of range and/or comma separated values<br>such as 0-4,7. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "platform_sfe_interface.profile.[].interfaces.[].rx_queue.mode") | String |  |  | Valid Values:<br>- <code>shared</code><br>- <code>exclusive</code> | Mode applicable to the workers. Default mode is 'shared'. |
    | [<samp>&nbsp;&nbsp;interface_profile</samp>](## "platform_sfe_interface.interface_profile") | String |  |  |  | RSS profile name to apply for the platform.<br>Needs system reload or Sfe agent restart for change to take effect. |

=== "YAML"

    ```yaml
    # Configure interface related settings for Sfe platform.
    platform_sfe_interface:

      # Configure one or more Receive Side Scaling (RSS) interface profiles.
      # This is supported on select platforms.
      profile:

          # RSS interface profile-name.
        - name: <str; required; unique>

          # Interfaces within RSS profile.
          interfaces:

              # Interface name such as 'Ethernet2'.
            - name: <str; required; unique>

              # Receive queue parameters for the selected interface.
              rx_queue:

                # Number of receive queues.
                # The maximum value is platform dependent.
                count: <int; >=1>

                # Worker ids specified as combination of range and/or comma separated values
                # such as 0-4,7.
                worker: <str>

                # Mode applicable to the workers. Default mode is 'shared'.
                mode: <str; "shared" | "exclusive">

      # RSS profile name to apply for the platform.
      # Needs system reload or Sfe agent restart for change to take effect.
      interface_profile: <str>
    ```
