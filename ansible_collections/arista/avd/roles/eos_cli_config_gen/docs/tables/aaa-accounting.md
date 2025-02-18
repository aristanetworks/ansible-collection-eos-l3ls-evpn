<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>aaa_accounting</samp>](## "aaa_accounting") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;exec</samp>](## "aaa_accounting.exec") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;console</samp>](## "aaa_accounting.exec.console") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_accounting.exec.console.type") | String | Required |  | Valid Values:<br>- <code>none</code><br>- <code>start-stop</code><br>- <code>stop-only</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.exec.console.group") <span style="color:red">deprecated</span> | String |  |  |  | Group Name.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>methods.group</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "aaa_accounting.exec.console.logging") <span style="color:red">deprecated</span> | Boolean |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>methods.method</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;methods</samp>](## "aaa_accounting.exec.console.methods") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;method</samp>](## "aaa_accounting.exec.console.methods.[].method") | String | Required |  | Valid Values:<br>- <code>logging</code><br>- <code>group</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.exec.console.methods.[].group") | String |  |  |  | Specify the server group to be used.<br>This option is applicable only when the `method` key is explicitly set to `group`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_accounting.exec.default") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_accounting.exec.default.type") | String |  |  | Valid Values:<br>- <code>none</code><br>- <code>start-stop</code><br>- <code>stop-only</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.exec.default.group") <span style="color:red">deprecated</span> | String |  |  |  | Group Name.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>methods.group</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "aaa_accounting.exec.default.logging") <span style="color:red">deprecated</span> | Boolean |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>methods.method</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;methods</samp>](## "aaa_accounting.exec.default.methods") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;method</samp>](## "aaa_accounting.exec.default.methods.[].method") | String | Required |  | Valid Values:<br>- <code>logging</code><br>- <code>group</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.exec.default.methods.[].group") | String |  |  |  | Specify the server group to be used.<br>This option is applicable only when the `method` key is explicitly set to `group`. |
    | [<samp>&nbsp;&nbsp;system</samp>](## "aaa_accounting.system") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_accounting.system.default") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_accounting.system.default.type") | String |  |  | Valid Values:<br>- <code>none</code><br>- <code>start-stop</code><br>- <code>stop-only</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.system.default.group") <span style="color:red">deprecated</span> | String |  |  |  | Group Name.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>methods.group</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;methods</samp>](## "aaa_accounting.system.default.methods") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;method</samp>](## "aaa_accounting.system.default.methods.[].method") | String | Required |  | Valid Values:<br>- <code>logging</code><br>- <code>group</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.system.default.methods.[].group") | String |  |  |  | Specify the server group to be used.<br>This option is applicable only when the `method` key is explicitly set to `group`. |
    | [<samp>&nbsp;&nbsp;dot1x</samp>](## "aaa_accounting.dot1x") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_accounting.dot1x.default") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_accounting.dot1x.default.type") | String |  |  | Valid Values:<br>- <code>start-stop</code><br>- <code>stop-only</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.dot1x.default.group") <span style="color:red">deprecated</span> | String |  |  |  | Group Name.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>methods.group</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;methods</samp>](## "aaa_accounting.dot1x.default.methods") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;multicast</samp>](## "aaa_accounting.dot1x.default.methods.[].multicast") | Boolean |  |  |  | Forward accounting packets to all servers within the specified group.<br>This option is applicable only when the `method` key is explicitly set to `group`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;method</samp>](## "aaa_accounting.dot1x.default.methods.[].method") | String | Required |  | Valid Values:<br>- <code>logging</code><br>- <code>group</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.dot1x.default.methods.[].group") | String |  |  |  | Specify the server group to be used.<br>This option is applicable only when the `method` key is explicitly set to `group`. |
    | [<samp>&nbsp;&nbsp;commands</samp>](## "aaa_accounting.commands") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;console</samp>](## "aaa_accounting.commands.console") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;commands</samp>](## "aaa_accounting.commands.console.[].commands") | String |  |  |  | Privilege level 'all' or 0-15. Ensure that if ranges are used, they do not overlap with one another. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_accounting.commands.console.[].type") | String |  |  | Valid Values:<br>- <code>none</code><br>- <code>start-stop</code><br>- <code>stop-only</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.commands.console.[].group") <span style="color:red">deprecated</span> | String |  |  |  | Group Name.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>methods.group</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "aaa_accounting.commands.console.[].logging") <span style="color:red">deprecated</span> | Boolean |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>methods.method</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;methods</samp>](## "aaa_accounting.commands.console.[].methods") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;method</samp>](## "aaa_accounting.commands.console.[].methods.[].method") | String | Required |  | Valid Values:<br>- <code>logging</code><br>- <code>group</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.commands.console.[].methods.[].group") | String |  |  |  | Specify the server group to be used.<br>This option is applicable only when the `method` key is explicitly set to `group`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_accounting.commands.default") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;commands</samp>](## "aaa_accounting.commands.default.[].commands") | String |  |  |  | Privilege level 'all' or 0-15. Ensure that if ranges are used, they do not overlap with one another. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_accounting.commands.default.[].type") | String |  |  | Valid Values:<br>- <code>none</code><br>- <code>start-stop</code><br>- <code>stop-only</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.commands.default.[].group") <span style="color:red">deprecated</span> | String |  |  |  | Group Name.<span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>methods.group</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "aaa_accounting.commands.default.[].logging") <span style="color:red">deprecated</span> | Boolean |  |  |  | <span style="color:red">This key is deprecated. Support will be removed in AVD version 6.0.0. Use <samp>methods.method</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;methods</samp>](## "aaa_accounting.commands.default.[].methods") | List, items: Dictionary |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;method</samp>](## "aaa_accounting.commands.default.[].methods.[].method") | String | Required |  | Valid Values:<br>- <code>logging</code><br>- <code>group</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.commands.default.[].methods.[].group") | String |  |  |  | Specify the server group to be used.<br>This option is applicable only when the `method` key is explicitly set to `group`. |

=== "YAML"

    ```yaml
    aaa_accounting:
      exec:
        console:
          type: <str; "none" | "start-stop" | "stop-only"; required>

          # Group Name.
          # This key is deprecated.
          # Support will be removed in AVD version 6.0.0.
          # Use <samp>methods.group</samp> instead.
          group: <str>
          # This key is deprecated.
          # Support will be removed in AVD version 6.0.0.
          # Use <samp>methods.method</samp> instead.
          logging: <bool>
          methods: # >=1 items
            - method: <str; "logging" | "group"; required>

              # Specify the server group to be used.
              # This option is applicable only when the `method` key is explicitly set to `group`.
              group: <str>
        default:
          type: <str; "none" | "start-stop" | "stop-only">

          # Group Name.
          # This key is deprecated.
          # Support will be removed in AVD version 6.0.0.
          # Use <samp>methods.group</samp> instead.
          group: <str>
          # This key is deprecated.
          # Support will be removed in AVD version 6.0.0.
          # Use <samp>methods.method</samp> instead.
          logging: <bool>
          methods: # >=1 items
            - method: <str; "logging" | "group"; required>

              # Specify the server group to be used.
              # This option is applicable only when the `method` key is explicitly set to `group`.
              group: <str>
      system:
        default:
          type: <str; "none" | "start-stop" | "stop-only">

          # Group Name.
          # This key is deprecated.
          # Support will be removed in AVD version 6.0.0.
          # Use <samp>methods.group</samp> instead.
          group: <str>
          methods: # >=1 items
            - method: <str; "logging" | "group"; required>

              # Specify the server group to be used.
              # This option is applicable only when the `method` key is explicitly set to `group`.
              group: <str>
      dot1x:
        default:
          type: <str; "start-stop" | "stop-only">

          # Group Name.
          # This key is deprecated.
          # Support will be removed in AVD version 6.0.0.
          # Use <samp>methods.group</samp> instead.
          group: <str>
          methods: # >=1 items

              # Forward accounting packets to all servers within the specified group.
              # This option is applicable only when the `method` key is explicitly set to `group`.
            - multicast: <bool>
              method: <str; "logging" | "group"; required>

              # Specify the server group to be used.
              # This option is applicable only when the `method` key is explicitly set to `group`.
              group: <str>
      commands:
        console:

            # Privilege level 'all' or 0-15. Ensure that if ranges are used, they do not overlap with one another.
          - commands: <str>
            type: <str; "none" | "start-stop" | "stop-only">

            # Group Name.
            # This key is deprecated.
            # Support will be removed in AVD version 6.0.0.
            # Use <samp>methods.group</samp> instead.
            group: <str>
            # This key is deprecated.
            # Support will be removed in AVD version 6.0.0.
            # Use <samp>methods.method</samp> instead.
            logging: <bool>
            methods: # >=1 items
              - method: <str; "logging" | "group"; required>

                # Specify the server group to be used.
                # This option is applicable only when the `method` key is explicitly set to `group`.
                group: <str>
        default:

            # Privilege level 'all' or 0-15. Ensure that if ranges are used, they do not overlap with one another.
          - commands: <str>
            type: <str; "none" | "start-stop" | "stop-only">

            # Group Name.
            # This key is deprecated.
            # Support will be removed in AVD version 6.0.0.
            # Use <samp>methods.group</samp> instead.
            group: <str>
            # This key is deprecated.
            # Support will be removed in AVD version 6.0.0.
            # Use <samp>methods.method</samp> instead.
            logging: <bool>
            methods: # >=1 items
              - method: <str; "logging" | "group"; required>

                # Specify the server group to be used.
                # This option is applicable only when the `method` key is explicitly set to `group`.
                group: <str>
    ```
