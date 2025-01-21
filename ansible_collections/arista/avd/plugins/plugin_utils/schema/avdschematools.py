# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING

from ansible.errors import AnsibleActionFail

from ansible_collections.arista.avd.plugins.plugin_utils.pyavd_wrappers import RaiseOnUse

if TYPE_CHECKING:
    from collections.abc import Generator

    from ansible.utils.display import Display

try:
    from pyavd._errors import AristaAvdError, AvdDeprecationWarning
    from pyavd._schema.avdschema import AvdSchema
except ImportError as e:
    AvdSchema = RaiseOnUse(AnsibleActionFail("The 'arista.avd' collection requires the 'pyavd' Python library. Got import error", orig_exc=e))
    AristaAvdError = AvdDeprecationWarning = ImportError


VALID_VALIDATION_MODES = ["error", "warning"]
DEFAULT_VALIDATION_MODE = "error"


class AvdSchemaTools:
    """Tools that wrap the various schema components for easy reuse in Ansible plugins."""

    def __init__(
        self,
        hostname: str,
        ansible_display: Display,
        schema: dict | None = None,
        schema_id: str | None = None,
        validation_mode: str | None = None,
        plugin_name: str | None = None,
    ) -> None:
        self._set_schema(schema, schema_id)
        self.hostname = hostname
        self.ansible_display = ansible_display
        self.plugin_name = plugin_name
        self._set_validation_mode(validation_mode)

    def _set_schema(self, schema: dict | None, schema_id: str | None) -> None:
        if schema is None and schema_id is None:
            msg = "Either argument 'schema' or 'schema_id' must be set"
            raise AnsibleActionFail(msg)

        try:
            self.avdschema = AvdSchema(schema=schema, schema_id=schema_id)
        except AristaAvdError as e:
            msg = "Invalid Schema!"
            raise AnsibleActionFail(msg) from e

    def _set_validation_mode(self, validation_mode: str | None) -> None:
        if validation_mode is None:
            validation_mode = DEFAULT_VALIDATION_MODE

        if not isinstance(validation_mode, str):
            msg = "The argument 'validation_mode' must be a string"
            raise AnsibleActionFail(msg)

        if validation_mode not in VALID_VALIDATION_MODES:
            msg = f"Invalid value '{validation_mode}' for the argument 'validation_mode'. Must be one of {VALID_VALIDATION_MODES}"
            raise AnsibleActionFail(msg)

        self.validation_mode = validation_mode

    def convert_data(self, data: dict) -> int:
        """
        Convert data according to the schema (convert_types).

        The data conversion is done in-place (updating the original "data" dict).

        The conversion code will also emit deprecation warnings and fatal errors for removed vars or conflicts.

        Returns:
        -------
        int : number of validation errors
        """
        # avd_schema.convert returns a generator, which we iterate through in handle_exceptions to perform the actual conversions.
        exceptions = self.avdschema.convert(data)
        return self.handle_validation_exceptions(exceptions, "error")

    def validate_data(self, data: dict) -> int:
        """
        Validate data according to the schema.

        Returns:
        -------
        int : number of validation errors
        """
        # avd_schema.validate returns a generator, which we iterate through in handle_exceptions to perform the actual validations.
        exceptions = self.avdschema.validate(data)
        return self.handle_validation_exceptions(exceptions, self.validation_mode)

    def convert_and_validate_data(self, data: dict, return_counters: bool = False) -> dict:
        """
        Convert & Validate data according to the schema.

        Calls conversion and validation methods and gather resulting messages

        Returns dict which can contain either or both of the following keys:
        - failed: <bool>
        - msg: <str with concatenated summary messages from validation>
        - validation_errors: <int with number of validation errors - returned if return_counters is set>
        The return value should be applied on Ansible Action "result" dictionary
        """
        result = {}

        # Perform data conversions
        validation_errors = self.convert_data(data)
        # All errors raised from conversion are fatal.
        if validation_errors:
            result["failed"] = True

        # Perform validation
        validation_errors += self.validate_data(data)
        if validation_errors and self.validation_mode == "error":
            result["failed"] = True

        result["msg"] = self.build_result_message(validation_errors=validation_errors)

        if return_counters:
            result["validation_errors"] = validation_errors

        return result

    def handle_validation_exceptions(self, exceptions: Generator, mode: str | None) -> int:
        """
        Iterate through the Generator of exceptions.

        This method is actually where the content of the generator gets executed.

        It displays various messages depending on the `mode` parameter

        Returns:
        - counter: <int> the number of AristaAvdError in the exceptions Generator (not including deprecation warnings)
        """
        counter = 0
        for exception in exceptions:
            if not isinstance(exception, AristaAvdError):
                continue

            message = f"[{self.hostname}]: {exception}"
            if isinstance(exception, AvdDeprecationWarning):
                # Deprecation warnings are displayed using Ansible's deprecation notices.
                if exception.removed:
                    # Thank you! ansible-core>=2.16 broke support for removed=True and
                    # they do not test it, so apparently we were the only ones using it.
                    message = self.ansible_display.get_deprecation_message(
                        msg=message,
                        version=exception.version,
                        date=exception.date,
                        collection_name=self.plugin_name,
                        removed=exception.removed,
                    )
                # Conflicts are handled as errors below.
                elif not exception.conflict:
                    self.ansible_display.deprecated(
                        msg=message,
                        version=exception.version,
                        date=exception.date,
                        collection_name=self.plugin_name,
                        removed=exception.removed,
                    )
                    continue

            counter += 1
            if mode == "warning":
                self.ansible_display.warning(message)
            else:
                # when mode == "error"
                self.ansible_display.error(message, wrap_text=False)
        return counter

    def validate_schema(self) -> int:
        """
        Validate the loaded schema according to the meta-schema.

        Returns int with number of validation errors
        """
        # avd_schema.validate_schema returns a generator, which we iterate through in handle_exceptions to perform the actual validations.
        exceptions = self.avdschema.validate_schema(self.avdschema._schema)
        return self.handle_validation_exceptions(exceptions, "error")

    def build_result_message(self, validation_errors: int = 0, schema_validation_errors: int = 0) -> str | None:
        result_messages = []

        if validation_errors:
            result_messages.append(f"{validation_errors} errors found during schema validation of input vars.")

        if schema_validation_errors:
            result_messages.append(f"{schema_validation_errors} errors found during meta-schema validation of the generated schema.")

        if result_messages:
            return " ".join(result_messages)

        return None
