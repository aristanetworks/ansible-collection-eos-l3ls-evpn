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
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "<network_services_keys.name>.[].vrfs") | List, items: Dictionary |  |  |  | VRFs will only be configured on a node if any of the underlying objects like `svis` or `l3_interfaces` apply to the node.<br><br>It is recommended to only define a VRF in one Tenant. If the same VRF name is used across multiple tenants and those tenants<br>are accepted by `filter.tenants` on the node, any object set under the duplicate VRFs must either be unique or be an exact match.<br><br>VRF "default" is partially supported under network-services. Currently the supported options for "default" vrf are route-target,<br>route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.<br>Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "<network_services_keys.name>.[].vrfs.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l3_interfaces</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces") | List, items: Dictionary |  |  |  | List of L3 interfaces.<br>This will create IP routed interface inside VRF. Length of interfaces, nodes and ip_addresses must match.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;interfaces</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].interfaces") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].interfaces.[]") | String |  |  |  | Interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encapsulation_dot1q_vlan</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].encapsulation_dot1q_vlan") | List, items: Integer |  |  |  | For sub-interfaces the dot1q vlan is derived from the interface name by default, but can also be specified. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;int&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].encapsulation_dot1q_vlan.[]") | Integer |  |  | Min: 1<br>Max: 4094 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_addresses</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ip_addresses") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ip_addresses.[]") | String |  |  |  | IPv4_address/Mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nodes</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].nodes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].nodes.[]") | String |  |  |  | Node. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;descriptions</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].descriptions") | List, items: String |  |  |  | "descriptions" has precedence over "description".<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].descriptions.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mtu</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].mtu") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_in</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ipv4_acl_in") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_acl_out</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ipv4_acl_out") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ospf</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf") | Dictionary |  |  |  | OSPF interface configuration. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;point_to_point</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf.point_to_point") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;area</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf.area") | String |  | `0.0.0.0` |  | OSPF area ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cost</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf.cost") | Integer |  |  |  | OSPF link cost. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf.authentication") | String |  |  | Valid Values:<br>- <code>simple</code><br>- <code>message-digest</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;simple_auth_key</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf.simple_auth_key") | String |  |  |  | Password used with simple authentication. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;message_digest_keys</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf.message_digest_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf.message_digest_keys.[].id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf.message_digest_keys.[].hash_algorithm") | String |  | `sha512` | Valid Values:<br>- <code>md5</code><br>- <code>sha1</code><br>- <code>sha256</code><br>- <code>sha384</code><br>- <code>sha512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].ospf.message_digest_keys.[].key") | String |  |  |  | Key password. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pim</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].pim") | Dictionary |  |  |  | Enable PIM sparse-mode on the interface; requires "evpn_l3_multicast" to be enabled on the VRF/Tenant.<br>Enabling this implicitly makes the device a PIM External Gateway (PEG) in EVPN designs only.<br>At least one RP address must be configured for EVPN PEG to be configured.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].pim.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flow_tracking</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].flow_tracking") | Dictionary |  |  |  | Configures flow-tracking on the interface. Overrides `fabric_flow_tracking.l3_interfaces` setting. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].flow_tracking.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].flow_tracking.name") | String |  |  |  | Flow tracker name as defined in flow_tracking_settings. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;structured_config</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].structured_config") | Dictionary |  |  |  | Custom structured config added under ethernet_interfaces.[name=<interface>] for eos_cli_config_gen. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;raw_eos_cli</samp>](## "<network_services_keys.name>.[].vrfs.[].l3_interfaces.[].raw_eos_cli") | String |  |  |  | EOS CLI rendered directly on the Ethernet interface in the final EOS configuration.<br> |

=== "YAML"

    ```yaml
    <network_services_keys.name>:

        # Specify a tenant name.
        # Tenant provide a construct to group L3 VRFs and L2 VLANs.
        # Networks services can be filtered by tenant name.
      - name: <str; required; unique>

        # VRFs will only be configured on a node if any of the underlying objects like `svis` or `l3_interfaces` apply to the node.
        #
        # It is recommended to only define a VRF in one Tenant. If the same VRF name is used across multiple tenants and those tenants
        # are accepted by `filter.tenants` on the node, any object set under the duplicate VRFs must either be unique or be an exact match.
        #
        # VRF "default" is partially supported under network-services. Currently the supported options for "default" vrf are route-target,
        # route-distinguisher settings, structured_config, raw_eos_cli in bgp and SVIs are the only supported interface type.
        # Vlan-aware-bundles are supported as well inside default vrf. OSPF is not supported currently.
        vrfs:
          - name: <str; required; unique>

            # List of L3 interfaces.
            # This will create IP routed interface inside VRF. Length of interfaces, nodes and ip_addresses must match.
            l3_interfaces:
              - interfaces:

                    # Interface name.
                  - <str>

                # For sub-interfaces the dot1q vlan is derived from the interface name by default, but can also be specified.
                encapsulation_dot1q_vlan:
                  - <int; 1-4094>
                ip_addresses:

                    # IPv4_address/Mask.
                  - <str>
                nodes:

                    # Node.
                  - <str>
                description: <str>

                # "descriptions" has precedence over "description".
                descriptions:
                  - <str>
                enabled: <bool; default=True>
                mtu: <int>
                ipv4_acl_in: <str>
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

                # Enable PIM sparse-mode on the interface; requires "evpn_l3_multicast" to be enabled on the VRF/Tenant.
                # Enabling this implicitly makes the device a PIM External Gateway (PEG) in EVPN designs only.
                # At least one RP address must be configured for EVPN PEG to be configured.
                pim:
                  enabled: <bool>

                # Configures flow-tracking on the interface. Overrides `fabric_flow_tracking.l3_interfaces` setting.
                flow_tracking:
                  enabled: <bool>

                  # Flow tracker name as defined in flow_tracking_settings.
                  name: <str>

                # Custom structured config added under ethernet_interfaces.[name=<interface>] for eos_cli_config_gen.
                structured_config: <dict>

                # EOS CLI rendered directly on the Ethernet interface in the final EOS configuration.
                raw_eos_cli: <str>
    ```
