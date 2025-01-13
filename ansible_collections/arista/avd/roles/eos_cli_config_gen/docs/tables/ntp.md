<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>ntp</samp>](## "ntp") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;local_interface</samp>](## "ntp.local_interface") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "ntp.local_interface.name") | String |  |  |  | Source interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ntp.local_interface.vrf") | String |  |  |  | VRF name. |
    | [<samp>&nbsp;&nbsp;servers</samp>](## "ntp.servers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "ntp.servers.[].name") | String |  |  |  | IP or hostname e.g., 2.2.2.55, 2001:db8::55, ie.pool.ntp.org. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;burst</samp>](## "ntp.servers.[].burst") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;iburst</samp>](## "ntp.servers.[].iburst") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "ntp.servers.[].key") | Integer |  |  | Min: 1<br>Max: 65535 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;local_interface</samp>](## "ntp.servers.[].local_interface") | String |  |  |  | Source interface. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;maxpoll</samp>](## "ntp.servers.[].maxpoll") | Integer |  |  | Min: 3<br>Max: 17 | Value of maxpoll between 3 - 17 (Logarithmic). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;minpoll</samp>](## "ntp.servers.[].minpoll") | Integer |  |  | Min: 3<br>Max: 17 | Value of minpoll between 3 - 17 (Logarithmic). |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preferred</samp>](## "ntp.servers.[].preferred") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;version</samp>](## "ntp.servers.[].version") | Integer |  |  | Min: 1<br>Max: 4 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrf</samp>](## "ntp.servers.[].vrf") | String |  |  |  | VRF name. |
    | [<samp>&nbsp;&nbsp;authenticate</samp>](## "ntp.authenticate") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;authenticate_servers_only</samp>](## "ntp.authenticate_servers_only") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;authentication_keys</samp>](## "ntp.authentication_keys") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "ntp.authentication_keys.[].id") | Integer | Required, Unique |  | Min: 1<br>Max: 65534 | Key identifier. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hash_algorithm</samp>](## "ntp.authentication_keys.[].hash_algorithm") | String |  |  | Valid Values:<br>- <code>md5</code><br>- <code>sha1</code> |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key</samp>](## "ntp.authentication_keys.[].key") | String |  |  |  | Obfuscated key. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;key_type</samp>](## "ntp.authentication_keys.[].key_type") | String |  |  | Valid Values:<br>- <code>0</code><br>- <code>7</code><br>- <code>8a</code> |  |
    | [<samp>&nbsp;&nbsp;trusted_keys</samp>](## "ntp.trusted_keys") | String |  |  |  | List of trusted-keys as string ex. 10-12,15. |

=== "YAML"

    ```yaml
    ntp:
      local_interface:

        # Source interface.
        name: <str>

        # VRF name.
        vrf: <str>
      servers:

          # IP or hostname e.g., 2.2.2.55, 2001:db8::55, ie.pool.ntp.org.
        - name: <str>
          burst: <bool>
          iburst: <bool>
          key: <int; 1-65535>

          # Source interface.
          local_interface: <str>

          # Value of maxpoll between 3 - 17 (Logarithmic).
          maxpoll: <int; 3-17>

          # Value of minpoll between 3 - 17 (Logarithmic).
          minpoll: <int; 3-17>
          preferred: <bool>
          version: <int; 1-4>

          # VRF name.
          vrf: <str>
      authenticate: <bool>
      authenticate_servers_only: <bool>
      authentication_keys:

          # Key identifier.
        - id: <int; 1-65534; required; unique>
          hash_algorithm: <str; "md5" | "sha1">

          # Obfuscated key.
          key: <str>
          key_type: <str; "0" | "7" | "8a">

      # List of trusted-keys as string ex. 10-12,15.
      trusted_keys: <str>
    ```
