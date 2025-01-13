<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>daemons</samp>](## "daemons") | List, items: Dictionary |  |  |  | This will add a daemon to the eos configuration that is most useful when trying to run OpenConfig clients like ocprometheus. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "daemons.[].name") | String | Required, Unique |  |  | Daemon Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;exec</samp>](## "daemons.[].exec") | String | Required |  |  | command to run as a daemon.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "daemons.[].enabled") | Boolean |  | `True` |  |  |

=== "YAML"

    ```yaml
    # This will add a daemon to the eos configuration that is most useful when trying to run OpenConfig clients like ocprometheus.
    daemons:

        # Daemon Name.
      - name: <str; required; unique>

        # command to run as a daemon.
        exec: <str; required>
        enabled: <bool; default=True>
    ```
