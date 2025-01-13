<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>bfd_multihop</samp>](## "bfd_multihop") | Dictionary |  | See (+) on YAML tab |  | BFD Multihop tuning. |
    | [<samp>&nbsp;&nbsp;interval</samp>](## "bfd_multihop.interval") | Integer | Required |  | Min: 50<br>Max: 60000 |  |
    | [<samp>&nbsp;&nbsp;min_rx</samp>](## "bfd_multihop.min_rx") | Integer | Required |  | Min: 50<br>Max: 60000 |  |
    | [<samp>&nbsp;&nbsp;multiplier</samp>](## "bfd_multihop.multiplier") | Integer | Required |  | Min: 3<br>Max: 50 |  |

=== "YAML"

    ```yaml
    # BFD Multihop tuning.
    bfd_multihop: # (1)!
      interval: <int; 50-60000; required>
      min_rx: <int; 50-60000; required>
      multiplier: <int; 3-50; required>
    ```

    1. Default Value

        ```yaml
        bfd_multihop:
          interval: 300
          min_rx: 300
          multiplier: 3
        ```
