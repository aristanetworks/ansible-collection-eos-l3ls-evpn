# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from textwrap import indent, wrap

from schema_tools.constants import LICENSE_HEADER

SRC_HEADER = indent(LICENSE_HEADER + "\n\n", "# ") + "from __future__ import annotations\n"

BASE_IMPORTS = """\
from typing import TYPE_CHECKING

from pyavd._schema.models.avd_indexed_list import AvdIndexedList
from pyavd._schema.models.avd_list import AvdList
from pyavd._schema.models.avd_model import AvdModel

if TYPE_CHECKING:
    from pyavd._utils import Undefined, UndefinedType
"""
BASE_MODEL_NAME = "AvdModel"
INDENT = "    "


@dataclass
class FieldSrc:
    """
    Dataclass containing the elements to generate Python source code for one field.

    Use str() on the instance to render the source code.
    """

    name: str
    field_type: str
    type_hints: list[FieldTypeHintSrc]
    key: str | None = None
    description: str | None = None
    optional: bool = True
    default_value: str | None = None
    """The default assignment source code for assigning lists or dicts as default values."""

    def __str__(self) -> str:
        """
        Render source code for one field.

        <name>: <type-hints> | UndefinedType = Undefined
        """
        return f"{self.field_as_class_attr()} | UndefinedType = Undefined"

    def field_as_class_attr(self) -> str:
        """
        Render source code for one field without default assignment.

        Used for class attributes.

        <name>: <type-hints>
        """
        # Build union of multiple type hints
        type_hints = " | ".join(str(type_hint) for type_hint in self.type_hints)
        if self.optional and not self.default_value and "None" not in self.type_hints and self.field_type in ("str", "int", "bool", "float"):
            type_hints += " | None"

        return f"{self.name}: {type_hints}"

    def _docstring(self) -> str:
        """Render the content of the docstring for this field as source code."""
        docstring = ""
        if self.description:
            docstring += "\n".join(wrap(self.description, width=100, replace_whitespace=False))
        if self.default_value:
            docstring += f"\n\nDefault value: `{self.default_value}`"
        return docstring

    def get_imports(self) -> set:
        """Return a set of strings with Python imports that are needed for this class."""
        imports = set()
        if self.default_value and "coerce_type" in self.default_value:
            imports.add("from pyavd._schema.coerce_type import coerce_type")
        for type_hint in self.type_hints:
            imports.update(type_hint.get_imports())
        return imports

    def field_as_dict_str(self) -> str:
        """
        Return a representation of the field to be inserted in a dict string.

        Used for _fields classvar
        """
        dict_fields_src = [f'"type": {self.field_type}']
        if self.default_value:
            dict_fields_src.append(f'"default": {self.default_value}')

        return f'"{self.name}": {{{", ".join(dict_fields_src)}}}'


@dataclass
class ClassVarSrc:
    """
    Dataclass containing the elements to generate Python source code for one ClassVar.

    Use str() on the instance to render the source code.
    """

    name: str
    type_hint: FieldTypeHintSrc
    value: str
    description: str | None = None
    """The default assignment source code for assigning lists or dicts as default values."""

    def __str__(self) -> str:
        """
        Render source code for one field.

        <name>: ClassVar[<type-hint>] = <value>
        """
        return f"{self.name}: ClassVar[{self.type_hint!s}] = {self.value}"

    def _docstring(self) -> str:
        """Render the content of the docstring for this field as source code."""
        if not self.description:
            return ""

        docstring = "\n".join(wrap(self.description, width=100, replace_whitespace=False))
        return f"{docstring}\n"

    def get_imports(self) -> set:
        imports = {"from typing import ClassVar"}
        imports.update(self.type_hint.get_imports())
        return imports


