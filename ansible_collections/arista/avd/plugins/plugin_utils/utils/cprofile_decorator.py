# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

import cProfile
import pstats
from functools import wraps
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable


def cprofile(sort_by: str = "cumtime") -> Callable:
    """Profile an Ansible action plugin with cProfile.

    Profiling is conditionally enabled based on the presence of `cprofile_file` in the task arguments.

    Args:
    ----
        sort_by (str): The criterion to sort the profiling results. Default is 'cumtime'.

    Returns:
    -------
        Callable: The decorated function with conditional profiling.
    """

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Enable cProfile or not.

            If `cprofile_file` is present in the task arguments, cProfile will be enabled
            and will dump the stats to the provided cProfile file.

            Args:
            ----
                *args: Arbitrary positional arguments.
                **kwargs: Arbitrary keyword arguments.

            Returns:
            -------
                The result of the function call.
            """
            # The instance of the ActionModule class
            self = args[0]

            cprofile_file = self._task.args.get("cprofile_file")
            profiling_enabled = bool(cprofile_file)

            if profiling_enabled:
                profiler = cProfile.Profile()
                profiler.enable()

            try:
                result = func(*args, **kwargs)
            finally:
                if profiling_enabled:
                    profiler.disable()
                    stats = pstats.Stats(profiler).sort_stats(sort_by)
                    stats.dump_stats(cprofile_file)

            return result

        return wrapper

    return decorator
