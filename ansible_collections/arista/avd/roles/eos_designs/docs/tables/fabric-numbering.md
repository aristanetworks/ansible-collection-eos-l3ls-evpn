<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>fabric_numbering</samp>](## "fabric_numbering") | Dictionary |  |  |  | PREVIEW: This feature is in marked as "preview", which means it is subject to change at any time.<br><br>Assignment policies for numbers like Node ID. |
    | [<samp>&nbsp;&nbsp;node_id</samp>](## "fabric_numbering.node_id") | Dictionary |  |  |  | Assignment policy for Node ID.<br>Node ID is mainly used for IP address assignment but can also affect BGP AS and/or<br>interface assignments depending on other settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;algorithm</samp>](## "fabric_numbering.node_id.algorithm") | String |  | `static` | Valid Values:<br>- <code>static</code><br>- <code>pool_manager</code> | IDs will be automatically assigned according to the configured algorithm.<br>- `static` will use the statically set IDs under node setting.<br>- `pool_manager` will activate the pool manager for ID pools.<br>  Any statically set ID under node settings will be reserved in the pool if possible.<br>  Otherwise an error will be raised. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pools_file</samp>](## "fabric_numbering.node_id.pools_file") | String |  |  |  | Path to file to use for storing ID pool data when using "pool_manager" as algorithm.<br>This can be an absolute path or a path relative to current working directory.<br><br>By default the path is "<root_dir>/intended/data/<fabric_name>-ids.yml".<br><br>Note: Since the pool manager will remove stale entries after every run, each fabric should be using its own file. |

=== "YAML"

    ```yaml
    # PREVIEW: This feature is in marked as "preview", which means it is subject to change at any time.
    #
    # Assignment policies for numbers like Node ID.
    fabric_numbering:

      # Assignment policy for Node ID.
      # Node ID is mainly used for IP address assignment but can also affect BGP AS and/or
      # interface assignments depending on other settings.
      node_id:

        # IDs will be automatically assigned according to the configured algorithm.
        # - `static` will use the statically set IDs under node setting.
        # - `pool_manager` will activate the pool manager for ID pools.
        #   Any statically set ID under node settings will be reserved in the pool if possible.
        #   Otherwise an error will be raised.
        algorithm: <str; "static" | "pool_manager"; default="static">

        # Path to file to use for storing ID pool data when using "pool_manager" as algorithm.
        # This can be an absolute path or a path relative to current working directory.
        #
        # By default the path is "<root_dir>/intended/data/<fabric_name>-ids.yml".
        #
        # Note: Since the pool manager will remove stale entries after every run, each fabric should be using its own file.
        pools_file: <str>
    ```
