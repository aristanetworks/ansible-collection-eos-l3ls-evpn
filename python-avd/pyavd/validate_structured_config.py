# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .validation_result import ValidationResult


def validate_structured_config(structured_config: dict) -> ValidationResult:
    """
    Validate structured config according the `eos_cli_config_gen` schema as documented on avd.arista.com.

    Where supported by the schema, types will be auto type-converted like from "int" to "str".

    Args:
        structured_config: Dictionary with structured configuration.

    Returns:
        Validation result object with any validation errors or deprecation warnings.
    """
    # pylint: disable=import-outside-toplevel
    from .avd_schema_tools import EosCliConfigGenAvdSchemaTools

    # pylint: enable=import-outside-toplevel

    eos_cli_config_gen_schema_tools = EosCliConfigGenAvdSchemaTools()
    # Inplace conversion of data
    validation_result = eos_cli_config_gen_schema_tools.convert_data(structured_config)

    # Validate input data
    validation_result.merge(eos_cli_config_gen_schema_tools.validate_data(structured_config))
    return validation_result
