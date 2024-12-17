# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
This module provides Pydantic models (classes) representing the meta-schema of the AVD Schema.

Each variable in the schema is called a field, and for each type of field we have a corresponding Pydantic model:
- AvdSchemaInt
- AvdSchemaBool
- AvdSchemaStr
- AvdSchemaList
- AvdSchemaDict

The alias "AvdSchemaField" is a union of all the models above, and can be used as an easy type hint for any field type.

All the type-specific Pydantic models inherit the common base class "AvdSchemaBaseModel", and have local overrides
as needed. For example, only "AvdSchemaList" and "AvdSchemaDict" need to parse child fields.

The overall schema is covered by the class "AristaAvdSchema" which inherits from "AvdSchemaDict" since the root of the schema is a dict.
"""

from __future__ import annotations

import logging
from abc import ABC
from enum import Enum
from functools import cached_property
from typing import TYPE_CHECKING, Annotated, Any, ClassVar, Literal

from pydantic import BaseModel, ConfigDict, Field, constr

from schema_tools.generate_classes.class_src_gen import SrcGenBase, SrcGenBool, SrcGenDict, SrcGenInt, SrcGenList, SrcGenRootDict, SrcGenStr
from schema_tools.generate_docs.tablerowgen import TableRow, TableRowGenBase, TableRowGenBool, TableRowGenDict, TableRowGenInt, TableRowGenList, TableRowGenStr
from schema_tools.generate_docs.yamllinegen import YamlLine, YamlLineGenBase, YamlLineGenBool, YamlLineGenDict, YamlLineGenInt, YamlLineGenList, YamlLineGenStr

from .resolvemodel import merge_schema_from_ref

if TYPE_CHECKING:
    from collections.abc import Generator

    from schema_tools.generate_classes.src_generators import SrcData

LOGGER = logging.getLogger(__name__)

KEY_PATTERN = r"^[a-z][a-z0-9_]*$"
"""Common pattern to match legal key strings"""


class AvdSchemaBaseModel(BaseModel, ABC):
    """
    Base class for AvdSchema fields.

    Contains nested models and common fields that applies to all subclasses.

    Also covers internal attributes and methods used for documentation generation.
    All these are prefixed with underscore.
    """

    # Common nested models used by common fields
    class Deprecation(BaseModel):
        """Deprecation settings."""

        warning: bool = True
        """Emit deprecation warning if key is set."""
        new_key: str | None = None
        """Relative path to new key."""
        removed: bool | None = False
        """Support for this key has been removed."""
        remove_in_version: str | None = None
        """Version in which the key will be removed."""
        remove_after_date: str | None = None
        """Date after which the key will be removed in the next major version."""
        url: str | None = None
        """URL detailing the deprecation and migration guidelines."""

    class DocumentationOptions(BaseModel):
        """Schema field options used for controlling documentation generation."""

        # Pydantic config option to forbid keys in the inputs that are not covered by the model
        model_config = ConfigDict(extra="forbid")

        table: str | None = None
        """
        Setting 'table' will allow for custom grouping of schema fields in the documentation.
        By default each root key has it's own table. By setting the same table-value on multiple keys, they will be merged to a single table.
        If 'table' is set on a 'child' key, all 'ancestor' keys are automatically included in the table so the full path is visible.
        The 'table' option is inherited to all child keys, unless specifically set on the child.
        """

    # Pydantic config option to forbid keys in the inputs that are not covered by the model
    model_config = ConfigDict(extra="forbid")

    # Common field properties
    display_name: str | None = Field(None, pattern=r"^[^\n]+$")
    """Free text display name for forms and documentation (single line)"""
    description: Annotated[str, constr(min_length=1)] | None = None
    """Free text description for forms and documentation (multi-line)"""
    required: bool | None = None
    """Key is required"""
    deprecation: Deprecation | None = None
    field_ref: str | None = Field(None, alias="$ref")
    """
    Reference to Sub Schema using JSON Path.
    Example 'eos_designs#/keys/mykey' will resolve the schema for 'mykey' under the root dictionary of the eos_designs schema.
    """
    documentation_options: DocumentationOptions | None = None
    """Schema field options used for controlling documentation generation"""

    # Type of schema docs generators to use for this schema field.
    _table_row_generator: type[TableRowGenBase]
    _yaml_line_generator: type[YamlLineGenBase]
    # Type of class source generator to use for this schema field.
    _class_src_generator: type[SrcGenBase]

    # Internal attributes used by schema docs generators
    _key: str | None = None
    _parent_schema: AvdSchemaField | None = None
    _is_primary_key: bool = False
    """
    Primary keys are always included in the documentation tables if any other key of the same dict is present.
    """
    _is_unique: bool = False
    """
    Key values must be unique. This is set on ancestor list schemas
    """
    _is_first_list_key: bool = False
    """
    Simple types or the first key of a dict contained in a list will be rendered with a hyphen as part of the indentation.
    """

    # Signal to __init__ if the $ref in the schema should be resolved before initializing the pydantic model.
    _resolve_schema: ClassVar[Literal["eos_designs", "eos_cli_config_gen", "all"] | None] = "all"

    def __init__(self, _resolve_schema: Literal["eos_designs", "eos_cli_config_gen", "all"] | None = None, **data: Any) -> None:
        """
        Takes a kwarg "_resolve_schema" which controls if $refs are resolved, and if a string, only the given schema will be resolved.

        The $ref expansion _only_ covers this field.
        Any $ref on child fields are expanded as they are initialized by Pydantic since they are based on this base class.
        """
        # Setting the resolve_schema attribute on the class, so all sub-classes will inherit this automatically.
        if _resolve_schema is not None:
            AvdSchemaBaseModel._resolve_schema = _resolve_schema

        if self._resolve_schema:
            data = merge_schema_from_ref(data, resolve_schema=self._resolve_schema)

        super().__init__(**data)

    @cached_property
    def _descendant_tables(self) -> set[str]:
        """
        Descendant tables are used for schema docs to identify if a key should be included in a certain table.

        Descendant tables should return all table names from fields below this field. Not the field itself.

        There are no descendant tables on most fields so the base class returns an empty set. Overridden on list and dict.
        """
        return set()

    @cached_property
    def _table(self) -> str | None:
        """
        Return the name of the schema documentation table where this field should be included.

        The table name can be derived from several sources depending on the position and configuration of the field.
        In order the sources are:
        - Statically defined under "documentation_options.table".
        - Inherit from parent schema if available.
        - None if this is the root dict. This means that the first level of keys - called root keys - will not find a parent table.
        - Root keys will default to a hyphen variant of their key name.

        Most fields will inherit from parent schema.
        """
        if self.documentation_options and self.documentation_options.table:
            return self.documentation_options.table

        # No local table, so use the _table from the parent_schema if available.
        if self._parent_schema and self._parent_schema._table:
            return self._parent_schema._table

        # This should never happen, since only the root key should be without a parent_schema.
        if len(self._path) != 1:
            msg = "Something went wrong in _table"
            raise ValueError(msg, self._path)

        # This is a root key the default table is the key with hyphens and removing <,>
        return self._key.replace("<", "").replace(">", "").replace("_", "-")

    @cached_property
    def _path(self) -> list[str]:
        """
        Returns the variable path for this field to be used in schema docs.

        Like "rootkey.subkey.[].mykey".
        """
        # A list item has no key, so add "[]" to the parent schema for representing the list-item
        if not self._key:
            return [*self._parent_schema._path, "[]"]

        # Add the key to the parent path
        return [*self._parent_schema._path, self._key]

    def _generate_table_rows(self, target_table: str | None = None) -> Generator[TableRow]:
        """
        Yields "TableRow"s to be used in schema docs.

        The function is called recursively inside the YamlLineGen classes for parsing children.
        """
        # Using the Type of table row generator set in the subclass attribute _table_row_generator
        yield from self._table_row_generator().generate_table_rows(schema=self, target_table=target_table)

    def _generate_yaml_lines(self, target_table: str | None = None) -> Generator[YamlLine]:
        """
        Yields "YamlLine"s to be used in schema docs.

        The function is called recursively inside the YamlLineGen classes for parsing children.
        """
        # Using the Type of yaml line generator set in the subclass attribute _yaml_line_generator
        yield from self._yaml_line_generator().generate_yaml_lines(schema=self, target_table=target_table)

    def _generate_class_src(self, class_name: str | None = None) -> SrcData:
        """
        Returns one instance of "Src" to be used for generating python class models based on the schemas.

        The function is called recursively inside the SrcGen classes for parsing children.
        """
        # Using the Type of yaml line generator set in the subclass attribute _yaml_line_generator
        return self._class_src_generator().generate_class_src(schema=self, class_name=class_name)


class AvdSchemaInt(AvdSchemaBaseModel):
    """
    Pydantic model for AvdSchema fields of type "int".

    Contains fields that applies to this type specifically. Other fields are inherited from the base class.

    Also covers internal attributes and methods used for documentation generation.
    All these are prefixed with underscore.
    """

    class ConvertType(str, Enum):
        bool = "bool"
        str = "str"
        float = "float"

    # AvdSchema field properties
    type: Literal["int"]
    convert_types: list[ConvertType] | None = None
    """List of types to auto-convert from. For 'int' auto-conversion is supported from 'bool', 'str' and 'float'"""
    default: int | None = None
    """Default value"""
    min: int | None = None
    """Minimum value"""
    max: int | None = None
    """Maximum value"""
    valid_values: list[int] | None = None
    """List of valid values"""
    dynamic_valid_values: list[str] | None = None
    """
    List of path to variable under the parent dictionary containing valid values.
    Variable path use dot-notation and variable path must be relative to the parent dictionary.
    If an element of the variable path is a list, every list item will be unpacked.
    Note that this is building the schema from values in the _data_ being validated!
    """

    # Type of schema docs generators to use for this schema field.
    _table_row_generator = TableRowGenInt
    _yaml_line_generator = YamlLineGenInt
    # Type of class source generator to use for this schema field.
    _class_src_generator = SrcGenInt


class AvdSchemaBool(AvdSchemaBaseModel):
    """
    Pydantic model for AvdSchema fields of type "bool".

    Contains fields that applies to this type specifically. Other fields are inherited from the base class.

    Also covers internal attributes and methods used for documentation generation.
    All these are prefixed with underscore.
    """

    class ConvertType(str, Enum):
        int = "int"
        str = "str"

    # AvdSchema field properties
    type: Literal["bool"]
    convert_types: list[ConvertType] | None = None
    """List of types to auto-convert from. For 'bool' auto-conversion is supported from 'int' and 'str'"""
    default: bool | None = None
    """Default value"""
    valid_values: list[bool] | None = None
    """List of valid values"""
    dynamic_valid_values: list[str] | None = None
    """
    List of paths to variable under the parent dictionary containing valid values.
    Variable path use dot-notation and variable path must be relative to the parent dictionary.
    If an element of the variable path is a list, every list item will be unpacked.
    Note that this is building the schema from values in the _data_ being validated!
    """

    # Type of schema docs generators to use for this schema field.
    _table_row_generator = TableRowGenBool
    _yaml_line_generator = YamlLineGenBool
    # Type of class source generator to use for this schema field.
    _class_src_generator = SrcGenBool


class AvdSchemaStr(AvdSchemaBaseModel):
    """
    Pydantic model for AvdSchema fields of type "str".

    Contains fields that applies to this type specifically. Other fields are inherited from the base class.

    Also covers internal attributes and methods used for documentation generation.
    All these are prefixed with underscore.
    """

    class ConvertType(str, Enum):
        bool = "bool"
        int = "int"
        float = "float"

    class Format(str, Enum):
        ipv4 = "ipv4"
        ipv4_cidr = "ipv4_cidr"
        ipv6 = "ipv6"
        ipv6_cidr = "ipv6_cidr"
        ip = "ip"
        cidr = "cidr"
        mac = "mac"

        def __str__(self) -> str:
            return self.value

    # AvdSchema field properties
    type: Literal["str"]
    convert_to_lower_case: bool | None = False
    """Convert string value to lower case before performing validation"""
    convert_types: list[ConvertType] | None = None
    """List of types to auto-convert from.\n\nFor 'str' auto-conversion is supported from 'bool' and 'int'"""
    default: str | None = None
    """Default value"""
    format: Format | None = None
    """String format"""
    min_length: int | None = None
    """Mininmum string length"""
    max_length: int | None = None
    """Maximum string length"""
    pattern: str | None = None
    """
    A regular expression which will be matched on the variable value.
    The regular expression should be valid according to the ECMA 262 dialect.
    Remember to use double escapes.
    """
    valid_values: list[str] | None = None
    """List of valid values"""
    dynamic_valid_values: list[str] | None = None
    """
    List of paths to variable under the parent dictionary containing valid values.
    Variable path use dot-notation and variable path must be relative to the parent dictionary.
    If an element of the variable path is a list, every list item will be unpacked.
    Note that this is building the schema from values in the _data_ being validated!
    """

    # Type of schema docs generators to use for this schema field.
    _table_row_generator = TableRowGenStr
    _yaml_line_generator = YamlLineGenStr
    # Type of class source generator to use for this schema field.
    _class_src_generator = SrcGenStr


class AvdSchemaList(AvdSchemaBaseModel):
    """
    Pydantic model for AvdSchema fields of type "list".

    Contains fields that applies to this type specifically. Other fields are inherited from the base class.

    Also covers internal attributes and methods used for documentation generation.
    All these are prefixed with underscore.
    """

    class ConvertType(str, Enum):
        dict = "dict"
        list = "list"
        str = "str"

    # AvdSchema field properties
    type: Literal["list"]
    convert_types: list[ConvertType] | None = None
    """
    List of types to auto-convert from.
    For 'list of dicts' auto-conversion is supported from 'dict' if 'primary_key' is set on the list schema.
    For other list item types conversion from dict will use the keys as list items.
    """
    default: list | None = None
    """Default value"""
    items: Annotated[AvdSchemaField, Field(discriminator="type")] | None = None
    """Schema for list items"""
    min_length: int | None = None
    """Minimum list items"""
    max_length: int | None = None
    """Maximum list items"""
    primary_key: str | None = Field(None, pattern=KEY_PATTERN)
    """
    Name of a primary key in a list of dictionaries.
    The configured key is implicitly required and must have unique values between the list elements.
    """
    unique_keys: list[str] | None = None
    """
    Name of a key in a list of dictionaries.
    The configured key must have unique values between the list elements.
    This can also be a variable path using dot-notation like 'parent_key.child_key' in case of nested lists of dictionaries.
    """
    allow_duplicate_primary_key: bool | None = None
    """
    Set to True to allow duplicate primary_key values for a list of dicts.
    Useful when primary key is only used for convert_dicts.
    NOTE! Should only be used in eos_designs inputs since we cannot merge on primary key if there are duplicate entries.
    """

    # Type of schema docs generators to use for this schema field.
    _table_row_generator = TableRowGenList
    _yaml_line_generator = YamlLineGenList
    # Type of class source generator to use for this schema field.
    _class_src_generator = SrcGenList

    @cached_property
    def _descendant_tables(self) -> set[str]:
        """
        Descendant tables are used for schema docs to identify if a key should be included in a certain table.

        Descendant tables returns all table names from fields below this field. Not the field itself.
        """
        if not self.items:
            return set()

        descendant_tables = set()
        descendant_tables.add(self.items._table)
        descendant_tables.update(self.items._descendant_tables)

        return descendant_tables

    def model_post_init(self, context: Any) -> None:
        """
        Overrides BaseModel.model_post_init.

        Runs after this model including all child models have been initialized.

        Sets Internal attributes on child schema (if set):
            - _parent_schema
            - _is_first_list_key (except for dict)

        Sets Internal attributes on grandchild schemas if child schema is a dict:
            - _is_primary_key
            - _is_unique
            - _is_first_list_key
        """
        if self.items:
            self.items._parent_schema = self
            if isinstance(self.items, AvdSchemaDict) and self.items.keys:
                first_key = True
                for key, grandchildschema in self.items.keys.items():
                    if first_key:
                        grandchildschema._is_first_list_key = True
                        first_key = False

                    if self.primary_key and self.primary_key == key:
                        grandchildschema._is_primary_key = True
                        grandchildschema._is_unique = self.allow_duplicate_primary_key is not True
                        # No need to look any further if we found the primary key.
                        break
            else:
                self.items._is_first_list_key = True

        return super().model_post_init(context)


class AvdSchemaDict(AvdSchemaBaseModel):
    """
    Pydantic model for AvdSchema fields of type "dict".

    Contains fields that applies to this type specifically. Other fields are inherited from the base class.

    Also covers internal attributes and methods used for documentation generation.
    All these are prefixed with underscore.
    """

    class DocumentationOptions(AvdSchemaBaseModel.DocumentationOptions):
        """Extra schema field options used for controlling documentation generation for dicts."""

        hide_keys: bool | None = None
        # """
        # Prevent keys of the dict from being displayed in the generated documentation.
        # This is used for structured_config where we wish to avoid displaying the full eos_cli_config_gen schema everywhere.
        # """

    # AvdSchema field properties
    type: Literal["dict"]
    default: dict[str, Any] | None = None
    """Default value"""

    keys: dict[str, Annotated[AvdSchemaField, Field(discriminator="type")]] | None = None
    """
    Dictionary of dictionary-keys in the format `{<keyname>: {<schema>}}`.
    `keyname` must use snake_case.
    `schema` is the schema for each key. This is a recursive schema, so the value must conform to AVD Schema.
    """
    dynamic_keys: dict[str, Annotated[AvdSchemaField, Field(discriminator="type")]] | None = None
    """
    Dictionary of dynamic dictionary-keys in the format `{<variable.path>: {<schema>}}`.
    `variable.path` is a variable path using dot-notation and pointing to a variable under the parent dictionary containing dictionary-keys.
    If an element of the variable path is a list, every list item will unpacked.
    `schema` is the schema for each key. This is a recursive schema, so the value must conform to AVD Schema.
    Note that this is building the schema from values in the _data_ being validated!
    """
    relaxed_validation: bool | None = False
    """Disable validation of `required` keys for any children."""
    allow_other_keys: bool | None = False
    """Allow keys in the dictionary which are not defined in the schema."""
    documentation_options: DocumentationOptions | None = None
    """Schema field options used for controlling documentation generation"""
    field_schema: str | None = Field(None, alias="$schema")
    """Schema name used when exporting to JSON schema"""
    field_id: str | None = Field(None, alias="$id")
    """Schema ID used when exporting to JSON schema"""
    field_defs: dict[str, Annotated[AvdSchemaField, Field(discriminator="type")]] = Field(None, alias="$defs")
    """Storage for reusable schema fragments"""

    # Type of schema docs generators to use for this schema field.
    _table_row_generator = TableRowGenDict
    _yaml_line_generator = YamlLineGenDict
    # Type of class source generator to use for this schema field.
    _class_src_generator = SrcGenDict

    @cached_property
    def _descendant_tables(self) -> set[str]:
        """
        Descendant tables are used for schema docs to identify if a key should be included in a certain table.

        Descendant tables returns all table names from fields below this field. Not the field itself.
        """
        descendant_tables = set()
        if self.documentation_options and self.documentation_options.hide_keys:
            return descendant_tables
        if self.keys:
            for childschema in self.keys.values():
                descendant_tables.add(childschema._table)
                descendant_tables.update(childschema._descendant_tables)
        if self.dynamic_keys:
            for childschema in self.dynamic_keys.values():
                descendant_tables.add(childschema._table)
                descendant_tables.update(childschema._descendant_tables)

        return descendant_tables

    def model_post_init(self, context: Any) -> None:
        """
        Overrides BaseModel.model_post_init.

        Runs after this model including all child models have been initialized.

        Set Internal attributes on child schemas:
            - _key
            - _parent_schema
        """
        if self.keys:
            for key, childschema in self.keys.items():
                childschema._key = key
                childschema._parent_schema = self

        if self.dynamic_keys:
            for key, childschema in self.dynamic_keys.items():
                childschema._key = f"<{key}>"
                childschema._parent_schema = self

        return super().model_post_init(context)


class AristaAvdSchema(AvdSchemaDict):
    """
    Arista AVD Schema.

    This is the schema root dict class providing specific fields and overrides of AvdSchemaDict.
    """

    # Type of class source generator to use for this schema field.
    _class_src_generator = SrcGenRootDict

    # Internal attributes used by schema docs generators
    @cached_property
    def _table(self) -> str | None:
        """
        Return the name of the schema documentation table where this field should be included.

        The table name is not applicable to the root schema so we return None
        """
        return None

    @cached_property
    def _path(self) -> list[str]:
        """
        Returns the variable path for this field to be used in schema docs.

        The root dict has an empty path.
        """
        return []


AvdSchemaField = AvdSchemaInt | AvdSchemaBool | AvdSchemaStr | AvdSchemaList | AvdSchemaDict
"""Alias for any of the AvdSchema field types"""
