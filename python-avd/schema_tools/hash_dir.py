# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from hashlib import sha1
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator

IGNORED_DIRS = ["__pycache__", "compiled_templates"]


def _filehash(path: Path) -> str:
    """Compute SHA1 fhash of the content of the file at path."""
    sha = sha1(usedforsecurity=False)
    block = bytearray(128 * 1024)
    mv = memoryview(block)
    # TODO: when only python>=3.11 is supported, can use hashlib.file_digest() instead
    with path.open("rb", buffering=0) as fd:
        while n := fd.readinto(mv):
            sha.update(mv[:n])
    return sha.hexdigest()


def changed_hash(path: Path) -> tuple[bool, str]:
    """
    Check if the hash of the given path is different from the .hash file stored.

    If no .hash file is found, recompute

    Returns (True, new_hash) if the hash has changed.
    Returns (False, current_hash) if the hash has not changed.
    """
    saved_hash_path = path / ".hash"
    if saved_hash_path.exists():
        with saved_hash_path.open() as fd:
            saved_hash = fd.read()
    else:
        saved_hash = ""
    current_hash = hash_dir(path)
    return (True, current_hash) if saved_hash != current_hash else (False, current_hash)


def hash_dir(path: Path) -> str:
    """Recursively hash all the files in a directory using SHA1 and returns the sha1 hash of all their hashes."""
    sha = sha1(usedforsecurity=False)

    def walk(path: Path) -> Generator[Path, None, None]:
        """Walk a directory at Path and yield all the files (not the dir)."""
        for p in Path(path).iterdir():
            if p.is_dir():
                if p.name in IGNORED_DIRS:
                    # Skipping ignored directories
                    continue
                yield from walk(p)
                continue
            yield p.resolve()

    for p in walk(path):
        # Ignore .hash files
        if p.name == ".hash":
            continue
        p_sha = _filehash(p)
        p_sha_b = bytes(p_sha, encoding="UTF-8")
        sha.update(p_sha_b)
    return sha.hexdigest()
