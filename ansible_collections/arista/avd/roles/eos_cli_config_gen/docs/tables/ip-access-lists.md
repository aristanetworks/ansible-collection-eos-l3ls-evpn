<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ip_access_lists</samp>](## "ip_access_lists") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "ip_access_lists.[].name") | String | Required, Unique |  |  | Access-list Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters_per_entry</samp>](## "ip_access_lists.[].counters_per_entry") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;entries</samp>](## "ip_access_lists.[].entries") | List, items: Dictionary |  |  |  | ACL Entries. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;sequence</samp>](## "ip_access_lists.[].entries.[].sequence") | Integer |  |  |  | ACL entry sequence number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remark</samp>](## "ip_access_lists.[].entries.[].remark") | String |  |  |  | Comment up to 100 characters.<br>If remark is defined, other keys in the ACL entry will be ignored. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "ip_access_lists.[].entries.[].action") | String |  |  | Valid Values:<br>- <code>permit</code><br>- <code>deny</code> | ACL action.<br>Required except for remarks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;protocol</samp>](## "ip_access_lists.[].entries.[].protocol") | String |  |  |  | "ip", "tcp", "udp", "icmp" or other protocol name or number.<br>Required except for remarks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "ip_access_lists.[].entries.[].source") | String |  |  |  | "any", "<ip>/<mask>" or "<ip>".<br>"<ip>" without a mask means host.<br>Required except for remarks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ports_match</samp>](## "ip_access_lists.[].entries.[].source_ports_match") | String |  | `eq` | Valid Values:<br>- <code>eq</code><br>- <code>gt</code><br>- <code>lt</code><br>- <code>neq</code><br>- <code>range</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_ports</samp>](## "ip_access_lists.[].entries.[].source_ports") | List, items: String |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "ip_access_lists.[].entries.[].source_ports.[]") | String |  |  |  | TCP/UDP source port name or number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination</samp>](## "ip_access_lists.[].entries.[].destination") | String |  |  |  | "any", "<ip>/<mask>" or "<ip>".<br>"<ip>" without a mask means host.<br>Required except for remarks. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_ports_match</samp>](## "ip_access_lists.[].entries.[].destination_ports_match") | String |  | `eq` | Valid Values:<br>- <code>eq</code><br>- <code>gt</code><br>- <code>lt</code><br>- <code>neq</code><br>- <code>range</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destination_ports</samp>](## "ip_access_lists.[].entries.[].destination_ports") | List, items: String |  |  | Min Length: 1 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "ip_access_lists.[].entries.[].destination_ports.[]") | String |  |  |  | TCP/UDP destination port name or number. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tcp_flags</samp>](## "ip_access_lists.[].entries.[].tcp_flags") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "ip_access_lists.[].entries.[].tcp_flags.[]") | String |  |  |  | TCP Flag Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fragments</samp>](## "ip_access_lists.[].entries.[].fragments") | Boolean |  |  |  | Match non-head fragment packets. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;log</samp>](## "ip_access_lists.[].entries.[].log") | Boolean |  |  |  | Log matches against this rule. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl</samp>](## "ip_access_lists.[].entries.[].ttl") | Integer |  |  | Min: 0<br>Max: 255 | TTL value. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ttl_match</samp>](## "ip_access_lists.[].entries.[].ttl_match") | String |  | `eq` | Valid Values:<br>- <code>eq</code><br>- <code>gt</code><br>- <code>lt</code><br>- <code>neq</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;icmp_type</samp>](## "ip_access_lists.[].entries.[].icmp_type") | String |  |  |  | Message type name/number for ICMP packets. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;icmp_code</samp>](## "ip_access_lists.[].entries.[].icmp_code") | String |  |  |  | Message code for ICMP packets. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nexthop_group</samp>](## "ip_access_lists.[].entries.[].nexthop_group") | String |  |  |  | nexthop-group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tracked</samp>](## "ip_access_lists.[].entries.[].tracked") | Boolean |  |  |  | Match packets in existing ICMP/UDP/TCP connections. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp</samp>](## "ip_access_lists.[].entries.[].dscp") | String |  |  |  | DSCP value or name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_number</samp>](## "ip_access_lists.[].entries.[].vlan_number") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_inner</samp>](## "ip_access_lists.[].entries.[].vlan_inner") | Boolean |  | `False` |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlan_mask</samp>](## "ip_access_lists.[].entries.[].vlan_mask") | String |  |  |  | 0x000-0xFFF VLAN mask. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;permit_response_traffic</samp>](## "ip_access_lists.[].permit_response_traffic") | String |  |  | Valid Values:<br>- <code>nat</code> | Permit response traffic automatically based on NAT translations.<br>Minimum EOS version requirement 4.32.2F. |

=== "YAML"

    ```yaml
    ip_access_lists:

        # Access-list Name.
      - name: <str; required; unique>
        counters_per_entry: <bool>

        # ACL Entries.
        entries:

            # ACL entry sequence number.
          - sequence: <int>

            # Comment up to 100 characters.
            # If remark is defined, other keys in the ACL entry will be ignored.
            remark: <str>

            # ACL action.
            # Required except for remarks.
            action: <str; "permit" | "deny">

            # "ip", "tcp", "udp", "icmp" or other protocol name or number.
            # Required except for remarks.
            protocol: <str>

            # "any", "<ip>/<mask>" or "<ip>".
            # "<ip>" without a mask means host.
            # Required except for remarks.
            source: <str>
            source_ports_match: <str; "eq" | "gt" | "lt" | "neq" | "range"; default="eq">
            source_ports: # >=1 items

                # TCP/UDP source port name or number.
              - <str>

            # "any", "<ip>/<mask>" or "<ip>".
            # "<ip>" without a mask means host.
            # Required except for remarks.
            destination: <str>
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

        # Permit response traffic automatically based on NAT translations.
        # Minimum EOS version requirement 4.32.2F.
        permit_response_traffic: <str; "nat">
    ```
