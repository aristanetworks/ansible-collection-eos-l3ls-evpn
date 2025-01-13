# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from schema_tools.metaschema.meta_schema_model import AristaAvdSchema


def get_yaml(schema: AristaAvdSchema, target_table: str | None = None) -> str:
    """
    Returns one markdown codeblock with YAML either containing all keys of the given schema or only a subset if "target_table" is set.

    Also adds foot notes for use with mkdocs codeblock annotations as required.
    """
    lines = []
    annotations = []
    for yamlline in schema._generate_yaml_lines(target_table=target_table):
        if yamlline.annotation:
            annotation_number = len(annotations) + 1
            annotations.append(yamlline.render_annotation(annotation_number))
            lines.append(f"{yamlline.line}{yamlline.render_annotation_link(annotation_number)}")
        else:
            lines.append(yamlline.line)
    lines.append("")  # Add final newline
    yaml = "\n".join(lines).strip()
    markdown = f"```yaml\n{yaml}\n```\n"
    if annotations:
        markdown += "".join(annotations)
    return markdown
