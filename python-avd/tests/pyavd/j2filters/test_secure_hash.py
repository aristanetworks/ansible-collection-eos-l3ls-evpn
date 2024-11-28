# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from __future__ import annotations

import re

import pytest

from pyavd.j2filters import secure_hash

INVALID_PASSWORDS = [
    pytest.param(True, TypeError, "Password MUST be of type 'str' but is of type <class 'bool'>"),
    pytest.param([], TypeError, "Password MUST be of type 'str' but is of type <class 'list'>"),
    pytest.param({"key": "value"}, TypeError, "Password MUST be of type 'str' but is of type <class 'list'>"),
]


VALID_PASSWORDS = [
    pytest.param("arista", r"^\$6\$[A-Za-z0-9\.\\]{16}\$[A-Za-z0-9\.\\\/]{86}"),
    pytest.param("rAnDoM123456789", r"^\$6\$[A-Za-z0-9\.\\]{16}\$[A-Za-z0-9\.\\\/]{86}"),
    pytest.param("aristaCloudvisionUser", r"^\$6\$[A-Za-z0-9\.\\]{16}\$[A-Za-z0-9\.\\\/]{86}"),
    pytest.param("superSecure999", r"^\$6\$[A-Za-z0-9\.\\]{16}\$[A-Za-z0-9\.\\\/]{86}"),
]


class TestSecureHashFilter:
    @pytest.mark.parametrize(("user_password", "expected_raise", "expected_raise_message"), INVALID_PASSWORDS)
    def test_secure_hash_invalid(self, user_password: str, expected_raise: Exception, expected_raise_message: str) -> None:
        with pytest.raises(expected_raise, match=expected_raise_message):
            secure_hash(user_password)

    @pytest.mark.parametrize(("user_password", "regex_of_hashed_password"), VALID_PASSWORDS)
    def test_secure_hash_valid(self, user_password: str, regex_of_hashed_password: str) -> None:
        hashed_password = secure_hash(user_password)
        assert re.fullmatch(regex_of_hashed_password, hashed_password)
