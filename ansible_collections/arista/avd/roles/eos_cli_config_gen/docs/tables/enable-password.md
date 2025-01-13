<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>enable_password</samp>](## "enable_password") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;disabled</samp>](## "enable_password.disabled") | Boolean |  |  |  | Set to `true` to configure `no enable password` which is the EOS default. |
    | [<samp>&nbsp;&nbsp;hash_algorithm</samp>](## "enable_password.hash_algorithm") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>sha512</code> |  |
    | [<samp>&nbsp;&nbsp;key</samp>](## "enable_password.key") | String |  |  |  | Must be the hash of the password using the specified algorithm.<br>By default EOS salts the password, so the simplest is to generate the hash on an EOS device.<br> |

=== "YAML"

    ```yaml
    enable_password:

      # Set to `true` to configure `no enable password` which is the EOS default.
      disabled: <bool>
      hash_algorithm: <str; "md5" | "sha512">

      # Must be the hash of the password using the specified algorithm.
      # By default EOS salts the password, so the simplest is to generate the hash on an EOS device.
      key: <str>
    ```
