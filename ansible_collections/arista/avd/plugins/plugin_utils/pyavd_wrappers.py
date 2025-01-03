# Copyright (c) 2019-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import warnings
from functools import partial, wraps
from typing import TYPE_CHECKING, Any, Literal

from ansible.errors import AnsibleFilterError, AnsibleInternalError, AnsibleUndefinedVariable
from ansible.module_utils.basic import to_native
from ansible.utils.display import Display
from jinja2.exceptions import UndefinedError

if TYPE_CHECKING:
    from collections.abc import Callable
    from typing import NoReturn

display = Display()


class RaiseOnUse:
    """
    Class that will delay raises of errors until the instance is called.

    Used with Ansible try/except import logic to not fail on import of plugins, but instead fail on first use.
    """

    def __init__(self, exception: Exception) -> None:
        self.exception = exception

    def __call__(self, *_args: Any, **_kwargs: Any) -> NoReturn:
        raise self.exception

    def __getattr__(self, name: str) -> Any:
        if not name.startswith("__"):
            raise self.exception
        return self.__getattribute__(name)


def wrap_plugin(plugin_type: Literal["filter", "test"], name: str) -> Callable:
    plugin_map = {
        "filter": AnsibleFilterError,
        "test": AnsibleFilterError,
    }

    if plugin_type not in plugin_map:
        msg = f"Wrong plugin type {plugin_type} passed to wrap_plugin."
        raise AnsibleInternalError(msg)

    def wrap_plugin_decorator(func: Callable) -> Callable:
        @wraps(func)
        def plugin_wrapper(*args: Any, **kwargs: Any) -> Any:
            """Wrapper function for plugins.

            NOTE: if the same warning is raised multiple times, Ansible Display() will print only one
            """
            try:
                with warnings.catch_warnings(record=True) as w:
                    result = func(*args, **kwargs)
                    if w:
                        for warning in w:
                            display.warning(str(warning.message))
            except UndefinedError as e:
                msg = f"{plugin_type.capitalize()} '{name}' failed: {to_native(e)}"
                raise AnsibleUndefinedVariable(msg, orig_exc=e) from e
            except Exception as e:
                msg = f"{plugin_type.capitalize()} '{name}' failed: {to_native(e)}"
                raise plugin_map[plugin_type](msg, orig_exc=e) from e

            return result

        return plugin_wrapper

    return wrap_plugin_decorator


wrap_filter = partial(wrap_plugin, "filter")
wrap_test = partial(wrap_plugin, "test")
