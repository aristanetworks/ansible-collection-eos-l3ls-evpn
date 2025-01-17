# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
import pytest

from pyavd._cv.client.async_decorators import LimitCvVersion, grpc_msg_size_handler
from pyavd._cv.client.exceptions import CVMessageSizeExceeded
from pyavd._cv.client.versioning import CVAAS_VERSION_STRING, CvVersion

INVALID_VERSION_TESTS = [
    # version , expected_exception
    pytest.param("2023.1.0", LookupError("Unsupported version of CloudVision: '2023.1.0'."), id="invalid_version"),
    pytest.param("223.1.0", ValueError("Invalid CV Version '223.1.0'. The version must conform to the pattern '.+'"), id="invalid_version_syntax_1"),
    pytest.param("cvaas", ValueError("Invalid CV Version 'cvaas'. The version must conform to the pattern '.+'"), id="invalid_version_syntax_2"),
]

VALID_VERSION_TESTS = [
    # Format: version , expected_response (matched_min_ver, matched_max_ver)
    pytest.param("2024.1.0", ("2024.1.0", "2024.1.99"), id="valid_version_1"),
    pytest.param("2024.1.5", ("2024.1.0", "2024.1.99"), id="valid_version_2"),
    pytest.param("2025.42.25", ("2025.1.0", "2025.99.99"), id="valid_version_3"),
    pytest.param(CVAAS_VERSION_STRING, (CVAAS_VERSION_STRING, CVAAS_VERSION_STRING), id="valid_version_4"),
]

MSG_SIZE_HANDLER_TESTS = [
    # Format: data, max_len, expected_response (list of ints where each entry is one execution and the int is the number of entries covered)
    pytest.param([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, [5, 5], id="equal_sized_chunks_1"),
    pytest.param([1, 2, 3, 4, 5, 6, 7, 8, 9], 3, [3, 3, 3], id="equal_sized_chunks_2"),
    pytest.param([1, 2, 3, 4, 5, 6, 7, 8, 9], 1, [1, 1, 1, 1, 1, 1, 1, 1, 1], id="equal_sized_chunks_3"),
    # The items are chunked by calculating a ratio. This ratio rounds up, so the number of items per message is rounded down. So numbers below can look funny.
    # This is on purpose since this is actually variable sized items in bytes fitting into messages of 10MB.
    # We wish to pack many but also avoid many attempts stepping over the boundary.
    pytest.param([1, 2, 3, 4, 5, 6, 7, 8, 9], 4, [3, 3, 3], id="variable_sized_chunks_1"),
    pytest.param([1, 2, 3, 4, 5, 6, 7, 8, 9], 5, [4, 4, 1], id="variable_sized_chunks_2"),
]


class CvClass:
    _cv_version: CvVersion

    def __init__(self, version: CvVersion) -> None:
        self._cv_version = version

    @LimitCvVersion(min_ver="2024.1.0", max_ver="2024.1.99")
    async def version_limited_method(self) -> tuple[str, str]:
        return ("2024.1.0", "2024.1.99")

    @LimitCvVersion(min_ver="2024.2.0", max_ver="2024.99.99")
    async def version_limited_method(self) -> tuple[str, str]:  # noqa: F811
        return ("2024.2.0", "2024.99.99")

    @LimitCvVersion(min_ver="2025.1.0", max_ver="2025.99.99")
    async def version_limited_method(self) -> tuple[str, str]:  # noqa: F811
        return ("2025.1.0", "2025.99.99")

    @LimitCvVersion(min_ver=CVAAS_VERSION_STRING, max_ver=CVAAS_VERSION_STRING)
    async def version_limited_method(self) -> tuple[str, str]:  # noqa: F811
        return (CVAAS_VERSION_STRING, CVAAS_VERSION_STRING)

    @grpc_msg_size_handler(list_field="field")
    async def msgsize_limited_method(self, field: list, max_accepted_len: int) -> list[bool]:
        # Check if the number of entries is higher than the max accepted length and raise.
        if len(field) > max_accepted_len:
            e = CVMessageSizeExceeded("Too long")
            e.max_size = max_accepted_len
            e.size = len(field)
            raise e

        # return list with len of fields for this execution.
        return [len(field)]


@pytest.mark.asyncio
@pytest.mark.parametrize(("version", "expected_exception"), INVALID_VERSION_TESTS)
async def test_invalid_versions(version: str, expected_exception: Exception) -> None:
    with pytest.raises(type(expected_exception), match=expected_exception.args[0]):
        await CvClass(CvVersion(version)).version_limited_method()


@pytest.mark.asyncio
@pytest.mark.parametrize(("version", "expected_response"), VALID_VERSION_TESTS)
async def test_valid_versions(version: str, expected_response: tuple[str, str]) -> None:
    resp = await CvClass(CvVersion(version)).version_limited_method()
    assert resp == expected_response


@pytest.mark.asyncio
@pytest.mark.parametrize(("data", "max_len", "expected_response"), MSG_SIZE_HANDLER_TESTS)
async def test_msg_size_handler(data: list, max_len: int, expected_response: list[int]) -> None:
    resp = await CvClass(CvVersion(CVAAS_VERSION_STRING)).msgsize_limited_method(field=data, max_accepted_len=max_len)
    assert resp == expected_response


@pytest.mark.asyncio
async def test_msg_size_handler_invalid_fuction_return_type() -> None:
    def function_not_returning_list(_field: list) -> str:
        return "foo"

    with pytest.raises(TypeError, match="grpc_msg_size_handler decorator is unable to bind to the function .+"):
        await grpc_msg_size_handler(list_field="_field")(function_not_returning_list)(["foo", "bar"])


@pytest.mark.asyncio
async def test_msg_size_handler_invalid_fuction_list_field() -> None:
    def function_with_wrong_arg(_wrong_field: list) -> list:
        return ["foo"]

    with pytest.raises(KeyError, match="grpc_msg_size_handler decorator is unable to find the list_field .+"):
        await grpc_msg_size_handler(list_field="_field")(function_with_wrong_arg)(["foo", "bar"])
