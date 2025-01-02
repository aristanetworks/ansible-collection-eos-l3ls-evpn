<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>avd_eos_designs_debug</samp>](## "avd_eos_designs_debug") | Boolean |  | `False` |  | Dump all vars and facts per device after generating `avd_switch_facts`. |
    | [<samp>avd_eos_designs_structured_config</samp>](## "avd_eos_designs_structured_config") | Boolean |  | `True` |  | Generate structured configuration per device. |
    | [<samp>avd_eos_designs_unset_facts</samp>](## "avd_eos_designs_unset_facts") | Boolean |  | `True` |  | Unset `avd_switch_facts` to gain a small performance improvement since Ansible needs to handle fewer variables. |
    | [<samp>eos_designs_documentation</samp>](## "eos_designs_documentation") | Dictionary |  |  |  | Control fabric documentation generation.<br> |
    | [<samp>&nbsp;&nbsp;enable</samp>](## "eos_designs_documentation.enable") | Boolean |  | `True` |  | Generate fabric-wide documentation. |
    | [<samp>&nbsp;&nbsp;connected_endpoints</samp>](## "eos_designs_documentation.connected_endpoints") | Boolean |  | `False` |  | Include connected endpoints in the fabric-wide documentation.<br>This is `false` by default to avoid cluttering documentation for projects with thousands of endpoints. |
    | [<samp>&nbsp;&nbsp;topology_csv</samp>](## "eos_designs_documentation.topology_csv") | Boolean |  | `False` |  | Generate Topology CSV with all interfaces towards other devices. |
    | [<samp>&nbsp;&nbsp;p2p_links_csv</samp>](## "eos_designs_documentation.p2p_links_csv") | Boolean |  | `False` |  | Generate P2P links CSV with all routed point-to-point links between devices. |

=== "YAML"

    ```yaml
    # Dump all vars and facts per device after generating `avd_switch_facts`.
    avd_eos_designs_debug: <bool; default=False>

    # Generate structured configuration per device.
    avd_eos_designs_structured_config: <bool; default=True>

    # Unset `avd_switch_facts` to gain a small performance improvement since Ansible needs to handle fewer variables.
    avd_eos_designs_unset_facts: <bool; default=True>

    # Control fabric documentation generation.
    eos_designs_documentation:

      # Generate fabric-wide documentation.
      enable: <bool; default=True>

      # Include connected endpoints in the fabric-wide documentation.
      # This is `false` by default to avoid cluttering documentation for projects with thousands of endpoints.
      connected_endpoints: <bool; default=False>

      # Generate Topology CSV with all interfaces towards other devices.
      topology_csv: <bool; default=False>

      # Generate P2P links CSV with all routed point-to-point links between devices.
      p2p_links_csv: <bool; default=False>
    ```
