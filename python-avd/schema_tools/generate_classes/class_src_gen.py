# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from keyword import iskeyword
from typing import TYPE_CHECKING

from .src_generators import ClassVarSrc, FieldSrc, FieldTypeHintSrc, ListSrc, ModelSrc, SrcData
from .utils import generate_class_name, generate_class_name_from_ref

if TYPE_CHECKING:
    from schema_tools.metaschema.meta_schema_model import AvdSchemaBool, AvdSchemaDict, AvdSchemaField, AvdSchemaInt, AvdSchemaList, AvdSchemaStr


class SrcGenBase:
    """Provides the method "generate_class_src" used to build source code for Python classes representing the schema."""

    # TODO: add deprecation handling
    #       dynamic_valid_values

    def generate_class_src(self, schema: AvdSchemaField, class_name: str | None = None) -> SrcData:
        """
        Returns SrcData for the given schema.

        Recursively walks child schemas and creates nested classes and fields.
        """
        self.schema = schema
        self.class_name = class_name

        if schema.deprecation and schema.deprecation.removed:
            return SrcData()

        return SrcData(field=self.get_field(), cls=self.get_class())

    def get_field(self) -> FieldSrc | None:
        """Returns FieldSrc for the given schema to be used for the field definition in the parent object."""
        if not self.schema._key:
            return None

        return FieldSrc(
            name=self.get_field_name(),
            key=self.get_key(),
            field_type=self.get_type(),
            type_hints=self.get_type_hints(),
            optional=not (bool(self.schema.required) or self.schema._is_primary_key),
            default_value=self.get_default(),
            description=self.get_description(),
        )

    def get_type(self) -> str:
        return self.schema.type

    def get_description(self) -> str | None:
        return self.schema.description

    def get_type_hints(self) -> list[FieldTypeHintSrc]:
        """Returns a list of FieldTypeHintSrc representing the type hints for this schema."""
        field_type = cls.name if (cls := self.get_class()) else self.schema.type

        return [
            FieldTypeHintSrc(
                field_type=field_type,
                # TODO: For annotation based validation we need this: annotations=get_annotations_for_field(self.schema),
            )
        ]

    def get_class_name(self) -> str:
        """Returns the class name to be used for the class definition in the parent object."""
        if self.class_name:
            return self.class_name

        return generate_class_name(self.get_key())

    def get_class(self) -> ModelSrc | None:
        """Returns ModelSrc for the given schema to be used for the class definition in the parent object."""
        return None

    def get_key(self) -> str:
        """Returns the key name after stripping dynamic key syntax."""
        return self.schema._key.replace("<", "").replace(">", "").replace(".", "_")

    def get_field_name(self) -> str:
        """
        Returns the name to be used for the field definition in the parent object.

        Python reserved keywords pr mixed case keys will get a prefix of "field_".
        """
        if not self.valid_key:
            return f"field_{self.get_key()}"
        return self.get_key()

    @property
    def valid_key(self) -> bool:
        """Check if the key name can be used as field name."""
        return not iskeyword(self.schema._key) and self.schema._key.islower()

    def get_default(self) -> str | None:
        """Returns the default value from the schema as a source code string."""
        if self.schema.default is not None:
            return str(self.schema.default)
        return None


class SrcGenInt(SrcGenBase):
    """Provides the method "generate_class_src" used to build source code for Python classes representing the schema."""

    schema: AvdSchemaInt

    def get_type_hints(self) -> list[FieldTypeHintSrc]:
        """Returns a list of FieldTypeHintSrc representing the type hints for this schema."""
        field_type = cls.name if (cls := self.get_class()) else self.schema.type

        if self.schema.valid_values is None:
            return [FieldTypeHintSrc(field_type=field_type)]

        return [FieldTypeHintSrc(field_type=f"Literal[{', '.join(map(str, self.schema.valid_values))}]")]


class SrcGenBool(SrcGenBase):
    """Provides the method "generate_class_src" used to build source code for Python classes representing the schema."""

    schema: AvdSchemaBool


class SrcGenStr(SrcGenBase):
    """Provides the method "generate_class_src" used to build source code for Python classes representing the schema."""

    schema: AvdSchemaStr

    def get_default(self) -> str | None:
        """Returns the default value from the schema as a source code string."""
        if self.schema.default is not None:
            return f'"{self.schema.default}"'
        return None

    def get_type_hints(self) -> list[FieldTypeHintSrc]:
        """Returns a list of FieldTypeHintSrc representing the type hints for this schema."""
        field_type = cls.name if (cls := self.get_class()) else self.schema.type

        if self.schema.valid_values is None:
            return [FieldTypeHintSrc(field_type=field_type)]

        def quote(string: str) -> str:
            return f'"{string}"'

        return [FieldTypeHintSrc(field_type=f"Literal[{', '.join(map(quote, self.schema.valid_values))}]")]


