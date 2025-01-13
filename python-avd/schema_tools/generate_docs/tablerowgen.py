# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel

from .utils import render_schema_field

if TYPE_CHECKING:
    from collections.abc import Generator

    from schema_tools.metaschema.meta_schema_model import AvdSchemaField

LEGACY_OUTPUT = False


class TableRow(BaseModel):
    """
    Dataclass for one table row.

    Content is markdown formatted so it can be rendered directly.
    """

    key: str
    type: str
    required: str | None = None
    default: str | None = None
    restrictions: str | None = None
    description: str | None = None

    def __str__(self) -> str:
        return f"| {self.key} | {self.type} | {self.required or ''} | {self.default or ''} | {self.restrictions or ''} | {self.description or ''} |"


class TableRowGenBase:
    """
    Base class to be used with schema pydantic models.

    Provides the method "generate_table_rows" used to build schema documentation tables.

    Sub-classed per schema type to generate type-specific documentation.
    """

    def generate_table_rows(
        self,
        schema: AvdSchemaField,
        target_table: str | None = None,
    ) -> Generator[TableRow]:
        """
        Yields TableRow for this schema field if the field is part of the given target_table.

        Recursively walks children if applicable (only for lists and dicts)
        """
        self.schema = schema
        self.target_table = target_table

        # The render_schema_field function contains all the logic to device whether this field should be part of the target_table or not.
        if render_schema_field(schema, target_table):
            if schema._path:
                # Only render this field when there is a path (not the root dict), but always render children.

                yield TableRow(
                    key=self.render_key(),
                    type=self.render_type(),
                    required=self.render_required(),
                    default=self.render_default(),
                    restrictions=self.render_restrictions(),
                    description=self.render_description(),
                )

            yield from self.render_children()

    def get_indentation(self) -> str:
        """
        Indentation is two spaces for dicts and 4 spaces for lists (so the hyphen will be indented 2).

        For the variable {"my":{"random":{"list":[<str>]}}} the schema._path would be ["my", "random", "list", []].
        The indentation would be 4*2-2+2 = 8 spaces. Since all items are simple values (not a dict with keys)
        we replace the second to last space with a hyphen for yaml style lists.

        For the variable {"my":{"random":{"list":[{"key": <value>}]}}} the schema._path would be ["my", "random", "list", [], "key"].
        The indentation would be 5*2-2 = 8 spaces.
        For the first key in the dict we replace the second to last space with a hyphen for yaml style lists.
        """
        indentation_count = len(self.schema._path) * 2 - 2
        if not self.schema._key:
            # this is a flat list item so path is one shorter than for dict. So we add 2 to the indentation
            indentation_count += 2

        i = "&nbsp;"  # Indentation character
        if self.schema._is_first_list_key:
            # TODO: Remove legacy output
            if LEGACY_OUTPUT:
                return i * (indentation_count - 2) + "-" + " "  # Using space as last indentation to match legacy behavior

            return i * (indentation_count - 2) + "-" + i

        return i * indentation_count

    def get_deprecation_label(self) -> str | None:
        """Returns None or a markdown formatted colored string with the deprecation status."""
        if self.schema.deprecation is None:
            return ""

        label = "removed" if self.schema.deprecation.removed else "deprecated"

        return f' <span style="color:red">{label}</span>'

    def get_deprecation_description(self) -> str | None:
        """Returns None or a markdown formatted colored string with the deprecation description."""
        if self.schema.deprecation is None:
            return None

        descriptions = []
        if self.schema.deprecation.removed:
            descriptions.append("This key was removed.")
            removed_verb = "was"
        else:
            descriptions.append("This key is deprecated.")
            removed_verb = "will be"

        if self.schema.deprecation.remove_in_version:
            descriptions.append(f"Support {removed_verb} removed in AVD version {self.schema.deprecation.remove_in_version}.")
        elif self.schema.deprecation.remove_after_date:
            descriptions.append(f"Support {removed_verb} removed in the first major AVD version released after {self.schema.deprecation.remove_after_date}.")
        elif self.schema.deprecation.removed:
            descriptions.append("Support was removed in AVD.")

        if self.schema.deprecation.new_key:
            descriptions.append(f"Use <samp>{self.schema.deprecation.new_key}</samp> instead.")

        if self.schema.deprecation.url:
            descriptions.append(f"See [here]({self.schema.deprecation.url}) for details.")

        description = " ".join(descriptions)
        return f'<span style="color:red">{description}</span>'

    def render_key(self) -> str:
        """Renders markdown for "key" field including mouse-over and deprecation label with color."""
        path = ".".join(self.schema._path)

        if self.schema._key:
            key = self.schema._key.replace("<", "&lt;").replace(">", "&gt;")
        else:
            key = f"&lt;{self.schema.type}&gt;"

            # TODO: Remove legacy output
            if LEGACY_OUTPUT:
                path += f".{key}"

        if LEGACY_OUTPUT:
            path = path.replace("<", "&lt;").replace(">", "&gt;")

        return f'[<samp>{self.get_indentation()}{key}</samp>](## "{path}"){self.get_deprecation_label()}'

    def render_type(self) -> str:
        """Renders markdown for "type" field."""
        type_converters = {
            "str": "String",
            "int": "Integer",
            "bool": "Boolean",
            "dict": "Dictionary",
            "list": "List",
        }
        return type_converters[self.schema.type]

    def render_required(self) -> str | None:
        """Render markdown for "required" field."""
        if self.schema._is_primary_key or self.schema.required:
            return "Required, Unique" if self.schema._is_unique else "Required"
        return None

    def render_default(self) -> str | None:
        """Should render markdown for "default" field."""
        if self.schema.default is not None:
            if isinstance(self.schema.default, (list, dict)) and (len(self.schema.default) > 1 or len(str(self.schema.default)) > 40):
                return "See (+) on YAML tab"

            return f"`{self.schema.default}`"
        return None

    def render_description(self) -> str | None:
        """Renders markdown for "description" field including deprecation text with color."""
        descriptions = []
        if self.schema.description:
            descriptions.append(self.schema.description.replace("\n", "<br>"))

        if deprecation := self.get_deprecation_description():
            descriptions.append(deprecation)

        return "".join(descriptions) or None

    def render_children(self) -> Generator[TableRow]:
        """Noop for classes without children. Override in subclasses for dict and list."""
        yield from []

    def render_restrictions(self) -> str | None:
        """Renders markdown for "restrictions" field as a multiline text compatible with a markdown table cell."""
        return "<br>".join(self.get_restrictions()) or None

    def get_restrictions(self) -> list:
        """
        Returns a list of field restrictions to be rendered in the docs.

        Only covers generic restrictions. Should be overridden in type specific subclasses.
        """
        restrictions = []
        valid_values = []
        if getattr(self.schema, "dynamic_valid_values", None):
            valid_values.extend(f"<value(s) of {dynamic_valid_value}>" for dynamic_valid_value in self.schema.dynamic_valid_values)

        if getattr(self.schema, "valid_values", None):
            valid_values.extend(self.schema.valid_values)

        if valid_values:
            restrictions.append("Valid Values:")
            # TODO: Remove legacy output
            if LEGACY_OUTPUT:
                restrictions.extend(f"- {valid_value}" for valid_value in valid_values)
            else:
                restrictions.extend(f"- <code>{valid_value}</code>" for valid_value in valid_values)

        return restrictions


