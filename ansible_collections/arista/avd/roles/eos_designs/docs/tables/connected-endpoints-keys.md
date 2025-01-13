<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>connected_endpoints_keys</samp>](## "connected_endpoints_keys") | List, items: Dictionary |  | See (+) on YAML tab |  | Endpoints connecting to the fabric can be grouped by using separate keys.<br>The keys can be customized to provide a better better organization or grouping of your data.<br>`connected_endpoints_keys` should be defined in the top level group_vars for the fabric.<br>The default values will be overridden if defining this key, so it is recommended to copy the defaults and modify them.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;key</samp>](## "connected_endpoints_keys.[].key") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "connected_endpoints_keys.[].type") | String |  |  |  | Type used for documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "connected_endpoints_keys.[].description") | String |  |  |  | Description used for documentation. |

=== "YAML"

    ```yaml
    # Endpoints connecting to the fabric can be grouped by using separate keys.
    # The keys can be customized to provide a better better organization or grouping of your data.
    # `connected_endpoints_keys` should be defined in the top level group_vars for the fabric.
    # The default values will be overridden if defining this key, so it is recommended to copy the defaults and modify them.
    connected_endpoints_keys: # (1)!
      - key: <str; required; unique>

        # Type used for documentation.
        type: <str>

        # Description used for documentation.
        description: <str>
    ```

    1. Default Value

        ```yaml
        connected_endpoints_keys:
        - description: Server
          key: servers
          type: server
        - description: Firewall
          key: firewalls
          type: firewall
        - description: Router
          key: routers
          type: router
        - description: Load Balancer
          key: load_balancers
          type: load_balancer
        - description: Storage Array
          key: storage_arrays
          type: storage_array
        - description: CPE
          key: cpes
          type: cpe
        - description: Workstation
          key: workstations
          type: workstation
        - description: Access Point
          key: access_points
          type: access_point
        - description: Phone
          key: phones
          type: phone
        - description: Printer
          key: printers
          type: printer
        - description: Camera
          key: cameras
          type: camera
        - description: Generic Device
          key: generic_devices
          type: generic_device
        ```
