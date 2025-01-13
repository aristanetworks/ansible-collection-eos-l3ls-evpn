<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>snmp_server</samp>](## "snmp_server") | Dictionary |  |  |  | SNMP settings. |
    | [<samp>&nbsp;&nbsp;engine_ids</samp>](## "snmp_server.engine_ids") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;local</samp>](## "snmp_server.engine_ids.local") | String |  |  |  | Engine ID in hexadecimal.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;remotes</samp>](## "snmp_server.engine_ids.remotes") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "snmp_server.engine_ids.remotes.[].id") | String |  |  |  | Remote engine ID in hexadecimal.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address</samp>](## "snmp_server.engine_ids.remotes.[].address") | String |  |  |  | Hostname or IP of remote engine.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;udp_port</samp>](## "snmp_server.engine_ids.remotes.[].udp_port") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;contact</samp>](## "snmp_server.contact") | String |  |  |  | SNMP contact. |
    | [<samp>&nbsp;&nbsp;location</samp>](## "snmp_server.location") | String |  |  |  | SNMP location. |
    | [<samp>&nbsp;&nbsp;communities</samp>](## "snmp_server.communities") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "snmp_server.communities.[].name") | String | Required, Unique |  |  | Community name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access</samp>](## "snmp_server.communities.[].access") | String |  |  | Valid Values:<br>- <code>ro</code><br>- <code>rw</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_list_ipv4</samp>](## "snmp_server.communities.[].access_list_ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "snmp_server.communities.[].access_list_ipv4.name") | String |  |  |  | IPv4 access list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_list_ipv6</samp>](## "snmp_server.communities.[].access_list_ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "snmp_server.communities.[].access_list_ipv6.name") | String |  |  |  | IPv6 access list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;view</samp>](## "snmp_server.communities.[].view") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ipv4_acls</samp>](## "snmp_server.ipv4_acls") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "snmp_server.ipv4_acls.[].name") | String |  |  |  | IPv4 access list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "snmp_server.ipv4_acls.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ipv6_acls</samp>](## "snmp_server.ipv6_acls") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "snmp_server.ipv6_acls.[].name") | String |  |  |  | IPv6 access list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "snmp_server.ipv6_acls.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;local_interfaces</samp>](## "snmp_server.local_interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "snmp_server.local_interfaces.[].name") | String | Required, Unique |  |  | Interface name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "snmp_server.local_interfaces.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;views</samp>](## "snmp_server.views") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "snmp_server.views.[].name") | String |  |  |  | SNMP view name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mib_family_name</samp>](## "snmp_server.views.[].mib_family_name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;included</samp>](## "snmp_server.views.[].included") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MIB_family_name</samp>](## "snmp_server.views.[].MIB_family_name") <span style="color:red">removed</span> | String |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>mib_family_name</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;groups</samp>](## "snmp_server.groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "snmp_server.groups.[].name") | String |  |  |  | Group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "snmp_server.groups.[].version") | String |  |  | Valid Values:<br>- <code>v1</code><br>- <code>v2c</code><br>- <code>v3</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "snmp_server.groups.[].authentication") | String |  |  | Valid Values:<br>- <code>auth</code><br>- <code>noauth</code><br>- <code>priv</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;read</samp>](## "snmp_server.groups.[].read") | String |  |  |  | Read view. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;write</samp>](## "snmp_server.groups.[].write") | String |  |  |  | Write view. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;notify</samp>](## "snmp_server.groups.[].notify") | String |  |  |  | Notify view. |
    | [<samp>&nbsp;&nbsp;users</samp>](## "snmp_server.users") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "snmp_server.users.[].name") | String |  |  |  | Username. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "snmp_server.users.[].group") | String |  |  |  | Group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;remote_address</samp>](## "snmp_server.users.[].remote_address") | String |  |  |  | Hostname or ip of remote engine.<br>The remote_address and udp_port are used for remote users.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;udp_port</samp>](## "snmp_server.users.[].udp_port") | Integer |  |  |  | udp_port will not be used if no remote_address is configured.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "snmp_server.users.[].version") | String |  |  | Valid Values:<br>- <code>v1</code><br>- <code>v2c</code><br>- <code>v3</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;localized</samp>](## "snmp_server.users.[].localized") | String |  |  |  | Engine ID in hexadecimal for localizing auth and/or priv.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth</samp>](## "snmp_server.users.[].auth") | String |  |  |  | Hash algorithm.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth_passphrase</samp>](## "snmp_server.users.[].auth_passphrase") | String |  |  |  | Hashed authentication passphrase if localized is used else cleartext authentication passphrase.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priv</samp>](## "snmp_server.users.[].priv") | String |  |  |  | Encryption algorithm.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priv_passphrase</samp>](## "snmp_server.users.[].priv_passphrase") | String |  |  |  | Hashed privacy passphrase if localized is used else cleartext privacy passphrase.<br> |
    | [<samp>&nbsp;&nbsp;hosts</samp>](## "snmp_server.hosts") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;host</samp>](## "snmp_server.hosts.[].host") | String |  |  |  | Host IP address or name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "snmp_server.hosts.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "snmp_server.hosts.[].version") | String |  |  | Valid Values:<br>- <code>1</code><br>- <code>2c</code><br>- <code>3</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;community</samp>](## "snmp_server.hosts.[].community") | String |  |  |  | Community name. Required with version "1" or "2c". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;users</samp>](## "snmp_server.hosts.[].users") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;username</samp>](## "snmp_server.hosts.[].users.[].username") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication_level</samp>](## "snmp_server.hosts.[].users.[].authentication_level") | String |  |  | Valid Values:<br>- <code>auth</code><br>- <code>noauth</code><br>- <code>priv</code> |  |
    | [<samp>&nbsp;&nbsp;traps</samp>](## "snmp_server.traps") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "snmp_server.traps.enable") | Boolean |  | `False` |  | Enable or disable all snmp-traps.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;snmp_traps</samp>](## "snmp_server.traps.snmp_traps") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "snmp_server.traps.snmp_traps.[].name") | String |  |  |  | Enable or disable specific snmp-traps and their sub_traps.<br>Examples:<br>- "bgp"<br>- "bgp established"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "snmp_server.traps.snmp_traps.[].enabled") | Boolean |  | `True` |  |  |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "snmp_server.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "snmp_server.vrfs.[].name") | String | Required, Unique |  |  | VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "snmp_server.vrfs.[].enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ifmib_ifspeed_shape_rate</samp>](## "snmp_server.ifmib_ifspeed_shape_rate") | Boolean |  |  |  | SNMP ifspeed reflecting shaping rate. |

=== "YAML"

    ```yaml
    # SNMP settings.
    snmp_server:
      engine_ids:

        # Engine ID in hexadecimal.
        local: <str>
        remotes:

            # Remote engine ID in hexadecimal.
          - id: <str>

            # Hostname or IP of remote engine.
            address: <str>
            udp_port: <int>

      # SNMP contact.
      contact: <str>

      # SNMP location.
      location: <str>
      communities:

          # Community name.
        - name: <str; required; unique>
          access: <str; "ro" | "rw">
          access_list_ipv4:

            # IPv4 access list name.
            name: <str>
          access_list_ipv6:

            # IPv6 access list name.
            name: <str>
          view: <str>
      ipv4_acls:

          # IPv4 access list name.
        - name: <str>
          vrf: <str>
      ipv6_acls:

          # IPv6 access list name.
        - name: <str>
          vrf: <str>
      local_interfaces:

          # Interface name.
        - name: <str; required; unique>
          vrf: <str>
      views:

          # SNMP view name.
        - name: <str>
          mib_family_name: <str>
          included: <bool>
      groups:

          # Group name.
        - name: <str>
          version: <str; "v1" | "v2c" | "v3">
          authentication: <str; "auth" | "noauth" | "priv">

          # Read view.
          read: <str>

          # Write view.
          write: <str>

          # Notify view.
          notify: <str>
      users:

          # Username.
        - name: <str>

          # Group name.
          group: <str>

          # Hostname or ip of remote engine.
          # The remote_address and udp_port are used for remote users.
          remote_address: <str>

          # udp_port will not be used if no remote_address is configured.
          udp_port: <int>
          version: <str; "v1" | "v2c" | "v3">

          # Engine ID in hexadecimal for localizing auth and/or priv.
          localized: <str>

          # Hash algorithm.
          auth: <str>

          # Hashed authentication passphrase if localized is used else cleartext authentication passphrase.
          auth_passphrase: <str>

          # Encryption algorithm.
          priv: <str>

          # Hashed privacy passphrase if localized is used else cleartext privacy passphrase.
          priv_passphrase: <str>
      hosts:

          # Host IP address or name.
        - host: <str>
          vrf: <str>
          version: <str; "1" | "2c" | "3">

          # Community name. Required with version "1" or "2c".
          community: <str>
          users:
            - username: <str>
              authentication_level: <str; "auth" | "noauth" | "priv">
      traps:

        # Enable or disable all snmp-traps.
        enable: <bool; default=False>
        snmp_traps:

            # Enable or disable specific snmp-traps and their sub_traps.
            # Examples:
            # - "bgp"
            # - "bgp established"
          - name: <str>
            enabled: <bool; default=True>
      vrfs:

          # VRF name.
        - name: <str; required; unique>
          enable: <bool>

      # SNMP ifspeed reflecting shaping rate.
      ifmib_ifspeed_shape_rate: <bool>
    ```
