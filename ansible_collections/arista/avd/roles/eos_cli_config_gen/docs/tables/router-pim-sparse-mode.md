<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>router_pim_sparse_mode</samp>](## "router_pim_sparse_mode") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ipv4</samp>](## "router_pim_sparse_mode.ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "router_pim_sparse_mode.ipv4.bfd") | Boolean |  |  |  | Enable/Disable BFD. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;make_before_break</samp>](## "router_pim_sparse_mode.ipv4.make_before_break") | Boolean |  |  |  | Enable/Disable Make-Before-Break. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ssm_range</samp>](## "router_pim_sparse_mode.ipv4.ssm_range") | String |  |  |  | IPv4 Prefix associated with SSM. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;rp_addresses</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;address</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses.[].address") | String | Required |  |  | RP Address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses.[].groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses.[].groups.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_lists</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses.[].access_lists") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses.[].access_lists.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses.[].priority") | Integer |  |  | Min: 0<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hashmask</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses.[].hashmask") | Integer |  |  | Min: 0<br>Max: 32 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;override</samp>](## "router_pim_sparse_mode.ipv4.rp_addresses.[].override") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;anycast_rps</samp>](## "router_pim_sparse_mode.ipv4.anycast_rps") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;address</samp>](## "router_pim_sparse_mode.ipv4.anycast_rps.[].address") | String | Required, Unique |  |  | Anycast RP Address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;other_anycast_rp_addresses</samp>](## "router_pim_sparse_mode.ipv4.anycast_rps.[].other_anycast_rp_addresses") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;address</samp>](## "router_pim_sparse_mode.ipv4.anycast_rps.[].other_anycast_rp_addresses.[].address") | String | Required, Unique |  |  | Other Anycast RP Address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;register_count</samp>](## "router_pim_sparse_mode.ipv4.anycast_rps.[].other_anycast_rp_addresses.[].register_count") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "router_pim_sparse_mode.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "router_pim_sparse_mode.vrfs.[].name") | String | Required, Unique |  |  | VRF Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv4</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.bfd") | Boolean |  |  |  | Enable/Disable BFD. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;make_before_break</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.make_before_break") | Boolean |  |  |  | Enable/Disable Make-Before-Break. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rp_addresses</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;address</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses.[].address") | String | Required |  |  | RP Address. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;groups</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses.[].groups") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses.[].groups.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_lists</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses.[].access_lists") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses.[].access_lists.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priority</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses.[].priority") | Integer |  |  | Min: 0<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hashmask</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses.[].hashmask") | Integer |  |  | Min: 0<br>Max: 32 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;override</samp>](## "router_pim_sparse_mode.vrfs.[].ipv4.rp_addresses.[].override") | Boolean |  |  |  |  |

=== "YAML"

    ```yaml
    router_pim_sparse_mode:
      ipv4:

        # Enable/Disable BFD.
        bfd: <bool>

        # Enable/Disable Make-Before-Break.
        make_before_break: <bool>

        # IPv4 Prefix associated with SSM.
        ssm_range: <str>
        rp_addresses:

            # RP Address.
          - address: <str; required>
            groups:
              - <str>
            access_lists:
              - <str>
            priority: <int; 0-255>
            hashmask: <int; 0-32>
            override: <bool>
        anycast_rps:

            # Anycast RP Address.
          - address: <str; required; unique>
            other_anycast_rp_addresses:

                # Other Anycast RP Address.
              - address: <str; required; unique>
                register_count: <int>
      vrfs:

          # VRF Name.
        - name: <str; required; unique>
          ipv4:

            # Enable/Disable BFD.
            bfd: <bool>

            # Enable/Disable Make-Before-Break.
            make_before_break: <bool>
            rp_addresses:

                # RP Address.
              - address: <str; required>
                groups:
                  - <str>
                access_lists:
                  - <str>
                priority: <int; 0-255>
                hashmask: <int; 0-32>
                override: <bool>
    ```
