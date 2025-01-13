<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>terminal</samp>](## "terminal") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;length</samp>](## "terminal.length") | Integer |  |  | Min: 0<br>Max: 32767 |  |
    | [<samp>&nbsp;&nbsp;width</samp>](## "terminal.width") | Integer |  |  | Min: 10<br>Max: 32767 |  |

=== "YAML"

    ```yaml
    terminal:
      length: <int; 0-32767>
      width: <int; 10-32767>
    ```
