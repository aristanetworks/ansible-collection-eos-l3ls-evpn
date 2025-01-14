# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
"""Logging utilities used by PyAVD for ANTA."""

from __future__ import annotations

import string
from contextlib import contextmanager
from enum import Enum
from logging import LoggerAdapter
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Generator
    from logging import Logger


class TestLoggerAdapter(LoggerAdapter):
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

    @contextmanager
    def context(self, context: str) -> Generator[TestLoggerAdapter, None, None]:
        """Temporarily add context to the logger."""
        original_extra = dict(self.extra)
        try:
            self.extra["context"] = context
            yield self
        finally:
            self.extra = original_extra

    @staticmethod
    def create(device: str, test: str, logger: Logger, context: str | None = None) -> TestLoggerAdapter:
        """Construct a new TestLoggerAdapter instance."""
        extra = {"device": device, "test": test, "context": context or ""}
        return TestLoggerAdapter(logger, extra)


class LogMessage(Enum):
    """Log message templates for test input generation.

    Adapter adds: `<device> [test] (context):`
    """

    # Peer-related messages
    PEER_UNAVAILABLE = "{caller} skipped - peer {peer} not in fabric or not deployed"
    PEER_OUTSIDE_BOUNDARY = "{caller} skipped - peer {peer} not in {boundary} boundary"
    PEER_INTERFACE_NO_IP = "{caller} skipped - peer {peer} interface {peer_interface} has no IP"

    # Interface state messages
    INTERFACE_SHUTDOWN = "{caller} skipped - interface is shutdown"
    INTERFACE_USING_DHCP = "{caller} skipped - DHCP interface"
    INTERFACE_IS_SUBINTERFACE = "{caller} skipped - subinterface"
    INTERFACE_NOT_INBAND_MGMT = "{caller} skipped - not an inband management SVI"
    INTERFACE_VALIDATION_DISABLED = "{caller} skipped - validate_state or validate_lldp disabled"
    INTERFACE_NO_IP = "{caller} skipped - no IP address configured"

    # IP-related messages
    IPV6_UNSUPPORTED = "{caller} skipped - IPv6 not supported"
    LOOPBACK0_NO_IP = "skipped - no Loopback0 IP"
    VTEP_NO_IP = "skipped - no VTEP IP"

    # Device role messages
    DEVICE_NOT_VTEP = "skipped - device is not a VTEP or is a WAN router"
    DEVICE_NOT_WAN_ROUTER = "skipped - device is not a WAN router"
    DEVICE_NO_INBAND_MGMT = "skipped - no inband management SVI found"

    # BGP-specific messages
    BGP_AF_NOT_ACTIVATED = "{caller} - address families {capability} skipped"

    # STUN-specific messages
    STUN_NO_CLIENT_INTERFACE = "path group {caller} skipped - no STUN client interfaces found"
    STUN_NO_STATIC_PEERS = "path group {caller} skipped - no static peers configured"

    # Input generation messages
    INPUT_NONE_FOUND = "skipped - no inputs available"
    INPUT_NO_DATA_MODEL = "skipped - data model {caller} not found"
    INPUT_MISSING_FIELDS = "{caller} skipped - missing required fields: {fields}"
    INPUT_RENDERING = "rendering inputs with {caller}"
    INPUT_RENDERED = "rendered input dict: {inputs}"
