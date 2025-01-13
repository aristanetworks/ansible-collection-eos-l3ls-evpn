<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_multicast</samp>](## "router_multicast") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ipv4</samp>](## "router_multicast.ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;activity_polling_interval</samp>](## "router_multicast.ipv4.activity_polling_interval") | Integer |  |  | Min: 1<br>Max: 60 | MFIB entry activity polling interval. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;counters</samp>](## "router_multicast.ipv4.counters") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rate_period_decay</samp>](## "router_multicast.ipv4.counters.rate_period_decay") | Integer |  |  | Min: 0<br>Max: 600 | Rate in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;routing</samp>](## "router_multicast.ipv4.routing") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;multipath</samp>](## "router_multicast.ipv4.multipath") | String |  |  | Valid Values:<br>- <code>none</code><br>- <code>deterministic</code><br>- <code>deterministic color</code><br>- <code>deterministic router-id</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;software_forwarding</samp>](## "router_multicast.ipv4.software_forwarding") | String |  |  | Valid Values:<br>- <code>kernel</code><br>- <code>sfe</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rpf</samp>](## "router_multicast.ipv4.rpf") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;routes</samp>](## "router_multicast.ipv4.rpf.routes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;source_prefix</samp>](## "router_multicast.ipv4.rpf.routes.[].source_prefix") | String | Required |  |  | Source address A.B.C.D or Source prefix A.B.C.D/E. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;destinations</samp>](## "router_multicast.ipv4.rpf.routes.[].destinations") | List, items: Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;nexthop</samp>](## "router_multicast.ipv4.rpf.routes.[].destinations.[].nexthop") | String | Required |  |  | Next-hop IP address or interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distance</samp>](## "router_multicast.ipv4.rpf.routes.[].destinations.[].distance") | Integer |  |  | Min: 1<br>Max: 255 | Administrative distance for this route. |
    | [<samp>&nbsp;&nbsp;ipv6</samp>](## "router_multicast.ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;activity_polling_interval</samp>](## "router_multicast.ipv6.activity_polling_interval") | Integer |  |  | Min: 1<br>Max: 60 | MFIB entry activity polling interval. |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "router_multicast.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_multicast.vrfs.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "router_multicast.vrfs.[].ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;routing</samp>](## "router_multicast.vrfs.[].ipv4.routing") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    router_multicast:
      ipv4:

        # MFIB entry activity polling interval.
        activity_polling_interval: <int; 1-60>
        counters:

          # Rate in seconds.
          rate_period_decay: <int; 0-600>
        routing: <bool>
        multipath: <str; "none" | "deterministic" | "deterministic color" | "deterministic router-id">
        software_forwarding: <str; "kernel" | "sfe">
        rpf:
          routes:

              # Source address A.B.C.D or Source prefix A.B.C.D/E.
            - source_prefix: <str; required>
              destinations: # required

                  # Next-hop IP address or interface name.
                - nexthop: <str; required>

                  # Administrative distance for this route.
                  distance: <int; 1-255>
      ipv6:

        # MFIB entry activity polling interval.
        activity_polling_interval: <int; 1-60>
      vrfs:
        - name: <str; required; unique>
          ipv4:
            routing: <bool>
    ```
