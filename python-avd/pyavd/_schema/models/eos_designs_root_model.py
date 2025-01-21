# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from collections import ChainMap
from collections.abc import Iterator, Mapping
from typing import TYPE_CHECKING

from pyavd._eos_cli_config_gen.schema import EosCliConfigGen
from pyavd._schema.store import create_store
from pyavd._schema.utils import get_instance_with_defaults
from pyavd._utils import get_all

from .avd_list import AvdList
from .avd_model import AvdModel

if TYPE_CHECKING:
    from pyavd._eos_designs.schema import EosDesigns

SKIP_KEYS = ["custom_structured_configuration_list_merge", "custom_structured_configuration_prefix"]


class EosDesignsRootModel(AvdModel):
    @classmethod
    def _from_dict(cls: type[EosDesigns], data: Mapping, keep_extra_keys: bool = False, load_custom_structured_config: bool = True) -> EosDesigns:
        """
        Returns a new instance loaded with the data from the given dict.

        The EosDesignsRootModel is special because it will also load "dynamic keys" like `node_type_keys` and `network_services_keys` and
        `connected_endpoints_keys`. Those models will be parsed and all mentioned keys will be searched for in the input and loaded into the
        corresponding model under `_dynamic_keys`.

        Furthermore the EosDesignsRootModel will also load `custom_structured_configuration_prefix` and search for any keys prefixed with those. Found keys
        will be loaded into the `_custom_structured_configurations` model.

        Args:
            data: A mapping containing the EosDesigns input data to be loaded.
            keep_extra_keys: Store all unknown keys in the _custom_data dict and include it again in the output of _to_dict().
                By default only keys starting with _ will be stored in _custom_data. This will change the behavior to store _all_ keys.
            load_custom_structured_config: Some custom structured config contains inline Jinja templates relying on variables produced by EosDesignsFacts.
                To avoid such templates breaking the type checks, we can skip loading custom_structured_configuration during the facts phase by setting this
                to False.

        TODO: AVD6.0.0 remove the keep_extra_keys option so we no longer support custom keys without _ in structured config
        """
        if not isinstance(data, Mapping):
            msg = f"Expecting 'data' as a 'Mapping' when loading data into '{cls.__name__}'. Got '{type(data)}"
            raise TypeError(msg)

        root_data = {"_dynamic_keys": cls._get_dynamic_keys(data)}
        if load_custom_structured_config:
            root_data["_custom_structured_configurations"] = cls._CustomStructuredConfigurations(cls._get_csc_items(data))

        return super()._from_dict(ChainMap(root_data, data), keep_extra_keys=keep_extra_keys)

    @classmethod
    def _get_csc_items(cls: type[EosDesigns], data: Mapping) -> Iterator[EosDesigns._CustomStructuredConfigurationsItem]:
        """
        Returns a list of _CustomStructuredConfigurationsItem objects containing each custom structured configuration extracted from the inputs.

        Find any keys starting with any prefix defined under "custom_structured_configuration_prefix".
        """
        prefixes = data.get("custom_structured_configuration_prefix", cls._get_field_default_value("custom_structured_configuration_prefix"))
        if not isinstance(prefixes, (list, AvdList)):
            # Invalid prefix format.
            return

        for prefix in prefixes:
            if not isinstance(prefix, str):
                # Invalid prefix format.
                continue

            if not (matching_keys := [key for key in data if str(key).startswith(prefix) and key not in SKIP_KEYS]):
                continue

            prefix_length = len(prefix)
            for key in matching_keys:
                yield cls._CustomStructuredConfigurationsItem(key=key, value=EosCliConfigGen._from_dict({key[prefix_length:]: data[key]}))

    @classmethod
    def _get_dynamic_keys(cls: type[EosDesigns], data: Mapping) -> EosDesigns._DynamicKeys:
        """
        Returns the DynamicKeys object which holds a list for each dynamic key.

        The lists contain an entry for each dynamic key found in the inputs and the content of that key conforming to the schema.

        The corresponding data models are auto created by the conversion from schemas, which also sets "_dynamic_key_maps" on the class:
        ```python
        _dynamic_key_maps: list[dict] = [{"dynamic_keys_path": "connected_endpoints_keys.key", "model_key": "connected_endpoints_keys"}, ...]
        ```

        Here we parse "_dynamic_key_maps" and for entry  find all values for the dynamic_keys_path (ex "node_type_keys.key") in the input data
        to identify all dynamic keys (ex "l3leaf", "spine" ...)
        """
        schema = create_store(load_from_yaml=False)["eos_designs"]

        dynamic_keys_dict = {}

        for dynamic_key_map in cls._DynamicKeys._dynamic_key_maps:
            dynamic_keys_path: str = dynamic_key_map["dynamic_keys_path"]
            model_key_list: list = dynamic_keys_dict.setdefault(dynamic_key_map["model_key"], [])

            # TODO: Improve the fetch of default. We need to store the default value somewhere, since this is executed before __init__ of EosDesigns.
            data_with_default = get_instance_with_defaults(data, dynamic_keys_path, schema)
            dynamic_keys = get_all(data_with_default, dynamic_keys_path)
            for dynamic_key in dynamic_keys:
                # dynamic_key is one key like "l3leaf".
                if (value := data.get(dynamic_key)) is None:
                    # Do not add missing key or None.
                    continue

                model_key_list.append({"key": dynamic_key, "value": value})

        # TODO: Just create to proper data models instead of using coerce type.
        return cls._DynamicKeys._from_dict(dynamic_keys_dict)
