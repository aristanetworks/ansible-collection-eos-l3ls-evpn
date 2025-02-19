# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import pytest

from pyavd._utils.password_utils import (
    bgp_decrypt,
    bgp_encrypt,
    isis_decrypt,
    isis_encrypt,
    ospf_message_digest_decrypt,
    ospf_message_digest_encrypt,
    ospf_simple_decrypt,
    ospf_simple_encrypt,
)

##########
# BGP
##########

BGP_INPUT_DICT_ENCRYPT_EXPECTED = [
    ("42.42.42.42", "arista", "3QGcqpU2YTwKh2jVQ4Vj/A=="),  # NOSONAR, IP is just test data
    ("AVD-TEST", "arista", "bM7t58t04qSqLHAfZR/Szg=="),
]
# password used is "arista"
BGP_VALID_INPUT_DICT_DECRYPT_EXPECTED = [
    ("42.42.42.42", "3QGcqpU2YTwKh2jVQ4Vj/A==", "arista"),  # NOSONAR, IP is just test data
    ("AVD-TEST", "bM7t58t04qSqLHAfZR/Szg==", "arista"),
]
BGP_INVALID_INPUT_DICT_DECRYPT = [
    ("10.42.42.43", "3QGcqpU2YTwKh2jVQ4Vj/A=="),  # NOSONAR, IP is just test data
    ("AVD-TEST-DUMMY", "bM7t58t04qSqLHAfZR/Szg=="),
]
# The following list uses all the molecule BGP passwords available
# and the expected encryption
# The password is always arista123
BGP_MOLECULE_PASSWORDS_TEST = [
    ("UNDERLAY-PEERS", "arista123", "0nsCUm70mvSTxVO0ldytrg=="),
    ("UNDERLAY_PEERS", "arista123", "af6F4WLl4wUrWRZcwbEwkQ=="),
    ("123.1.1.10", "arista123", "oBztv71m2uhR7hh58/OCNA=="),  # NOSONAR, IP is just test data
    ("123.1.1.11", "arista123", "oBztv71m2uhR7hh58/OCNA=="),  # NOSONAR, IP is just test data
    ("MPLS-IBGP-PEERS", "arista123", "mWV4B6WpLCfOTyKATLWuBg=="),
    ("EVPN-OVERLAY-RS-PEERS", "arista123", "dRx9sULvl+hzkCMYJLEQCw=="),
    ("EVPN-OVERLAY", "arista123", "MY+KbyJy4kSu+X/blnVwsg=="),
    ("IPV4-UNDERLAY", "arista123", "dt5J2fw8tymeDFPyoYLB3w=="),
    ("IPV6-UNDERLAY", "arista123", "WkH9/oj4atEwv2MgOprY8A=="),
    ("IPV6-UNDERLAY-MLAG", "arista123", "CXS0NveSYzQRmm6SRGp42w=="),
    ("IPV4-UNDERLAY-MLAG", "arista123", "46jF9S9T7v5RRceVzhrlBg=="),
    ("MPLS-OVERLAY-PEERS", "arista123", "SHsTgDgjVUU5a9blyxSt3Q=="),
    ("192.168.48.1", "arista123", "toZKiUFLVUTU4hdS5V8F4Q=="),  # NOSONAR, IP is just test data
    ("192.168.48.3", "arista123", "OajzUG59/YF0NkgvOQyRnQ=="),  # NOSONAR, IP is just test data
    ("MLAG-PEERS", "arista123", "15AwQNBEJ1nyF/kBEtoAGw=="),
    ("OVERLAY-PEERS", "arista123", "64fqSH5CFUNLRHErezMrRg=="),
    ("RR-OVERLAY-PEERS", "arista123", "04FdfTXWrEfpDTUc3mlSjg=="),
    ("MLAG_PEER", "arista123", "arwUnrq9ydqIhjfTwRhAlg=="),
]
OSPF_MESSAGE_DIGEST_HASH_ALGORITHMS = ["md5", "sha1", "sha256", "sha384", "sha512"]


@pytest.mark.parametrize(("key", "password", "expected"), BGP_INPUT_DICT_ENCRYPT_EXPECTED)
def test_bgp_encrypt(key: str, password: str, expected: str) -> None:
    """Test bgp_encrypt."""
    assert bgp_encrypt(password, key=key) == expected


@pytest.mark.parametrize(("key", "password", "expected"), BGP_VALID_INPUT_DICT_DECRYPT_EXPECTED)
def test_bgp_decrypt_success(key: str, password: str, expected: str) -> None:
    """Test bgp_decrypt successful cases."""
    assert bgp_decrypt(password, key=key) == expected


