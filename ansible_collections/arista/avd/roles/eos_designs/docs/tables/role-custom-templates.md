<!--
  ~ Copyright (c) 2025 Arista Networks, Inc.
  ~ Use of this source code is governed by the Apache License 2.0
  ~ that can be found in the LICENSE file.
  -->
=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>eos_designs_custom_templates</samp>](## "eos_designs_custom_templates") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;-&nbsp;template</samp>](## "eos_designs_custom_templates.[].template") | String | Required |  |  | Template file. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;options</samp>](## "eos_designs_custom_templates.[].options") | Dictionary |  |  |  | Template options. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;list_merge</samp>](## "eos_designs_custom_templates.[].options.list_merge") | String |  | `append_rp` |  | Merge strategy for lists. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;strip_empty_keys</samp>](## "eos_designs_custom_templates.[].options.strip_empty_keys") | Boolean |  | `True` |  | Filter out keys from the generated output if value is null/none/undefined. |

=== "YAML"

    ```yaml
    eos_designs_custom_templates:

        # Template file.
      - template: <str; required>

        # Template options.
        options:

          # Merge strategy for lists.
          list_merge: <str; default="append_rp">

          # Filter out keys from the generated output if value is null/none/undefined.
          strip_empty_keys: <bool; default=True>
    ```
