<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>interface_profiles</samp>](## "interface_profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "interface_profiles.[].name") | String | Required, Unique |  |  | Interface-Profile Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;commands</samp>](## "interface_profiles.[].commands") | List, items: String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "interface_profiles.[].commands.[]") | String |  |  |  | EOS CLI interface command.<br>Example: "switchport mode access"<br> |

=== "YAML"

    ```yaml
    interface_profiles:

        # Interface-Profile Name.
      - name: <str; required; unique>
        commands: # required

            # EOS CLI interface command.
            # Example: "switchport mode access"
          - <str>
    ```
