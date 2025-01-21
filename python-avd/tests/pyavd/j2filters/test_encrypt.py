# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from contextlib import AbstractContextManager
from contextlib import nullcontext as does_not_raise

import pytest

from pyavd.j2filters import encrypt


@pytest.mark.parametrize(
    ("password", "passwd_type", "key", "kwargs", "expected_raise"),
    [
        pytest.param("dummy", None, "dummy", {}, pytest.raises(TypeError), id="Missing Type"),
        pytest.param("dummy", "eigrp", "dummy", {}, pytest.raises(KeyError), id="Wrong Type"),
        pytest.param(
            42,
            "bgp",
            "42.42.42.42",  # NOSONAR, IP is just test data
            {},
            does_not_raise(),
            id="Password is not a string",
        ),
        pytest.param(
            "arista",
            "bgp",
            "42.42.42.42",  # NOSONAR, IP is just test data
            {},
            does_not_raise(),
            id="Implemented Type BGP",
        ),
        pytest.param("arista", "ospf_simple", "Ethernet1", {}, does_not_raise(), id="Implemented Type OSPF simple"),
        pytest.param("arista", "ospf_message_digest", "Ethernet1", {"hash_algorithm": "sha512", "key_id": 66}, does_not_raise(), id="Implemented Type OSPF MD"),
    ],
)
def test_encrypt(password: str | int, passwd_type: str | None, key: str, kwargs: dict, expected_raise: AbstractContextManager) -> None:
    """Test encrypt method for non-existing and existing type."""
    with expected_raise:
        encrypt(password, passwd_type=passwd_type, key=key, **kwargs)
