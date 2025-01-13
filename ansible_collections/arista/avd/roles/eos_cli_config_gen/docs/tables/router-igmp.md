<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_igmp</samp>](## "router_igmp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;host_proxy_match_mroute</samp>](## "router_igmp.host_proxy_match_mroute") | String |  |  | Valid Values:<br>- <code>all</code><br>- <code>iif</code> | Specify conditions for sending IGMP joins for host-proxy.<br>'iif' will enable igmp host-proxy to work in iif aware.<br>'all' will enable igmp host-proxy to work in iif unaware mode (EOS default).<br> |
    | [<samp>&nbsp;&nbsp;ssm_aware</samp>](## "router_igmp.ssm_aware") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "router_igmp.vrfs") | List, items: Dictionary |  |  |  | Configure IGMP in a VRF.<br>VRF 'default' is not supported in EOS, please see keys directly under 'router_igmp'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_igmp.vrfs.[].name") | String | Required, Unique |  |  | VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;host_proxy_match_mroute</samp>](## "router_igmp.vrfs.[].host_proxy_match_mroute") | String |  |  | Valid Values:<br>- <code>all</code><br>- <code>iif</code> | Specify conditions for sending IGMP joins for host-proxy.<br>'iif' will enable igmp host-proxy to work in iif aware.<br>'all' will enable igmp host-proxy to work in iif unaware mode (EOS default).<br> |

=== "YAML"

    ```yaml
    router_igmp:

      # Specify conditions for sending IGMP joins for host-proxy.
      # 'iif' will enable igmp host-proxy to work in iif aware.
      # 'all' will enable igmp host-proxy to work in iif unaware mode (EOS default).
      host_proxy_match_mroute: <str; "all" | "iif">
      ssm_aware: <bool>

      # Configure IGMP in a VRF.
      # VRF 'default' is not supported in EOS, please see keys directly under 'router_igmp'.
      vrfs:

          # VRF name.
        - name: <str; required; unique>

          # Specify conditions for sending IGMP joins for host-proxy.
          # 'iif' will enable igmp host-proxy to work in iif aware.
          # 'all' will enable igmp host-proxy to work in iif unaware mode (EOS default).
          host_proxy_match_mroute: <str; "all" | "iif">
    ```
