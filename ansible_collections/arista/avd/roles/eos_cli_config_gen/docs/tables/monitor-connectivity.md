<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>monitor_connectivity</samp>](## "monitor_connectivity") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;shutdown</samp>](## "monitor_connectivity.shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;interval</samp>](## "monitor_connectivity.interval") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;interface_sets</samp>](## "monitor_connectivity.interface_sets") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_connectivity.interface_sets.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "monitor_connectivity.interface_sets.[].interfaces") | String |  |  |  | Interface range(s) should be of same type, Ethernet, Loopback, Management etc.<br>Multiple interface ranges can be specified separated by ",".<br> |
    | [<samp>&nbsp;&nbsp;local_interfaces</samp>](## "monitor_connectivity.local_interfaces") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;address_only</samp>](## "monitor_connectivity.address_only") | Boolean |  | `True` |  | When address-only is configured, the source IP of the packet is set to the interface<br>IP but the packet may exit the device via a different interface.<br>When set to `false`, the probe uses the interface to exit the device. |
    | [<samp>&nbsp;&nbsp;hosts</samp>](## "monitor_connectivity.hosts") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_connectivity.hosts.[].name") | String | Required, Unique |  |  | Host Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "monitor_connectivity.hosts.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "monitor_connectivity.hosts.[].ip") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;icmp_echo_size</samp>](## "monitor_connectivity.hosts.[].icmp_echo_size") | Integer |  |  | Min: 36<br>Max: 18024 | Size of ICMP probe in bytes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interfaces</samp>](## "monitor_connectivity.hosts.[].local_interfaces") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_only</samp>](## "monitor_connectivity.hosts.[].address_only") | Boolean |  | `True` |  | When address-only is configured, the source IP of the packet is set to the interface<br>IP but the packet may exit the device via a different interface.<br>When set to `false`, the probe uses the interface to exit the device. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;url</samp>](## "monitor_connectivity.hosts.[].url") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "monitor_connectivity.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_connectivity.vrfs.[].name") | String | Required, Unique |  |  | VRF Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "monitor_connectivity.vrfs.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interface_sets</samp>](## "monitor_connectivity.vrfs.[].interface_sets") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_connectivity.vrfs.[].interface_sets.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "monitor_connectivity.vrfs.[].interface_sets.[].interfaces") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interfaces</samp>](## "monitor_connectivity.vrfs.[].local_interfaces") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_only</samp>](## "monitor_connectivity.vrfs.[].address_only") | Boolean |  | `True` |  | When address-only is configured, the source IP of the packet is set to the interface<br>IP but the packet may exit the device via a different interface.<br>When set to `false`, the probe uses the interface to exit the device. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hosts</samp>](## "monitor_connectivity.vrfs.[].hosts") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "monitor_connectivity.vrfs.[].hosts.[].name") | String | Required, Unique |  |  | Host name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "monitor_connectivity.vrfs.[].hosts.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip</samp>](## "monitor_connectivity.vrfs.[].hosts.[].ip") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;icmp_echo_size</samp>](## "monitor_connectivity.vrfs.[].hosts.[].icmp_echo_size") | Integer |  |  | Min: 36<br>Max: 18024 | Size of ICMP probe in bytes. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interfaces</samp>](## "monitor_connectivity.vrfs.[].hosts.[].local_interfaces") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_only</samp>](## "monitor_connectivity.vrfs.[].hosts.[].address_only") | Boolean |  | `True` |  | When address-only is configured, the source IP of the packet is set to the interface<br>IP but the packet may exit the device via a different interface.<br>When set to `false`, the probe uses the interface to exit the device. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;url</samp>](## "monitor_connectivity.vrfs.[].hosts.[].url") | String |  |  |  |  |

=== "YAML"

    ```yaml
    monitor_connectivity:
      shutdown: <bool>
      interval: <int>
      interface_sets:
        - name: <str>

          # Interface range(s) should be of same type, Ethernet, Loopback, Management etc.
          # Multiple interface ranges can be specified separated by ",".
          interfaces: <str>
      local_interfaces: <str>

      # When address-only is configured, the source IP of the packet is set to the interface
      # IP but the packet may exit the device via a different interface.
      # When set to `false`, the probe uses the interface to exit the device.
      address_only: <bool; default=True>
      hosts:

          # Host Name.
        - name: <str; required; unique>
          description: <str>
          ip: <str>

          # Size of ICMP probe in bytes.
          icmp_echo_size: <int; 36-18024>
          local_interfaces: <str>

          # When address-only is configured, the source IP of the packet is set to the interface
          # IP but the packet may exit the device via a different interface.
          # When set to `false`, the probe uses the interface to exit the device.
          address_only: <bool; default=True>
          url: <str>
      vrfs:

          # VRF Name.
        - name: <str; required; unique>
          description: <str>
          interface_sets:
            - name: <str>
              interfaces: <str>
          local_interfaces: <str>

          # When address-only is configured, the source IP of the packet is set to the interface
          # IP but the packet may exit the device via a different interface.
          # When set to `false`, the probe uses the interface to exit the device.
          address_only: <bool; default=True>
          hosts:

              # Host name.
            - name: <str; required; unique>
              description: <str>
              ip: <str>

              # Size of ICMP probe in bytes.
              icmp_echo_size: <int; 36-18024>
              local_interfaces: <str>

              # When address-only is configured, the source IP of the packet is set to the interface
              # IP but the packet may exit the device via a different interface.
              # When set to `false`, the probe uses the interface to exit the device.
              address_only: <bool; default=True>
              url: <str>
    ```
