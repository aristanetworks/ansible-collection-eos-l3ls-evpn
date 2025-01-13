<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>cv_server</samp>](## "cv_server") | String |  |  |  | PREVIEW: These keys are in preview mode.<br><br>Hostname or IP address of CloudVision host. Ex. "www.arista.io" for CVaaS.<br>For `eos_designs` this variable is only used for the WAN Internet-exit integration with Zscaler.<br>The same variable name is also used by the `cv_deploy` role, and will override the value of `ansible_host` on inventory 'cloudvision' host.<br>Make sure to set it in a common group_vars file. |
    | [<samp>cv_token</samp>](## "cv_token") | String |  |  |  | PREVIEW: These keys are in preview mode.<br><br>Service account token as defined on CloudVision. This value should be using Ansible Vault.<br>For `eos_designs` this variable is only used for the WAN Internet-exit integration with Zscaler.<br>The same variable name is also used by the `cv_deploy` role, and will override the value of `ansible_password` on inventory 'cloudvision' host.<br>Make sure to set it in a common group_vars file. |

=== "YAML"

    ```yaml
    # PREVIEW: These keys are in preview mode.
    #
    # Hostname or IP address of CloudVision host. Ex. "www.arista.io" for CVaaS.
    # For `eos_designs` this variable is only used for the WAN Internet-exit integration with Zscaler.
    # The same variable name is also used by the `cv_deploy` role, and will override the value of `ansible_host` on inventory 'cloudvision' host.
    # Make sure to set it in a common group_vars file.
    cv_server: <str>

    # PREVIEW: These keys are in preview mode.
    #
    # Service account token as defined on CloudVision. This value should be using Ansible Vault.
    # For `eos_designs` this variable is only used for the WAN Internet-exit integration with Zscaler.
    # The same variable name is also used by the `cv_deploy` role, and will override the value of `ansible_password` on inventory 'cloudvision' host.
    # Make sure to set it in a common group_vars file.
    cv_token: <str>
    ```
