# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Used by Encrypt / Decrypt filters."""

from __future__ import annotations

import random
from typing import Any

from .password_utils import cbc_decrypt, cbc_encrypt


def _validate_password_and_key(password: Any, key: str) -> None:
    """
    Validates the password and key values.

    Args:
        password (str): The password to validate.
        key (str): The key to validate.

    Raises:
        ValueError: If the key or password is missing.
        TypeError: If the password is not of type `str`.
    """
    if not key:
        msg = "Key is required for encryption"
        raise ValueError(msg)

    if not password:
        msg = "Password is required for encryption"
        raise ValueError(msg)

    if not isinstance(password, str):
        msg = f"Password MUST be of type 'str' but is of type {type(password)}"
        raise TypeError(msg)


##############
# OSPF
##############
def ospf_simple_encrypt(password: str, key: str) -> str:
    """
    Encrypt a password for OSPF simple authentication.

    Args:
        password (str): The password to be encrypted.
        key (str): The interface name, e.g., "Ethernet1".

    Returns:
        str: The encrypted password as a base64-encoded string.

    Raises:
        ValueError: If the key or password is missing.
        TypeError: If the password is not of type `str`.
    """
    _validate_password_and_key(password, key)

    data = bytes(password, encoding="UTF-8")
    key_b = bytes(f"{key}_passwd", encoding="UTF-8")

    return cbc_encrypt(key_b, data).decode()


def ospf_simple_decrypt(password: str, key: str) -> str:
    """
    Decrypt a password for OSPF simple authentication.

    Args:
        password (str): The encrypted password to be decrypted.
        key (str): The interface name, e.g., "Ethernet1".

    Returns:
        str: The decrypted password as a string.

    Raises:
        ValueError: If decryption fails.
        ValueError: If the key or password is missing.
        TypeError: If the password is not of type `str`.
    """
    _validate_password_and_key(password, key)

    data = bytes(password, encoding="UTF-8")
    key_b = bytes(f"{key}_passwd", encoding="UTF-8")

    try:
        return cbc_decrypt(key_b, data).decode()
    except Exception as exc:
        msg = "OSPF password decryption failed - check the input parameters"
        raise ValueError(msg) from exc


OSPF_MESSAGE_DIGEST_HASH_ALGORITHMS = ["md5", "sha1", "sha256", "sha384", "sha512"]


def ospf_message_digest_encrypt(password: str, key: str, hash_algorithm: str | None = None, key_id: str | None = None) -> str:
    """
    Encrypt a password for Message Digest Keys.

    Args:
        password (str): The password to be encrypted.
        key (str): The interface name, e.g., "Ethernet1".
        hash_algorithm (str, optional): The hash algorithm to use. Must be one of ["md5", "sha1", "sha256", "sha384", "sha512"].
        key_id (str, optional): The key ID to use.

    Returns:
        str: The encrypted password as a base64-encoded string.

    Raises:
        ValueError: If `hash_algorithm` or `key_id` is not provided.
        ValueError: If `hash_algorithm` is not one of the allowed values.
        ValueError: If the key or password is missing.
        TypeError: If the password is not of type `str`.
    """
    _validate_password_and_key(password, key)
    if hash_algorithm is None or key_id is None:
        msg = "For OSPF message digest keys, both hash_algorithm and key_id are required"
        raise ValueError(msg)
    if hash_algorithm not in OSPF_MESSAGE_DIGEST_HASH_ALGORITHMS:
        msg = f"For OSPF message digest keys, `hash_algorithm` must be in {OSPF_MESSAGE_DIGEST_HASH_ALGORITHMS}"
        raise ValueError(msg)

    data = bytes(password, encoding="UTF-8")
    key_b = bytes(f"{key}_{hash_algorithm}Key_{key_id}", encoding="UTF-8")

    return cbc_encrypt(key_b, data).decode()


