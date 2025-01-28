# Copyright (c) 2023-2025 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the LICENSE file.
from __future__ import annotations

from pyavd._eos_designs.structured_config.structured_config_generator import StructuredConfigGenerator

CUSTOM_STRUCTURED_CONFIGURATION_EXEMPT_KEYS = ["custom_structured_configuration_prefix", "custom_structured_configuration_list_merge"]


class AvdStructuredConfigCustomStructuredConfiguration(StructuredConfigGenerator):
    """
    The AvdStructuredConfig Class is imported by "get_structured_config" to render parts of the structured config.

    "get_structured_config" imports, instantiates and run the .render() method on the class.

    The Class uses StructuredConfigGenerator, as the base class, to inherit _hostvars other attributes.
    """

    ignore_avd_eos_designs_enforce_duplication_checks_across_all_models = True

    def render(self) -> None:
        """
        Custom Structured Configuration can contain any key, so we cannot use the regular render method.

        This method merges each custom structured config on top of self.structured_config.

        First strip all (None, {}, []) from regular structured_config. This is to avoid empty objects showing up in the output dict.
        Next we merge in custom structured config from various sources including None, {}, [].
        """
        # Strip empties from regular structured config
        self.structured_config._strip_empties()

        # Apply structured_config from node config
        if struct_cfg := self.shared_utils.node_config.structured_config:
            self.structured_config._deepmerge(struct_cfg, list_merge=self.custom_structured_configs.list_merge_strategy)

        # Apply structured configs from root.
        [
            self.structured_config._deepmerge(struct_cfg, list_merge=self.custom_structured_configs.list_merge_strategy)
            for struct_cfg in self.custom_structured_configs.root
        ]

        # Apply structured configs from "nested" meaning structured config for smaller objects like ethernet_interfaces, peer-groups etc.
        self.structured_config._deepmerge(self.custom_structured_configs.nested, list_merge=self.custom_structured_configs.list_merge_strategy)

        # Apply custom_structured_configuration
        [
            self.structured_config._deepmerge(custom_structured_configuration.value, list_merge=self.custom_structured_configs.list_merge_strategy)
            for custom_structured_configuration in self.inputs._custom_structured_configurations
        ]
