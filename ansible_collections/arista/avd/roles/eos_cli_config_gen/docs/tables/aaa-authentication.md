<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>aaa_authentication</samp>](## "aaa_authentication") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;login</samp>](## "aaa_authentication.login") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_authentication.login.default") | String |  |  |  | Login authentication method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group radius group MYGROUP local"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;console</samp>](## "aaa_authentication.login.console") | String |  |  |  | Console authentication method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group radius group MYGROUP local"<br> |
    | [<samp>&nbsp;&nbsp;enable</samp>](## "aaa_authentication.enable") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_authentication.enable.default") | String |  |  |  | Enable authentication method(s) as a string.<br>Examples:<br>- "group tacacs+ local"<br>- "group MYGROUP none"<br>- "group radius group MYGROUP local"<br> |
    | [<samp>&nbsp;&nbsp;dot1x</samp>](## "aaa_authentication.dot1x") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;default</samp>](## "aaa_authentication.dot1x.default") | String |  |  |  | 802.1x authentication method(s) as a string.<br>Examples:<br>- "group radius"<br>- "group MYGROUP group radius"<br> |
    | [<samp>&nbsp;&nbsp;policies</samp>](## "aaa_authentication.policies") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;on_failure_log</samp>](## "aaa_authentication.policies.on_failure_log") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;on_success_log</samp>](## "aaa_authentication.policies.on_success_log") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;local</samp>](## "aaa_authentication.policies.local") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allow_nopassword</samp>](## "aaa_authentication.policies.local.allow_nopassword") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lockout</samp>](## "aaa_authentication.policies.lockout") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;failure</samp>](## "aaa_authentication.policies.lockout.failure") | Integer |  |  | Min: 1<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;duration</samp>](## "aaa_authentication.policies.lockout.duration") | Integer |  |  | Min: 1<br>Max: 4294967295 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;window</samp>](## "aaa_authentication.policies.lockout.window") | Integer |  |  | Min: 1<br>Max: 4294967295 |  |

=== "YAML"

    ```yaml
    aaa_authentication:
      login:

        # Login authentication method(s) as a string.
        # Examples:
        # - "group tacacs+ local"
        # - "group MYGROUP none"
        # - "group radius group MYGROUP local"
        default: <str>

        # Console authentication method(s) as a string.
        # Examples:
        # - "group tacacs+ local"
        # - "group MYGROUP none"
        # - "group radius group MYGROUP local"
        console: <str>
      enable:

        # Enable authentication method(s) as a string.
        # Examples:
        # - "group tacacs+ local"
        # - "group MYGROUP none"
        # - "group radius group MYGROUP local"
        default: <str>
      dot1x:

        # 802.1x authentication method(s) as a string.
        # Examples:
        # - "group radius"
        # - "group MYGROUP group radius"
        default: <str>
      policies:
        on_failure_log: <bool>
        on_success_log: <bool>
        local:
          allow_nopassword: <bool>
        lockout:
          failure: <int; 1-255>
          duration: <int; 1-4294967295>
          window: <int; 1-4294967295>
    ```