class SrcGenList(SrcGenBase):
    """Provides the method "generate_class_src" used to build source code for Python classes representing the schema."""

    schema: AvdSchemaList

    def get_type(self) -> str:
        return self.get_class_name()

    def generate_class_src(self, schema: AvdSchemaList, class_name: str | None = None) -> SrcData:
        """
        Returns SrcData for the given schema.

        Recursively walks child schemas and creates nested classes and fields.
        """
        self.schema = schema
        self.class_name = class_name

        if schema.deprecation and schema.deprecation.removed:
            return SrcData(field=None, cls=None)

        return SrcData(field=self.get_field(), cls=self.get_class(), item_classes=self.get_item_classes())

    def get_class(self) -> ListSrc:
        """Returns ListSrc for the given schema to be used for the class definition in the parent object."""
        if self.schema.field_ref:
            # TODO: Currently we only skip resolving ref for indexedlists. Improve this.
            return ListSrc(
                name=self.get_class_name(),
                base_class=generate_class_name_from_ref(self.schema.field_ref),
            )

        class_name = self.get_class_name()
        if self.schema.items is None:
            item_class_name = "Any"
        elif self.schema.items.type in ["dict", "list"]:
            item_class_name = f"{class_name}Item"
        else:
            item_class_name = self.schema.items.type

        # Regular list
        if not self.schema.primary_key or self.schema.allow_duplicate_primary_key:
            return ListSrc(
                name=class_name,
                base_class=f"AvdList[{item_class_name}]",
                item_type=item_class_name,
                description=f"Subclass of AvdList with `{item_class_name}` items.",
            )

        # Indexed list (list with unique primary_key)
        if not self.schema.items or self.schema.items.type != "dict" or not self.schema.items.keys:
            # This should never happen but helps type system detect the relevant schema type below.
            msg = "Some inconsistent types or schema..."
            raise TypeError(msg)

        primary_key_type = self.schema.items.keys[self.schema.primary_key].type
        return ListSrc(
            name=class_name,
            base_class=f"AvdIndexedList[{primary_key_type}, {item_class_name}]",
            item_type=item_class_name,
            description=(
                f"Subclass of AvdIndexedList with `{item_class_name}` items. Primary key is `{self.get_primary_key_field_name()}` (`{primary_key_type}`)."
            ),
            class_vars=[ClassVarSrc("_primary_key", FieldTypeHintSrc("str"), f'"{self.get_primary_key_field_name()}"')],
        )

    def get_item_classes(self) -> list[ModelSrc | ListSrc] | None:
        """Returns a list of src classes for the items schema. There will only be multiple items if we have nested lists."""
        if self.schema.field_ref or not self.schema.items or self.schema.items.type not in ["dict", "list"]:
            return None

        item_classes = []
        fieldsrc = self.schema.items._generate_class_src(f"{self.get_class_name()}Item")
        item_classes.append(fieldsrc.cls)
        if fieldsrc.item_classes:
            item_classes.extend(fieldsrc.item_classes)

        return item_classes

    def get_type_hints(self) -> list[FieldTypeHintSrc]:
        """Returns a list of FieldTypeHintSrc representing the type hints for this schema."""
        return [FieldTypeHintSrc(field_type=self.get_class().name)]

    def get_default(self) -> str | None:
        """Returns the default value from the schema as a source code string."""
        if self.schema.default is None:
            return None
        default_value_as_str = str(self.schema.default).replace("'", '"')
        return f"lambda cls: coerce_type({default_value_as_str}, target_type=cls)"

    def get_primary_key_field_name(self) -> str | None:
        """
        Returns the name to be used for the field used as primary_key.

        Python reserved keywords or mixed case keys will get a prefix of "field_".
        """
        if (primary_key := self.schema.primary_key) is None:
            return None

        if iskeyword(primary_key) or not primary_key.islower():
            return f"field_{primary_key}"

        return primary_key

    def get_description(self) -> str:
        descriptions = [super().get_description(), self.get_class().description]
        return "\n\n".join(description for description in descriptions if description is not None)


