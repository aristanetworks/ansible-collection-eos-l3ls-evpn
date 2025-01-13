<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cvp_ingestauth_key</samp>](## "cvp_ingestauth_key") | String |  |  |  | On-premise CVP ingest auth key. If set, TerminAttr will be configured with key-based authentication for on-premise CVP.<br>If not set, TerminAttr will be configured with certificate based authentication:<br>- On-premise using token onboarding. Default token path is '/tmp/token'.<br>- CVaaS using token-secure onboarding. Default token path is '/tmp/cv-onboarding-token'.<br>Token must be copied to the device first. |
    | [<samp>cvp_instance_ip</samp>](## "cvp_instance_ip") <span style="color:red">removed</span> | String |  |  |  | IPv4 address or DNS name for CloudVision.<br>This variable only supports an on-premise single-node cluster or the DNS name of a CloudVision as a Service instance.<br><span style="color:red">This key was removed. Support was removed in AVD version 5.0.0. Use <samp>cvp_instance_ips</samp> instead.</span> |
    | [<samp>cvp_instance_ips</samp>](## "cvp_instance_ips") | List, items: String |  |  |  | List of IPv4 addresses or DNS names for CloudVision.<br>For on-premise CloudVision enter all the nodes of the cluster.<br>For CloudVision as a Service enter the DNS name of the instance.<br>`eos_designs` only supports one CloudVision cluster.<br> |
    | [<samp>&nbsp;&nbsp;-&nbsp;&lt;str&gt;</samp>](## "cvp_instance_ips.[]") | String |  |  |  | IPv4 address or DNS name for CloudVision. |
    | [<samp>cvp_token_file</samp>](## "cvp_token_file") | String |  |  |  | cvp_token_file is the path to the token file on the switch.<br>If not set the default locations for on-premise or CVaaS will be used.<br>See cvp_ingestauth_key for details. |
    | [<samp>terminattr_disable_aaa</samp>](## "terminattr_disable_aaa") | Boolean |  | `False` |  |  |
    | [<samp>terminattr_ingestexclude</samp>](## "terminattr_ingestexclude") | String |  | `/Sysdb/cell/1/agent,/Sysdb/cell/2/agent` |  |  |
    | [<samp>terminattr_ingestgrpcurl_port</samp>](## "terminattr_ingestgrpcurl_port") | Integer |  | `9910` |  | Port number used for Terminattr connection to an on-premise CloudVision cluster.<br>The port number is always 443 when using CloudVision as a Service, so this value is ignored. |
    | [<samp>terminattr_smashexcludes</samp>](## "terminattr_smashexcludes") | String |  | `ale,flexCounter,hardware,kni,pulse,strata` |  |  |

=== "YAML"

    ```yaml
    # On-premise CVP ingest auth key. If set, TerminAttr will be configured with key-based authentication for on-premise CVP.
    # If not set, TerminAttr will be configured with certificate based authentication:
    # - On-premise using token onboarding. Default token path is '/tmp/token'.
    # - CVaaS using token-secure onboarding. Default token path is '/tmp/cv-onboarding-token'.
    # Token must be copied to the device first.
    cvp_ingestauth_key: <str>

    # List of IPv4 addresses or DNS names for CloudVision.
    # For on-premise CloudVision enter all the nodes of the cluster.
    # For CloudVision as a Service enter the DNS name of the instance.
    # `eos_designs` only supports one CloudVision cluster.
    cvp_instance_ips:

        # IPv4 address or DNS name for CloudVision.
      - <str>

    # cvp_token_file is the path to the token file on the switch.
    # If not set the default locations for on-premise or CVaaS will be used.
    # See cvp_ingestauth_key for details.
    cvp_token_file: <str>
    terminattr_disable_aaa: <bool; default=False>
    terminattr_ingestexclude: <str; default="/Sysdb/cell/1/agent,/Sysdb/cell/2/agent">

    # Port number used for Terminattr connection to an on-premise CloudVision cluster.
    # The port number is always 443 when using CloudVision as a Service, so this value is ignored.
    terminattr_ingestgrpcurl_port: <int; default=9910>
    terminattr_smashexcludes: <str; default="ale,flexCounter,hardware,kni,pulse,strata">
    ```
