# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

import re

from pyavd._errors import AristaAvdError

try:
    from passlib.hash import sha512_crypt
except ImportError as imp_exc:
    raise AristaAvdError(imp_exc) from imp_exc


def _validate_salt(salt: str | None) -> None:
    """
    Validate a given salt value.

    Args:
        salt: The salt value provided by the user.

    Raises:
        TypeError: If the salt is not of type `str`.
        ValueError: If the salt is greater than 16 characters.
        ValueError: If the salt contains a character not matching ./0-9A-Za-z
    """
    if salt is not None and not isinstance(salt, str):
        msg = f"Salt value MUST be of type 'str' but is of type {type(salt)}"
        raise TypeError(msg)

    if salt is not None and len(salt) > 16:
        msg = f"Salt value length MUST not be greater than 16 characters but is {len(salt)}"
        raise ValueError(msg)

    if salt is not None and not re.fullmatch(r"[\.\/0-9A-Za-z]{1,16}", salt):
        msg = "Salt value MUST only contain the characters ./0-9A-Za-z"
        raise ValueError(msg)


def _get_password_hash(user_password: str, salt: str | None = None) -> str:
    """
    Generate a SHA-512 password hash from a cleartext password for a local user.

    Parameters:
    ----------
        user_password: The cleartext password provided by the user that will be hashed.
        salt: Salt value to be used when creating password hash. A randomly generated salt will be used unless the user specifies one.

    Returns:
    -------
        The SHA-512 password hash

    Raises:
    ------
        TypeError: If the password is not of type `str`
        ValueError: If sha512_crypt fails for any reason
    """
    if not isinstance(user_password, str):
        msg = f"Password MUST be of type 'str' but is of type {type(user_password)}"
        raise TypeError(msg)

    _validate_salt(salt)

    try:
        # setting the rounds parameter to 5000 to omit rounds from the hash string, similar to EOS implementation
        return sha512_crypt.using(rounds=5000, salt=salt).hash(user_password)
    except Exception as exc:
        msg = "SHA-512 password hashing failed - check the input parameters of arista.avd.secure_hash"
        raise ValueError(msg) from exc


def secure_hash(user_password: str, salt: str | None = None) -> str:
    return _get_password_hash(user_password, salt)
