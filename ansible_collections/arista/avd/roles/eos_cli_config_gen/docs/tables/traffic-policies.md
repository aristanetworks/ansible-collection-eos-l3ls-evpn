<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>traffic_policies</samp>](## "traffic_policies") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;options</samp>](## "traffic_policies.options") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counter_per_interface</samp>](## "traffic_policies.options.counter_per_interface") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;field_sets</samp>](## "traffic_policies.field_sets") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "traffic_policies.field_sets.ipv4") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "traffic_policies.field_sets.ipv4.[].name") | String | Required, Unique |  |  | IPv4 Prefix Field Set Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefixes</samp>](## "traffic_policies.field_sets.ipv4.[].prefixes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "traffic_policies.field_sets.ipv4.[].prefixes.[]") | String |  |  |  | IPv4 Prefix. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "traffic_policies.field_sets.ipv6") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "traffic_policies.field_sets.ipv6.[].name") | String | Required, Unique |  |  | IPv6 Prefix Field Set Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefixes</samp>](## "traffic_policies.field_sets.ipv6.[].prefixes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "traffic_policies.field_sets.ipv6.[].prefixes.[]") | String |  |  |  | IPv6 Prefix. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ports</samp>](## "traffic_policies.field_sets.ports") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "traffic_policies.field_sets.ports.[].name") | String | Required, Unique |  |  | L4 Port Field Set Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_range</samp>](## "traffic_policies.field_sets.ports.[].port_range") | String |  |  |  | Example: '10,20,80,440-450' |
    | [<samp>&nbsp;&nbsp;policies</samp>](## "traffic_policies.policies") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "traffic_policies.policies.[].name") | String | Required, Unique |  |  | Traffic Policy Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;matches</samp>](## "traffic_policies.policies.[].matches") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "traffic_policies.policies.[].matches.[].name") | String | Required, Unique |  |  | Traffic Policy Item. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "traffic_policies.policies.[].matches.[].type") | String | Required |  | Valid Values:<br>- <code>ipv4</code><br>- <code>ipv6</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "traffic_policies.policies.[].matches.[].source") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefixes</samp>](## "traffic_policies.policies.[].matches.[].source.prefixes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "traffic_policies.policies.[].matches.[].source.prefixes.[]") | String |  |  |  | IP address or prefix. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_lists</samp>](## "traffic_policies.policies.[].matches.[].source.prefix_lists") | List, items: String |  |  |  | Field-set prefix lists. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "traffic_policies.policies.[].matches.[].source.prefix_lists.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "traffic_policies.policies.[].matches.[].destination") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefixes</samp>](## "traffic_policies.policies.[].matches.[].destination.prefixes") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "traffic_policies.policies.[].matches.[].destination.prefixes.[]") | String |  |  |  | IP address or prefix. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_lists</samp>](## "traffic_policies.policies.[].matches.[].destination.prefix_lists") | List, items: String |  |  |  | Field-set prefix lists. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "traffic_policies.policies.[].matches.[].destination.prefix_lists.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp>](## "traffic_policies.policies.[].matches.[].ttl") | String |  |  |  | TTL range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fragment</samp>](## "traffic_policies.policies.[].matches.[].fragment") | Dictionary |  |  |  | The 'fragment' command is not supported when 'source port'<br>or 'destination port' command is configured.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;offset</samp>](## "traffic_policies.policies.[].matches.[].fragment.offset") | String |  |  |  | Fragment offset range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocols</samp>](## "traffic_policies.policies.[].matches.[].protocols") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;protocol</samp>](## "traffic_policies.policies.[].matches.[].protocols.[].protocol") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;src_port</samp>](## "traffic_policies.policies.[].matches.[].protocols.[].src_port") | String |  |  |  | Port range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dst_port</samp>](## "traffic_policies.policies.[].matches.[].protocols.[].dst_port") | String |  |  |  | Port range. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;src_field</samp>](## "traffic_policies.policies.[].matches.[].protocols.[].src_field") | String |  |  |  | L4 port range field set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dst_field</samp>](## "traffic_policies.policies.[].matches.[].protocols.[].dst_field") | String |  |  |  | L4 port range field set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flags</samp>](## "traffic_policies.policies.[].matches.[].protocols.[].flags") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "traffic_policies.policies.[].matches.[].protocols.[].flags.[]") | String |  |  | Valid Values:<br>- <code>established</code><br>- <code>initial</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;icmp_type</samp>](## "traffic_policies.policies.[].matches.[].protocols.[].icmp_type") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "traffic_policies.policies.[].matches.[].protocols.[].icmp_type.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enforce_gtsm</samp>](## "traffic_policies.policies.[].matches.[].protocols.[].enforce_gtsm") | Boolean |  |  |  | Enforce the GTSM for BGP speakers. Only supported when protocol is set to 'neighbors'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;actions</samp>](## "traffic_policies.policies.[].matches.[].actions") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "traffic_policies.policies.[].matches.[].actions.dscp") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp>](## "traffic_policies.policies.[].matches.[].actions.traffic_class") | Integer |  |  |  | Traffic class ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;count</samp>](## "traffic_policies.policies.[].matches.[].actions.count") | String |  |  |  | Counter name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "traffic_policies.policies.[].matches.[].actions.drop") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;log</samp>](## "traffic_policies.policies.[].matches.[].actions.log") | Boolean |  |  |  | Only supported when action is set to drop. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_actions</samp>](## "traffic_policies.policies.[].default_actions") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "traffic_policies.policies.[].default_actions.ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "traffic_policies.policies.[].default_actions.ipv4.dscp") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp>](## "traffic_policies.policies.[].default_actions.ipv4.traffic_class") | Integer |  |  |  | Traffic class ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;count</samp>](## "traffic_policies.policies.[].default_actions.ipv4.count") | String |  |  |  | Counter name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "traffic_policies.policies.[].default_actions.ipv4.drop") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;log</samp>](## "traffic_policies.policies.[].default_actions.ipv4.log") | Boolean |  |  |  | Only supported when action is set to drop. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6</samp>](## "traffic_policies.policies.[].default_actions.ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "traffic_policies.policies.[].default_actions.ipv6.dscp") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_class</samp>](## "traffic_policies.policies.[].default_actions.ipv6.traffic_class") | Integer |  |  |  | Traffic class ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;count</samp>](## "traffic_policies.policies.[].default_actions.ipv6.count") | String |  |  |  | Counter name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;drop</samp>](## "traffic_policies.policies.[].default_actions.ipv6.drop") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;log</samp>](## "traffic_policies.policies.[].default_actions.ipv6.log") | Boolean |  |  |  | Only supported when action is set to drop. |

=== "YAML"

    ```yaml
    traffic_policies:
      options:
        counter_per_interface: <bool>
      field_sets:
        ipv4:

            # IPv4 Prefix Field Set Name.
          - name: <str; required; unique>
            prefixes:

                # IPv4 Prefix.
              - <str>
        ipv6:

            # IPv6 Prefix Field Set Name.
          - name: <str; required; unique>
            prefixes:

                # IPv6 Prefix.
              - <str>
        ports:

            # L4 Port Field Set Name.
          - name: <str; required; unique>

            # Example: '10,20,80,440-450'
            port_range: <str>
      policies:

          # Traffic Policy Name.
        - name: <str; required; unique>
          matches:

              # Traffic Policy Item.
            - name: <str; required; unique>
              type: <str; "ipv4" | "ipv6"; required>
              source:
                prefixes:

                    # IP address or prefix.
                  - <str>

                # Field-set prefix lists.
                prefix_lists:
                  - <str>
              destination:
                prefixes:

                    # IP address or prefix.
                  - <str>

                # Field-set prefix lists.
                prefix_lists:
                  - <str>

              # TTL range.
              ttl: <str>

              # The 'fragment' command is not supported when 'source port'
              # or 'destination port' command is configured.
              fragment:

                # Fragment offset range.
                offset: <str>
              protocols:
                - protocol: <str; required; unique>

                  # Port range.
                  src_port: <str>

                  # Port range.
                  dst_port: <str>

                  # L4 port range field set.
                  src_field: <str>

                  # L4 port range field set.
                  dst_field: <str>
                  flags:
                    - <str; "established" | "initial">
                  icmp_type:
                    - <str>

                  # Enforce the GTSM for BGP speakers. Only supported when protocol is set to 'neighbors'.
                  enforce_gtsm: <bool>
              actions:
                dscp: <int>

                # Traffic class ID.
                traffic_class: <int>

                # Counter name.
                count: <str>
                drop: <bool>

                # Only supported when action is set to drop.
                log: <bool>
          default_actions:
            ipv4:
              dscp: <int>

              # Traffic class ID.
              traffic_class: <int>

              # Counter name.
              count: <str>
              drop: <bool>

              # Only supported when action is set to drop.
              log: <bool>
            ipv6:
              dscp: <int>

              # Traffic class ID.
              traffic_class: <int>

              # Counter name.
              count: <str>
              drop: <bool>

              # Only supported when action is set to drop.
              log: <bool>
    ```
