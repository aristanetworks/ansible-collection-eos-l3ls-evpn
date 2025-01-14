# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from .constants import EOS_CLI_CONFIG_GEN_SCHEMA_ID, EOS_DESIGNS_SCHEMA_ID

if TYPE_CHECKING:
    from collections.abc import Generator

    from typing_extensions import Self

    from .validation_result import ValidationResult


class AvdSchemaTools:
    """Tools that wrap the various schema components for easy use."""

    def __init__(self, schema: dict | None = None, schema_id: str | None = None) -> None:
        """
        Convert data according to the schema (convert_types).

        The data conversion is done in-place (updating the original "data" dict).

        Args:
            schema:
                Optional AVD schema as dict
            schema_id:
                Optional Name of AVD Schema to load from store
        """
        # pylint: disable=import-outside-toplevel
        from ._schema.avdschema import AvdSchema

        # pylint: enable=import-outside-toplevel

        self.avdschema = AvdSchema(schema=schema, schema_id=schema_id)

    def convert_data(self, data: dict) -> ValidationResult:
        """
        Convert data according to the schema (convert_types).

        The data conversion is done in-place (updating the original "data" dict).

        Args:
            data:
                Input variables which should be converted according to the schema.

        Returns:
            ValidationResult object with any validation errors or deprecation warnings.
        """
        # pylint: disable=import-outside-toplevel
        from ._errors import AvdDeprecationWarning
        from .validation_result import ValidationResult

        # pylint: enable=import-outside-toplevel

        result = ValidationResult(failed=False)

        # avdschema.convert returns a Generator, so we have to iterate through it to perform the actual conversions.
        exceptions: Generator = self.avdschema.convert(data)
        for exception in exceptions:
            # Store but continue for deprecations
            if isinstance(exception, AvdDeprecationWarning):
                if exception.removed or exception.conflict:
                    result.validation_errors.append(exception._as_validation_error())
                    result.failed = True
                    continue

                result.deprecation_warnings.append(exception)
                continue

            # Raise on other exceptions
            if isinstance(exception, Exception):
                raise exception

        return result

    def validate_data(self, data: dict) -> ValidationResult:
        """
        Validate data according to the schema.

        Args:
            data:
                Input variables which are to be validated according to the schema.

        Returns:
            Validation result object with any validation errors or deprecation warnings.
        """
        # pylint: disable=import-outside-toplevel
        from ._errors import AvdDeprecationWarning, AvdValidationError
        from .validation_result import ValidationResult

        # pylint: enable=import-outside-toplevel

        result = ValidationResult(failed=False)

        # avdschema.validate returns a Generator, so we have to iterate through it to perform the actual validations.
        exceptions: Generator = self.avdschema.validate(data)
        for exception in exceptions:
            # Store and fail but continue for validation errors
            if isinstance(exception, AvdValidationError):
                result.validation_errors.append(exception)
                result.failed = True
                continue

            # Store but continue for deprecations
            if isinstance(exception, AvdDeprecationWarning):
                result.deprecation_warnings.append(exception)
                continue

            # Raise on other exceptions
            if isinstance(exception, Exception):
                raise exception

        return result

    def convert_and_validate_data(self, data: dict) -> dict:
        """
        Convert and validate data according to the schema.

        Returns dictionary to be compatible with Ansible plugin. Called from vendored "get_structured_config".

        Args:
            data:
                Input variables which are to be validated according to the schema.

        Returns:
            dict :
                failed : bool
                    True if data is invalid. Otherwise False.
                errors : list[Exception]
                    Any data validation issues.
        """
        validation_result = self.convert_data(data)
        validation_result.merge(self.validate_data(data))
        return {"failed": validation_result.failed, "errors": validation_result.validation_errors}


class EosDesignsAvdSchemaTools(AvdSchemaTools):
    """Singleton AvdSchemaTools instance for eos_designs schema."""

    def __new__(cls) -> Self:
        if not hasattr(cls, "instance"):
            cls.instance = AvdSchemaTools(schema_id=EOS_DESIGNS_SCHEMA_ID)
        return cls.instance


class EosCliConfigGenAvdSchemaTools(AvdSchemaTools):
    """Singleton AvdSchemaTools instance for eos_cli_config_gen schema."""

    def __new__(cls) -> Self:
        if not hasattr(cls, "instance"):
            cls.instance = AvdSchemaTools(schema_id=EOS_CLI_CONFIG_GEN_SCHEMA_ID)
        return cls.instance
