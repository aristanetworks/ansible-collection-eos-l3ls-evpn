# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
import string
from enum import Enum


class TestLoggerAdapter(logging.LoggerAdapter):
    """Custom LoggerAdapter used to add device, test, and an optional context information to log messages.

    It uses the same constructor as the standard LoggerAdapter and `extra` should have the following structure:

    ```python
    extra = {
        "device": "<device_name>",
        "test": "<test_name>",
        "context": "<test_context>",
    }
    ```
    The `create` method can be used as an alternative constructor to create a new TestLoggerAdapter instance using the proper `extra` dict shown above.

    When logging a message, the logger will format the `LogMessage` Enum message using the kwargs passed to the logger,
    and prepend the message with the device and test names, and optionally the context.
    """

    def process(self, msg: LogMessage, kwargs: dict) -> tuple[str, dict]:
        """Process the message and kwargs before logging."""
        # Keep the extra dict in kwargs to pass it to the formatter if needed (following the standard LoggerAdapter behavior)
        kwargs["extra"] = self.extra

        # Extract the device, test, and context from extra
        device = self.extra["device"]
        test = self.extra["test"]
        context = self.extra.get("context", "")

        # Format: <device> [test] (context): message
        prefix = f"<{device}> [{test}]"
        if context:
            prefix += f" ({context})"

        # Format the LogMessage using the provided kwargs and extract the fields name from the message string
        fields = [field_name for _, field_name, _, _ in string.Formatter().parse(msg.value) if field_name is not None]
        msg = msg.value.format(**kwargs)

        # Removing the fields name from kwargs to preserve standard logging kwargs only that should always be passed through (e.g. exc_info, stack_info, etc.)
        for field in fields:
            kwargs.pop(field, None)

        return f"{prefix}: {msg}", kwargs

    def add_context(self, context: str) -> TestLoggerAdapter:
        """Add a new context to the existing logger and return a new TestLoggerAdapter instance.

        Used when you want to add a new context to an existing logger without modifying the original one.
        """
        extra = dict(self.extra)
        extra["context"] = context
        return TestLoggerAdapter(self.logger, extra)

    @staticmethod
    def create(device: str, test: str, logger: logging.Logger, context: str | None = None) -> TestLoggerAdapter:
        """Construct a new TestLoggerAdapter instance."""
        extra = {"device": device, "test": test, "context": context or ""}
        return TestLoggerAdapter(logger, extra)


class LogMessage(Enum):
    """Enum class to store log messages."""

    NO_INPUTS = "No inputs found. Skipping."
    NO_DATA_MODEL = "Data model(s) {entity} not found. Skipping."
    NO_SOURCES = "No {entity} sources found. Skipping."
    UNAVAILABLE_PEER = "{entity} skipped. Peer {peer} unavailable."
    UNAVAILABLE_PEER_IP = "{entity} skipped. Peer {peer} IP for {peer_interface} missing."
    UNAVAILABLE_IP = "{entity} skipped. IP address missing."
    INVALID_DATA = "{entity} skipped. Invalid data; {issues}"
    SUBINTERFACE = "Subinterface {entity} skipped."
    SKIP_INTERFACE = "{entity} skipped. `validate_state` set to False."
    NOT_VTEP = "Skipped. Not a VTEP."
    WAN_VTEP = "Skipped. WAN VTEP."
