# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .validation_result import ValidationResult


def validate_inputs(inputs: dict) -> ValidationResult:
    """
    Validate input variables according to the `eos_designs` schema as documented on avd.arista.com.

    Where supported by the schema, types will be auto type-converted like from "int" to "str".

    Args:
        inputs: Dictionary with inputs for "eos_designs".

    Returns:
        Validation result object with any validation errors or deprecation warnings.
    """
    # pylint: disable=import-outside-toplevel
    from .avd_schema_tools import EosDesignsAvdSchemaTools

    # pylint: enable=import-outside-toplevel

    eos_designs_schema_tools = EosDesignsAvdSchemaTools()

    # Inplace conversion of data
    validation_result = eos_designs_schema_tools.convert_data(inputs)

    # Validate input data
    validation_result.merge(eos_designs_schema_tools.validate_data(inputs))
    return validation_result
