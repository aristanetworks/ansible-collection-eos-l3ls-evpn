<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ipv4_acls</samp>](## "ipv4_acls") | List, items: Dictionary |  |  |  | IPv4 extended access-lists supporting substitution on certain fields.<br>These access-lists can be referenced under node settings `l3_interfaces`, and will only be configured on devices where they are in use.<br><br>The substitution is useful when assigning the same access-list on multiple interfaces,<br>but where certain fields require unique values like the "interface_ip" or "peer_ip".<br>When using substitution, the interface name will be appended to the ACL name. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "ipv4_acls.[].name") | String | Required, Unique |  |  | Access-list name.<br>When using substitution for any fields, the interface name will be appended to the ACL name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "ipv4_acls.[].entries") | List, items: Dictionary | Required |  |  | ACL Entries. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;source</samp>](## "ipv4_acls.[].entries.[].source") | String |  |  |  | This field supports substitution of the fields "interface_ip" for SVIs and both "interface_ip" and "peer_ip" for Layer 3 interfaces.<br>Alternatively it can be set with a static value of "any", "<ip>/<mask>" or "<ip>".<br>"<ip>" without a mask means host.<br>Required except for remarks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "ipv4_acls.[].entries.[].destination") | String |  |  |  | This field supports substitution of the fields "interface_ip" for SVIs and both "interface_ip" and "peer_ip" for Layer 3 interfaces.<br>Alternatively it can be set with a static value of "any", "<ip>/<mask>" or "<ip>".<br>"<ip>" without a mask means host.<br>Required except for remarks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence</samp>](## "ipv4_acls.[].entries.[].sequence") | Integer |  |  |  | ACL entry sequence number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remark</samp>](## "ipv4_acls.[].entries.[].remark") | String |  |  |  | Comment up to 100 characters.<br>If remark is defined, other keys in the ACL entry will be ignored. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ipv4_acls.[].entries.[].action") | String |  |  | Valid Values:<br>- <code>permit</code><br>- <code>deny</code> | ACL action.<br>Required except for remarks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "ipv4_acls.[].entries.[].protocol") | String |  |  |  | "ip", "tcp", "udp", "icmp" or other protocol name or number.<br>Required except for remarks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ports_match</samp>](## "ipv4_acls.[].entries.[].source_ports_match") | String |  | `eq` | Valid Values:<br>- <code>eq</code><br>- <code>gt</code><br>- <code>lt</code><br>- <code>neq</code><br>- <code>range</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ports</samp>](## "ipv4_acls.[].entries.[].source_ports") | List, items: String |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "ipv4_acls.[].entries.[].source_ports.[]") | String |  |  |  | TCP/UDP source port name or number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_ports_match</samp>](## "ipv4_acls.[].entries.[].destination_ports_match") | String |  | `eq` | Valid Values:<br>- <code>eq</code><br>- <code>gt</code><br>- <code>lt</code><br>- <code>neq</code><br>- <code>range</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_ports</samp>](## "ipv4_acls.[].entries.[].destination_ports") | List, items: String |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "ipv4_acls.[].entries.[].destination_ports.[]") | String |  |  |  | TCP/UDP destination port name or number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tcp_flags</samp>](## "ipv4_acls.[].entries.[].tcp_flags") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "ipv4_acls.[].entries.[].tcp_flags.[]") | String |  |  |  | TCP Flag Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fragments</samp>](## "ipv4_acls.[].entries.[].fragments") | Boolean |  |  |  | Match non-head fragment packets. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;log</samp>](## "ipv4_acls.[].entries.[].log") | Boolean |  |  |  | Log matches against this rule. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp>](## "ipv4_acls.[].entries.[].ttl") | Integer |  |  | Min: 0<br>Max: 255 | TTL value. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl_match</samp>](## "ipv4_acls.[].entries.[].ttl_match") | String |  | `eq` | Valid Values:<br>- <code>eq</code><br>- <code>gt</code><br>- <code>lt</code><br>- <code>neq</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;icmp_type</samp>](## "ipv4_acls.[].entries.[].icmp_type") | String |  |  |  | Message type name/number for ICMP packets. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;icmp_code</samp>](## "ipv4_acls.[].entries.[].icmp_code") | String |  |  |  | Message code for ICMP packets. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nexthop_group</samp>](## "ipv4_acls.[].entries.[].nexthop_group") | String |  |  |  | nexthop-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tracked</samp>](## "ipv4_acls.[].entries.[].tracked") | Boolean |  |  |  | Match packets in existing ICMP/UDP/TCP connections. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "ipv4_acls.[].entries.[].dscp") | String |  |  |  | DSCP value or name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_number</samp>](## "ipv4_acls.[].entries.[].vlan_number") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_inner</samp>](## "ipv4_acls.[].entries.[].vlan_inner") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_mask</samp>](## "ipv4_acls.[].entries.[].vlan_mask") | String |  |  |  | 0x000-0xFFF VLAN mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp>](## "ipv4_acls.[].counters_per_entry") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;permit_response_traffic</samp>](## "ipv4_acls.[].permit_response_traffic") | String |  |  | Valid Values:<br>- <code>nat</code> | Permit response traffic automatically based on NAT translations.<br>Minimum EOS version requirement 4.32.2F. |

=== "YAML"

    ```yaml
    # IPv4 extended access-lists supporting substitution on certain fields.
    # These access-lists can be referenced under node settings `l3_interfaces`, and will only be configured on devices where they are in use.
    #
    # The substitution is useful when assigning the same access-list on multiple interfaces,
    # but where certain fields require unique values like the "interface_ip" or "peer_ip".
    # When using substitution, the interface name will be appended to the ACL name.
    ipv4_acls:

        # Access-list name.
        # When using substitution for any fields, the interface name will be appended to the ACL name.
      - name: <str; required; unique>

        # ACL Entries.
        entries: # required

            # This field supports substitution of the fields "interface_ip" for SVIs and both "interface_ip" and "peer_ip" for Layer 3 interfaces.
            # Alternatively it can be set with a static value of "any", "<ip>/<mask>" or "<ip>".
            # "<ip>" without a mask means host.
            # Required except for remarks.
          - source: <str>

            # This field supports substitution of the fields "interface_ip" for SVIs and both "interface_ip" and "peer_ip" for Layer 3 interfaces.
            # Alternatively it can be set with a static value of "any", "<ip>/<mask>" or "<ip>".
            # "<ip>" without a mask means host.
            # Required except for remarks.
            destination: <str>

            # ACL entry sequence number.
            sequence: <int>

            # Comment up to 100 characters.
            # If remark is defined, other keys in the ACL entry will be ignored.
            remark: <str>

            # ACL action.
            # Required except for remarks.
            action: <str; "permit" | "deny">

            # "ip", "tcp", "udp", "icmp" or other protocol name or number.
            # Required except for remarks.
            protocol: <str>
            source_ports_match: <str; "eq" | "gt" | "lt" | "neq" | "range"; default="eq">
            source_ports: # >=1 items

                # TCP/UDP source port name or number.
              - <str>
            destination_ports_match: <str; "eq" | "gt" | "lt" | "neq" | "range"; default="eq">
            destination_ports: # >=1 items

                # TCP/UDP destination port name or number.
              - <str>
            tcp_flags:

                # TCP Flag Name.
              - <str>

            # Match non-head fragment packets.
            fragments: <bool>

            # Log matches against this rule.
            log: <bool>

            # TTL value.
            ttl: <int; 0-255>
            ttl_match: <str; "eq" | "gt" | "lt" | "neq"; default="eq">

            # Message type name/number for ICMP packets.
            icmp_type: <str>

            # Message code for ICMP packets.
            icmp_code: <str>

            # nexthop-group name.
            nexthop_group: <str>

            # Match packets in existing ICMP/UDP/TCP connections.
            tracked: <bool>

            # DSCP value or name.
            dscp: <str>
            vlan_number: <int>
            vlan_inner: <bool; default=False>

            # 0x000-0xFFF VLAN mask.
            vlan_mask: <str>
        counters_per_entry: <bool>

        # Permit response traffic automatically based on NAT translations.
        # Minimum EOS version requirement 4.32.2F.
        permit_response_traffic: <str; "nat">
    ```
