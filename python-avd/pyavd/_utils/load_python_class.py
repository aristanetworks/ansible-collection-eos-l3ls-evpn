# Copyright (c) 2023-2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import importlib
import inspect
import pkgutil
from typing import TYPE_CHECKING

from pyavd._errors import AristaAvdError, AristaAvdMissingVariableError

if TYPE_CHECKING:
    from collections.abc import Callable
    from types import ModuleType


def load_python_class(module_path: str, class_name: str, parent_class: type | None = None) -> type:
    """
    Load Python Class via importlib.

    Parameters
    ----------
    module_path : str
        Path to import the module from
    class_name : str
        Name of the class to load
    parent_class : type
        Class from which the imported class must inherit if present

    Returns:
    -------
    type
        The loaded Class (and not an instance of the Class)

    Raises:
    ------
    AristaAvdMissingVariableError
        If module_path or class_name are not present

    AristaAvdError
        If importlib fails to load the Class
        If the loaded Class is not inheriting from the optional parent_class
    """
    if not module_path:
        msg = "Cannot load a python class without the module_path set."
        raise AristaAvdMissingVariableError(msg)
    if not class_name:
        msg = "Cannot load a python class without the class_name set."
        raise AristaAvdMissingVariableError(msg)

    try:
        cls = getattr(importlib.import_module(module_path), class_name)
    except ImportError as imp_exc:
        raise AristaAvdError(imp_exc) from imp_exc

    if parent_class is not None and not issubclass(cls, parent_class):
        msg = f"{cls} is not a subclass of {parent_class} class"
        raise AristaAvdError(msg)

    return cls


def load_classes(package_name: str, class_filter: Callable[[str, type], bool] | None = None) -> dict[str, type]:
    """Recursively load all classes from a package and its sub-packages. Optionally filter the classes using a filter function.

    Parameters
    ----------
    package_name : str
        Name of the package to load classes from.
    class_filter : Callable
        Optional filter function to filter the classes to load. The function should take the class name and class object as arguments and return a boolean.

    Returns:
    -------
    dict
        Dictionary containing the class name as key and the class object as value.
    """
    classes = {}
    package = importlib.import_module(package_name)

    def load_from_module(module: ModuleType) -> None:
        for name, obj in inspect.getmembers(module, inspect.isclass):
            if obj.__module__.startswith(package_name) and (class_filter is None or class_filter(name, obj)):
                classes[name] = obj  # noqa: PERF403

    for _, module_name, is_pkg in pkgutil.walk_packages(package.__path__, package_name + "."):
        module = importlib.import_module(module_name)
        if not is_pkg:
            load_from_module(module)

    return classes
