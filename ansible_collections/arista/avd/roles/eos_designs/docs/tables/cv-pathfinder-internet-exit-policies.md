<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cv_pathfinder_internet_exit_policies</samp>](## "cv_pathfinder_internet_exit_policies") | List, items: Dictionary |  |  |  | PREVIEW: These keys are in preview mode.<br><br>List of internet-exit policies used for the WAN configuration. |
    | [<samp>&nbsp;&nbsp;-&nbsp;name</samp>](## "cv_pathfinder_internet_exit_policies.[].name") | String | Required, Unique |  |  | Internet-exit policy name. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "cv_pathfinder_internet_exit_policies.[].type") | String | Required |  | Valid Values:<br>- <code>direct</code><br>- <code>zscaler</code> | Internet-exit policy type.<br>direct: Exit directly over wan interfaces<br>zscaler: Exit using Zscaler secure web gateway service |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;fallback_to_system_default</samp>](## "cv_pathfinder_internet_exit_policies.[].fallback_to_system_default") | Boolean |  | `True` |  | Add system default exit-group at the end of the policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;zscaler</samp>](## "cv_pathfinder_internet_exit_policies.[].zscaler") | Dictionary |  |  |  | Zscaler information. Only used if `type` is 'zscaler'. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ipsec_key_salt</samp>](## "cv_pathfinder_internet_exit_policies.[].zscaler.ipsec_key_salt") | String | Required |  |  | "Salt" used for auto generation of encryption keys for IPsec tunnels to Zscaler.<br>The keys will be generated as a hash of `salt_<hostname>_<policy_name>`.<br>Since this salt can be used to deduct the encryption key, it is recommended to use vault. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;domain_name</samp>](## "cv_pathfinder_internet_exit_policies.[].zscaler.domain_name") | String | Required |  |  | Domain name as configured in Zscaler for the tenant. Used as UFQDN suffix for authentication. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;encrypt_traffic</samp>](## "cv_pathfinder_internet_exit_policies.[].zscaler.encrypt_traffic") | Boolean |  | `True` |  | When `true` the traffic going over the tunnels will be encrypted with AES-256-GCM. Otherwise the traffic will be using NULL encryption.<br>Note that encryption requires a subscription on the Zscaler account. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;download_bandwidth</samp>](## "cv_pathfinder_internet_exit_policies.[].zscaler.download_bandwidth") | Integer |  |  |  | Maximum allowed download bandwidth in Mbps for each device using this policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;upload_bandwidth</samp>](## "cv_pathfinder_internet_exit_policies.[].zscaler.upload_bandwidth") | Integer |  |  |  | Maximum allowed upload bandwidth in Mbps for each device using this policy. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;firewall</samp>](## "cv_pathfinder_internet_exit_policies.[].zscaler.firewall") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "cv_pathfinder_internet_exit_policies.[].zscaler.firewall.enabled") | Boolean |  | `False` |  | Enforce firewall controls. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ips</samp>](## "cv_pathfinder_internet_exit_policies.[].zscaler.firewall.ips") | Boolean |  | `False` |  | Enable IPS Controls for the firewall. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;acceptable_use_policy</samp>](## "cv_pathfinder_internet_exit_policies.[].zscaler.acceptable_use_policy") | Boolean |  | `False` |  | Display an Acceptable Use Policy (AUP) and require users to accept it. |

=== "YAML"

    ```yaml
    # PREVIEW: These keys are in preview mode.
    #
    # List of internet-exit policies used for the WAN configuration.
    cv_pathfinder_internet_exit_policies:

        # Internet-exit policy name.
      - name: <str; required; unique>

        # Internet-exit policy type.
        # direct: Exit directly over wan interfaces
        # zscaler: Exit using Zscaler secure web gateway service
        type: <str; "direct" | "zscaler"; required>

        # Add system default exit-group at the end of the policy.
        fallback_to_system_default: <bool; default=True>

        # Zscaler information. Only used if `type` is 'zscaler'.
        zscaler:

          # "Salt" used for auto generation of encryption keys for IPsec tunnels to Zscaler.
          # The keys will be generated as a hash of `salt_<hostname>_<policy_name>`.
          # Since this salt can be used to deduct the encryption key, it is recommended to use vault.
          ipsec_key_salt: <str; required>

          # Domain name as configured in Zscaler for the tenant. Used as UFQDN suffix for authentication.
          domain_name: <str; required>

          # When `true` the traffic going over the tunnels will be encrypted with AES-256-GCM. Otherwise the traffic will be using NULL encryption.
          # Note that encryption requires a subscription on the Zscaler account.
          encrypt_traffic: <bool; default=True>

          # Maximum allowed download bandwidth in Mbps for each device using this policy.
          download_bandwidth: <int>

          # Maximum allowed upload bandwidth in Mbps for each device using this policy.
          upload_bandwidth: <int>
          firewall:

            # Enforce firewall controls.
            enabled: <bool; default=False>

            # Enable IPS Controls for the firewall.
            ips: <bool; default=False>

          # Display an Acceptable Use Policy (AUP) and require users to accept it.
          acceptable_use_policy: <bool; default=False>
    ```
