<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>snmp_settings</samp>](## "snmp_settings") | Dictionary |  |  |  | SNMP settings.<br>For SNMP local-interfaces see "source_interfaces.snmp".<br>Configuration of remote SNMP engine IDs are currently only possible using `structured_config`. |
    | [<samp>&nbsp;&nbsp;contact</samp>](## "snmp_settings.contact") | String |  |  |  | SNMP contact. |
    | [<samp>&nbsp;&nbsp;location</samp>](## "snmp_settings.location") | Boolean |  | `False` |  | Set SNMP location. Formatted as "<fabric_name> <dc_name> <pod_name> <switch_rack> <inventory_hostname>". |
    | [<samp>&nbsp;&nbsp;vrfs</samp>](## "snmp_settings.vrfs") | List, items: Dictionary |  |  |  | Enable/disable SNMP for one or more VRFs.<br>Can be used in combination with "enable_mgmt_interface_vrf" and "enable_inband_mgmt_vrf". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "snmp_settings.vrfs.[].name") | String | Required, Unique |  |  | VRF name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "snmp_settings.vrfs.[].enable") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enable_mgmt_interface_vrf</samp>](## "snmp_settings.enable_mgmt_interface_vrf") | Boolean |  |  |  | Enable/disable SNMP for the VRF set with "mgmt_interface_vrf".<br>Ignored if 'mgmt_ip' or 'ipv6_mgmt_ip' are not configured for the device.<br>Can be used in combination with "vrfs" and "enable_inband_mgmt_vrf". |
    | [<samp>&nbsp;&nbsp;enable_inband_mgmt_vrf</samp>](## "snmp_settings.enable_inband_mgmt_vrf") | Boolean |  |  |  | Enable/disable SNMP for the VRF set with "inband_mgmt_vrf".<br>Ignored if inband management is not configured for the device.<br>Can be used in combination with "vrfs" and "enable_mgmt_interface_vrf". |
    | [<samp>&nbsp;&nbsp;compute_local_engineid</samp>](## "snmp_settings.compute_local_engineid") | Boolean |  | `False` |  | Generate a local engineId for SNMP using the 'compute_local_engineid_source' method.<br> |
    | [<samp>&nbsp;&nbsp;compute_local_engineid_source</samp>](## "snmp_settings.compute_local_engineid_source") | String |  | `hostname_and_ip` | Valid Values:<br>- <code>hostname_and_ip</code><br>- <code>system_mac</code> | `compute_local_engineid_source` supports:<br>- `hostname_and_ip` generate a local engineId for SNMP by hashing via SHA1<br>  the string generated via the concatenation of the hostname plus the management IP.<br>  {{ inventory_hostname }} + {{ switch.mgmt_ip }}.<br>- `system_mac` generate the switch default engine id for AVD usage.<br>  To use this, `system_mac_address` MUST be set for the device.<br>  The formula is f5717f + system_mac_address + 00.<br> |
    | [<samp>&nbsp;&nbsp;compute_v3_user_localized_key</samp>](## "snmp_settings.compute_v3_user_localized_key") | Boolean |  | `False` |  | Requires compute_local_engineid to be `true`.<br>If enabled, the SNMPv3 passphrases for auth and priv are transformed using RFC 2574, matching the value they would take in EOS CLI.<br>The algorithm requires a local engineId, which is unknown to AVD, hence the necessity to generate one beforehand.<br> |
    | [<samp>&nbsp;&nbsp;users</samp>](## "snmp_settings.users") | List, items: Dictionary |  |  |  | Configuration of local SNMP users.<br>Configuration of remote SNMP users are currently only possible using `structured_config`. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "snmp_settings.users.[].name") | String |  |  |  | Username. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;group</samp>](## "snmp_settings.users.[].group") | String |  |  |  | Group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "snmp_settings.users.[].version") | String |  |  | Valid Values:<br>- <code>v1</code><br>- <code>v2c</code><br>- <code>v3</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth</samp>](## "snmp_settings.users.[].auth") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>sha</code><br>- <code>sha256</code><br>- <code>sha384</code><br>- <code>sha512</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;auth_passphrase</samp>](## "snmp_settings.users.[].auth_passphrase") | String |  |  |  | Cleartext passphrase so the recommendation is to use vault. Requires 'auth' to be set. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priv</samp>](## "snmp_settings.users.[].priv") | String |  |  | Valid Values:<br>- <code>des</code><br>- <code>aes</code><br>- <code>aes192</code><br>- <code>aes256</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;priv_passphrase</samp>](## "snmp_settings.users.[].priv_passphrase") | String |  |  |  | Cleartext passphrase so the recommendation is to use vault. Requires 'priv' to be set. |
    | [<samp>&nbsp;&nbsp;hosts</samp>](## "snmp_settings.hosts") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;host</samp>](## "snmp_settings.hosts.[].host") | String |  |  |  | Host IP address or name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "snmp_settings.hosts.[].vrf") | String |  |  |  | VRF Name.<br>Can be used in combination with "use_mgmt_interface_vrf" and "use_inband_mgmt_vrf" to configure the SNMP host under multiple VRFs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use_mgmt_interface_vrf</samp>](## "snmp_settings.hosts.[].use_mgmt_interface_vrf") | Boolean |  |  |  | Configure the SNMP host under the VRF set with "mgmt_interface_vrf". Ignored if 'mgmt_ip' or 'ipv6_mgmt_ip' are not configured for the device, so if the host is only configured with this VRF, the host will not be configured at all. Can be used in combination with "vrf" and "use_inband_mgmt_vrf" to configure the SNMP host under multiple VRFs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;use_inband_mgmt_vrf</samp>](## "snmp_settings.hosts.[].use_inband_mgmt_vrf") | Boolean |  |  |  | Configure the SNMP host under the VRF set with "inband_mgmt_vrf". Ignored if inband management is not configured for the device, so if the host is only configured with this VRF, the host will not be configured at all. Can be used in combination with "vrf" and "use_mgmt_interface_vrf" to configure the SNMP host under multiple VRFs. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "snmp_settings.hosts.[].version") | String |  |  | Valid Values:<br>- <code>1</code><br>- <code>2c</code><br>- <code>3</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;community</samp>](## "snmp_settings.hosts.[].community") | String |  |  |  | Community name. Required with version "1" or "2c". |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;users</samp>](## "snmp_settings.hosts.[].users") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;username</samp>](## "snmp_settings.hosts.[].users.[].username") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication_level</samp>](## "snmp_settings.hosts.[].users.[].authentication_level") | String |  |  | Valid Values:<br>- <code>auth</code><br>- <code>noauth</code><br>- <code>priv</code> |  |
    | [<samp>&nbsp;&nbsp;communities</samp>](## "snmp_settings.communities") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "snmp_settings.communities.[].name") | String | Required, Unique |  |  | Community name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access</samp>](## "snmp_settings.communities.[].access") | String |  |  | Valid Values:<br>- <code>ro</code><br>- <code>rw</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_list_ipv4</samp>](## "snmp_settings.communities.[].access_list_ipv4") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "snmp_settings.communities.[].access_list_ipv4.name") | String |  |  |  | IPv4 access list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_list_ipv6</samp>](## "snmp_settings.communities.[].access_list_ipv6") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "snmp_settings.communities.[].access_list_ipv6.name") | String |  |  |  | IPv6 access list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;view</samp>](## "snmp_settings.communities.[].view") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ipv4_acls</samp>](## "snmp_settings.ipv4_acls") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "snmp_settings.ipv4_acls.[].name") | String |  |  |  | IPv4 access list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "snmp_settings.ipv4_acls.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;ipv6_acls</samp>](## "snmp_settings.ipv6_acls") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "snmp_settings.ipv6_acls.[].name") | String |  |  |  | IPv6 access list name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "snmp_settings.ipv6_acls.[].vrf") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;views</samp>](## "snmp_settings.views") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "snmp_settings.views.[].name") | String |  |  |  | SNMP view name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mib_family_name</samp>](## "snmp_settings.views.[].mib_family_name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;included</samp>](## "snmp_settings.views.[].included") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;MIB_family_name</samp>](## "snmp_settings.views.[].MIB_family_name") <span style="color:red">removed</span> | String |  |  |  | <span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>mib_family_name</samp> instead.</span> |
    | [<samp>&nbsp;&nbsp;groups</samp>](## "snmp_settings.groups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "snmp_settings.groups.[].name") | String |  |  |  | Group name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "snmp_settings.groups.[].version") | String |  |  | Valid Values:<br>- <code>v1</code><br>- <code>v2c</code><br>- <code>v3</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;authentication</samp>](## "snmp_settings.groups.[].authentication") | String |  |  | Valid Values:<br>- <code>auth</code><br>- <code>noauth</code><br>- <code>priv</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;read</samp>](## "snmp_settings.groups.[].read") | String |  |  |  | Read view. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;write</samp>](## "snmp_settings.groups.[].write") | String |  |  |  | Write view. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;notify</samp>](## "snmp_settings.groups.[].notify") | String |  |  |  | Notify view. |
    | [<samp>&nbsp;&nbsp;traps</samp>](## "snmp_settings.traps") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;enable</samp>](## "snmp_settings.traps.enable") | Boolean |  | `False` |  | Enable or disable all snmp-traps.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;snmp_traps</samp>](## "snmp_settings.traps.snmp_traps") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "snmp_settings.traps.snmp_traps.[].name") | String |  |  |  | Enable or disable specific snmp-traps and their sub_traps.<br>Examples:<br>- "bgp"<br>- "bgp established"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "snmp_settings.traps.snmp_traps.[].enabled") | Boolean |  | `True` |  |  |

=== "YAML"

    ```yaml
    # SNMP settings.
    # For SNMP local-interfaces see "source_interfaces.snmp".
    # Configuration of remote SNMP engine IDs are currently only possible using `structured_config`.
    snmp_settings:

      # SNMP contact.
      contact: <str>

      # Set SNMP location. Formatted as "<fabric_name> <dc_name> <pod_name> <switch_rack> <inventory_hostname>".
      location: <bool; default=False>

      # Enable/disable SNMP for one or more VRFs.
      # Can be used in combination with "enable_mgmt_interface_vrf" and "enable_inband_mgmt_vrf".
      vrfs:

          # VRF name.
        - name: <str; required; unique>
          enable: <bool>

      # Enable/disable SNMP for the VRF set with "mgmt_interface_vrf".
      # Ignored if 'mgmt_ip' or 'ipv6_mgmt_ip' are not configured for the device.
      # Can be used in combination with "vrfs" and "enable_inband_mgmt_vrf".
      enable_mgmt_interface_vrf: <bool>

      # Enable/disable SNMP for the VRF set with "inband_mgmt_vrf".
      # Ignored if inband management is not configured for the device.
      # Can be used in combination with "vrfs" and "enable_mgmt_interface_vrf".
      enable_inband_mgmt_vrf: <bool>

      # Generate a local engineId for SNMP using the 'compute_local_engineid_source' method.
      compute_local_engineid: <bool; default=False>

      # `compute_local_engineid_source` supports:
      # - `hostname_and_ip` generate a local engineId for SNMP by hashing via SHA1
      #   the string generated via the concatenation of the hostname plus the management IP.
      #   {{ inventory_hostname }} + {{ switch.mgmt_ip }}.
      # - `system_mac` generate the switch default engine id for AVD usage.
      #   To use this, `system_mac_address` MUST be set for the device.
      #   The formula is f5717f + system_mac_address + 00.
      compute_local_engineid_source: <str; "hostname_and_ip" | "system_mac"; default="hostname_and_ip">

      # Requires compute_local_engineid to be `true`.
      # If enabled, the SNMPv3 passphrases for auth and priv are transformed using RFC 2574, matching the value they would take in EOS CLI.
      # The algorithm requires a local engineId, which is unknown to AVD, hence the necessity to generate one beforehand.
      compute_v3_user_localized_key: <bool; default=False>

      # Configuration of local SNMP users.
      # Configuration of remote SNMP users are currently only possible using `structured_config`.
      users:

          # Username.
        - name: <str>

          # Group name.
          group: <str>
          version: <str; "v1" | "v2c" | "v3">
          auth: <str; "md5" | "sha" | "sha256" | "sha384" | "sha512">

          # Cleartext passphrase so the recommendation is to use vault. Requires 'auth' to be set.
          auth_passphrase: <str>
          priv: <str; "des" | "aes" | "aes192" | "aes256">

          # Cleartext passphrase so the recommendation is to use vault. Requires 'priv' to be set.
          priv_passphrase: <str>
      hosts:

          # Host IP address or name.
        - host: <str>

          # VRF Name.
          # Can be used in combination with "use_mgmt_interface_vrf" and "use_inband_mgmt_vrf" to configure the SNMP host under multiple VRFs.
          vrf: <str>

          # Configure the SNMP host under the VRF set with "mgmt_interface_vrf". Ignored if 'mgmt_ip' or 'ipv6_mgmt_ip' are not configured for the device, so if the host is only configured with this VRF, the host will not be configured at all. Can be used in combination with "vrf" and "use_inband_mgmt_vrf" to configure the SNMP host under multiple VRFs.
          use_mgmt_interface_vrf: <bool>

          # Configure the SNMP host under the VRF set with "inband_mgmt_vrf". Ignored if inband management is not configured for the device, so if the host is only configured with this VRF, the host will not be configured at all. Can be used in combination with "vrf" and "use_mgmt_interface_vrf" to configure the SNMP host under multiple VRFs.
          use_inband_mgmt_vrf: <bool>
          version: <str; "1" | "2c" | "3">

          # Community name. Required with version "1" or "2c".
          community: <str>
          users:
            - username: <str>
              authentication_level: <str; "auth" | "noauth" | "priv">
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
    ```