class SrcGenDict(SrcGenBase):
    """Provides the method "generate_class_src" used to build source code for Python classes representing the schema."""

    schema: AvdSchemaDict

    def get_type(self) -> str:
        if self.get_class() is not None:
            return self.get_class_name()
        return "dict"

    def get_class(self) -> ModelSrc | None:
        """Returns ModelSrc for the given schema to be used for the class definition in the parent object."""
        if not self.schema.keys:
            if not self.schema.field_ref:
                return None

            classes, fields = [], []

        else:
            classes, fields = self.get_children_classes_and_fields()
        return ModelSrc(
            name=self.get_class_name(),
            base_classes=self.get_base_classes(),
            classes=classes,
            fields=fields,
            imports=self.get_imports(),
            allow_extra=self.schema.allow_other_keys or False,
            description="Subclass of AvdModel.",
        )

    def get_base_classes(self) -> list[str]:
        """Return a list of base classes. Only used if there is an unresolved $ref in the schema."""
        if not self.schema.field_ref:
            return []

        return [generate_class_name_from_ref(self.schema.field_ref)]

    def get_imports(self) -> set[str]:
        """Return a set of strings with Python imports that are needed for this class."""
        imports = set()
        imports.add("from typing import Any")
        if self.schema.field_ref:
            schema_name = self.schema.field_ref.split("#", maxsplit=1)[0]
            imports.add(f"from pyavd._{schema_name}.schema import {generate_class_name(schema_name)}")

        return imports

    def get_children_classes_and_fields(self) -> tuple[list[ModelSrc | ListSrc], list[FieldSrc]]:
        """Return lists of ModelSrc and FieldSrc for any nested fields."""
        classes = []
        fields = []

        if self.schema.keys:
            for childschema in self.schema.keys.values():
                fieldsrc = childschema._generate_class_src()
                if fieldsrc.field:
                    fields.append(fieldsrc.field)
                # Reversing the order to ensure we put items before the class needing it.
                if fieldsrc.item_classes:
                    classes.extend(reversed(fieldsrc.item_classes))
                if fieldsrc.cls:
                    classes.append(fieldsrc.cls)

            fields.append(
                FieldSrc(
                    name="_custom_data",
                    field_type="dict",
                    optional=False,
                    type_hints=[FieldTypeHintSrc(field_type="dict[str, Any]")],
                )
            )

        return classes, fields

    def get_default(self) -> str | None:
        """Returns the default value from the schema as a source code string."""
        # TODO: Improve this to assign a class instance directly instead of using coerce_type.
        if self.schema.default is None:
            return None
        default_value_as_str = str(self.schema.default).replace("'", '"')
        target_type = self.get_type_hints()[0].field_type
        if target_type[0].isupper():
            return f"lambda cls: coerce_type({default_value_as_str}, target_type=cls)"

        return default_value_as_str

    def get_description(self) -> str:
        descriptions = [super().get_description(), cls_src.description if (cls_src := self.get_class()) is not None else None]
        return "\n\n".join(description for description in descriptions if description is not None)


