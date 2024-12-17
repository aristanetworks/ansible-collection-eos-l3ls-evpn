# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from __future__ import annotations

import re

import pytest

from pyavd.j2filters import secure_hash

sha512_regex = r"^\$6\$[A-Za-z0-9\.\/]{16}\$[A-Za-z0-9\.\/]{86}"


INVALID_PASSWORDS = [
    pytest.param(True, TypeError, "Password MUST be of type 'str' but is of type <class 'bool'>"),
    pytest.param([], TypeError, "Password MUST be of type 'str' but is of type <class 'list'>"),
    pytest.param({}, TypeError, "Password MUST be of type 'str' but is of type <class 'dict'>"),
]

INVALID_SALTS = [
    pytest.param("password", "DxaFhA,rzqgZV", ValueError, "Salt value MUST only contain the characters ./0-9A-Za-z"),
    pytest.param("password", "abcdefghijklmnopqrs", ValueError, "Salt value length MUST not be greater than 16 characters but is 19"),
    pytest.param("password", [], TypeError, "Salt value MUST be of type 'str' but is of type <class 'list'>"),
]

VALID_PASSWORD_FORMAT = [
    pytest.param("rAnDoM123456789", sha512_regex),
    pytest.param("ar!st@Us95r", sha512_regex),
]

VALID_PASSWORDS = [
    pytest.param("pass", "DxaFhAPPrrOzqgZV", "$6$DxaFhAPPrrOzqgZV$pdiZUeB6SRwVsiTzW1jPQvBy3eP5DqJWjZ1Fd3mpO8E9tjJ/ntaiZx7CaIIkfYyOnzgV92AW7fFSWnQzzowzP."),
    pytest.param("pass123", "LYP1.qA2GBfCkgjG", "$6$LYP1.qA2GBfCkgjG$fKJUO/Rd0WoedrBv1ZQRHJgXAQVto7FiRB7qftH5ojHhhazwjG8r.J54ekLskS6M7ET/jDwhttxub1k4Af.Re1"),
    pytest.param("987pass", "L6FWaPqBAGw9cchr", "$6$L6FWaPqBAGw9cchr$72Aw0G3LEmjzR2JFaC4vKzuB8Y1QhSQWoNAvFeCT0/i1td7LVxcGu/d3C9zBGOufbE.fQa/dRpQVLoFuaM4GH0"),
    pytest.param("@rista", "md1wAfP0nC2/4M8d", "$6$md1wAfP0nC2/4M8d$qlQTd/ShOtMBImVvdXxVo.4MqLFI6BUQHoAqqyUUyKWTdtGi7wMQBqkDCRJ.ZLvotQtOyzYXQGuvc8SsAGyFM1"),
]


class TestSecureHashFilter:
    @pytest.mark.parametrize(("user_password", "expected_raise", "expected_raise_message"), INVALID_PASSWORDS)
    def test_secure_hash_invalid_password(self, user_password: str, expected_raise: Exception, expected_raise_message: str) -> None:
        with pytest.raises(expected_raise, match=expected_raise_message):
            secure_hash(user_password)

    @pytest.mark.parametrize(("user_password", "salt", "expected_raise", "expected_raise_message"), INVALID_SALTS)
    def test_secure_hash_invalid_salt(self, user_password: str, salt: str, expected_raise: Exception, expected_raise_message: str) -> None:
        with pytest.raises(expected_raise, match=expected_raise_message):
            secure_hash(user_password, salt)

    @pytest.mark.parametrize(("user_password", "regex_of_hashed_password"), VALID_PASSWORD_FORMAT)
    def test_secure_hash_password_format(self, user_password: str, regex_of_hashed_password: str) -> None:
        hashed_password = secure_hash(user_password)
        assert re.fullmatch(regex_of_hashed_password, hashed_password)

    @pytest.mark.parametrize(("user_password", "salt", "expected_hash_password"), VALID_PASSWORDS)
    def test_secure_hash_expected_password(self, user_password: str, salt: str, expected_hash_password: str) -> None:
        hashed_password = secure_hash(user_password, salt)
        assert hashed_password == expected_hash_password
