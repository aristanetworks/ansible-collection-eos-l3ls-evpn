<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.exec.console.group") | String |  |  |  | Group Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "aaa_accounting.exec.console.logging") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_accounting.exec.default") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_accounting.exec.default.type") | String |  |  | Valid Values:<br>- <code>none</code><br>- <code>start-stop</code><br>- <code>stop-only</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.exec.default.group") | String |  |  |  | Group Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "aaa_accounting.exec.default.logging") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;system</samp>](## "aaa_accounting.system") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_accounting.system.default") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_accounting.system.default.type") | String |  |  | Valid Values:<br>- <code>none</code><br>- <code>start-stop</code><br>- <code>stop-only</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.system.default.group") | String |  |  |  | Group Name. |
    | [<samp>&nbsp;&nbsp;dot1x</samp>](## "aaa_accounting.dot1x") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_accounting.dot1x.default") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_accounting.dot1x.default.type") | String |  |  | Valid Values:<br>- <code>start-stop</code><br>- <code>stop-only</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.dot1x.default.group") | String |  |  |  | Group Name. |
    | [<samp>&nbsp;&nbsp;commands</samp>](## "aaa_accounting.commands") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;console</samp>](## "aaa_accounting.commands.console") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;commands</samp>](## "aaa_accounting.commands.console.[].commands") | String |  |  |  | Privilege level 'all' or 0-15. Ensure that if ranges are used, they do not overlap with one another. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_accounting.commands.console.[].type") | String |  |  | Valid Values:<br>- <code>none</code><br>- <code>start-stop</code><br>- <code>stop-only</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.commands.console.[].group") | String |  |  |  | Group Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "aaa_accounting.commands.console.[].logging") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_accounting.commands.default") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;commands</samp>](## "aaa_accounting.commands.default.[].commands") | String |  |  |  | Privilege level 'all' or 0-15. Ensure that if ranges are used, they do not overlap with one another. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "aaa_accounting.commands.default.[].type") | String |  |  | Valid Values:<br>- <code>none</code><br>- <code>start-stop</code><br>- <code>stop-only</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "aaa_accounting.commands.default.[].group") | String |  |  |  | Group Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;logging</samp>](## "aaa_accounting.commands.default.[].logging") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    aaa_accounting:
      exec:
        console:
          type: <str; "none" | "start-stop" | "stop-only"; required>

          # Group Name.
          group: <str>
          logging: <bool>
        default:
          type: <str; "none" | "start-stop" | "stop-only">

          # Group Name.
          group: <str>
          logging: <bool>
      system:
        default:
          type: <str; "none" | "start-stop" | "stop-only">

          # Group Name.
          group: <str>
      dot1x:
        default:
          type: <str; "start-stop" | "stop-only">

          # Group Name.
          group: <str>
      commands:
        console:

            # Privilege level 'all' or 0-15. Ensure that if ranges are used, they do not overlap with one another.
          - commands: <str>
            type: <str; "none" | "start-stop" | "stop-only">

            # Group Name.
            group: <str>
            logging: <bool>
        default:

            # Privilege level 'all' or 0-15. Ensure that if ranges are used, they do not overlap with one another.
          - commands: <str>
            type: <str; "none" | "start-stop" | "stop-only">

            # Group Name.
            group: <str>
            logging: <bool>
    ```
