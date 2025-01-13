<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>patch_panel</samp>](## "patch_panel") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;connector</samp>](## "patch_panel.connector") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "patch_panel.connector.interface") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;patch</samp>](## "patch_panel.connector.interface.patch") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bgp_vpws_remote_failure_errdisable</samp>](## "patch_panel.connector.interface.patch.bgp_vpws_remote_failure_errdisable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;recovery</samp>](## "patch_panel.connector.interface.recovery") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;review_delay</samp>](## "patch_panel.connector.interface.recovery.review_delay") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min</samp>](## "patch_panel.connector.interface.recovery.review_delay.min") | Integer | Required |  | Min: 10<br>Max: 600 | Minimum delay. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;max</samp>](## "patch_panel.connector.interface.recovery.review_delay.max") | Integer | Required |  | Min: 15<br>Max: 900 | Maximum delay. |
    | [<samp>&nbsp;&nbsp;patches</samp>](## "patch_panel.patches") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "patch_panel.patches.[].name") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "patch_panel.patches.[].enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connectors</samp>](## "patch_panel.patches.[].connectors") | List, items: Dictionary |  |  | Min Length: 2<br>Max Length: 2 | Must have exactly two connectors to a patch of which at least one must be of type "interface". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "patch_panel.patches.[].connectors.[].id") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "patch_panel.patches.[].connectors.[].type") | String | Required |  | Valid Values:<br>- <code>interface</code><br>- <code>pseudowire</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;endpoint</samp>](## "patch_panel.patches.[].connectors.[].endpoint") | String | Required |  |  | String with relevant endpoint depending on type.<br>Examples:<br>- "Ethernet1"<br>- "Ethernet1 dot1q vlan 123"<br>- "bgp vpws TENANT_A pseudowire VPWS_PW_1"<br>- "ldp LDP_PW_1"<br> |

=== "YAML"

    ```yaml
    patch_panel:
      connector:
        interface:
          patch:
            bgp_vpws_remote_failure_errdisable: <bool>
          recovery:
            review_delay:

              # Minimum delay.
              min: <int; 10-600; required>

              # Maximum delay.
              max: <int; 15-900; required>
      patches:
        - name: <str; required; unique>
          enabled: <bool>

          # Must have exactly two connectors to a patch of which at least one must be of type "interface".
          connectors: # 2-2 items
            - id: <str; required; unique>
              type: <str; "interface" | "pseudowire"; required>

              # String with relevant endpoint depending on type.
              # Examples:
              # - "Ethernet1"
              # - "Ethernet1 dot1q vlan 123"
              # - "bgp vpws TENANT_A pseudowire VPWS_PW_1"
              # - "ldp LDP_PW_1"
              endpoint: <str; required>
    ```