@pytest.mark.parametrize(("key", "password"), BGP_INVALID_INPUT_DICT_DECRYPT)
def test_bgp_decrypt_failure(key: str, password: str) -> None:
    """Test bgp_decrypt failure cases."""
    with pytest.raises(ValueError):  # noqa: PT011
        bgp_decrypt(password, key=key)


@pytest.mark.parametrize(("key", "password", "expected"), BGP_MOLECULE_PASSWORDS_TEST)
def test_molecule_bgp_encrypt(key: str, password: str, expected: str) -> None:
    """Test bgp_encrypt."""
    assert bgp_encrypt(password, key=key) == expected


##########
# OSPF
##########
OSPF_INPUT_SIMPLE_DICT_ENCRYPT_EXPECTED = [
    ("Ethernet1", "arista", "qCTcuwOSntAmLZaW2QjKcA=="),
]
# password used is "arista"
OSPF_VALID_INPUT_SIMPLE_DICT_DECRYPT_EXPECTED = [
    ("Ethernet1", "qCTcuwOSntAmLZaW2QjKcA==", "arista"),
]
OSPF_INVALID_INPUT_SIMPLE_DICT_DECRYPT = [
    pytest.param("Ethernet1", "3QGcqpU2YTwKh2jVQ4Vj/A==", id="Wrong password simple auth"),
]
OSPF_INPUT_MD_DICT_ENCRYPT_EXPECTED = [
    ("Ethernet1", "arista", "md5", 42, "aPW9RqfXquTBASVDMYxSJw=="),
    ("Ethernet1", "arista", "sha512", 66, "tDvJjUyf8///ktvy/xpfeQ=="),
]
# password used is "arista"
OSPF_VALID_INPUT_MD_DICT_DECRYPT_EXPECTED = [
    ("Ethernet1", "aPW9RqfXquTBASVDMYxSJw==", "md5", 42, "arista"),
    ("Ethernet1", "tDvJjUyf8///ktvy/xpfeQ==", "sha512", 66, "arista"),
]
OSPF_INVALID_INPUT_MD_DICT_DECRYPT = [
    pytest.param("Ethernet1", "bM7t58t04qSqLHAfZR/Szg==", "sha512", 42, id="Wrong password message digest key"),
    pytest.param("Ethernet1", "bM7t58t04qSqLHAfZR/Szg==", "sha512", None, id="Missing key id"),
    pytest.param("Ethernet1", "bM7t58t04qSqLHAfZR/Szg==", None, 42, id="Missing hash_algorithm"),
    pytest.param("Ethernet1", "bM7t58t04qSqLHAfZR/Szg==", "sha666", 42, id="Wrong hash_algorithm"),
]
# The following list uses all the molecule OSPF passwords available
# and the expected encryption
# The password is always arista123
# TODO: OSPF_MOLECULE_PASSWORDS_TEST = []


@pytest.mark.parametrize(("key", "password", "expected"), OSPF_INPUT_SIMPLE_DICT_ENCRYPT_EXPECTED)
def test_ospf_simple_encrypt(key: str, password: str, expected: str) -> None:
    """Test ospf_simple_encrypt."""
    assert ospf_simple_encrypt(password, key=key) == expected


@pytest.mark.parametrize(("key", "password", "expected"), OSPF_VALID_INPUT_SIMPLE_DICT_DECRYPT_EXPECTED)
def test_ospf_simple_decrypt_success(key: str, password: str, expected: str) -> None:
    """Test ospf_simple_decrypt successful cases."""
    assert ospf_simple_decrypt(password, key=key) == expected


@pytest.mark.parametrize(("key", "password"), OSPF_INVALID_INPUT_SIMPLE_DICT_DECRYPT)
def test_ospf_simple_decrypt_failure(key: str, password: str) -> None:
    """Test ospf_simple_decrypt failure cases."""
    with pytest.raises(ValueError):  # noqa: PT011
        ospf_simple_decrypt(password, key=key)


@pytest.mark.parametrize(("key", "password", "hash_algorithm", "key_id", "expected"), OSPF_INPUT_MD_DICT_ENCRYPT_EXPECTED)
def test_ospf_message_digest_encrypt(key: str, password: str, expected: str, hash_algorithm: str, key_id: str) -> None:
    """Test ospf_message_digest_encrypt."""
    assert ospf_message_digest_encrypt(password, key=key, hash_algorithm=hash_algorithm, key_id=key_id) == expected


