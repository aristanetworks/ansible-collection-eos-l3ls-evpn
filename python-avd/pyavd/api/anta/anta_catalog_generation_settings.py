# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field, field_validator

from .test_spec import TestSpec


# TODO: Consider naming this InputFactoryGenerationSettings
class TestGenerationSettings(BaseModel):
    """Model defining settings for test input generation."""

    allow_bgp_vrfs: bool = False


class AntaCatalogGenerationSettings(BaseModel):
    """Model defining settings for ANTA catalog generation."""

    model_config = ConfigDict(extra="forbid", arbitrary_types_allowed=True)

    test_generation_settings: TestGenerationSettings = Field(default_factory=TestGenerationSettings)
    run_tests: list[str] = Field(default_factory=list)
    skip_tests: list[str] = Field(default_factory=list)
    custom_test_specs: list[TestSpec] = Field(default_factory=list)
    output_dir: str | Path | None = None
    ignore_is_deployed: bool = False

    @field_validator("output_dir")
    @classmethod
    def validate_output_dir(cls, value: str | Path | None) -> Path | None:
        if value is None:
            return None
        path = Path(value)
        if not (path.exists() and path.is_dir()):
            msg = f"Provided output_dir {value} does not exist or is not a directory"
            raise ValueError(msg)
        return path
