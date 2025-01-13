<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>management_api_http</samp>](## "management_api_http") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enable_http</samp>](## "management_api_http.enable_http") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;enable_https</samp>](## "management_api_http.enable_https") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;https_ssl_profile</samp>](## "management_api_http.https_ssl_profile") | String |  |  |  | SSL Profile Name. |
    | [<samp>&nbsp;&nbsp;default_services</samp>](## "management_api_http.default_services") | Boolean |  |  |  | Enable default services: capi-doc and tapagg. |
    | [<samp>&nbsp;&nbsp;enable_vrfs</samp>](## "management_api_http.enable_vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;name</samp>](## "management_api_http.enable_vrfs.[].name") | String | Required, Unique |  |  | VRF Name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;access_group</samp>](## "management_api_http.enable_vrfs.[].access_group") | String |  |  |  | Standard IPv4 ACL name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipv6_access_group</samp>](## "management_api_http.enable_vrfs.[].ipv6_access_group") | String |  |  |  | Standard IPv6 ACL name. |
    | [<samp>&nbsp;&nbsp;protocol_https_certificate</samp>](## "management_api_http.protocol_https_certificate") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;certificate</samp>](## "management_api_http.protocol_https_certificate.certificate") | String |  |  |  | Name of certificate; private key must also be specified. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;private_key</samp>](## "management_api_http.protocol_https_certificate.private_key") | String |  |  |  | Name of private key; certificate must also be specified. |

=== "YAML"

    ```yaml
    management_api_http:
      enable_http: <bool>
      enable_https: <bool>

      # SSL Profile Name.
      https_ssl_profile: <str>

      # Enable default services: capi-doc and tapagg.
      default_services: <bool>
      enable_vrfs:

          # VRF Name.
        - name: <str; required; unique>

          # Standard IPv4 ACL name.
          access_group: <str>

          # Standard IPv6 ACL name.
          ipv6_access_group: <str>
      protocol_https_certificate:

        # Name of certificate; private key must also be specified.
        certificate: <str>

        # Name of private key; certificate must also be specified.
        private_key: <str>
    ```
