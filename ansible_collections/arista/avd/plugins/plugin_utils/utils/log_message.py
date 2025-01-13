# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from typing import Any

LOGGER = logging.getLogger(__name__)
LOGGING_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


def log_message(
    key: str,
    value: Any = None,
    key_path: str | None = None,
    message: str | None = None,
    log_level: str = "INFO",
    *,
    prepend_message: bool = False,
) -> None:
    """Log a message when a key from a data model is missing or has an invalid value.

    The function can take optional parameters to customize the log message.

    Args:
    ----
    key (str): The key to be logged.
    value (Any | None): Optional expected value of the key. When not provided, the message will indicate that the key is missing.
    key_path (str | None): Optional key path in dot notation.
    message (str | None): Optional custom message to be appended or prepended. By default, the message is appended unless `prepend_message=True`.
    log_level (str): The logging level to be used. Default is `INFO`.
    prepend_message (bool): Indicates whether the message should be prepended to the log message. Default is `False`.
    """
    # Validate logging level
    if log_level.upper() not in LOGGING_LEVELS:
        msg = "Invalid logging level. Please choose from DEBUG, INFO, WARNING, ERROR, CRITICAL."
        raise ValueError(msg)

    dot_notation = f"{key_path}.{key}" if key_path else f"{key}"
    msg_type = "is missing" if not value else f"!= '{value}'"
    log_msg = f"Key '{dot_notation}' {msg_type}."

    # Append or prepend the optional message
    if message:
        log_msg = f"{message}. {log_msg}" if prepend_message else f"{log_msg} {message}."

    # Logging the message
    log_level = logging.getLevelName(log_level.upper())
    LOGGER.log(log_level, log_msg)
