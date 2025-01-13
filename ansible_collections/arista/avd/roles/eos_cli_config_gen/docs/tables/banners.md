<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>banners</samp>](## "banners") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;login</samp>](## "banners.login") | String |  |  |  | Multiline string ending with EOF on the last line. |
    | [<samp>&nbsp;&nbsp;motd</samp>](## "banners.motd") | String |  |  |  | Multiline string ending with EOF on the last line. |

=== "YAML"

    ```yaml
    banners:

      # Multiline string ending with EOF on the last line.
      login: <str>

      # Multiline string ending with EOF on the last line.
      motd: <str>
    ```