class SrcGenRootDict(SrcGenDict):
    """Provides the method "generate_class_src" used to build source code for Python classes representing the schema."""

    def get_field(self) -> None:
        """
        Returns FieldSrc for the given schema to be used for the field definition in the parent object.

        For the root dict there is no parent, so this always returns None.
        """

    def get_base_classes(self) -> list[str]:
        """Return a list of base classes."""
        if self.get_class_name() == "EosDesigns":
            return ["EosDesignsRootModel"]
        return ["EosCliConfigGenRootModel"]

    def get_imports(self) -> set[str]:
        imports = super().get_imports()
        if self.get_class_name() == "EosDesigns":
            imports.add("from pyavd._schema.models.eos_designs_root_model import EosDesignsRootModel")
        else:
            imports.add("from pyavd._schema.models.eos_cli_config_gen_root_model import EosCliConfigGenRootModel")
        return imports

    def get_children_classes_and_fields(self) -> tuple[list[ModelSrc | ListSrc], list[FieldSrc]]:
        """
        Return lists of ModelSrc and FieldSrc for any nested fields.

        For the EosDesigns root dict we also insert placeholders for custom structured configuration and dynamic keys.
        """
        classes, fields = super().get_children_classes_and_fields()
        if self.get_class_name() != "EosDesigns":
            return classes, fields

        classes.extend(
            [
                ModelSrc(
                    name="_CustomStructuredConfigurationsItem",
                    classes=[],
                    fields=[
                        FieldSrc(
                            name="key",
                            field_type="str",
                            type_hints=[FieldTypeHintSrc(field_type="str")],
                            description="Complete key including prefix",
                            optional=False,
                        ),
                        FieldSrc(
                            name="value",
                            field_type="EosCliConfigGen",
                            type_hints=[FieldTypeHintSrc(field_type="EosCliConfigGen")],
                            description="Structured config including the suffix part of the key.",
                            optional=False,
                        ),
                    ],
                ),
                ListSrc(
                    name="_CustomStructuredConfigurations",
                    base_class="AvdIndexedList[str, _CustomStructuredConfigurationsItem]",
                    item_type="_CustomStructuredConfigurationsItem",
                    class_vars=[ClassVarSrc("_primary_key", FieldTypeHintSrc("str"), '"key"')],
                ),
            ]
        )
        fields.append(
            FieldSrc(
                name="_custom_structured_configurations",
                field_type="_CustomStructuredConfigurations",
                type_hints=[FieldTypeHintSrc(field_type="_CustomStructuredConfigurations")],
            )
        )
        if self.schema.dynamic_keys:
            """
            Build a data model like this:
            dynamic_keys:
              _dynamic_key_maps:
                - dynamic_keys_path: "node_type_keys.key"
                  model_key: "node_type_keys"
              node_type_keys:
                - key: "l2leaf"
                  value: NodeTypeKeysKey
            }
            """
            dyn_classes = []
            dyn_fields = []
            _dynamic_key_maps = []
            for dynamic_keys_path, childschema in self.schema.dynamic_keys.items():
                # dynamic_key_type will be "node_type_keys", "connected_endpoints_keys" or "network_services_keys"
                if not childschema.display_name:
                    msg = "Schemas for dynamic_keys *must* have 'display_name' set."
                    raise ValueError(msg)
                dynamic_key_type = childschema.display_name.replace(" ", "_").lower()
                dynamic_key_model_name = generate_class_name(f"dynamic_{dynamic_key_type}")
                _dynamic_key_maps.append({"dynamic_keys_path": dynamic_keys_path, "model_key": dynamic_key_type})
                fieldsrc = childschema._generate_class_src(class_name=generate_class_name(dynamic_key_type))
                # Overriding the details from the autocreated field. This way we can reuse the field definition with types and type hints
                fieldsrc.field.name = "value"
                fieldsrc.field.description = "Value of dynamic key"
                dyn_classes.extend(
                    [
                        ModelSrc(
                            name=f"{dynamic_key_model_name}Item",
                            # Reversing the order to ensure we put items before the class needing it.
                            classes=[cls for cls in [*reversed(fieldsrc.item_classes or []), fieldsrc.cls] if cls is not None],
                            fields=[
                                FieldSrc(
                                    name="key",
                                    field_type="str",
                                    type_hints=[FieldTypeHintSrc(field_type="str")],
                                    description="Key used as dynamic key",
                                    optional=False,
                                ),
                                fieldsrc.field,
                            ],
                        ),
                        ListSrc(
                            name=dynamic_key_model_name,
                            base_class=f"AvdIndexedList[str, {dynamic_key_model_name}Item]",
                            item_type=f"{dynamic_key_model_name}Item",
                            class_vars=[ClassVarSrc("_primary_key", FieldTypeHintSrc("str"), '"key"')],
                        ),
                    ]
                )
                dyn_fields.append(
                    FieldSrc(
                        name=dynamic_key_type,
                        field_type=dynamic_key_model_name,
                        optional=False,
                        type_hints=[FieldTypeHintSrc(field_type=dynamic_key_model_name)],
                        description=f"Collection of dynamic '{dynamic_key_type}'.",
                    )
                )
            class_vars = [
                ClassVarSrc(
                    name="_dynamic_key_maps",
                    type_hint=FieldTypeHintSrc(field_type="tuple", list_item_type="dict, ..."),
                    description="Internal tuple of mappings from dynamic_keys_path to model_key.",
                    value=str(tuple(_dynamic_key_maps)),
                )
            ]

            classes.append(
                ModelSrc(
                    name="_DynamicKeys",
                    classes=dyn_classes,
                    fields=dyn_fields,
                    class_vars=class_vars,
                    description="Data models for dynamic keys.",
                )
            )
            fields.append(
                FieldSrc(
                    name="_dynamic_keys",
                    field_type="_DynamicKeys",
                    optional=False,
                    type_hints=[FieldTypeHintSrc(field_type="_DynamicKeys")],
                    description="Dynamic keys",
                )
            )

        return classes, fields