@dataclass
class ModelSrc:
    """
    Dataclass containing the elements to generate Python source code for this class including any nested classes and fields.

    Can have nested classes and fields.

    Use str() on the instance to render the source code.
    """

    name: str
    classes: list[ModelSrc | ListSrc]
    fields: list[FieldSrc]
    class_vars: list[ClassVarSrc] | None = None
    imports: set[str] | None = None
    base_classes: list[str] | None = None
    description: str | None = None
    allow_extra: bool = False

    def __str__(self) -> str:
        """Renders the Python source code for this class including any nested classes and fields."""
        base_classes = ", ".join(self.base_classes) if self.base_classes else BASE_MODEL_NAME

        classsrc = f"class {self.name}({base_classes}):\n" if base_classes else f"class {self.name}:\n"

        if self.description:
            description = "\n".join(wrap(self.description, width=100, replace_whitespace=False))
            if "\n" in description:
                classsrc += indent(f'"""\n{description.strip()}\n"""\n', INDENT)
            else:
                classsrc += indent(f'"""{description}"""\n', INDENT)

        if classes := self._render_classes():
            classsrc += f"{classes}\n"

        if class_vars := self._render_class_vars():
            classsrc += f"{class_vars}\n"

        if fields := self._render_fields():
            classsrc += f"{fields}\n"

        if not classes and not fields:
            classsrc += "    pass\n"

        return classsrc

    def _init_docstring(self) -> str:
        """Render the docstring for the __init__ method for this model as source code."""
        docstring_elements = [f"{self.name}.\n"]
        if self.description:
            # Build docstring styled description
            docstring_elements.append("\n".join(wrap(self.description, width=100, replace_whitespace=False)))

        if self.fields:
            args = "Args:\n"
            for field in self.fields:
                field_arg = f"{field.name}"
                if field.description:
                    description = (
                        "\n".join(wrap(field.description, width=100, replace_whitespace=False))
                        .replace("Example:\n", "Example:  # fmt: skip\n")
                        .replace("Examples:\n", "Examples:  # fmt: skip\n")
                        .replace("Note:\n", "Note:  # fmt: skip\n")
                        .replace("Notes:\n", "Notes:  # fmt: skip\n")
                    )
                    if "\n" in description:
                        field_arg += f":\n{indent(description, '   ')}"
                    else:
                        field_arg += f": {description}"
                else:
                    field_arg += f": {field.name}"
                args += indent(field_arg, INDENT)
                args += "\n"
            docstring_elements.append(args)

        if docstring_elements:
            docstring_content = "\n\n".join(docstring_elements)
            return indent(f'"""\n{docstring_content}\n"""\n', INDENT)
        return ""

    def _render_classes(self) -> str:
        """Renders the Python source code for any nested classes."""
        if not self.classes:
            return ""

        return indent("\n".join(str(cls) for cls in self.classes), INDENT)

    def _render_class_vars(self) -> str:
        """Renders the Python source code for any ClassVars."""
        if not self.class_vars:
            return ""

        return indent("\n".join(str(class_var) for class_var in self.class_vars), INDENT)

    def _render_fields(self) -> str:
        """Renders the Python source code for any nested fields."""
        if not self.fields:
            return ""

        fields_types_dict = ", ".join(field.field_as_dict_str() for field in self.fields)
        src = f"    _fields: ClassVar[dict] = {{{fields_types_dict}}}\n"

        if field_to_key_map := {field.name: field.key for field in self.fields if field.name and field.key and field.name != field.key}:
            src += f"    _field_to_key_map: ClassVar[dict] = {field_to_key_map}\n"

        if key_to_field_map := {field.key: field.name for field in self.fields if field.name and field.key and field.name != field.key}:
            src += f"    _key_to_field_map: ClassVar[dict] = {key_to_field_map}\n"

        if self.allow_extra:
            src += "    _allow_other_keys: ClassVar[bool] = True\n"
        if not self.fields:
            return src

        for field in self.fields:
            src += indent(f"{field.field_as_class_attr()}\n", INDENT)
            if docstring := field._docstring().strip():
                if "\n" in docstring:
                    src += indent(f'"""\n{docstring}\n"""\n', INDENT)
                else:
                    src += indent(f'"""{docstring}"""\n', INDENT)
        if self.base_classes == ["object"]:
            # This is some internal class so we don't need __init__
            return src

        field_as_args = ["self", "*", *(str(field).split("\n", maxsplit=1)[0] for field in self.fields)]
        src += indent("\n\nif TYPE_CHECKING:\n", INDENT)
        src += indent(f"def __init__({', '.join(field_as_args)}) -> None:\n", INDENT * 2)
        src += indent(self._init_docstring(), INDENT * 2)
        return src

    def get_imports(self) -> set:
        """Returns Python import statements required for this class including any nested classes and fields."""
        imports = self.imports or set()
        if self.fields:
            imports.add("from typing import ClassVar")
        if self.class_vars:
            for class_var in self.class_vars:
                imports.update(class_var.get_imports())
        for cls in self.classes:
            imports.update(cls.get_imports())
        for field in self.fields:
            imports.update(field.get_imports())
        return imports