@pytest.mark.parametrize(("key", "password", "hash_algorithm", "key_id", "expected"), OSPF_VALID_INPUT_MD_DICT_DECRYPT_EXPECTED)
def test_ospf_message_digest_decrypt_success(key: str, password: str, hash_algorithm: str, key_id: str, expected: str) -> None:
    """Test ospf_message_digest_decrypt successful cases."""
    assert ospf_message_digest_decrypt(password, key=key, hash_algorithm=hash_algorithm, key_id=key_id) == expected


@pytest.mark.parametrize(("key", "password", "hash_algorithm", "key_id"), OSPF_INVALID_INPUT_MD_DICT_DECRYPT)
def test_ospf_message_digest_decrypt_failure(key: str, password: str, hash_algorithm: str, key_id: str) -> None:
    """Test ospf_message_digest_decrypt failure cases."""
    if hash_algorithm is None or key_id is None:
        with pytest.raises(ValueError, match="For OSPF message digest keys, both hash_algorithm and key_id are required"):
            ospf_message_digest_encrypt(password, key=key, hash_algorithm=hash_algorithm, key_id=key_id)
    elif hash_algorithm not in OSPF_MESSAGE_DIGEST_HASH_ALGORITHMS:
        with pytest.raises(ValueError, match=f"For OSPF message digest keys, `hash_algorithm` must be in {'|'.join(OSPF_MESSAGE_DIGEST_HASH_ALGORITHMS)}"):
            ospf_message_digest_encrypt(password, key=key, hash_algorithm=hash_algorithm, key_id=key_id)


##########
# ISIS
##########
ISIS_INPUT_EXPECTED = [
    # password used is "arista"
    # (key (ISIS Instance name), mode, password, encrypted_password)
    ("test", "none", "arista", "hY+wzlrNzMvQ9wSWDgN4LQ=="),
    ("", "none", "arista", "7h4BlaA7By3z4DS4JcikPQ=="),
    ("", "text", "arista", "VC8nPxnXqNN2KI3k+m0uTw=="),
    ("test", "text", "arista", "MMoVrmED9QBzNX4VWjknKQ=="),
    ("", "sha", "arista", "32qevp9HovmOQ7PGBI/Eiw=="),
    ("test", "sha", "arista", "eEepxKOs2HDJdRVO8JXufg=="),
    ("", "md5", "arista", "Xe8ywYMTkcpNrvJCQ+qXOg=="),
    ("test", "md5", "arista", "IL5p7lzM3hEaLFRduo6Ypg=="),
    ("", "sha-1", "arista", "I8FDDBTK3uNtsb7nFAJa5Q=="),
    ("test", "sha-1", "arista", "R1kVx0uewexSn4faCIDoRg=="),
    ("", "sha-224", "arista", "T2GR2UVUI/OBlBbcTYLU3A=="),
    ("test", "sha-224", "arista", "F0L0RDFPOwjY3V8+ipXygQ=="),
    ("", "sha-256", "arista", "YMugwMTs91tlqsLV0GmCoQ=="),
    ("test", "sha-256", "arista", "10tBVHGUNO3i1sD5SvHoPA=="),
    ("", "sha-384", "arista", "m1SXF59lXikxlPwJZUYO1w=="),
    ("test", "sha-384", "arista", "RvmoSqQYrlsLJb7/eV3tYQ=="),
    ("", "sha-512", "arista", "vC1eGC70oNIHly729wfi2g=="),
    ("test", "sha-512", "arista", "dGP9ycyN4QCHv9wfPVkzbg=="),
]

ISIS_INVALID_INPUT_DECRYPT = [
    pytest.param("test", "none", "3QGcqpU2YTwKh2jVQ4Vj/A==", id="Wrong password"),
]


@pytest.mark.parametrize(("key", "mode", "password", "encrypted_password"), ISIS_INPUT_EXPECTED)
def test_isis_encrypt(key: str, mode: str, password: str, encrypted_password: str) -> None:
    """Test isis_encrypt."""
    assert isis_encrypt(password, key=key, mode=mode) == encrypted_password


@pytest.mark.parametrize(("key", "mode", "password", "encrypted_password"), ISIS_INPUT_EXPECTED)
def test_isis_decrypt_success(key: str, mode: str, password: str, encrypted_password: str) -> None:
    """Test isis_decrypt successful cases."""
    assert isis_decrypt(encrypted_password, key=key, mode=mode) == password


@pytest.mark.parametrize(("key", "mode", "password"), ISIS_INVALID_INPUT_DECRYPT)
def test_isis_decrypt_failure(key: str, mode: str, password: str) -> None:
    """Test isis_decrypt failure cases."""
    with pytest.raises(ValueError):  # noqa: PT011
        isis_decrypt(password, key=key, mode=mode)
