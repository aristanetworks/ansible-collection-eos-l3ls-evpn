# Copyright (c) 2024 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from functools import wraps
from inspect import signature
from logging import getLogger
from typing import TYPE_CHECKING, Any, ClassVar, get_origin

from pyavd._utils import batch

from .constants import CVAAS_VERSION_STRING
from .exceptions import CVMessageSizeExceeded
from .versioning import CvVersion

if TYPE_CHECKING:
    from collections.abc import Callable

LOGGER = getLogger(__name__)


def grpc_msg_size_handler(list_field: str) -> Callable:
    def decorator_grpc_msg_size_handler(func: Callable) -> Callable:
        func_signature = signature(func)
        # Sometimes the return_annotation is a proper type, and sometimes - when using forward references - it is a string. Here we normalize to type.
        return_annotation = (
            list if type(func_signature.return_annotation) is str and func_signature.return_annotation.startswith("list") else func_signature.return_annotation
        )
        if return_annotation is not list and get_origin(return_annotation) is not list:
            msg = (
                f"grpc_msg_size_handler decorator is unable to bind to the function '{func.__name__}'. "
                f"Expected a return type of 'list'. Got '{return_annotation}'."
            )
            raise TypeError(msg)

        @wraps(func)
        async def wrapper_grpc_msg_size_handler(*args: Any, **kwargs: Any) -> list:
            bound_arguments = func_signature.bind(*args, **kwargs)
            arguments = bound_arguments.arguments
            if list_field not in arguments:
                msg = f"grpc_msg_size_handler decorator is unable to find the list_field '{list_field}' in the given arguments to '{func.__name__}'."
                raise KeyError(msg)

            list_value: list = arguments[list_field]
            if not isinstance(list_value, list):
                msg = f"grpc_msg_size_handler decorator expected the value of the list_field '{list_field}' to be a list. Got '{type(list_value)}'"
                raise TypeError(msg)

            LOGGER.info("wrapper_grpc_msg_size_handler: Called '%s' with '%s' items", func.__name__, len(list_value))

            if len(list_value) < 2:
                # No need to try/except if we cannot split the list.
                return await func(*args, **kwargs)

            try:
                return await func(*args, **kwargs)
            except CVMessageSizeExceeded as e:
                # At minimum try to split in two.
                # The double negatives make // round up instead of down.
                ratio = max(2, -(-e.size // e.max_size))
                chunk_size = len(list_value) // ratio
                LOGGER.info(
                    "wrapper_grpc_msg_size_handler: Message size %s exceeded the max of %s. Splitting into %s smaller calls with up to %s items each.",
                    e.size,
                    e.max_size,
                    ratio,
                    chunk_size,
                )
                # For every chunk we call ourselves recursively, so we can catch any further needs of splitting.
                result = []
                for chunk in batch(list_value, chunk_size):
                    arguments[list_field] = chunk
                    result.extend(await wrapper_grpc_msg_size_handler(*bound_arguments.args, **bound_arguments.kwargs))
                return result

        return wrapper_grpc_msg_size_handler

    return decorator_grpc_msg_size_handler


class LimitCvVersion:
    """
    Decorator used to limit the supported CloudVision versions for a certain method.

    The decorator will maintain a map of decorated function variants and their supported versions.

    The decorator will only work in CvClient class methods since it expects the _cv_client attribute on 'self'.
    """

    versioned_funcs: ClassVar[dict[str, dict[tuple[CvVersion, CvVersion], Callable]]] = {}
    """
    Map of versioned functions keyed by function name.

    {
        <function_name>: {
            (<min_cv_version>, <max_cv_version>): <method>,
            (<min_cv_version>, <max_cv_version>): <method>,
        }
    }
    """

    def __init__(self, min_ver: str = "2024.1.0", max_ver: str = CVAAS_VERSION_STRING) -> None:
        """__init__ is called with the arguments of the decorator."""
        # Storing these on the instance so it can be read in the __call__ method.
        self.min_version = CvVersion(min_ver)
        self.max_version = CvVersion(max_ver)

        if self.max_version < self.min_version:
            msg = (
                "Invalid min and max versions passed to 'cv_version' decorator. Min version must be larger than max version. "
                f"Got min_ver '{self.min_version}', max_var '{self.max_version}'."
            )
            raise ValueError(msg)

    def __call__(self, func: Callable) -> Callable:
        """
        Store the method in the map of versioned functions after checking for overlapping decorators for the same method.

        __call__ is called with the method being decorated.
        """
        for existing_min_version, existing_max_version in LimitCvVersion.versioned_funcs.get(func.__name__, []):
            if existing_min_version <= self.max_version and existing_max_version >= self.min_version:
                msg = (
                    "Overlapping min and max versions passed to 'cv_version' decorator."
                    f"{self.min_version}-{self.max_version} overlaps with {existing_min_version}-{existing_max_version}."
                )
                raise ValueError(msg)

        LimitCvVersion.versioned_funcs.setdefault(func.__name__, {})[(self.min_version, self.max_version)] = func

        @wraps(func)
        async def wrapper_cv_version(*args: Any, **kwargs: Any) -> list:
            """
            Call the appropriate original method depending on the _cv_version attribute of 'self'.

            The wrapper is being called by regular method calls with the args and kwargs given by the calling code (including 'self').
            """
            # Extract the version of the connected CloudVision server from the 'self' object passed to the method.
            # Defaulting to 'CVaaS' which means newest versions.
            cv_version: CvVersion = getattr(args[0], "_cv_version", CvVersion("CVaaS"))
            LOGGER.info("wrapper_cv_version: Called '%s' with version '%s'", func.__name__, cv_version)

            for min_max_versions, versioned_func in LimitCvVersion.versioned_funcs[func.__name__].items():
                min_version, max_version = min_max_versions
                if min_version <= cv_version <= max_version:
                    return await versioned_func(*args, **kwargs)

            msg = f"Unsupported version of CloudVision: '{cv_version}'."
            raise LookupError(msg)

        return wrapper_cv_version
