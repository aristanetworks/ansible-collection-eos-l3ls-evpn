<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>aliases</samp>](## "aliases") | String |  |  |  | Multi-line string with one or more alias commands.<br><br>Example:<br><br>```yaml<br>aliases: |<br>  alias wr copy running-config startup-config<br>  alias siib show ip interface brief<br>```<br> |

=== "YAML"

    ```yaml
    # Multi-line string with one or more alias commands.
    #
    # Example:
    #
    # ```yaml
    # aliases: |
    #   alias wr copy running-config startup-config
    #   alias siib show ip interface brief
    # ```
    aliases: <str>
    ```
