# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import logging
from logging import Filter, Handler
from typing import TYPE_CHECKING

from ansible.utils.display import Display

if TYPE_CHECKING:
    from logging import LogRecord


class PythonToAnsibleHandler(Handler):
    """
    Logging Handler that makes a bridge between Ansible display and plugin Result objects.

    It is used to:
    * send ERROR or CRITICAL logs to result[stderr] and failed the plugins
    * send WARNING logs to result["warning"] for the plugins that will be display in the logs
    * send INFO logs to display.v which can be visualized using `-v` in the ansible-playbook argument
      provided the logger level is set to INFO or above
    * send DEBUG logs to display.vvv which can be visualized when running a playbook with `-vvv`
    """

    def __init__(self, result: dict | None, display: Display | None = None) -> None:
        super().__init__()
        # If no display object was given, retrieve the Singleton
        self.display = display or Display()
        self.result = result

    def emit(self, record: LogRecord) -> None:
        """Custom emit function that reads the message level."""
        message = self._format_msg(record)
        if record.levelno in [logging.CRITICAL, logging.ERROR]:
            if self.result is not None:
                self.result.setdefault("stderr_lines", []).append(message)
                self.result["stderr"] = self.result.setdefault("stderr", "") + f"{message!s}\n"
                self.result["failed"] = True
            else:
                self.display.error(str(message))
        elif record.levelno in [logging.WARNING, logging.WARNING]:
            if self.result is not None:
                self.result.setdefault("warnings", []).append(message)
            else:
                self.display.warning(str(message))
        elif record.levelno == logging.INFO:
            self.display.v(str(message))
        elif record.levelno == logging.DEBUG:
            self.display.vvv(str(message))

    def _format_msg(self, record: LogRecord) -> str:
        """Used to format an augmented LogRecord that contains the 'hostname' attribute."""
        return f"<{record.hostname}> {self.format(record)}" if hasattr(record, "hostname") else self.format(record)


class PythonToAnsibleContextFilter(Filter):
    """
    Logging Filter to extend the LogRecord that goes through it with an extra attribute 'hostname'. For this, it needs to be initialized with a hostname.

    This extra attribute can then be used in the PythonToAnsibleHandler to format the messages
    """

    def __init__(self, hostname: str) -> None:
        super().__init__()
        self.hostname = hostname

    def filter(self, record: LogRecord) -> bool:
        """Add self.hostname as an attribute to the LogRecord."""
        record.hostname = self.hostname
        return True
