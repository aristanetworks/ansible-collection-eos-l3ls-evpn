# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

"""
Generate AvdSchema documentation.

"mdtabsgen.py" generates a markdown file with mkdocs tabs for one given "table name":
- Markdown table representing the schema using "tablegen.py":
  - Generates table rows by recursively walking the schema with the relevant TableRowGen<type>
- YAML code block representing the schema using "yamlgen.py"
  - Generates YAML lines by recursively walking the schema with the relevant YamlLineGen<type>
"""
