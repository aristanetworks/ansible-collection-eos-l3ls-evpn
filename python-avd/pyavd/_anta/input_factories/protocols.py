# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol, runtime_checkable

if TYPE_CHECKING:
    from anta.models import AntaTest

    from pyavd._anta.utils import ConfigManager, TestLoggerAdapter


@runtime_checkable
class AntaTestInputFactory(Protocol):
    """Protocol for all AntaTest.Input factories available in this package."""

    @classmethod
    def create(cls, test: type[AntaTest], manager: ConfigManager, logger: TestLoggerAdapter) -> AntaTest.Input | None: ...
