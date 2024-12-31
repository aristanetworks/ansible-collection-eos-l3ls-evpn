# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from __future__ import annotations
from typing import ClassVar
from typing import Any
from pyavd._schema.models.eos_cli_config_gen_root_model import EosCliConfigGenRootModel
from typing import TYPE_CHECKING

from pyavd._schema.models.avd_indexed_list import AvdIndexedList
from pyavd._schema.models.avd_list import AvdList
from pyavd._schema.models.avd_model import AvdModel

if TYPE_CHECKING:
    from pyavd._utils import Undefined, UndefinedType


class DataMergingTestSchema(EosCliConfigGenRootModel):
    """Subclass of AvdModel."""
    class SomeIndexedListItem(AvdModel):
        """Subclass of AvdModel."""
        _fields: ClassVar[dict] = {"name": {"type": str}, "some_int": {"type": int}, "_custom_data": {"type": dict}}
        name: str
        some_int: int | None
        _custom_data: dict[str, Any]


        if TYPE_CHECKING:
            def __init__(self, *, name: str | UndefinedType = Undefined, some_int: int | None | UndefinedType = Undefined, _custom_data: dict[str, Any] | UndefinedType = Undefined) -> None:
                """
                SomeIndexedListItem.


                Subclass of AvdModel.

                Args:
                    name: name
                    some_int: some_int
                    _custom_data: _custom_data

                """


    class SomeIndexedList(AvdIndexedList[str, SomeIndexedListItem]):
        """Subclass of AvdIndexedList with `SomeIndexedListItem` items. Primary key is `name` (`str`)."""
        _primary_key: ClassVar[str] = "name"

    SomeIndexedList._item_type = SomeIndexedListItem

    class SomeList(AvdList[int]):
        """Subclass of AvdList with `int` items."""

    SomeList._item_type = int

    _fields: ClassVar[dict] = {"some_indexed_list": {"type": SomeIndexedList}, "some_list": {"type": SomeList}, "_custom_data": {"type": dict}}
    _allow_other_keys: ClassVar[bool] = True
    some_indexed_list: SomeIndexedList
    """Subclass of AvdIndexedList with `SomeIndexedListItem` items. Primary key is `name` (`str`)."""
    some_list: SomeList
    """Subclass of AvdList with `int` items."""
    _custom_data: dict[str, Any]


    if TYPE_CHECKING:
        def __init__(self, *, some_indexed_list: SomeIndexedList | UndefinedType = Undefined, some_list: SomeList | UndefinedType = Undefined, _custom_data: dict[str, Any] | UndefinedType = Undefined) -> None:
            """
            DataMergingTestSchema.


            Subclass of AvdModel.

            Args:
                some_indexed_list: Subclass of AvdIndexedList with `SomeIndexedListItem` items. Primary key is `name` (`str`).
                some_list: Subclass of AvdList with `int` items.
                _custom_data: _custom_data

            """
