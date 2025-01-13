<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>trackers</samp>](## "trackers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "trackers.[].name") | String | Required, Unique |  |  | Name of tracker object. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "trackers.[].interface") | String | Required |  |  | Name of tracked interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tracked_property</samp>](## "trackers.[].tracked_property") | String |  | `line-protocol` |  | Property to track. |

=== "YAML"

    ```yaml
    trackers:

        # Name of tracker object.
      - name: <str; required; unique>

        # Name of tracked interface.
        interface: <str; required>

        # Property to track.
        tracked_property: <str; default="line-protocol">
    ```
