<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>application_traffic_recognition</samp>](## "application_traffic_recognition") | Dictionary |  |  |  | Application traffic recognition configuration. |
    | [<samp>&nbsp;&nbsp;categories</samp>](## "application_traffic_recognition.categories") | List, items: Dictionary |  |  |  | List of categories. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.categories.[].name") | String | Required, Unique |  |  | Category name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;applications</samp>](## "application_traffic_recognition.categories.[].applications") | List, items: Dictionary |  |  |  | List of applications. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.categories.[].applications.[].name") | String |  |  |  | Application name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;service</samp>](## "application_traffic_recognition.categories.[].applications.[].service") | String |  |  | Valid Values:<br>- <code>audio-video</code><br>- <code>chat</code><br>- <code>default</code><br>- <code>file-transfer</code><br>- <code>networking-protocols</code><br>- <code>peer-to-peer</code><br>- <code>software-update</code> | Service Name.<br>Specific service to target for this application.<br>If no service is specified, all supported services of the application are matched.<br>Not all valid values are valid for all applications, check on EOS CLI. |
    | [<samp>&nbsp;&nbsp;field_sets</samp>](## "application_traffic_recognition.field_sets") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l4_ports</samp>](## "application_traffic_recognition.field_sets.l4_ports") | List, items: Dictionary |  |  |  | L4 port field-set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.field_sets.l4_ports.[].name") | String | Required, Unique |  |  | L4 port field-set name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;port_values</samp>](## "application_traffic_recognition.field_sets.l4_ports.[].port_values") | List, items: String |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "application_traffic_recognition.field_sets.l4_ports.[].port_values.[]") | String |  |  |  | Port values or range of port values.<br>Port values are between 0 and 65535. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4_prefixes</samp>](## "application_traffic_recognition.field_sets.ipv4_prefixes") | List, items: Dictionary |  |  |  | IPv4 prefix field set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.field_sets.ipv4_prefixes.[].name") | String | Required, Unique |  |  | IPv4 prefix field-set name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_values</samp>](## "application_traffic_recognition.field_sets.ipv4_prefixes.[].prefix_values") | List, items: String |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "application_traffic_recognition.field_sets.ipv4_prefixes.[].prefix_values.[]") | String |  |  |  | IP prefix (ex 1.2.3.0/24). |
    | [<samp>&nbsp;&nbsp;applications</samp>](## "application_traffic_recognition.applications") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4_applications</samp>](## "application_traffic_recognition.applications.ipv4_applications") | List, items: Dictionary |  |  |  | List of user defined IPv4 applications. The name should be unique over all defined applications (ipv4 and l4). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].name") | String | Required, Unique |  |  | Application name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;src_prefix_set_name</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].src_prefix_set_name") | String |  |  |  | Source prefix set name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dest_prefix_set_name</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].dest_prefix_set_name") | String |  |  |  | Destination prefix set name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp_ranges</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].dscp_ranges") | List, items: String |  |  |  | Accept DSCP value(s) or range(s).<br>DSCP values can be between 0 and 63.<br>Other valid values are cs0 to cs7, af11-13, af21-23, af31-33, af41-af43 and ef.<br>Note: The values are not sorted so the list items need to be supplied in the right order to match the CLI if required. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].dscp_ranges.[]") | String |  |  | Pattern: `^(?:cs[1-7]|af[1-4][1-3]|ef|(?:(?:,|,\s|^)(?:\d|[1-5]\d|6[0-3])(?:-(?:\d|[1-5]\d|6[0-3]))?)+)$` | DSCP value or range syntax. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocols</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].protocols") | List, items: String |  |  |  | List of protocols to consider for this application.<br>To use port field-sets (source, destination or both), the list<br>must contain only one or two protocols, either `tcp` or `udp`.<br>When using both protocols, one line is rendered for each in the configuration,<br>hence the field-sets must have the same value for `tcp_src_port_set_name` and<br>`udp_src_port_set_name` and for `tcp_dest_port_set_name` and `udp_dest_port_set_name`<br>if set in order to generate valid configuration in EOS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].protocols.[]") | String |  |  | Valid Values:<br>- <code>ahp</code><br>- <code>esp</code><br>- <code>icmp</code><br>- <code>igmp</code><br>- <code>ospf</code><br>- <code>pim</code><br>- <code>rsvp</code><br>- <code>tcp</code><br>- <code>udp</code><br>- <code>vrrp</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol_ranges</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].protocol_ranges") | List, items: String |  |  |  | Accept protocol value(s) or range(s).<br>Protocol values can be between 1 and 255. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].protocol_ranges.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;udp_src_port_set_name</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].udp_src_port_set_name") | String |  |  |  | Name of field set for UDP source ports.<br>When the `protocols` list contain both `tcp` and `udp`, this key value<br>must be the same as `tcp_src_port_set_name`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tcp_src_port_set_name</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].tcp_src_port_set_name") | String |  |  |  | Name of field set for TCP source ports.<br>When the `protocols` list contain both `tcp` and `udp`, this key value<br>must be the same as `udp_src_port_set_name`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;udp_dest_port_set_name</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].udp_dest_port_set_name") | String |  |  |  | Name of field set for UDP destination ports.<br>When the `protocols` list contain both `tcp` and `udp`, this key value<br>must be the same as `tcp_dest_port_set_name`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tcp_dest_port_set_name</samp>](## "application_traffic_recognition.applications.ipv4_applications.[].tcp_dest_port_set_name") | String |  |  |  | Name of field set for TCP destination ports.<br>When the `protocols` list contain both `tcp` and `udp`, this key value<br>must be the same as `udp_dest_port_set_name`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;l4_applications</samp>](## "application_traffic_recognition.applications.l4_applications") | List, items: Dictionary |  |  |  | List of user defined L4 applications. The name should be unique over all defined applications (ipv4 and l4). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.applications.l4_applications.[].name") | String | Required, Unique |  |  | Application name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocols</samp>](## "application_traffic_recognition.applications.l4_applications.[].protocols") | List, items: String |  |  |  | List of protocols to consider for this application.<br>To use port field-sets (source, destination or both), the list<br>must contain only one or two protocols, either `tcp` or `udp`.<br>When using both protocols, one line is rendered for each in the configuration,<br>hence the field-sets must have the same value for `tcp_src_port_set_name` and<br>`udp_src_port_set_name` and for `tcp_dest_port_set_name` and `udp_dest_port_set_name`<br>if set in order to generate valid configuration in EOS. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "application_traffic_recognition.applications.l4_applications.[].protocols.[]") | String |  |  | Valid Values:<br>- <code>ahp</code><br>- <code>esp</code><br>- <code>icmp</code><br>- <code>igmp</code><br>- <code>ospf</code><br>- <code>pim</code><br>- <code>rsvp</code><br>- <code>tcp</code><br>- <code>udp</code><br>- <code>vrrp</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol_ranges</samp>](## "application_traffic_recognition.applications.l4_applications.[].protocol_ranges") | List, items: String |  |  |  | Accept protocol value(s) or range(s).<br>Protocol values can be between 1 and 255. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "application_traffic_recognition.applications.l4_applications.[].protocol_ranges.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;udp_src_port_set_name</samp>](## "application_traffic_recognition.applications.l4_applications.[].udp_src_port_set_name") | String |  |  |  | Name of field set for UDP source ports.<br>When the `protocols` list contain both `tcp` and `udp`, this key value<br>must be the same as `tcp_src_port_set_name`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tcp_src_port_set_name</samp>](## "application_traffic_recognition.applications.l4_applications.[].tcp_src_port_set_name") | String |  |  |  | Name of field set for TCP source ports.<br>When the `protocols` list contain both `tcp` and `udp`, this key value<br>must be the same as `udp_src_port_set_name`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;udp_dest_port_set_name</samp>](## "application_traffic_recognition.applications.l4_applications.[].udp_dest_port_set_name") | String |  |  |  | Name of field set for UDP destination ports.<br>When the `protocols` list contain both `tcp` and `udp`, this key value<br>must be the same as `tcp_dest_port_set_name`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tcp_dest_port_set_name</samp>](## "application_traffic_recognition.applications.l4_applications.[].tcp_dest_port_set_name") | String |  |  |  | Name of field set for TCP destination ports.<br>When the `protocols` list contain both `tcp` and `udp`, this key value<br>must be the same as `udp_dest_port_set_name`. |
    | [<samp>&nbsp;&nbsp;application_profiles</samp>](## "application_traffic_recognition.application_profiles") | List, items: Dictionary |  |  |  | Group of applications. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.application_profiles.[].name") | String | Required, Unique |  |  | Application Profile name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;applications</samp>](## "application_traffic_recognition.application_profiles.[].applications") | List, items: Dictionary |  |  |  | List of applications part of the application profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.application_profiles.[].applications.[].name") | String |  |  |  | Application Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;service</samp>](## "application_traffic_recognition.application_profiles.[].applications.[].service") | String |  |  | Valid Values:<br>- <code>audio-video</code><br>- <code>chat</code><br>- <code>default</code><br>- <code>file-transfer</code><br>- <code>networking-protocols</code><br>- <code>peer-to-peer</code><br>- <code>software-update</code> | Service Name.<br>Specific service to target for this application.<br>If no service is specified, all supported services of the application are matched.<br>Not all valid values are valid for all applications, check on EOS CLI. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;application_transports</samp>](## "application_traffic_recognition.application_profiles.[].application_transports") | List, items: String |  |  |  | List of transport protocols. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "application_traffic_recognition.application_profiles.[].application_transports.[]") | String |  |  | Valid Values:<br>- <code>http</code><br>- <code>https</code><br>- <code>udp</code><br>- <code>tcp</code><br>- <code>ip</code><br>- <code>ip6</code><br>- <code>ssl</code><br>- <code>rtp</code><br>- <code>sctp</code><br>- <code>quic</code> | Transport name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;categories</samp>](## "application_traffic_recognition.application_profiles.[].categories") | List, items: Dictionary |  |  |  | Categories under this application profile. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "application_traffic_recognition.application_profiles.[].categories.[].name") | String |  |  |  | Name of a category. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;service</samp>](## "application_traffic_recognition.application_profiles.[].categories.[].service") | String |  |  | Valid Values:<br>- <code>audio-video</code><br>- <code>chat</code><br>- <code>default</code><br>- <code>file-transfer</code><br>- <code>networking-protocols</code><br>- <code>peer-to-peer</code><br>- <code>software-update</code> | Service Name.<br>Specific service to target for this application.<br>If no service is specified, all supported services of the application are matched.<br>Not all valid values are valid for all applications, check on EOS CLI. |

=== "YAML"

    ```yaml
    # Application traffic recognition configuration.
    application_traffic_recognition:

      # List of categories.
      categories:

          # Category name.
        - name: <str; required; unique>

          # List of applications.
          applications:

              # Application name.
            - name: <str>

              # Service Name.
              # Specific service to target for this application.
              # If no service is specified, all supported services of the application are matched.
              # Not all valid values are valid for all applications, check on EOS CLI.
              service: <str; "audio-video" | "chat" | "default" | "file-transfer" | "networking-protocols" | "peer-to-peer" | "software-update">
      field_sets:

        # L4 port field-set.
        l4_ports:

            # L4 port field-set name.
          - name: <str; required; unique>
            port_values: # >=1 items

                # Port values or range of port values.
                # Port values are between 0 and 65535.
              - <str>

        # IPv4 prefix field set.
        ipv4_prefixes:

            # IPv4 prefix field-set name.
          - name: <str; required; unique>
            prefix_values: # >=1 items

                # IP prefix (ex 1.2.3.0/24).
              - <str>
      applications:

        # List of user defined IPv4 applications. The name should be unique over all defined applications (ipv4 and l4).
        ipv4_applications:

            # Application name.
          - name: <str; required; unique>

            # Source prefix set name.
            src_prefix_set_name: <str>

            # Destination prefix set name.
            dest_prefix_set_name: <str>

            # Accept DSCP value(s) or range(s).
            # DSCP values can be between 0 and 63.
            # Other valid values are cs0 to cs7, af11-13, af21-23, af31-33, af41-af43 and ef.
            # Note: The values are not sorted so the list items need to be supplied in the right order to match the CLI if required.
            dscp_ranges:

                # DSCP value or range syntax.
              - <str>

            # List of protocols to consider for this application.
            # To use port field-sets (source, destination or both), the list
            # must contain only one or two protocols, either `tcp` or `udp`.
            # When using both protocols, one line is rendered for each in the configuration,
            # hence the field-sets must have the same value for `tcp_src_port_set_name` and
            # `udp_src_port_set_name` and for `tcp_dest_port_set_name` and `udp_dest_port_set_name`
            # if set in order to generate valid configuration in EOS.
            protocols:
              - <str; "ahp" | "esp" | "icmp" | "igmp" | "ospf" | "pim" | "rsvp" | "tcp" | "udp" | "vrrp">

            # Accept protocol value(s) or range(s).
            # Protocol values can be between 1 and 255.
            protocol_ranges:
              - <str>

            # Name of field set for UDP source ports.
            # When the `protocols` list contain both `tcp` and `udp`, this key value
            # must be the same as `tcp_src_port_set_name`.
            udp_src_port_set_name: <str>

            # Name of field set for TCP source ports.
            # When the `protocols` list contain both `tcp` and `udp`, this key value
            # must be the same as `udp_src_port_set_name`.
            tcp_src_port_set_name: <str>

            # Name of field set for UDP destination ports.
            # When the `protocols` list contain both `tcp` and `udp`, this key value
            # must be the same as `tcp_dest_port_set_name`.
            udp_dest_port_set_name: <str>

            # Name of field set for TCP destination ports.
            # When the `protocols` list contain both `tcp` and `udp`, this key value
            # must be the same as `udp_dest_port_set_name`.
            tcp_dest_port_set_name: <str>

        # List of user defined L4 applications. The name should be unique over all defined applications (ipv4 and l4).
        l4_applications:

            # Application name.
          - name: <str; required; unique>

            # List of protocols to consider for this application.
            # To use port field-sets (source, destination or both), the list
            # must contain only one or two protocols, either `tcp` or `udp`.
            # When using both protocols, one line is rendered for each in the configuration,
            # hence the field-sets must have the same value for `tcp_src_port_set_name` and
            # `udp_src_port_set_name` and for `tcp_dest_port_set_name` and `udp_dest_port_set_name`
            # if set in order to generate valid configuration in EOS.
            protocols:
              - <str; "ahp" | "esp" | "icmp" | "igmp" | "ospf" | "pim" | "rsvp" | "tcp" | "udp" | "vrrp">

            # Accept protocol value(s) or range(s).
            # Protocol values can be between 1 and 255.
            protocol_ranges:
              - <str>

            # Name of field set for UDP source ports.
            # When the `protocols` list contain both `tcp` and `udp`, this key value
            # must be the same as `tcp_src_port_set_name`.
            udp_src_port_set_name: <str>

            # Name of field set for TCP source ports.
            # When the `protocols` list contain both `tcp` and `udp`, this key value
            # must be the same as `udp_src_port_set_name`.
            tcp_src_port_set_name: <str>

            # Name of field set for UDP destination ports.
            # When the `protocols` list contain both `tcp` and `udp`, this key value
            # must be the same as `tcp_dest_port_set_name`.
            udp_dest_port_set_name: <str>

            # Name of field set for TCP destination ports.
            # When the `protocols` list contain both `tcp` and `udp`, this key value
            # must be the same as `udp_dest_port_set_name`.
            tcp_dest_port_set_name: <str>

      # Group of applications.
      application_profiles:

          # Application Profile name.
        - name: <str; required; unique>

          # List of applications part of the application profile.
          applications:

              # Application Name.
            - name: <str>

              # Service Name.
              # Specific service to target for this application.
              # If no service is specified, all supported services of the application are matched.
              # Not all valid values are valid for all applications, check on EOS CLI.
              service: <str; "audio-video" | "chat" | "default" | "file-transfer" | "networking-protocols" | "peer-to-peer" | "software-update">

          # List of transport protocols.
          application_transports:

              # Transport name.
            - <str; "http" | "https" | "udp" | "tcp" | "ip" | "ip6" | "ssl" | "rtp" | "sctp" | "quic">

          # Categories under this application profile.
          categories:

              # Name of a category.
            - name: <str>

              # Service Name.
              # Specific service to target for this application.
              # If no service is specified, all supported services of the application are matched.
              # Not all valid values are valid for all applications, check on EOS CLI.
              service: <str; "audio-video" | "chat" | "default" | "file-transfer" | "networking-protocols" | "peer-to-peer" | "software-update">
    ```
