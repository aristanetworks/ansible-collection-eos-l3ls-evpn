<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>vmtracer_sessions</samp>](## "vmtracer_sessions") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "vmtracer_sessions.[].name") | String | Required, Unique |  |  | Vmtracer Session Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;url</samp>](## "vmtracer_sessions.[].url") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;username</samp>](## "vmtracer_sessions.[].username") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;password</samp>](## "vmtracer_sessions.[].password") | String |  |  |  | Type 7 Password Hash. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;autovlan_disable</samp>](## "vmtracer_sessions.[].autovlan_disable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "vmtracer_sessions.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "vmtracer_sessions.[].source_interface") | String |  |  |  |  |

=== "YAML"

    ```yaml
    vmtracer_sessions:

        # Vmtracer Session Name.
      - name: <str; required; unique>
        url: <str>
        username: <str>

        # Type 7 Password Hash.
        password: <str>
        autovlan_disable: <bool>
        vrf: <str>
        source_interface: <str>
    ```
