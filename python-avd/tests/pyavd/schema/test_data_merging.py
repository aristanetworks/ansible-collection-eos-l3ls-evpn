# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from importlib.machinery import ModuleSpec
from importlib.util import module_from_spec
from pathlib import Path
from typing import TYPE_CHECKING, Literal

import pytest
import yaml

from schema_tools.generate_classes.src_generators import FileSrc
from schema_tools.metaschema.meta_schema_model import AristaAvdSchema

if TYPE_CHECKING:
    from .data_merging_schema_class import DataMergingTestSchema


script_dir = Path(__file__).parent


@pytest.fixture(scope="module")
def data_merging_schema_class() -> DataMergingTestSchema:
    with Path(script_dir, "data_merging.schema.yml").open(encoding="utf-8") as schema_file:
        raw_schema = yaml.load(schema_file, Loader=yaml.CSafeLoader)

    schema = AristaAvdSchema(**raw_schema)
    schemasrc = schema._generate_class_src(class_name="DataMergingTestSchema")
    src_file_contents = FileSrc(classes=[schemasrc.cls])

    # Writing to file to assist the type-checker for these tests.
    with Path(script_dir, "data_merging_schema_class.py").open(mode="w", encoding="UTF-8") as file:
        file.write(str(src_file_contents))

    cls_module = module_from_spec(ModuleSpec(name="cls_module", loader=None))
    exec(str(src_file_contents), cls_module.__dict__)  # noqa: S102

    return cls_module.DataMergingTestSchema


A_LIST = {"some_list": [1, 2]}
B_LIST = {"some_list": [2, 3, 4]}
ALL_A_AND_B_LISTS = {"some_list": [1, 2, 2, 3, 4]}
UNIQUE_A_AND_B_LISTS = {"some_list": [1, 2, 3, 4]}
ALL_B_AND_A_LISTS = {"some_list": [2, 3, 4, 1, 2]}
UNIQUE_B_AND_A_LISTS = {"some_list": [3, 4, 1, 2]}

A_INDEXED_LIST = {"some_indexed_list": [{"name": "one", "some_int": 1}, {"name": "two", "some_int": 2}]}
B_INDEXED_LIST = {"some_indexed_list": [{"name": "two", "some_int": 2}, {"name": "three", "some_int": 3}, {"name": "four", "some_int": 4}]}
UNIQUE_A_AND_B_INDEXED_LISTS = {
    "some_indexed_list": [{"name": "one", "some_int": 1}, {"name": "two", "some_int": 2}, {"name": "three", "some_int": 3}, {"name": "four", "some_int": 4}]
}
UNIQUE_B_AND_A_INDEXED_LISTS = {
    "some_indexed_list": [{"name": "three", "some_int": 3}, {"name": "four", "some_int": 4}, {"name": "one", "some_int": 1}, {"name": "two", "some_int": 2}]
}


@pytest.mark.parametrize(
    ("a_data", "b_data", "list_merge", "expected"),
    [
        pytest.param({}, {}, "append_unique", {}, id="empty_data"),
        # Testing AvdList
        pytest.param(A_LIST, B_LIST, "append_unique", UNIQUE_A_AND_B_LISTS, id="list_append_unique"),
        pytest.param(A_LIST, B_LIST, "append", ALL_A_AND_B_LISTS, id="list_append"),
        pytest.param(A_LIST, B_LIST, "replace", B_LIST, id="list_replace"),
        pytest.param(A_LIST, B_LIST, "keep", A_LIST, id="list_keep"),
        pytest.param(A_LIST, B_LIST, "prepend", ALL_B_AND_A_LISTS, id="list_prepend"),
        pytest.param(A_LIST, B_LIST, "prepend_unique", UNIQUE_B_AND_A_LISTS, id="list_prepend_unique"),
        # Testing AvdIndexedList
        pytest.param(A_INDEXED_LIST, B_INDEXED_LIST, "append_unique", UNIQUE_A_AND_B_INDEXED_LISTS, id="indexed_list_append_unique"),
        pytest.param(A_INDEXED_LIST, B_INDEXED_LIST, "append", UNIQUE_A_AND_B_INDEXED_LISTS, id="indexed_list_append"),
        pytest.param(A_INDEXED_LIST, B_INDEXED_LIST, "replace", B_INDEXED_LIST, id="indexed_list_replace"),
        pytest.param(A_INDEXED_LIST, B_INDEXED_LIST, "keep", A_INDEXED_LIST, id="indexed_list_keep"),
        pytest.param(A_INDEXED_LIST, B_INDEXED_LIST, "prepend", UNIQUE_B_AND_A_INDEXED_LISTS, id="indexed_list_prepend"),
        pytest.param(A_INDEXED_LIST, B_INDEXED_LIST, "prepend_unique", UNIQUE_B_AND_A_INDEXED_LISTS, id="indexed_list_prepend_unique"),
    ],
)
def test_data_merging(
    a_data: dict,
    b_data: dict,
    list_merge: Literal["append_unique", "append", "replace", "keep", "prepend", "prepend_unique"],
    expected: dict,
    data_merging_schema_class: DataMergingTestSchema,
) -> None:
    a = data_merging_schema_class._from_dict(a_data)
    b = data_merging_schema_class._from_dict(b_data)
    assert a._deepmerged(b, list_merge=list_merge)._as_dict() == expected
