# Copyright (c) 2024-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from collections import ChainMap

from pyavd._utils import get


def get_instance_with_defaults(instance: dict, dynamic_key_path: str, schema: dict) -> dict | ChainMap:
    """
    Returns the instance including any default value of the given dynamic key path.

    If the dynamic key path is already in the instance, the instance is returned as-is.
    """
    dynamic_root_key = dynamic_key_path.split(".", maxsplit=1)[0]

    if dynamic_root_key in instance:
        # The key is already set, so no need to find the default value.
        return instance

    if dynamic_root_key == "node_type_keys":
        # TODO: AVD6.0.0 remove this if block when we remove the reliance on design.type.
        from pyavd._eos_designs.shared_utils.node_type_keys import DEFAULT_NODE_TYPE_KEYS

        design_type = get(instance, "design.type", default="l3ls-evpn")
        return ChainMap(instance, {"node_type_keys": DEFAULT_NODE_TYPE_KEYS[design_type]})

    # Fetch default value from schema
    return ChainMap(instance, {dynamic_root_key: get(schema, f"keys.{dynamic_root_key}.default")})
