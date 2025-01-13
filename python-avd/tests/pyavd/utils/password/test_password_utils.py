# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import pytest

from pyavd._utils.password_utils.password_utils import cbc_check_password, cbc_decrypt, cbc_encrypt

# password used is "arista"
VALID_PASSWORD_KEY_PAIRS = [
    ("42.42.42.42", b"3QGcqpU2YTwKh2jVQ4Vj/A=="),  # NOSONAR, IP is just test data
    ("AVD-TEST", b"bM7t58t04qSqLHAfZR/Szg=="),
]
INVALID_PASSWORD_KEY_PAIRS = [
    ("10.42.42.43", b"3QGcqpU2YTwKh2jVQ4Vj/A=="),  # NOSONAR, IP is just test data
    ("AVD-TEST-DUMMY", b"bM7t58t04qSqLHAfZR/Szg=="),
]


@pytest.mark.parametrize(("key", "expected"), VALID_PASSWORD_KEY_PAIRS)
def test_cbc_encrypt(key: str, expected: bytes) -> None:
    """Valid cases for both neighbor IP and peer group name."""
    augmented_key = bytes(f"{key}_passwd", encoding="utf-8")
    assert cbc_encrypt(augmented_key, b"arista") == expected


@pytest.mark.parametrize(("key", "password"), VALID_PASSWORD_KEY_PAIRS)
def test_cbc_decrypt(key: str, password: bytes) -> None:
    """Valid cases for both neighbor IP and peer group name."""
    augmented_key = bytes(f"{key}_passwd", encoding="utf-8")
    assert cbc_decrypt(augmented_key, password) == b"arista"


@pytest.mark.parametrize(
    ("key", "password", "expected_raise"),
    [
        pytest.param("TOTO", b"3QGcqpU2YTwKh2jVQ4Vj/A==", ValueError, id="ValueError"),
    ],
)
def test_cbc_decrypt_failure(key: str, password: bytes, expected_raise: type[Exception]) -> None:
    """Valid cases for both neighbor IP and peer group name."""
    augmented_key = bytes(f"{key}_passwd", encoding="utf-8")
    with pytest.raises(expected_raise):
        cbc_decrypt(augmented_key, password)


@pytest.mark.parametrize(("key", "password"), VALID_PASSWORD_KEY_PAIRS)
def test_cbc_check_password_success(key: str, password: bytes) -> None:
    """Valid cases for both neighbor IP and peer group name."""
    augmented_key = bytes(f"{key}_passwd", encoding="utf-8")
    assert cbc_check_password(augmented_key, password) is True


@pytest.mark.parametrize(("key", "password"), INVALID_PASSWORD_KEY_PAIRS)
def test_cbc_check_password_invalid_values(key: str, password: bytes) -> None:
    """Invalid cases for both neighbor IP and peer group name."""
    augmented_key = bytes(f"{key}_passwd", encoding="utf-8")
    assert cbc_check_password(augmented_key, password) is False
