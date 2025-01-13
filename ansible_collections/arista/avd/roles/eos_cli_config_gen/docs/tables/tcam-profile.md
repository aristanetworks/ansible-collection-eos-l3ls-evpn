<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>tcam_profile</samp>](## "tcam_profile") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;system</samp>](## "tcam_profile.system") | String |  |  |  | TCAM profile name to activate.<br> |
    | [<samp>&nbsp;&nbsp;profiles</samp>](## "tcam_profile.profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "tcam_profile.profiles.[].name") | String | Required, Unique |  |  | Tcam-Profile Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;config</samp>](## "tcam_profile.profiles.[].config") | String |  |  |  | TCAM Profile Config. Since these can be very long, it is often a good idea to import the config from a file.<br>Example: "{{ lookup('file', 'TCAM_TRAFFIC_POLICY.conf') }}"<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source</samp>](## "tcam_profile.profiles.[].source") | String |  |  |  | TCAM profile local source path. Used to read the TCAM profile from a local path existing on the device.<br> |

=== "YAML"

    ```yaml
    tcam_profile:

      # TCAM profile name to activate.
      system: <str>
      profiles:

          # Tcam-Profile Name.
        - name: <str; required; unique>

          # TCAM Profile Config. Since these can be very long, it is often a good idea to import the config from a file.
          # Example: "{{ lookup('file', 'TCAM_TRAFFIC_POLICY.conf') }}"
          config: <str>

          # TCAM profile local source path. Used to read the TCAM profile from a local path existing on the device.
          source: <str>
    ```
