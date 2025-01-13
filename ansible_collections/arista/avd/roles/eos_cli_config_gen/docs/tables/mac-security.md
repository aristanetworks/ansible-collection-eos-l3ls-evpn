<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mac_security</samp>](## "mac_security") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;license</samp>](## "mac_security.license") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;license_name</samp>](## "mac_security.license.license_name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;license_key</samp>](## "mac_security.license.license_key") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;fips_restrictions</samp>](## "mac_security.fips_restrictions") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;profiles</samp>](## "mac_security.profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "mac_security.profiles.[].name") | String | Required, Unique |  |  | Profile-Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cipher</samp>](## "mac_security.profiles.[].cipher") | String |  |  | Valid Values:<br>- <code>aes128-gcm</code><br>- <code>aes128-gcm-xpn</code><br>- <code>aes256-gcm</code><br>- <code>aes256-gcm-xpn</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;connection_keys</samp>](## "mac_security.profiles.[].connection_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "mac_security.profiles.[].connection_keys.[].id") | String | Required, Unique |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encrypted_key</samp>](## "mac_security.profiles.[].connection_keys.[].encrypted_key") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fallback</samp>](## "mac_security.profiles.[].connection_keys.[].fallback") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mka</samp>](## "mac_security.profiles.[].mka") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_server_priority</samp>](## "mac_security.profiles.[].mka.key_server_priority") | Integer |  |  | Min: 0<br>Max: 255 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;session</samp>](## "mac_security.profiles.[].mka.session") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;rekey_period</samp>](## "mac_security.profiles.[].mka.session.rekey_period") | Integer |  |  | Min: 30<br>Max: 100000 | Rekey period in seconds. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sci</samp>](## "mac_security.profiles.[].sci") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l2_protocols</samp>](## "mac_security.profiles.[].l2_protocols") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ethernet_flow_control</samp>](## "mac_security.profiles.[].l2_protocols.ethernet_flow_control") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "mac_security.profiles.[].l2_protocols.ethernet_flow_control.mode") | String | Required |  | Valid Values:<br>- <code>encrypt</code><br>- <code>bypass</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lldp</samp>](## "mac_security.profiles.[].l2_protocols.lldp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mode</samp>](## "mac_security.profiles.[].l2_protocols.lldp.mode") | String | Required |  | Valid Values:<br>- <code>bypass</code><br>- <code>bypass unauthorized</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;traffic_unprotected</samp>](## "mac_security.profiles.[].traffic_unprotected") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;action</samp>](## "mac_security.profiles.[].traffic_unprotected.action") | String | Required |  | Valid Values:<br>- <code>allow</code><br>- <code>drop</code> | Allow/drop the transmit/receive of unprotected traffic. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;allow_active_sak</samp>](## "mac_security.profiles.[].traffic_unprotected.allow_active_sak") | Boolean |  |  |  | Allow transmit/receive of encrypted traffic using operational SAK and block otherwise. |

=== "YAML"

    ```yaml
    mac_security:
      license:
        license_name: <str; required>
        license_key: <str; required>
      fips_restrictions: <bool>
      profiles:

          # Profile-Name.
        - name: <str; required; unique>
          cipher: <str; "aes128-gcm" | "aes128-gcm-xpn" | "aes256-gcm" | "aes256-gcm-xpn">
          connection_keys:
            - id: <str; required; unique>
              encrypted_key: <str>
              fallback: <bool>
          mka:
            key_server_priority: <int; 0-255>
            session:

              # Rekey period in seconds.
              rekey_period: <int; 30-100000>
          sci: <bool>
          l2_protocols:
            ethernet_flow_control:
              mode: <str; "encrypt" | "bypass"; required>
            lldp:
              mode: <str; "bypass" | "bypass unauthorized"; required>
          traffic_unprotected:

            # Allow/drop the transmit/receive of unprotected traffic.
            action: <str; "allow" | "drop"; required>

            # Allow transmit/receive of encrypted traffic using operational SAK and block otherwise.
            allow_active_sak: <bool>
    ```
