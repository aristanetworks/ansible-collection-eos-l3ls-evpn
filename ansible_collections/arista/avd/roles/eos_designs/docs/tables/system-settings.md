<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;node_type_keys.key&gt;</samp>](## "<node_type_keys.key>") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;defaults</samp>](## "<node_type_keys.key>.defaults") | Dictionary |  |  |  | Define variables for all nodes of this type. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;data_plane_cpu_allocation_max</samp>](## "<node_type_keys.key>.defaults.data_plane_cpu_allocation_max") | Integer |  |  | Min: 1<br>Max: 128 | Set the maximum number of CPU used for the data plane.<br>This setting is useful on virtual Route Reflectors and Pathfinders where more CPU cores should be allocated for control plane. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;data_plane_cpu_allocation_max</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].data_plane_cpu_allocation_max") | Integer |  |  | Min: 1<br>Max: 128 | Set the maximum number of CPU used for the data plane.<br>This setting is useful on virtual Route Reflectors and Pathfinders where more CPU cores should be allocated for control plane. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;data_plane_cpu_allocation_max</samp>](## "<node_type_keys.key>.node_groups.[].data_plane_cpu_allocation_max") | Integer |  |  | Min: 1<br>Max: 128 | Set the maximum number of CPU used for the data plane.<br>This setting is useful on virtual Route Reflectors and Pathfinders where more CPU cores should be allocated for control plane. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;data_plane_cpu_allocation_max</samp>](## "<node_type_keys.key>.nodes.[].data_plane_cpu_allocation_max") | Integer |  |  | Min: 1<br>Max: 128 | Set the maximum number of CPU used for the data plane.<br>This setting is useful on virtual Route Reflectors and Pathfinders where more CPU cores should be allocated for control plane. |
    | [<samp>default_igmp_snooping_enabled</samp>](## "default_igmp_snooping_enabled") | Boolean |  | `True` |  | When set to false, disables IGMP snooping at fabric level and overrides per vlan settings.<br> |
    | [<samp>default_interface_mtu</samp>](## "default_interface_mtu") | Integer |  |  | Min: 68<br>Max: 65535 | Default interface MTU configured on EOS under "interface defaults".<br>Can be overridden per platform under platform settings.<br> |
    | [<samp>hardware_counters</samp>](## "hardware_counters") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;features</samp>](## "hardware_counters.features") | List, items: Dictionary |  |  |  | This data model allows to configure the list of hardware counters feature<br>available on Arista platforms.<br><br>The `name` key accepts a list of valid_values which MUST be updated to support<br>new feature as they are released in EOS.<br><br>The available values of the different keys like 'direction' or 'address_type'<br>are feature and hardware dependent and this model DOES NOT validate that the<br>combinations are valid. It is the responsibility of the user of this data model<br>to make sure that the rendered CLI is accepted by the targeted device.<br><br>Examples:<br><br>  * Use:<br>    ```yaml<br>    hardware_counters:<br>      features:<br>        - name: ip<br>          direction: out<br>          layer3: true<br>          units_packets: true<br>    ```<br><br>    to render:<br>    ```eos<br>    hardware counter feature ip out layer3 units packets<br>    ```<br>  * Use:<br>    ```yaml<br>    hardware_counters:<br>      features:<br>        - name: route<br>          address_type: ipv4<br>          vrf: test<br>          prefix: 192.168.0.0/24<br>    ```<br><br>    to render:<br>    ```eos<br>    hardware counter feature route ipv4 vrf test 192.168.0.0/24<br>    ```<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "hardware_counters.features.[].name") | String | Required |  | Valid Values:<br>- <code>acl</code><br>- <code>decap-group</code><br>- <code>directflow</code><br>- <code>ecn</code><br>- <code>flow-spec</code><br>- <code>gre tunnel interface</code><br>- <code>ip</code><br>- <code>mpls interface</code><br>- <code>mpls lfib</code><br>- <code>mpls tunnel</code><br>- <code>multicast</code><br>- <code>nexthop</code><br>- <code>pbr</code><br>- <code>pdp</code><br>- <code>policing interface</code><br>- <code>qos</code><br>- <code>qos dual-rate-policer</code><br>- <code>route</code><br>- <code>routed-port</code><br>- <code>segment-security</code><br>- <code>subinterface</code><br>- <code>tapagg</code><br>- <code>traffic-class</code><br>- <code>traffic-policy</code><br>- <code>vlan</code><br>- <code>vlan-interface</code><br>- <code>vni decap</code><br>- <code>vni encap</code><br>- <code>vtep decap</code><br>- <code>vtep encap</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "hardware_counters.features.[].direction") | String |  |  | Valid Values:<br>- <code>in</code><br>- <code>out</code><br>- <code>cpu</code> | Most features support only 'in' and 'out'. Some like traffic-policy support 'cpu'.<br>Some features DO NOT have any direction.<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_type</samp>](## "hardware_counters.features.[].address_type") | String |  |  | Valid Values:<br>- <code>ipv4</code><br>- <code>ipv6</code><br>- <code>mac</code> | Supported only for the following features:<br>- acl: [ipv4, ipv6, mac] if direction is 'out'<br>- multicast: [ipv4, ipv6]<br>- route: [ipv4, ipv6]<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;layer3</samp>](## "hardware_counters.features.[].layer3") | Boolean |  |  |  | Supported only for the 'ip' feature.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "hardware_counters.features.[].vrf") | String |  |  |  | Supported only for the 'route' feature.<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix</samp>](## "hardware_counters.features.[].prefix") | String |  |  |  | Supported only for the 'route' feature.<br>Mandatory for the 'route' feature.<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;units_packets</samp>](## "hardware_counters.features.[].units_packets") | Boolean |  |  |  |  |
    | [<samp>internal_vlan_order</samp>](## "internal_vlan_order") | Dictionary |  | See (+) on YAML tab |  | Internal vlan allocation order and range. |
    | [<samp>&nbsp;&nbsp;allocation</samp>](## "internal_vlan_order.allocation") | String | Required |  | Valid Values:<br>- <code>ascending</code><br>- <code>descending</code> |  |
    | [<samp>&nbsp;&nbsp;range</samp>](## "internal_vlan_order.range") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;beginning</samp>](## "internal_vlan_order.range.beginning") | Integer | Required |  | Min: 2<br>Max: 4094 | First VLAN ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ending</samp>](## "internal_vlan_order.range.ending") | Integer | Required |  | Min: 2<br>Max: 4094 | Last VLAN ID. |
    | [<samp>mac_address_table</samp>](## "mac_address_table") | Dictionary |  |  |  | MAC address-table aging time.<br>Use to change the EOS default of 300.<br> |
    | [<samp>&nbsp;&nbsp;aging_time</samp>](## "mac_address_table.aging_time") | Integer |  |  | Min: 0<br>Max: 1000000 | Aging time in seconds 10-1000000.<br>Enter 0 to disable aging.<br> |
    | [<samp>queue_monitor_length</samp>](## "queue_monitor_length") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enabled</samp>](## "queue_monitor_length.enabled") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;notifying</samp>](## "queue_monitor_length.notifying") | Boolean |  |  |  | If True, `eos_designs` will configure `queue-monitor length notifying` according to the<br>`platform_settings.[].feature_support.queue_monitor_length_notify` setting.<br> |
    | [<samp>&nbsp;&nbsp;default_thresholds</samp>](## "queue_monitor_length.default_thresholds") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;high</samp>](## "queue_monitor_length.default_thresholds.high") | Integer | Required |  |  | Default high threshold for Ethernet Interfaces.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;low</samp>](## "queue_monitor_length.default_thresholds.low") | Integer |  |  |  | Default low threshold for Ethernet Interfaces.<br>Low threshold support is platform dependent.<br> |
    | [<samp>&nbsp;&nbsp;log</samp>](## "queue_monitor_length.log") | Integer |  |  |  | Logging interval in seconds. |
    | [<samp>&nbsp;&nbsp;cpu</samp>](## "queue_monitor_length.cpu") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;thresholds</samp>](## "queue_monitor_length.cpu.thresholds") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;high</samp>](## "queue_monitor_length.cpu.thresholds.high") | Integer | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;low</samp>](## "queue_monitor_length.cpu.thresholds.low") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;tx_latency</samp>](## "queue_monitor_length.tx_latency") | Boolean |  |  |  | Enable tx-latency mode. |
    | [<samp>redundancy</samp>](## "redundancy") | Dictionary |  |  |  | Redundancy for chassis platforms with dual supervisors | Optional. |
    | [<samp>&nbsp;&nbsp;protocol</samp>](## "redundancy.protocol") | String |  |  | Valid Values:<br>- <code>sso</code><br>- <code>rpr</code> |  |
    | [<samp>serial_number</samp>](## "serial_number") | String |  |  |  | Serial Number of the device.<br>Used for documentation purpose in the fabric documentation as can also be used by the 'eos_config_deploy_cvp' role.<br>"serial_number" can also be set directly under node type settings.<br>If both are set, the value under node type settings takes precedence.<br> |
    | [<samp>system_mac_address</samp>](## "system_mac_address") | String |  |  |  | Set to the same MAC address as available in "show version" on the device.<br>"system_mac_address" can also be set under node type settings.<br>If both are set, the value under node type settings takes precedence.<br> |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:

        # Set the maximum number of CPU used for the data plane.
        # This setting is useful on virtual Route Reflectors and Pathfinders where more CPU cores should be allocated for control plane.
        data_plane_cpu_allocation_max: <int; 1-128>

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>

              # Set the maximum number of CPU used for the data plane.
              # This setting is useful on virtual Route Reflectors and Pathfinders where more CPU cores should be allocated for control plane.
              data_plane_cpu_allocation_max: <int; 1-128>

          # Set the maximum number of CPU used for the data plane.
          # This setting is useful on virtual Route Reflectors and Pathfinders where more CPU cores should be allocated for control plane.
          data_plane_cpu_allocation_max: <int; 1-128>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>

          # Set the maximum number of CPU used for the data plane.
          # This setting is useful on virtual Route Reflectors and Pathfinders where more CPU cores should be allocated for control plane.
          data_plane_cpu_allocation_max: <int; 1-128>

    # When set to false, disables IGMP snooping at fabric level and overrides per vlan settings.
    default_igmp_snooping_enabled: <bool; default=True>

    # Default interface MTU configured on EOS under "interface defaults".
    # Can be overridden per platform under platform settings.
    default_interface_mtu: <int; 68-65535>
    hardware_counters:

      # This data model allows to configure the list of hardware counters feature
      # available on Arista platforms.
      #
      # The `name` key accepts a list of valid_values which MUST be updated to support
      # new feature as they are released in EOS.
      #
      # The available values of the different keys like 'direction' or 'address_type'
      # are feature and hardware dependent and this model DOES NOT validate that the
      # combinations are valid. It is the responsibility of the user of this data model
      # to make sure that the rendered CLI is accepted by the targeted device.
      #
      # Examples:
      #
      #   * Use:
      #     ```yaml
      #     hardware_counters:
      #       features:
      #         - name: ip
      #           direction: out
      #           layer3: true
      #           units_packets: true
      #     ```
      #
      #     to render:
      #     ```eos
      #     hardware counter feature ip out layer3 units packets
      #     ```
      #   * Use:
      #     ```yaml
      #     hardware_counters:
      #       features:
      #         - name: route
      #           address_type: ipv4
      #           vrf: test
      #           prefix: 192.168.0.0/24
      #     ```
      #
      #     to render:
      #     ```eos
      #     hardware counter feature route ipv4 vrf test 192.168.0.0/24
      #     ```
      features:
        - name: <str; "acl" | "decap-group" | "directflow" | "ecn" | "flow-spec" | "gre tunnel interface" | "ip" | "mpls interface" | "mpls lfib" | "mpls tunnel" | "multicast" | "nexthop" | "pbr" | "pdp" | "policing interface" | "qos" | "qos dual-rate-policer" | "route" | "routed-port" | "segment-security" | "subinterface" | "tapagg" | "traffic-class" | "traffic-policy" | "vlan" | "vlan-interface" | "vni decap" | "vni encap" | "vtep decap" | "vtep encap"; required>

          # Most features support only 'in' and 'out'. Some like traffic-policy support 'cpu'.
          # Some features DO NOT have any direction.
          # This validation IS NOT made by the schemas.
          direction: <str; "in" | "out" | "cpu">

          # Supported only for the following features:
          # - acl: [ipv4, ipv6, mac] if direction is 'out'
          # - multicast: [ipv4, ipv6]
          # - route: [ipv4, ipv6]
          # This validation IS NOT made by the schemas.
          address_type: <str; "ipv4" | "ipv6" | "mac">

          # Supported only for the 'ip' feature.
          layer3: <bool>

          # Supported only for the 'route' feature.
          # This validation IS NOT made by the schemas.
          vrf: <str>

          # Supported only for the 'route' feature.
          # Mandatory for the 'route' feature.
          # This validation IS NOT made by the schemas.
          prefix: <str>
          units_packets: <bool>

    # Internal vlan allocation order and range.
    internal_vlan_order: # (1)!
      allocation: <str; "ascending" | "descending"; required>
      range:

        # First VLAN ID.
        beginning: <int; 2-4094; required>

        # Last VLAN ID.
        ending: <int; 2-4094; required>

    # MAC address-table aging time.
    # Use to change the EOS default of 300.
    mac_address_table:

      # Aging time in seconds 10-1000000.
      # Enter 0 to disable aging.
      aging_time: <int; 0-1000000>
    queue_monitor_length:
      enabled: <bool; required>

      # If True, `eos_designs` will configure `queue-monitor length notifying` according to the
      # `platform_settings.[].feature_support.queue_monitor_length_notify` setting.
      notifying: <bool>
      default_thresholds:

        # Default high threshold for Ethernet Interfaces.
        high: <int; required>

        # Default low threshold for Ethernet Interfaces.
        # Low threshold support is platform dependent.
        low: <int>

      # Logging interval in seconds.
      log: <int>
      cpu:
        thresholds:
          high: <int; required>
          low: <int>

      # Enable tx-latency mode.
      tx_latency: <bool>

    # Redundancy for chassis platforms with dual supervisors | Optional.
    redundancy:
      protocol: <str; "sso" | "rpr">

    # Serial Number of the device.
    # Used for documentation purpose in the fabric documentation as can also be used by the 'eos_config_deploy_cvp' role.
    # "serial_number" can also be set directly under node type settings.
    # If both are set, the value under node type settings takes precedence.
    serial_number: <str>

    # Set to the same MAC address as available in "show version" on the device.
    # "system_mac_address" can also be set under node type settings.
    # If both are set, the value under node type settings takes precedence.
    system_mac_address: <str>
    ```

    1. Default Value

        ```yaml
        internal_vlan_order:
          allocation: ascending
          range:
            beginning: 1006
            ending: 1199
        ```
