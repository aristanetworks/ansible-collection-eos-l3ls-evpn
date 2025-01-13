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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "<node_type_keys.key>.defaults.id") | Integer |  |  |  | Unique identifier used for IP addressing and other algorithms. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;platform</samp>](## "<node_type_keys.key>.defaults.platform") | String |  |  |  | Arista platform family. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mac_address</samp>](## "<node_type_keys.key>.defaults.mac_address") | String |  |  |  | Leverage to document management interface mac address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;system_mac_address</samp>](## "<node_type_keys.key>.defaults.system_mac_address") | String |  |  |  | System MAC Address in this following format: "xx:xx:xx:xx:xx:xx".<br>Set to the same MAC address as available in "show version" on the device.<br>"system_mac_address" can also be set directly as a hostvar.<br>If both are set, the setting under node type settings takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;serial_number</samp>](## "<node_type_keys.key>.defaults.serial_number") | String |  |  |  | Set to the Serial Number of the device.<br>Only used for documentation purpose in the fabric documentation and part of the structured_config.<br>"serial_number" can also be set directly as a hostvar.<br>If both are set, the setting under node type settings takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "<node_type_keys.key>.defaults.rack") | String |  |  |  | Rack that the switch is located in (only used in snmp_settings location). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "<node_type_keys.key>.defaults.mgmt_ip") | String |  |  | Format: cidr | Node management interface IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6_mgmt_ip</samp>](## "<node_type_keys.key>.defaults.ipv6_mgmt_ip") | String |  |  | Format: cidr | Node management interface IPv6 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;mgmt_interface</samp>](## "<node_type_keys.key>.defaults.mgmt_interface") | String |  |  |  | Management Interface Name.<br>Default -> platform_management_interface -> mgmt_interface -> "Management1".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lacp_port_id_range</samp>](## "<node_type_keys.key>.defaults.lacp_port_id_range") | Dictionary |  |  |  | This will generate the "lacp port-id range", "begin" and "end" values based on node "id" and the number of nodes in the "node_group".<br>Unique LACP port-id ranges are recommended for EVPN Multihoming designs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.defaults.lacp_port_id_range.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "<node_type_keys.key>.defaults.lacp_port_id_range.size") | Integer |  | `128` |  | Recommended size > = number of ports in the switch. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset</samp>](## "<node_type_keys.key>.defaults.lacp_port_id_range.offset") | Integer |  | `0` |  | Offset is used to avoid overlapping port-id ranges of different switches.<br>Useful when a "connected-endpoint" is connected to switches in different "node_groups".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;always_configure_ip_routing</samp>](## "<node_type_keys.key>.defaults.always_configure_ip_routing") | Boolean |  | `False` |  | Force configuration of "ip routing" even on L2 devices.<br>Use this to retain behavior of AVD versions below 4.0.0.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "<node_type_keys.key>.defaults.raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the root level of the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<node_type_keys.key>.defaults.structured_config") | Dictionary |  |  |  | Custom structured config for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;node_groups</samp>](## "<node_type_keys.key>.node_groups") | List, items: Dictionary |  |  |  | Define variables related to all nodes part of this group. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;group</samp>](## "<node_type_keys.key>.node_groups.[].group") | String | Required, Unique |  |  | The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.<br>The Node Group Name is also used for peer description on downstream switches' uplinks.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.node_groups.[].nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].id") | Integer |  |  |  | Unique identifier used for IP addressing and other algorithms. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;platform</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].platform") | String |  |  |  | Arista platform family. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_address</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mac_address") | String |  |  |  | Leverage to document management interface mac address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;system_mac_address</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].system_mac_address") | String |  |  |  | System MAC Address in this following format: "xx:xx:xx:xx:xx:xx".<br>Set to the same MAC address as available in "show version" on the device.<br>"system_mac_address" can also be set directly as a hostvar.<br>If both are set, the setting under node type settings takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serial_number</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].serial_number") | String |  |  |  | Set to the Serial Number of the device.<br>Only used for documentation purpose in the fabric documentation and part of the structured_config.<br>"serial_number" can also be set directly as a hostvar.<br>If both are set, the setting under node type settings takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].rack") | String |  |  |  | Rack that the switch is located in (only used in snmp_settings location). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mgmt_ip") | String |  |  | Format: cidr | Node management interface IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_mgmt_ip</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].ipv6_mgmt_ip") | String |  |  | Format: cidr | Node management interface IPv6 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_interface</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].mgmt_interface") | String |  |  |  | Management Interface Name.<br>Default -> platform_management_interface -> mgmt_interface -> "Management1".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lacp_port_id_range</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].lacp_port_id_range") | Dictionary |  |  |  | This will generate the "lacp port-id range", "begin" and "end" values based on node "id" and the number of nodes in the "node_group".<br>Unique LACP port-id ranges are recommended for EVPN Multihoming designs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].lacp_port_id_range.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].lacp_port_id_range.size") | Integer |  | `128` |  | Recommended size > = number of ports in the switch. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].lacp_port_id_range.offset") | Integer |  | `0` |  | Offset is used to avoid overlapping port-id ranges of different switches.<br>Useful when a "connected-endpoint" is connected to switches in different "node_groups".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_configure_ip_routing</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].always_configure_ip_routing") | Boolean |  | `False` |  | Force configuration of "ip routing" even on L2 devices.<br>Use this to retain behavior of AVD versions below 4.0.0.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the root level of the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<node_type_keys.key>.node_groups.[].nodes.[].structured_config") | Dictionary |  |  |  | Custom structured config for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "<node_type_keys.key>.node_groups.[].id") | Integer |  |  |  | Unique identifier used for IP addressing and other algorithms. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;platform</samp>](## "<node_type_keys.key>.node_groups.[].platform") | String |  |  |  | Arista platform family. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_address</samp>](## "<node_type_keys.key>.node_groups.[].mac_address") | String |  |  |  | Leverage to document management interface mac address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;system_mac_address</samp>](## "<node_type_keys.key>.node_groups.[].system_mac_address") | String |  |  |  | System MAC Address in this following format: "xx:xx:xx:xx:xx:xx".<br>Set to the same MAC address as available in "show version" on the device.<br>"system_mac_address" can also be set directly as a hostvar.<br>If both are set, the setting under node type settings takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serial_number</samp>](## "<node_type_keys.key>.node_groups.[].serial_number") | String |  |  |  | Set to the Serial Number of the device.<br>Only used for documentation purpose in the fabric documentation and part of the structured_config.<br>"serial_number" can also be set directly as a hostvar.<br>If both are set, the setting under node type settings takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "<node_type_keys.key>.node_groups.[].rack") | String |  |  |  | Rack that the switch is located in (only used in snmp_settings location). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "<node_type_keys.key>.node_groups.[].mgmt_ip") | String |  |  | Format: cidr | Node management interface IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_mgmt_ip</samp>](## "<node_type_keys.key>.node_groups.[].ipv6_mgmt_ip") | String |  |  | Format: cidr | Node management interface IPv6 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_interface</samp>](## "<node_type_keys.key>.node_groups.[].mgmt_interface") | String |  |  |  | Management Interface Name.<br>Default -> platform_management_interface -> mgmt_interface -> "Management1".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lacp_port_id_range</samp>](## "<node_type_keys.key>.node_groups.[].lacp_port_id_range") | Dictionary |  |  |  | This will generate the "lacp port-id range", "begin" and "end" values based on node "id" and the number of nodes in the "node_group".<br>Unique LACP port-id ranges are recommended for EVPN Multihoming designs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.node_groups.[].lacp_port_id_range.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "<node_type_keys.key>.node_groups.[].lacp_port_id_range.size") | Integer |  | `128` |  | Recommended size > = number of ports in the switch. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset</samp>](## "<node_type_keys.key>.node_groups.[].lacp_port_id_range.offset") | Integer |  | `0` |  | Offset is used to avoid overlapping port-id ranges of different switches.<br>Useful when a "connected-endpoint" is connected to switches in different "node_groups".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_configure_ip_routing</samp>](## "<node_type_keys.key>.node_groups.[].always_configure_ip_routing") | Boolean |  | `False` |  | Force configuration of "ip routing" even on L2 devices.<br>Use this to retain behavior of AVD versions below 4.0.0.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "<node_type_keys.key>.node_groups.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the root level of the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<node_type_keys.key>.node_groups.[].structured_config") | Dictionary |  |  |  | Custom structured config for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;nodes</samp>](## "<node_type_keys.key>.nodes") | List, items: Dictionary |  |  |  | Define variables per node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<node_type_keys.key>.nodes.[].name") | String | Required, Unique |  |  | The Node Name is used as "hostname". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "<node_type_keys.key>.nodes.[].id") | Integer |  |  |  | Unique identifier used for IP addressing and other algorithms. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;platform</samp>](## "<node_type_keys.key>.nodes.[].platform") | String |  |  |  | Arista platform family. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mac_address</samp>](## "<node_type_keys.key>.nodes.[].mac_address") | String |  |  |  | Leverage to document management interface mac address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;system_mac_address</samp>](## "<node_type_keys.key>.nodes.[].system_mac_address") | String |  |  |  | System MAC Address in this following format: "xx:xx:xx:xx:xx:xx".<br>Set to the same MAC address as available in "show version" on the device.<br>"system_mac_address" can also be set directly as a hostvar.<br>If both are set, the setting under node type settings takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;serial_number</samp>](## "<node_type_keys.key>.nodes.[].serial_number") | String |  |  |  | Set to the Serial Number of the device.<br>Only used for documentation purpose in the fabric documentation and part of the structured_config.<br>"serial_number" can also be set directly as a hostvar.<br>If both are set, the setting under node type settings takes precedence.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rack</samp>](## "<node_type_keys.key>.nodes.[].rack") | String |  |  |  | Rack that the switch is located in (only used in snmp_settings location). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_ip</samp>](## "<node_type_keys.key>.nodes.[].mgmt_ip") | String |  |  | Format: cidr | Node management interface IPv4 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_mgmt_ip</samp>](## "<node_type_keys.key>.nodes.[].ipv6_mgmt_ip") | String |  |  | Format: cidr | Node management interface IPv6 address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mgmt_interface</samp>](## "<node_type_keys.key>.nodes.[].mgmt_interface") | String |  |  |  | Management Interface Name.<br>Default -> platform_management_interface -> mgmt_interface -> "Management1".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lacp_port_id_range</samp>](## "<node_type_keys.key>.nodes.[].lacp_port_id_range") | Dictionary |  |  |  | This will generate the "lacp port-id range", "begin" and "end" values based on node "id" and the number of nodes in the "node_group".<br>Unique LACP port-id ranges are recommended for EVPN Multihoming designs.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<node_type_keys.key>.nodes.[].lacp_port_id_range.enabled") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;size</samp>](## "<node_type_keys.key>.nodes.[].lacp_port_id_range.size") | Integer |  | `128` |  | Recommended size > = number of ports in the switch. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset</samp>](## "<node_type_keys.key>.nodes.[].lacp_port_id_range.offset") | Integer |  | `0` |  | Offset is used to avoid overlapping port-id ranges of different switches.<br>Useful when a "connected-endpoint" is connected to switches in different "node_groups".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;always_configure_ip_routing</samp>](## "<node_type_keys.key>.nodes.[].always_configure_ip_routing") | Boolean |  | `False` |  | Force configuration of "ip routing" even on L2 devices.<br>Use this to retain behavior of AVD versions below 4.0.0.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "<node_type_keys.key>.nodes.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the root level of the final EOS configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<node_type_keys.key>.nodes.[].structured_config") | Dictionary |  |  |  | Custom structured config for eos_cli_config_gen. |

=== "YAML"

    ```yaml
    <node_type_keys.key>:

      # Define variables for all nodes of this type.
      defaults:

        # Unique identifier used for IP addressing and other algorithms.
        id: <int>

        # Arista platform family.
        platform: <str>

        # Leverage to document management interface mac address.
        mac_address: <str>

        # System MAC Address in this following format: "xx:xx:xx:xx:xx:xx".
        # Set to the same MAC address as available in "show version" on the device.
        # "system_mac_address" can also be set directly as a hostvar.
        # If both are set, the setting under node type settings takes precedence.
        system_mac_address: <str>

        # Set to the Serial Number of the device.
        # Only used for documentation purpose in the fabric documentation and part of the structured_config.
        # "serial_number" can also be set directly as a hostvar.
        # If both are set, the setting under node type settings takes precedence.
        serial_number: <str>

        # Rack that the switch is located in (only used in snmp_settings location).
        rack: <str>

        # Node management interface IPv4 address.
        mgmt_ip: <str>

        # Node management interface IPv6 address.
        ipv6_mgmt_ip: <str>

        # Management Interface Name.
        # Default -> platform_management_interface -> mgmt_interface -> "Management1".
        mgmt_interface: <str>

        # This will generate the "lacp port-id range", "begin" and "end" values based on node "id" and the number of nodes in the "node_group".
        # Unique LACP port-id ranges are recommended for EVPN Multihoming designs.
        lacp_port_id_range:
          enabled: <bool; default=False>

          # Recommended size > = number of ports in the switch.
          size: <int; default=128>

          # Offset is used to avoid overlapping port-id ranges of different switches.
          # Useful when a "connected-endpoint" is connected to switches in different "node_groups".
          offset: <int; default=0>

        # Force configuration of "ip routing" even on L2 devices.
        # Use this to retain behavior of AVD versions below 4.0.0.
        always_configure_ip_routing: <bool; default=False>

        # EOS CLI rendered directly on the root level of the final EOS configuration.
        raw_eos_cli: <str>

        # Custom structured config for eos_cli_config_gen.
        structured_config: <dict>

      # Define variables related to all nodes part of this group.
      node_groups:

          # The Node Group Name is used for MLAG domain unless set with 'mlag_domain_id'.
          # The Node Group Name is also used for peer description on downstream switches' uplinks.
        - group: <str; required; unique>

          # Define variables per node.
          nodes:

              # The Node Name is used as "hostname".
            - name: <str; required; unique>

              # Unique identifier used for IP addressing and other algorithms.
              id: <int>

              # Arista platform family.
              platform: <str>

              # Leverage to document management interface mac address.
              mac_address: <str>

              # System MAC Address in this following format: "xx:xx:xx:xx:xx:xx".
              # Set to the same MAC address as available in "show version" on the device.
              # "system_mac_address" can also be set directly as a hostvar.
              # If both are set, the setting under node type settings takes precedence.
              system_mac_address: <str>

              # Set to the Serial Number of the device.
              # Only used for documentation purpose in the fabric documentation and part of the structured_config.
              # "serial_number" can also be set directly as a hostvar.
              # If both are set, the setting under node type settings takes precedence.
              serial_number: <str>

              # Rack that the switch is located in (only used in snmp_settings location).
              rack: <str>

              # Node management interface IPv4 address.
              mgmt_ip: <str>

              # Node management interface IPv6 address.
              ipv6_mgmt_ip: <str>

              # Management Interface Name.
              # Default -> platform_management_interface -> mgmt_interface -> "Management1".
              mgmt_interface: <str>

              # This will generate the "lacp port-id range", "begin" and "end" values based on node "id" and the number of nodes in the "node_group".
              # Unique LACP port-id ranges are recommended for EVPN Multihoming designs.
              lacp_port_id_range:
                enabled: <bool; default=False>

                # Recommended size > = number of ports in the switch.
                size: <int; default=128>

                # Offset is used to avoid overlapping port-id ranges of different switches.
                # Useful when a "connected-endpoint" is connected to switches in different "node_groups".
                offset: <int; default=0>

              # Force configuration of "ip routing" even on L2 devices.
              # Use this to retain behavior of AVD versions below 4.0.0.
              always_configure_ip_routing: <bool; default=False>

              # EOS CLI rendered directly on the root level of the final EOS configuration.
              raw_eos_cli: <str>

              # Custom structured config for eos_cli_config_gen.
              structured_config: <dict>

          # Unique identifier used for IP addressing and other algorithms.
          id: <int>

          # Arista platform family.
          platform: <str>

          # Leverage to document management interface mac address.
          mac_address: <str>

          # System MAC Address in this following format: "xx:xx:xx:xx:xx:xx".
          # Set to the same MAC address as available in "show version" on the device.
          # "system_mac_address" can also be set directly as a hostvar.
          # If both are set, the setting under node type settings takes precedence.
          system_mac_address: <str>

          # Set to the Serial Number of the device.
          # Only used for documentation purpose in the fabric documentation and part of the structured_config.
          # "serial_number" can also be set directly as a hostvar.
          # If both are set, the setting under node type settings takes precedence.
          serial_number: <str>

          # Rack that the switch is located in (only used in snmp_settings location).
          rack: <str>

          # Node management interface IPv4 address.
          mgmt_ip: <str>

          # Node management interface IPv6 address.
          ipv6_mgmt_ip: <str>

          # Management Interface Name.
          # Default -> platform_management_interface -> mgmt_interface -> "Management1".
          mgmt_interface: <str>

          # This will generate the "lacp port-id range", "begin" and "end" values based on node "id" and the number of nodes in the "node_group".
          # Unique LACP port-id ranges are recommended for EVPN Multihoming designs.
          lacp_port_id_range:
            enabled: <bool; default=False>

            # Recommended size > = number of ports in the switch.
            size: <int; default=128>

            # Offset is used to avoid overlapping port-id ranges of different switches.
            # Useful when a "connected-endpoint" is connected to switches in different "node_groups".
            offset: <int; default=0>

          # Force configuration of "ip routing" even on L2 devices.
          # Use this to retain behavior of AVD versions below 4.0.0.
          always_configure_ip_routing: <bool; default=False>

          # EOS CLI rendered directly on the root level of the final EOS configuration.
          raw_eos_cli: <str>

          # Custom structured config for eos_cli_config_gen.
          structured_config: <dict>

      # Define variables per node.
      nodes:

          # The Node Name is used as "hostname".
        - name: <str; required; unique>

          # Unique identifier used for IP addressing and other algorithms.
          id: <int>

          # Arista platform family.
          platform: <str>

          # Leverage to document management interface mac address.
          mac_address: <str>

          # System MAC Address in this following format: "xx:xx:xx:xx:xx:xx".
          # Set to the same MAC address as available in "show version" on the device.
          # "system_mac_address" can also be set directly as a hostvar.
          # If both are set, the setting under node type settings takes precedence.
          system_mac_address: <str>

          # Set to the Serial Number of the device.
          # Only used for documentation purpose in the fabric documentation and part of the structured_config.
          # "serial_number" can also be set directly as a hostvar.
          # If both are set, the setting under node type settings takes precedence.
          serial_number: <str>

          # Rack that the switch is located in (only used in snmp_settings location).
          rack: <str>

          # Node management interface IPv4 address.
          mgmt_ip: <str>

          # Node management interface IPv6 address.
          ipv6_mgmt_ip: <str>

          # Management Interface Name.
          # Default -> platform_management_interface -> mgmt_interface -> "Management1".
          mgmt_interface: <str>

          # This will generate the "lacp port-id range", "begin" and "end" values based on node "id" and the number of nodes in the "node_group".
          # Unique LACP port-id ranges are recommended for EVPN Multihoming designs.
          lacp_port_id_range:
            enabled: <bool; default=False>

            # Recommended size > = number of ports in the switch.
            size: <int; default=128>

            # Offset is used to avoid overlapping port-id ranges of different switches.
            # Useful when a "connected-endpoint" is connected to switches in different "node_groups".
            offset: <int; default=0>

          # Force configuration of "ip routing" even on L2 devices.
          # Use this to retain behavior of AVD versions below 4.0.0.
          always_configure_ip_routing: <bool; default=False>

          # EOS CLI rendered directly on the root level of the final EOS configuration.
          raw_eos_cli: <str>

          # Custom structured config for eos_cli_config_gen.
          structured_config: <dict>
    ```
