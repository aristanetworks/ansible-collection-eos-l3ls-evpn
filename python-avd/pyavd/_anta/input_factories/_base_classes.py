# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from anta.models import AntaTest

    from pyavd._anta.utils import ConfigManager, TestLoggerAdapter


class AntaTestInputFactory(ABC):
    """Base class for AntaTest.Input factories."""

    def __init__(self, test: type[AntaTest], manager: ConfigManager, logger: TestLoggerAdapter) -> None:
        self.test = test
        self.manager = manager
        self.logger = logger

    @abstractmethod
    def create(self) -> AntaTest.Input | None:
        """Create the AntaTest.Input model for the AntaTest."""
