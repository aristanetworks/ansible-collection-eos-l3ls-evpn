# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from typing import TYPE_CHECKING, Any, Protocol

if TYPE_CHECKING:
    from collections.abc import Callable

    from . import CVClientProtocol


class UtilsMixin(Protocol):
    """Only to be used as mixin on CVClient class."""

    @staticmethod
    def _remove_item_from_list(itm: Any, lst: list, matcher: Callable) -> None:
        """
        Remove one item from the given list.

        Used for Tags and TagAssignments.

        Ignore if we are told to remove an item that is not present.
        This happens if you add a tag in a workspace and then remove it again.
        """
        for index, item in enumerate(lst):
            if matcher(item, itm):
                lst.pop(index)
                return

    @staticmethod
    def _upsert_item_in_list(itm: Any, lst: list, matcher: Callable) -> None:
        """
        Update or append one item from the given list.

        Used for Tags and TagAssignments.
        """
        for index, item in enumerate(lst):
            if matcher(item, itm):
                lst[index] = itm
                return

        lst.append(itm)

    def _set_value_from_path(self: CVClientProtocol, path: list[str], data: list | dict, value: Any) -> None:
        """
        Recursive function to walk through data to set value on path, creating any level needed.

        Parameters:
            path: Variable path to walk to set the value.
            data: Dict or list of which the path is walked and the value is set.
            Value: Value to set on the given path.

        Returns:
            No return value since all updates are done in-place in the given data.
        """
        if not path:
            if isinstance(value, dict) and isinstance(data, dict):
                data.update(value)
                return
            msg = f"Path '{path}', value type '{type(value)}' cannot be set on data type '{type(data)}'"
            raise RuntimeError(msg)
        # Convert '0' to 0.
        path = [int(element) if str(element).isnumeric() else element for element in path]
        if len(path) == 1:
            if isinstance(data, dict):
                data[path[0]] = value
            elif isinstance(data, list) and isinstance(path[0], int):
                # We ignore the actual integer value and just append the item to the list.
                data.append(value)
            else:
                msg = f"Path '{path}' cannot be set on data of type '{type(data)}'"
                raise RuntimeError(msg)
            return

        # Two or more elements in path.
        if isinstance(data, dict):
            # For dict, create the child key with correct type and call recursively.
            if isinstance(path[1], int):
                data.setdefault(path[0], [])
                self._set_value_from_path(path[1:], data[path[0]], value)
            else:
                data.setdefault(path[0], {})
                self._set_value_from_path(path[1:], data[path[0]], value)
        elif isinstance(data, list) and isinstance(path[0], int):
            index = path[0]
            # For list, pad the list with None values if it is smaller than the path index.
            if missing_indexes := max(0, (index + 1) - len(data)):
                data.extend([None] * missing_indexes)

            # Then assign the index with the correct type and call recursively.
            if isinstance(path[1], int):
                if not isinstance(data[index], list):
                    data[index] = []
                self._set_value_from_path(path[1:], data[index], value)
            else:
                if not isinstance(data[index], dict):
                    data[index] = {}
                self._set_value_from_path(path[1:], data[index], value)

        else:
            msg = f"Path '{path}', value type '{type(value)}' cannot be set on data of type '{type(data)}'"
            raise TypeError(msg)

    def _get_value_from_path(self: CVClientProtocol, path: list[str], data: list | dict, default_value: Any = None) -> Any:
        """
        Recursive function to walk through data to get a value from the given path.

        Parameters:
            path: Variable path to walk to get the value.
            data: Dict or list of which the path is walked and the value is found.
            default_value: Value to return if a value is not found at the given path.

        Returns:
            The value at the given path.

        Raises:
            TypeError: If the path does not match the data types of the given data (ex. 0 for a dict)
        """
        if not path:
            return data

        # Convert '0' to 0.
        path = [int(element) if str(element).isnumeric() else element for element in path]
        if isinstance(path[0], int) and not isinstance(data, list):
            msg = f"Path element is '{path[0]}' but data is not a list (got '{type(data)}')."
            raise TypeError(msg)

        try:
            return self._get_value_from_path(path[1:], data[path[0]])
        except (IndexError, KeyError):
            return default_value