def ospf_message_digest_decrypt(password: str, key: str, hash_algorithm: str | None = None, key_id: str | None = None) -> str:
    """
    Decrypt a password for Message Digest Keys.

    Args:
        password (str): The encrypted password to be decrypted.
        key (str): The interface name, e.g., "Ethernet1".
        hash_algorithm (str, optional): The hash algorithm used for encryption. Must be one of ["md5", "sha1", "sha256", "sha384", "sha512"].
        key_id (str, optional): The key ID used for encryption.

    Returns:
        str: The decrypted password as a string.

    Raises:
        ValueError: If `hash_algorithm` or `key_id` is not provided.
        ValueError: If `hash_algorithm` is not one of the allowed values.
        ValueError: If decryption fails.
        ValueError: If the key or password is missing.
        TypeError: If the password is not of type `str`.
    """
    _validate_password_and_key(password, key)
    if hash_algorithm is None or key_id is None:
        msg = "For OSPF message digest keys, both hash_algorithm and key_id are required"
        raise ValueError(msg)
    if hash_algorithm not in OSPF_MESSAGE_DIGEST_HASH_ALGORITHMS:
        msg = f"For OSPF message digest keys, `hash_algorithm` must be in {OSPF_MESSAGE_DIGEST_HASH_ALGORITHMS}"
        raise ValueError(msg)

    data = bytes(password, encoding="UTF-8")
    key_b = bytes(f"{key}_{hash_algorithm}Key_{key_id}", encoding="UTF-8")

    try:
        return cbc_decrypt(key_b, data).decode()
    except Exception as exc:
        msg = "OSPF password decryption failed - check the input parameters"
        raise ValueError(msg) from exc


##############
# BGP
##############
def bgp_encrypt(password: str, key: str) -> str:
    """
    Encrypts a password for BGP (Border Gateway Protocol) authentication.

    Args:
        password (str): The password to be encrypted.
        key (str): The key used for encryption, derived from either <PEER_GROUP_NAME> or <NEIGHBOR_IP>.

    Returns:
        str: The encrypted password as a base64-encoded string.

    Raises:
        ValueError: If the key or password is missing.
        TypeError: If the password is not of type `str`.
    """
    _validate_password_and_key(password, key)

    data = bytes(password, encoding="UTF-8")
    key = bytes(f"{key}_passwd", encoding="UTF-8")

    return cbc_encrypt(key, data).decode()


def bgp_decrypt(password: str, key: str) -> str:
    """
    Decrypts a password for BGP (Border Gateway Protocol) authentication.

    Args:
        password (str): The encrypted password to be decrypted.
        key (str): The key used for decryption, derived from either <PEER_GROUP_NAME> or <NEIGHBOR_IP>.

    Returns:
        str: The decrypted password as a string.

    Raises:
        ValueError: If decryption fails.
        ValueError: If the key or password is missing.
        TypeError: If the password is not of type `str`.
    """
    _validate_password_and_key(password, key)

    data = bytes(password, encoding="UTF-8")
    key = bytes(f"{key}_passwd", encoding="UTF-8")

    try:
        return cbc_decrypt(key, data).decode()
    except Exception as exc:
        msg = "BGP password decryption failed - check the input parameters"
        raise ValueError(msg) from exc


##############
# ISIS
##############
_ISIS_MODE_MAP = {
    "none": "noAuth",
    "text": "clearText",
    "md5": "md5",
    "sha": "sha",
    "sha-1": "sha_1",
    "sha-224": "sha_224",
    "sha-256": "sha_256",
    "sha-384": "sha_384",
    "sha-512": "sha_512",
}


def _validate_isis_args(password: str, key: str, mode: str) -> None:
    """
    Validates the arguments for ISIS (Intermediate System to Intermediate System) encryption/decryption.

    Args:
        password (str): The password to be encrypted/decrypted.
        key (str): The key used for encryption/decryption.
        mode (str): The mode of operation for encryption/decryption, which should be one of the options in `_ISIS_MODE_MAP`.

    Raises:
        ValueError: If `password` is empty or missing.
        TypeError: If `password` is not of type `str`.
        TypeError: If `key` is not of type `str`.
        TypeError: If `mode` is not of type `str` or is not one of the valid options in `_ISIS_MODE_MAP`.
        ValueError: If `mode` is empty or missing.
    """
    if not password:
        msg = "Password is required for encryption/decryption"
        raise ValueError(msg)

    if not isinstance(password, str):
        msg = f"Password MUST be of type 'str' but is of type {type(password)}"
        raise TypeError(msg)

    if not isinstance(key, str):
        msg = f"Key MUST be of type 'str' but is of type {type(key)}"
        raise TypeError(msg)

    if not isinstance(mode, str):
        msg = f"Mode MUST be a string with one of the following options: {list(_ISIS_MODE_MAP)}. Got '{mode}'."
        raise TypeError(msg)

    if not mode:
        msg = "Mode is required for encryption/decryption"
        raise ValueError(msg)


