# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.


from typing import Any

import pytest

from pyavd.j2filters import list_compress

LIST_COMPRESS_INVALID_TESTS = [
    ("1-3", "Value must be of type list, got <class 'str'>"),
    ({"key": "value"}, "Value must be of type list, got <class 'dict'>"),
    (33, "Value must be of type list, got <class 'int'>"),
    (["a", "b", "c"], "All elements of the list ['a', 'b', 'c'] must be integers"),
    ([1, "a"], "All elements of the list [1, 'a'] must be integers"),
]

LIST_COMPRESS_VALID_TESTS = [
    ([1, 2, 3, 4], "1-4"),
    ([1, 2, 3, 7, 8], "1-3,7-8"),
    ([9, 10, 11, 4, 2, 1], "1-2,4,9-11"),
]


class TestListCompressFilter:
    @pytest.mark.parametrize(("invalid_list_to_compress", "error_msg"), LIST_COMPRESS_INVALID_TESTS)
    def test_list_compress_invalid(self, invalid_list_to_compress: Any, error_msg: str) -> None:
        with pytest.raises(TypeError) as exc_info:
            list_compress(invalid_list_to_compress)
        assert str(exc_info.value) == error_msg

    @pytest.mark.parametrize(("valid_list_to_compress", "compressed_string"), LIST_COMPRESS_VALID_TESTS)
    def test_list_compress_valid(self, valid_list_to_compress: list, compressed_string: str) -> None:
        resp = list_compress(valid_list_to_compress)
        assert resp in compressed_string
