<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>dhcp_servers</samp>](## "dhcp_servers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;disabled</samp>](## "dhcp_servers.[].disabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "dhcp_servers.[].vrf") | String | Required, Unique |  |  | VRF in which to configure the DHCP server, use `default` to indicate default VRF. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lease_time_ipv4</samp>](## "dhcp_servers.[].lease_time_ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;days</samp>](## "dhcp_servers.[].lease_time_ipv4.days") | Integer | Required |  | Min: 0<br>Max: 2000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hours</samp>](## "dhcp_servers.[].lease_time_ipv4.hours") | Integer | Required |  | Min: 0<br>Max: 23 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minutes</samp>](## "dhcp_servers.[].lease_time_ipv4.minutes") | Integer | Required |  | Min: 0<br>Max: 59 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;lease_time_ipv6</samp>](## "dhcp_servers.[].lease_time_ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;days</samp>](## "dhcp_servers.[].lease_time_ipv6.days") | Integer | Required |  | Min: 0<br>Max: 2000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hours</samp>](## "dhcp_servers.[].lease_time_ipv6.hours") | Integer | Required |  | Min: 0<br>Max: 23 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minutes</samp>](## "dhcp_servers.[].lease_time_ipv6.minutes") | Integer | Required |  | Min: 0<br>Max: 59 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dns_domain_name_ipv4</samp>](## "dhcp_servers.[].dns_domain_name_ipv4") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dns_domain_name_ipv6</samp>](## "dhcp_servers.[].dns_domain_name_ipv6") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dns_servers_ipv4</samp>](## "dhcp_servers.[].dns_servers_ipv4") | List, items: String |  |  | Min Length: 1 | List of DNS servers for IPv4 clients. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "dhcp_servers.[].dns_servers_ipv4.[]") | String | Required |  |  | IPv4 address of DNS server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;dns_servers_ipv6</samp>](## "dhcp_servers.[].dns_servers_ipv6") | List, items: String |  |  | Min Length: 1 | List of DNS servers for IPv6 clients. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "dhcp_servers.[].dns_servers_ipv6.[]") | String | Required |  |  | IPv6 address of DNS server. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tftp_server</samp>](## "dhcp_servers.[].tftp_server") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;file_ipv4</samp>](## "dhcp_servers.[].tftp_server.file_ipv4") | String |  |  | Min Length: 1<br>Max Length: 255 | Name of TFTP file for IPv4 clients. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;file_ipv6</samp>](## "dhcp_servers.[].tftp_server.file_ipv6") | String |  |  | Min Length: 1<br>Max Length: 255 | Name of TFTP file for IPv6 clients. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ipv4_vendor_options</samp>](## "dhcp_servers.[].ipv4_vendor_options") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;vendor_id</samp>](## "dhcp_servers.[].ipv4_vendor_options.[].vendor_id") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sub_options</samp>](## "dhcp_servers.[].ipv4_vendor_options.[].sub_options") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;code</samp>](## "dhcp_servers.[].ipv4_vendor_options.[].sub_options.[].code") | Integer | Required, Unique |  | Min: 1<br>Max: 254 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;string</samp>](## "dhcp_servers.[].ipv4_vendor_options.[].sub_options.[].string") | String |  |  |  | String value for suboption data.<br>Only one of `string`, `ipv4_address` and `array_ipv4_address` variables should be used for any one suboption.<br>The order of precedence if multiple of these variables are defined is `string` -> `ipv4_address` -> `array_ipv4_address`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_address</samp>](## "dhcp_servers.[].ipv4_vendor_options.[].sub_options.[].ipv4_address") | String |  |  |  | IPv4 address value for suboption data.<br>Only one of `string`, `ipv4_address` and `array_ipv4_address` variables should be used for any one suboption.<br>The order of precedence if multiple of these variables are defined is `string` -> `ipv4_address` -> `array_ipv4_address`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;array_ipv4_address</samp>](## "dhcp_servers.[].ipv4_vendor_options.[].sub_options.[].array_ipv4_address") | List, items: String |  |  |  | Array of IPv4 addresses for suboption data.<br>Only one of `string`, `ipv4_address` and `array_ipv4_address` variables should be used for any one suboption.<br>The order of precedence if multiple of these variables are defined is `string` -> `ipv4_address` -> `array_ipv4_address`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "dhcp_servers.[].ipv4_vendor_options.[].sub_options.[].array_ipv4_address.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;subnets</samp>](## "dhcp_servers.[].subnets") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;subnet</samp>](## "dhcp_servers.[].subnets.[].subnet") | String | Required, Unique |  |  | IPv4/IPv6 subnet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "dhcp_servers.[].subnets.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;default_gateway</samp>](## "dhcp_servers.[].subnets.[].default_gateway") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dns_servers</samp>](## "dhcp_servers.[].subnets.[].dns_servers") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "dhcp_servers.[].subnets.[].dns_servers.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ranges</samp>](## "dhcp_servers.[].subnets.[].ranges") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;start</samp>](## "dhcp_servers.[].subnets.[].ranges.[].start") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;end</samp>](## "dhcp_servers.[].subnets.[].ranges.[].end") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lease_time</samp>](## "dhcp_servers.[].subnets.[].lease_time") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;days</samp>](## "dhcp_servers.[].subnets.[].lease_time.days") | Integer | Required |  | Min: 0<br>Max: 2000 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hours</samp>](## "dhcp_servers.[].subnets.[].lease_time.hours") | Integer | Required |  | Min: 0<br>Max: 23 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minutes</samp>](## "dhcp_servers.[].subnets.[].lease_time.minutes") | Integer | Required |  | Min: 0<br>Max: 59 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;reservations</samp>](## "dhcp_servers.[].subnets.[].reservations") | List, items: Dictionary |  |  |  | DHCP client reservations. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;mac_address</samp>](## "dhcp_servers.[].subnets.[].reservations.[].mac_address") | String | Required, Unique |  |  | Ethernet address in format - HHHH.HHHH.HHHH |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hostname</samp>](## "dhcp_servers.[].subnets.[].reservations.[].hostname") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4_address</samp>](## "dhcp_servers.[].subnets.[].reservations.[].ipv4_address") | String |  |  |  | Valid IPv4 address from the given subnet.<br>This should only be used within an IPv4 subnet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_address</samp>](## "dhcp_servers.[].subnets.[].reservations.[].ipv6_address") | String |  |  |  | Valid IPv6 address from the given subnet.<br>This should only be used within an IPv6 subnet. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "dhcp_servers.[].eos_cli") | String |  |  |  | Multiline EOS CLI rendered directly on the dhcp server in the final EOS configuration. |

=== "YAML"

    ```yaml
    dhcp_servers:
      - disabled: <bool>

        # VRF in which to configure the DHCP server, use `default` to indicate default VRF.
        vrf: <str; required; unique>
        lease_time_ipv4:
          days: <int; 0-2000; required>
          hours: <int; 0-23; required>
          minutes: <int; 0-59; required>
        lease_time_ipv6:
          days: <int; 0-2000; required>
          hours: <int; 0-23; required>
          minutes: <int; 0-59; required>
        dns_domain_name_ipv4: <str>
        dns_domain_name_ipv6: <str>

        # List of DNS servers for IPv4 clients.
        dns_servers_ipv4: # >=1 items

            # IPv4 address of DNS server.
          - <str; required>

        # List of DNS servers for IPv6 clients.
        dns_servers_ipv6: # >=1 items

            # IPv6 address of DNS server.
          - <str; required>
        tftp_server:

          # Name of TFTP file for IPv4 clients.
          file_ipv4: <str; length 1-255>

          # Name of TFTP file for IPv6 clients.
          file_ipv6: <str; length 1-255>
        ipv4_vendor_options:
          - vendor_id: <str; required; unique>
            sub_options:
              - code: <int; 1-254; required; unique>

                # String value for suboption data.
                # Only one of `string`, `ipv4_address` and `array_ipv4_address` variables should be used for any one suboption.
                # The order of precedence if multiple of these variables are defined is `string` -> `ipv4_address` -> `array_ipv4_address`.
                string: <str>

                # IPv4 address value for suboption data.
                # Only one of `string`, `ipv4_address` and `array_ipv4_address` variables should be used for any one suboption.
                # The order of precedence if multiple of these variables are defined is `string` -> `ipv4_address` -> `array_ipv4_address`.
                ipv4_address: <str>

                # Array of IPv4 addresses for suboption data.
                # Only one of `string`, `ipv4_address` and `array_ipv4_address` variables should be used for any one suboption.
                # The order of precedence if multiple of these variables are defined is `string` -> `ipv4_address` -> `array_ipv4_address`.
                array_ipv4_address:
                  - <str>
        subnets:

            # IPv4/IPv6 subnet.
          - subnet: <str; required; unique>
            name: <str>
            default_gateway: <str>
            dns_servers:
              - <str>
            ranges:
              - start: <str; required>
                end: <str; required>
            lease_time:
              days: <int; 0-2000; required>
              hours: <int; 0-23; required>
              minutes: <int; 0-59; required>

            # DHCP client reservations.
            reservations:

                # Ethernet address in format - HHHH.HHHH.HHHH
              - mac_address: <str; required; unique>
                hostname: <str>

                # Valid IPv4 address from the given subnet.
                # This should only be used within an IPv4 subnet.
                ipv4_address: <str>

                # Valid IPv6 address from the given subnet.
                # This should only be used within an IPv6 subnet.
                ipv6_address: <str>

        # Multiline EOS CLI rendered directly on the dhcp server in the final EOS configuration.
        eos_cli: <str>
    ```
