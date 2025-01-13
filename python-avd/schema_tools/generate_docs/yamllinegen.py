# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from textwrap import indent
from typing import TYPE_CHECKING

import yaml
from pydantic import BaseModel

from .utils import render_schema_field

if TYPE_CHECKING:
    from collections.abc import Generator

    from schema_tools.metaschema.meta_schema_model import AvdSchemaField

LEGACY_OUTPUT = False


class YamlLine(BaseModel):
    """
    Dataclass for one YAML line (and any associated descriptions).

    Content of line is yaml formatted so it should be rendered in a code block.
    The field may need an mkdocs code block annotation link to show large default values.
    If so the content of the annotation is stored in the 'annotation' attribute.

    Since annotation numbers must be tracked across all yaml lines, it is up to the caller
    to provide the annotation number at rendering time.

    The annotation link can be rendered with .render_annotation_link(annotation_number).
    The annotation foot note can be rendered with .render_annotation(annotation_number).
    """

    line: str
    annotation: str | None = None

    def __str__(self) -> str:
        return self.line

    def render_annotation(self, annotation_number: int) -> str:
        """
        Returns markdown for annotation foot note, providing the contents of mkdocs code block annotation popup.

        Like below (including the leading blank line):

        1. Default Value

            ```yaml
            default: "one"
            values: 2
            ```
        """
        if self.annotation is None:
            return ""
        annotation_codeblock = f"```yaml\n{self.annotation}```"
        return f"\n{annotation_number}. Default Value\n\n{indent(annotation_codeblock, '    ')}\n"

    def render_annotation_link(self, annotation_number: int) -> str:
        """
        Returns codeblock comment used for mkdocs codeblock annotations.

        Like: " # (123)!"
        """
        return "" if self.annotation is None else f" # ({annotation_number})!"


