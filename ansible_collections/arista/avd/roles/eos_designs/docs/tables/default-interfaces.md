<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>default_interfaces</samp>](## "default_interfaces") | List, items: Dictionary |  |  |  | Default uplink, downlink, and MLAG interfaces, which will be used if these interfaces are not defined on a device (either directly or through inheritance).<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;types</samp>](## "default_interfaces.[].types") | List, items: String | Required |  |  | List of node type keys. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "default_interfaces.[].types.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;platforms</samp>](## "default_interfaces.[].platforms") | List, items: String | Required |  |  | List of platform families.<br>This is defined as a Python regular expression that matches the full platform type.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "default_interfaces.[].platforms.[]") | String |  |  |  | Arista platform family regular expression. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;uplink_interfaces</samp>](## "default_interfaces.[].uplink_interfaces") | List, items: String |  |  |  | List of uplink interfaces or uplink interface ranges. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "default_interfaces.[].uplink_interfaces.[]") | String |  |  |  | Interface range or interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mlag_interfaces</samp>](## "default_interfaces.[].mlag_interfaces") | List, items: String |  |  |  | List of MLAG interfaces or MLAG interface ranges. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "default_interfaces.[].mlag_interfaces.[]") | String |  |  |  | Interface range or interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;downlink_interfaces</samp>](## "default_interfaces.[].downlink_interfaces") | List, items: String |  |  |  | List of downlink interfaces or downlink interface ranges. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "default_interfaces.[].downlink_interfaces.[]") | String |  |  |  | Interface range or interface. |

=== "YAML"

    ```yaml
    # Default uplink, downlink, and MLAG interfaces, which will be used if these interfaces are not defined on a device (either directly or through inheritance).
    default_interfaces:

        # List of node type keys.
      - types: # required
          - <str>

        # List of platform families.
        # This is defined as a Python regular expression that matches the full platform type.
        platforms: # required

            # Arista platform family regular expression.
          - <str>

        # List of uplink interfaces or uplink interface ranges.
        uplink_interfaces:

            # Interface range or interface.
          - <str>

        # List of MLAG interfaces or MLAG interface ranges.
        mlag_interfaces:

            # Interface range or interface.
          - <str>

        # List of downlink interfaces or downlink interface ranges.
        downlink_interfaces:

            # Interface range or interface.
          - <str>
    ```