class TableRowGenBool(TableRowGenBase):
    pass


class TableRowGenInt(TableRowGenBase):
    def get_restrictions(self) -> list:
        """
        Returns a list of field restrictions to be rendered in the docs.

        Leverages common restrictions from base class.
        """
        restrictions = []
        if self.schema.min is not None:
            restrictions.append(f"Min: {self.schema.min}")
        if self.schema.max is not None:
            restrictions.append(f"Max: {self.schema.max}")

        restrictions.extend(super().get_restrictions())

        return restrictions


class TableRowGenStr(TableRowGenBase):
    def get_restrictions(self) -> list:
        """
        Returns a list of field restrictions to be rendered in the docs.

        Leverages common restrictions from base class.
        """
        restrictions = []
        if self.schema.min_length is not None:
            restrictions.append(f"Min Length: {self.schema.min_length}")
        if self.schema.max_length is not None:
            restrictions.append(f"Max Length: {self.schema.max_length}")
        if self.schema.format is not None:
            restrictions.append(f"Format: {self.schema.format}")
        if self.schema.convert_to_lower_case:
            # TODO: Remove legacy output
            if LEGACY_OUTPUT:
                restrictions.append("Value is converted to lower case")
            else:
                restrictions.append("Value is converted to lower case.")

        restrictions.extend(super().get_restrictions())

        if self.schema.pattern is not None:
            restrictions.append(f"Pattern: `{self.schema.pattern}`")

        return restrictions


class TableRowGenList(TableRowGenBase):
    def render_type(self) -> str:
        """Renders markdown for "type" field."""
        type_converters = {
            "str": "String",
            "int": "Integer",
            "bool": "Boolean",
            "dict": "Dictionary",
            "list": "List",
        }
        field_type = type_converters[self.schema.type]
        if self.schema.items:
            field_type += f", items: {type_converters[self.schema.items.type]}"

        return field_type

    def get_restrictions(self) -> list:
        """
        Returns a list of field restrictions to be rendered in the docs.

        Leverages common restrictions from base class.
        """
        restrictions = []
        if self.schema.min_length is not None:
            restrictions.append(f"Min Length: {self.schema.min_length}")
        if self.schema.max_length is not None:
            restrictions.append(f"Max Length: {self.schema.max_length}")

        restrictions.extend(super().get_restrictions())

        return restrictions

    def render_children(self) -> Generator[TableRow]:
        """Yields TableRow from each child class."""
        if not self.schema.items:
            return

        if getattr(self.schema.items, "keys", None):
            for child_schema in self.schema.items.keys.values():
                yield from child_schema._generate_table_rows(
                    target_table=self.target_table,
                )
        else:
            yield from self.schema.items._generate_table_rows(
                target_table=self.target_table,
            )


class TableRowGenDict(TableRowGenBase):
    def render_children(self) -> Generator[TableRow]:
        """Yields TableRow from each child class."""
        if self.schema.documentation_options and self.schema.documentation_options.hide_keys:
            # Skip generating table fields for children, if "hide_keys" is set.
            return

        if self.schema.dynamic_keys:
            for child_schema in self.schema.dynamic_keys.values():
                yield from child_schema._generate_table_rows(
                    target_table=self.target_table,
                )

        if self.schema.keys:
            for child_schema in self.schema.keys.values():
                yield from child_schema._generate_table_rows(
                    target_table=self.target_table,
                )