class YamlLineGenBase:
    """
    Base class to be used with schema pydantic models.

    Provides the method "generate_yaml_lines" to build documentation tables.
    """

    def generate_yaml_lines(
        self,
        schema: AvdSchemaField,
        target_table: str | None = None,
    ) -> Generator[YamlLine]:
        self.schema = schema
        self.target_table = target_table

        if self.is_removed:
            # Skip removed keys from YAML
            return

        if render_schema_field(schema, target_table):
            if schema._path:
                # Only render this field when there is a path (not the root dict), but always render children.

                # TODO: Remove legacy output
                if not LEGACY_OUTPUT:
                    yield from self.render_description()
                    yield from self.render_deprecation_description()

                yield from self.render_field()

            yield from self.render_children()

    def get_indentation(self, *, honor_first_list_key: bool = True) -> str:
        """Indentation is two spaces for dicts and 4 spaces for lists (so the hyphen will be indented 2)."""
        indentation_count = len(self.schema._path) * 2 - 2
        if not self.schema._key:
            # this is a flat list item so path is one shorter than for dict. So we add 2 to the indentation
            indentation_count += 2

        i = " "  # Indentation character
        if self.schema._is_first_list_key and honor_first_list_key:
            return (i * (indentation_count - 2)) + "-" + i

        return i * indentation_count

    @property
    def is_removed(self) -> bool:
        return self.schema.deprecation and self.schema.deprecation.removed

    def render_field(self) -> Generator[YamlLine]:
        """Renders YamlLines for this field including description."""
        # Build semicolon separated list of field properties.
        value_fields = [
            self.schema.type,
            self.render_restrictions(),
            self.get_default(),
            self.get_required(),
        ]
        # TODO: Remove legacy output
        value = self.schema.type if LEGACY_OUTPUT else "; ".join(field for field in value_fields if field)

        key = f"{self.schema._key}: " if self.schema._key else ""

        yield YamlLine(
            line=f"{self.get_indentation()}{key}<{value}>",
            annotation=self.get_annotation(),
        )

    def render_description(self) -> Generator[YamlLine]:
        """Yields YamlLine with description for this field."""
        if self.schema.description:
            indentation = self.get_indentation(honor_first_list_key=False)
            description = indent(self.schema.description.strip(), f"{indentation}# ")
            # Insert # with no extra whitespace for blank lines.
            description = indent(description, f"{indentation}#", lambda line: line == "\n")
            yield YamlLine(line=f"\n{description}")

    def render_deprecation_description(self) -> Generator[YamlLine]:
        """Yields YamlLine with deprecation description for this field."""
        if self.schema.deprecation is None:
            return

        descriptions = ["This key is deprecated."]

        if self.schema.deprecation.remove_in_version:
            descriptions.append(f"Support will be removed in AVD version {self.schema.deprecation.remove_in_version}.")
        elif self.schema.deprecation.remove_after_date:
            descriptions.append(f"Support will be removed in the first major AVD version released after {self.schema.deprecation.remove_after_date}.")

        if self.schema.deprecation.new_key:
            descriptions.append(f"Use <samp>{self.schema.deprecation.new_key}</samp> instead.")

        if self.schema.deprecation.url:
            descriptions.append(f"See [here]({self.schema.deprecation.url}) for details.")

        indentation = self.get_indentation(honor_first_list_key=False)
        description = indent("\n".join(descriptions), f"{indentation}# ")
        yield YamlLine(line=description)

    def get_required(self) -> str | None:
        """Returns "required", "required; unique" or None depending on self.schema.required and self.is_primary_key."""
        if self.schema._is_primary_key or self.schema.required:
            return "required; unique" if self.schema._is_unique else "required"
        return None

    @property
    def needs_annotation_for_default_value(self) -> bool:
        """
        Determines if this field should use a mkdocs codeblock annotation / popup to display the default value.

        Is true for list or dict with length above 1. Otherwise false.
        """
        return (
            self.schema.default is not None
            and isinstance(self.schema.default, (list, dict))
            and (len(self.schema.default) > 1 or len(str(self.schema.default)) > 40)
        )

    def get_default(self) -> str | None:
        """
        Returns default value or None.

        For list or dict with len > 1 it will return none.
        See get_default_popup.
        """
        if self.schema.default is not None and not self.needs_annotation_for_default_value:
            if self.schema.type == "str":
                # Add quotes to string default value.
                return f'default="{self.schema.default}"'
            return f"default={self.schema.default}"
        return None

    def get_annotation(self) -> str | None:
        if self.needs_annotation_for_default_value:
            return yaml.dump({self.schema._key: self.schema.default}, indent=2)
        return None

    def render_restrictions(self) -> str | None:
        """Returns restrictions as inline semicolon separated strings."""
        return "; ".join(self.get_restrictions()) or None

    def get_restrictions(self) -> list:
        """
        Returns a list of restrictions.

        Only covers generic restrictions. Should be overridden in type specific subclasses.
        """
        restrictions = []
        valid_values = []
        if getattr(self.schema, "dynamic_valid_values", None):
            valid_values.extend(f"<value(s) of {dynamic_valid_value}>" for dynamic_valid_value in self.schema.dynamic_valid_values)

        if getattr(self.schema, "valid_values", None):
            valid_values.extend(self.schema.valid_values)

        if valid_values:
            if self.schema.type == "str":
                # Add quotes around string values.
                valid_values = [f'"{valid_value}"' for valid_value in valid_values]
            else:
                valid_values = [str(valid_value) for valid_value in valid_values]

            restrictions.append(" | ".join(valid_values))

        return restrictions

    def render_children(self) -> Generator[YamlLine]:
        """Noop for classes without children. Override in subclasses for dict and list."""
        yield from []


class YamlLineGenBool(YamlLineGenBase):
    pass


class YamlLineGenInt(YamlLineGenBase):
    def get_restrictions(self) -> list:
        """
        Returns a list of restrictions.

        Leverages common restrictions from base class.
        """
        restrictions = []
        if self.schema.min is not None or self.schema.max is not None:
            if self.schema.min is not None and self.schema.max is not None:
                restrictions.append(f"{self.schema.min}-{self.schema.max}")
            elif self.schema.min is not None:
                restrictions.append(f">={self.schema.min}")
            elif self.schema.max is not None:
                restrictions.append(f"<={self.schema.max}")

        restrictions.extend(super().get_restrictions())

        return restrictions