@dataclass
class ListSrc:
    """
    Dataclass containing the elements to generate Python source code for this class.

    Use str() on the instance to render the source code.
    """

    name: str
    base_class: str
    item_type: str | None = None
    class_vars: list[ClassVarSrc] | None = None
    imports: set[str] | None = None
    description: str | None = None

    def __str__(self) -> str:
        """Renders the Python source code for this class including any nested classes and fields."""
        classsrc = f"class {self.name}({self.base_class}):\n"

        if self.description:
            description = "\n".join(wrap(self.description, width=100, replace_whitespace=False))
            if "\n" in description:
                classsrc += indent(f'"""\n{description.strip()}\n"""\n', INDENT)
            else:
                classsrc += indent(f'"""{description}"""\n', INDENT)

        if class_vars := self._render_class_vars():
            classsrc += f"{class_vars}\n"

        if not (self.description or class_vars):
            classsrc += "    pass\n"

        if self.item_type:
            classsrc += f"\n{self.name}._item_type = {self.item_type}\n"

        return classsrc

    def _render_class_vars(self) -> str:
        """Renders the Python source code for any ClassVars."""
        if not self.class_vars:
            return ""

        return indent("\n".join(str(class_var) for class_var in self.class_vars), INDENT)

    def get_imports(self) -> set:
        """Returns Python import statements required for this class including any nested classes and fields."""
        imports = self.imports or set()
        if self.class_vars:
            for class_var in self.class_vars:
                imports.update(class_var.get_imports())
        return imports


@dataclass
class SrcData:
    """Dataclass containing a field and an associated class for one schema field including child fields."""

    field: FieldSrc | None = None
    """
    field should be set on all instances except for the root model
    """

    cls: ModelSrc | ListSrc | None = None
    """
    cls is a full model for a 'dict' field or the main class for a 'list' field.
    """

    item_classes: list[ModelSrc | ListSrc] | None = None
    """
    item_classes is a list of Models uses as items in lists. If there are multiple classes here it is because the first one is also a list.
    """


@dataclass
class FileSrc:
    """
    Dataclass containing the elements to generate Python source code for this file.

    Use str() on the instance to render the source code.
    """

    classes: list[ModelSrc]

    def __str__(self) -> str:
        """Returns Python source code for this file."""
        src = f"{SRC_HEADER}"
        # BASE_IMPORTS comes last since we have if TYPE_CHECKING.
        src += f"{self._render_imports()}\n{BASE_IMPORTS}\n\n"
        src += self._render_classes()
        return src.rstrip() + "\n"

    def _render_classes(self) -> str:
        """Render the python source code for classes."""
        return "\n\n".join(str(cls) for cls in self.classes)

    def _render_imports(self) -> str:
        """Render the python source code for imports."""
        imports = set()
        for cls in self.classes:
            imports.update(cls.get_imports())
        return "\n".join(str(imp) for imp in imports)


@dataclass
class AnnotationSrc(ABC):
    """
    Base class for generating python source code for one annotation.

    Subclasses must implement __str__() and get_imports().
    """

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def get_imports(self) -> set:
        pass


@dataclass
class FieldTypeHintSrc(AnnotationSrc):
    """
    Dataclass containing the type and any annotations for one dataclass field.

    The annotations can either be a string, a subclass of AnnotationSrc or another FieldTypeHintSrc.
    For field_type=="list" there list_item_type can be a string or another FieldTypeHintSrc.
    """

    field_type: str
    list_item_type: str | FieldTypeHintSrc | None = None
    annotations: list[str | AnnotationSrc] | None = None

    def __str__(self) -> str:
        """
        Returns Python source code for type hint and optional annotation for one dataclass field.

        If there are types but no annotations given it will render "<type1> | <type2>"
        If there are annotations as well as types it will render "Annotated[<type1> | <type2>, <annotation1>, <annotation2>]"
        If there are nested annotations it could look like "Annotated[<type>, Annotated[<nested_type>, <nested_annotation>]]"
        """
        field_type = f"{self.field_type}[{self.list_item_type}]" if self.field_type in ("list", "tuple") else self.field_type

        if not self.annotations:
            return field_type

        return f"Annotated[{field_type}, {', '.join(str(annotation) for annotation in self.annotations)}]"

    def get_imports(self) -> set:
        """Returns Python import statements required for this type hint and annotations."""
        imports = set()
        if self.field_type == "list" and self.list_item_type in [None, "Any"]:
            imports.add("from typing import Any")

        if "Literal[" in self.field_type:
            imports.add("from typing import Literal")

        if not self.annotations:
            return imports

        imports.add("from typing import Annotated")
        for annotation in self.annotations:
            if isinstance(annotation, AnnotationSrc):
                imports.update(annotation.get_imports())

        return imports
