<!--
  ~ Copyright (c) 2024 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>zscaler_endpoints</samp>](## "zscaler_endpoints") | Dictionary |  |  |  | PREVIEW: These keys are in preview mode.<br><br>Special data model used for testing the WAN internet-exit integration with Zscaler.<br>The model is supposed to be autofilled per-device by `eos_designs`.<br>Manually setting this model will take precedence and prevent `eos_designs` from trying to contact CloudVision.<br>This can be useful for offline testing or if CloudVision is not available or not configured for Zscaler integration. |
    | [<samp>&nbsp;&nbsp;primary</samp>](## "zscaler_endpoints.primary") | Dictionary | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "zscaler_endpoints.primary.ip_address") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;datacenter</samp>](## "zscaler_endpoints.primary.datacenter") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;city</samp>](## "zscaler_endpoints.primary.city") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;country</samp>](## "zscaler_endpoints.primary.country") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;region</samp>](## "zscaler_endpoints.primary.region") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;latitude</samp>](## "zscaler_endpoints.primary.latitude") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;longitude</samp>](## "zscaler_endpoints.primary.longitude") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;secondary</samp>](## "zscaler_endpoints.secondary") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "zscaler_endpoints.secondary.ip_address") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;datacenter</samp>](## "zscaler_endpoints.secondary.datacenter") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;city</samp>](## "zscaler_endpoints.secondary.city") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;country</samp>](## "zscaler_endpoints.secondary.country") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;region</samp>](## "zscaler_endpoints.secondary.region") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;latitude</samp>](## "zscaler_endpoints.secondary.latitude") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;longitude</samp>](## "zscaler_endpoints.secondary.longitude") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;tertiary</samp>](## "zscaler_endpoints.tertiary") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;ip_address</samp>](## "zscaler_endpoints.tertiary.ip_address") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;datacenter</samp>](## "zscaler_endpoints.tertiary.datacenter") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;city</samp>](## "zscaler_endpoints.tertiary.city") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;country</samp>](## "zscaler_endpoints.tertiary.country") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;region</samp>](## "zscaler_endpoints.tertiary.region") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;latitude</samp>](## "zscaler_endpoints.tertiary.latitude") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;longitude</samp>](## "zscaler_endpoints.tertiary.longitude") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;cloud_name</samp>](## "zscaler_endpoints.cloud_name") | String | Required |  |  | The name of the Zscaler cloud the CloudVision cluster is integrated with like 'zscaler1' or 'zscalerbeta'. |
    | [<samp>&nbsp;&nbsp;device_location</samp>](## "zscaler_endpoints.device_location") | Dictionary | Required |  |  | The location of the calling device after being resolved by Zscaler location APIs. This is required since Zscaler only accepts their own variants of City and Country. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;city</samp>](## "zscaler_endpoints.device_location.city") | String | Required |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;country</samp>](## "zscaler_endpoints.device_location.country") | String | Required |  |  |  |

=== "YAML"

    ```yaml
    # PREVIEW: These keys are in preview mode.
    #
    # Special data model used for testing the WAN internet-exit integration with Zscaler.
    # The model is supposed to be autofilled per-device by `eos_designs`.
    # Manually setting this model will take precedence and prevent `eos_designs` from trying to contact CloudVision.
    # This can be useful for offline testing or if CloudVision is not available or not configured for Zscaler integration.
    zscaler_endpoints:
      primary: # required
        ip_address: <str; required>
        datacenter: <str; required>
        city: <str; required>
        country: <str; required>
        region: <str; required>
        latitude: <str; required>
        longitude: <str; required>
      secondary:
        ip_address: <str; required>
        datacenter: <str; required>
        city: <str; required>
        country: <str; required>
        region: <str; required>
        latitude: <str; required>
        longitude: <str; required>
      tertiary:
        ip_address: <str; required>
        datacenter: <str; required>
        city: <str; required>
        country: <str; required>
        region: <str; required>
        latitude: <str; required>
        longitude: <str; required>

      # The name of the Zscaler cloud the CloudVision cluster is integrated with like 'zscaler1' or 'zscalerbeta'.
      cloud_name: <str; required>

      # The location of the calling device after being resolved by Zscaler location APIs. This is required since Zscaler only accepts their own variants of City and Country.
      device_location: # required
        city: <str; required>
        country: <str; required>
    ```
