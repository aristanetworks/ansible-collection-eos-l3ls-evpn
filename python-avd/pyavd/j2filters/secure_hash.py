# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.

from pyavd._errors import AristaAvdError

try:
    from passlib.hash import sha512_crypt
except ImportError as imp_exc:
    raise AristaAvdError(imp_exc) from imp_exc


def _get_password_hash(user_password: str) -> str:
    """

    Generate a SHA512-Crypt password hash with a random salt value.

    Parameters:
    ----------
    user_password : str
                    the password provided by the user that will be hashed

    Returns:
    -------
    str
        the SHA512-Crypt password hash with modular crypt prefix $6$

    Raises:
    ------
    TypeError
        If the password is not of type `str`
    ValueError
        If sha512_crypt fails for any reason
    """
    if isinstance(user_password, str):
        try:
            # setting the rounds parameter to 5000 to omit rounds from the hash string, similar to EOS implementation
            return sha512_crypt.using(rounds=5000).hash(user_password)
        except Exception as exc:
            msg = "SHA512 password hashing failed - check the input parameters of arista.avd.hash"
            raise ValueError(msg) from exc

    else:
        msg = f"Password MUST be of type 'str' but is of type {type(user_password)}"
        raise TypeError(msg)


def secure_hash(user_password: str) -> str:
    return _get_password_hash(user_password)
