# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from abc import ABC, abstractmethod
from json import dumps
from typing import TYPE_CHECKING

from pydantic import BaseModel, ValidationError

if TYPE_CHECKING:
    from anta.models import AntaTest

    from pyavd._anta.utils import ConfigManager, TestLoggerAdapter


class AntaTestInputFactory(ABC):
    """Base class for AntaTest.Input factories."""

    def __init__(
        self,
        test: type[AntaTest],
        manager: ConfigManager,
        logger: TestLoggerAdapter,
        input_filter: AntaTestInputFactoryFilter | None = None,
    ) -> None:
        self.test = test
        self.manager = manager
        self.logger = logger
        self.input_filter = input_filter or AntaTestInputFactoryFilter()

    @abstractmethod
    def create(self) -> AntaTest.Input | None:
        """Create the AntaTest.Input model for the AntaTest."""

    def is_peer_filtered(self, peer: str) -> bool:
        """Check if a peer is filtered by `input_filter`."""
        return peer in getattr(self.input_filter, "exclude_peers", [])


class AntaTestInputFactoryFilter(BaseModel, extra="forbid"):
    """Base class for AntaTestInputFactory filters."""

    def get_filter_example(self) -> str:
        """Return a formatted dictionary example of how to use the filter."""
        schema = self.model_json_schema()

        # Build example dictionary
        return {field_name: field_info.get("examples", [None]) for field_name, field_info in schema.get("properties", {}).items()}

    def format_validation_error(self, error: ValidationError, test_name: str) -> str:
        """Format a validation error with an example of valid filter structure."""
        example = self.get_filter_example()
        formatted_example = dumps(example, indent=2)

        return f"Invalid filter for test {test_name}: {error}\nExample filter:\n{formatted_example}"
