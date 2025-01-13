<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>aaa_root</samp>](## "aaa_root") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;disabled</samp>](## "aaa_root.disabled") | Boolean |  |  |  | Set to `true` to configure `no aaa root` which is the EOS default. |
    | [<samp>&nbsp;&nbsp;secret</samp>](## "aaa_root.secret") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sha512_password</samp>](## "aaa_root.secret.sha512_password") | String |  |  |  |  |

=== "YAML"

    ```yaml
    aaa_root:

      # Set to `true` to configure `no aaa root` which is the EOS default.
      disabled: <bool>
      secret:
        sha512_password: <str>
    ```
