<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>route_maps</samp>](## "route_maps") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "route_maps.[].name") | String | Required, Unique |  |  | Route-map Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;sequence_numbers</samp>](## "route_maps.[].sequence_numbers") | List, items: Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;sequence</samp>](## "route_maps.[].sequence_numbers.[].sequence") | Integer | Required, Unique |  |  | Sequence ID. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "route_maps.[].sequence_numbers.[].type") | String | Required |  | Valid Values:<br>- <code>permit</code><br>- <code>deny</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "route_maps.[].sequence_numbers.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;match</samp>](## "route_maps.[].sequence_numbers.[].match") | List, items: String |  |  |  | List of "match" statements. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "route_maps.[].sequence_numbers.[].match.[]") | String |  |  |  | Match as string.<br>Example: "ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;set</samp>](## "route_maps.[].sequence_numbers.[].set") | List, items: String |  |  |  | List of "set" statements. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "route_maps.[].sequence_numbers.[].set.[]") | String |  |  |  | Set as string.<br>Example: "origin incomplete"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sub_route_map</samp>](## "route_maps.[].sequence_numbers.[].sub_route_map") | String |  |  |  | Name of Sub-Route-map. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;continue</samp>](## "route_maps.[].sequence_numbers.[].continue") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "route_maps.[].sequence_numbers.[].continue.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sequence_number</samp>](## "route_maps.[].sequence_numbers.[].continue.sequence_number") | Integer |  |  |  |  |

=== "YAML"

    ```yaml
    route_maps:

        # Route-map Name.
      - name: <str; required; unique>
        sequence_numbers: # required

            # Sequence ID.
          - sequence: <int; required; unique>
            type: <str; "permit" | "deny"; required>
            description: <str>

            # List of "match" statements.
            match:

                # Match as string.
                # Example: "ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY"
              - <str>

            # List of "set" statements.
            set:

                # Set as string.
                # Example: "origin incomplete"
              - <str>

            # Name of Sub-Route-map.
            sub_route_map: <str>
            continue:
              enabled: <bool>
              sequence_number: <int>
    ```