def _get_isis_key(key: str, mode: str) -> bytes:
    """
    Constructs a key for ISIS (Intermediate System to Intermediate System) encryption/decryption.

    Args:
        key (str): The base key string.
        mode (str): The mode of operation, which determines how the key is formatted.

    Returns:
        bytes: The constructed key as bytes.
    """
    return bytes(f"{key}_{_ISIS_MODE_MAP[mode]}", encoding="UTF-8")


def isis_encrypt(password: str, key: str, mode: str) -> str:
    """
    Encrypt a password for ISIS authentication.

    Args:
        password: Password as string
        key: ISIS instance name as string.
        mode: 'none', 'text', 'md5' or 'sha' or for shared-secret mode 'sha-1', 'sha-224', 'sha-256', 'sha-384', 'sha-512'.

    Returns:
        str: The encrypted password as a string.
    """
    _validate_isis_args(password, key, mode)

    data = bytes(password, encoding="UTF-8")

    return cbc_encrypt(_get_isis_key(key, mode), data).decode()


def isis_decrypt(password: str, key: str, mode: str) -> str:
    """
    Decrypt a password for ISIS authentication.

    Args:
        password (str): The encrypted password to be decrypted.
        key (str): The ISIS instance name used to derive the decryption key.
        mode (str): Specifies the decryption mode. Can be one of:
            - 'none': No encryption.
            - 'text': Plain text (no decryption needed, but processed accordingly).
            - 'md5': MD5 hash decryption.
            - 'sha': SHA-1 hash decryption.
            - 'sha-1', 'sha-224', 'sha-256', 'sha-384', 'sha-512': Various SHA hash decryptions.

    Returns:
        str: The decrypted password as a string.

    Raises:
        ValueError: If decryption fails for any reason.
    """
    _validate_isis_args(password, key, mode)

    data = bytes(password, encoding="UTF-8")

    try:
        return cbc_decrypt(_get_isis_key(key, mode), data).decode()
    except Exception as exc:
        msg = "ISIS password decryption failed - check the input parameters"
        raise ValueError(msg) from exc


###############
# Simple type 7
###############
SIMPLE_7_SEED = b"dsfd;kfoA,.iyewrkldJKDHSUBsgvca69834ncxv9873254k;fg87"


def simple_7_decrypt(data: str) -> str:
    """
    Decrypt (deobfuscate) a password from insecure type-7.

    Args:
        data: The encrypted password

    Returns:
        str: The decrypted password as a string.
    """
    salt = int(data[0:2])
    secret = bytearray.fromhex(data[2:])
    return bytes(char ^ (SIMPLE_7_SEED[(salt + i) % 53]) for i, char in enumerate(secret)).decode("UTF-8")


def simple_7_encrypt(data: str, salt: int | None = None) -> str:
    """
    Encrypt (obfuscate) a password with insecure type-7.

    Args:
        data: The clear text password
        salt: Optionally a number within the range 0-15. If not set, a random salt will be used.

    Returns:
        str: The encrypted password as a string.
    """
    if salt is None:
        # Accepting SonarLint issue: Pseudo random is ok since this is simply creating a visible salt
        salt = random.randint(0, 15)  # NOSONAR # noqa: S311
    cleartext = data.encode("UTF-8")
    return f"{salt:02}" + bytearray(char ^ (SIMPLE_7_SEED[(salt + i) % 53]) for i, char in enumerate(cleartext)).hex().upper()
