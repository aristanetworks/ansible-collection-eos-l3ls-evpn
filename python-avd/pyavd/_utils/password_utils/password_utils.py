# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""
This code original credit goes to Kristian Kohntopp @isotopp who authorized to reuse it in AVD.

https://blog.koehntopp.info/2021/11/22/arista-type-7-passwords.html

It is used  in the encrypt and decrypt filters
"""

import base64

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, modes

# Starting cyryptography 43.0.0, TripleDES cipher has been moved to cryptography.hazmat.decrepit module
try:
    from cryptography.hazmat.decrepit.ciphers.algorithms import TripleDES
except ImportError:
    from cryptography.hazmat.primitives.ciphers.algorithms import TripleDES

SEED = b"\xd5\xa8\xc9\x1e\xf5\xd5\x8a\x23"

PARITY_BITS = [
    0x01,
    0x01,
    0x02,
    0x02,
    0x04,
    0x04,
    0x07,
    0x07,
    0x08,
    0x08,
    0x0B,
    0x0B,
    0x0D,
    0x0D,
    0x0E,
    0x0E,
    0x10,
    0x10,
    0x13,
    0x13,
    0x15,
    0x15,
    0x16,
    0x16,
    0x19,
    0x19,
    0x1A,
    0x1A,
    0x1C,
    0x1C,
    0x1F,
    0x1F,
    0x20,
    0x20,
    0x23,
    0x23,
    0x25,
    0x25,
    0x26,
    0x26,
    0x29,
    0x29,
    0x2A,
    0x2A,
    0x2C,
    0x2C,
    0x2F,
    0x2F,
    0x31,
    0x31,
    0x32,
    0x32,
    0x34,
    0x34,
    0x37,
    0x37,
    0x38,
    0x38,
    0x3B,
    0x3B,
    0x3D,
    0x3D,
    0x3E,
    0x3E,
    0x40,
    0x40,
    0x43,
    0x43,
    0x45,
    0x45,
    0x46,
    0x46,
    0x49,
    0x49,
    0x4A,
    0x4A,
    0x4C,
    0x4C,
    0x4F,
    0x4F,
    0x51,
    0x51,
    0x52,
    0x52,
    0x54,
    0x54,
    0x57,
    0x57,
    0x58,
    0x58,
    0x5B,
    0x5B,
    0x5D,
    0x5D,
    0x5E,
    0x5E,
    0x61,
    0x61,
    0x62,
    0x62,
    0x64,
    0x64,
    0x67,
    0x67,
    0x68,
    0x68,
    0x6B,
    0x6B,
    0x6D,
    0x6D,
    0x6E,
    0x6E,
    0x70,
    0x70,
    0x73,
    0x73,
    0x75,
    0x75,
    0x76,
    0x76,
    0x79,
    0x79,
    0x7A,
    0x7A,
    0x7C,
    0x7C,
    0x7F,
    0x7F,
]

ENC_SIG = b"\x4c\x88\xbb"


def des_setparity(key: bytes) -> bytes:
    res = b""
    for b in key:
        pos = b & 0x7F
        res += PARITY_BITS[pos].to_bytes(1, byteorder="big")
    return res


def hashkey(pw: bytes) -> bytes:
    result = bytearray(SEED)

    for idx, b in enumerate(pw):
        result[idx & 7] ^= b

    result = des_setparity(result)

    return bytes(result)


def cbc_encrypt(key: bytes, data: bytes) -> bytes:
    """
    Encrypt a password.

    Args:
        key (bytes): The encryption key, which should be the peer group name or neighbor IP with '_passwd' suffix.
        data (bytes): The data to be encrypted.

    Returns:
        bytes: The encrypted data, encoded in base64.
    """
    hashed_key = hashkey(key)
    padding = (8 - ((len(data) + 4) % 8)) % 8
    ciphertext = ENC_SIG + bytes([padding * 16 + 0xE]) + data + bytes(padding)

    # Accepting SonarLint issue: The insecure algorithm is ok since this simply matches the algorithm of EOS.
    cipher = Cipher(TripleDES(hashed_key), modes.CBC(bytes(8)), default_backend())  # NOSONAR
    encryptor = cipher.encryptor()
    result = encryptor.update(ciphertext)
    encryptor.finalize()

    return base64.b64encode(result)


def cbc_decrypt(key: bytes, data: bytes) -> bytes:
    """
    Decrypt a password.

    Args:
        key (bytes): The decryption key, which should be the peer group name or neighbor IP with '_passwd' suffix.
        data (bytes): The base64-encoded data to be decrypted.

    Returns:
        bytes: The decrypted data.

    Raises:
        ValueError: If the decrypted data is invalid or the length of the provided data is not a multiple of the block length.
    """
    data = base64.b64decode(data)
    hashed_key = hashkey(key)

    # Accepting SonarLint issue: Insecure algorithm is ok since this is simply matching the algorithm of EOS.
    cipher = Cipher(TripleDES(hashed_key), modes.CBC(bytes(8)), default_backend())  # NOSONAR
    decryptor = cipher.decryptor()
    result = decryptor.update(data)
    decryptor.finalize()

    # Checking the decrypted string
    pad = result[3] >> 4
    if result[:3] != ENC_SIG or pad >= 8 or len(result[4:]) < pad:
        msg = "Invalid Encrypted String"
        raise ValueError(msg)
    password_len = len(result) - pad
    return result[4:password_len]


def cbc_check_password(key: bytes, data: bytes) -> bool:
    """
    Verify if an encrypted password is decryptable.

    It does not return the password but only raises an error if the password cannot be decrypted.

    Args:
        key (bytes): The decryption key, which should be the peer group name or neighbor IP with '_passwd' suffix.
        data (bytes): The base64-encoded encrypted password data to be decrypted.

    Returns:
        bool: `True` if the password is decryptable, `False` otherwise.
    """
    # pylint: disable=W0718

    try:
        cbc_decrypt(key, data)
    except Exception:
        return False

    return True
