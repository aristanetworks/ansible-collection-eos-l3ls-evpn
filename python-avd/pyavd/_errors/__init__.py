# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.


class AristaAvdError(Exception):
    def __init__(self, message: str = "An Error has occurred in an arista.avd plugin") -> None:
        self.message = message
        super().__init__(self.message)

    def _json_path_to_string(self, json_path: list[str | int]) -> str:
        path = ""
        for index, elem in enumerate(json_path):
            if isinstance(elem, int):
                path += f"[{elem}]"
            else:
                if index == 0:
                    path += elem
                    continue
                path += f".{elem}"
        return path


class AristaAvdInvalidInputsError(AristaAvdError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class AristaAvdMissingVariableError(AristaAvdError):
    def __init__(self, variable: str | None = None) -> None:
        self.message = f"'{variable}' is required but was not found."
        super().__init__(self.message)


class AvdSchemaError(AristaAvdError):
    def __init__(self, message: str = "Schema Error", path: list[str | int] | None = None) -> None:
        if path is not None:
            self.path = self._json_path_to_string(path)
            message = f"'Validation Error: {self.path}': {message}"
        super().__init__(message)


class AvdValidationError(AristaAvdError):
    def __init__(self, message: str = "Schema Error", path: list[str | int] | None = None) -> None:
        if path is not None:
            self.path = self._json_path_to_string(path)
            message = f"'Validation Error: {self.path}': {message}"
        super().__init__(message)


class AvdDeprecationWarning(AristaAvdError):  # noqa: N818
    def __init__(
        self,
        key: list[str | int],
        new_key: str | None = None,
        remove_in_version: str | None = None,
        remove_after_date: str | None = None,
        url: str | None = None,
        *,
        removed: bool = False,
        conflict: bool = False,
    ) -> None:
        messages = []
        self.path = self._json_path_to_string(key)
        self.version = remove_in_version
        self.date = remove_after_date
        self.removed = removed
        self.conflict = conflict

        if removed:
            messages.append(f"The input data model '{self.path}' was removed.")
        elif conflict and new_key:
            self.new_key_path = self._json_path_to_string(key[:-1]) + "." + new_key
            messages.append(
                f"The input data model '{self.path}' is deprecated and cannot be used in conjunction with the new data model '{self.new_key_path}'. "
                "This usually happens when a data model has been updated and custom structured configuration still uses the old model."
            )
            if not url:
                url = "the porting guide on https://avd.arista.com"
        else:
            messages.append(f"The input data model '{self.path}' is deprecated.")

        if new_key and not conflict:
            messages.append(f"Use '{new_key}' instead.")

        if url:
            messages.append(f"See {url} for details.")

        self.message = " ".join(messages)
        super().__init__(self.message)

    def _as_validation_error(self) -> AvdValidationError:
        """Converting AvdDeprecationWarning to AvdValidationError."""
        return AvdValidationError(message=self.message, path=self.path.split("."))


class AristaAvdDuplicateDataError(AristaAvdError):
    def __init__(self, context: str, context_item_a: str, context_item_b: str) -> None:
        self.message = (
            f"Found duplicate objects with conflicting data while generating configuration for {context}. {context_item_a} conflicts with {context_item_b}."
        )
        super().__init__(self.message)
