<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>metadata</samp>](## "metadata") | Dictionary |  |  |  | The data under `metadata` is used for documentation, validation or integration purposes.<br>It will not affect the generated EOS configuration. |
    | [<samp>&nbsp;&nbsp;platform</samp>](## "metadata.platform") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;system_mac_address</samp>](## "metadata.system_mac_address") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;cv_tags</samp>](## "metadata.cv_tags") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;device_tags</samp>](## "metadata.cv_tags.device_tags") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "metadata.cv_tags.device_tags.[].name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "metadata.cv_tags.device_tags.[].value") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface_tags</samp>](## "metadata.cv_tags.interface_tags") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;interface</samp>](## "metadata.cv_tags.interface_tags.[].interface") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tags</samp>](## "metadata.cv_tags.interface_tags.[].tags") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "metadata.cv_tags.interface_tags.[].tags.[].name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;value</samp>](## "metadata.cv_tags.interface_tags.[].tags.[].value") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;cv_pathfinder</samp>](## "metadata.cv_pathfinder") | Dictionary |  |  |  | Metadata used for CV Pathfinder visualization on CloudVision. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;role</samp>](## "metadata.cv_pathfinder.role") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;region</samp>](## "metadata.cv_pathfinder.region") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;zone</samp>](## "metadata.cv_pathfinder.zone") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;site</samp>](## "metadata.cv_pathfinder.site") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vtep_ip</samp>](## "metadata.cv_pathfinder.vtep_ip") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ssl_profile</samp>](## "metadata.cv_pathfinder.ssl_profile") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;address</samp>](## "metadata.cv_pathfinder.address") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pathfinders</samp>](## "metadata.cv_pathfinder.pathfinders") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;vtep_ip</samp>](## "metadata.cv_pathfinder.pathfinders.[].vtep_ip") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interfaces</samp>](## "metadata.cv_pathfinder.interfaces") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "metadata.cv_pathfinder.interfaces.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;carrier</samp>](## "metadata.cv_pathfinder.interfaces.[].carrier") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;circuit_id</samp>](## "metadata.cv_pathfinder.interfaces.[].circuit_id") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pathgroup</samp>](## "metadata.cv_pathfinder.interfaces.[].pathgroup") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;public_ip</samp>](## "metadata.cv_pathfinder.interfaces.[].public_ip") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;pathgroups</samp>](## "metadata.cv_pathfinder.pathgroups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "metadata.cv_pathfinder.pathgroups.[].name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;carriers</samp>](## "metadata.cv_pathfinder.pathgroups.[].carriers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "metadata.cv_pathfinder.pathgroups.[].carriers.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;imported_carriers</samp>](## "metadata.cv_pathfinder.pathgroups.[].imported_carriers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "metadata.cv_pathfinder.pathgroups.[].imported_carriers.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;regions</samp>](## "metadata.cv_pathfinder.regions") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "metadata.cv_pathfinder.regions.[].id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "metadata.cv_pathfinder.regions.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;zones</samp>](## "metadata.cv_pathfinder.regions.[].zones") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "metadata.cv_pathfinder.regions.[].zones.[].id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "metadata.cv_pathfinder.regions.[].zones.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;sites</samp>](## "metadata.cv_pathfinder.regions.[].zones.[].sites") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;id</samp>](## "metadata.cv_pathfinder.regions.[].zones.[].sites.[].id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "metadata.cv_pathfinder.regions.[].zones.[].sites.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;location</samp>](## "metadata.cv_pathfinder.regions.[].zones.[].sites.[].location") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;address</samp>](## "metadata.cv_pathfinder.regions.[].zones.[].sites.[].location.address") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "metadata.cv_pathfinder.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "metadata.cv_pathfinder.vrfs.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni</samp>](## "metadata.cv_pathfinder.vrfs.[].vni") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;avts</samp>](## "metadata.cv_pathfinder.vrfs.[].avts") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;constraints</samp>](## "metadata.cv_pathfinder.vrfs.[].avts.[].constraints") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;jitter</samp>](## "metadata.cv_pathfinder.vrfs.[].avts.[].constraints.jitter") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;latency</samp>](## "metadata.cv_pathfinder.vrfs.[].avts.[].constraints.latency") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;lossrate</samp>](## "metadata.cv_pathfinder.vrfs.[].avts.[].constraints.lossrate") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;hop_count</samp>](## "metadata.cv_pathfinder.vrfs.[].avts.[].constraints.hop_count") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "metadata.cv_pathfinder.vrfs.[].avts.[].description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;id</samp>](## "metadata.cv_pathfinder.vrfs.[].avts.[].id") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "metadata.cv_pathfinder.vrfs.[].avts.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pathgroups</samp>](## "metadata.cv_pathfinder.vrfs.[].avts.[].pathgroups") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "metadata.cv_pathfinder.vrfs.[].avts.[].pathgroups.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preference</samp>](## "metadata.cv_pathfinder.vrfs.[].avts.[].pathgroups.[].preference") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;application_profiles</samp>](## "metadata.cv_pathfinder.vrfs.[].avts.[].application_profiles") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "metadata.cv_pathfinder.vrfs.[].avts.[].application_profiles.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;internet_exit_policies</samp>](## "metadata.cv_pathfinder.internet_exit_policies") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "metadata.cv_pathfinder.internet_exit_policies.[].name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "metadata.cv_pathfinder.internet_exit_policies.[].type") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;city</samp>](## "metadata.cv_pathfinder.internet_exit_policies.[].city") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;country</samp>](## "metadata.cv_pathfinder.internet_exit_policies.[].country") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;upload_bandwidth</samp>](## "metadata.cv_pathfinder.internet_exit_policies.[].upload_bandwidth") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;download_bandwidth</samp>](## "metadata.cv_pathfinder.internet_exit_policies.[].download_bandwidth") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;firewall</samp>](## "metadata.cv_pathfinder.internet_exit_policies.[].firewall") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ips_control</samp>](## "metadata.cv_pathfinder.internet_exit_policies.[].ips_control") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;acceptable_use_policy</samp>](## "metadata.cv_pathfinder.internet_exit_policies.[].acceptable_use_policy") | Boolean | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vpn_credentials</samp>](## "metadata.cv_pathfinder.internet_exit_policies.[].vpn_credentials") | List, items: Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;fqdn</samp>](## "metadata.cv_pathfinder.internet_exit_policies.[].vpn_credentials.[].fqdn") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vpn_type</samp>](## "metadata.cv_pathfinder.internet_exit_policies.[].vpn_credentials.[].vpn_type") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pre_shared_key</samp>](## "metadata.cv_pathfinder.internet_exit_policies.[].vpn_credentials.[].pre_shared_key") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;tunnels</samp>](## "metadata.cv_pathfinder.internet_exit_policies.[].tunnels") | List, items: Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "metadata.cv_pathfinder.internet_exit_policies.[].tunnels.[].name") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;preference</samp>](## "metadata.cv_pathfinder.internet_exit_policies.[].tunnels.[].preference") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;endpoint</samp>](## "metadata.cv_pathfinder.internet_exit_policies.[].tunnels.[].endpoint") | Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "metadata.cv_pathfinder.internet_exit_policies.[].tunnels.[].endpoint.ip_address") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;datacenter</samp>](## "metadata.cv_pathfinder.internet_exit_policies.[].tunnels.[].endpoint.datacenter") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;city</samp>](## "metadata.cv_pathfinder.internet_exit_policies.[].tunnels.[].endpoint.city") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;country</samp>](## "metadata.cv_pathfinder.internet_exit_policies.[].tunnels.[].endpoint.country") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;region</samp>](## "metadata.cv_pathfinder.internet_exit_policies.[].tunnels.[].endpoint.region") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;latitude</samp>](## "metadata.cv_pathfinder.internet_exit_policies.[].tunnels.[].endpoint.latitude") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;longitude</samp>](## "metadata.cv_pathfinder.internet_exit_policies.[].tunnels.[].endpoint.longitude") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;applications</samp>](## "metadata.cv_pathfinder.applications") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;profiles</samp>](## "metadata.cv_pathfinder.applications.profiles") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "metadata.cv_pathfinder.applications.profiles.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;builtin_applications</samp>](## "metadata.cv_pathfinder.applications.profiles.[].builtin_applications") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "metadata.cv_pathfinder.applications.profiles.[].builtin_applications.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;services</samp>](## "metadata.cv_pathfinder.applications.profiles.[].builtin_applications.[].services") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "metadata.cv_pathfinder.applications.profiles.[].builtin_applications.[].services.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;user_defined_applications</samp>](## "metadata.cv_pathfinder.applications.profiles.[].user_defined_applications") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "metadata.cv_pathfinder.applications.profiles.[].user_defined_applications.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;categories</samp>](## "metadata.cv_pathfinder.applications.profiles.[].categories") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;category</samp>](## "metadata.cv_pathfinder.applications.profiles.[].categories.[].category") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;services</samp>](## "metadata.cv_pathfinder.applications.profiles.[].categories.[].services") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "metadata.cv_pathfinder.applications.profiles.[].categories.[].services.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;transport_protocols</samp>](## "metadata.cv_pathfinder.applications.profiles.[].transport_protocols") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "metadata.cv_pathfinder.applications.profiles.[].transport_protocols.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;categories</samp>](## "metadata.cv_pathfinder.applications.categories") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;builtin_applications</samp>](## "metadata.cv_pathfinder.applications.categories.builtin_applications") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "metadata.cv_pathfinder.applications.categories.builtin_applications.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;category</samp>](## "metadata.cv_pathfinder.applications.categories.builtin_applications.[].category") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;services</samp>](## "metadata.cv_pathfinder.applications.categories.builtin_applications.[].services") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "metadata.cv_pathfinder.applications.categories.builtin_applications.[].services.[]") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;user_defined_applications</samp>](## "metadata.cv_pathfinder.applications.categories.user_defined_applications") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "metadata.cv_pathfinder.applications.categories.user_defined_applications.[].name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;category</samp>](## "metadata.cv_pathfinder.applications.categories.user_defined_applications.[].category") | String |  |  |  |  |

=== "YAML"

    ```yaml
    # The data under `metadata` is used for documentation, validation or integration purposes.
    # It will not affect the generated EOS configuration.
    metadata:
      platform: <str>
      system_mac_address: <str>
      cv_tags:
        device_tags:
          - name: <str; required>
            value: <str; required>
        interface_tags:
          - interface: <str; required>
            tags:
              - name: <str; required>
                value: <str; required>

      # Metadata used for CV Pathfinder visualization on CloudVision.
      cv_pathfinder:
        role: <str>
        region: <str>
        zone: <str>
        site: <str>
        vtep_ip: <str>
        ssl_profile: <str>
        address: <str>
        pathfinders:
          - vtep_ip: <str; required>
        interfaces:
          - name: <str>
            carrier: <str>
            circuit_id: <str>
            pathgroup: <str>
            public_ip: <str>
        pathgroups:
          - name: <str; required>
            carriers:
              - name: <str>
            imported_carriers:
              - name: <str>
        regions:
          - id: <int>
            name: <str>
            zones:
              - id: <int>
                name: <str>
                sites:
                  - id: <int>
                    name: <str>
                    location:
                      address: <str>
        vrfs:
          - name: <str>
            vni: <int>
            avts:
              - constraints:
                  jitter: <int>
                  latency: <int>
                  lossrate: <str>
                  hop_count: <str>
                description: <str>
                id: <int>
                name: <str>
                pathgroups:
                  - name: <str>
                    preference: <str>
                application_profiles:
                  - <str>
        internet_exit_policies:
          - name: <str; required>
            type: <str; required>
            city: <str; required>
            country: <str; required>
            upload_bandwidth: <int>
            download_bandwidth: <int>
            firewall: <bool; required>
            ips_control: <bool; required>
            acceptable_use_policy: <bool; required>
            vpn_credentials: # required
              - fqdn: <str; required>
                vpn_type: <str; required>
                pre_shared_key: <str; required>
            tunnels: # required
              - name: <str; required>
                preference: <str; required>
                endpoint: # required
                  ip_address: <str; required>
                  datacenter: <str; required>
                  city: <str; required>
                  country: <str; required>
                  region: <str; required>
                  latitude: <str; required>
                  longitude: <str; required>
        applications:
          profiles:
            - name: <str>
              builtin_applications:
                - name: <str>
                  services:
                    - <str>
              user_defined_applications:
                - name: <str>
              categories:
                - category: <str>
                  services:
                    - <str>
              transport_protocols:
                - <str>
          categories:
            builtin_applications:
              - name: <str>
                category: <str>
                services:
                  - <str>
            user_defined_applications:
              - name: <str>
                category: <str>
    ```
