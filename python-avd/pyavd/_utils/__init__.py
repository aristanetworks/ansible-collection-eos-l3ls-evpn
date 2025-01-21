# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from .append_if_not_duplicate import append_if_not_duplicate
from .batch import batch
from .compare_dicts import compare_dicts
from .default import default
from .format_string import AvdStringFormatter
from .get import get, get_v2
from .get_all import get_all, get_all_with_path
from .get_indices_of_duplicate_items import get_indices_of_duplicate_items
from .get_ip_from_ip_prefix import get_ip_from_ip_prefix
from .get_ip_from_pool import get_ip_from_pool
from .get_item import get_item
from .groupby import groupby, groupby_obj
from .load_python_class import load_python_class
from .merge import merge
from .replace_or_append_item import replace_or_append_item
from .short_esi_to_route_target import short_esi_to_route_target
from .strip_empties import strip_empties_from_dict, strip_empties_from_list, strip_null_from_data
from .template import template
from .template_var import template_var
from .undefined import Undefined, UndefinedType
from .unique import unique

__all__ = [
    "AvdStringFormatter",
    "Undefined",
    "UndefinedType",
    "append_if_not_duplicate",
    "batch",
    "compare_dicts",
    "default",
    "get",
    "get_all",
    "get_all_with_path",
    "get_indices_of_duplicate_items",
    "get_ip_from_ip_prefix",
    "get_ip_from_pool",
    "get_item",
    "get_v2",
    "groupby",
    "groupby_obj",
    "load_python_class",
    "merge",
    "replace_or_append_item",
    "short_esi_to_route_target",
    "strip_empties_from_dict",
    "strip_empties_from_list",
    "strip_null_from_data",
    "template",
    "template_var",
    "unique",
]
