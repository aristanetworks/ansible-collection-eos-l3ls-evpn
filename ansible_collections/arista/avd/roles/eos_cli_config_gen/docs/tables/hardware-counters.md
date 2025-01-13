<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>hardware_counters</samp>](## "hardware_counters") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;features</samp>](## "hardware_counters.features") | List, items: Dictionary |  |  |  | This data model allows to configure the list of hardware counters feature<br>available on Arista platforms.<br><br>The `name` key accepts a list of valid_values which MUST be updated to support<br>new feature as they are released in EOS.<br><br>The available values of the different keys like 'direction' or 'address_type'<br>are feature and hardware dependent and this model DOES NOT validate that the<br>combinations are valid. It is the responsibility of the user of this data model<br>to make sure that the rendered CLI is accepted by the targeted device.<br><br>Examples:<br><br>  * Use:<br>    ```yaml<br>    hardware_counters:<br>      features:<br>        - name: ip<br>          direction: out<br>          layer3: true<br>          units_packets: true<br>    ```<br><br>    to render:<br>    ```eos<br>    hardware counter feature ip out layer3 units packets<br>    ```<br>  * Use:<br>    ```yaml<br>    hardware_counters:<br>      features:<br>        - name: route<br>          address_type: ipv4<br>          vrf: test<br>          prefix: 192.168.0.0/24<br>    ```<br><br>    to render:<br>    ```eos<br>    hardware counter feature route ipv4 vrf test 192.168.0.0/24<br>    ```<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "hardware_counters.features.[].name") | String | Required |  | Valid Values:<br>- <code>acl</code><br>- <code>decap-group</code><br>- <code>directflow</code><br>- <code>ecn</code><br>- <code>flow-spec</code><br>- <code>gre tunnel interface</code><br>- <code>ip</code><br>- <code>mpls interface</code><br>- <code>mpls lfib</code><br>- <code>mpls tunnel</code><br>- <code>multicast</code><br>- <code>nexthop</code><br>- <code>pbr</code><br>- <code>pdp</code><br>- <code>policing interface</code><br>- <code>qos</code><br>- <code>qos dual-rate-policer</code><br>- <code>route</code><br>- <code>routed-port</code><br>- <code>segment-security</code><br>- <code>subinterface</code><br>- <code>tapagg</code><br>- <code>traffic-class</code><br>- <code>traffic-policy</code><br>- <code>vlan</code><br>- <code>vlan-interface</code><br>- <code>vni decap</code><br>- <code>vni encap</code><br>- <code>vtep decap</code><br>- <code>vtep encap</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;direction</samp>](## "hardware_counters.features.[].direction") | String |  |  | Valid Values:<br>- <code>in</code><br>- <code>out</code><br>- <code>cpu</code> | Most features support only 'in' and 'out'. Some like traffic-policy support 'cpu'.<br>Some features DO NOT have any direction.<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address_type</samp>](## "hardware_counters.features.[].address_type") | String |  |  | Valid Values:<br>- <code>ipv4</code><br>- <code>ipv6</code><br>- <code>mac</code> | Supported only for the following features:<br>- acl: [ipv4, ipv6, mac] if direction is 'out'<br>- multicast: [ipv4, ipv6]<br>- route: [ipv4, ipv6]<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;layer3</samp>](## "hardware_counters.features.[].layer3") | Boolean |  |  |  | Supported only for the 'ip' feature.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "hardware_counters.features.[].vrf") | String |  |  |  | Supported only for the 'route' feature.<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix</samp>](## "hardware_counters.features.[].prefix") | String |  |  |  | Supported only for the 'route' feature.<br>Mandatory for the 'route' feature.<br>This validation IS NOT made by the schemas.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;units_packets</samp>](## "hardware_counters.features.[].units_packets") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
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
    ```
