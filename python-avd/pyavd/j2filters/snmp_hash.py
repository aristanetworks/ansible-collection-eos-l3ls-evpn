# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

import hashlib

_PRIV_KEY_LENGTH = {"des": 128, "aes": 128, "aes192": 192, "aes256": 256}


def _get_hash_object(auth_type: str) -> object:
    """
    :param auth_type: a string in [md5|sha|sha224|sha256|sha384|sha512]

    :return: an instance of hashlib Hash object corresponding to the
             auth_type

    :raises: AristaAvdError, when the auth_type is not valid
    """
    auth = "sha1" if auth_type == "sha" else auth_type
    try:
        return hashlib.new(auth)
    except ValueError:
        msg = f"{auth_type} is not a valid Auth algorithm for SNMPv3"
        raise ValueError(msg) from ValueError


def _key_from_passphrase(passphrase: str, auth_type: str) -> str:
    """
    RFC 2574 section A.2 algorithm.

    https://www.rfc-editor.org/rfc/rfc2574.html#appendix-A2.

    :param passphrase: the passphrase to use to generate the key
    :param auth_type: a string in [md5|sha|sha224|sha256|sha384|sha512]

    :return: the key generated from the passphrase using auth_type as per
             the algorithm described in the RFC.

    :raises: AristaAvdError, when the auth_type is not valid
    """
    b_passphrase = passphrase
    if isinstance(passphrase, str):
        b_passphrase = passphrase.encode("UTF-8", errors="strict")
    hash_object = _get_hash_object(auth_type)
    count = 0
    password_index = 0
    password_length = len(b_passphrase)
    while count < 1048576:
        cp = bytearray()
        for _ in range(64):
            cp.append(b_passphrase[password_index % password_length])
            password_index += 1
        hash_object.update(cp)
        count += 64
    return hash_object.hexdigest()


def _localize_passphrase(passphrase: str, auth_type: str, engine_id: str, priv_type: str | None = None) -> str:
    """
    Key localization as described in RFC 2574, section 2.6.

    https://www.rfc-editor.org/rfc/rfc2574.html#section-2.6.

    :param passphrase: the passphrase to localize, if priv_type is None
                       it is the auth passphrase else it is the priv
                       passphrase
    :param auth_type: a string in [md5|sha|sha224|sha256|sha384|sha512]
    :param engine_id: an hexadecimal string containing the engine_id to be
                      used to localize the key
    :param auth_type: an optional argument indicating the priv algorithm
                    in [des|aes|aes192|aes256]

    :return: the localized key generated from the passphrase using auth_type
             and if required truncated to match the appropriate keylength for
             the priv_type.

    :raises: AristaAvdError, when the auth_type or priv_type is not valid
             or if the engined_id is not a proper hexadecimal string
    """
    key = bytes.fromhex(_key_from_passphrase(passphrase, auth_type))
    hash_object = _get_hash_object(auth_type)
    try:
        hash_object.update(key + bytes.fromhex(engine_id) + key)
    except ValueError as error:
        msg = f"engine ID {engine_id} is not an hexadecimal string"
        raise ValueError(msg) from error
    localized_key = hash_object.hexdigest()
    if priv_type is not None:
        try:
            while len(localized_key) * 4 < _PRIV_KEY_LENGTH[priv_type]:
                hash_object = _get_hash_object(auth_type)
                hash_object.update(bytes.fromhex(localized_key))
                localized_key = localized_key + hash_object.hexdigest()
            # Truncate ithe key if required
            localized_key = localized_key[: _PRIV_KEY_LENGTH[priv_type] // 4]
        except KeyError as error:
            msg = f"{priv_type} is not a valid Priv algorithm for SNMPv3"
            raise ValueError(msg) from error
    return localized_key


def snmp_hash(input_dict: dict) -> str:
    passphrase = input_dict["passphrase"]
    auth_type = input_dict["auth"]
    engine_id = input_dict["engine_id"]
    priv_type = input_dict.get("priv")
    return _localize_passphrase(passphrase, auth_type, engine_id, priv_type)