class YamlLineGenStr(YamlLineGenBase):
    def get_restrictions(self) -> list:
        """
        Returns a list of restrictions.

        Leverages common restrictions from base class.
        """
        restrictions = []
        if self.schema.min_length is not None or self.schema.max_length is not None:
            if self.schema.min_length is not None and self.schema.max_length is not None:
                restrictions.append(f"length {self.schema.min_length}-{self.schema.max_length}")
            elif self.schema.min_length is not None:
                restrictions.append(f"length >={self.schema.min_length}")
            elif self.schema.max_length is not None:
                restrictions.append(f"length <={self.schema.max_length}")

        restrictions.extend(super().get_restrictions())

        return restrictions


class YamlLineGenList(YamlLineGenBase):
    def render_field(self) -> Generator[YamlLine]:
        """Renders YamlLine for this field."""
        # Build semicolon separated list of field properties.
        properties_fields = [
            self.render_restrictions(),
            self.get_default(),
            self.get_required(),
        ]
        properties = "; ".join(field for field in properties_fields if field)
        if properties:
            properties = f" # {properties}"

        # TODO: Remove legacy output
        if LEGACY_OUTPUT:
            properties = ""

        if self.schema.items is None:
            # Add <list> when we don't have the items schema.
            properties = f" <list>{properties}"

        yield YamlLine(
            line=f"{self.get_indentation()}{self.schema._key}:{properties}",
            annotation=self.get_annotation(),
        )

    def get_restrictions(self) -> list:
        """
        Returns a list of restrictions.

        Leverages common restrictions from base class.
        """
        restrictions = []
        if self.schema.min_length is not None or self.schema.max_length is not None:
            if self.schema.min_length is not None and self.schema.max_length is not None:
                restrictions.append(f"{self.schema.min_length}-{self.schema.max_length} items")
            elif self.schema.min_length is not None:
                restrictions.append(f">={self.schema.min_length} items")
            elif self.schema.max_length is not None:
                restrictions.append(f"<={self.schema.max_length} items")

        restrictions.extend(super().get_restrictions())

        return restrictions

    def render_children(self) -> Generator[YamlLine]:
        """Yields TableRow from each child class."""
        if not self.schema.items:
            return

        if getattr(self.schema.items, "keys", None):
            for child_schema in self.schema.items.keys.values():
                yield from child_schema._generate_yaml_lines(
                    target_table=self.target_table,
                )
        else:
            yield from self.schema.items._generate_yaml_lines(
                target_table=self.target_table,
            )


class YamlLineGenDict(YamlLineGenBase):
    def render_field(self) -> Generator[YamlLine]:
        """Renders YamlLine for this field."""
        # Build semicolon separated list of field properties.
        properties_fields = [
            self.render_restrictions(),
            self.get_default(),
            self.get_required(),
        ]
        properties = "; ".join(field for field in properties_fields if field)
        if properties:
            properties = f" # {properties}"

        # TODO: Remove legacy output
        if LEGACY_OUTPUT:
            properties = ""

        if not self.schema.keys or (self.schema.documentation_options and self.schema.documentation_options.hide_keys):
            # Add <dict> when we don't generate yaml for child keys.
            properties = f" <dict>{properties}"

        key = f"{self.schema._key}:" if self.schema._key else ""

        yield YamlLine(
            line=f"{self.get_indentation()}{key}{properties}",
            annotation=self.get_annotation(),
        )

    def render_children(self) -> Generator[YamlLine]:
        """Yields TableRow from each child class."""
        if self.schema.documentation_options and self.schema.documentation_options.hide_keys:
            # Skip generating table fields for children, if "hide_keys" is set.
            return

        if self.schema.dynamic_keys:
            for child_schema in self.schema.dynamic_keys.values():
                yield from child_schema._generate_yaml_lines(
                    target_table=self.target_table,
                )

        if self.schema.keys:
            for child_schema in self.schema.keys.values():
                yield from child_schema._generate_yaml_lines(
                    target_table=self.target_table,
                )
