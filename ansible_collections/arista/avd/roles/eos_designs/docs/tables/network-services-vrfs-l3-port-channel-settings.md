<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>&lt;network_services_keys.name&gt;</samp>](## "<network_services_keys.name>") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "<network_services_keys.name>.[].name") | String | Required, Unique |  |  | Specify a tenant name.<br>Tenant provide a construct to group L3 VRFs and L2 VLANs.<br>Networks services can be filtered by tenant name.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "<network_services_keys.name>.[].vrfs") | List, items: Dictionary |  |  |  | VRFs will only be configured on a node if any of the underlying objects like `svis`, `l3_interfaces` or `l3_port_channels` apply to the node.<br><br>It is recommended to only define a VRF in one Tenant. If the same VRF name is used across multiple tenants and those tenants<br>are accepted by `filter.tenants` on the node, any object set under the duplicate VRFs must either be unique or be an exact match.<br><br>VRF "default" is partially supported under network-services. Currently the supported options for "default" vrf are route-target,<br>route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.<br>Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<network_services_keys.name>.[].vrfs.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l3_port_channels</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].name") | String | Required, Unique |  | Pattern: `Port-Channel[\d/]+(\.[\d]+)?` | Port-Channel interface name like 'Port-Channel2' or subinterface name like 'Port-Channel2.42'.<br>For a Port-Channel subinterface, the parent Port-Channel interface must be defined as well. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].nodes") | List, items: String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].nodes.[]") | String |  |  |  | Node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].description") | String |  |  |  | Interface description.<br>If not set, a default description will be configured with '[<peer>[ <peer_port_channel>]]'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;descriptions</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].descriptions") | List, items: String |  |  |  | "descriptions" has precedence over "description".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].descriptions.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].mode") | String |  | `active` | Valid Values:<br>- <code>active</code><br>- <code>passive</code><br>- <code>on</code> | Port-Channel mode.<br>Should not be set on Port-Channel subinterfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;member_interfaces</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].member_interfaces") | List, items: Dictionary |  |  |  | Port-Channel member interfaces.<br>Should not be set on Port-Channel subinterfaces. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].member_interfaces.[].name") | String | Required, Unique |  | Pattern: `Ethernet[\d/]+` | Ethernet interface name like 'Ethernet2'.<br>Member interface cannot be subinterface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].member_interfaces.[].description") | String |  |  |  | Interface description for this member.<br>If not set, a default description will be configured with '[<peer>[ <peer_interface>]]'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].member_interfaces.[].peer") | String |  |  |  | The peer device name. Used for description and documentation.<br>If not set, this inherits the peer setting on the port-channel interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_interface</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].member_interfaces.[].peer_interface") | String |  |  |  | The peer device interface. Used for description and documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;speed</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].member_interfaces.[].speed") | String |  |  |  | Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].member_interfaces.[].structured_config") | Dictionary |  |  |  | Custom structured config for the member ethernet interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].ip_address") | String |  |  |  | IPv4 address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_addresses</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].ip_addresses") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].ip_addresses.[]") | String |  |  |  | IPv4_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].encapsulation_dot1q_vlan") | Integer |  |  | Min: 1<br>Max: 4094 | For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].enabled") | Boolean |  | `True` |  | Enable or Shutdown the interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].peer") | String |  |  |  | The peer device name. Used for description and documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;peer_port_channel</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].peer_port_channel") | String |  |  |  | The peer device port-channel interface. Used for description and documentation. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].mtu") | Integer |  |  |  | MTU can only be set on the parent Port-Channel. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_in</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].ipv4_acl_in") | String |  |  |  | Name of the IPv4 access-list to be assigned in the ingress direction. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_out</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].ipv4_acl_out") | String |  |  |  | Name of the IPv4 Access-list to be assigned in the egress direction. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].ospf") | Dictionary |  |  |  | OSPF interface configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].ospf.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].ospf.point_to_point") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].ospf.area") | String |  | `0.0.0.0` |  | OSPF area ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cost</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].ospf.cost") | Integer |  |  |  | OSPF link cost. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].ospf.authentication") | String |  |  | Valid Values:<br>- <code>simple</code><br>- <code>message-digest</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;simple_auth_key</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].ospf.simple_auth_key") | String |  |  |  | Password used with simple authentication. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;message_digest_keys</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].ospf.message_digest_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].ospf.message_digest_keys.[].id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].ospf.message_digest_keys.[].hash_algorithm") | String |  | `sha512` | Valid Values:<br>- <code>md5</code><br>- <code>sha1</code><br>- <code>sha256</code><br>- <code>sha384</code><br>- <code>sha512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].ospf.message_digest_keys.[].key") | String |  |  |  | Key password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flow_tracking</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].flow_tracking") | Dictionary |  |  |  | Configures flow-tracking on the interface. Overrides `fabric_flow_tracking.l3_port_channels` setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].flow_tracking.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].flow_tracking.name") | String |  |  |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].structured_config") | Dictionary |  |  |  | Custom structured config added under port_channel_interfaces.[name=<interface>] for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_port_channels.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the Port-Channel interface in the final EOS configuration.<br> |

=== "YAML"

    ```yaml
    <network_services_keys.name>:

        # Specify a tenant name.
        # Tenant provide a construct to group L3 VRFs and L2 VLANs.
        # Networks services can be filtered by tenant name.
      - name: <str; required; unique>

        # VRFs will only be configured on a node if any of the underlying objects like `svis`, `l3_interfaces` or `l3_port_channels` apply to the node.
        #
        # It is recommended to only define a VRF in one Tenant. If the same VRF name is used across multiple tenants and those tenants
        # are accepted by `filter.tenants` on the node, any object set under the duplicate VRFs must either be unique or be an exact match.
        #
        # VRF "default" is partially supported under network-services. Currently the supported options for "default" vrf are route-target,
        # route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.
        # Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.
        vrfs:
          - name: <str; required; unique>
            l3_port_channels:

                # Port-Channel interface name like 'Port-Channel2' or subinterface name like 'Port-Channel2.42'.
                # For a Port-Channel subinterface, the parent Port-Channel interface must be defined as well.
              - name: <str; required; unique>
                nodes: # required

                    # Node.
                  - <str>

                # Interface description.
                # If not set, a default description will be configured with '[<peer>[ <peer_port_channel>]]'.
                description: <str>

                # "descriptions" has precedence over "description".
                descriptions:
                  - <str>

                # Port-Channel mode.
                # Should not be set on Port-Channel subinterfaces.
                mode: <str; "active" | "passive" | "on"; default="active">

                # Port-Channel member interfaces.
                # Should not be set on Port-Channel subinterfaces.
                member_interfaces:

                    # Ethernet interface name like 'Ethernet2'.
                    # Member interface cannot be subinterface.
                  - name: <str; required; unique>

                    # Interface description for this member.
                    # If not set, a default description will be configured with '[<peer>[ <peer_interface>]]'.
                    description: <str>

                    # The peer device name. Used for description and documentation.
                    # If not set, this inherits the peer setting on the port-channel interface.
                    peer: <str>

                    # The peer device interface. Used for description and documentation.
                    peer_interface: <str>

                    # Speed should be set in the format `<interface_speed>` or `forced <interface_speed>` or `auto <interface_speed>`.
                    speed: <str>

                    # Custom structured config for the member ethernet interface.
                    structured_config: <dict>

                # IPv4 address/Mask.
                ip_address: <str>
                ip_addresses:

                    # IPv4_address/Mask.
                  - <str>

                # For subinterfaces the dot1q vlan is derived from the interface name by default, but can also be specified.
                encapsulation_dot1q_vlan: <int; 1-4094>

                # Enable or Shutdown the interface.
                enabled: <bool; default=True>

                # The peer device name. Used for description and documentation.
                peer: <str>

                # The peer device port-channel interface. Used for description and documentation.
                peer_port_channel: <str>

                # MTU can only be set on the parent Port-Channel.
                mtu: <int>

                # Name of the IPv4 access-list to be assigned in the ingress direction.
                ipv4_acl_in: <str>

                # Name of the IPv4 Access-list to be assigned in the egress direction.
                ipv4_acl_out: <str>

                # OSPF interface configuration.
                ospf:
                  enabled: <bool>
                  point_to_point: <bool; default=False>

                  # OSPF area ID.
                  area: <str; default="0.0.0.0">

                  # OSPF link cost.
                  cost: <int>
                  authentication: <str; "simple" | "message-digest">

                  # Password used with simple authentication.
                  simple_auth_key: <str>
                  message_digest_keys:
                    - id: <int>
                      hash_algorithm: <str; "md5" | "sha1" | "sha256" | "sha384" | "sha512"; default="sha512">

                      # Key password.
                      key: <str>

                # Configures flow-tracking on the interface. Overrides `fabric_flow_tracking.l3_port_channels` setting.
                flow_tracking:
                  enabled: <bool>

                  # Flow tracker name as defined in flow_tracking_settings.
                  name: <str>

                # Custom structured config added under port_channel_interfaces.[name=<interface>] for eos_cli_config_gen.
                structured_config: <dict>

                # EOS CLI rendered directly on the Port-Channel interface in the final EOS configuration.
                raw_eos_cli: <str>
    ```
